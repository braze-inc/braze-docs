### Cross-referencing

To cross-reference pages outside Braze Docs, use [standard Markdown link syntax](https://www.markdownguide.org/basic-syntax/#links). To cross-reference pages on Braze Docs instead, use the following syntax:

{% raw %}
```markdown
[LINK_TEXT]({{site.baseurl}}/SHORT_URL)
```
{% endraw %}

Replace the following:

| Placeholder  | Description                                            |
|--------------|--------------------------------------------------------|
| `LINK_TEXT`  | The page title or related action.                      |
| `SHORT_URL`  | The page URL with `https://www.braze.com` removed. |

Your cross-reference link should be similar to the following:

{% raw %}
```markdown
Before continuing, [create your SSH token]({{site.baseurl}}/docs/developer_guide/platform_wide/sdk_authentication).
```
{% endraw %}

{% alert note %}
For a full walkthrough, see [Cross-referencing]({{site.baseurl}}/home/contributing/content_management/cross_referencing/).
{% endalert %}