export type ArchiveKind = 'case' | 'project' | 'resource';

export type ArchiveItem = {
  id: string;
  kind: ArchiveKind;
  title: string;
  summary: string;
  href: string;
  category: string;
  period?: string;
  tags: string[];
  featured?: boolean;
  external?: boolean;
};

export const archiveKindLabels: Record<ArchiveKind, string> = {
  case: '실무 케이스',
  project: '프로젝트',
  resource: '지원 자료'
};

export const archiveKindDescriptions: Record<ArchiveKind, string> = {
  case: '인하우스 실무 판단 구조 — 문제 → 지표 → 액션',
  project: 'API·대시보드·분석 도구 — Live Demo 포함',
  resource: '이력서 PDF · JD Fit · 지원용 문서'
};

export function getResourceArchiveItems(base: string): ArchiveItem[] {
  return [
    {
      id: 'resume-hub',
      kind: 'resource',
      title: 'Resume · JD Fit',
      summary: 'Growth Operations·CRM·Growth PM 직무별 포지셔닝과 PDF 이력서 다운로드.',
      href: `${base}resume/`,
      category: '지원 자료',
      period: '2026',
      tags: ['Growth Ops', 'Resume', 'PDF'],
      featured: true
    },
    {
      id: 'baro-interactive',
      kind: 'resource',
      title: '바로인터랙티브 맞춤 지원 페이지',
      summary: '온라인광고 운영·분석 AM / 퍼포먼스 마케터 JD에 맞춘 원페이지 + 맞춤 이력서 PDF.',
      href: `${base}baro-interactive/`,
      category: 'JD Fit',
      period: '2026-07',
      tags: ['Agency', 'SA/DA', 'PDF'],
      featured: true
    },
    {
      id: 'portfolio-hub',
      kind: 'resource',
      title: 'Portfolio Hub · JD /for/{slug}',
      summary: 'JD별 맞춤 URL 허브. fintech-growth-pm · content-marketing 샘플 프로필.',
      href: 'https://banseok-kang1.github.io/portfolio-hub/',
      category: 'JD Fit',
      period: '2026-07',
      tags: ['Hub', 'JD Fit'],
      featured: true,
      external: true
    },
    {
      id: 'pm-portfolio',
      kind: 'resource',
      title: 'PM Portfolio · Work Archive',
      summary: 'APS Problem Solver 핏 PM 사이트. 케이스 전체는 /work/에서.',
      href: 'https://banseok-kang1.github.io/pm/work/',
      category: 'PM',
      period: '2026',
      tags: ['PM', 'Archive'],
      featured: false,
      external: true
    },
    {
      id: 'resume-tracks',
      kind: 'resource',
      title: '직무별 이력서 한눈에 보기',
      summary: 'Growth Operations·CRM·Growth PM 트랙별 강점, 증거, 기여 가능성 비교.',
      href: `${base}resume/#role-resumes`,
      category: '지원 자료',
      tags: ['Growth Ops', 'Role Fit']
    },
    {
      id: 'about',
      kind: 'resource',
      title: 'About · Working Style',
      summary: '문제정의, 측정 기준, 퍼널 통합, 실행 우선순위 — 일하는 방식과 포지션 방향.',
      href: `${base}about/`,
      category: '소개',
      tags: ['About', 'Principles']
    }
  ];
}
