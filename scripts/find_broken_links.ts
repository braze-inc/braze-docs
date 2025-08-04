/**
 * Scans Markdown files in the documentation folder for broken links.
 * Uses 'assets/js/broken_redirect_list.js' to determine valid redirects.
 *
 * Usage: ./bdocs fblinks
 */

import { existsSync, link } from 'fs';
import path, { resolve } from 'path';
import fs from 'fs';
import { execSync } from 'child_process';

const PROJECT_ROOT = execSync('git rev-parse --show-toplevel', { encoding: 'utf8' }).trim();

const redirectList: string[] = Object.keys(require(path.join(PROJECT_ROOT, 'assets/js/broken_redirect_list.js')));
const docsBasePath = path.join(PROJECT_ROOT, '_docs');
interface LinkData {
  sourceFile: string;
  link: string;
  markdownFile: string;
}

/**
 * Converts a URL path to its corresponding markdown file path
 * @param link - The URL path to convert (e.g., "/user_guide/administrative")
 * @returns The corresponding markdown file path
 */
const convertLinkToMarkdownPath = (link: string): string => {
  // Remove leading and trailing slashes
  const trimmedLink = link.replace(/^\/|\/$/g, '');

  // Split the path into segments
  const segments = trimmedLink.split('/');

  // If there's only one segment, return simple _docs path
  if (segments.length === 1) {
    return path.join(docsBasePath, `${segments[0]}.md`);
  }

  // Add underscore to first segment
  const docPath = path.join(docsBasePath, `_${segments[0]}`);

  // Add remaining path segments
  const remainingPath = segments.slice(1).join('/');

  // Combine paths and add .md extension
  return path.join(docPath, `${remainingPath}.md`);
};

