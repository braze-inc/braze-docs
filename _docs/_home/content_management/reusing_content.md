---
nav_title: Reusing content
page_order: 4
noindex: true
---

# Reusing content

> Learn how to reuse content across Braze Docs, so you can ... For general information about content reuse, see [About our framework]().

{% multi_lang_include contributing/general_getting_started.md %}

## Reusing content

Includes are small page fragments in the `/_docs/_includes/` directory which can be included in multiple places on the site via the include tag. For example:

```plaintext
{% raw %}{% multi_lang_include header.html %}{% endraw %}
```

Like Jekyll pages, articles and layouts, these page fragments can be populated via Liquid templating. Includes in combination with Liquid templating can be extremely useful in preventing redundancy.

How to use include formatting:

1. Create a file in the `includes/archive` folder.
2. Add your content to the markdown file, no introductory YAML/metadata needed.
3. In the files you want to reference the alert, include `{% raw %}{% multi_lang_include archive/alert_name.md %}{% endraw %}`
