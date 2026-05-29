export const funnelMetrics = [
  { stage: '광고 노출', metrics: ['CPM', 'Reach', 'Frequency'], question: '타겟이 맞는가?' },
  { stage: '클릭', metrics: ['CTR', 'CPC'], question: '소재/카피가 반응을 만드는가?' },
  { stage: '랜딩', metrics: ['Bounce', 'Scroll', 'CTA Click'], question: '사용자가 설득되는가?' },
  { stage: '전환', metrics: ['CVR', 'CPA', 'Lead Quality'], question: '문의/가입까지 이어지는가?' },
  { stage: '후속', metrics: ['Meeting Rate', 'Purchase Rate', 'ROAS'], question: '진짜 매출로 연결되는가?' },
  { stage: 'CRM', metrics: ['Open Rate', 'CTR', 'Retention'], question: '다시 행동하게 만드는가?' }
];

export type DecisionType = 'expand' | 'maintain' | 'reduce' | 'experiment';

export type FunnelRow = {
  channel: string;
  campaign: string;
  adContent: string;
  landingPage: string;
  utmSource: string;
  utmMedium: string;
  utmCampaign: string;
  spend: number;
  impression: number;
  click: number;
  lead: number;
  qualifiedLead: number;
  meeting: number;
  revenue: number;
};

export type ChannelSummary = {
  channel: string;
  spend: number;
  impression: number;
  click: number;
  lead: number;
  qualifiedLead: number;
  meeting: number;
  revenue: number;
  ctr: string;
  cpc: string;
  cvr: string;
  cpa: string;
  roas: string;
  leadQuality: string;
  meetingRate: string;
  decision: DecisionType;
  action: string;
};

export type CrmSegment = {
  id: string;
  name: string;
  problem: string;
  message: string;
  metrics: string[];
  priority: 'high' | 'medium' | 'low';
};

const formatWon = (value: number) => {
  if (value >= 1_000_000) return `₩${(value / 1_000_000).toFixed(1)}M`;
  if (value >= 1_000) return `₩${Math.round(value / 1_000)}K`;
  return `₩${value}`;
};

const formatPercent = (value: number) => `${value.toFixed(1)}%`;

export const calcCtr = (click: number, impression: number) => (impression ? (click / impression) * 100 : 0);
export const calcCpc = (spend: number, click: number) => (click ? spend / click : 0);
export const calcCvr = (lead: number, click: number) => (click ? (lead / click) * 100 : 0);
export const calcCpa = (spend: number, lead: number) => (lead ? spend / lead : 0);
export const calcRoas = (revenue: number, spend: number) => (spend ? (revenue / spend) * 100 : 0);
export const calcLeadQuality = (qualifiedLead: number, lead: number) => (lead ? (qualifiedLead / lead) * 100 : 0);
export const calcMeetingRate = (meeting: number, qualifiedLead: number) =>
  qualifiedLead ? (meeting / qualifiedLead) * 100 : 0;

