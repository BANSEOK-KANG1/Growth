"""Meta Marketing API client for ads, creatives, and insights."""

from __future__ import annotations

import os
from typing import Any

import pandas as pd
import requests


class MetaAPIError(Exception):
    pass


class MetaClient:
    BASE = "https://graph.facebook.com"

    def __init__(
        self,
        access_token: str | None = None,
        ad_account_id: str | None = None,
        api_version: str | None = None,
    ):
        self.access_token = access_token or os.getenv("META_ACCESS_TOKEN", "")
        self.ad_account_id = (ad_account_id or os.getenv("META_AD_ACCOUNT_ID", "")).strip()
        self.api_version = api_version or os.getenv("META_API_VERSION", "v21.0")

        if self.ad_account_id and not self.ad_account_id.startswith("act_"):
            self.ad_account_id = f"act_{self.ad_account_id}"

    @property
    def is_configured(self) -> bool:
        return bool(self.access_token and self.ad_account_id)

    def _get(self, path: str, params: dict[str, Any] | None = None) -> dict:
        if not self.access_token:
            raise MetaAPIError("META_ACCESS_TOKEN is not set")

        url = f"{self.BASE}/{self.api_version}/{path.lstrip('/')}"
        query = {"access_token": self.access_token, **(params or {})}
        response = requests.get(url, params=query, timeout=60)

        if response.status_code != 200:
            payload = response.json() if response.content else {}
            message = payload.get("error", {}).get("message", response.text)
            raise MetaAPIError(f"Meta API error ({response.status_code}): {message}")

        return response.json()

    def _paginate(self, path: str, params: dict[str, Any]) -> list[dict]:
        items: list[dict] = []
        data = self._get(path, params)

        while True:
            items.extend(data.get("data", []))
            paging = data.get("paging", {})
            next_url = paging.get("next")
            if not next_url:
                break
            response = requests.get(next_url, timeout=60)
            if response.status_code != 200:
                break
            data = response.json()

        return items

    def fetch_ads_with_creatives(self, limit: int = 100) -> list[dict]:
        fields = (
            "id,name,status,creative{"
            "id,title,body,call_to_action_type,object_type,"
            "object_story_spec,video_id,thumbnail_url,image_url"
            "}"
        )
        return self._paginate(
            f"{self.ad_account_id}/ads",
            {"fields": fields, "limit": min(limit, 100)},
        )

    def fetch_ad_insights(
        self,
        date_preset: str = "last_30d",
        level: str = "ad",
    ) -> list[dict]:
        fields = (
            "ad_id,ad_name,spend,impressions,clicks,ctr,cpc,"
            "actions,cost_per_action_type"
        )
        return self._paginate(
            f"{self.ad_account_id}/insights",
            {
                "fields": fields,
                "level": level,
                "date_preset": date_preset,
                "limit": 100,
            },
        )

    def load_creatives_dataframe(
        self,
        date_preset: str = "last_30d",
        limit: int = 100,
    ) -> pd.DataFrame:
        ads = self.fetch_ads_with_creatives(limit=limit)
        insights = self.fetch_ad_insights(date_preset=date_preset)
        insights_map = {row.get("ad_id"): row for row in insights}

        rows: list[dict] = []
        for ad in ads:
            creative = ad.get("creative") or {}
            insight = insights_map.get(ad.get("id"), {})

            object_type = creative.get("object_type") or "UNKNOWN"
            video_id = creative.get("video_id")
            format_tag = _infer_format(object_type, video_id, creative)

            conversions = _extract_conversions(insight.get("actions", []))
            spend = float(insight.get("spend") or 0)
            clicks = int(insight.get("clicks") or 0)
            cpa = round(spend / conversions, 1) if conversions else None
            cvr = round(conversions / clicks * 100, 2) if clicks else None

            title = creative.get("title") or ""
            body = creative.get("body") or ""
            hook = _extract_hook_keyword(title, body)

            rows.append(
                {
                    "ad_id": ad.get("id"),
                    "ad_name": ad.get("name"),
                    "title": title,
                    "body": body,
                    "call_to_action_type": creative.get("call_to_action_type") or "NONE",
                    "object_type": object_type,
                    "format_tag": format_tag,
                    "hook_keyword": hook,
                    "spend": spend,
                    "impressions": int(insight.get("impressions") or 0),
                    "clicks": clicks,
                    "ctr": float(insight.get("ctr") or 0),
                    "cpc": float(insight.get("cpc") or 0),
                    "conversions": conversions,
                    "cpa": cpa,
                    "cvr": cvr,
                }
            )

        return pd.DataFrame(rows)


def _infer_format(object_type: str, video_id: str | None, creative: dict) -> str:
    if video_id or object_type == "VIDEO":
        return "Video"
    if object_type in ("CAROUSEL", "CAROUSEL_IMAGE", "CAROUSEL_VIDEO"):
        return "Carousel"
    spec = creative.get("object_story_spec") or {}
    if spec.get("link_data", {}).get("child_attachments"):
        return "Carousel"
    return "Image"


def _extract_conversions(actions: list[dict] | None) -> int:
    if not actions:
        return 0
    priority = (
        "lead",
        "offsite_conversion.fb_pixel_lead",
        "contact",
        "offsite_conversion.fb_pixel_custom",
        "complete_registration",
    )
    total = 0
    for action_type in priority:
        for action in actions:
            if action.get("action_type") == action_type:
                total += int(float(action.get("value", 0)))
        if total:
            return total
    for action in actions:
        if "conversion" in action.get("action_type", "") or action.get("action_type") == "link_click":
            continue
        total += int(float(action.get("value", 0)))
    return total


def _extract_hook_keyword(title: str, body: str) -> str:
    text = f"{title} {body}".strip()
    if not text:
        return "일반"
    if "?" in text or "왜" in text or "어떻" in text or "아직" in text:
        return "질문형"
    if any(k in text for k in ("한정", "지금", "오늘", "마감", "선착순")):
        return "긴급형"
    if any(k in text for k in ("후기", "사례", "실제", "검증")):
        return "사회적증거"
    if any(k in text for k in ("단계", "방법", "How", "how")):
        return "How-to"
    if any(k in text for k in ("무료", "혜택", "맞춤", "추천", "지원")):
        return "혜택형"
    return "일반"


def load_sample_dataframe() -> pd.DataFrame:
    import json
    from pathlib import Path

    sample_path = Path(__file__).resolve().parent.parent / "data" / "sample_creatives.json"
    with sample_path.open(encoding="utf-8") as f:
        rows = json.load(f)
    return pd.DataFrame(rows)
