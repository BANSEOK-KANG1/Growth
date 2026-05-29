import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

// GitHub Pages 배포 팁
// 1) username.github.io 저장소로 배포하면 BASE_PATH 없이 그대로 사용
// 2) 프로젝트 저장소(/growth-performance-portfolio/)로 배포하면
//    GitHub Actions 환경변수에 BASE_PATH=/growth-performance-portfolio 를 추가
const site = process.env.SITE_URL || 'https://kangbanseok.github.io';
const base = process.env.BASE_PATH || '/';

export default defineConfig({
  site,
  base,
  integrations: [mdx()],
  markdown: {
    shikiConfig: {
      theme: 'github-light'
    }
  }
});
