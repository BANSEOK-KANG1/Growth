import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

export default defineConfig({
  site: 'https://BANSEOK-KANG1.github.io',
  base: '/Growth/',
  integrations: [mdx()],
  markdown: {
    shikiConfig: {
      theme: 'github-light'
    }
  }
});
