const growthAppBase = (
  import.meta.env.PUBLIC_GROWTH_APP_URL ??
  import.meta.env.PUBLIC_META_CREATIVE_APP_URL ??
  ''
).replace(/\/$/, '');

export const youtubeTrendSnapshot = {
  videoCount: 50,
  categoryCount: 15,
  shortsShare: 38,
  engagementRate: 4.2,
  categories: [
    { name: 'Entertainment', share: 82 },
    { name: 'Music', share: 65 },
    { name: 'Gaming', share: 48 },
    { name: 'Howto', share: 35 },
    { name: 'News', share: 28 }
  ],
  keywords: ['#AI', '#먹방', '#K-pop', '#브이로그', '#챌린지'],
  modes: ['Trending', 'Keyword Search', 'Insight Report', 'Deep Dive']
};

export const youtubeTrendProject = {
  slug: 'youtube-trend-analyzer',
  title: 'YouTube KR 트렌드 분석 허브',
  period: '2025 – 2026',
  role: 'PM · Data Marketing (Solo)',
  githubUrl: 'https://github.com/BANSEOK-KANG1/Growth/tree/main/apps/meta-creative-analyzer',
  liveDemoUrl: growthAppBase ? `${growthAppBase}/YouTube_KR_Trends` : '',
  problem:
    '콘텐츠·마케팅 기획 시 KR YouTube 트렌드를 빠르게 파악해야 하지만, 트렌딩 목록·키워드 검색·정량 비교가 여러 도구에 분산되어 있었습니다.',
  approach: [
    'YouTube Data API로 KR 인기 영상 수집 (ETL) + engagement·Shorts·훅 파생 지표',
    '마케팅 vertical 키워드(SaaS, AI 마케팅, CRM 등) vs 트렌딩 overlap 분석',
    '카테고리·포맷·제목 훅 패턴 집계 → Content Brief 자동 생성',
    'Growth Analytics Hub Streamlit 4탭: Overview / Explorer / Keyword & Pattern / Brief'
  ],
  tools: ['YouTube Data API', 'Python', 'pandas', 'Streamlit', 'Markdown export'],
  metrics: [
    { label: '데이터 소스', value: 'Live API' },
    { label: '탐색 모드', value: '4' },
    { label: '키워드 프리셋', value: '6+' },
    { label: '출력', value: 'Content Brief' }
  ],
  learnings: [
    '키워드 search.list는 100 quota — 프리셋·캐시 설계가 필수입니다.',
    '마케팅 사용자는 차트보다 “다음 콘텐츠 테스트 4가지” 문장형 브리프를 바로 씁니다.',
    '트렌딩 vs vertical 키워드 engagement gap이 블루오션 후보를 데이터로 설명합니다.',
    'YouTube API Key만으로 회사 승인 없이 실 KR 데이터 Live 데모가 가능합니다.'
  ]
};
