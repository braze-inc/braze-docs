
# Cross-referencing

> Learn how to cross-reference other pages on Braze Docs. To cross-reference pages outside Braze Docs, use [standard Markdown syntax](https://www.markdownguide.org/basic-syntax/#links). For general information about cross-references, see [About content management](../content_management.md#cross-references).

<!--
## Prerequisites

If you haven't already, review [Documentation feedback](https://www.braze.com/docs/feedback/) for how to reach the docs team. Full authoring guides for contributors with repository access live under `docs/contributing/` in the braze-docs repo.
-->


## Create a cross-reference

> **Important:**
> Because Liquid's `{% tab %}` tag does not support reference-style links, only in-line links are documented below. Existing reference links will continue to work, but are no longer recommended.



### Markdown

Open the relevant Markdown file, then create your in-line link.
```markdown
[LINK_TEXT](https://www.braze.com/docs/SHORT_URL)
```
Replace the following:

| Placeholder | Description                                        |
|-------------|----------------------------------------------------|
| `LINK_TEXT` | The page title or related action.                  |
| `SHORT_URL` | The page URL with `https://www.braze.com` removed. |


Your in-line link should be similar to the following:
```markdown
Before continuing, [create your SSH token](https://www.braze.com/docs/dev_guide/auth).
```
---

### HTML

Open the relevant Markdown file, then create your in-line link.
```markdown
<a href='[SHORT_URL]'>[LINK_TEXT]</a>
```
Replace the following:

| Placeholder | Description                                        |
|-------------|----------------------------------------------------|
| `LINK_TEXT` | The page title or related action.                  |
| `SHORT_URL` | The page URL with `https://www.braze.com` removed. |


Your in-line link should be similar to the following:
```markdown
To learn about the different custom attribute data types you can use to segment users, view <a href="/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types">Custom attribute data types</a>.
```
