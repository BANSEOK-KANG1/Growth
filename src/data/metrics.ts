export const funnelMetrics = [
  { stage: '광고 노출', metrics: ['CPM', 'Reach', 'Frequency'], question: '타겟이 맞는가?' },
  { stage: '클릭', metrics: ['CTR', 'CPC'], question: '소재/카피가 반응을 만드는가?' },
  { stage: '랜딩', metrics: ['Bounce', 'Scroll', 'CTA Click'], question: '사용자가 설득되는가?' },
  { stage: '전환', metrics: ['CVR', 'CPA', 'Lead Quality'], question: '문의/가입까지 이어지는가?' },
  { stage: '후속', metrics: ['Meeting Rate', 'Purchase Rate', 'ROAS'], question: '진짜 매출로 연결되는가?' },
  { stage: 'CRM', metrics: ['Open Rate', 'CTR', 'Retention'], question: '다시 행동하게 만드는가?' }
];

export const dashboardSample = [
  { channel: 'Meta', spend: '₩24.0M', cvr: '3.8%', cpa: '₩68K', leadQuality: '42%', action: '소재 실험 유지 / 고품질 리드 캠페인 분리' },
  { channel: 'Naver', spend: '₩10.0M', cvr: '5.1%', cpa: '₩52K', leadQuality: '35%', action: '전환 키워드 확장 / 검색 의도별 랜딩 분리' },
  { channel: 'Google', spend: '₩0.7M', cvr: '1.4%', cpa: '₩142K', leadQuality: '21%', action: '예산 제한 / 리마케팅 중심 재검토' },
  { channel: 'TikTok', spend: '₩3.0M', cvr: '1.9%', cpa: '₩120K', leadQuality: '18%', action: '인지 목적 실험 / 전환 캠페인 분리' }
];
