export type ToolItem = {
  name: string;
  level: number;
  note?: string;
};

export type ToolCategory = {
  id: string;
  label: string;
  description: string;
  items: ToolItem[];
};

export const toolCategories: ToolCategory[] = [
  {
    id: 'marketing',
    label: 'Marketing & Ads',
    description: '매체 운영과 성과 판단',
    items: [
      { name: 'Meta Ads', level: 90 },
      { name: 'Google Ads', level: 88 },
      { name: 'Naver Search Ads', level: 85 },
      { name: 'TikTok Ads', level: 82 },
      { name: 'UTM Naming', level: 92 }
    ]
  },
  {
    id: 'analytics',
    label: 'Analytics & Tracking',
    description: '전환 측정과 행동 분석',
    items: [
      { name: 'GA4', level: 90 },
      { name: 'GTM', level: 88 },
      { name: 'Microsoft Clarity', level: 85 },
      { name: 'Airbridge', level: 82 },
      { name: 'SQL', level: 78, note: '마케팅 Raw·퍼널 쿼리' },
      { name: 'Python (pandas)', level: 72, note: '트렌드·리포트 자동화' }
    ]
  },
  {
    id: 'data',
    label: 'Data & Reporting',
    description: '리포트와 대시보드',
    items: [
      { name: 'Google Sheets', level: 92 },
      { name: 'Excel', level: 90 },
      { name: 'Looker Studio', level: 75 },
      { name: 'Notion', level: 88 }
    ]
  },
  {
    id: 'design',
    label: 'Design & Prototyping',
    description: 'UX 구조 이해와 시각 작업',
    items: [
      { name: 'Figma', level: 80, note: '와이어프레임·프로토타입' },
      { name: 'Photoshop', level: 72, note: '소재·랜딩 비주얼' },
      { name: 'Adobe XD', level: 70 }
    ]
  },
  {
    id: 'ops',
    label: 'Ops & Collaboration',
    description: '문서화와 협업',
    items: [
      { name: 'GitHub', level: 75 },
      { name: 'WordPress', level: 68 },
      { name: 'Webflow', level: 62 },
      { name: 'Slack', level: 85 }
    ]
  }
];

export const toolHighlights = [
  'Meta Ads',
  'GA4 / GTM',
  'SQL',
  'Figma',
  'Python',
  'Airbridge',
  'Notion',
  'Photoshop'
];
