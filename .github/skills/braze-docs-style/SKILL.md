---
name: braze-docs-style
description: Apply Braze Docs writing, style, and structural standards when drafting, editing, or reviewing documentation. Use when working on markdown files in _docs/ or _includes/, creating or updating pull requests for docs content, reviewing documentation changes, fixing broken links, updating cross-references, adding Liquid formatting, or when the user asks about Braze documentation conventions.
---

# Braze Docs Style Guide

All documentation must follow the Braze Docs Style Guide. When drafting or reviewing content, apply these rules. Reject or correct any content that conflicts with them.

## Style guide source files

For detailed guidance on any topic, consult the full style guide files:

| Path | Use for |
|------|---------|
| `_docs/_contributing/style_guide.md` | Parent index — start here |
| `_docs/_contributing/style_guide/writing_style_guide.md` | Writing style, voice, tone, grammar, punctuation, formatting |
| `_docs/_contributing/style_guide/image_style_guide.md` | Image styling, cropping, alt text, screenshots |
| `_docs/_contributing/style_guide/alerts.md` | Important, Note, Tip, Warning alerts — when and how to use |
| `_docs/_contributing/style_guide/api_endpoint_guidelines.md` | API endpoint article structure and formatting |

When the full style guide has specific guidance on a topic, defer to the source file over this summary.

## Voice and tone

The Braze voice is **straightforward**, **empowering**, and **human**.

- Explain complicated things simply. Be concise.
- Explain the "why" and "how" to give users confidence to take action.
- Aim for a conversational tone, not a formal one.
- Cut jargon and acronyms. If unavoidable, define them on first use.
- Write for a global audience. Avoid slang, idioms, and culturally specific humor.

## Core writing rules

### Active voice

Use active voice. Avoid passive voice unless de-emphasizing a subject (to avoid blaming the reader) or when who performed the action is unimportant.

- Do: "Braze connects consumers to the brands they love."
- Don't: "Consumers are connected to the brands they love."

### Second person

Address the reader as "you". Avoid first person ("we", "our") except when referring to Braze as an organization. Use the imperative for direct instructions.

- Do: "Upload the CSV file."
- Don't: "You can upload the CSV file." / "We can upload the CSV file."

### Present tense

Use present tense. Avoid "will" or hypothetical "would" for the result of user action.

- Do: "Archived subscription groups cannot be edited and no longer appear in segment filters."
- Don't: "Archived groups cannot be edited and will no longer appear in segment filters."

### Contractions

Use standard contractions (you're, can't, don't) for an approachable tone. Do not use noun+verb contractions (Braze'll) or double contractions (mightn't've).

### Avoid condescending language

Never use "simple", "simply", "just", "easy", or "it's easy" when describing steps or instructions.

### Oxford comma

Always use the Oxford (serial) comma before the last conjunction in a series.

- Do: "campaigns, Canvases, and segments"
- Don't: "campaigns, Canvases and segments"

### Abbreviations

Spell out uncommon abbreviations on first mention, followed by the abbreviation in parentheses. Use the abbreviation for subsequent mentions. Do not spell out common abbreviations (PDF, USB, API, SDK).

- Pluralize without an apostrophe: APIs, SDKs
- Use "a" or "an" based on pronunciation: "an ISP", "a CSV file"

## Inclusive language

