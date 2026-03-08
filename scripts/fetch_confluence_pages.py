#!/usr/bin/env python3
"""
Fetch pages from a Confluence space via the Confluence Cloud REST API and write
them to _data/confluence_pages.json for use with the Confluence use-case
library workflow.

Credentials are read from environment variables (never hardcoded).

Required env vars:
  CONFLUENCE_BASE_URL   Base URL of your Confluence (e.g. https://yourcompany.atlassian.net/wiki)
  CONFLUENCE_EMAIL     Your Atlassian account email (used for API auth)
  CONFLUENCE_API_TOKEN Atlassian API token (create at https://id.atlassian.com/manage-profile/security/api-tokens)

Optional:
  CONFLUENCE_SPACE_KEY      Space key to export (e.g. TAM). Used when not using a parent page.
  CONFLUENCE_PARENT_PAGE_ID Parent page ID (numeric). Fetches this page and all descendant pages only.
  CONFLUENCE_PARENT_PAGE_URL Alternatively, the full URL to the parent page (script extracts pageId).

Use either CONFLUENCE_SPACE_KEY (whole space) or CONFLUENCE_PARENT_PAGE_ID / CONFLUENCE_PARENT_PAGE_URL (subset).
Parent page takes precedence if both are set.

Usage:
  # List spaces (to find CONFLUENCE_SPACE_KEY)
  python scripts/fetch_confluence_pages.py --list-spaces

  # Fetch all pages from one space
  CONFLUENCE_SPACE_KEY=TAM python scripts/fetch_confluence_pages.py

  # Fetch only a parent page and its descendants (subset)
  CONFLUENCE_PARENT_PAGE_URL="https://confluence.atl.braze.com/wiki/pages/viewpage.action?pageId=123456789" python scripts/fetch_confluence_pages.py
  # Or: CONFLUENCE_PARENT_PAGE_ID=123456789 python scripts/fetch_confluence_pages.py

Output:
  _data/confluence_pages.json  List of pages with id, title, spaceKey, link, body (HTML), labels, etc.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import List, Optional, Tuple

try:
    import requests
except ImportError:
    print("This script requires the 'requests' library. Install with: pip install requests", file=sys.stderr)
    sys.exit(1)


def load_env():
    """Load CONFLUENCE_* from environment. Optionally load from .env file if present."""
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                key, value = key.strip(), value.strip().strip('"\'')
                if key.startswith("CONFLUENCE_") and key not in os.environ:
                    os.environ[key] = value


def _normalize_base_url(base: str) -> str:
    """Ensure base URL has a scheme and ends with /wiki for Confluence REST API."""
    base = (base or "").strip().rstrip("/")
    if not base:
        return ""
    if not base.startswith("http://") and not base.startswith("https://"):
        base = "https://" + base
    if "/wiki" not in base:
        base = base.rstrip("/") + "/wiki"
    return base.rstrip("/")


def get_auth():
    load_env()
    base = _normalize_base_url(os.environ.get("CONFLUENCE_BASE_URL", ""))
    email = os.environ.get("CONFLUENCE_EMAIL", "")
    token = os.environ.get("CONFLUENCE_API_TOKEN", "")
    if not base or not email or not token:
        print(
            "Set CONFLUENCE_BASE_URL, CONFLUENCE_EMAIL, and CONFLUENCE_API_TOKEN (env or .env file).",
            file=sys.stderr,
        )
        return None, None, None
    return base, email, token


def _request(base: str, email: str, token: str, path: str, params: Optional[dict] = None):
    """GET request to base + path with Basic auth."""
    url = f"{base.rstrip('/')}{path}"
    r = requests.get(
        url,
        auth=(email, token),
        headers={"Accept": "application/json"},
        params=params or {},
        timeout=30,
    )
    if not r.ok:
        msg = f"{r.status_code} {r.reason} for url: {r.url}"
        try:
            body = r.json()
            if body:
                msg += f"\nResponse: {json.dumps(body, indent=2)[:500]}"
        except Exception:
            if r.text:
                msg += f"\nResponse (first 300 chars): {r.text[:300]}"
        raise requests.exceptions.HTTPError(msg, response=r)
    return r.json()


def list_spaces(base: str, email: str, token: str):
    """Fetch all spaces the user can see (Space API)."""
    spaces = []
    start = 0
    limit = 50
    while True:
        data = _request(
            base, email, token,
            "/rest/api/space",
            params={"start": start, "limit": limit},
        )
        results = data.get("results") or []
        spaces.extend(results)
        if len(results) < limit:
            break
        start += limit
    return spaces


def page_id_from_url(url: str) -> Optional[str]:
    """Extract Confluence page ID from a viewpage or spaces URL. Returns None if not found."""
    if not url or not url.strip():
        return None
    # viewpage.action?pageId=123456789
    m = re.search(r"[?&]pageId=(\d+)", url, re.I)
    if m:
        return m.group(1)
    # /spaces/XXX/pages/123456789/Title or /pages/123456789/Title
    m = re.search(r"/pages/(\d+)(?:/|$)", url, re.I)
    if m:
        return m.group(1)
    return None


def get_descendant_page_ids(base: str, email: str, token: str, parent_id: str):
    """Fetch all descendant page IDs under a parent (children, grandchildren, etc.) via REST API."""
    page_ids = []
    start = 0
    limit = 50
    while True:
        data = _request(
            base,
            email,
            token,
            f"/rest/api/content/{parent_id}/descendant/page",
            params={"start": start, "limit": limit},
        )
        results = data.get("results") or []
        for item in results:
            pid = item.get("id")
            if pid:
                page_ids.append((str(pid), item.get("title", "")))
        if len(results) < limit:
            break
        start += limit
    return page_ids


def get_all_pages_in_space(base: str, email: str, token: str, space_key: str):
    """Fetch all page IDs in a space using CQL search (paginated). Do not expand body here to avoid 50-result limit."""
    page_ids = []
    start = 0
    limit = 25
    while True:
        data = _request(
            base,
            email,
            token,
            "/rest/api/content/search",
            params={
                "cql": f'space = "{space_key}" and type = page',
                "start": start,
                "limit": limit,
            },
        )
        results = data.get("results") or []
        for item in results:
            # Search can return content directly or under a "content" key
            content = item.get("content") or item
            pid = content.get("id")
            if pid:
                page_ids.append((str(pid), content.get("title", "")))
        if len(results) < limit:
            break
        start += limit
    return page_ids


def get_page_by_id(base: str, email: str, token: str, page_id: str):
    """Fetch a single page with body.storage (HTML) and labels."""
    return _request(
        base,
        email,
        token,
        f"/rest/api/content/{page_id}",
        params={"expand": "body.storage,body.view,version,metadata.labels"},
    )


def slug(title: str) -> str:
    """Simple URL-safe slug from title."""
    s = re.sub(r"[^\w\s-]", "", title.lower())
    return re.sub(r"[-\s]+", "-", s).strip("-") or "untitled"


def _fetch_pages_by_id_list(base: str, email: str, token: str, page_list: List[Tuple[str, str]], space_key: Optional[str] = None):
    """Fetch full content for each (page_id, title) in page_list. space_key used as fallback in output."""
    out = []
    for i, (page_id, title) in enumerate(page_list):
        try:
            page = get_page_by_id(base, email, token, page_id)
            body_storage = ""
            body_view = ""
            if "body" in page:
                if "storage" in page["body"]:
                    body_storage = page["body"]["storage"].get("value", "")
                if "view" in page["body"]:
                    body_view = page["body"]["view"].get("value", "")
            labels = []
            if "metadata" in page and "labels" in page["metadata"]:
                labels = [lb.get("name") for lb in page["metadata"]["labels"].get("results", []) if lb.get("name")]
            version = page.get("version", {})
            sk = (page.get("space") or {}).get("key") or space_key or ""
            out.append({
                "id": page.get("id"),
                "title": page.get("title", title),
                "spaceKey": sk,
                "link": f"{base}/pages/viewpage.action?pageId={page.get('id')}" if page.get("id") else "",
                "bodyStorage": body_storage,
                "bodyView": body_view,
                "labels": labels,
                "version": version.get("number"),
                "createdAt": page.get("history", {}).get("createdBy", {}).get("when") or page.get("createdAt"),
                "updatedAt": page.get("version", {}).get("when") or page.get("updatedAt"),
                "slug": slug(page.get("title", title)),
            })
            print(f"  [{i+1}/{len(page_list)}] {page.get('title', title)}", file=sys.stderr)
        except Exception as e:
            print(f"  Skip page {page_id} ({title}): {e}", file=sys.stderr)
    return out


def fetch_space_pages(base: str, email: str, token: str, space_key: str):
    """Fetch full content for every page in the space."""
    print(f"Listing pages in space '{space_key}'...", file=sys.stderr)
    page_list = get_all_pages_in_space(base, email, token, space_key)
    print(f"Found {len(page_list)} pages. Fetching content...", file=sys.stderr)
    return _fetch_pages_by_id_list(base, email, token, page_list, space_key)


def fetch_parent_and_descendants(base: str, email: str, token: str, parent_id: str):
    """Fetch the parent page and all its descendant pages (subset of the space)."""
    print(f"Fetching parent page {parent_id}...", file=sys.stderr)
    parent = get_page_by_id(base, email, token, parent_id)
    parent_title = parent.get("title", "")
    space_key = (parent.get("space") or {}).get("key", "")
    print(f"Fetching descendants of '{parent_title}'...", file=sys.stderr)
    descendant_list = get_descendant_page_ids(base, email, token, parent_id)
    page_list = [(parent_id, parent_title)] + descendant_list
    print(f"Found 1 parent + {len(descendant_list)} descendants. Fetching content...", file=sys.stderr)
    return _fetch_pages_by_id_list(base, email, token, page_list, space_key)


def main():
    parser = argparse.ArgumentParser(description="Fetch Confluence space pages for use-case library.")
    parser.add_argument("--list-spaces", action="store_true", help="List space keys and exit.")
    parser.add_argument("--output", default="_data/confluence_pages.json", help="Output JSON file path (default: _data/confluence_pages.json)")
    args = parser.parse_args()

    base, email, token = get_auth()
    if not base:
        sys.exit(1)

    if args.list_spaces:
        spaces = list_spaces(base, email, token)
        print("Spaces (use CONFLUENCE_SPACE_KEY=<key> to fetch pages):")
        for s in spaces:
            print(f"  {s.get('key')}  {s.get('name', '')}")
        return

    # Prefer parent page (subset) over whole space
    parent_id = os.environ.get("CONFLUENCE_PARENT_PAGE_ID", "").strip()
    parent_url = os.environ.get("CONFLUENCE_PARENT_PAGE_URL", "").strip()
    if parent_url and not parent_id:
        parent_id = page_id_from_url(parent_url)
        if not parent_id:
            print("Could not parse page ID from CONFLUENCE_PARENT_PAGE_URL.", file=sys.stderr)
            sys.exit(1)

    if parent_id:
        pages = fetch_parent_and_descendants(base, email, token, parent_id)
        payload = {"parentPageId": parent_id, "pages": pages}
    else:
        space_key = os.environ.get("CONFLUENCE_SPACE_KEY", "").strip()
        if not space_key:
            print(
                "Set CONFLUENCE_SPACE_KEY (whole space) or CONFLUENCE_PARENT_PAGE_ID / CONFLUENCE_PARENT_PAGE_URL (subset).",
                file=sys.stderr,
            )
            sys.exit(1)
        pages = fetch_space_pages(base, email, token, space_key)
        payload = {"spaceKey": space_key, "pages": pages}

    out_path = Path(__file__).resolve().parent.parent / args.output.lstrip("/")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {len(pages)} pages to {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
