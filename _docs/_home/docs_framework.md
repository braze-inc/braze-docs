---
nav_title: Docs framework
page_order: 3
noindex: true
---

# Docs framework

> Braze Docs is built using Jekyll, a framework--or more specifically, a Static-Site Generator (SSG)--for managing docs-as-code repositories.

## Docs-as-code

> TODO: What is docs-as-code?

## Static-site generators

> TODO: What is a static-site generator?

## Languages and file types

> TODO: What is Markdown and YAML, and how does it fit into the big picture?

Articles are written in [Markdown syntax](http://daringfireball.net/projects/markdown/) as .md files housed within the `_docs/` directory. Jekyll uses [kramdown](http://kramdown.gettalong.org/) to parse Markdown files from plain text into HTML. [Configuration for Markdown parsers](http://jekyllrb.com/docs/configuration/#markdown-options) can be set in `_config.yml`.

> TODO: improve/make better examples. Input should be code example, output should be an image.

To be recognized and processed by Jekyll, a file requires YAML Front Matter. Front matter must be the first thing in the file and must take the form of valid YAML set between triple-dashed lines. Here is an example of the front matter in `/_docs/_developer_guide/platform_integration_guides/ios/initial_sdk_setup/initial_sdk_setup.md`:

```yaml
---
nav_title: Set Up
platform: iOS
page_order: 0
search_rank: 5
---
```

> TODO: should we actually be suggesting people to do this, or no?

Front matter can be empty as well, if you want Jekyll to recognize the file but don't care to actually set any variables:

```yaml
---
---
```

Within a file's front matter, you can set [predefined variables](http://jekyllrb.com/docs/frontmatter/#predefined-global-variables) as well as [custom ones](http://jekyllrb.com/docs/frontmatter/#custom-variables). For each file with front matter, Jekyll makes a variety of data available via the [Liquid templating system](https://github.com/Shopify/liquid/wiki). All front matter variables will be available via Liquid tags, both further down in the file and in any layouts or includes that reference the given page. Therefore, in `Creating_a_Segment.md`, `{% raw %}{{ page.title }}{% endraw %}` would render to "Creating a Segment."

More information on front matter variables as data can be found on the [Jekyll Variables documentation](http://jekyllrb.com/docs/variables/) and [Front Matter](https://jekyllrb.com/docs/front-matter/).

## Layouts

Pages are rendered using the HTML files stored in the `/_docs/_layouts/` directory. Each page has a global `layout` variable in its front matter, which specifies which layout file to use.


Jekyll uses [Liquid](https://github.com/Shopify/liquid/wiki) templating to process templates. For example, in `/_docs/_layouts/self_help.html`:

```html
  <div id="help_list" >
      {%- for help_list in page.resources_list  -%}
        {%- if help_list.link -%}
        <a href="{{ help_list.link }}">
          {%- endif %}
      <div id="{{ help_list.name | handle }}" class="help_item">
        <div class="help_img" >
        {%- if help_list.image -%}
        <img src="{{site.baseurl}}{{ help_list.image}} " />
        {%- endif -%}
        </div>
        <div class="help_info">
          <div class="help_name">
              {{ help_list.name }}
          </div>
        </div>
      </div>
        {%- if help_list.link -%}
        </a>
        {%- endif %}
      {%- endfor -%}
    </div>
```

## Pages

Let's take a look at the YAML front matter for `/_docs/_developer_guide/platform_integration_guides/ios/push_notifications/customization.md`:

```yaml
---
nav_title: Customization
platform: iOS
ex_push_payload: archive/apple/push_payload.json
page_order: 1
search_rank: 5
layout: documents
---
```

## Sections

> TODO: Something like "There are main sections and subsections... Primary are X and sub are Y."

### Top-level sections

> TODO: improve/make better examples.

Articles are organized into section folders (i.e., `_docs/`), and each section folder is defined as a [Jekyll collection](http://jekyllrb.com/docs/collections/). Collections can be thought of as groupings of Jekyll posts that can be given their own unique properties.  Files within `_docs/` will mimic the url structure unless they have a permalinks config value or are `hidden` pages.

Each collection holds relevant articles. For example:

```plaintext
/_docs/_developer_guide/platform_integration_guides/ios/initial_sdk_setup/initial_sdk_setup.md
```

The live url will be based on the collections url. For example:

```plaintext
https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/initial_sdk_setup/
```

### Subsections

Folders can be created to generate the navigation sidebar layout as desired. Navigation name will use the folder name. If a different folder name is desired, then on the same level as the folder, a config folder file of the same name can be created to determine the order.

In the previous example, there's an iOS folder:

```plaintext
└──_docs/
   └──_developer_guide/
      └──platform_integration_guides/
         ├──ios/
         └──ios.md
```

To label this folder "iOS" in the navigation sidebar, we'll add the following metadata to `ios.md`:

```yaml
---
nav_title: iOS
config_only: true
layout: blank_config
page_order: 1
---
```

## Includes

Includes are small page fragments in the `/_docs/_includes/` directory which can be included in multiple places on the site via the include tag. For example:

```plaintext
{% raw %}{% multi_lang_include header.html %}{% endraw %}
```

For a step-by-step guide, see [Reusing content]().
