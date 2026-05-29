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


def get_secret(key: str) -> str:
    """Resolve secret from env → Streamlit Cloud Secrets."""
    value = os.getenv(key, "").strip()
    if value:
        return value
    try:
        if key in st.secrets:
            return str(st.secrets[key]).strip()
    except Exception:
        pass
    return ""


def inject_streamlit_secrets() -> None:
    """Streamlit Cloud Secrets → os.environ for downstream os.getenv callers."""
    for key in SECRET_KEYS:
        if os.getenv(key):
            continue
        value = get_secret(key)
        if value:
            os.environ[key] = value


def is_streamlit_cloud() -> bool:
    return os.getenv("STREAMLIT_RUNTIME_ENVIRONMENT") == "cloud" or "streamlit.app" in os.getenv(
        "STREAMLIT_SERVER_ADDRESS", ""
    )


def secrets_status() -> dict[str, bool]:
    return {
        "meta": bool(get_secret("META_ACCESS_TOKEN") and get_secret("META_AD_ACCOUNT_ID")),
        "youtube": bool(get_secret("YOUTUBE_API_KEY")),
    }
