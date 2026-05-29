# Growth Performance Portfolio — Kang Banseok

인하우스 퍼포먼스/그로스/CRM 직무 지원을 위한 케이스 스터디형 포트폴리오 사이트입니다.

핵심 포지셔닝은 다음과 같습니다.

> 광고비가 실제 문의·가입·매출로 이어지는 흐름을 추적하고, 지표 기반으로 개선 액션을 설계하는 퍼포먼스/그로스 마케터.

## 사이트 목적

이 포트폴리오는 “툴을 다룰 줄 안다”보다 “성과를 어떻게 판단하고 다음 액션으로 바꾸는가”를 보여주기 위해 설계되었습니다.

- 인하우스 퍼포먼스 마케터 지원
- 그로스 마케터 지원
- CRM/Marketing Ops 지원
- Growth PM/PM Assistant 확장 가능성 증명

## 주요 페이지

```txt
/
  Home — 포지셔닝, 핵심 역량, 대표 케이스
/cases
  Case Studies — 실무형 케이스 목록
/cases/performance-funnel-analysis
  광고 성과 분석 및 예산 판단
/cases/ga4-gtm-tracking-system
  GA4/GTM/UTM 전환 측정 구조
/cases/global-app-growth-funnel
  글로벌 앱 유입–설치–전환 퍼널
/cases/crm-retention-scenario
  CRM/그로스 실험 시나리오
/projects/marketing-lead-dashboard
  신규 프로젝트: 마케팅 리드 퍼널 대시보드
/resume
  이력서 요약
/about
  일하는 방식과 강점
/contact
  연락처 및 링크
```

## 기술 스택

- Astro
- MDX
- TypeScript
- CSS Custom Properties
- GitHub Pages
- GitHub Actions

## 실행 방법

```bash
npm install
npm run dev
```

브라우저에서 `http://localhost:4321`로 확인합니다.

## 빌드

```bash
npm run build
npm run preview
```

## GitHub Pages 배포

이 저장소에는 `.github/workflows/deploy.yml`이 포함되어 있습니다.

1. GitHub 저장소를 생성합니다.
2. 이 폴더의 파일을 push합니다.
3. GitHub 저장소의 `Settings > Pages`에서 `Build and deployment`를 `GitHub Actions`로 설정합니다.
4. `main` 브랜치에 push하면 자동으로 배포됩니다.

### URL 방식

개인 메인 사이트로 배포할 경우:

```txt
https://github-username.github.io
```

프로젝트 저장소로 배포할 경우:

```txt
https://github-username.github.io/growth-performance-portfolio/
```

프로젝트 저장소 방식이면 GitHub Actions 환경변수에 다음 값을 추가하세요.

```txt
BASE_PATH=/growth-performance-portfolio
```

## 수정해야 할 개인정보

아래 파일에서 본인 정보로 교체하세요.

```txt
src/data/profile.ts
```

수정 권장 항목:

- email
- githubUrl
- notionUrl
- resumePdfPath
- portfolioPdfPath

PDF 이력서를 넣으려면 다음 폴더에 파일을 추가합니다.

```txt
public/files/
```

## 콘텐츠 수정 방식

케이스 스터디는 MDX 파일로 관리합니다.

```txt
src/content/cases/
```

각 파일의 frontmatter와 본문을 수정하면 사이트에 반영됩니다.

## 주의사항

- 실제 회사 데이터는 익명화하거나 범위값으로 처리하세요.
- 민감한 광고비, 매출, 전환 수치는 그대로 공개하지 마세요.
- 포트폴리오에는 “성과 과장”보다 “판단 기준과 한계 인식”을 명확히 적는 편이 좋습니다.
