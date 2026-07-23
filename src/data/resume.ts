export type ResumeTrack = {
  id: 'growth-operations' | 'crm-ops' | 'growth-product';
  eyebrow: string;
  title: string;
  target: string;
  summary: string;
  contribution: string;
  strengths: string[];
  evidence: Array<{
    label: string;
    href: string;
    note: string;
    project?: boolean;
  }>;
  pdf: string;
};

export type ExperienceEntry = {
  company: string;
  role: string;
  period: string;
  summary: string;
  bullets: string[];
};

export type ProjectEntry = {
  title: string;
  period: string;
  type: string;
  summary: string;
  bullets: string[];
  href: string;
};

export const resumeTracks: ResumeTrack[] = [
  {
    id: 'growth-operations',
    eyebrow: 'TRACK 01 · PRIMARY',
    title: 'Growth Operations / Marketing Analytics',
    target: '성장 문제·측정 기준·실행 우선순위를 연결하는 포지션',
    summary:
      '마케팅 실무에서 얻은 채널·전환 이해를 기반으로 데이터를 같은 기준으로 연결하고, 성과가 끊기는 구간과 다음 의사결정을 구조화합니다.',
    contribution:
      '흩어진 매체·행동·리드 데이터를 하나의 흐름으로 정리하고, 팀이 같은 지표를 보며 유지·중단·실험 우선순위를 결정할 수 있는 운영 구조를 만들 수 있습니다.',
    strengths: [
      '문제 → 이벤트 → 지표 → 판단 → 액션으로 의사결정 구조화',
      'GA4/GTM/UTM 기반 유입 → 행동 → 전환 측정 기준 설계',
      '날짜·매체·캠페인·리드 상태값을 연결하는 Raw 구조 설계',
      'API·Python·Streamlit 기반 분석 도구와 실행 브리프 구현'
    ],
    evidence: [
      {
        label: 'Marketing Lead Funnel Dashboard',
        href: 'projects/marketing-lead-dashboard/',
        note: '데이터 연결·판단 구조 프로젝트',
        project: true
      },
      {
        label: 'GA4/GTM/UTM 전환 측정 구조',
        href: 'cases/ga4-gtm-tracking-system/',
        note: '실무 경험 기반 · 도메인/ID 익명화'
      },
      {
        label: '글로벌 앱 그로스 퍼널',
        href: 'cases/global-app-growth-funnel/',
        note: '실무 경험 기반 · 서비스/수치 익명화'
      }
    ],
    pdf: 'files/kang-banseok-resume-growth-operations.pdf'
  },
  {
    id: 'crm-ops',
    eyebrow: 'TRACK 02',
    title: 'CRM / Marketing Operations',
    target: '광고 유입 이후 전환 누수를 줄이는 포지션',
    summary:
      '광고 이후 문의 미완료, 미팅 미진행, 구매 미전환 구간을 세그먼트로 나누고 메시지·지표·판단 기준을 설계합니다.',
    contribution:
      '실무 측정 경험과 프로젝트형 CRM 설계를 결합해, 리드 상태값·캠페인·후속 전환을 연결하는 운영 구조를 제안할 수 있습니다.',
    strengths: [
      'UTM·이벤트명·리포트 기준 문서화 및 표준화',
      '퍼널 단계별 이탈 세그먼트와 후속 메시지 가설 설계',
      '오픈율·CTR·미팅 전환율 중심 CRM 실험 지표 정의',
      'Sheets·Looker Studio·SQL·Python 기반 데이터 구조화'
    ],
    evidence: [
      {
        label: 'CRM/그로스 실험 시나리오',
        href: 'cases/crm-retention-scenario/',
        note: '프로젝트형 설계 · 실제 CRM 발송 성과 아님',
        project: true
      },
      {
        label: 'GA4/GTM/UTM 전환 측정 구조',
        href: 'cases/ga4-gtm-tracking-system/',
        note: '실무 경험 기반 · 도메인/ID 익명화'
      },
      {
        label: 'Marketing Lead Funnel Dashboard',
        href: 'projects/marketing-lead-dashboard/',
        note: '리드 상태값 연결 대시보드 프로젝트',
        project: true
      }
    ],
    pdf: 'files/kang-banseok-resume-crm-ops.pdf'
  },
  {
    id: 'growth-product',
    eyebrow: 'TRACK 03',
    title: 'Growth PM / Product Analytics',
    target: '문제·지표·실험·우선순위를 구조화하는 포지션',
    summary:
      '사용자가 어디서 멈추는지 퍼널로 정의하고, 대표 지표와 트레이드오프를 기준으로 다음 실험의 우선순위를 정합니다.',
    contribution:
      '마케팅 실무에서 익힌 측정 감각과 개인 프로젝트의 문제정의 프레임을 바탕으로, 마케팅·데이터·제품 사이의 판단 기준을 정리할 수 있습니다.',
    strengths: [
      '유입 → 활성화 → 전환 퍼널의 병목 단계 정의',
      '가설 → 이벤트 → 지표 → 판단 기준으로 실험 구조화',
      '단기 전환과 리텐션의 트레이드오프 명시',
      'API·Python·Streamlit을 활용한 분석 도구 기획·구현'
    ],
    evidence: [
      {
        label: '글로벌 앱 그로스 퍼널',
        href: 'cases/global-app-growth-funnel/',
        note: '실무 경험 기반 · 서비스/수치 익명화'
      },
      {
        label: 'CRM/그로스 실험 시나리오',
        href: 'cases/crm-retention-scenario/',
        note: '프로젝트형 설계',
        project: true
      },
      {
        label: 'Marketing Keyword Gap → Shoot Brief',
        href: 'projects/youtube-trend-analyzer/',
        note: '1인 기획·개발',
        project: true
      }
    ],
    pdf: 'files/kang-banseok-resume-growth-product.pdf'
  }
];

