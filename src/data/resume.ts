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
      '해외 타깃 캠페인 운영 및 성과 분석, 측정 체계 정리를 중심으로 Meta·Google·Naver·TikTok 광고를 운영했습니다. UTM 네이밍 규칙과 채널별 측정 기준을 정리하고, GA4/GTM 기반 리드 측정 흐름을 점검했습니다.',
    bullets: [
      '주요 광고 매체 운영 및 성과 리포팅',
      'UTM 네이밍, 문의하기 클릭·전환 이벤트 측정 구조 정리',
      'CPA, CVR, ROAS, 문의 전환율 기준 캠페인 판단',
      '국가·채널·카테고리·소재별 성과 비교 분석 및 운영 개선안 작성'
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
    category: 'Performance Marketing',
    company: '글로벌알파미디어',
    title: 'Meta 캠페인 CPA 기준 운영',
    description:
      '소재별 성과 차이가 커서 짧은 주기로 검증하고 확장/중단 기준을 세울 필요가 있었습니다. 소재 테스트 주기를 단축하고 CPA, CVR, 클릭수, 문의 전환율을 기준으로 운영 판단을 정리했습니다.'
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
    period: '2025 – 2026',
    category: 'Marketing Data / Reporting',
    company: '글로벌알파미디어',
    title: '성과 리포팅·운영 판단 기준 데이터 구조화',
    description:
      '매체별 광고 수치가 흩어져 확장/중단 판단이 어려웠습니다. 클릭, 비용, 전환, CPA, CVR, ROAS를 기준으로 성과를 비교하고 개선 우선순위를 볼 수 있는 리포팅 구조로 정리했습니다.'
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
  'Google Sheets',
  'Excel',
  'Notion'
];

export const supplementarySkills = [
  { name: 'KPI Definition', level: '90%', category: 'Product & Documentation' },
  { name: 'Funnel Mapping', level: '92%', category: 'Product & Documentation' },
  { name: 'Reporting Structure', level: '88%', category: 'Product & Documentation' },
  { name: 'SQL', level: '75%', category: 'Analytics' }
];
