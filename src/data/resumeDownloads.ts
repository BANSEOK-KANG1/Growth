export type ResumeDownload = {
  id: string;
  label: string;
  description: string;
  filename: string;
  tags: string[];
  primary?: boolean;
};

export const resumeDownloads: ResumeDownload[] = [
  {
    id: 'crm-growth',
    label: '그로스 마케터 이력서',
    description: 'JD Fit · 퍼널·전환·CRM · GA4/GTM 중심 그로스 마케터 지원용',
    filename: 'files/kang-banseok-resume-crm-growth.pdf',
    tags: ['Growth', 'CRM', 'GA4', 'Funnel'],
    primary: true
  },
  {
    id: 'baro-interactive',
    label: '바로인터랙티브 맞춤 이력서',
    description: '온라인광고 운영·분석 AM · SA/DA · GA4/GTM · CPA/CVR/ROAS 중심 지원용',
    filename: 'files/kang-banseok-resume-baro-interactive.pdf',
    tags: ['Agency AM', 'Performance', 'SA/DA', 'GA4/GTM']
  },
  {
    id: 'revised',
    label: '한장 이력서 (수정본)',
    description: 'Product / Growth Analyst · Metric-driven Decision Support',
    filename: 'files/kang-banseok-resume-revised.pdf',
    tags: ['Growth', 'PM', 'CRM']
  },
  {
    id: 'one-page',
    label: '한장 이력서',
    description: 'Problem & Metric-driven PM 포지셔닝',
    filename: 'files/kang-banseok-resume-one-page.pdf',
    tags: ['PM', 'Analytics']
  },
  {
    id: 'performance',
    label: '퍼포먼스 마케팅 요약',
    description: '글로벌알파미디어 실무 중심 웹 요약 PDF',
    filename: 'files/kang-banseok-resume.pdf',
    tags: ['Performance', 'Ads', 'Tracking']
  }
];