export const experience: ExperienceEntry[] = [
  {
    company: '글로벌알파미디어',
    role: '퍼포먼스 마케터',
    period: '2025.12 – 2026',
    summary:
      '해외 타깃 리드형 캠페인을 멀티채널로 운영하고, 광고 클릭 이후 문의·진성문의·미팅 전환까지 판단할 수 있도록 측정 및 리포팅 구조를 정리했습니다.',
    bullets: [
      'Meta·Google·Naver·TikTok 채널별 비용·CPA·리드 품질을 비교해 예산 유지·축소·확장 후보 도출',
      'UTM 규칙과 GTM 이벤트를 정리하고 GA4에서 문의 클릭·폼 진입·제출 완료를 구분',
      'CPA 단독이 아닌 진성문의율·미팅 전환율까지 포함해 월 3,800만 원 이상 규모 캠페인 분석',
      '소재·타깃·랜딩 조합별 성과 변화를 정리해 테스트 우선순위 및 개선안 작성',
      '날짜·매체·캠페인 기준 Raw 통합 및 Sheets·Looker Studio 리포트 구조 설계',
      'Airbridge 이벤트 구조를 검토하고 국가·채널별 설치 → 예약 전환 분석 흐름 정리'
    ]
  }
];

export const projects: ProjectEntry[] = [
  {
    title: 'Meta Creative Intelligence',
    period: '2025 – 2026',
    type: '1인 기획·개발',
    summary:
      'Meta 소재 메타와 성과 지표를 결합해 포맷·훅·CTA별 CPA 패턴을 분석하고 다음 제작 방향을 제안하는 Streamlit 앱입니다.',
    bullets: [
      'Meta Marketing API 데이터 수집·정규화 구조 설계',
      'Creative Meta + Insights 결합 후 Direction Brief 생성'
    ],
    href: 'projects/meta-creative-intelligence/'
  },
  {
    title: 'Marketing Keyword Gap → Shoot Brief',
    period: '2025',
    type: '1인 기획·개발',
    summary:
      'YouTube Data API로 대중 트렌드와 마케팅 키워드의 차이를 분석하고, 촬영에 바로 쓰는 포맷·훅·제목·태그 브리프를 생성합니다.',
    bullets: [
      '트렌드 탐색을 콘텐츠 제작 의사결정으로 변환',
      'API → 분석 → 실행 브리프의 반복 가능한 흐름 구현'
    ],
    href: 'projects/youtube-trend-analyzer/'
  },
  {
    title: 'CRM/그로스 실험 시나리오',
    period: '2026',
    type: '개인 프로젝트 · 실제 발송 성과 아님',
    summary:
      '문의 미완료·미팅 미진행·미구매 세그먼트별 메시지 가설과 오픈율·CTR·미팅 전환율 판단 기준을 설계했습니다.',
    bullets: [
      'Segment → Hypothesis → Message → Metric → Decision 구조',
      '실제 적용 시 필요한 CRM 인프라·표본·개인정보 한계 명시'
    ],
    href: 'cases/crm-retention-scenario/'
  }
];

export const toolGroups = [
  {
    label: '광고 운영',
    tools: ['Meta Ads', 'Google Ads', 'Naver Search Ads', 'TikTok Ads']
  },
  {
    label: '측정·분석',
    tools: ['GA4', 'GTM', 'UTM', 'Microsoft Clarity', 'Airbridge']
  },
  {
    label: '데이터·리포팅',
    tools: ['SQL', 'Python (pandas)', 'Google Sheets', 'Excel', 'Looker Studio']
  },
  {
    label: '기획·제작',
    tools: ['Figma', 'Photoshop', 'Notion', 'GitHub', 'Streamlit']
  }
];

export const supportingBackground = [
  '요기요 영업 1년 — 고객 니즈 파악·서비스 가치 설명·관계 관리',
  '삼성생명 SFP 6개월 — 1:1 상담·제안 커뮤니케이션',
  '웹디자인 경험 — 랜딩·소재 수정 요청을 제작 관점에서 구체화'
];
