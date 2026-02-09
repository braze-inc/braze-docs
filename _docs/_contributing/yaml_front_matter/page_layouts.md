---
nav_title: Page layouts
article_title: Page layouts
description: "These are the page layouts that can be assigned to the `page_layout` key in a page's YAML front matter."
page_order: 2
noindex: true
---

#  Page layouts

> These are the page layouts that can be assigned to the [`page_layout`]({{site.baseurl}}/contributing/yaml_front_matter/metadata/#page-layout) key in a page's YAML front matter. Most `page_layout` keys will visually modify the page&#8212;however, some only modify how the page functions. For more general information, see [About content management]({{site.baseurl}}/contributing/content_management/#layouts).

## Applying a layout

To apply a layout to your page, add the following line to your YAML front matter, then replace `PAGE_LAYOUT_VALUE` with one of the keys found on this page.

```markdown
---
page_layout: PAGE_LAYOUT_VALUE
---
```

## Visual layouts

### `api_page`

The `api_page` layout is used to apply the API page format. In the following example, this format is applied to the [List integrations]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/) page.

```markdown
---
layout: api_page
---
```

{% tabs local %}
{% tab example output %}
![An example page using the 'api_page' layout.]({% image_buster /assets/img/contributing/styling_examples/layouts/api_page.png %})
{% endtab %}
{% endtabs %}

### `dev_guide`

The `dev_guide` layout is used to apply the developer guide format. In the following example, this format is applied to the [Catalogs Endpoints]({{site.baseurl}}/api/endpoints/catalogs) page.

```markdown
---
layout: dev_guide
---
```

{% tabs local %}
{% tab example output %}
![An example page using the 'dev_guide' layout.]({% image_buster /assets/img/contributing/styling_examples/layouts/dev_guide.png %})
{% endtab %}
{% endtabs %}

### `featured`

The `featured` layout is used to apply the featured page format. In the following example, this format is applied to the [Predictive Events]({{site.baseurl}}/user_guide/brazeai/predictive_events/) page.

```markdown
---
layout: featured
---
```

{% tabs local %}
{% tab example output %}
![An example page using the 'featured' layout.]({% image_buster /assets/img/contributing/styling_examples/layouts/featured.png %})
{% endtab %}
{% endtabs %}

### `glossary_page`

The `glossary_page` layout is used to apply the glossary page format. In the following example, this format is applied to the [Types of push notifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/types) page.

```markdown
---
layout: glossary_page
---
```

{% tabs local %}
{% tab example output %}
![An example page using the 'glossary_page' layout.]({% image_buster /assets/img/contributing/styling_examples/layouts/glossary_page.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
In certain layouts, a value like `"guide_top_text:"` might benefit from having Markdown formatting. You can use Markdown formatting for certain YAML values. To do so, add `>` as the YAML value, and indent the text afterwards. For example:<br><br>
<code>
guide_top_text: ><br>
&nbsp;&nbsp;&nbsp;&nbsp;# This is example Markdown formatting
</code>
{% endalert %}

## Other layouts

### `blank_config`

Use the `blank_config` layout with [`config_only: true`]({{site.baseurl}}/contributing/yaml_front_matter/metadata/#navigation-only) to prevent a page's content from displaying when its selected from the left-side navigation. This is helpful when you don't plan on adding content to a [subsection's]({{site.baseurl}}/contributing/content_management/#subsections) landing page.

```markdown
---
layout: blank_config
config_only: true
---
```

{% tabs local %}
{% tab example output %}
![The left-side navigation for the Contributing section on Braze Docs. The "YAML Front Matter" page is selected, but the page content shows the previously selected page still.]({% image_buster /assets/img/contributing/styling_examples/layouts/blank_config.png %})
{% endtab %}
{% endtabs %}

### `redirect`

The `redirect` layout is used to redirect an existing page from its current URL to a different URL of your choice.

{% alert warning %}
Do not use this method if you also plan on moving the file, renaming the file, or renaming any of its parent directories. Instead, [create a redirect in the `broken_redirect_list.js` file]({{site.baseurl}}/contributing/content_management/redirecting_urls/#redirecting-a-heading).
{% endalert %}

```markdown
---
layout: redirect
redirect_to: NEW_URL
---
```

Replace `NEW_URL` with the URL you want to redirect to with `https://www.braze.com/` removed from the URL string.

In the following example, `_docs/_contributing/content_management/images.md` is set to automatically redirect to `https://www.braze.com/docs/contributing/home`.

```markdown
nav_title: Images
article_title: Managing Images
description: "Learn how to add, modify, and remove images on Braze Docs."
page_order: 1

layout: redirect
redirect_to: /docs/contributing/home
```
