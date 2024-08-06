---
nav_title: Page Layouts
article: Page layouts
description: "These are the page layouts that can be assigned to the `page_layout` key in a page's YAML front matter."
page_order: 2
noindex: true
---

#  Page layouts

> These are the page layouts that can be assigned to the [`page_layout`]({{site.baseurl}}/contributing/yaml_front_matter/metadata/#page-layout) key in a page's YAML front matter. For more general information, see [About content management]({{site.baseurl}}/contributing/content_management/#layouts).

## Prerequisites

To use a page layout, you'll need to add the [`page_layout`]({{site.baseurl}}/contributing/yaml_front_matter/metadata/#page-layout) key to your YAML front matter.

```markdown
---
nav_title: Getting started
article_title: Getting started with Braze Docs
page_layout: PAGE_LAYOUT_VALUE
---
```

Replace `PAGE_LAYOUT_VALUE` with one of the values from the following sections.

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

The `featured` value is used to apply the featured page format. In the following example, this format is applied to the [Predictive Events]({{site.baseurl}}/user_guide/sage_ai/predictive_suite/predictive_events) page:

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
For example:<br>
guide_top_text: ><br>
&nbsp;&nbsp;&nbsp;&nbsp;# This is example Markdown formatting
{% endalert %}

## Other layouts

### Blank config

The `blank_config` value is combined with `config_only: true` to make the current article a folder. This lets you create subsections without needing a landing page. Because the landing page becomes a folder and has no page content, users who try to visit the URL directly are automatically redirected to `www.braze.com/docs`. For more information, see [Redirecting URLs]({{site.baseurl}}/contributing/content_management/redirecting_urls/?tab=home%20page#redirecting-a-page).

### Redirect

The `redirect` value is used to redirect the URL for an in-page heading. For more information, see [Redirecting URLs]({{site.baseurl}}/contributing/content_management/redirecting_urls/#redirecting-a-heading).
