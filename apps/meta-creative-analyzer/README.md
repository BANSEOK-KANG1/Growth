# Meta Creative Intelligence

Meta Marketing API로 광고 **소재 메타데이터**(카피, CTA, 포맷)와 **성과 지표**(CTR, CPA, CVR)를 통합해, 다음 소재/영상 방향을 제안하는 로컬 Streamlit 앱입니다.

## Quick start

```bash
cd apps/meta-creative-analyzer
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # 토큰·광고계정 ID 입력
streamlit run app.py
```

`.env` 없이 실행하면 **Sample data (demo mode)** 로 동작합니다.

## Meta API 설정

1. [Meta Developer](https://developers.facebook.com/) 앱 생성
2. Marketing API `ads_read` 권한 부여
3. System User 또는 Long-lived Access Token 발급
4. `.env` 작성:

```env
META_ACCESS_TOKEN=your_token
META_AD_ACCOUNT_ID=act_1234567890
META_API_VERSION=v21.0
```

5. Streamlit 사이드바에서 **Meta API 사용** 토글 ON

## 기능 (4탭)

| 탭 | 설명 |
|---|---|
| Overview | 소재 수, 평균 CTR/CPA, 포맷 비율 |
| Creative Explorer | 소재별 메타 + 성과 테이블, 필터·정렬 |
| Pattern Analysis | 포맷·훅·CTA별 CPA 비교 |
| Direction Brief | 상위 패턴 요약 + 다음 테스트 제안 |

## 보안

- `.env`와 실제 광고 계정 데이터는 **GitHub에 push하지 마세요**
- 공개 포트폴리오는 익명 샘플 데이터 목업만 사용합니다

## 포트폴리오

웹 데모: [Meta Creative Intelligence](https://banseok-kang1.github.io/Growth/projects/meta-creative-intelligence/)
