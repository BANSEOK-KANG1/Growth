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
    slug: 'meta-creative-intelligence',
    title: 'Meta Creative Intelligence',
    period: '2025 – 2026',
    summary:
      'Meta Marketing API로 소재 메타데이터(카피, CTA, 포맷)와 CPA/CTR/CVR 성과를 통합해, 포맷·훅·CTA 패턴 분석과 다음 영상/크리에이티브 방향 브리프를 자동 생성하는 분석 앱입니다.',
    tags: ['Meta Marketing API', 'Creative Analytics', 'Python', 'Streamlit'],
    featured: true
  },
  {
    slug: 'youtube-trend-analyzer',
    title: 'Marketing Keyword Gap → Shoot Brief',
    period: '2025 – 2026',
    summary:
      'KR YouTube 대중 트렌드 vs 마케팅 키워드(SaaS·리드gen) gap을 분석해, 포맷·훅·제목·태그가 담긴 Shoot Brief 1장으로 이번 주 촬영 액션을 도출하는 도구입니다.',
    tags: ['YouTube API', 'Content Planning', 'Python', 'Streamlit'],
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
