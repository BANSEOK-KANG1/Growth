"""Marketing Keyword Gap → Shoot Brief (YouTube KR)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from datetime import datetime, timezone

import pandas as pd
import streamlit as st

from bootstrap import inject_streamlit_secrets, is_streamlit_cloud, secrets_status
from youtube_analyze import aggregate_by_dimension, category_mix, format_comparison
from youtube_client import (
    MARKETING_KEYWORD_PRESETS,
    YouTubeAPIError,
    YouTubeClient,
    load_sample_trending_dataframe,
)
from youtube_recommend import brief_to_markdown, build_shoot_brief
from youtube_transform import enrich_youtube_dataframe, overview_metrics

inject_streamlit_secrets()

st.set_page_config(
    page_title="Keyword Gap → Shoot Brief",
    page_icon="🎬",
    layout="wide",
)

st.title("Marketing Keyword Gap → Shoot Brief")
st.caption(
    "KR 대중 트렌드(K-pop·먹방 noise) vs **내 마케팅 키워드** — gap 분석 후 **이번 주 찍을 영상 1편** 브리프"
)

if is_streamlit_cloud():
    st.sidebar.info("YouTube API Key → Secrets · 키워드 1개 입력 → Shoot Brief 1장")

has_youtube_key = secrets_status()["youtube"]


@st.cache_data(ttl=3600, show_spinner="KR 트렌딩 baseline 불러오는 중…")
def load_trending(use_api: bool) -> tuple[pd.DataFrame, str]:
    if use_api:
        client = YouTubeClient()
        if not client.is_configured:
            raise YouTubeAPIError("YOUTUBE_API_KEY가 설정되지 않았습니다.")
        df = client.load_trending_dataframe(max_results=50)
        source = f"YouTube API · KR baseline · {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}"
    else:
        df = load_sample_trending_dataframe()
        source = "Sample baseline (demo)"
    return enrich_youtube_dataframe(df), source


@st.cache_data(ttl=1800, show_spinner="키워드 검색 중… (약 100 quota units)")
def load_keyword(keyword: str, use_api: bool) -> pd.DataFrame:
    if not keyword.strip():
        return pd.DataFrame()
    if use_api:
        client = YouTubeClient()
        df = client.load_keyword_dataframe(keyword.strip(), max_results=25)
        return enrich_youtube_dataframe(df)
    sample = load_sample_trending_dataframe()
    enriched = enrich_youtube_dataframe(sample)
    mask = enriched["title"].str.contains(keyword.split()[0], case=False, na=False)
    filtered = enriched[mask].head(12)
    if filtered.empty:
        filtered = enriched.sample(min(8, len(enriched)), random_state=hash(keyword) % 2**32)
    filtered = filtered.copy()
    filtered["source_keyword"] = keyword
    return filtered


with st.sidebar:
    st.header("Settings")
    use_api = st.toggle("YouTube API 사용", value=has_youtube_key)
    st.caption("Region: KR")
    st.warning("키워드 검색 1회 ≈ 100 quota units")

    try:
        trending_df, source = load_trending(use_api)
        st.success(source)
    except YouTubeAPIError as exc:
        st.error(str(exc))
        trending_df, source = load_trending(False)

# ── Step 1: Keyword ──────────────────────────────────────────────
st.markdown("### ① 내 마케팅 키워드")
st.markdown("광고·유튜브·UGC 기획 전 — **내 상품/주제**로 검색했을 때 대중 트렌드와 얼마나 다른지 봅니다.")

col_kw, col_custom = st.columns([2, 2])
with col_kw:
    preset = st.selectbox(
        "마케팅 vertical 프리셋",
        MARKETING_KEYWORD_PRESETS,
        index=MARKETING_KEYWORD_PRESETS.index("SaaS") if "SaaS" in MARKETING_KEYWORD_PRESETS else 0,
    )
with col_custom:
    custom = st.text_input("또는 직접 입력", placeholder="예: 퍼포먼스 마케팅, CRM")

primary_keyword = custom.strip() or preset
keyword_df = load_keyword(primary_keyword, use_api)
shoot = build_shoot_brief(primary_keyword, trending_df, keyword_df)

st.divider()

# ── Step 2: Gap Report ───────────────────────────────────────────
st.markdown("### ② Gap Report — 트렌딩 vs 내 키워드")
gap = shoot["gap"]

g1, g2, g3, g4, g5 = st.columns(5)
g1.metric("내 키워드", primary_keyword)
g2.metric("검색 결과", gap["keyword_count"])
g3.metric("Engagement gap", f"{gap['engagement_gap']:+.2f}%p", help="키워드 vs KR 트렌딩 평균")
g4.metric("Category overlap", f"{gap['category_overlap_pct']:.0f}%", help="낮을수록 블루오션")
g5.metric("판정", shoot["verdict_label"])

st.info(f"**{shoot['verdict_label']}** — {shoot['verdict_detail']}")

if gap.get("unique_keyword_hashtags"):
    st.caption(f"키워드 고유 태그: {', '.join(gap['unique_keyword_hashtags'][:5])}")
if gap.get("unique_trending_hashtags"):
    st.caption(f"트렌딩만 있는 태그 (피하기): {', '.join(gap['unique_trending_hashtags'][:5])}")

st.divider()

# ── Step 3: Shoot Brief ──────────────────────────────────────────
st.markdown("### ③ Shoot Brief — 이번 주 찍을 1편")

st.success(f"**{shoot['this_week_action']}**")

brief_col1, brief_col2 = st.columns(2)

with brief_col1:
    st.markdown("#### 포맷")
    st.markdown(f"**{shoot['format']}** · {shoot['duration']}")
    st.caption(shoot["format_rationale"])

    st.markdown("#### 제목 훅")
    st.markdown(f"**{shoot['title_hook']}**")
    for i, title in enumerate(shoot["title_examples"], 1):
        st.markdown(f"{i}. 「{title}」")

with brief_col2:
    st.markdown("#### 테스트 태그")
    st.markdown(" · ".join(f"`{t}`" for t in shoot["test_tags"]))

    st.markdown("#### Gap 한 줄")
    st.markdown(shoot["headline"])

    md = brief_to_markdown({"shoot_brief": shoot})
    st.download_button(
        "Shoot Brief Markdown",
        md,
        f"shoot_brief_{primary_keyword.replace(' ', '_')}.md",
        "text/markdown",
        use_container_width=True,
    )

st.divider()

# ── Detail data (collapsed) ──────────────────────────────────────
with st.expander("상세 데이터 — KR 트렌딩 baseline · 키워드 검색 결과 · 패턴"):
    tab_base, tab_kw, tab_pat = st.tabs(["KR Baseline", "키워드 검색 결과", "패턴"])

    with tab_base:
        ov = overview_metrics(trending_df)
        b1, b2, b3, b4 = st.columns(4)
        b1.metric("Baseline 영상", ov["video_count"])
        b2.metric("평균 engagement", f"{ov['avg_engagement']}%")
        b3.metric("Shorts %", f"{ov['shorts_pct']}%")
        b4.metric("Dominant cat.", ov["dominant_category"])
        mix = category_mix(trending_df)
        if not mix.empty:
            st.bar_chart(mix.set_index("category_name")[["share_pct"]])
        fmt = format_comparison(trending_df)
        st.caption(
            f"Shorts {fmt['shorts_engagement']}% vs Long {fmt['long_engagement']}% "
            f"(gap {fmt['engagement_gap']:+.3f}%p)"
        )
        st.dataframe(
            trending_df[
                ["title", "category_name", "format_label", "views", "engagement_rate"]
            ].head(20),
            use_container_width=True,
            hide_index=True,
        )

    with tab_kw:
        if keyword_df.empty:
            st.warning("키워드 검색 결과 없음")
        else:
            st.dataframe(
                keyword_df[
                    ["title", "channel_title", "format_label", "title_hook", "views", "engagement_rate"]
                ],
                use_container_width=True,
                hide_index=True,
            )

    with tab_pat:
        dim = st.radio(
            "차원",
            ["title_hook", "format_label", "category_name"],
            horizontal=True,
            format_func=lambda x: {"title_hook": "제목 훅", "format_label": "포맷", "category_name": "카테고리"}[x],
        )
        stats = aggregate_by_dimension(trending_df, dim)
        if not stats.empty:
            st.bar_chart(stats.set_index(dim)[["avg_engagement"]])

    csv = keyword_df.to_csv(index=False).encode("utf-8-sig") if not keyword_df.empty else trending_df.to_csv(index=False).encode("utf-8-sig")
    st.download_button("CSV 내보내기", csv, "youtube_gap_export.csv", "text/csv")
