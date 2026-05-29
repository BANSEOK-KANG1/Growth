import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

function normalizeBase(path) {
  if (!path || path === '/') return '/';
  let base = path.startsWith('/') ? path : `/${path}`;
  if (!base.endsWith('/')) base += '/';
  return base;
}

// GitHub Pages: https://github.com/BANSEOK-KANG1/Growth
// Repository Variables: BASE_PATH=/Growth, SITE_URL=https://banseok-kang1.github.io
const site = process.env.SITE_URL || 'https://banseok-kang1.github.io';
const base = normalizeBase(process.env.BASE_PATH || '/Growth/');

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
