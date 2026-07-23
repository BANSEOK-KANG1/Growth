# PDF 파일 위치

이 폴더의 직무별 PDF 이력서는 `/resume/`에서 다운로드·미리보기로 표시됩니다.

## 권장 파일명

```txt
kang-banseok-resume-growth-operations.pdf ← Growth Operations/Marketing Analytics (기본·추천)
kang-banseok-resume-crm-ops.pdf           ← CRM/Marketing Ops
kang-banseok-resume-growth-product.pdf     ← Growth PM/Product Analytics
```

경로 설정: `src/data/profile.ts`, `src/data/resumeDownloads.ts`

재생성:

```bash
python3 scripts/generate_resumes.py
```

스크립트는 최초 실행 시 Google Fonts의 Noto Sans KR을 임시 폴더에 내려받습니다.

## 표시 위치

- **Home** — PDF 존재 시 히어로 다운로드 버튼
- **Header** — Resume PDF 바로가기
- **Resume** — 직무별 트랙·다운로드 + 대표 이력서 iframe 미리보기
- **Contact** — PDF 목록

직무별 파일이 없으면 해당 다운로드 버튼만 비활성 상태로 표시됩니다.
