import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { profile } from '../data/profile';
import { projects } from '../data/projects';

const siteUrl = profile.siteUrl.replace(/\/$/, '');

const staticPaths = [
  '',
  'work/',
  'cases/',
  'projects/',
  'projects/meta-creative-intelligence/',
  'projects/youtube-trend-analyzer/',
  'projects/marketing-lead-dashboard/',
  'resume/',
  'about/',
  'contact/'
];

function escapeXml(value: string) {
  return value
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

export const GET: APIRoute = async () => {
  const cases = await getCollection('cases');
  const casePaths = cases.map((entry) => {
    const slug = String(entry.id).replace(/\.(md|mdx)$/, '');
    return `cases/${slug}/`;
  });

  const projectPaths = projects.map((project) => `projects/${project.slug}/`);
  const allPaths = [...new Set([...staticPaths, ...casePaths, ...projectPaths])];

  const body = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${allPaths
  .map(
    (path) => `  <url>
    <loc>${escapeXml(`${siteUrl}/${path}`)}</loc>
    <changefreq>${path === '' ? 'weekly' : 'monthly'}</changefreq>
    <priority>${path === '' ? '1.0' : path.startsWith('cases/') || path.startsWith('projects/') ? '0.8' : '0.7'}</priority>
  </url>`
  )
  .join('\n')}
</urlset>`;

  return new Response(body, {
    headers: {
      'Content-Type': 'application/xml; charset=utf-8'
    }
  });
};
