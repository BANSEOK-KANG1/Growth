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
      summary: '그로스 마케터 JD 8항목 매핑, 이력서 bullet·자소서 훅 복사, PDF 다운로드.',
      href: `${base}resume/`,
      category: '지원 자료',
      period: '2026',
      tags: ['Resume', 'JD Fit', 'PDF'],
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
      id: 'resume-jd-fit',
      kind: 'resource',
      title: 'JD Fit 한눈에 보기',
      summary: '자주 보는 그로스 JD 요건과 경험을 1:1 연결. 강점/부분매칭/갭 구분.',
      href: `${base}resume/#jd-fit`,
      category: '지원 자료',
      tags: ['Growth', 'Cover Letter']
    },
    {
      id: 'about',
      kind: 'resource',
      title: 'About · Working Style',
      summary: '측정 우선, 퍼널 통합, 지표 기반 의사결정 — 일하는 방식과 포지션 방향.',
      href: `${base}about/`,
      category: '소개',
      tags: ['About', 'Principles']
    }
  ];
}
