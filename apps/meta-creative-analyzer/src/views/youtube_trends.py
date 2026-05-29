"""Marketing Keyword Gap → Shoot Brief view with Live / Sample / Compare modes."""

from __future__ import annotations

from datetime import timedelta

import pandas as pd
import streamlit as st

from bootstrap import get_secret, inject_streamlit_secrets, mask_secret, secrets_status
from youtube_client import MARKETING_KEYWORD_PRESETS, YouTubeClient, load_sample_trending_dataframe
from youtube_live import compare_live_sample, now_kst_label, top_trending_titles
from youtube_recommend import brief_to_markdown, build_shoot_brief
from youtube_transform import enrich_youtube_dataframe, overview_metrics


def _refresh_token() -> int:
    return int(st.session_state.get("yt_refresh_token", 0))


def _bump_refresh() -> None:
    st.session_state["yt_refresh_token"] = _refresh_token() + 1
    load_trending.clear()
    load_keyword.clear()


@st.cache_data(ttl=300, show_spinner="KR 트렌딩 baseline 불러오는 중…")
def load_trending(use_api: bool, _refresh: int = 0) -> tuple[pd.DataFrame, str, str]:
    fetched_at = now_kst_label()
    client = YouTubeClient()
    if use_api and client.is_configured:
        df = client.load_trending_dataframe(max_results=50)
        source = f"🟢 Live · KR baseline · {fetched_at}"
    else:
        df = load_sample_trending_dataframe()
        source = f"Sample baseline · {fetched_at}"
    return enrich_youtube_dataframe(df), source, fetched_at


@st.cache_data(ttl=300, show_spinner="키워드 검색 중… (약 100 quota units)")
def load_keyword(keyword: str, use_api: bool, _refresh: int = 0) -> pd.DataFrame:
    if not keyword.strip():
        return pd.DataFrame()

    client = YouTubeClient()
    if use_api and client.is_configured:
        df = client.load_keyword_dataframe(keyword.strip(), max_results=25)
        return enrich_youtube_dataframe(df)

    sample = load_sample_trending_dataframe()
    enriched = enrich_youtube_dataframe(sample)
    token = keyword.split()[0]
    mask = enriched["title"].str.contains(token, case=False, na=False)
    filtered = enriched[mask].head(12)
    if filtered.empty:
        filtered = enriched.sample(min(8, len(enriched)), random_state=hash(keyword) % 2**32)
    filtered = filtered.copy()
    filtered["source_keyword"] = keyword
    return filtered


def _render_live_ticker(df: pd.DataFrame, label: str) -> None:
    st.markdown(f"**{label} — 인기 TOP 5**")
    for i, item in enumerate(top_trending_titles(df, 5), 1):
        st.markdown(
            f"{i}. **{item['title'][:60]}{'…' if len(item['title']) > 60 else ''}**  \n"
            f"   조회수 {item['views']:,} · engagement {item['engagement']:.2f}% · {item['format']}"
        )


def _render_shoot_brief(shoot: dict, keyword: str) -> None:
    st.success(f"**{shoot['this_week_action']}**")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"**포맷:** {shoot['format']} · {shoot['duration']}")
        st.caption(shoot["format_rationale"])
        st.markdown(f"**훅:** {shoot['title_hook']}")
        for i, title in enumerate(shoot["title_examples"], 1):
            st.markdown(f"{i}. 「{title}」")
    with c2:
        st.markdown("**태그:** " + " · ".join(f"`{t}`" for t in shoot["test_tags"]))
        st.caption(shoot["headline"])


def _render_compare(keyword: str, live_t: pd.DataFrame, sample_t: pd.DataFrame, live_k: pd.DataFrame, sample_k: pd.DataFrame) -> tuple[dict, dict]:
    cmp = compare_live_sample(keyword, live_t, sample_t, live_k, sample_k)
    st.markdown("### Live vs Sample — 실시간 vs 데모 데이터")
    st.caption(f"마지막 Live fetch: {now_kst_label()}")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Live engagement", f"{cmp['live_overview']['avg_engagement']}%")
    m2.metric("Sample engagement", f"{cmp['sample_overview']['avg_engagement']}%")
    m3.metric("Δ engagement", f"{cmp['engagement_delta']:+.2f}%p")
    m4.metric("Δ Shorts %", f"{cmp['shorts_delta']:+.1f}%p")

    col_live, col_sample = st.columns(2)
    with col_live:
        st.markdown("#### 🟢 Live API")
        ls = cmp["live_shoot"]
        st.metric("판정", ls["verdict_label"])
        st.metric("Engagement gap", f"{ls['gap']['engagement_gap']:+.2f}%p")
        _render_shoot_brief(ls, keyword)
    with col_sample:
        st.markdown("#### Sample (데모)")
        ss = cmp["sample_shoot"]
        st.metric("판정", ss["verdict_label"])
        st.metric("Engagement gap", f"{ss['gap']['engagement_gap']:+.2f}%p")
        _render_shoot_brief(ss, keyword)

    if cmp["verdict_changed"]:
        st.warning(
            f"판정 차이: Live **{cmp['live_shoot']['verdict_label']}** vs "
            f"Sample **{cmp['sample_shoot']['verdict_label']}** — Live 기준으로 기획하세요."
        )
    return cmp["live_shoot"], cmp["sample_shoot"]


@st.fragment(run_every=timedelta(minutes=5))
def _auto_refresh_fragment(has_api: bool, compare_mode: bool) -> None:
    if not has_api or not st.session_state.get("yt_auto_refresh", False):
        return
    _bump_refresh()
    st.toast(f"Live 데이터 자동 갱신 · {now_kst_label()}", icon="🔄")


