### Cross-referencing other pages

To cross-reference other Braze Docs pages in your content, use the following syntax:

```markdown
[LINK_TEXT]({{site.baseurl}}LINK)
```

Replace the following:

| Placeholder  | Description                                              |
|--------------|----------------------------------------------------------|
| `LINK_TEXT`  | The page title or related action.                        |
| `SHORT_LINK` | The page URL with `https://www.braze.com/docs/` removed. |

Your cross-reference link should be similar to the following:

```markdown
Before continuing, [create your SSH token]({{site.baseurl}}developer_guide/platform_wide/sdk_authentication).
```

{% alert note %}
For a full walkthrough, see [Cross-referencing pages]().
{% endalert %}