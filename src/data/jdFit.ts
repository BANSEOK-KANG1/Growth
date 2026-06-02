export type JdFitStatus = 'strong' | 'partial' | 'gap';

export type JdFitEntry = {
  id: string;
  jdKeyword: string;
  status: JdFitStatus;
  headline: string;
  evidence: string;
  caseSlug?: string;
  resumeBullet: string;
  coverLetterHook: string;
  gapNote?: string;
};

export type CoverLetterSection = {
  id: string;
  title: string;
  paragraphs: string[];
};

export const jdFitEntries: JdFitEntry[] = [
  {
    id: 'ga4-analytics',
    jdKeyword: 'GA4 또는 유사 웹 분석 툴 활용',
    status: 'strong',
    headline: '광고 클릭 이후 전환까지 GA4/GTM으로 퍼널을 직접 설계',
    evidence:
      '글로벌알파미디어 실무 — UTM 표준화, 문의 클릭→폼 진입→제출 완료 이벤트 분리. GA4/GTM 측정 구조 케이스 스터디.',
    caseSlug: 'ga4-gtm-tracking-system',
    resumeBullet:
      'GA4/GTM 기반 문의 전환 퍼널(클릭→폼→제출) 설계 — 매체별 성과를 동일 지표로 비교',
    coverLetterHook:
      '광고비를 쓰는데 어떤 매체가 실제 전환을 만드는지 모르는 상태가 가장 먼저 해결해야 할 문제였습니다. UTM 규칙 표준화와 GTM 이벤트 분리로 퍼널을 보이게 만들었습니다.'
  },
  {
    id: 'hypothesis-ab',
    jdKeyword: '데이터 기반 가설 설정 → A/B 테스트 → 개선 사이클',
    status: 'strong',
    headline: '가설→측정→개선 루프를 실무·프로젝트 모두에서 반복',
    evidence:
      '실무: 소재·랜딩·타깃 A/B식 운영. CRM 케이스: Segment→Hypothesis→Message→Metric 실험 설계. A/B Test Design 85%.',
    caseSlug: 'crm-retention-scenario',
    resumeBullet:
      '소재·랜딩·타깃 조합 A/B식 운영 — CPA·CVR 변화를 숫자로 개선안 작성',
    coverLetterHook:
      "감으로 '잘 될 것 같다'가 아니라, 가설→측정→개선을 주간 리뷰 리듬으로 반복했습니다. 퍼포먼스 실무와 CRM 실험 설계 모두 같은 프레임으로 접근합니다."
  },
  {
    id: 'spreadsheet-sql',
    jdKeyword: '스프레드시트 고급 활용 또는 SQL 기초 이상',
    status: 'strong',
    headline: 'Raw 통합 구조 설계 + Sheets/Looker Studio 리포트 자동화',
    evidence:
      '날짜·매체·캠페인 기준 통합 Raw 데이터 구조. SQL 78%, Python pandas, Looker Studio 75%. Olist ETL 프로젝트.',
    caseSlug: 'performance-funnel-analysis',
    resumeBullet:
      '날짜·매체·캠페인 기준 Raw 통합 구조 설계 — Sheets/Looker Studio 리포트 자동화',
    coverLetterHook:
      '매체별 대시보드 숫자를 그대로 믿지 않고, 하나의 Raw 파일로 연결해 판단 기준을 통일했습니다. SQL과 스프레드시트로 리포트 구조를 직접 설계합니다.'
  },
  {
    id: 'education',
    jdKeyword: '대학교 졸업(4년) 이상',
    status: 'strong',
    headline: '경상국립대학교 동물생명과학전공 졸업',
    evidence: '4년제 대학 졸업 — 학력 요건 충족',
    resumeBullet: '경상국립대학교 동물생명과학전공 졸업',
    coverLetterHook: '4년제 대학을 졸업했으며, 이후 퍼포먼스·데이터 기반 마케팅 역량을 실무와 프로젝트로 쌓았습니다.'
  },
  {
    id: 'b2b-funnel',
    jdKeyword: 'B2B 마케팅 환경 퍼널 전환 분석 (필수)',
    status: 'partial',
    headline: '리드형 퍼널 — CPA + 진성문의율 + 미팅 전환율 기준 판단',
    evidence:
      '실무는 B2C·리드형 캠페인이나, B2B 리드형과 동일한 문의→상담→전환 판단 프레임 적용. 월 ₩3,800만+ 규모 채널별 비교.',
    caseSlug: 'performance-funnel-analysis',
    resumeBullet:
      '리드형 마케팅 — CPA + 진성문의율 + 미팅 전환율 기준 채널별 예산 판단',
    coverLetterHook:
      'B2B SaaS만 다룬 것은 아니지만, 문의→진성 리드→미팅 전환으로 이어지는 리드형 퍼널 판단 구조는 동일하게 적용해 왔습니다. CPA 하나만 보지 않고 리드 품질까지 함께 봅니다.',
    gapNote:
      '"B2B 3년" 대신 → B2B 리드형과 동일한 문의→상담→전환 판단 프레임을 B2C·리드 캠페인에서 실무 적용'
  },
  {
    id: 'crm-mql',
    jdKeyword: 'CRM 데이터 연계 분석 및 MQL 관리',
    status: 'partial',
    headline: '퍼널 단계별 이탈 세그먼트 + CRM 메시지·지표 설계',
    evidence:
      'CRM/그로스 실험 시나리오 — 문의 미완료·미팅 미진행·미구매 세그먼트, 리드 상태값 기반 후속 액션 설계.',
    caseSlug: 'crm-retention-scenario',
    resumeBullet:
      '퍼널 단계별 이탈 세그먼트 정의 및 CRM 메시지·측정 지표 설계 (그로스 실험 프로젝트)',
    coverLetterHook:
      '광고로 유입한 뒤 어디서 이탈하는지 세그먼트로 나누고, 각 단계에 맞는 메시지와 측정 지표를 설계했습니다. MQL 툴 실운영보다 리드→후속 전환 연결 설계에 강점이 있습니다.',
    gapNote:
      'HubSpot/Salesforce MQL 실운영 경험 없음 → "MQL 관리" 대신 리드 상태값 기반 후속 전환 설계 역량 강조'
  },
  {
    id: 'google-search-ads',
    jdKeyword: 'Google Ads 실운영 (검색광고 최소 1년 이상)',
    status: 'partial',
    headline: 'Meta·Google·Naver·TikTok 멀티채널 — 채널별 CPA·리드 품질 비교',
    evidence:
      'Google Ads 포함 멀티채널 운영. 케이스에서 Google Spend ₩0.7M — Meta/Naver 대비 비중 낮음. 검색 vs 디스플레이 vs SNS 성과 차이 데이터 판단.',
    caseSlug: 'performance-funnel-analysis',
    resumeBullet:
      'Meta·Google·Naver·TikTok 멀티채널 운영 — 채널별 CPA·리드 품질 비교 후 예산 재배분',
    coverLetterHook:
      'Google을 포함한 멀티채널에서 검색·디스플레이·SNS 매체별 CPA와 리드 품질 차이를 비교해 예산을 재배분했습니다. 검색 단독 1년+보다 채널 간 성과 판단 역량을 강조합니다.',
    gapNote:
      '"검색 1년+" 주장 금지 → Google 포함 멀티채널에서 검색 vs 디스플레이 vs SNS 성과 차이를 데이터로 판단'
  },
  {
    id: 'experience-years',
    jdKeyword: '경력 2년 이상 · B2B 디지털/그로스 마케팅 3년+',
    status: 'gap',
    headline: '실무 1년+ — 측정·퍼널·실험 설계로 빠른 기여 가능',
    evidence:
      '글로벌알파미디어 2025–2026 퍼포먼스 실무. 케이스 4개 + API 분석 앱 2개로 역량 보완.',
    resumeBullet:
      '인하우스 기여 가능 영역: 측정 인프라(GA4/GTM) + 리드 품질 판단 + Raw 리포트 구조',
    coverLetterHook:
      '실무 연차는 JD 요건에 미달하지만, 측정 구조 설계·리드 품질 판단·가설 기반 개선은 현장에서 바로 기여할 수 있는 영역입니다. 케이스와 Live Demo로 판단력을 보완했습니다.',
    gapNote:
      '경력 연차는 솔직히 인정. 대신 측정 인프라 + 리드 품질 판단 + Marketing Ops 적성( API·Streamlit )으로 차별화'
  }
];

