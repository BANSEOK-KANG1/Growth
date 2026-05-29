# Meta Creative Intelligence

Meta Marketing API로 광고 **소재 메타데이터**(카피, CTA, 포맷)와 **성과 지표**(CTR, CPA, CVR)를 통합해, 다음 소재/영상 방향을 제안하는 Streamlit 앱입니다.

## Live demo (Railway)

배포 후 공개 URL에서 **Sample mode**로 바로 사용할 수 있습니다. Meta 실데이터는 Railway Variables에 토큰을 넣고 앱에서 **Meta API 사용** 토글을 켜세요.

포트폴리오 목업: [Meta Creative Intelligence](https://banseok-kang1.github.io/Growth/projects/meta-creative-intelligence/)

---

## Railway 배포

### 1. Railway에서 새 서비스 생성

1. [Railway](https://railway.app/) → **New Project** → **Deploy from GitHub repo**
2. Repo: `BANSEOK-KANG1/Growth`
3. **Settings → Root Directory**: `apps/meta-creative-analyzer`
4. Builder: Dockerfile ( `railway.toml` 자동 인식 )

### 2. 환경 변수 (Variables)

| Variable | 필수 | 설명 |
|----------|------|------|
| `META_ACCESS_TOKEN` | 선택 | Meta Marketing API 토큰 (없으면 Sample mode) |
| `META_AD_ACCOUNT_ID` | 선택 | `act_1234567890` 형식 |
| `META_API_VERSION` | 선택 | 기본 `v21.0` |

`PORT`는 Railway가 자동 주입합니다.

### 3. 도메인

**Settings → Networking → Generate Domain** → `https://xxx.up.railway.app` 발급

### 4. 포트폴리오 Live Demo URL 연결

Railway URL을 받은 뒤 GitHub repo **Settings → Secrets and variables → Actions** 에 추가:

```
PUBLIC_META_CREATIVE_APP_URL=https://your-app.up.railway.app
```

포트폴리오 재배포 시 프로젝트 페이지 **Live App** 버튼이 활성화됩니다.

### CLI 배포 (선택)

```bash
npm i -g @railway/cli
railway login
cd apps/meta-creative-analyzer
railway link
railway up
railway domain
```

---

## 로컬 실행

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
4. `.env` 또는 Railway Variables:

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

- 토큰·광고계정 ID는 **GitHub에 commit하지 마세요**
- Railway Variables 또는 로컬 `.env`만 사용
- 공개 URL은 기본 Sample mode — Meta API는 본인만 토글 ON
