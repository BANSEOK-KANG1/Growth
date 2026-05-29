const growthAppBase = (
  import.meta.env.PUBLIC_GROWTH_APP_URL ??
  import.meta.env.PUBLIC_META_CREATIVE_APP_URL ??
  ''
).replace(/\/$/, '');

export const youtubeTrendSnapshot = {
  keyword: 'SaaS',
  verdict: '블루오cean',
  engagementGap: '+1.2%p',
  overlap: '22%',
  format: 'Long-form 3분',
  titleHook: 'How-to',
  titleExample: 'SaaS 3단계 실전 가이드 | 초보도 10분 만에',
  testTags: ['#saas', '#b2b', '#리드gen'],
  modes: ['Keyword', 'Gap Report', 'Shoot Brief']
};

export const youtubeTrendProject = {
  slug: 'youtube-trend-analyzer',
  title: 'Marketing Keyword Gap → Shoot Brief',
  period: '2025 – 2026',
  role: 'PM · Data Marketing (Solo)',
  githubUrl: 'https://github.com/BANSEOK-KANG1/Growth/tree/main/apps/meta-creative-analyzer',
  liveDemoUrl: growthAppBase ? `${growthAppBase}/YouTube_KR_Trends` : '',
  problem:
    'KR YouTube 대중 트렌드(K-pop·먹방)와 내 마케팅 키워드(SaaS·리드gen) 콘텐츠가 달라서, 광고·UGC·브랜드 유튜브 기획 시 “뭘 찍어야 할지” 감으로만 결정했습니다.',
  approach: [
    'YouTube Data API — KR 트렌딩 baseline + 마케팅 키워드 검색 join',
    'Engagement gap · Category overlap · Shorts share gap → 블루/레드/니치 판정',
    '포맷·제목 훅·제목 예시·태그 → 이번 주 촬영 1편 Shoot Brief 자동 생성',
    'Live + Sample 비교 · 5분 자동 새로고침 · 포트폴리오 Live Embed',
  ],
  tools: ['YouTube Data API', 'Python', 'pandas', 'Streamlit', 'Markdown export'],
  metrics: [
    { label: 'USP', value: 'Gap → 1편 Brief' },
    { label: '입력', value: '키워드 1개' },
    { label: '출력', value: 'Shoot Brief' },
    { label: 'Live', value: 'API + Compare' },
  ],
  learnings: [
    '범용 트렌드 분석보다 “내 키워드 vs 대중 noise” gap이 기획 액션으로 이어집니다.',
    '출력을 Shoot Brief 1장(포맷·훅·제목·태그·이번 주 액션)으로 고정하면 USP가 명확해집니다.',
    'Meta Creative(집행 중 CPA)와 짝 — YouTube는 기획 전 organic reference 리서치.',
    'Live + Sample 비교 모드로 실시간 트렌드와 데모 데이터를 나란히 검증할 수 있습니다.',
    '포트폴리오 Live Embed + Streamlit 5분 자동 새로고침으로 “지금 KR 트렌드”를 함께 확인.',
  ]
};
