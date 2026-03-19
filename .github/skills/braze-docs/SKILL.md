---
name: braze-docs
description: >
  This skill applies Braze Docs writing, style, and structural standards when
  drafting, editing, or reviewing documentation. It should be used when working
  on markdown files in _docs/ or _includes/, creating or updating pull requests
  for docs content, reviewing documentation changes, fixing broken links,
  updating cross-references, or adding Liquid formatting. It covers site
  structure, YAML frontmatter, internal linking conventions, redirect
  configuration, Liquid syntax, and page anatomy.
---

# Braze Docs

## Overview

This skill provides the conventions for writing, structuring, and linking Braze
documentation. It covers two areas: writing style (voice, grammar, formatting)
and site structure (frontmatter, linking, Liquid syntax, redirects). For detailed
writing and formatting rules, load [references/writing-style.md](references/writing-style.md).
For the canonical source of truth, consult the full style guide files listed below.

## Style guide source files

| Path | Use for |
|------|---------|
| `_docs/_contributing/style_guide.md` | Parent index — start here |
| `_docs/_contributing/style_guide/writing_style_guide.md` | Writing style, voice, tone, grammar, punctuation, formatting |
| `_docs/_contributing/style_guide/image_style_guide.md` | Image styling, cropping, alt text, screenshots |
| `_docs/_contributing/style_guide/alerts.md` | Important, Note, Tip, Warning alerts — when and how to use |
| `_docs/_contributing/style_guide/api_endpoint_guidelines.md` | API endpoint article structure and formatting |

When the full style guide has specific guidance on a topic, defer to the source file over this summary.

## Writing style summary

The Braze voice is **straightforward**, **empowering**, and **human**. Key rules:

- Active voice. Present tense. Second person ("you"). Imperative for instructions.
- Standard contractions (you're, can't). No noun+verb contractions (Braze'll).
- Oxford comma required. Sentence case for headings.
- Never use "simple", "simply", "just", "easy" in instructions.
- Use "customers" for brands, "consumers" for their end users, "company users" for platform users. Never "clients".
- Descriptive link text. Never "Learn more", "here", "click here".
- Use gender-neutral pronouns. Avoid ableist language.

For the complete writing rules — including UI element formatting, numbers, lists,
punctuation, accessibility, and procedures — load
[references/writing-style.md](references/writing-style.md).

## Site structure

Jekyll site. Collections dir: `_docs/`. Base URL: `/docs`.

| Collection | Folder | Content |
|---|---|---|
| user_guide | `_user_guide/` | Product docs for dashboard users |
| developer_guide | `_developer_guide/` | SDK integration and developer docs |
| api | `_api/` | REST API endpoint docs |
| partners | `_partners/` | Technology partner integrations |
| releases | `_releases/` | Release notes |
| help | `_help/` | Troubleshooting and support |
| contributing | `_contributing/` | Docs contribution guides |

Permalink pattern: `./:collection/:path/` (pretty URLs, trailing slash).

## YAML frontmatter

Every doc file requires YAML frontmatter. Required fields:

```yaml
---
nav_title: Permissions
article_title: Company user permissions
page_order: 1
page_type: reference
description: "This reference article covers how user permissions work at Braze."
---
```

| Field | Purpose | Notes |
|---|---|---|
| `nav_title` | Sidebar navigation label | Short, scannable |
| `article_title` | Page title (H1) | Descriptive, sentence case |
| `page_order` | Sort position in nav | Integer, lower = higher |
| `page_type` | Content type | `reference`, `glossary`, `landing`, `solution` |
| `description` | SEO meta description | Wrap in quotes |

Optional fields: `tool`, `noindex`, `hidden`, `layout`, `local_redirect`, `search_rank`.

## Internal linking

### Link format

```markdown
[Link text]({{site.baseurl}}/user_guide/path/to/page/)
```

- Always use `{{site.baseurl}}` (resolves to `/docs`).
- Trailing slash required.
- Anchor links: `{{site.baseurl}}/user_guide/path/to/page/#heading-slug`
- Same-page anchors: `[heading text](#heading-slug)`

### Cross-referencing child pages

To link from a parent page to a dedicated child page:

```markdown
To learn more, refer to [Topic name]({{site.baseurl}}/user_guide/.../topic_name/).
```

Other acceptable phrases:
- "For more information, see [Topic](...)."
- "For more information about X, see [Topic](...)."

### Same-page references

- "On this page, see [heading](#anchor)."
- "For more information, refer to the section [heading](#anchor)."

## Broken link detection and fixing

To fix a broken or suspect link:

1. Identify the link target path (strip `{{site.baseurl}}` prefix).
2. Check if a file exists at `_docs/_<collection>/<path>.md`.
3. If not, search `assets/js/broken_redirect_list.js` for the path.
4. Follow any redirect chain to the final destination.
5. Verify the final destination file exists.
6. If the link has an anchor (`#slug`), verify the heading exists in the target.
7. Update the link to the current canonical path.
8. If the old path has no redirect entry, add one to `broken_redirect_list.js`.

Heading anchors are auto-generated from heading text: lowercased, spaces become
hyphens, special characters stripped. Example: `## Custom event analytics`
generates `#custom-event-analytics`.

## Redirect configuration

Redirects live in `assets/js/broken_redirect_list.js`:

```javascript
validurls['/docs/user_guide/old_section/old_page/'] = '/docs/user_guide/new_section/new_page/';
```

- One entry per moved path.
- Paths include the `/docs/` prefix, lowercase, trailing slash.
- Collapse redirect chains (old to new directly, not old to intermediate to new).
- Other mechanisms: `layout: redirect` in frontmatter, `local_redirect` for heading-level redirects.

## Liquid syntax

### Alerts

```liquid
{% alert important %}
Must-know caveats, billing impacts, deprecated features, beta status.
{% endalert %}
```

Types: `important`, `note`, `tip`, `warning`. Use sparingly. Do not stack two in a row.

### Tabs

```liquid
{% tabs %}
{% tab Tab Name %}
Content for this tab.
{% endtab %}
{% endtabs %}
```

Use `{% tabs local %}` for tabs that do not sync across the page. Subtabs: `{% subtabs %}` / `{% subtab Name %}`.

### Images

```markdown
![Alt text describing the image.]({% image_buster /assets/img/directory/filename.png %})
```

Optional styling: `{: style="max-width:60%"}`

Alt text: plain language, complete sentence, sentence case. Do not use "image of" or "picture of". Use "and" not "&".

## Page anatomy

### Introduction

Place 1-5 sentences immediately after the H1 heading. Two patterns:

1. **Lead-in paragraph:** Opens the topic with context.
2. **Content statement:** "This reference article covers..."

Use block quotes (`>`) for intro text.

### Prerequisites

Place a `## Prerequisites` section near the top, before the first task heading. Format as bullets, a numbered list, or a table.

## Key glossary

- **Canvas** — Always capitalized. Plural: Canvases.
- **workspace** — Not "app group" (deprecated term).
- **capacity** — Use instead of "limit" for custom data constraints.
- **eCommerce** — Not "ecommerce" or "e-commerce".
- Avoid: "via" (use "through"), "e.g." (use "for example"), "i.e." (use "that is").
- Avoid: "out-of-the-box" (use "default"), "whitelist" (use "allowlist"), "blacklist" (use "blocklist").
