"""YouTube Data API v3 client for KR trending and keyword search."""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd
import requests


class YouTubeAPIError(Exception):
    pass


MARKETING_KEYWORD_PRESETS = [
    "AI 마케팅",
    "SaaS",
    "퍼포먼스 마케팅",
    "리드 생성",
    "CRM",
    "B2B 마케팅",
]

ISO8601_DURATION = re.compile(
    r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?",
    re.IGNORECASE,
)


class YouTubeClient:
    BASE = "https://www.googleapis.com/youtube/v3"

    def __init__(self, api_key: str | None = None, region_code: str = "KR"):
        self.api_key = api_key or os.getenv("YOUTUBE_API_KEY", "")
        self.region_code = region_code

    @property
    def is_configured(self) -> bool:
        return bool(self.api_key)

    def _get(self, path: str, params: dict[str, Any]) -> dict:
        if not self.api_key:
            raise YouTubeAPIError("YOUTUBE_API_KEY is not set")

        query = {"key": self.api_key, **params}
        response = requests.get(f"{self.BASE}/{path.lstrip('/')}", params=query, timeout=60)

        if response.status_code != 200:
            payload = response.json() if response.content else {}
            message = payload.get("error", {}).get("message", response.text)
            raise YouTubeAPIError(f"YouTube API error ({response.status_code}): {message}")

        return response.json()

    def fetch_categories(self) -> dict[str, str]:
        data = self._get(
            "videoCategories",
            {"part": "snippet", "regionCode": self.region_code},
        )
        return {
            item["id"]: item["snippet"]["title"]
            for item in data.get("items", [])
            if item["snippet"].get("assignable")
        }

    def fetch_trending_videos(self, max_results: int = 50) -> list[dict]:
        data = self._get(
            "videos",
            {
                "part": "snippet,contentDetails,statistics",
                "chart": "mostPopular",
                "regionCode": self.region_code,
                "maxResults": min(max_results, 50),
            },
        )
        return data.get("items", [])

    def search_videos(self, keyword: str, max_results: int = 25) -> list[str]:
        data = self._get(
            "search",
            {
                "part": "snippet",
                "q": keyword,
                "type": "video",
                "regionCode": self.region_code,
                "maxResults": min(max_results, 25),
                "order": "relevance",
            },
        )
        return [item["id"]["videoId"] for item in data.get("items", []) if item.get("id", {}).get("videoId")]

    def fetch_videos_by_ids(self, video_ids: list[str]) -> list[dict]:
        if not video_ids:
            return []

        data = self._get(
            "videos",
            {
                "part": "snippet,contentDetails,statistics",
                "id": ",".join(video_ids[:50]),
            },
        )
        return data.get("items", [])

    def load_trending_dataframe(self, max_results: int = 50) -> pd.DataFrame:
        categories = self.fetch_categories()
        items = self.fetch_trending_videos(max_results=max_results)
        return _items_to_dataframe(items, categories)

    def load_keyword_dataframe(self, keyword: str, max_results: int = 25) -> pd.DataFrame:
        categories = self.fetch_categories()
        video_ids = self.search_videos(keyword, max_results=max_results)
        items = self.fetch_videos_by_ids(video_ids)
        return _items_to_dataframe(items, categories, source_keyword=keyword)


def parse_duration_seconds(duration: str) -> int:
    match = ISO8601_DURATION.match(duration or "")
    if not match:
        return 0
    hours, minutes, seconds = match.groups()
    return int(hours or 0) * 3600 + int(minutes or 0) * 60 + int(seconds or 0)


def _items_to_dataframe(
    items: list[dict],
    categories: dict[str, str],
    source_keyword: str | None = None,
) -> pd.DataFrame:
    rows: list[dict] = []
    now = datetime.now(timezone.utc)

    for item in items:
        snippet = item.get("snippet", {})
        stats = item.get("statistics", {})
        content = item.get("contentDetails", {})
        duration_seconds = parse_duration_seconds(content.get("duration", ""))

        published_raw = snippet.get("publishedAt", "")
        try:
            published_at = datetime.fromisoformat(published_raw.replace("Z", "+00:00"))
            hours_since = round((now - published_at).total_seconds() / 3600, 1)
        except ValueError:
            published_at = None
            hours_since = None

        category_id = snippet.get("categoryId", "")
        tags = snippet.get("tags") or []
        title = snippet.get("title", "")

        views = int(stats.get("viewCount", 0))
        likes = int(stats.get("likeCount", 0))
        comments = int(stats.get("commentCount", 0))

        rows.append(
            {
                "video_id": item.get("id"),
                "title": title,
                "channel_title": snippet.get("channelTitle", ""),
                "category_id": category_id,
                "category_name": categories.get(category_id, "Unknown"),
                "published_at": published_raw,
                "duration_seconds": duration_seconds,
                "views": views,
                "likes": likes,
                "comments": comments,
                "tags": tags,
                "source_keyword": source_keyword,
                "is_shorts": duration_seconds <= 60 or "#shorts" in title.lower(),
                "hours_since_publish": hours_since,
            }
        )

    return pd.DataFrame(rows)


def load_sample_trending_dataframe() -> pd.DataFrame:
    sample_path = Path(__file__).resolve().parent.parent / "data" / "sample_trending.json"
    with sample_path.open(encoding="utf-8") as f:
        rows = json.load(f)
    return pd.DataFrame(rows)
