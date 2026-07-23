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
    id: 'growth-operations',
    label: 'Growth Operations / Marketing Analytics 이력서',
    description: '문제정의 · 측정 구조 · 퍼널 분석 · 데이터 기반 실행 우선순위 중심',
    filename: 'files/kang-banseok-resume-growth-operations.pdf',
    tags: ['Growth Ops', 'Marketing Analytics', 'Measurement', 'Decision'],
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
