"""Live vs sample comparison helpers."""

from __future__ import annotations

from datetime import datetime, timezone, timedelta

import pandas as pd

from youtube_analyze import keyword_vs_trending
from youtube_recommend import build_shoot_brief
from youtube_transform import overview_metrics


KST = timezone(timedelta(hours=9))


def now_kst_label() -> str:
    return datetime.now(KST).strftime("%Y-%m-%d %H:%M KST")


def compare_live_sample(
    keyword: str,
    live_trending: pd.DataFrame,
    sample_trending: pd.DataFrame,
    live_keyword: pd.DataFrame,
    sample_keyword: pd.DataFrame,
) -> dict:
    live_shoot = build_shoot_brief(keyword, live_trending, live_keyword)
    sample_shoot = build_shoot_brief(keyword, sample_trending, sample_keyword)
    live_ov = overview_metrics(live_trending)
    sample_ov = overview_metrics(sample_trending)
    live_gap = live_shoot["gap"]
    sample_gap = sample_shoot["gap"]

    return {
        "live_shoot": live_shoot,
        "sample_shoot": sample_shoot,
        "live_overview": live_ov,
        "sample_overview": sample_ov,
        "engagement_delta": round(live_ov["avg_engagement"] - sample_ov["avg_engagement"], 2),
        "shorts_delta": round(live_ov["shorts_pct"] - sample_ov["shorts_pct"], 1),
        "live_gap_engagement": live_gap.get("engagement_gap", 0),
        "sample_gap_engagement": sample_gap.get("engagement_gap", 0),
        "verdict_changed": live_shoot["verdict_label"] != sample_shoot["verdict_label"],
    }


def top_trending_titles(df: pd.DataFrame, limit: int = 5) -> list[dict]:
    if df.empty:
        return []
    top = df.sort_values("views", ascending=False).head(limit)
    return [
        {
            "title": row["title"],
            "views": int(row["views"]),
            "engagement": float(row["engagement_rate"]),
            "format": row.get("format_label", "—"),
        }
        for _, row in top.iterrows()
    ]
