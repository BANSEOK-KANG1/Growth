"""Generate Shoot Brief — keyword gap vs KR trending → one video to shoot."""

from __future__ import annotations

import pandas as pd

from youtube_analyze import (
    aggregate_by_dimension,
    compare_top_bottom,
    format_comparison,
    keyword_vs_trending,
    top_hashtags,
)


def _pick_format(keyword_df: pd.DataFrame, trending_fmt: dict) -> tuple[str, str]:
    """Return (format_label, rationale)."""
    if len(keyword_df) >= 3:
        kw_shorts = keyword_df["is_shorts"].mean() * 100
        kw_shorts_eng = (
            float(keyword_df[keyword_df["is_shorts"]]["engagement_rate"].mean())
            if keyword_df["is_shorts"].any()
            else 0.0
        )
        kw_long_eng = (
            float(keyword_df[~keyword_df["is_shorts"]]["engagement_rate"].mean())
            if (~keyword_df["is_shorts"]).any()
            else 0.0
        )
        if kw_long_eng > kw_shorts_eng + 0.3:
            return "Long-form (3분 내외)", f"키워드 검색 결과 Long-form engagement {kw_long_eng:.2f}% > Shorts {kw_shorts_eng:.2f}%"
        if kw_shorts_eng > kw_long_eng + 0.3:
            return "Shorts (30~60초)", f"키워드 검색 결과 Shorts engagement {kw_shorts_eng:.2f}% > Long-form {kw_long_eng:.2f}%"
        return (
            "Shorts 훅 30초 + Long 설명 3분 (페어링)",
            "키워드 내 Shorts/Long engagement 차이 미미 — 훅·본편 분리 테스트",
        )

    if trending_fmt["engagement_gap"] < -0.3:
        return "Long-form (3분 내외)", f"KR 트렌딩 Long-form engagement가 Shorts 대비 {abs(trending_fmt['engagement_gap']):.2f}%p 높음"
    if trending_fmt["shorts_pct"] >= 50:
        return "Shorts (30~60초)", f"KR 트렌딩 Shorts 비중 {trending_fmt['shorts_pct']}% — 먼저 훅 테스트"
    return "Long-form (3분 내외)", "트렌딩 기준 설명형 콘텐츠 비중 높음"


def _pick_hook(keyword_df: pd.DataFrame, trending_df: pd.DataFrame) -> str:
    if len(keyword_df) >= 3:
        hooks = keyword_df["title_hook"].value_counts()
        if len(hooks):
            return hooks.index[0]
    comp = compare_top_bottom(trending_df)
    return comp.get("top_hook") or "How-to"


def _gap_verdict(gap: dict) -> tuple[str, str]:
    overlap = gap.get("category_overlap_pct", 0)
    eng_gap = gap.get("engagement_gap", 0)

    if overlap < 30 and eng_gap >= 0:
        return (
            "블루오션",
            "대중 트렌딩과 카테고리 겹침 낮음 · 키워드 전용 콘텐츠로 차별화 가능",
        )
    if overlap >= 60:
        return (
            "레드오션",
            "트렌딩과 카테고리 대부분 겹침 · 제목 훅·포맷으로 차별화 필요",
        )
    if eng_gap < -0.5:
        return (
            "니치 · 품질 우선",
            "키워드 검색 engagement가 트렌딩 대비 낮음 · How-to·사례형으로 신뢰도 확보",
        )
    return (
        "니치 · 성장 가능",
        "트렌딩과 부분 겹침 · 키워드 특화 각도로 포지셔닝",
    )


def _title_examples(keyword: str, hook: str) -> list[str]:
    templates = {
        "질문형": [
            f"{keyword}, 아직도 감으로만 기획하시나요?",
            f"왜 {keyword} 콘텐츠는 조회수는 높은데 전환이 안 될까?",
        ],
        "How-to": [
            f"{keyword} 3단계 실전 가이드 | 초보도 10분 만에",
            f"[How-to] {keyword} 성과 내는 영상 구조 (템플릿 공개)",
        ],
        "혜택형": [
            f"{keyword}로 리드 2배 늘리는 영상 공식",
            f"무료 템플릿 | {keyword} 촬영 전 체크리스트",
        ],
        "사회적증거": [
            f"실제 {keyword} 사례 — 전환율 X% 달성한 방법",
            f"{keyword} 후기 모음 | B2B 마케터가 검증한 3가지",
        ],
        "긴급형": [
            f"이번 주만 | {keyword} 트렌드 반영 촬영 가이드",
            f"지금 {keyword} 영상 올려야 하는 이유 (데이터 근거)",
        ],
    }
    return templates.get(hook, templates["How-to"])


