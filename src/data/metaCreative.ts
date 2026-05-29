export const metaCreativeSnapshot = {
  creativeCount: 8,
  avgCtr: 2.4,
  avgCpa: 10293,
  videoPct: 50,
  imagePct: 25,
  carouselPct: 25,
  formatStats: [
    { name: 'Video', avgCpa: 8961, share: 50 },
    { name: 'Carousel', avgCpa: 10237, share: 25 },
    { name: 'Image', avgCpa: 17083, share: 25 }
  ],
  hookStats: [
    { name: '질문형', avgCpa: 9636, share: 25 },
    { name: 'How-to', avgCpa: 8793, share: 12.5 },
    { name: '사회적증거', avgCpa: 8429, share: 12.5 },
    { name: '혜택형', avgCpa: 12808, share: 25 },
    { name: '긴급형', avgCpa: 11667, share: 12.5 },
    { name: '일반', avgCpa: 22500, share: 12.5 }
  ],
  creatives: [
    {
      name: 'Video · How-to Hook E',
      format: 'Video',
      hook: 'How-to',
      cta: '문의하기',
      ctr: 3.0,
      cpa: 8793
    },
    {
      name: 'Carousel · Social Proof D',
      format: 'Carousel',
      hook: '사회적증거',
      cta: '문의하기',
      ctr: 3.0,
      cpa: 8429
    },
    {
      name: 'Video · Question Hook G',
      format: 'Video',
      hook: '질문형',
      cta: '문의하기',
      ctr: 3.0,
      cpa: 9271
    },
    {
      name: 'Video · Question Hook A',
      format: 'Video',
      hook: '질문형',
      cta: '문의하기',
      ctr: 3.0,
      cpa: 10000
    }
  ],
  brief: {
    summary:
      'CPA 상위 그룹은 Video + 질문형/How-to 훅 + 문의하기 CTA 조합이 우세합니다. Image + 일반 훅은 CPA 22,500원으로 하위 성과.',
    recommendations: [
      '포맷: Video 소재가 평균 CPA 8,961원으로 가장 효율적',
      '훅: How-to 메시지가 CVR 1.61% 기준 상위',
      'CTA: 문의하기(CONTACT_US) 조합을 우선 테스트'
    ],
    nextTests: [
      'Video + 질문형 훅 + 문의하기 CTA — 기존 상위 패턴 변형 A/B',
      'Video + How-to 훅 — 15초/30초 영상 버전',
      '하위 Image/일반 훅 예산 축소 → 상위 패턴 재배분'
    ]
  }
};

export const metaCreativeProject = {
  slug: 'meta-creative-intelligence',
  title: 'Meta Creative Intelligence — 소재 메타데이터 기반 방향성 분석',
  period: '2025 – 2026',
  role: 'Performance Marketer · Data (Solo)',
  githubUrl: 'https://github.com/BANSEOK-KANG1/Growth/tree/main/apps/meta-creative-analyzer',
  /** Streamlit Cloud live app — set PUBLIC_META_CREATIVE_APP_URL in GitHub Actions Variables */
  liveDemoUrl: import.meta.env.PUBLIC_META_CREATIVE_APP_URL ?? '',
  problem:
    '소재별 카피·포맷·성과가 Ads Manager에 흩어져 있어, “다음에 어떤 영상/메시지를 만들지” 판단이 감에 의존했습니다. Meta API로 소재 메타와 CPA/CTR/CVR을 한 구조로 묶을 필요가 있었습니다.',
  approach: [
    'Meta Marketing API로 Creative 메타 + Ad Insights 성과 수집 (ETL)',
    '포맷·훅 키워드·CTA 차원으로 CPA/CTR/CVR 패턴 집계',
    '상위 25% vs 하위 25% 비교 → Direction Brief 자동 생성',
    'Streamlit 4탭 UI: Overview / Explorer / Pattern / Brief'
  ],
  tools: ['Meta Marketing API', 'Python', 'pandas', 'Streamlit', 'SQL export'],
  metrics: [
    { label: '분석 차원', value: '3+' },
    { label: 'UI 탭', value: '4' },
    { label: '추천 출력', value: 'Brief' },
    { label: '데이터 모드', value: 'API + Sample' }
  ],
  learnings: [
    '소재 카피 메타(훅·CTA·포맷)와 성과를 join해야 “다음 영상 방향”이 데이터로 설명됩니다.',
    'API 토큰·계정 정보는 로컬 전용 — 공개 포트폴리오에는 익명 샘플만 노출합니다.',
    '마케터는 차트보다 “다음 테스트 3가지” 문장형 브리프를 바로 씁니다.',
    'Streamlit Cloud에 배포해 Sample mode 공개 데모 + Secrets로 Meta API 연동이 가능합니다.'
  ]
};