export const coverLetterSections: CoverLetterSection[] = [
  {
    id: 'problem',
    title: 'P1 — 문제의식',
    paragraphs: [
      '퍼포먼스 마케팅 현장에서 가장 먼저 마주한 문제는 "클릭은 나는데 왜 문의가 안 오지?"였습니다. 매체별 대시보드 숫자는 좋아 보였지만, 광고 클릭 이후 실제 전환까지 이어지는 흐름이 보이지 않았습니다.',
      '저는 광고 집행보다 먼저 측정 구조부터 고쳤습니다. UTM 네이밍 규칙을 표준화하고, GA4/GTM으로 문의하기 클릭→폼 진입→제출 완료를 이벤트로 분리해 매체별 성과를 동일 기준으로 비교할 수 있게 만들었습니다.'
    ]
  },
  {
    id: 'methodology',
    title: 'P2 — 방법론',
    paragraphs: [
      '성과 개선은 감이 아니라 가설→측정→개선 사이클로 접근합니다. 실무에서 소재·랜딩·타깃 조합을 A/B식으로 운영하며 CPA·CVR 변화를 숫자로 개선안을 작성했고, CRM 실험 프로젝트에서는 퍼널 단계별 이탈 세그먼트에 맞는 메시지와 측정 지표를 설계했습니다.',
      'CPA 하나만 보면 놓치는 것이 있습니다. 진성문의율과 미팅 전환율을 함께 봐야 실제 성과를 판단할 수 있었고, 이 프레임으로 채널별 예산 유지·축소·확장 후보를 도출했습니다.'
    ]
  },
  {
    id: 'contribution',
    title: 'P3 — 기여',
    paragraphs: [
      '저는 광고를 단순히 집행하는 마케터가 아니라, 광고비가 어디서 성과로 이어지고 어디서 새는지 추적해 다음 액션으로 바꾸는 그로스 마케터입니다.',
      '인하우스에서 퍼널 측정·리드 품질 판단·CRM 실험 설계를 하나의 성장 흐름으로 연결하는 역할을 지향합니다. Meta Marketing API 기반 소재 분석 앱 등 데이터 도구를 직접 만들며 Marketing Ops 역량도 함께 가져갑니다.'
    ]
  }
];

export const gapResponseNote =
  '경력 연차·MQL 툴 실운영·Google 검색 1년+는 JD와 갭이 있습니다. 자소서에서는 짧게 인정한 뒤, 측정 인프라·리드 품질 판단·가설 기반 개선 역량으로 차별화하세요.';

export const statusLabels: Record<JdFitStatus, string> = {
  strong: '강점',
  partial: '부분 매칭',
  gap: '갭 · 대안 프레이밍'
};