def _pick_tags(keyword: str, gap: dict, keyword_df: pd.DataFrame, trending_df: pd.DataFrame) -> list[str]:
    tags: list[str] = []
    unique = gap.get("unique_keyword_hashtags") or []
    tags.extend(unique[:2])

    normalized_kw = keyword.replace(" ", "").lower()
    if not any(normalized_kw in t for t in tags):
        tags.append(f"#{normalized_kw}")

    trending_tags = top_hashtags(trending_df, limit=3)
    for t, _ in trending_tags:
        if t not in tags and len(tags) < 3:
            tags.append(t)

    if len(keyword_df) >= 2:
        for row_tags in keyword_df["hashtags"].head(5):
            if isinstance(row_tags, list):
                for t in row_tags:
                    if t not in tags and len(tags) < 3:
                        tags.append(t)

    return tags[:3] if tags else [f"#{normalized_kw}", "#b2b", "#마케팅"]


def build_shoot_brief(
    keyword: str,
    trending_df: pd.DataFrame,
    keyword_df: pd.DataFrame,
) -> dict:
    gap = keyword_vs_trending(trending_df, keyword_df, keyword)
    trending_fmt = format_comparison(trending_df)
    verdict_label, verdict_detail = _gap_verdict(gap)

    format_label, format_rationale = _pick_format(keyword_df, trending_fmt)
    hook = _pick_hook(keyword_df, trending_df)
    title_examples = _title_examples(keyword, hook)
    test_tags = _pick_tags(keyword, gap, keyword_df, trending_df)

    duration = "30~60초" if "Shorts" in format_label and "페어링" not in format_label else "2~4분"
    if "페어링" in format_label:
        duration = "Shorts 30초 + Long 3분"

    this_week_action = (
        f"이번 주: {format_label.split('(')[0].strip()} · {hook} 훅 · "
        f"제목 「{title_examples[0]}」 1편 촬영 후 {', '.join(test_tags)} 태그로 업로드"
    )

    headline = (
        f"「{keyword}」는 KR 대중 트렌드와 {gap['category_overlap_pct']:.0f}% 겹침 · "
        f"engagement {gap['engagement_gap']:+.2f}%p → **{verdict_label}**"
    )

    return {
        "keyword": keyword,
        "headline": headline,
        "gap": gap,
        "verdict_label": verdict_label,
        "verdict_detail": verdict_detail,
        "format": format_label,
        "format_rationale": format_rationale,
        "duration": duration,
        "title_hook": hook,
        "title_examples": title_examples,
        "test_tags": test_tags,
        "this_week_action": this_week_action,
    }


def build_content_brief(
    trending_df: pd.DataFrame,
    keyword_comparisons: list[dict] | None = None,
    primary_keyword: str | None = None,
    keyword_df: pd.DataFrame | None = None,
) -> dict:
    """Legacy wrapper — prefer build_shoot_brief for primary keyword."""
    if primary_keyword and keyword_df is not None:
        shoot = build_shoot_brief(primary_keyword, trending_df, keyword_df)
        return {
            "summary": shoot["headline"],
            "recommendations": [
                f"Gap: {shoot['verdict_label']} — {shoot['verdict_detail']}",
                f"포맷: {shoot['format']} ({shoot['format_rationale']})",
                f"제목 훅: {shoot['title_hook']}",
                f"태그: {', '.join(shoot['test_tags'])}",
            ],
            "next_tests": shoot["title_examples"] + [shoot["this_week_action"]],
            "shoot_brief": shoot,
            "keyword_comparisons": [shoot["gap"]],
        }

    keyword_comparisons = keyword_comparisons or []
    return {
        "summary": "키워드를 입력하면 Shoot Brief가 생성됩니다.",
        "recommendations": [],
        "next_tests": [],
        "shoot_brief": None,
        "keyword_comparisons": keyword_comparisons,
    }


def brief_to_markdown(brief: dict) -> str:
    shoot = brief.get("shoot_brief")
    if not shoot:
        return "# Shoot Brief\n\n키워드를 선택하세요.\n"

    lines = [
        f"# Shoot Brief — {shoot['keyword']}",
        "",
        shoot["headline"],
        "",
        f"**판정:** {shoot['verdict_label']} — {shoot['verdict_detail']}",
        "",
        "## 이번 주 촬영 1편",
        shoot["this_week_action"],
        "",
        "## 포맷",
        f"- {shoot['format']} ({shoot['duration']})",
        f"- {shoot['format_rationale']}",
        "",
        "## 제목 훅 & 예시",
        f"- 훅: **{shoot['title_hook']}**",
    ]
    for i, title in enumerate(shoot["title_examples"], 1):
        lines.append(f"{i}. {title}")

    lines.extend(["", "## 테스트 태그", ", ".join(shoot["test_tags"]), "", "## Gap 수치"])
    gap = shoot["gap"]
    lines.append(f"- Engagement gap: {gap['engagement_gap']:+.3f}%p")
    lines.append(f"- Shorts share gap: {gap['shorts_share_gap']:+.1f}%p")
    lines.append(f"- Category overlap: {gap['category_overlap_pct']}%")

    return "\n".join(lines)
