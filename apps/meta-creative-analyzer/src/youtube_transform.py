"""Enrich YouTube video data with marketing-derived metrics."""

from __future__ import annotations

import re
from typing import Iterable

import pandas as pd

HASHTAG_RE = re.compile(r"#\S+")


def extract_title_hook(title: str) -> str:
    text = title.strip()
    if not text:
        return "일반"
    if "?" in text or any(k in text for k in ("왜", "어떻", "아직", "무엇")):
        return "질문형"
    if any(k in text for k in ("한정", "지금", "오늘", "마감", "선착순")):
        return "긴급형"
    if any(k in text for k in ("후기", "사례", "실제", "검증", "리뷰")):
        return "사회적증거"
    if any(k in text for k in ("단계", "방법", "How", "how", "하는법", "가이드")):
        return "How-to"
    if any(k in text for k in ("무료", "혜택", "맞춤", "추천", "지원", "리드")):
        return "혜택형"
    return "일반"


def extract_hashtags(title: str, tags: Iterable[str] | None) -> list[str]:
    found: set[str] = set()
    for match in HASHTAG_RE.findall(title):
        found.add(match.lower())
    if tags:
        for tag in tags:
            normalized = tag if tag.startswith("#") else f"#{tag}"
            found.add(normalized.lower())
    return sorted(found)


def enrich_youtube_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    out["engagement_rate"] = out.apply(
        lambda r: round((r["likes"] + r["comments"]) / r["views"] * 100, 3)
        if r.get("views") and r["views"] > 0
        else 0.0,
        axis=1,
    )

    if "title_hook" not in out.columns:
        out["title_hook"] = out["title"].apply(extract_title_hook)

    if "hashtags" not in out.columns or out["hashtags"].isna().any():
        out["hashtags"] = out.apply(
            lambda r: extract_hashtags(r.get("title", ""), r.get("tags")),
            axis=1,
        )

    if "format_label" not in out.columns:
        out["format_label"] = out["is_shorts"].map(lambda x: "Shorts" if x else "Long-form")

    return out


def overview_metrics(df: pd.DataFrame) -> dict:
    if df.empty:
        return {
            "video_count": 0,
            "avg_views": 0,
            "avg_engagement": 0.0,
            "shorts_pct": 0.0,
            "dominant_category": "—",
            "median_hours_since_publish": None,
        }

    category_counts = df["category_name"].value_counts()
    shorts_pct = round(df["is_shorts"].mean() * 100, 1) if "is_shorts" in df.columns else 0.0
    median_hours = None
    if "hours_since_publish" in df.columns and df["hours_since_publish"].notna().any():
        median_hours = round(float(df["hours_since_publish"].median()), 1)

    return {
        "video_count": len(df),
        "avg_views": int(df["views"].mean()),
        "avg_engagement": round(float(df["engagement_rate"].mean()), 2),
        "shorts_pct": shorts_pct,
        "dominant_category": category_counts.index[0] if len(category_counts) else "—",
        "median_hours_since_publish": median_hours,
    }