export const funnelRows: FunnelRow[] = [
  {
    channel: 'Meta',
    campaign: 'lead_quality_v2',
    adContent: 'video_case_a',
    landingPage: '/landing/main',
    utmSource: 'meta',
    utmMedium: 'paid_social',
    utmCampaign: 'lead_quality_v2',
    spend: 24_000_000,
    impression: 1_850_000,
    click: 38_400,
    lead: 1_460,
    qualifiedLead: 613,
    meeting: 184,
    revenue: 92_000_000
  },
  {
    channel: 'Meta',
    campaign: 'awareness_test',
    adContent: 'carousel_b',
    landingPage: '/landing/awareness',
    utmSource: 'meta',
    utmMedium: 'paid_social',
    utmCampaign: 'awareness_test',
    spend: 8_500_000,
    impression: 2_100_000,
    click: 21_000,
    lead: 420,
    qualifiedLead: 126,
    meeting: 25,
    revenue: 12_500_000
  },
  {
    channel: 'Naver',
    campaign: 'search_brand',
    adContent: 'keyword_main',
    landingPage: '/landing/search',
    utmSource: 'naver',
    utmMedium: 'search',
    utmCampaign: 'search_brand',
    spend: 10_000_000,
    impression: 520_000,
    click: 19_600,
    lead: 1_000,
    qualifiedLead: 350,
    meeting: 140,
    revenue: 70_000_000
  },
  {
    channel: 'Naver',
    campaign: 'power_content',
    adContent: 'blog_c076',
    landingPage: '/landing/content',
    utmSource: 'naver',
    utmMedium: 'content',
    utmCampaign: 'power_content',
    spend: 4_200_000,
    impression: 310_000,
    click: 8_400,
    lead: 380,
    qualifiedLead: 114,
    meeting: 34,
    revenue: 17_000_000
  },
  {
    channel: 'Google',
    campaign: 'remarketing',
    adContent: 'display_rmk',
    landingPage: '/landing/rmk',
    utmSource: 'google',
    utmMedium: 'display',
    utmCampaign: 'remarketing',
    spend: 700_000,
    impression: 180_000,
    click: 2_800,
    lead: 39,
    qualifiedLead: 8,
    meeting: 2,
    revenue: 1_000_000
  },
  {
    channel: 'TikTok',
    campaign: 'install_test',
    adContent: 'short_video_c',
    landingPage: '/landing/tiktok',
    utmSource: 'tiktok',
    utmMedium: 'paid_social',
    utmCampaign: 'install_test',
    spend: 3_000_000,
    impression: 980_000,
    click: 15_800,
    lead: 300,
    qualifiedLead: 54,
    meeting: 8,
    revenue: 4_000_000
  }
];

const decisionLabels: Record<DecisionType, string> = {
  expand: '확대',
  maintain: '유지',
  reduce: '축소',
  experiment: '실험'
};

export const getDecisionLabel = (decision: DecisionType) => decisionLabels[decision];

export const aggregateByChannel = (rows: FunnelRow[]): ChannelSummary[] => {
  const map = new Map<string, FunnelRow[]>();

  for (const row of rows) {
    const existing = map.get(row.channel) ?? [];
    existing.push(row);
    map.set(row.channel, existing);
  }

  return [...map.entries()].map(([channel, channelRows]) => {
    const totals = channelRows.reduce(
      (acc, row) => ({
        spend: acc.spend + row.spend,
        impression: acc.impression + row.impression,
        click: acc.click + row.click,
        lead: acc.lead + row.lead,
        qualifiedLead: acc.qualifiedLead + row.qualifiedLead,
        meeting: acc.meeting + row.meeting,
        revenue: acc.revenue + row.revenue
      }),
      { spend: 0, impression: 0, click: 0, lead: 0, qualifiedLead: 0, meeting: 0, revenue: 0 }
    );

    const leadQuality = calcLeadQuality(totals.qualifiedLead, totals.lead);
    const meetingRate = calcMeetingRate(totals.meeting, totals.qualifiedLead);
    const cpa = calcCpa(totals.spend, totals.lead);

    let decision: DecisionType = 'maintain';
    let action = '성과 모니터링 유지';

    if (leadQuality >= 35 && meetingRate >= 25) {
      decision = 'expand';
      action = '고품질 리드 캠페인 예산 확대 검토';
    } else if (leadQuality < 25 || (cpa > 100_000 && meetingRate < 15)) {
      decision = 'reduce';
      action = '예산 제한 / 리마케팅·테스트 용도 재정의';
    } else if (leadQuality >= 25 && meetingRate < 20) {
      decision = 'experiment';
      action = '소재·랜딩 실험 후 재평가';
    }

    return {
      channel,
      ...totals,
      ctr: formatPercent(calcCtr(totals.click, totals.impression)),
      cpc: formatWon(calcCpc(totals.spend, totals.click)),
      cvr: formatPercent(calcCvr(totals.lead, totals.click)),
      cpa: formatWon(cpa),
      roas: formatPercent(calcRoas(totals.revenue, totals.spend)),
      leadQuality: formatPercent(leadQuality),
      meetingRate: formatPercent(meetingRate),
      decision,
      action
    };
  });
};

