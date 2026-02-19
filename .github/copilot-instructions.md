# General instructions

These instructions are for contributors using GitHub Copilot to draft or edit documentation for Braze.

## Mandatory: Follow the Braze Docs Style Guide

**All documentation work must follow the Braze Docs Style Guide.** This is non-negotiable.

- **When:** For every review, edit, and newly created content. Before suggesting or accepting any documentation change, consult the relevant style guide topic(s) and apply their guidance.
- **Scope:** The style guide is the single source of truth for writing style, voice and tone, accessibility, inclusive language, language and grammar, punctuation, formatting, images, alerts, API endpoint documentation, and all other documentation standards. Do not rely on abbreviated or out-of-date summaries; use the full style guide.
- **Where to look:** The style guide is split into a parent page and four child topics. Use the parent as an index; open the specific child file(s) that apply to the content you are drafting or reviewing.

  | Path | Use this topic for |
  |------|--------------------|
  | `_docs/_contributing/style_guide.md` | Parent index; links to all style guide topics. Start here to find the right topic. |
  | `_docs/_contributing/style_guide/writing_style_guide.md` | Writing style, voice and tone, accessibility, inclusive language, language and grammar, punctuation, technical documentation, formatting and organizing, linking, glossary. **Use for most doc edits.** |
  | `_docs/_contributing/style_guide/image_style_guide.md` | Image styling, cropping, censorship, emphasizing components, alt text, screenshots. |
  | `_docs/_contributing/style_guide/alerts.md` | When and how to use Important, Note, Tip, and Warning alerts; alert examples and best practices. |
  | `_docs/_contributing/style_guide/api_endpoint_guidelines.md` | API endpoint articles: structure, parameters, naming, rate limits, sample code, Postman. |

- **Action:** When drafting or reviewing docs, open the parent `_docs/_contributing/style_guide.md` to orient, then open and follow the child topic(s) that apply (for example, `writing_style_guide.md` for prose and formatting, `alerts.md` when adding or changing alerts, `api_endpoint_guidelines.md` for API endpoint docs). Reject or correct any suggestion that conflicts with the style guide.

## Pull request titles

The title of the pull request should always match the corresponding issue title.

1. Retrieve the corresponding issue's title from the GitHub context (issue.title).
2. Set the pull request title to exactly match issue.title (PR title := issue.title)
3. Do not hardcode, paraphrase, or insert example text. Preserve the title exactly as written, including the pre-pended Jira ticket number in the format [BD-NUMBER] if present.
4. If no linked issue is found or issue.title is empty, stop and prompt for a valid issue with a properly formatted title.

## Pull request body

The pull request body should always use the [PULL_REQUEST_TEMPLATE](./PULL_REQUEST_TEMPLATE) as a base and add/edit the relevant sections in the template as needed. Specifically the Jira ticket number should always be linked using the following syntax:

```
- [BD-NUMBER](https://jira.braze.com/browse/BD-NUMBER)
```