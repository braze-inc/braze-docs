---
nav_title: Cross-referencing
article: Cross-referencing
description: "Learn how to cross-reference other pages on Braze Docs."
page_order: 3
noindex: true
---

# Cross-referencing

> Learn how to cross-reference other pages on Braze Docs. To cross-reference pages outside Braze Docs, use [standard Markdown syntax](https://www.markdownguide.org/basic-syntax/#links). For general information about cross-references, see [About content management]({{site.baseurl}}/contributing/content_management/#cross-references).

{% multi_lang_include contributing/prerequisites.md %}

## Create a cross-reference

{% alert important %}
Because Liquid's {% raw %}`{% tab %}`{% endraw %} tag does not support reference-style links, only in-line links are documented below. Existing reference links will continue to work, but are no longer recommended.
{% endalert %}

{% tabs %}
{% tab Markdown %}
Open the relevant Markdown file, then create your in-line link.

{% raw %}
```markdown
[LINK_TEXT]({{site.baseurl}}/SHORT_URL)
```
{% endraw %}

Replace the following:

| Placeholder | Description                                        |
|-------------|----------------------------------------------------|
| `LINK_TEXT` | The page title or related action.                  |
| `SHORT_URL` | The page URL with `https://www.braze.com` removed. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Your in-line link should be similar to the following:

{% raw %}
```markdown
Before continuing, [create your SSH token]({{site.baseurl}}/dev_guide/auth).
```
{% endraw %}
{% endtab %}

{% tab HTML %}
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
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Your in-line link should be similar to the following:

{% raw %}
```markdown
To learn about the different custom attribute data types you can use to segment users, view <a href="/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types">Custom attribute data types</a>.
```
{% endraw %}
{% endtab %}
{% endtabs %}
