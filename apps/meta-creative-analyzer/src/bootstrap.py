"""Shared app bootstrap: paths, env, Streamlit secrets."""

from __future__ import annotations

import os
import sys
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

load_dotenv(ROOT / ".env")

SECRET_KEYS = (
    "META_ACCESS_TOKEN",
    "META_AD_ACCOUNT_ID",
    "META_API_VERSION",
    "YOUTUBE_API_KEY",
)


def inject_streamlit_secrets() -> None:
    """Streamlit Cloud Secrets → os.environ."""
    try:
        for key in SECRET_KEYS:
            if key in st.secrets and not os.getenv(key):
                os.environ[key] = str(st.secrets[key])
    except Exception:
        pass


def is_streamlit_cloud() -> bool:
    return os.getenv("STREAMLIT_RUNTIME_ENVIRONMENT") == "cloud" or "streamlit.app" in os.getenv(
        "STREAMLIT_SERVER_ADDRESS", ""
    )


def secrets_status() -> dict[str, bool]:
    return {
        "meta": bool(os.getenv("META_ACCESS_TOKEN") and os.getenv("META_AD_ACCOUNT_ID")),
        "youtube": bool(os.getenv("YOUTUBE_API_KEY")),
    }