export const channelSummaries = aggregateByChannel(funnelRows);

export const campaignSummaries = funnelRows.map((row) => {
  const leadQuality = calcLeadQuality(row.qualifiedLead, row.lead);
  const meetingRate = calcMeetingRate(row.meeting, row.qualifiedLead);
  const cpa = calcCpa(row.spend, row.lead);
  const cvr = calcCvr(row.lead, row.click);

  let decision: DecisionType = 'maintain';
  if (leadQuality >= 40 && meetingRate >= 28) decision = 'expand';
  else if (leadQuality < 22 || cpa > 130_000) decision = 'reduce';
  else if (cvr < 2.5 && leadQuality >= 30) decision = 'experiment';

  return {
    channel: row.channel,
    campaign: row.campaign,
    spend: formatWon(row.spend),
    cvr: formatPercent(cvr),
    cpa: formatWon(cpa),
    leadQuality: formatPercent(leadQuality),
    meetingRate: formatPercent(meetingRate),
    decision,
    action:
      decision === 'expand'
        ? '예산 확대 후보'
        : decision === 'reduce'
          ? '예산 축소 후보'
          : decision === 'experiment'
            ? 'A/B 실험 우선'
            : '현 수준 유지'
  };
});

export const meetingPriority = [...campaignSummaries].sort(
  (a, b) => parseFloat(b.meetingRate) - parseFloat(a.meetingRate)
);

/** @deprecated Use channelSummaries — kept for backward compat during migration */
export const dashboardSample = channelSummaries.map((row) => ({
  channel: row.channel,
  spend: formatWon(row.spend),
  cvr: row.cvr,
  cpa: row.cpa,
  leadQuality: row.leadQuality,
  action: row.action
}));

export const crmSegments: CrmSegment[] = [
  {
    id: 'incomplete-inquiry',
    name: '문의 미완료',
    problem: '광고 클릭 후 랜딩까지 왔지만 문의를 완료하지 않은 유저',
    message: '사례/혜택/FAQ 중심 리마인드',
    metrics: ['재방문율', 'CTA 클릭률', '문의 완료율'],
    priority: 'high'
  },
  {
    id: 'no-meeting',
    name: '미팅 미진행',
    problem: '문의는 완료했지만 상담/미팅으로 이어지지 않은 리드',
    message: '상담 프로세스 안내 + 신뢰 콘텐츠',
    metrics: ['미팅 전환율', '메시지 오픈율', 'CTA 클릭률'],
    priority: 'high'
  },
  {
    id: 'no-purchase',
    name: '구매 미전환',
    problem: '미팅 후 구매/계약으로 이어지지 않은 잠재고객',
    message: '비교표, 후기, 가격/조건 안내',
    metrics: ['구매 전환율', '상담→계약 리드타임'],
    priority: 'medium'
  },
  {
    id: 'returning-customer',
    name: '재방문/재구매',
    problem: '기존 고객의 재방문·재구매가 낮은 구간',
    message: '시즌별 혜택, 업셀/크로스셀 메시지',
    metrics: ['재구매율', 'LTV', '리텐션'],
    priority: 'medium'
  }
];

export const beforeAfterComparison = {
  before: {
    title: 'CPA 단일 기준',
    items: [
      '매체 대시보드 CTR/CPC만 비교',
      'CPA 낮은 캠페인에 예산 집중',
      '리드 품질·미팅 전환 미반영',
      'CRM 후속 액션과 분리'
    ]
  },
  after: {
    title: '리드 품질 + 미팅 기준',
    items: [
      '채널–캠페인–UTM–리드 상태값 연결',
      '진성문의율·미팅 전환율 함께 판단',
      '예산 확대/축소 후보 분리',
      'CRM 리마인드 세그먼트까지 연결'
    ]
  }
};
