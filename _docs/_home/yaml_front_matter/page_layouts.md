---
nav_title: Page Layouts 
page_order: 2
noindex: true
---

#  Page layouts

> The following page layouts can be assigned to the [`page_layout`]({{site.baseurl}}/home/yaml_front_matter/metadata/#page-layout) key in a page's YAML front matter. For more general information, see [About our framework]({{site.baseurl}}/home/about_our_framework/#layouts).

## Prerequisites

To use a page layout, you'll need to add the [`page_layout`]({{site.baseurl}}/home/yaml_front_matter/metadata/#page-layout) key to your YAML front matter:

```markdown
---
nav_title: Getting started
article_title: Getting started with Braze Docs
page_layout: PAGE_LAYOUT_VALUE
---
```

Replace `PAGE_LAYOUT_VALUE` with one of the values from the following sections:

## Accepted values

### API page

The `api_page` value is used to apply the API page format.

{% tabs local %}
{% tab example input %}
```markdown
---
page_layout: api_page
---
```
{% endtab %}

{% tab example output %}
![An example page using the 'api_page' layout.]()
{% endtab %}
{% endtabs %}

### Blank page

The `blank_config` value is used to apply the blank page format. 

{% tabs local %}
{% tab example input %}
```markdown
---
page_layout: blank_config
---
```
{% endtab %}

{% tab example output %}
![An example page using the 'blank_config' layout.]()
{% endtab %}
{% endtabs %}

### Developer guide

The `dev_guide` value is used to apply the developer guide format. 

{% tabs local %}
{% tab example input %}
```markdown
---
page_layout: dev_guide
---
```
{% endtab %}

{% tab example output %}
![An example page using the 'dev_guide' layout.]()
{% endtab %}
{% endtabs %}

### Video page

The `featured_video` value is used to apply the video page format. 

{% tabs local %}
{% tab example input %}
```markdown
---
page_layout: featured_video
---
```
{% endtab %}

{% tab example output %}
![An example page using the 'featured_video' layout.]()
{% endtab %}
{% endtabs %}

### Featured page

The `featured` value is used to apply the featured page format. 

{% tabs local %}
{% tab example input %}
```markdown
---
page_layout: featured
---
```
{% endtab %}

{% tab example output %}
![An example page using the 'featured' layout.]()
{% endtab %}
{% endtabs %}

### Glossary page

The `glossary_page` value is used to apply the glossary page format. 

{% tabs local %}
{% tab example input %}
```markdown
---
page_layout: glossary_page
---
```
{% endtab %}

{% tab example output %}
![An example page using the 'glossary_page' layout.]()
{% endtab %}
{% endtabs %}

### Redirect page URL

The `redirect` value is used to [redirect URLs for in-page headings]({{site.baseurl}}/home/content_management/redirecting_urls/#redirecting-a-heading). 

{% tabs local %}
{% tab example input %}
```markdown
---
page_layout: redirect
---
```
{% endtab %}

{% tab example output %}
![An example page using the 'redirect' layout.]()
{% endtab %}
{% endtabs %}
