"""Generate creative direction briefs from performance patterns."""

from __future__ import annotations

import pandas as pd

from analyze import aggregate_by_dimension, compare_top_bottom


CTA_LABELS = {
    "CONTACT_US": "문의하기",
    "LEARN_MORE": "더 알아보기",
    "SIGN_UP": "가입하기",
    "DOWNLOAD": "다운로드",
    "NONE": "CTA 없음",
}


def build_direction_brief(df: pd.DataFrame) -> dict:
    comparison = compare_top_bottom(df)
    format_stats = aggregate_by_dimension(df, "format_tag")
    hook_stats = aggregate_by_dimension(df, "hook_keyword")
    cta_stats = aggregate_by_dimension(df, "call_to_action_type")

    best_format = _best_row(format_stats, "format_tag")
    best_hook = _best_row(hook_stats, "hook_keyword")
    best_cta = _best_row(cta_stats, "call_to_action_type")

    recommendations: list[str] = []

    if best_format:
        recommendations.append(
            f"포맷: {best_format['format_tag']} 소재가 평균 CPA {int(best_format['avg_cpa']):,}원으로 가장 효율적입니다."
        )
    if best_hook:
        recommendations.append(
            f"훅: {best_hook['hook_keyword']} 메시지가 CTR {best_hook['avg_ctr']}% · CVR {best_hook['avg_cvr']}% 기준 상위입니다."
        )
    if best_cta:
        cta_label = CTA_LABELS.get(best_cta["call_to_action_type"], best_cta["call_to_action_type"])
        recommendations.append(f"CTA: {cta_label}({best_cta['call_to_action_type']}) 조합을 우선 테스트하세요.")

    if comparison.get("top_format") and comparison.get("bottom_format"):
        if comparison["top_format"] != comparison["bottom_format"]:
            recommendations.append(
                f"상위 25%는 {comparison['top_format']} 중심, 하위 25%는 {comparison['bottom_format']} 비중이 높습니다."
            )

    next_tests = _next_test_ideas(comparison, best_format, best_hook, best_cta)

    summary = (
        f"CPA 상위 그룹 평균 {comparison.get('top_avg_cpa'):,.0f}원 vs "
        f"하위 그룹 {comparison.get('bottom_avg_cpa'):,.0f}원 — "
        f"{best_format['format_tag'] if best_format else 'Video'} + "
        f"{best_hook['hook_keyword'] if best_hook else '질문형'} 조합을 다음 소재 방향으로 제안합니다."
        if comparison.get("top_avg_cpa")
        else "성과 데이터를 기준으로 포맷·훅·CTA 패턴을 비교해 다음 테스트 방향을 도출합니다."
    )

    return {
        "summary": summary,
        "recommendations": recommendations,
        "next_tests": next_tests,
        "comparison": comparison,
        "best_format": best_format,
        "best_hook": best_hook,
        "best_cta": best_cta,
    }


def _best_row(stats: pd.DataFrame, col: str) -> dict | None:
    if stats.empty:
        return None
    row = stats.iloc[0]
    return row.to_dict()


def _next_test_ideas(
    comparison: dict,
    best_format: dict | None,
    best_hook: dict | None,
    best_cta: dict | None,
) -> list[str]:
    ideas: list[str] = []

    fmt = best_format["format_tag"] if best_format else "Video"
    hook = best_hook["hook_keyword"] if best_hook else "질문형"
    cta = best_cta["call_to_action_type"] if best_cta else "CONTACT_US"
    cta_label = CTA_LABELS.get(cta, cta)

    ideas.append(f"{fmt} + {hook} 훅 + {cta_label} CTA — 기존 상위 패턴 변형 A/B")
    ideas.append(f"{fmt} + How-to 훅 — 3단계 설명형 영상 15초/30초 버전")
    ideas.append("하위 성과 Image/일반 훅 소재 예산 축소 → 상위 패턴으로 재배분")

    if comparison.get("top_hook") == "질문형":
        ideas.append("질문형 훅 변형: Pain point 질문 vs Benefit 질문 2종 동시 테스트")

    return ideas[:4]
