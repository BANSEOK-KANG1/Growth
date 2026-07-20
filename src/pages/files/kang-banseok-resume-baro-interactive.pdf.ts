import part1 from '../../data/baroResumePdfChunks/part1';
import part2 from '../../data/baroResumePdfChunks/part2';
import part3 from '../../data/baroResumePdfChunks/part3';
import part4 from '../../data/baroResumePdfChunks/part4';
import part5 from '../../data/baroResumePdfChunks/part5';
import part6a from '../../data/baroResumePdfChunks/part6a';
import part6b from '../../data/baroResumePdfChunks/part6b';
import part7 from '../../data/baroResumePdfChunks/part7';

export const prerender = true;

export function GET() {
  const base64 = [part1, part2, part3, part4, part5, part6a, part6b, part7].join('');
  const binary = globalThis.atob(base64);
  const bytes = new Uint8Array(binary.length);

  for (let index = 0; index < binary.length; index += 1) {
    bytes[index] = binary.charCodeAt(index);
  }

  return new Response(bytes, {
    headers: {
      'Content-Type': 'application/pdf',
      'Content-Disposition': 'inline; filename="kang-banseok-resume-baro-interactive.pdf"',
      'Content-Length': String(bytes.byteLength),
      'Cache-Control': 'public, max-age=3600'
    }
  });
}
