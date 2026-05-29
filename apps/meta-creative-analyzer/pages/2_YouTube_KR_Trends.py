"""YouTube KR Trends — Streamlit page."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from datetime import datetime, timezone

import pandas as pd
import streamlit as st

from bootstrap import inject_streamlit_secrets, is_streamlit_cloud, secrets_status
from youtube_analyze import (
    aggregate_by_dimension,
    category_mix,
    compare_top_bottom,
    format_comparison,
    keyword_vs_trending,
)
from youtube_client import (
    MARKETING_KEYWORD_PRESETS,
    YouTubeAPIError,
    YouTubeClient,
    load_sample_trending_dataframe,
)
from youtube_recommend import brief_to_markdown, build_content_brief
from youtube_transform import enrich_youtube_dataframe, overview_metrics

inject_streamlit_secrets()

st.set_page_config(
    page_title="YouTube KR Trends",
    page_icon="▶️",
    layout="wide",
)

st.title("YouTube KR Trends")
st.caption("KR 트렌딩 + 마케팅 vertical 키워드 → 패턴 분석 → Content Brief")

if is_streamlit_cloud():
    st.sidebar.info("YouTube API Key를 Secrets에 설정하면 실 KR 트렌딩 데이터를 사용합니다.")

has_youtube_key = secrets_status()["youtube"]


@st.cache_data(ttl=3600, show_spinner="KR 트렌딩 영상을 불러오는 중…")
def load_trending(use_api: bool) -> tuple[pd.DataFrame, str]:
    if use_api:
        client = YouTubeClient()
        if not client.is_configured:
            raise YouTubeAPIError("YOUTUBE_API_KEY가 설정되지 않았습니다.")
        df = client.load_trending_dataframe(max_results=50)
        source = f"YouTube API · KR trending · {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}"
    else:
        df = load_sample_trending_dataframe()
        source = "Sample data (demo mode)"
    return enrich_youtube_dataframe(df), source


@st.cache_data(ttl=1800, show_spinner="키워드 검색 중… (100 quota units)")
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
    default_api = has_youtube_key
    use_api = st.toggle("YouTube API 사용", value=default_api, help="Google Cloud API Key 필요")
    st.caption("Region: KR (고정)")
    st.warning("키워드 검색 1회 = 약 100 quota units")

    keyword_presets = st.multiselect(
        "마케팅 키워드 프리셋",
        MARKETING_KEYWORD_PRESETS,
        default=["SaaS", "AI 마케팅"],
    )
    custom_keyword = st.text_input("Custom keyword", placeholder="예: 퍼포먼스 마케팅")

    active_keywords = list(keyword_presets)
    if custom_keyword.strip() and custom_keyword.strip() not in active_keywords:
        active_keywords.append(custom_keyword.strip())

    sort_metric = st.selectbox(
        "정렬 기준",
        ["engagement_rate", "views", "hours_since_publish"],
        format_func=lambda x: {"engagement_rate": "Engagement", "views": "조회수", "hours_since_publish": "최신순"}[x],
    )

    try:
        trending_df, source = load_trending(use_api)
        st.success(source)
    except YouTubeAPIError as exc:
        st.error(str(exc))
        trending_df, source = load_trending(False)

overview = overview_metrics(trending_df)
fmt_stats = format_comparison(trending_df)

tab_overview, tab_explorer, tab_keyword, tab_brief = st.tabs(
    ["Overview", "Trending Explorer", "Keyword & Pattern", "Content Brief"]
)

with tab_overview:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("영상 수", overview["video_count"])
    c2.metric("평균 조회수", f"{overview['avg_views']:,}")
    c3.metric("평균 Engagement", f"{overview['avg_engagement']}%")
    c4.metric("Shorts 비율", f"{overview['shorts_pct']}%")

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("카테고리 Mix")
        mix = category_mix(trending_df)
        if not mix.empty:
            chart_df = mix.set_index("category_name")[["share_pct"]]
            st.bar_chart(chart_df)
        else:
            st.info("카테고리 데이터 없음")

    with col_b:
        st.subheader("Shorts vs Long-form")
        st.write(
            f"**Shorts** — engagement {fmt_stats['shorts_engagement']}% · "
            f"비중 {fmt_stats['shorts_pct']}%"
        )
        st.write(
            f"**Long-form** — engagement {fmt_stats['long_engagement']}% · "
            f"gap {fmt_stats['engagement_gap']:+.3f}%p"
        )
        comp = compare_top_bottom(trending_df)
        st.write(
            f"**Engagement 상위 25%** — {comp.get('top_format', '—')} · "
            f"{comp.get('top_hook', '—')} · {comp.get('top_category', '—')}"
        )

with tab_explorer:
    st.subheader("Trending Explorer")
    categories = sorted(trending_df["category_name"].unique())
    cat_filter = st.multiselect("카테고리", categories, default=categories)
    shorts_only = st.checkbox("Shorts만", value=False)
    min_views = st.number_input("최소 조회수", min_value=0, value=0, step=10000)

    filtered = trending_df[trending_df["category_name"].isin(cat_filter)].copy()
    if shorts_only:
        filtered = filtered[filtered["is_shorts"]]
    if min_views > 0:
        filtered = filtered[filtered["views"] >= min_views]

    ascending = sort_metric == "hours_since_publish"
    if sort_metric in filtered.columns:
        filtered = filtered.sort_values(sort_metric, ascending=ascending, na_position="last")

    display = filtered[
        [
            "title",
            "channel_title",
            "category_name",
            "format_label",
            "title_hook",
            "views",
            "engagement_rate",
            "hours_since_publish",
        ]
    ].rename(
        columns={
            "title": "제목",
            "channel_title": "채널",
            "category_name": "카테고리",
            "format_label": "포맷",
            "title_hook": "제목 훅",
            "views": "조회수",
            "engagement_rate": "Engagement(%)",
            "hours_since_publish": "업로드 후(h)",
        }
    )
    st.dataframe(display, use_container_width=True, hide_index=True)

with tab_keyword:
    st.subheader("Keyword & Pattern")

    if not active_keywords:
        st.info("사이드바에서 마케팅 키워드 프리셋 또는 Custom keyword를 선택하세요.")
    else:
        keyword_comparisons: list[dict] = []
        for kw in active_keywords[:3]:
            kw_df = load_keyword(kw, use_api)
            comparison = keyword_vs_trending(trending_df, kw_df, kw)
            keyword_comparisons.append(comparison)

            st.markdown(f"#### '{kw}' vs KR Trending")
            k1, k2, k3, k4 = st.columns(4)
            k1.metric("검색 결과", comparison["keyword_count"])
            k2.metric("Engagement gap", f"{comparison['engagement_gap']:+.3f}%p")
            k3.metric("Shorts share gap", f"{comparison['shorts_share_gap']:+.1f}%p")
            k4.metric("Category overlap", f"{comparison['category_overlap_pct']}%")

            if comparison.get("unique_keyword_hashtags"):
                st.caption(
                    f"키워드 고유 태그: {', '.join(comparison['unique_keyword_hashtags'][:5])}"
                )

        st.session_state["keyword_comparisons"] = keyword_comparisons

    st.markdown("---")
    st.subheader("Pattern by Dimension")
    dim = st.radio(
        "분석 차원",
        ["category_name", "format_label", "title_hook"],
        horizontal=True,
        format_func=lambda x: {"category_name": "카테고리", "format_label": "포맷", "title_hook": "제목 훅"}[x],
    )
    stats = aggregate_by_dimension(trending_df, dim)
    if not stats.empty:
        st.bar_chart(stats.set_index(dim)[["avg_engagement"]])
        st.dataframe(stats, use_container_width=True, hide_index=True)

with tab_brief:
    st.subheader("Content Brief")
    kw_comparisons = st.session_state.get("keyword_comparisons", [])
    if not kw_comparisons and active_keywords:
        kw_comparisons = [
            keyword_vs_trending(trending_df, load_keyword(kw, use_api), kw)
            for kw in active_keywords[:2]
        ]

    brief = build_content_brief(trending_df, kw_comparisons)
    st.info(brief["summary"])

    st.markdown("### 추천 방향")
    for item in brief["recommendations"]:
        st.markdown(f"- {item}")

    st.markdown("### 다음 콘텐츠 테스트")
    for idea in brief["next_tests"]:
        st.markdown(f"- {idea}")

    with st.expander("상세 비교 데이터"):
        st.json({"comparison": brief["comparison"], "format": brief["format_comparison"]})

    md = brief_to_markdown(brief)
    st.download_button("Markdown 내보내기", md, "youtube_content_brief.md", "text/markdown")
    csv = trending_df.to_csv(index=False).encode("utf-8-sig")
    st.download_button("CSV 내보내기", csv, "youtube_trending_export.csv", "text/csv")
