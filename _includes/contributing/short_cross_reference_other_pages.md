### Cross-reference other pages

To cross-reference other pages on Braze Docs within your content, use the following syntax:

{% raw %}
```markdown
[LINK_TEXT]({{site.baseurl}}SHORT_URL)
```
{% endraw %}

Replace the following:

| Placeholder  | Description                                             |
|--------------|---------------------------------------------------------|
| `LINK_TEXT`  | The page title or related action.                       |
| `SHORT_URL` | The page URL with `https://www.braze.com/docs` removed. |

Your cross-reference link should be similar to the following:

{% raw %}
```markdown
Before continuing, [create your SSH token]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication).
```
{% endraw %}

{% alert note %}
For a full walkthrough, see [Cross-referencing pages]().
{% endalert %}