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
    id: 'performance-growth',
    label: '퍼포먼스 / 그로스 이력서',
    description: '멀티채널 운영 · GA4/GTM 측정 · CPA/CVR · 리드 품질 중심',
    filename: 'files/kang-banseok-resume-performance-growth.pdf',
    tags: ['Performance', 'Growth', 'GA4/GTM', 'Lead Funnel'],
    primary: true
  },
  {
    id: 'crm-ops',
    label: 'CRM / Marketing Ops 이력서',
    description: '전환 누수 · 세그먼트 · 리드 상태값 · CRM 실험 설계 중심',
    filename: 'files/kang-banseok-resume-crm-ops.pdf',
    tags: ['CRM', 'Marketing Ops', 'Segmentation', 'Lifecycle']
  },
  {
    id: 'growth-product',
    label: 'Growth PM / Product Analytics 이력서',
    description: '문제정의 · 퍼널 · 실험 설계 · 트레이드오프 중심',
    filename: 'files/kang-banseok-resume-growth-product.pdf',
    tags: ['Growth PM', 'Product Analytics', 'Experiment', 'Funnel']
  }
];
