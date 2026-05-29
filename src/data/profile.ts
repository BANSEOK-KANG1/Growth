export const profile = {
  nameKo: '강반석',
  nameEn: 'Kang Banseok',
  role: 'Growth Performance Marketer',
  headline: '광고 성과와 사용자 행동 데이터를 연결해 유입–전환–리드–CRM 퍼널의 병목을 찾고 개선합니다.',
  summary:
    'Meta, Naver, Google, TikTok 광고 운영 경험과 GA4/GTM/UTM/Clarity 기반 전환 측정 경험을 바탕으로, 매체 데이터와 GA4 로그 데이터를 통합해 실제 문의·가입·매출로 이어지는 흐름을 분석합니다.',
  oneLineIntro:
    '저는 광고를 단순히 집행하는 사람이 아니라, 광고비가 어디서 성과로 이어지고 어디서 새는지 추적해 다음 액션으로 바꾸는 퍼포먼스/그로스 마케터입니다.',
  email: 'kangbs2486@gmail.com',
  phone: '010-9630-2486',
  location: '서울 관악구',
  githubUrl: 'https://github.com/BANSEOK-KANG1',
  notionUrl: 'https://www.notion.so/288307eb16758057959febc15739bf7f',
  siteUrl: 'https://banseok-kang1.github.io/Growth/',
  photoPath: 'images/profile.png',
  resumePdfPath: 'files/kang-banseok-resume.pdf',
  portfolioPdfPath: 'files/kang-banseok-portfolio.pdf',
  targetRoles: ['In-house Performance Marketer', 'Growth Marketer', 'CRM / Marketing Ops', 'Growth PM Assistant'],
  keywords: ['Performance Marketing', 'Growth Marketing', 'CRM Strategy', 'GA4 / GTM / UTM', 'Funnel Analytics', 'Marketing Ops']
};

export type EducationEntry = {
  period: string;
  school: string;
  degree: string;
  description: string;
};

export const education: EducationEntry[] = [
  {
    period: '2021.09 – 2024.09',
    school: '인터랙션 디자인',
    degree: '학사',
    description:
      'HCI, 시각 커뮤니케이션, 프로토타이핑 및 사용성 테스트 과정을 이수했습니다. 지역 농산물 직거래 앱 캡스톤, 교육용 게임 인터랙티브 프로토타입 등 사용자 탐색·와이어프레임·반복 디자인 경험을 쌓았습니다.'
  }
];
