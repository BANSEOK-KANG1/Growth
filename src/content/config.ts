import { defineCollection, z } from 'astro:content';

const cases = defineCollection({
  type: 'content',
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
