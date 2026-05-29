"""Growth Analytics Hub — Meta Creative + YouTube KR Trends."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

import streamlit as st

from bootstrap import inject_streamlit_secrets, is_streamlit_cloud, secrets_status

inject_streamlit_secrets()

st.set_page_config(
    page_title="Growth Analytics Hub",
    page_icon="📈",
    layout="wide",
)

st.title("Growth Analytics Hub")
st.caption("퍼포먼스·콘텐츠 마케팅 데이터 분석 — Meta 소재 패턴 + YouTube KR 트렌드")

if is_streamlit_cloud():
    st.info("Streamlit Cloud · 좌측 사이드바에서 Meta Creative 또는 YouTube KR Trends 페이지로 이동하세요.")

status = secrets_status()
col1, col2 = st.columns(2)

with col1:
    st.subheader("Meta Creative Intelligence")
    st.markdown(
        "소재 메타데이터(카피, CTA, 포맷) + CPA/CTR/CVR → 패턴 분석 → Direction Brief"
    )
    if status["meta"]:
        st.success("Meta API Secrets 설정됨")
    else:
        st.warning("Meta API 미설정 — Sample mode 사용")

with col2:
    st.subheader("YouTube KR Trends")
    st.markdown(
        "YouTube Data API KR 트렌딩 + 마케팅 vertical 키워드 → Content Brief"
    )
    if status["youtube"]:
        st.success("YouTube API Key 설정됨")
    else:
        st.warning("YouTube API Key 미설정 — Sample mode 사용")

st.markdown("---")
st.markdown("### 시작하기")
st.page_link("pages/1_Meta_Creative.py", label="Meta Creative Intelligence →", icon="📊")
st.page_link("pages/2_YouTube_KR_Trends.py", label="YouTube KR Trends →", icon="▶️")
