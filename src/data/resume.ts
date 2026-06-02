export type ResumeEntry = {
  period: string;
  category: string;
  title: string;
  company?: string;
  description: string;
  bullets?: string[];
};

export const resumeTimeline: ResumeEntry[] = [
  {
    period: '2025 – 2026',
    category: 'Performance Marketing',
    company: '글로벌알파미디어',
    title: '퍼포먼스마케터',
    description:
      '해외 타깃 리드형 캠페인을 Meta·Google·Naver·TikTok에서 운영하며, GA4/GTM 기반 전환 측정과 리드 품질 판단을 연결했습니다. CPA 단독이 아닌 진성문의율·미팅 전환율까지 함께 보고 예산 판단 후보를 도출했습니다.',
    bullets: [
      'Meta·Google·Naver·TikTok 멀티채널 운영 — 채널별 CPA·리드 품질 비교 후 예산 재배분',
      'GA4/GTM으로 문의 클릭→폼 진입→제출 완료 이벤트 분리 — 매체별 퍼널 전환율을 동일 기준으로 비교',
      'CPA 단독이 아닌 리드 품질·미팅 전환율 기준 예산 유지·축소·확장 후보 도출 (월 ₩3,800만+ 규모)',
      '소재·랜딩·타깃 조합 A/B식 운영 — CPA·CVR 변화를 숫자로 개선안 작성',
      '날짜·매체·캠페인 기준 Raw 통합 구조 설계 — Sheets/Looker Studio 리포트 자동화'
    ]
  },
  {
    period: '2025 – 2026',
    category: 'Tracking & Measurement',
    company: '글로벌알파미디어',
    title: 'GA4/GTM 문의 전환 측정 구조 정리',
    description:
      '광고 클릭 이후 실제 문의까지 이어지는 흐름이 불명확해 매체별 성과 판단이 어려웠습니다. UTM 규칙을 정리하고 문의하기 클릭, 폼 진입, 제출 완료 이벤트를 구분하는 측정 구조를 설계했습니다.'
  },
  {
    period: '2025 – 2026',
    category: 'App Growth Funnel',
    company: '글로벌알파미디어',
    title: '외국인 대상 병원 예약 앱 B2C 전환 흐름 분석',
    description:
      '앱 설치, 이벤트 참여, 예약 전환까지 이어지는 흐름을 채널별로 구분해 볼 필요가 있었습니다. Airbridge 기반 이벤트 구조를 검토하고 국가별·채널별 유입 차이를 비교할 수 있는 분석 흐름을 설계했습니다.'
  },
  {
    period: '2025.11 – 2025.12',
    category: 'Growth / PM',
    company: '개인 프로젝트',
    title: '신규 사용자 첫 행동 전환율 개선',
    description:
      '이벤트 기반 분석 환경을 가정한 시나리오 프로젝트입니다. 가입 → 첫 행동 전환 정체를 핵심 문제로 정의하고, UX 가이드 A/B 테스트로 전환·리텐션 트레이드오프를 비교했습니다.',
    bullets: [
      '북극성 지표: 가입 → 첫 행동 전환율',
      '단기 전환 vs 이해된 행동 유도 — UX 가이드 방식 선택',
      '전환 개선만으로는 리텐션 문제 해결 한계 확인'
    ]
  },
  {
    period: '2025.12',
    category: 'Growth / PM',
    company: '개인 프로젝트',
    title: '퍼널·리텐션 기반 문제 발생 단계 규명',
    description:
      '퍼널과 리텐션 지표를 함께 분석해, 리텐션 저하가 기능 부족이 아닌 핵심 가치 경험 이전 단계에서 시작됨을 규명했습니다. “무엇을 추가할 것인가”가 아닌 “어디부터 개입해야 하는가”로 문제를 재정의했습니다.'
  },
  {
    period: '2025 – 2026',
    category: 'Creative Analytics',
    company: '1인 기획·개발',
    title: 'Meta Creative Intelligence — 소재 방향성 분석 앱',
    description:
      'Meta Marketing API로 소재 메타(카피, CTA, 포맷)와 성과 지표를 join하고, 포맷·훅·CTA별 CPA 패턴을 분석해 Direction Brief를 생성하는 Streamlit 앱을 개발했습니다.'
  },
  {
    period: '2025',
    category: 'Data Marketing',
    company: '1인 기획·개발',
    title: 'Marketing Keyword Gap → Shoot Brief',
    description:
      'YouTube Data API로 KR 대중 트렌드 vs 마케팅 키워드 gap을 분석하고, 포맷·훅·제목·태그가 담긴 Shoot Brief 1장으로 이번 주 촬영 액션을 도출하는 Streamlit 앱입니다.'
  }
];

export const coreTools = [
  'Meta Ads',
  'Google Ads',
  'Naver Search Ads',
  'TikTok Ads',
  'GA4',
  'GTM',
  'UTM',
  'Microsoft Clarity',
  'Airbridge',
  'SQL',
  'Python (pandas)',
  'Google Sheets',
  'Excel',
  'Figma',
  'Photoshop',
  'Notion'
];

export const supplementarySkills = [
  { name: 'SQL', level: '78%', category: 'Analytics' },
  { name: 'Figma', level: '80%', category: 'Design' },
  { name: 'Photoshop', level: '72%', category: 'Design' },
  { name: 'Python (pandas)', level: '72%', category: 'Data' },
  { name: 'Looker Studio', level: '75%', category: 'Reporting' },
  { name: 'A/B Test Design', level: '85%', category: 'Growth / PM' }
];
