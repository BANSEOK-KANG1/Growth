"""Transform and enrich creative performance data."""

from __future__ import annotations

import pandas as pd


def enrich_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    if "cpa" not in out.columns or out["cpa"].isna().all():
        out["cpa"] = out.apply(
            lambda r: round(r["spend"] / r["conversions"], 1)
            if r.get("conversions") and r["conversions"] > 0
            else None,
            axis=1,
        )

    if "cvr" not in out.columns or out["cvr"].isna().all():
        out["cvr"] = out.apply(
            lambda r: round(r["conversions"] / r["clicks"] * 100, 2)
            if r.get("clicks") and r["clicks"] > 0
            else None,
            axis=1,
        )

    if "ctr" not in out.columns:
        out["ctr"] = out.apply(
            lambda r: round(r["clicks"] / r["impressions"] * 100, 2)
            if r.get("impressions") and r["impressions"] > 0
            else 0,
            axis=1,
        )

    out["copy_preview"] = out.apply(
        lambda r: _preview(f"{r.get('title', '')} — {r.get('body', '')}"),
        axis=1,
    )
    return out


def _preview(text: str, max_len: int = 80) -> str:
    text = " ".join(text.split())
    return text if len(text) <= max_len else text[: max_len - 1] + "…"


def overview_metrics(df: pd.DataFrame) -> dict:
    valid_cpa = df.dropna(subset=["cpa"])
    format_counts = df["format_tag"].value_counts(normalize=True).mul(100).round(1)

    return {
        "creative_count": len(df),
        "avg_ctr": round(df["ctr"].mean(), 2) if len(df) else 0,
        "avg_cpa": round(valid_cpa["cpa"].mean(), 0) if len(valid_cpa) else 0,
        "total_spend": int(df["spend"].sum()),
        "video_pct": float(format_counts.get("Video", 0)),
        "image_pct": float(format_counts.get("Image", 0)),
        "carousel_pct": float(format_counts.get("Carousel", 0)),
    }
