#!/usr/bin/env python3

# A script used to generate the list of pages on Braze Docs linking to Braze
# blog posts. This is a misc. utility script used to automate the content found 
# on this confluence page:
# https://confluence.braze.com/display/PDT/List+of+pages+linking+to+Braze+blog+posts
# 
# Usage: ./scripts/utils/get_blog_links.py

import os
import re
import subprocess
from collections import defaultdict

# Constants
PROJECT_ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode('utf-8').strip()
SEARCH_DIR = PROJECT_ROOT+"/_docs"

# Regex: non-image Markdown links with "learning.braze.com"
LINK_PATTERN = re.compile(r"(?<!\!)\[([^\]]+)\]\(([^)]*learning\.braze\.com/[^)]*)\)")

# Gets the article title from the page's YAML front matter.
def get_article_title(file_content):
    for line in file_content.splitlines():
        stripped = line.strip()
        if stripped.startswith("article_title:"):
            # Everything after the first colon:
            val = stripped.split(":", 1)[1].strip().strip("'\"")
            return val if val else None
    return None

# 1. Collect data into dictionary
page_titles = {}
file_blogs = defaultdict(set)

for root, _, files in os.walk(SEARCH_DIR):
    for fname in files:
        if fname.endswith(".md"):
            file_path = os.path.join(root, fname)
            
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Get article title
            title = get_article_title(content)
            if not title:
                # Fallback: use filename minus .md
                title = os.path.splitext(fname)[0]
            page_titles[file_path] = title
            
            # Find all non-image links referencing learning.braze.com
            matches = LINK_PATTERN.findall(content)
            for (_, blog_url) in matches:
                file_blogs[file_path].add(blog_url)

# 2. Remove any blog_url containing '{%'
for path, urls in file_blogs.items():
    file_blogs[path] = {u for u in urls if "{%" not in u}

# 3. Drop files with no valid links
file_blogs = {p: urls for p, urls in file_blogs.items() if urls}

# 4. Output in a Markdown table
print("# List of pages linking to Braze blogs")
print(f"_Total pages found: {len(file_blogs)}_\n")
print("| Page | Links |")
print("|------|-------|")

for md_file, blog_urls in file_blogs.items():
    article_title = page_titles[md_file]
    
    docs_url = md_file
    if "_docs/_" in docs_url:
        docs_url = docs_url.replace("_docs/_", "", 1)
    if docs_url.endswith(".md"):
        docs_url = docs_url[:-3]
    docs_url = "https://www.braze.com/docs/" + docs_url
    
    # Left column: [article_title](docs_url)
    left_col = f"[{article_title}]({docs_url})"
    
    # Right column: bullet list of blog URLs
    bullet_list = "<ul>"
    for url in sorted(blog_urls):
        bullet_list += f"<li>{url}</li>"
    bullet_list += "</ul>"
    
    print(f"|{left_col}|{bullet_list}|")
