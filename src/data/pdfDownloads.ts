import { profile } from './profile';
import { resumeDownloads, type ResumeDownload } from './resumeDownloads';

export type PdfDownload = ResumeDownload;

export const portfolioDownload: PdfDownload = {
  id: 'portfolio',
  label: '포트폴리오 PDF',
  description: '케이스·프로젝트·역량 요약본',
  filename: profile.portfolioPdfPath,
  tags: ['Portfolio', 'Case Study', 'Projects']
};

export const allPdfDownloads: PdfDownload[] = [...resumeDownloads, portfolioDownload];

export const primaryResumeDownload = resumeDownloads.find((item) => item.primary) ?? resumeDownloads[0];
