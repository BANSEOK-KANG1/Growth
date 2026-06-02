# PDF 파일 위치

이 폴더에 PDF 이력서와 포트폴리오를 넣으면 사이트에 **자동으로** 다운로드 버튼·미리보기가 표시됩니다.

## 권장 파일명

```txt
kang-banseok-resume-crm-growth.pdf   ← 그로스 마케터 JD Fit 이력서 (기본·추천)
kang-banseok-resume-revised.pdf      ← 한장 이력서 (수정본)
kang-banseok-resume-one-page.pdf     ← 한장 이력서
kang-banseok-resume.pdf              ← 퍼포먼스 마케팅 요약
kang-banseok-portfolio.pdf           ← 포트폴리오 PDF
```

경로 설정: `src/data/profile.ts`, `src/data/resumeDownloads.ts`

## 표시 위치

- **Home** — PDF 존재 시 히어로 다운로드 버튼
- **Header** — Resume PDF 바로가기
- **Resume** — 그리드 다운로드 + iframe 미리보기
- **Contact** — PDF 목록

파일이 없으면 해당 UI는 숨겨지고, Resume 페이지에 안내 문구가 표시됩니다.