const getLinks = (filePath: string): {links: LinkData[], aliases: string[], permalinks: string[]} => {
  if (!filePath) {
    process.exit(1);
  }

  let content: string;
  try {
    const raw = fs.readFileSync(filePath, 'utf8');
    content = raw.replace(/``````[\s\S]*?``````|```[\s\S]*?```/g, '');
    content = content.replace(/<script[\s\S]*?<\/script>/gi, '');
    content = content.replace(/<style[\s\S]*?<\/style>/gi, '');
    content = content.replace(/`[^`\n]+`/g, '');
  } catch (err) {
    console.error(`Error reading file: ${err}`);
    process.exit(1);
  }

  /**
   * Remove templated base URL, trim whitespace, and remove any hash fragments.
   */
  function cleanUrl(url: string): string {
    // Remove {{ site.baseurl }} variations (with or without spaces)
    url = url.replace(/{{\s*site\.baseurl\s*}}/g, '');
    url = url.trim();
    // Remove any hash fragment (e.g., /with/path#hash becomes /with/path)
    url = url.split('#')[0].trim();
    url = url.split('?')[0].trim();
    url = url.split(' ')[0].trim();
    return url;
  }

  /**
   * Returns true if the URL:
   * - Starts with a slash (i.e. a full/relative URL)
   * - And its last segment does not look like a file (i.e. has no extension).
   */
  function isValidLink(url: string): boolean {
    if (!url.startsWith('/')) return false;
    const segments = url.split('/');
    const lastSegment = segments[segments.length - 1];
    // If the last segment contains a dot (.) assume it has an extension
    if (lastSegment.includes('.')) return false;
    return true;
  }

  // Build a mapping of reference definitions from lines like: [ref]: URL
  const refMap: Record<string, string> = {};
  const refDefRegex = /^\s*\[([^\]]+)\]:\s*(.+)$/gm;
  let match;
  while ((match = refDefRegex.exec(content)) !== null) {
    const refId = match[1].trim();
    let url = cleanUrl(match[2]);
    refMap[refId] = url;
  }

  // Collect links from inline and reference-style markdown links
  let links: string[] = [];
  let aliases: string[] = [];
  let permalinks: string[] = [];

  // 1. Standard inline links: [text](URL)
  //    Skip any image links (those prefixed with an exclamation mark).
  const inlineRegex = /(!?)\[(.*?)\]\((.*?)\)/g;
  while ((match = inlineRegex.exec(content)) !== null) {
    const isImage = match[1] === '!';
    if (isImage) continue;
    let url = cleanUrl(match[3]);
    if (isValidLink(url)) {
      links.push(url);
    }
  }

  // 2. Reference-style links: [text][ref]
  const refLinkRegex = /\[(.*?)\]\[([^\]]+)\]/g;
  while ((match = refLinkRegex.exec(content)) !== null) {
    const refId = match[2].trim();
    if (refMap[refId]) {
      let url = cleanUrl(refMap[refId]);
      if (isValidLink(url)) {
        links.push(url);
      }
    }
  }

  // 3. Alternative pattern for non-standard inline links like: [link( {{site.baseurl}}/with/path)
  //    This regex handles the case where the closing bracket for the text is missing.
  const altRegex = /(!?)\[(.*?)\(\s*(.*?)\)/g;
  while ((match = altRegex.exec(content)) !== null) {
    const isImage = match[1] === '!';
    if (isImage) continue;
    let url = cleanUrl(match[3]);
    if (isValidLink(url)) {
      links.push(url);
    }
  }

  const aliasRegex = /alias:\s*(.*?)\s*$/gm;
  while ((match = aliasRegex.exec(content)) !== null) {
    aliases.push(match[1]);
  }

  const permalinkRegex = /permalink:\s*(.*?)\s*$/gm;
  while ((match = permalinkRegex.exec(content)) !== null) {
    permalinks.push(match[1]);
  }

  // Remove duplicate links
  links = Array.from(new Set(links));
  aliases = Array.from(new Set(aliases));

  const results = links.map(link => {
    const markdownPath = convertLinkToMarkdownPath(link);
    
    return {
      sourceFile: filePath,
      link: link,
      markdownFile: markdownPath
    }
  });

  return {links: results, aliases, permalinks}
};

let totalFiles = 0;
const links: LinkData[] = [];
const aliases: string[] = [];
const permalinks: string[] = [];
const ignored_files: string[] = [];
function getLinksRecursive(dir: string) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const filePath = path.join(dir, file);
    if (fs.statSync(filePath).isDirectory()) {
      getLinksRecursive(filePath);
    } else {
      if (ignored_files.includes(filePath)) {
        continue;
      }
      const data = getLinks(filePath);
      links.push(...data.links);
      aliases.push(...data.aliases);
      permalinks.push(...data.permalinks);
      totalFiles++;
    }
  }
}

getLinksRecursive(docsBasePath);

// Create CSV header
const headers = ['File', 'Broken Link', 'Path to Broken Link'];
const csv: string[] = [];

// Process each result
for (const item of links) {
  const fullLink = `/docs${item.link}`;
  let exists = fs.existsSync(path.join(item.markdownFile));
  if (!exists) {
    // Check if any redirect matches the link pattern
    const redirectRegex = new RegExp(`(/docs)?${item.link.replace(/\/$/, '')}/?`);
    const redirectMatches = redirectList.some(redirect => {
      return redirectRegex.test(redirect);
    });

    const aliasRegex = new RegExp(`(/docs)?${item.link.replace(/\/$/, '')}/?`);
    const aliasMatches = aliases.some(alias => {
      return aliasRegex.test(alias);
    });

    const permalinkRegex = new RegExp(`(/docs)?${item.link.replace(/\/$/, '')}/?`);
    const permalinkMatches = permalinks.some(permalink => {
      return permalinkRegex.test(permalink);
    });

    if (redirectMatches || aliasMatches || permalinkMatches) {
      exists = true;
    }
  }
  if (!exists) {
    csv.push(`${item.sourceFile},${fullLink},${item.markdownFile}`);
  }
}

const deduplicated = Array.from(new Set(csv)).sort();

fs.writeFileSync(path.join(PROJECT_ROOT, '/scripts/temp/broken-links.csv'), [headers, ...deduplicated].join('\n'));

if (deduplicated.length === 0) {
  console.log('No broken links found.');
} else {
  console.log(`${deduplicated.length} broken links were found. The full list can be found at:\n  ${path.join(PROJECT_ROOT, 'scripts/temp/broken-links.csv')}\n`);
}
