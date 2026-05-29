"""Meta Creative Intelligence — Streamlit dashboard."""

from __future__ import annotations

import os
import sys
from pathlib import Path

import pandas as pd
import streamlit as st
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

load_dotenv(ROOT / ".env")

from analyze import aggregate_by_dimension, compare_top_bottom  # noqa: E402
from meta_client import MetaAPIError, MetaClient, load_sample_dataframe  # noqa: E402
from recommend import CTA_LABELS, build_direction_brief  # noqa: E402
from transform import enrich_dataframe, overview_metrics  # noqa: E402

st.set_page_config(
    page_title="Meta Creative Intelligence",
    page_icon="📊",
    layout="wide",
)

st.title("Meta Creative Intelligence")
st.caption("소재 메타데이터 + 성과 지표 → 패턴 분석 → 다음 영상/크리에이티브 방향 제안")

if os.getenv("RAILWAY_ENVIRONMENT"):
    st.sidebar.info("Railway 배포 · Sample mode 기본 · Meta API는 Variables에 토큰 설정 후 토글 ON")


@st.cache_data(ttl=300, show_spinner="Meta API에서 소재·성과 데이터를 불러오는 중…")
def load_data(use_api: bool, date_preset: str, limit: int) -> tuple[pd.DataFrame, str]:
    if use_api:
        client = MetaClient()
        if not client.is_configured:
            raise MetaAPIError("META_ACCESS_TOKEN 또는 META_AD_ACCOUNT_ID가 설정되지 않았습니다.")
        df = client.load_creatives_dataframe(date_preset=date_preset, limit=limit)
        source = f"Meta API · {client.ad_account_id} · {date_preset}"
    else:
        df = load_sample_dataframe()
        source = "Sample data (demo mode)"
    return enrich_dataframe(df), source


with st.sidebar:
    st.header("Settings")
    use_api = st.toggle("Meta API 사용", value=False, help=".env에 토큰·광고계정 ID 필요")
    date_preset = st.selectbox(
        "기간",
        ["last_7d", "last_14d", "last_30d", "last_90d"],
        index=2,
    )
    limit = st.slider("최대 광고 수", 10, 200, 50, step=10)
    metric_sort = st.selectbox("정렬 기준", ["cpa", "ctr", "cvr", "spend"], index=0)

    try:
        df, source = load_data(use_api, date_preset, limit)
        st.success(source)
    except MetaAPIError as exc:
        st.error(str(exc))
        st.info("Sample mode로 전환하거나 .env.example을 참고해 설정하세요.")
        df, source = load_data(False, date_preset, limit)

overview = overview_metrics(df)
tab_overview, tab_explorer, tab_pattern, tab_brief = st.tabs(
    ["Overview", "Creative Explorer", "Pattern Analysis", "Direction Brief"]
)

with tab_overview:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("소재 수", overview["creative_count"])
    c2.metric("평균 CTR", f"{overview['avg_ctr']}%")
    c3.metric("평균 CPA", f"₩{overview['avg_cpa']:,.0f}" if overview["avg_cpa"] else "—")
    c4.metric("총 광고비", f"₩{overview['total_spend']:,}")

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("포맷 비율")
        format_df = pd.DataFrame(
            {
                "format": ["Video", "Image", "Carousel"],
                "pct": [overview["video_pct"], overview["image_pct"], overview["carousel_pct"]],
            }
        )
        st.bar_chart(format_df.set_index("format"))
    with col_b:
        st.subheader("CPA 상위 vs 하위")
        comp = compare_top_bottom(df)
        st.write(
            f"**상위 25%** — CPA ₩{comp.get('top_avg_cpa', 0):,.0f} · "
            f"{comp.get('top_format', '—')} · {comp.get('top_hook', '—')}"
        )
        st.write(
            f"**하위 25%** — CPA ₩{comp.get('bottom_avg_cpa', 0):,.0f} · "
            f"{comp.get('bottom_format', '—')} · {comp.get('bottom_hook', '—')}"
        )

with tab_explorer:
    st.subheader("Creative Explorer")
    format_filter = st.multiselect(
        "포맷 필터",
        sorted(df["format_tag"].unique()),
        default=sorted(df["format_tag"].unique()),
    )
    hook_filter = st.multiselect(
        "훅 필터",
        sorted(df["hook_keyword"].unique()),
        default=sorted(df["hook_keyword"].unique()),
    )

    filtered = df[
        df["format_tag"].isin(format_filter) & df["hook_keyword"].isin(hook_filter)
    ].copy()
    ascending = metric_sort == "cpa"
    if metric_sort in filtered.columns:
        filtered = filtered.sort_values(metric_sort, ascending=ascending, na_position="last")

    display_cols = [
        "ad_name",
        "format_tag",
        "hook_keyword",
        "call_to_action_type",
        "copy_preview",
        "spend",
        "ctr",
        "cpa",
        "cvr",
        "conversions",
    ]
    st.dataframe(
        filtered[display_cols].rename(
            columns={
                "ad_name": "광고명",
                "format_tag": "포맷",
                "hook_keyword": "훅",
                "call_to_action_type": "CTA",
                "copy_preview": "카피 미리보기",
                "spend": "비용",
                "ctr": "CTR(%)",
                "cpa": "CPA",
                "cvr": "CVR(%)",
                "conversions": "전환",
            }
        ),
        use_container_width=True,
        hide_index=True,
    )

with tab_pattern:
    st.subheader("Pattern Analysis")
    dim = st.radio("분석 차원", ["format_tag", "hook_keyword", "call_to_action_type"], horizontal=True)
    stats = aggregate_by_dimension(df, dim)
    if not stats.empty:
        label_col = dim
        chart_df = stats.set_index(label_col)[["avg_cpa"]]
        st.bar_chart(chart_df)
        stats_display = stats.copy()
        if dim == "call_to_action_type":
            stats_display[dim] = stats_display[dim].map(lambda x: CTA_LABELS.get(x, x))
        st.dataframe(stats_display, use_container_width=True, hide_index=True)
    else:
        st.warning("분석 가능한 CPA 데이터가 없습니다.")

with tab_brief:
    st.subheader("Direction Brief")
    brief = build_direction_brief(df)
    st.info(brief["summary"])

    st.markdown("### 추천 방향")
    for item in brief["recommendations"]:
        st.markdown(f"- {item}")

    st.markdown("### 다음 테스트 제안")
    for idea in brief["next_tests"]:
        st.markdown(f"- {idea}")

    with st.expander("상세 비교 데이터"):
        st.json(brief["comparison"])

    csv = df.to_csv(index=False).encode("utf-8-sig")
    st.download_button("CSV 내보내기", csv, "meta_creatives_export.csv", "text/csv")
