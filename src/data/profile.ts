export const profile = {
  nameKo: '강반석',
  nameEn: 'Kang Banseok',
  role: 'Growth Operations · Marketing Analytics',
  headline: '광고·사용자 행동·전환 데이터를 연결해 성장 문제를 측정 가능한 구조로 바꾸고 실행 우선순위를 정합니다.',
  summary:
    '퍼포먼스마케팅 실무에서 광고 유입과 전환 측정의 한계를 경험한 뒤, 채널 운영보다 문제 정의·측정 기준·데이터 구조·후속 액션을 연결하는 역할에 강점이 있음을 확인했습니다. GA4/GTM/UTM, 퍼널 분석, 리드 상태값, API 기반 분석 도구를 활용해 마케팅·데이터·제품 사이의 판단 기준을 구조화합니다.',
  oneLineIntro:
    '저는 매체 운영 자체보다, 성과가 어디에서 끊기는지 정의하고 측정 기준과 다음 액션을 명확하게 만드는 Growth Operations형 문제 해결자입니다.',
  email: 'kangbs2486@gmail.com',
  phone: '010-9630-2486',
  location: '서울 관악구',
  githubUrl: 'https://github.com/BANSEOK-KANG1',
  notionUrl: 'https://www.notion.so/DB-326538a06daf8081af93f5dcdcadb04c',
  siteUrl: 'https://banseok-kang1.github.io/Growth/',
  photoPath: 'images/profile.png',
  resumePdfPath: 'files/kang-banseok-resume-growth-operations.pdf',
  portfolioPdfPath: 'files/kang-banseok-portfolio.pdf',
  targetRoles: ['Growth Operations', 'Marketing Analytics', 'CRM / Marketing Ops', 'Growth PM / Product Operations'],
  keywords: ['Growth Operations', 'Marketing Analytics', 'CRM Strategy', 'GA4 / GTM / UTM', 'Funnel Analytics', 'Product Operations']
};

export type EducationEntry = {
  period: string;
  school: string;
  degree: string;
  description?: string;
};

export const education: EducationEntry[] = [
  {
    period: '졸업',
    school: '경상국립대학교',
    degree: '동물생명과학전공'
  }
];
