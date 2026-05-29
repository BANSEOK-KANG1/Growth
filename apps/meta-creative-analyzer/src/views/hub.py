"""Growth Analytics Hub landing view."""

from __future__ import annotations

import streamlit as st

from bootstrap import is_streamlit_cloud, secrets_status


def render() -> None:
    st.title("Growth Analytics Hub")
    st.caption("퍼포먼스·콘텐츠 마케팅 데이터 분석 — Meta 소재 패턴 + YouTube Shoot Brief")

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
        st.subheader("Keyword Gap → Shoot Brief")
        st.markdown(
            "마케팅 키워드 vs KR 대중 트렌드 gap → **이번 주 찍을 영상 1편** 브리프"
        )
        if status["youtube"]:
            st.success("YouTube API Key 설정됨")
        else:
            st.warning("YouTube API Key 미설정 — Sample mode 사용")

    st.markdown("---")
    st.markdown("### 시작하기")
    st.info("← **좌측 사이드바**에서 `Meta Creative` 또는 `Shoot Brief` 페이지를 선택하세요.")

    if is_streamlit_cloud():
        st.caption(
            "YouTube Live API: Streamlit **Settings → Secrets**에 "
            "`YOUTUBE_API_KEY` 추가 후 재시작"
        )
