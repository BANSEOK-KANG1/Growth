# Growth Performance Portfolio — Kang Banseok

인하우스 퍼포먼스/그로스/CRM 직무 지원을 위한 케이스 스터디형 포트폴리오 사이트입니다.

**Live:** [https://banseok-kang1.github.io/Growth/](https://banseok-kang1.github.io/Growth/)

> 광고비가 실제 문의·가입·매출로 이어지는 흐름을 추적하고, 지표 기반으로 개선 액션을 설계하는 퍼포먼스/그로스 마케터.

## 사이트 구조

```txt
/                     Home
/cases/               Case Studies (4)
/projects/            Projects 목록
/projects/marketing-lead-dashboard/   Featured Dashboard
/resume/              이력서 요약
/about/               일하는 방식
/contact/             연락처
```

## 기술 스택

- Astro 5 + MDX + TypeScript
- CSS Custom Properties (B2B SaaS 스타일)
- GitHub Pages + GitHub Actions

## 로컬 실행

```bash
npm install
npm run dev
```

`http://localhost:4321/Growth/` 에서 확인 (기본 base path: `/Growth/`)

## 빌드

```bash
npm run build
npm run preview
```

## 배포 (GitHub Pages)

1. `main` 브랜치 push
2. GitHub 저장소 Settings → Pages → Source: **GitHub Actions**
3. Repository Variables 설정:
   - `BASE_PATH` = `/Growth`
   - `SITE_URL` = `https://banseok-kang1.github.io`

## 개인정보 수정

[`src/data/profile.ts`](src/data/profile.ts) — email, notionUrl 등  
[`src/data/resume.ts`](src/data/resume.ts) — 경력 타임라인  
[`src/content/cases/`](src/content/cases/) — 케이스 MDX  
[`public/files/`](public/files/) — PDF 이력서·포트폴리오

## 프로젝트 구조

```txt
src/
├── components/     UI (Dashboard, Funnel, BeforeAfter, CRM Panel 등)
├── content/cases/  MDX 케이스 스터디
├── data/           profile, metrics, resume, projects
├── layouts/        BaseLayout, CaseLayout
├── pages/          라우트
└── styles/         global.css
```

## 기획 문서

[`PORTFOLIO_PLAN.md`](PORTFOLIO_PLAN.md) — 포지셔닝, 케이스 방향, 완성 기준

## 주의사항

- 실제 회사 데이터는 익명화하거나 범위값으로 처리
- 성과 과장보다 판단 기준과 한계 인식을 명확히 기술
