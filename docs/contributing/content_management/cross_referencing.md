
# Cross-referencing

> Learn how to cross-reference other pages on Braze Docs. To cross-reference pages outside Braze Docs, use [standard Markdown syntax](https://www.markdownguide.org/basic-syntax/#links). For general information about cross-references, see [About content management](../content_management.md#cross-references).

*Included in the site build from [`_includes/contributing/prerequisites.md`](../../../_includes/contributing/prerequisites.md).*

## Create a cross-reference

> **Important:**
> Because Liquid's {% raw %}`{% tab %}`{% endraw %} tag does not support reference-style links, only in-line links are documented below. Existing reference links will continue to work, but are no longer recommended.



### Markdown

Open the relevant Markdown file, then create your in-line link.

{% raw %}
```markdown
[LINK_TEXT](https://www.braze.com/docs/SHORT_URL)
```
{% endraw %}

Replace the following:

| Placeholder | Description                                        |
|-------------|----------------------------------------------------|
| `LINK_TEXT` | The page title or related action.                  |
| `SHORT_URL` | The page URL with `https://www.braze.com` removed. |


Your in-line link should be similar to the following:

{% raw %}
```markdown
Before continuing, [create your SSH token](https://www.braze.com/docs/dev_guide/auth).
```
{% endraw %}

---

### HTML

Open the relevant Markdown file, then create your in-line link.

{% raw %}
```markdown
<a href='[SHORT_URL]'>[LINK_TEXT]</a>
```
{% endraw %}

Replace the following:

| Placeholder | Description                                        |
|-------------|----------------------------------------------------|
| `LINK_TEXT` | The page title or related action.                  |
| `SHORT_URL` | The page URL with `https://www.braze.com` removed. |


Your in-line link should be similar to the following:

{% raw %}
```markdown
To learn about the different custom attribute data types you can use to segment users, view <a href="/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types">Custom attribute data types</a>.
```
{% endraw %}


