# General instructions

These instructions are for contributors using GitHub Copilot to draft or edit documentation for Braze.

## Mandatory: Follow the Braze Docs Style Guide

**All documentation work must follow the Braze Docs Style Guide.** This is non-negotiable.

- **Path:** `_docs/_contributing/style_guide.md`
- **When:** For every review, edit, and newly created content. Before suggesting or accepting any documentation change, consult the style guide and apply its guidance.
- **Scope:** The style guide is the single source of truth for writing style, voice and tone, accessibility, inclusive language, language and grammar, punctuation, formatting, images, alerts, API endpoint documentation, and all other documentation standards. Do not rely on abbreviated or out-of-date summaries; use the full style guide.
- **Action:** When drafting or reviewing docs, open and follow `_docs/_contributing/style_guide.md`. Reject or correct any suggestion that conflicts with it.

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