"""Pattern analysis for YouTube trending and keyword comparison."""

from __future__ import annotations

from collections import Counter

import pandas as pd


def quartile_split(
    df: pd.DataFrame,
    metric: str = "engagement_rate",
    ascending: bool = False,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    valid = df.dropna(subset=[metric]).copy()
    if len(valid) < 4:
        mid = len(valid) // 2
        sorted_df = valid.sort_values(metric, ascending=ascending)
        return sorted_df.head(max(mid, 1)), sorted_df.tail(max(len(valid) - mid, 1))

    q1 = valid[metric].quantile(0.25)
    q3 = valid[metric].quantile(0.75)

    if ascending:
        top = valid[valid[metric] <= q1]
        bottom = valid[valid[metric] >= q3]
    else:
        top = valid[valid[metric] >= q3]
        bottom = valid[valid[metric] <= q1]

    return top, bottom


def aggregate_by_dimension(
    df: pd.DataFrame,
    dimension: str,
    metric: str = "engagement_rate",
) -> pd.DataFrame:
    if df.empty or dimension not in df.columns:
        return pd.DataFrame(columns=[dimension, "count", "avg_views", "avg_engagement"])

    grouped = (
        df.groupby(dimension)
        .agg(
            count=("video_id", "count"),
            avg_views=("views", "mean"),
            avg_engagement=(metric, "mean"),
        )
        .reset_index()
        .sort_values("avg_engagement", ascending=False)
    )
    grouped["avg_views"] = grouped["avg_views"].round(0).astype(int)
    grouped["avg_engagement"] = grouped["avg_engagement"].round(3)
    return grouped


def compare_top_bottom(df: pd.DataFrame) -> dict:
    top, bottom = quartile_split(df, metric="engagement_rate", ascending=False)

    def mode_frame(frame: pd.DataFrame, col: str) -> str | None:
        if frame.empty or col not in frame.columns:
            return None
        counts = frame[col].value_counts()
        return counts.index[0] if len(counts) else None

    def shorts_share(frame: pd.DataFrame) -> float:
        if frame.empty or "is_shorts" not in frame.columns:
            return 0.0
        return round(frame["is_shorts"].mean() * 100, 1)

    return {
        "top_count": len(top),
        "bottom_count": len(bottom),
        "top_format": mode_frame(top, "format_label"),
        "bottom_format": mode_frame(bottom, "format_label"),
        "top_hook": mode_frame(top, "title_hook"),
        "bottom_hook": mode_frame(bottom, "title_hook"),
        "top_category": mode_frame(top, "category_name"),
        "bottom_category": mode_frame(bottom, "category_name"),
        "top_avg_engagement": round(float(top["engagement_rate"].mean()), 3) if len(top) else None,
        "bottom_avg_engagement": round(float(bottom["engagement_rate"].mean()), 3) if len(bottom) else None,
        "top_shorts_pct": shorts_share(top),
        "bottom_shorts_pct": shorts_share(bottom),
    }


def category_mix(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame(columns=["category_name", "share_pct", "avg_engagement"])

    counts = df["category_name"].value_counts(normalize=True).mul(100).round(1)
    engagement = df.groupby("category_name")["engagement_rate"].mean().round(3)

    mix = pd.DataFrame({"category_name": counts.index, "share_pct": counts.values})
    mix["avg_engagement"] = mix["category_name"].map(engagement)
    return mix.sort_values("share_pct", ascending=False)


def format_comparison(df: pd.DataFrame) -> dict:
    if df.empty or "format_label" not in df.columns:
        return {"shorts_pct": 0.0, "shorts_engagement": 0.0, "long_engagement": 0.0, "engagement_gap": 0.0}

    shorts = df[df["is_shorts"]]
    long_form = df[~df["is_shorts"]]
    shorts_eng = round(float(shorts["engagement_rate"].mean()), 3) if len(shorts) else 0.0
    long_eng = round(float(long_form["engagement_rate"].mean()), 3) if len(long_form) else 0.0

    return {
        "shorts_pct": round(len(shorts) / len(df) * 100, 1),
        "shorts_engagement": shorts_eng,
        "long_engagement": long_eng,
        "engagement_gap": round(shorts_eng - long_eng, 3),
    }


def _flatten_hashtags(series: pd.Series) -> list[str]:
    tags: list[str] = []
    for value in series:
        if isinstance(value, list):
            tags.extend(value)
    return tags


def keyword_vs_trending(
    trending_df: pd.DataFrame,
    keyword_df: pd.DataFrame,
    keyword: str,
) -> dict:
    if keyword_df.empty:
        return {
            "keyword": keyword,
            "keyword_count": 0,
            "engagement_gap": 0.0,
            "shorts_share_gap": 0.0,
            "category_overlap_pct": 0.0,
            "common_hashtags": [],
            "unique_keyword_hashtags": [],
            "unique_trending_hashtags": [],
        }

    trending_eng = float(trending_df["engagement_rate"].mean()) if len(trending_df) else 0.0
    keyword_eng = float(keyword_df["engagement_rate"].mean())
    trending_shorts = trending_df["is_shorts"].mean() * 100 if len(trending_df) else 0.0
    keyword_shorts = keyword_df["is_shorts"].mean() * 100

    trending_cats = set(trending_df["category_name"].unique())
    keyword_cats = set(keyword_df["category_name"].unique())
    overlap = len(trending_cats & keyword_cats) / len(trending_cats) * 100 if trending_cats else 0.0

    trending_tags = set(_flatten_hashtags(trending_df["hashtags"]))
    keyword_tags = set(_flatten_hashtags(keyword_df["hashtags"]))

    return {
        "keyword": keyword,
        "keyword_count": len(keyword_df),
        "engagement_gap": round(keyword_eng - trending_eng, 3),
        "shorts_share_gap": round(keyword_shorts - trending_shorts, 1),
        "category_overlap_pct": round(overlap, 1),
        "common_hashtags": sorted(trending_tags & keyword_tags)[:10],
        "unique_keyword_hashtags": sorted(keyword_tags - trending_tags)[:10],
        "unique_trending_hashtags": sorted(trending_tags - keyword_tags)[:10],
        "keyword_avg_engagement": round(keyword_eng, 3),
        "trending_avg_engagement": round(trending_eng, 3),
        "top_keyword_category": keyword_df["category_name"].value_counts().index[0]
        if len(keyword_df)
        else None,
    }


def top_hashtags(df: pd.DataFrame, limit: int = 10) -> list[tuple[str, int]]:
    counter: Counter[str] = Counter()
    for tags in df.get("hashtags", []):
        if isinstance(tags, list):
            counter.update(tags)
    return counter.most_common(limit)
