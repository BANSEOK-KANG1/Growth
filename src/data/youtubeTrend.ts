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
  period: '2025',
  role: 'PM · Data Marketing (Solo)',
  githubUrl: 'https://github.com/BANSEOK-KANG1',
  problem:
    '콘텐츠·마케팅 기획 시 KR YouTube 트렌드를 빠르게 파악해야 하지만, 트렌딩 목록·키워드 검색·정량 비교가 여러 도구에 분산되어 있었습니다.',
  approach: [
    'YouTube Data API로 KR 인기 영상 수집·저장 (ETL)',
    '카테고리·참여율·업로드 경과 시간 등 파생 지표 설계',
    '트렌딩 / 키워드 / 인사이트 / 딥다이브 4모드 HTML 허브 UI'
  ],
  tools: ['YouTube Data API', 'Python', 'pandas', 'Plotly', 'Streamlit/HTML Dashboard'],
  metrics: [
    { label: '분석 카테고리', value: '15+' },
    { label: '탐색 모드', value: '4' },
    { label: '리포트', value: '자동 Markdown' },
    { label: '데이터 갱신', value: '실시간 새로고침' }
  ],
  learnings: [
    'API 쿼터·스코프를 먼저 정의하면 기획 범위가 명확해집니다.',
    '마케팅 사용자는 차트보다 “다음 액션” 문장형 인사이트를 선호합니다.',
    '포트폴리오에는 HTML 인터랙티브 목업으로 제품 감을 전달했습니다.'
  ]
};
