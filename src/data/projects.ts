export type ProjectEntry = {
  slug: string;
  title: string;
  summary: string;
  tags: string[];
  featured: boolean;
};

export const projects: ProjectEntry[] = [
  {
    slug: 'marketing-lead-dashboard',
    title: 'Marketing Lead Funnel Dashboard',
    summary:
      '광고 채널별 유입부터 문의, 진성문의, 미팅, 매출까지 이어지는 퍼널을 분석하고 개선 액션을 도출하는 대시보드 프로젝트입니다.',
    tags: ['Performance', 'Funnel Analytics', 'CRM', 'Dashboard'],
    featured: true
  }
];
