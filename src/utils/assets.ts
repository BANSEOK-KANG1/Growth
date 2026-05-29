import fs from 'node:fs';
import path from 'node:path';

export function publicAssetExists(relativePath: string): boolean {
  const normalized = relativePath.replace(/^\//, '');
  return fs.existsSync(path.join(process.cwd(), 'public', normalized));
}

export function publicAssetUrl(base: string, relativePath: string): string {
  return `${base}${relativePath.replace(/^\//, '')}`;
}
