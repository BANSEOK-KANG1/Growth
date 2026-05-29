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
    id: 'revised',
    label: '한장 이력서 (수정본)',
    description: 'Product / Growth Analyst · Metric-driven Decision Support',
    filename: 'files/kang-banseok-resume-revised.pdf',
    tags: ['Growth', 'PM', 'CRM'],
    primary: true
  },
  {
    id: 'crm-growth',
    label: 'CRM · 그로스 지원용',
    description: '퍼널·전환·리텐션 의사결정 구조 중심 JD 맞춤 버전',
    filename: 'files/kang-banseok-resume-crm-growth.pdf',
    tags: ['CRM', 'Growth', 'Experiment']
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
