"""Pattern analysis across creative metadata and performance."""

from __future__ import annotations

import pandas as pd


def quartile_split(df: pd.DataFrame, metric: str = "cpa", ascending: bool = True) -> tuple[pd.DataFrame, pd.DataFrame]:
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


def aggregate_by_dimension(df: pd.DataFrame, dimension: str, metric: str = "cpa") -> pd.DataFrame:
    valid = df.dropna(subset=[metric])
    if valid.empty:
        return pd.DataFrame(columns=[dimension, "count", "avg_cpa", "avg_ctr", "avg_cvr"])

    grouped = (
        valid.groupby(dimension)
        .agg(
            count=("ad_id", "count"),
            avg_cpa=(metric, "mean"),
            avg_ctr=("ctr", "mean"),
            avg_cvr=("cvr", "mean"),
        )
        .reset_index()
        .sort_values("avg_cpa")
    )
    grouped["avg_cpa"] = grouped["avg_cpa"].round(0)
    grouped["avg_ctr"] = grouped["avg_ctr"].round(2)
    grouped["avg_cvr"] = grouped["avg_cvr"].round(2)
    return grouped


def compare_top_bottom(df: pd.DataFrame) -> dict:
    top, bottom = quartile_split(df, metric="cpa", ascending=True)

    def mode_frame(frame: pd.DataFrame, col: str) -> str | None:
        if frame.empty or col not in frame.columns:
            return None
        counts = frame[col].value_counts()
        return counts.index[0] if len(counts) else None

    return {
        "top_count": len(top),
        "bottom_count": len(bottom),
        "top_format": mode_frame(top, "format_tag"),
        "bottom_format": mode_frame(bottom, "format_tag"),
        "top_hook": mode_frame(top, "hook_keyword"),
        "bottom_hook": mode_frame(bottom, "hook_keyword"),
        "top_cta": mode_frame(top, "call_to_action_type"),
        "bottom_cta": mode_frame(bottom, "call_to_action_type"),
        "top_avg_cpa": round(top["cpa"].mean(), 0) if len(top) else None,
        "bottom_avg_cpa": round(bottom["cpa"].mean(), 0) if len(bottom) else None,
        "top_avg_ctr": round(top["ctr"].mean(), 2) if len(top) else None,
        "bottom_avg_ctr": round(bottom["ctr"].mean(), 2) if len(bottom) else None,
    }
