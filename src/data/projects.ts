export type ProjectEntry = {
  slug: string;
  title: string;
  summary: string;
  period?: string;
  tags: string[];
  featured: boolean;
  externalUrl?: string;
};

export const projects: ProjectEntry[] = [
  {
    slug: 'marketing-lead-dashboard',
    title: 'Marketing Lead Funnel Dashboard',
    period: '2025 – 2026',
    summary:
      '매체 데이터(비용, 노출, 클릭)와 GA4·리드 상태값(문의, 진성문의, 미팅, 매출)을 하나의 Raw 구조로 통합해 채널별 CPA/CVR/리드 품질을 비교하고 예산·CRM 액션을 도출하는 대시보드 프로젝트입니다.',
    tags: ['Performance', 'Funnel Analytics', 'CRM', 'Dashboard'],
    featured: true
  },
  {
    slug: 'youtube-trend-analyzer',
    title: 'YouTube KR 트렌드 분석 허브',
    period: '2025',
    summary:
      'YouTube Data API로 KR 트렌딩·키워드 검색을 한 화면에서 비교하고, 카테고리·Shorts·참여율 필터와 자동 인사이트 리포트로 기획 리서치 시간을 줄이는 데이터 분석 프로젝트입니다.',
    tags: ['YouTube API', 'Python', 'Trend Analysis', 'Data Marketing'],
    featured: true
  },
  {
    slug: 'growth-performance-portfolio',
    title: 'Growth Performance Portfolio',
    period: '2024 – 2026',
    summary:
      '인하우스 퍼포먼스/그로스/CRM 직무 지원을 위한 케이스 스터디형 포트폴리오입니다. Astro + GitHub Pages로 구축했습니다.',
    tags: ['Portfolio', 'Astro', 'Case Study'],
    featured: false,
    externalUrl: 'https://banseok-kang1.github.io/Growth/'
  }
];
