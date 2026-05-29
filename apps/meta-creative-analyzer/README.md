# Meta Creative Intelligence

Meta Marketing API로 광고 **소재 메타데이터**(카피, CTA, 포맷)와 **성과 지표**(CTR, CPA, CVR)를 통합해, 다음 소재/영상 방향을 제안하는 Streamlit 앱입니다.

포트폴리오 목업: [Meta Creative Intelligence](https://banseok-kang1.github.io/Growth/projects/meta-creative-intelligence/)

---

## Streamlit Cloud 배포 (권장)

GitHub repo만 있으면 무료로 공개 URL을 받을 수 있습니다.

### 1. Streamlit Cloud 접속

1. [https://share.streamlit.io](https://share.streamlit.io) (Streamlit Community Cloud)
2. **Continue with GitHub** 로 로그인
3. **New app** 클릭

### 2. 앱 설정

| 항목 | 값 |
|------|-----|
| Repository | `BANSEOK-KANG1/Growth` |
| Branch | `main` |
| Main file path | `apps/meta-creative-analyzer/app.py` |

**Deploy** 클릭 → 빌드 완료 후 URL 발급:

```
https://your-app-name.streamlit.app
```

> repo가 안 보이면 GitHub **Settings → Applications → Streamlit** 에서 `Growth` repo 접근 허용.

### 3. Meta API Secrets (선택)

앱 페이지 **⋮ → Settings → Secrets** 에 TOML 형식으로 입력:

```toml
META_ACCESS_TOKEN = "your_token"
META_AD_ACCOUNT_ID = "act_1234567890"
META_API_VERSION = "v21.0"
```

Secrets 없어도 **Sample mode**로 동작합니다. 앱에서 **Meta API 사용** 토글 ON.

### 4. 포트폴리오 Live App 버튼 연결

GitHub `Growth` repo → **Settings → Secrets and variables → Actions → Variables**:

```
PUBLIC_META_CREATIVE_APP_URL = https://your-app-name.streamlit.app
```

main push 또는 Actions **Run workflow** 후 포트폴리오에 **Live App** 버튼 활성화.

---

## 로컬 실행

```bash
cd apps/meta-creative-analyzer
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # 또는 .streamlit/secrets.toml.example → secrets.toml
streamlit run app.py
```

---

## 기능 (4탭)

| 탭 | 설명 |
|---|---|
| Overview | 소재 수, 평균 CTR/CPA, 포맷 비율 |
| Creative Explorer | 소재별 메타 + 성과 테이블, 필터·정렬 |
| Pattern Analysis | 포맷·훅·CTA별 CPA 비교 |
| Direction Brief | 상위 패턴 요약 + 다음 테스트 제안 |

## 보안

- 토큰은 **GitHub/Streamlit Secrets**에만 저장 (commit 금지)
- 공개 URL은 기본 Sample mode