def render() -> None:
    inject_streamlit_secrets()

    st.title("Marketing Keyword Gap → Shoot Brief")
    st.caption(
        "KR 대중 트렌드 vs **내 마케팅 키워드** — Live API · Sample · **나란히 비교**"
    )

    has_youtube_key = secrets_status()["youtube"]
    refresh = _refresh_token()

    with st.sidebar:
        st.header("Settings")

        mode_options = ["Sample (데모)", "YouTube Live API"]
        if has_youtube_key:
            mode_options.append("Live + Sample 비교")

        default_index = 1 if has_youtube_key else 0
        data_mode = st.radio("데이터 모드", mode_options, index=min(default_index, len(mode_options) - 1))

        compare_mode = data_mode == "Live + Sample 비교"
        use_api = data_mode in ("YouTube Live API", "Live + Sample 비교")

        if use_api and not has_youtube_key:
            st.warning("API Key 필요")
            manual_key = st.text_input("API Key (이번 세션)", type="password", key="yt_api_key_input")
            if manual_key.strip():
                st.session_state["yt_api_key_override"] = manual_key.strip()
                has_youtube_key = True
                st.success(f"Key: {mask_secret(manual_key.strip())}")
        elif has_youtube_key:
            st.success(f"API Key: {mask_secret(get_secret('YOUTUBE_API_KEY'))}")

        if has_youtube_key and use_api:
            if st.button("🔄 Live 데이터 새로고침", use_container_width=True):
                _bump_refresh()
                st.rerun()
            st.session_state["yt_auto_refresh"] = st.checkbox("자동 새로고침 (5분)", value=False)

        st.caption("Region: KR · Live cache 5분")
        st.warning("키워드 검색 1회 ≈ 100 quota units")

        effective_api = use_api and has_youtube_key
        if compare_mode and effective_api:
            live_t, live_src, _ = load_trending(True, refresh)
            sample_t, sample_src, _ = load_trending(False, refresh)
            st.success(live_src)
            st.info(sample_src)
            trending_df = live_t
            source = live_src
        else:
            trending_df, source, fetched_at = load_trending(effective_api, refresh)
            sample_t = None
            if effective_api:
                st.success(source)
            else:
                st.info(source)

    if has_youtube_key and use_api:
        _auto_refresh_fragment(has_youtube_key, compare_mode)

    if effective_api and not compare_mode:
        with st.expander("🟢 Live KR 트렌딩 NOW", expanded=True):
            _render_live_ticker(trending_df, "실시간")

    st.markdown("### ① 내 마케팅 키워드")
    col_kw, col_custom = st.columns([2, 2])
    with col_kw:
        preset = st.selectbox("마케팅 vertical 프리셋", MARKETING_KEYWORD_PRESETS, index=0)
    with col_custom:
        custom = st.text_input("또는 직접 입력", placeholder="예: 퍼포먼스 마케팅, CRM")

    primary_keyword = custom.strip() or preset

    if compare_mode and effective_api and sample_t is not None:
        live_k = load_keyword(primary_keyword, True, refresh)
        sample_k = load_keyword(primary_keyword, False, refresh)
        shoot, _ = _render_compare(primary_keyword, trending_df, sample_t, live_k, sample_k)
        keyword_df = live_k
        md = brief_to_markdown({"shoot_brief": shoot})
        st.download_button(
            "Live Shoot Brief Markdown",
            md,
            f"shoot_brief_live_{primary_keyword.replace(' ', '_')}.md",
            "text/markdown",
        )
    else:
        keyword_df = load_keyword(primary_keyword, effective_api, refresh)
        shoot = build_shoot_brief(primary_keyword, trending_df, keyword_df)

        st.divider()
        st.markdown("### ② Gap Report")
        gap = shoot["gap"]
        g1, g2, g3, g4, g5 = st.columns(5)
        g1.metric("키워드", primary_keyword)
        g2.metric("검색 결과", gap["keyword_count"])
        g3.metric("Engagement gap", f"{gap['engagement_gap']:+.2f}%p")
        g4.metric("Overlap", f"{gap['category_overlap_pct']:.0f}%")
        g5.metric("판정", shoot["verdict_label"])
        st.info(f"**{shoot['verdict_label']}** — {shoot['verdict_detail']}")

        st.divider()
        st.markdown("### ③ Shoot Brief")
        _render_shoot_brief(shoot, primary_keyword)

        md = brief_to_markdown({"shoot_brief": shoot})
        st.download_button(
            "Shoot Brief Markdown",
            md,
            f"shoot_brief_{primary_keyword.replace(' ', '_')}.md",
            "text/markdown",
        )

    st.divider()
    with st.expander("상세 데이터"):
        if compare_mode and effective_api and sample_t is not None:
            t1, t2 = st.tabs(["Live Baseline", "Sample Baseline"])
            with t1:
                st.dataframe(trending_df[["title", "views", "engagement_rate"]].head(15), hide_index=True)
            with t2:
                st.dataframe(sample_t[["title", "views", "engagement_rate"]].head(15), hide_index=True)
        else:
            st.dataframe(
                trending_df[["title", "category_name", "format_label", "views", "engagement_rate"]].head(20),
                use_container_width=True,
                hide_index=True,
            )
        csv = keyword_df.to_csv(index=False).encode("utf-8-sig") if not keyword_df.empty else trending_df.to_csv(index=False).encode("utf-8-sig")
        st.download_button("CSV 내보내기", csv, "youtube_export.csv", "text/csv")
