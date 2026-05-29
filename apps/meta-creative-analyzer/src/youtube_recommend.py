"""Generate Content Brief from YouTube trend patterns."""

from __future__ import annotations

import pandas as pd

from youtube_analyze import (
    aggregate_by_dimension,
    category_mix,
    compare_top_bottom,
    format_comparison,
    keyword_vs_trending,
    top_hashtags,
)


def build_content_brief(
    trending_df: pd.DataFrame,
    keyword_comparisons: list[dict] | None = None,
) -> dict:
    comparison = compare_top_bottom(trending_df)
    fmt = format_comparison(trending_df)
    cat_mix = category_mix(trending_df)
    hook_stats = aggregate_by_dimension(trending_df, "title_hook")
    keyword_comparisons = keyword_comparisons or []

    best_category = cat_mix.iloc[0].to_dict() if not cat_mix.empty else None
    best_hook = hook_stats.iloc[0].to_dict() if not hook_stats.empty else None

    recommendations: list[str] = []
    next_tests: list[str] = []

    if best_category:
        recommendations.append(
            f"카테고리: {best_category['category_name']}이 트렌딩 {best_category['share_pct']}% · "
            f"평균 engagement {best_category['avg_engagement']}%"
        )

    if fmt["shorts_pct"] > 0:
        gap_label = "높음" if fmt["engagement_gap"] >= 0 else "낮음"
        recommendations.append(
            f"포맷: Shorts 비중 {fmt['shorts_pct']}% · Shorts engagement {fmt['shorts_engagement']}% vs "
            f"Long-form {fmt['long_engagement']}% ({gap_label})"
        )
        if fmt["engagement_gap"] < 0:
            recommendations.append("포맷 액션: 설명형 Long-form 우선 — Shorts는 훅 테스트용으로 제한")

    if comparison.get("top_hook") and comparison.get("bottom_hook"):
        recommendations.append(
            f"제목 훅: engagement 상위 25%는 '{comparison['top_hook']}' 비중 높음 · "
            f"하위 25%는 '{comparison['bottom_hook']}'"
        )

    trending_tags = top_hashtags(trending_df, limit=5)
    if trending_tags:
        tag_str = ", ".join(t for t, _ in trending_tags[:3])
        recommendations.append(f"트렌딩 해시태그: {tag_str}")

    for kw in keyword_comparisons[:2]:
        if kw.get("keyword_count", 0) == 0:
            continue
        gap = kw["engagement_gap"]
        direction = "높음" if gap >= 0 else "낮음"
        overlap = kw["category_overlap_pct"]
        blue_ocean = "블루오션 후보" if overlap < 30 else "트렌딩과 카테고리 겹침 높음"
        recommendations.append(
            f"키워드 '{kw['keyword']}': engagement 트렌딩 대비 {gap:+.3f}%p ({direction}) · "
            f"카테고리 overlap {overlap}% — {blue_ocean}"
        )
        unique = kw.get("unique_keyword_hashtags") or []
        if unique:
            recommendations.append(
                f"키워드 '{kw['keyword']}' 고유 태그: {', '.join(unique[:3])} 테스트 추천"
            )

    hook = best_hook["title_hook"] if best_hook else "How-to"
    fmt_label = comparison.get("top_format") or "Long-form"
    primary_kw = keyword_comparisons[0]["keyword"] if keyword_comparisons else "SaaS"

    next_tests.append(f"{fmt_label} + {hook} 훅 + '{primary_kw}' Benefit 제목 — 30초/3분 A/B")
    next_tests.append(f"질문형 vs How-to 제목 2종 — {best_category['category_name'] if best_category else 'Science & Technology'} 카테고리")
    if trending_tags:
        next_tests.append(
            f"트렌딩 태그 {trending_tags[0][0]} + 마케팅 태그 #b2b #리드gen 조합 테스트"
        )
    next_tests.append("Shorts 훅 15초 → Long-form 설명 3분 리타겟 콘텐츠 페어링")

    shorts_pct = fmt.get("shorts_pct", 0)
    avg_eng = round(float(trending_df["engagement_rate"].mean()), 2) if len(trending_df) else 0

    kw_summary = ""
    if keyword_comparisons:
        first = keyword_comparisons[0]
        if first.get("keyword_count", 0) > 0:
            kw_summary = (
                f" · 마케팅 키워드 '{first['keyword']}' engagement는 "
                f"트렌딩 대비 {first['engagement_gap']:+.3f}%p"
            )

    summary = (
        f"KR 트렌딩 {len(trending_df)}개 · Shorts {shorts_pct}% · "
        f"평균 engagement {avg_eng}%{kw_summary} — "
        f"{best_category['category_name'] if best_category else '상위 카테고리'} + "
        f"{hook} 조합을 다음 콘텐츠 방향으로 제안합니다."
        if len(trending_df)
        else "트렌딩 데이터를 기준으로 카테고리·포맷·훅 패턴을 비교해 Content Brief를 생성합니다."
    )

    return {
        "summary": summary,
        "recommendations": recommendations[:6],
        "next_tests": next_tests[:4],
        "comparison": comparison,
        "format_comparison": fmt,
        "category_mix": cat_mix.to_dict(orient="records") if not cat_mix.empty else [],
        "keyword_comparisons": keyword_comparisons,
    }


def brief_to_markdown(brief: dict) -> str:
    lines = [
        "# YouTube KR Content Brief",
        "",
        brief["summary"],
        "",
        "## 추천 방향",
    ]
    for item in brief["recommendations"]:
        lines.append(f"- {item}")

    lines.extend(["", "## 다음 콘텐츠 테스트"])
    for item in brief["next_tests"]:
        lines.append(f"- {item}")

    return "\n".join(lines)
