---
nav_title: Page Layouts
article: Page layouts
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

### API page

The `api_page` value is used to apply the API page format. In the following example, this format is applied to the [List integrations]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/) page:

{% tabs local %}
{% tab example output %}
![An example page using the 'api_page' layout.]({% image_buster /assets/img/contributing/styling_examples/layouts/api_page.png %})
{% endtab %}
{% endtabs %}

### Developer guide

The `dev_guide` value is used to apply the developer guide format. In the following example, this format is applied to the [Catalogs Endpoints]({{site.baseurl}}/api/endpoints/catalogs) page: 

{% tabs local %}
{% tab example output %}
![An example page using the 'dev_guide' layout.]({% image_buster /assets/img/contributing/styling_examples/layouts/dev_guide.png %})
{% endtab %}
{% endtabs %}

### Featured page

The `featured` value is used to apply the featured page format. In the following example, this format is applied to the [Predictive Events]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events) page:

{% tabs local %}
{% tab example output %}
![An example page using the 'featured' layout.]({% image_buster /assets/img/contributing/styling_examples/layouts/featured.png %})
{% endtab %}
{% endtabs %}

### Glossary page

The `glossary_page` value is used to apply the glossary page format. In the following example, this format is applied to the [Types of push notifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/types) page:

{% tabs local %}
{% tab example output %}
![An example page using the 'glossary_page' layout.]({% image_buster /assets/img/contributing/styling_examples/layouts/glossary_page.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
In certain layouts, a value like `"guide_top_text:"` might benefit from having Markdown formatting. You can use Markdown formatting for certain YAML values. To do so, add `>` as the YAML value, and indent the text afterwards. 
<br>
<code>
For example:<br>
guide_top_text: ><br>
&nbsp;&nbsp;&nbsp;&nbsp;# This is example Markdown formatting
</code>
{% endalert %}

## Other layouts

### `blank_config`

Use `blank_config` and [`config_only: true`]({{site.baseurl}}/contributing/yaml_front_matter/metadata/#navigation-only) to prevent that page's content from being displayed when its selected from the left-side navigation. This is recommended if there's no relevant content worth adding to a [subsection's]({{site.baseurl}}/contributing/content_management/#subsections) landing page.

```markdown
---
layout: blank_config
config_only: true
---
```

In the following example, the `blank_config` and `config_only` keys are used to prevent the **YAML Front Matter** page from displaying its content&#8212;essentially using the page as a visual seperator only.

![The left-side navigation for the Contributing section on Braze Docs. The "YAML Front Matter" page is selected, but the page content shows the previously selected page still.]()

### `redirect`

The `redirect` value is used to redirect a page from the existing URL to a different URL. If you plan on changing the page's filename or change any of the directory names in its relative path, **do not use this method**&#8212;instead, [create a redirect in the `broken_redirect_list.js` file]({{site.baseurl}}/contributing/content_management/redirecting_urls/#redirecting-a-heading).

```markdown
---
layout: redirect
redirect_to: NEW_URL
---
```

Replace `NEW_URL` with the URL you want to redirect to with `https://www.braze.com/` removed from the URL string. In the following example, `_docs/_contributing/content_management/images.md` is set to automatically redirect to `https://www.braze.com/docs/contributing/home`.

```markdown
nav_title: Images
article: Managing Images
description: "Learn how to add, modify, and remove images on Braze Docs."
page_order: 1

layout: redirect
redirect_to: /docs/contributing/home
```
