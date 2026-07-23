#!/usr/bin/env python3
"""Generate the three role-specific Korean resume PDFs used by the portfolio."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.request import urlopen

from fontTools.ttLib import TTFont as FontToolsFont
from fontTools.varLib.instancer import instantiateVariableFont
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
FONT_SOURCE = ROOT / "tmp/pdfs/fonts/NotoSansKR.ttf"
FONT_DIR = ROOT / "tmp/pdfs/fonts/generated"
OUTPUT_DIR = ROOT / "public/files"

NAVY = colors.HexColor("#12233F")
BLUE = colors.HexColor("#3668D8")
INK = colors.HexColor("#1A2433")
MUTED = colors.HexColor("#5E6B7D")
LINE = colors.HexColor("#DCE3EE")
SOFT = colors.HexColor("#F4F7FB")
WHITE = colors.white

SITE = "https://banseok-kang1.github.io/Growth/"
FONT_URL = (
    "https://raw.githubusercontent.com/google/fonts/main/ofl/notosanskr/"
    "NotoSansKR%5Bwght%5D.ttf"
)
EMAIL = "kangbs2486@gmail.com"
PHONE = "010-9630-2486"


@dataclass(frozen=True)
class Evidence:
    title: str
    detail: str
    url: str
    badge: str


@dataclass(frozen=True)
class Track:
    filename: str
    label: str
    role: str
    target: str
    summary: str
    contribution: str
    strengths: tuple[str, ...]
    evidence: tuple[Evidence, ...]
    project_order: tuple[str, ...]
    fit_note: str


TRACKS = (
    Track(
        filename="kang-banseok-resume-growth-operations.pdf",
        label="GROWTH OPERATIONS / MARKETING ANALYTICS",
        role="Growth Operations · Marketing Analytics",
        target="성장 문제·측정 기준·실행 우선순위를 연결하는 포지션",
        summary=(
            "광고·사용자 행동·전환 데이터를 연결해 성과가 끊기는 지점을 정의하고, "
            "팀이 바로 움직일 수 있는 측정 기준과 다음 액션으로 바꿉니다."
        ),
        contribution=(
            "마케팅 실무의 맥락과 데이터 구조를 함께 이해해, 흩어진 지표를 공통 언어로 정리하고 "
            "운영·콘텐츠·CRM·제품 사이의 우선순위를 명확하게 만들 수 있습니다."
        ),
        strengths=(
            "문제 → 이벤트 → 지표 → 판단 → 액션의 공통 의사결정 구조 설계",
            "GA4·GTM·UTM 기반 사용자 행동과 전환 단계 측정",
            "Raw 데이터와 대시보드를 연결해 리드 품질·후속 전환까지 해석",
            "API·Python·Streamlit으로 반복 분석을 도구화하고 실행안으로 전환",
        ),
        evidence=(
            Evidence(
                "Marketing Lead Funnel Dashboard",
                "Lead → Qualified Lead → Meeting → Revenue 의사결정 구조",
                SITE + "projects/marketing-lead-dashboard/",
                "1인 프로젝트",
            ),
            Evidence(
                "GA4/GTM/UTM 전환 측정 구조",
                "문의 클릭·폼 진입·제출 완료 이벤트 분리",
                SITE + "cases/ga4-gtm-tracking-system/",
                "실무 기반",
            ),
            Evidence(
                "글로벌 앱 그로스 퍼널",
                "국가·채널별 설치 → 참여 → 예약 전환 흐름",
                SITE + "cases/global-app-growth-funnel/",
                "실무 기반",
            ),
        ),
        project_order=("dashboard", "youtube", "meta"),
        fit_note=(
            "퍼포먼스 마케팅 경험은 측정 감각과 비즈니스 맥락을 만든 실무 기반입니다. 지원 정체성은 "
            "매체 운영 자체보다 성장 문제 정의·데이터 구조·의사결정 운영에 둡니다."
        ),
    ),
    Track(
        filename="kang-banseok-resume-crm-ops.pdf",
        label="CRM / MARKETING OPS",
        role="CRM / Marketing Operations",
        target="광고 유입 이후 전환 누수를 줄이는 포지션",
        summary=(
            "광고 이후 문의 미완료, 미팅 미진행, 구매 미전환 구간을 세그먼트로 나누고 "
            "메시지·지표·판단 기준을 설계합니다."
        ),
        contribution=(
            "실무 측정 경험과 프로젝트형 CRM 설계를 결합해, 리드 상태값·캠페인·후속 전환을 "
            "연결하는 운영 구조를 제안할 수 있습니다."
        ),
        strengths=(
            "UTM·이벤트명·리포트 기준 문서화 및 표준화",
            "퍼널 단계별 이탈 세그먼트와 후속 메시지 가설 설계",
            "오픈율·CTR·미팅 전환율 중심 CRM 실험 지표 정의",
            "Sheets·Looker Studio·SQL·Python 기반 데이터 구조화",
        ),
        evidence=(
            Evidence(
                "CRM/그로스 실험 시나리오",
                "Segment → Hypothesis → Message → Metric → Decision",
                SITE + "cases/crm-retention-scenario/",
                "설계 프로젝트",
            ),
            Evidence(
                "GA4/GTM/UTM 전환 측정 구조",
                "광고 캠페인과 리드 이벤트를 같은 기준으로 연결",
                SITE + "cases/ga4-gtm-tracking-system/",
                "실무 기반",
            ),
            Evidence(
                "Marketing Lead Funnel Dashboard",
                "Lead → Qualified Lead → Meeting → Revenue 구조",
                SITE + "projects/marketing-lead-dashboard/",
                "1인 프로젝트",
            ),
        ),
        project_order=("crm", "meta", "youtube"),
        fit_note=(
            "HubSpot/Salesforce 실운영 성과를 주장하지 않습니다. 현재 강점은 광고 측정 기반의 "
            "세그먼트·리드 상태값·CRM 실험 구조 설계입니다."
        ),
    ),
    Track(
        filename="kang-banseok-resume-growth-product.pdf",
        label="GROWTH PM / PRODUCT ANALYTICS",
        role="Growth PM / Product Analytics",
        target="문제·지표·실험·우선순위를 구조화하는 포지션",
        summary=(
            "사용자가 어디서 멈추는지 퍼널로 정의하고, 대표 지표와 트레이드오프를 기준으로 "
            "다음 실험의 우선순위를 정합니다."
        ),
        contribution=(
            "마케팅 실무에서 익힌 측정 감각과 개인 프로젝트의 문제정의 프레임을 바탕으로, "
            "마케팅·데이터·제품 사이의 판단 기준을 정리할 수 있습니다."
        ),
        strengths=(
            "유입 → 활성화 → 전환 퍼널의 병목 단계 정의",
            "가설 → 이벤트 → 지표 → 판단 기준으로 실험 구조화",
            "단기 전환과 리텐션의 트레이드오프 명시",
            "API·Python·Streamlit을 활용한 분석 도구 기획·구현",
        ),
        evidence=(
            Evidence(
                "글로벌 앱 그로스 퍼널",
                "국가·채널별 설치 → 참여 → 예약 전환 흐름",
                SITE + "cases/global-app-growth-funnel/",
                "실무 기반",
            ),
            Evidence(
                "CRM/그로스 실험 시나리오",
                "세그먼트별 실험 가설과 의사결정 기준",
                SITE + "cases/crm-retention-scenario/",
                "설계 프로젝트",
            ),
            Evidence(
                "Marketing Keyword Gap → Shoot Brief",
                "API 데이터에서 이번 주 콘텐츠 액션 도출",
                SITE + "projects/youtube-trend-analyzer/",
                "1인 프로젝트",
            ),
        ),
        project_order=("youtube", "meta", "crm"),
        fit_note=(
            "정식 PM 경력이나 실제 서비스 A/B 테스트 성과를 주장하지 않습니다. 실무 측정 경험과 "
            "프로젝트에서 검증 가능한 문제정의·지표 설계·도구 구현 범위를 제시합니다."
        ),
    ),
)


EXPERIENCE_BULLETS = (
    "Meta·Google·Naver·TikTok 채널별 비용·CPA·리드 품질을 비교해 예산 유지·축소·확장 후보 도출",
    "UTM 규칙과 GTM 이벤트를 정리하고 GA4에서 문의 클릭·폼 진입·제출 완료를 구분",
    "CPA 단독이 아닌 진성문의율·미팅 전환율까지 포함해 월 3,800만 원 이상 규모 캠페인 분석",
    "소재·타깃·랜딩 조합별 성과 변화를 정리해 테스트 우선순위 및 개선안 작성",
    "날짜·매체·캠페인 기준 Raw 통합 및 Sheets·Looker Studio 리포트 구조 설계",
    "Airbridge 이벤트 구조를 검토하고 국가·채널별 설치 → 예약 전환 분석 흐름 정리",
)


PROJECTS = {
    "dashboard": (
        "Marketing Lead Funnel Dashboard",
        "2026 · 1인 기획·개발",
        "광고비와 표면 전환에 머물지 않고 Lead → Qualified Lead → Meeting → Revenue를 연결해 병목과 다음 액션을 판단하는 대시보드.",
        SITE + "projects/marketing-lead-dashboard/",
    ),
    "meta": (
        "Meta Creative Intelligence",
        "2025 – 2026 · 1인 기획·개발",
        "Meta Marketing API의 소재 메타와 성과 지표를 결합해 포맷·훅·CTA별 CPA 패턴을 분석하고 다음 제작 방향을 제안하는 Streamlit 앱.",
        SITE + "projects/meta-creative-intelligence/",
    ),
    "youtube": (
        "Marketing Keyword Gap → Shoot Brief",
        "2025 · 1인 기획·개발",
        "YouTube Data API로 대중 트렌드와 마케팅 키워드의 차이를 분석하고 포맷·훅·제목·태그가 담긴 촬영 브리프를 생성.",
        SITE + "projects/youtube-trend-analyzer/",
    ),
    "crm": (
        "CRM/그로스 실험 시나리오",
        "2026 · 개인 프로젝트 · 실제 발송 성과 아님",
        "문의 미완료·미팅 미진행·미구매 세그먼트별 메시지 가설과 오픈율·CTR·미팅 전환율 판단 기준을 설계.",
        SITE + "cases/crm-retention-scenario/",
    ),
}


def build_fonts() -> None:
    if not FONT_SOURCE.exists():
        FONT_SOURCE.parent.mkdir(parents=True, exist_ok=True)
        with urlopen(FONT_URL, timeout=60) as response:
            FONT_SOURCE.write_bytes(response.read())
    FONT_DIR.mkdir(parents=True, exist_ok=True)
    for weight, filename in ((400, "NotoSansKR-Regular.ttf"), (700, "NotoSansKR-Bold.ttf")):
        target = FONT_DIR / filename
        if not target.exists():
            font = FontToolsFont(str(FONT_SOURCE))
            instance = instantiateVariableFont(font, {"wght": weight}, inplace=False)
            instance.save(str(target))
    pdfmetrics.registerFont(TTFont("NotoKR", str(FONT_DIR / "NotoSansKR-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("NotoKR-Bold", str(FONT_DIR / "NotoSansKR-Bold.ttf")))


def styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name",
            parent=base["Title"],
            fontName="NotoKR-Bold",
            fontSize=23,
            leading=27,
            textColor=NAVY,
            spaceAfter=2,
        ),
        "role": ParagraphStyle(
            "Role",
            parent=base["Normal"],
            fontName="NotoKR-Bold",
            fontSize=13,
            leading=17,
            textColor=BLUE,
            spaceAfter=6,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName="NotoKR",
            fontSize=8.2,
            leading=12,
            textColor=MUTED,
        ),
        "kicker": ParagraphStyle(
            "Kicker",
            parent=base["Normal"],
            fontName="NotoKR-Bold",
            fontSize=7.5,
            leading=10,
            textColor=BLUE,
            spaceAfter=4,
        ),
        "title": ParagraphStyle(
            "SectionTitle",
            parent=base["Heading2"],
            fontName="NotoKR-Bold",
            fontSize=13,
            leading=17,
            textColor=NAVY,
            spaceBefore=5,
            spaceAfter=7,
        ),
        "heading": ParagraphStyle(
            "Heading",
            parent=base["Heading3"],
            fontName="NotoKR-Bold",
            fontSize=10.5,
            leading=14,
            textColor=INK,
            spaceAfter=3,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName="NotoKR",
            fontSize=8.7,
            leading=13.2,
            textColor=INK,
            alignment=TA_LEFT,
            wordWrap="CJK",
            spaceAfter=5,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=base["BodyText"],
            fontName="NotoKR",
            fontSize=7.7,
            leading=11.3,
            textColor=MUTED,
            wordWrap="CJK",
        ),
        "small_bold": ParagraphStyle(
            "SmallBold",
            parent=base["BodyText"],
            fontName="NotoKR-Bold",
            fontSize=8,
            leading=11.5,
            textColor=INK,
            wordWrap="CJK",
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["BodyText"],
            fontName="NotoKR",
            fontSize=8.4,
            leading=12.7,
            leftIndent=10,
            firstLineIndent=-7,
            bulletIndent=0,
            textColor=INK,
            wordWrap="CJK",
            spaceAfter=3,
        ),
        "quote": ParagraphStyle(
            "Quote",
            parent=base["BodyText"],
            fontName="NotoKR-Bold",
            fontSize=10,
            leading=15,
            textColor=NAVY,
            wordWrap="CJK",
        ),
    }


class ResumeDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, title: str):
        super().__init__(
            filename,
            pagesize=A4,
            leftMargin=15 * mm,
            rightMargin=15 * mm,
            topMargin=14 * mm,
            bottomMargin=15 * mm,
            title=title,
            author="강반석",
            subject="직무별 이력서",
        )
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="resume",
        )
        self.addPageTemplates(PageTemplate(id="resume", frames=frame, onPage=draw_page))


def draw_page(canvas, doc) -> None:
    canvas.saveState()
    width, _ = A4
    canvas.setStrokeColor(LINE)
    canvas.line(15 * mm, 10 * mm, width - 15 * mm, 10 * mm)
    canvas.setFont("NotoKR", 7)
    canvas.setFillColor(MUTED)
    canvas.drawString(15 * mm, 6.5 * mm, "강반석 · Growth Operations Portfolio")
    canvas.drawRightString(width - 15 * mm, 6.5 * mm, f"{doc.page} / 2")
    canvas.restoreState()


def bullet_list(items: Iterable[str], s: dict[str, ParagraphStyle]):
    return [Paragraph(f"• {item}", s["bullet"]) for item in items]


def section_header(kicker: str, title: str, s: dict[str, ParagraphStyle]):
    return [
        KeepTogether(
            [
                Spacer(1, 3 * mm),
                Paragraph(kicker, s["kicker"]),
                Paragraph(title, s["title"]),
                HRFlowable(width="100%", thickness=0.7, color=LINE, spaceAfter=7),
            ]
        )
    ]


def evidence_table(track: Track, s: dict[str, ParagraphStyle]):
    rows = []
    for item in track.evidence:
        rows.append(
            [
                Paragraph(item.badge, s["small_bold"]),
                Paragraph(
                    f'<link href="{item.url}" color="#3668D8"><b>{item.title}</b></link><br/>{item.detail}',
                    s["small"],
                ),
            ]
        )
    table = Table(rows, colWidths=[27 * mm, 144 * mm], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, -1), SOFT),
                ("BOX", (0, 0), (-1, -1), 0.6, LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.4, LINE),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return table


def build_story(track: Track, s: dict[str, ParagraphStyle]):
    story = [
        Paragraph("강반석", s["name"]),
        Paragraph(track.role, s["role"]),
        Paragraph(
            f'서울 관악구 · <link href="mailto:{EMAIL}" color="#3668D8">{EMAIL}</link> · {PHONE}<br/>'
            f'<link href="{SITE}" color="#3668D8">banseok-kang1.github.io/Growth</link> · '
            '<link href="https://github.com/BANSEOK-KANG1" color="#3668D8">github.com/BANSEOK-KANG1</link>',
            s["contact"],
        ),
        Spacer(1, 6 * mm),
        Table(
            [
                [
                    Paragraph(track.label, s["kicker"]),
                    Paragraph(track.target, s["small_bold"]),
                ],
                [Paragraph(track.summary, s["quote"]), ""],
                [
                    Paragraph("<b>입사 후 기여</b>", s["small_bold"]),
                    Paragraph(track.contribution, s["small"]),
                ],
            ],
            colWidths=[35 * mm, 136 * mm],
            style=TableStyle(
                [
                    ("SPAN", (0, 1), (1, 1)),
                    ("BACKGROUND", (0, 0), (-1, -1), SOFT),
                    ("BOX", (0, 0), (-1, -1), 0.8, LINE),
                    ("LINEBELOW", (0, 1), (-1, 1), 0.5, LINE),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 9),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                    ("TOPPADDING", (0, 0), (-1, -1), 8),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ]
            ),
        ),
        *section_header("CORE STRENGTHS", "이 포지션에서 먼저 보여줄 역량", s),
        *bullet_list(track.strengths, s),
        *section_header("VERIFIABLE EVIDENCE", "포트폴리오와 1:1로 연결되는 증거", s),
        evidence_table(track, s),
        *section_header("WORK EXPERIENCE", "글로벌알파미디어 · 퍼포먼스 마케터", s),
        Paragraph(
            "<b>2025.12 – 2026</b> · 해외 타깃 리드형 캠페인을 멀티채널로 운영하고, "
            "광고 클릭 이후 문의·진성문의·미팅 전환까지 판단할 수 있도록 측정 및 리포팅 구조를 정리했습니다.",
            s["body"],
        ),
        *bullet_list(EXPERIENCE_BULLETS, s),
        PageBreak(),
        Paragraph(track.label, s["kicker"]),
        Paragraph("프로젝트 · 도구 · 판단 원칙", s["title"]),
        HRFlowable(width="100%", thickness=0.8, color=LINE, spaceAfter=8),
        Paragraph(
            "아래 프로젝트는 회사 경력과 분리해 표시합니다. 실제 운영 성과가 아닌 경우 기획·구현 범위와 한계를 명시했습니다.",
            s["body"],
        ),
    ]

    for key in track.project_order:
        title, meta, detail, url = PROJECTS[key]
        story.extend(
            [
                KeepTogether(
                    [
                        Spacer(1, 3 * mm),
                        Paragraph(f'<link href="{url}" color="#3668D8">{title}</link>', s["heading"]),
                        Paragraph(meta, s["small"]),
                        Paragraph(detail, s["body"]),
                        HRFlowable(width="100%", thickness=0.45, color=LINE, spaceAfter=2),
                    ]
                )
            ]
        )

    tool_rows = [
        ["광고 운영", "Meta Ads · Google Ads · Naver Search Ads · TikTok Ads"],
        ["측정·분석", "GA4 · GTM · UTM · Microsoft Clarity · Airbridge"],
        ["데이터·리포팅", "SQL · Python(pandas) · Google Sheets · Excel · Looker Studio"],
        ["기획·제작", "Figma · Photoshop · Notion · GitHub · Streamlit"],
    ]
    story.extend(
        [
            *section_header("TOOLS BY USE", "숙련도 퍼센트 대신 실제 활용 맥락", s),
            Table(
                [
                    [Paragraph(f"<b>{label}</b>", s["small_bold"]), Paragraph(tools, s["small"])]
                    for label, tools in tool_rows
                ],
                colWidths=[35 * mm, 136 * mm],
                style=TableStyle(
                    [
                        ("BOX", (0, 0), (-1, -1), 0.6, LINE),
                        ("INNERGRID", (0, 0), (-1, -1), 0.4, LINE),
                        ("BACKGROUND", (0, 0), (0, -1), SOFT),
                        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 7),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                        ("TOPPADDING", (0, 0), (-1, -1), 6),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                    ]
                ),
            ),
            *section_header("BACKGROUND", "고객 커뮤니케이션 · 제작 이해 · 학력", s),
            *bullet_list(
                (
                    "요기요 영업 1년 — 고객 니즈 파악·서비스 가치 설명·관계 관리",
                    "삼성생명 SFP 6개월 — 1:1 상담·제안 커뮤니케이션",
                    "웹디자인 경험 — 랜딩·소재 수정 요청을 제작 관점에서 구체화",
                    "경상국립대학교 동물생명과학전공 졸업",
                ),
                s,
            ),
            *section_header("TRANSPARENCY", "경력과 프로젝트의 경계를 명확히 표시", s),
            Table(
                [[Paragraph(track.fit_note, s["small"])]],
                colWidths=[171 * mm],
                style=TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, -1), SOFT),
                        ("BOX", (0, 0), (-1, -1), 0.8, LINE),
                        ("LEFTPADDING", (0, 0), (-1, -1), 10),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                        ("TOPPADDING", (0, 0), (-1, -1), 8),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                    ]
                ),
            ),
            Spacer(1, 6 * mm),
            Table(
                [
                    [
                        Paragraph("<b>Portfolio</b><br/>문제 → 지표 → 판단 → 액션 → 한계", s["small"]),
                        Paragraph(
                            f'<link href="{SITE}" color="#3668D8">{SITE}</link><br/>'
                            '<link href="https://github.com/BANSEOK-KANG1" color="#3668D8">'
                            "github.com/BANSEOK-KANG1</link>",
                            s["small"],
                        ),
                    ]
                ],
                colWidths=[72 * mm, 99 * mm],
                style=TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
                        ("TEXTCOLOR", (0, 0), (-1, -1), WHITE),
                        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 10),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                        ("TOPPADDING", (0, 0), (-1, -1), 9),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
                    ]
                ),
            ),
        ]
    )
    return story


def generate() -> None:
    build_fonts()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    resume_styles = styles()
    for track in TRACKS:
        target = OUTPUT_DIR / track.filename
        doc = ResumeDocTemplate(str(target), f"강반석 - {track.role}")
        doc.build(build_story(track, resume_styles))
        print(target.relative_to(ROOT))


if __name__ == "__main__":
    generate()
