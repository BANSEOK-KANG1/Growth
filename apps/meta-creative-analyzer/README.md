# Growth Analytics Hub

Meta Creative Intelligence + YouTube KR Trends — Streamlit 멀티페이지 앱.

포트폴리오: [Growth Portfolio](https://banseok-kang1.github.io/Growth/)

---

## 앱 구성

| 페이지 | 설명 | API |
|--------|------|-----|
| **Meta Creative** | 소재 메타 + CPA/CTR → Direction Brief | Meta (Sample 기본) |
| **Keyword Gap → Shoot Brief** | 마케팅 키워드 vs KR 트렌딩 gap → 이번 주 촬영 1편 | YouTube Data API |

---

## Streamlit Cloud 배포

| 항목 | 값 |
|------|-----|
| Repository | `BANSEOK-KANG1/Growth` |
| Branch | `main` |
| Main file path | `apps/meta-creative-analyzer/app.py` |

**Secrets (Streamlit Cloud → Settings → Secrets):**

```toml
YOUTUBE_API_KEY = "your_google_cloud_api_key"

# Meta (선택)
META_ACCESS_TOKEN = "..."
META_AD_ACCOUNT_ID = "act_..."
META_API_VERSION = "v21.0"
```

**Live URLs**

- Hub: `https://growth-peter.streamlit.app/`
- Meta: `.../Meta_Creative`
- YouTube: `.../YouTube_KR_Trends`

---

## YouTube API Key 발급 (무료)

1. [Google Cloud Console](https://console.cloud.google.com/) → 프로젝트 생성
2. **YouTube Data API v3** 활성화
3. **Credentials → API Key** 생성
4. API Key 제한 → YouTube Data API v3만 허용 (권장)

일일 쿼터 10,000 units — 트렌딩(1 unit) + 키워드 검색(100 units/회) 충분.

---

## 로컬 실행

```bash
cd apps/meta-creative-analyzer
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # YOUTUBE_API_KEY 등 입력
streamlit run app.py
```

---

## YouTube Content Brief 로직

- **Overview:** 영상 수, 평균 조회수/engagement, Shorts 비율, 카테고리 mix
- **Keyword vs Trending:** SaaS, AI 마케팅, CRM 등 vertical 키워드 overlap · engagement gap
- **Pattern:** 카테고리 / Shorts / 제목 훅(질문형, How-to 등)별 engagement
- **Content Brief:** 추천 방향 + 다음 콘텐츠 테스트 4가지 + Markdown/CSV export

---

## 포트폴리오 Live App 연결

GitHub `Growth` repo → **Settings → Variables**:

```
PUBLIC_GROWTH_APP_URL = https://growth-peter.streamlit.app
```

(main push 후 GitHub Pages에 Live 버튼 활성화)

---

## 보안

- API Key / Meta 토큰은 Secrets에만 저장 — commit 금지
- 공개 URL에서 YouTube는 Live API, Meta는 Sample mode 기본
