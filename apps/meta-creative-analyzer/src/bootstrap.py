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
    """Resolve secret: session override → env → Streamlit Cloud Secrets."""
    if key == "YOUTUBE_API_KEY":
        override = str(st.session_state.get("yt_api_key_override", "")).strip()
        if override:
            return override

    value = os.getenv(key, "").strip()
    if value:
        return value

    try:
        if key in st.secrets:
            return str(st.secrets[key]).strip()
        # lowercase / nested fallbacks
        lower_map = {k.lower(): k for k in st.secrets.keys()}
        if key.lower() in lower_map:
            return str(st.secrets[lower_map[key.lower()]]).strip()
    except Exception:
        pass

    return ""


def inject_streamlit_secrets() -> None:
    """Streamlit Cloud Secrets → os.environ."""
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


def mask_secret(value: str) -> str:
    if len(value) <= 8:
        return "****"
    return f"{value[:4]}...{value[-4:]}"
