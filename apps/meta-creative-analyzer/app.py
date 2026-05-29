"""Growth Analytics Hub — Meta Creative + YouTube Shoot Brief."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

import streamlit as st

from bootstrap import inject_streamlit_secrets
from views.hub import render as render_hub
from views.meta_creative import render as render_meta
from views.youtube_trends import render as render_youtube

inject_streamlit_secrets()

st.set_page_config(
    page_title="Growth Analytics Hub",
    page_icon="📈",
    layout="wide",
)

pages = [
    st.Page(render_hub, title="Growth Hub", icon="📈", default=True),
    st.Page(render_meta, title="Meta Creative", icon="📊", url_path="Meta_Creative"),
    st.Page(render_youtube, title="Shoot Brief", icon="🎬", url_path="YouTube_KR_Trends"),
]

pg = st.navigation(pages)
pg.run()
