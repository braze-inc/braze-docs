---
nav_title: Cross-referencing pages
page_order: 3
noindex: true
---

# Cross-referencing pages

> Learn how to cross-reference other pages on Braze Docs. To cross-reference pages _outside_ Braze Docs, use [standard Markdown link syntax](https://www.markdownguide.org/basic-syntax/#links).

{% multi_lang_include contributing/prerequisites.md %}

## Create a cross-reference

When creating a cross-reference, you can either use the in-line method or reference-style method. The in-line method prioritizes clarity, while the reference-style method prioritizes readability.

{% tabs %}
{% tab in-line %}
In your text editor, open the file you'd like to edit, then create your in-line link.

{% raw %}
```markdown
[LINK_TEXT]({{site.baseurl}}SHORT_URL)
```
{% endraw %}

Replace the following:

| Placeholder | Description                                             |
|-------------|---------------------------------------------------------|
| `LINK_TEXT` | The page title or related action.                       |
| `SHORT_URL` | The page URL with `https://www.braze.com/docs` removed. |

Your in-line link should be similar to the following:

{% raw %}
```markdown
Before continuing, [create your SSH token]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication).
```
{% endraw %}

{% multi_lang_include contributing/short_creating_a_pull_request.md %}
{% endtab %}
{% tab reference-style %}
In your text editor, open the file you'd like to edit, then create your reference-style link.

```markdown
[LINK_TEXT][REFERENCE_NUMBER]
```

Replace the following:

| Placeholder        | Description                                                              |
|--------------------|--------------------------------------------------------------------------|
| `LINK_TEXT`        | The page title or related action.                                        |
| `REFERENCE_NUMBER` | Any integer not being used by another reference-style link on this page. |

Your references should look similar to the following:

```markdown
Before continuing, [create your SSH token][2]. When you're finished, see [Step 2: Uploading your token][5].
```

At the bottom of the page, you'll add the related links.

{% raw %}
```markdown
[REFERENCE_NUMBER]: {{site.baseurl}}SHORT_URL
```
{% endraw %}

Replace the following:

| Placeholder        | Description                                             |
|--------------------|---------------------------------------------------------|
| `REFERENCE_NUMBER` | The number of the reference you'd like to link to.      |
| `SHORT_URL`        | The page URL with `https://www.braze.com/docs` removed. |

Your links should look similar to the following:

{% raw %}
```markdown
[2]: {{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/
[5]: {{site.baseurl}}/developer_guide/platform_wide/swift#step-2-uploading-your-token
```
{% endraw %}

{% multi_lang_include contributing/short_creating_a_pull_request.md %}
{% endtab %}
{% endtabs %}
