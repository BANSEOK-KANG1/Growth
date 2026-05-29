import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const cases = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/cases' }),
  schema: z.object({
    title: z.string(),
    subtitle: z.string().optional(),
    category: z.string(),
    period: z.string(),
    order: z.number(),
    summary: z.string(),
    status: z.string(),
    heroMetric: z.string().optional(),
    tools: z.array(z.string()),
    metrics: z.array(z.string())
  })
});

export const collections = { cases };