- Use gender-neutral pronouns ("they/them/theirs" is always acceptable as singular).
- Use gender-neutral job titles (salesperson, not salesman).
- Avoid ableist language (don't use "crazy", "insane", "blind to", "cripple", "dumb").
- Don't refer to age, disability, race, religion, or ethnicity unless specifically relevant.
- Use "customers" for brands Braze works with. Never say "clients".
- Use "consumers" for customers' customers. Reserve "users" for user-metric contexts.

## Formatting conventions

### Headings and titles

- Use sentence case capitalization for all headings and titles.
- Use gerunds (-ing words) for article titles when applicable.
- Use imperative verbs for task-based headings.
- Don't skip heading levels (h3 follows h2, etc.).
- Use an h1 for page titles only.

### UI elements in instructions

| Element | Formatting | Example |
|---------|-----------|---------|
| Buttons | **Bold** the label. Don't say "the X button". | Click **Add Languages**. |
| Checkboxes | **Bold** the label. Use "select/clear", not "check/uncheck". | Select **Send in local time zone**. |
| Pages | **Bold** the page name. Use "the X page". | Go to the **Segments** page. |
| Tabs | **Bold** the tab name. | Select the **Settings** tab. |
| Filters/operators | `Code text`. Match UI case. | Select the `First Used App` filter. |
| Filenames/paths | `Code text`. | Open the `braze.xml` file. |
| Error messages | "Quotation marks". | "Push Bounced: MismatchSenderId" |
| Metrics (in text) | *Italics* with initial caps. | The *Machine Opens* metric shows... |
| Permissions | "Quotation marks". | Grant the "Manage Segments" permission. |

### Code in text

Use backtick code font for: attribute names/values, API parameters, filenames, file paths, method/variable/parameter names, HTML/XML elements, HTTP status codes, terminal input.

### Lists

- Bulleted lists: unordered information.
- Numbered lists: sequential steps.
- Lettered lists: mutually exclusive options.
- Start each item with a capital letter.
- Omit ending punctuation for single words, fragments without verbs, code items, or link/title items.
- Use parallel syntax across all items.

### Numbers

- Spell out numerals one through nine. Use numerals for 10+.
- Use commas for numbers over three digits (1,000).
- Never start a sentence with a numeral (except years).
- Percentages: use numeral + % with no space (10%). Spell out if starting a sentence.

### Links

- Use descriptive link text. Never use "Learn more", "here", "click here", or "this document".
- Use "For more information, see [Topic Name]" or "For more information about X, see [Topic Name]".
- Match link text to the destination's title or heading.
- Don't place two links back to back without separating text.

### Alerts

Four types: Important, Note, Tip, Warning. Use sparingly.

- **Important:** Essential info (deprecated features, billing impacts, beta status).
- **Note:** One-off caveats or helpful callouts.
- **Tip:** Supplementary knowledge, shortcuts, additional resources.
- **Warning:** Irreversible consequences, feature-breaking behavior, data loss.

Do not use alerts for essential article structure (intros, setup steps). Avoid stacking two or more alerts in a row. Keep alert content short and concise.

## Procedures and instructions

- Don't jump straight into steps. Provide context and list prerequisites first.
- Structure around what the user can do, not what the product can do.
  - Do: "Use this feature to send targeted messages."
  - Don't: "This feature sends targeted messages."
- Provide location steps: "On the **Settings** page, click **Edit**."
- Put conditional clauses first: "If you need X, do A then B."
- Use "When you've" or "After you've" to reinforce task order. Avoid "Once you've" (doesn't translate well).

## Accessibility

- Use plain language. Aim for no more than 20 words per sentence, five sentences per paragraph.
- Front-load sections with the most important information (inverted pyramid).
- Provide alt text for every image.
- Don't use images as the only way to show information.
- Don't use ampersands (&) in place of "and" unless matching UI text.
- Avoid Latin phrases; use simple alternatives.

## Punctuation quick reference

- **Colons:** Introductory sentence must stand alone as a complete sentence before the colon. Bold the colon if preceding text is bold.
- **Semicolons:** Use to separate closely related independent clauses. Use sparingly.
- **Apostrophes:** Singular nouns ending in S take 's (Chris's). Plural nouns ending in S take only ' (users').
- **Ampersands:** Don't use & for "and" in text or headings unless matching UI.

## Describing limitations

Write candidly about product limitations. Don't distort or minimize. Frame limitations with appropriate, positive context without promising future features.

## Reviews

When reviewing content, verify compliance with all rules above. Flag and correct violations. For detailed guidance on any topic, open and follow the relevant source file listed in the table at the top.

---

# Site structure and conventions

This section covers the technical conventions for structuring, linking, and formatting Braze documentation.

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

Every doc file needs YAML frontmatter. Required fields:

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

When a parent page introduces a topic that has its own dedicated child page:

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

When you encounter or suspect a broken link:

1. Identify the link target path (strip `{{site.baseurl}}` prefix).
2. Check if a file exists at `_docs/_<collection>/<path>.md`.
3. If not, search `assets/js/broken_redirect_list.js` for the path.
4. Follow any redirect chain to the final destination.
5. Verify the final destination file exists.
6. If the link has an anchor (`#slug`), verify the heading exists in the target.
7. Update the link to the current canonical path.
8. If the old path has no redirect entry, add one to `broken_redirect_list.js`.

Heading anchors are auto-generated from heading text: lowercased, spaces become hyphens, special characters stripped. Example: `## Custom event analytics` generates `#custom-event-analytics`.

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

Types: `important`, `note`, `tip`, `warning`. Use sparingly. Don't stack two in a row.

### Tabs

```liquid
{% tabs %}
{% tab Tab Name %}
Content for this tab.
{% endtab %}
{% endtabs %}
```

Use `{% tabs local %}` for tabs that don't sync across the page. Subtabs: `{% subtabs %}` / `{% subtab Name %}`.

### Images

```markdown
![Alt text describing the image.]({% image_buster /assets/img/directory/filename.png %})
```

Optional styling: `{: style="max-width:60%"}`

Alt text: plain language, complete sentence, sentence case. Don't use "image of" or "picture of". Use "and" not "&".

## Page anatomy

### Introduction

Place 1-5 sentences immediately after the H1 heading. Two patterns:

1. **Lead-in paragraph:** Opens the topic with context.
2. **Content statement:** "This reference article covers..."

Use block quotes (`>`) for intro text.

### Prerequisites

Place a `## Prerequisites` section near the top, before the first task heading. Format as bullets, a numbered list, or a table.

## Key glossary

| Term | Rule |
|---|---|
| Canvas | Always capitalized. Plural: Canvases. |
| workspace | Not "app group" (deprecated). |
| capacity | Use instead of "limit" for custom data constraints. |
| eCommerce | Not "ecommerce" or "e-commerce". |
| customers | Brands that use Braze. Never "clients". |
| consumers | End users of those brands. |
| company users | People who use the Braze platform. |

Avoid: "via" (use "through"), "e.g." (use "for example"), "i.e." (use "that is"), "simple"/"simply"/"just"/"easy" in instructions, "out-of-the-box" (use "default"), "whitelist" (use "allowlist"), "blacklist" (use "blocklist").
