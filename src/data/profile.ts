export const profile = {
  nameKo: '강반석',
  nameEn: 'Kang Banseok',
  role: 'Growth Performance Marketer',
  headline: '광고 성과와 사용자 행동 데이터를 연결해 유입–전환–리드–CRM 퍼널의 병목을 찾고 개선합니다.',
  summary:
    '퍼포먼스마케팅 실무를 기반으로 광고 유입, 전환 이벤트, 사용자 행동 데이터를 분석하고 측정 가능한 구조로 정리합니다. Meta, Google, Naver, TikTok 운영과 GA4/GTM/UTM/Clarity 기반 전환 측정 경험을 바탕으로 CPA·CVR·ROAS·문의 전환율을 기준으로 다음 액션을 판단합니다.',
  oneLineIntro:
    '저는 광고를 단순히 집행하는 사람이 아니라, 광고비가 어디서 성과로 이어지고 어디서 새는지 추적해 다음 액션으로 바꾸는 퍼포먼스/그로스 마케터입니다.',
  email: 'kangbs2486@gmail.com',
  phone: '010-9630-2486',
  location: '서울 관악구',
  githubUrl: 'https://github.com/BANSEOK-KANG1',
  notionUrl: 'https://www.notion.so/DB-326538a06daf8081af93f5dcdcadb04c',
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
  description?: string;
};

export const education: EducationEntry[] = [
  {
    period: '졸업',
    school: '경상국립대학교',
    degree: '동물생명과학전공'
  }
];
