export type ResumeEntry = {
  period: string;
  category: string;
  title: string;
  company?: string;
  description: string;
};

export const resumeTimeline: ResumeEntry[] = [
  {
    period: '2024 – 2026',
    category: 'Performance Marketing / Marketing Analytics',
    company: '실무 프로젝트',
    title: '광고 성과 분석 및 전환 측정',
    description:
      'Meta, Naver, Google, TikTok 광고 데이터를 기준으로 CPA/CVR/ROAS를 비교하고, GA4/GTM/UTM/Clarity를 활용해 문의하기 클릭과 제출완료 이벤트를 구분하는 전환 측정 구조를 정리했습니다. 매체 어드민 데이터와 GA4 유입·전환 데이터를 날짜·매체·캠페인 기준으로 통합해 성과 판단 Raw 구조를 설계했습니다.'
  },
  {
    period: '2025 – 2026',
    category: 'Global App Growth Funnel',
    company: 'ZIVO hospital',
    title: '글로벌 앱 유입–설치–전환 퍼널 설계',
    description:
      '외국인 대상 병원 예약 앱에서 국가별 유입 채널, 앱 설치, 인앱 이벤트, 병원 문의/예약 가능성을 분리해서 보는 퍼널 구조를 설계했습니다. Airbridge, Meta, TikTok, Google Ads 어트리뷰션 연결을 점검했습니다.'
  },
  {
    period: '2024 – 2025',
    category: 'Marketing Data / Dashboard',
    company: '디지털 마케팅 & 데이터분석',
    title: '마케팅 데이터 수집·대시보드 설계',
    description:
      '자체 데이터(GA4: 유입경로, 방문, 전환)와 매체 데이터(노출, 클릭, 비용)를 구분·통합하는 분석 구조를 학습하고 적용했습니다. Google Sheets, Looker Studio, SQL 기반 마케팅 대시보드 설계와 캠페인별 KPI 리포트 구조를 정리했습니다.'
  },
  {
    period: '2023.08 – 2024.03',
    category: 'Landing / Web Project',
    company: 'Bees Together (비영리)',
    title: '랜딩 페이지 기획·디자인·구축',
    description:
      '양봉 보호 재단 웹사이트를 기획·디자인·WordPress로 구축했습니다. 이해관계자 워크숍으로 니즈를 정리하고, CTA·콘텐츠 구조·론칭 후 트래픽 변화를 확인했습니다. 6개월간 사이트 트래픽 2배 증가.'
  },
  {
    period: '2022.06 – 2022.09',
    category: 'UI Design Internship',
    company: '당근마켓',
    title: 'UI 디자인 인턴십',
    description:
      '와이어프레임, 프로토타입, 사용자 플로우 제작을 지원하며 여러 팀과 협업했습니다. 사용자 조사·사용성 테스트 실무 경험을 통해 직관적인 UX 설계 역량을 쌓았습니다.'
  },
  {
    period: '2022.05 – 2022.08',
    category: 'E-commerce UI',
    company: 'Knitties',
    title: '이커머스 UI 디자인·Shopify 구축',
    description:
      '손뜨개 비니 이커머스의 Figma 와이어프레임·프로토타입, Shopify 구현, 사용성 테스트를 진행했습니다. 랜딩·상품 페이지 설득 구조와 전환 경험 설계 경험으로 퍼포먼스 마케팅 랜딩 개선에 연결합니다.'
  },
  {
    period: '2023 – 2024',
    category: 'RFP / Requirement Structuring',
    company: '공공 SI 제안',
    title: '요구사항 분석과 문서 구조화',
    description:
      'RFP 요구사항을 기능·운영·산출물 기준으로 분해하고, 제안서 목차와 메시지를 정렬하는 경험을 했습니다. Marketing Ops·PM Assistant 직무의 요구사항 정리 역량으로 연결합니다.'
  }
];

export const coreTools = [
  'Meta Ads',
  'Naver Ads',
  'Google Ads',
  'TikTok Ads',
  'GA4',
  'GTM',
  'UTM',
  'Clarity',
  'Airbridge',
  'Looker Studio',
  'Google Sheets',
  'SQL',
  'Figma',
  'Spreadsheet'
];

export const supplementarySkills = [
  { name: 'Figma', level: '80%', category: '디자인' },
  { name: 'Photoshop', level: '70%', category: '디자인' },
  { name: 'Notion', level: '85%', category: '프로젝트 관리' },
  { name: 'Webflow', level: '60%', category: '웹사이트 빌더' }
];
