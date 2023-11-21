---
nav_title: Docs framework
page_order: 3
noindex: true
---

# Docs framework

> Braze Docs is built using Jekyll, a Static-Site Generator (SSG) and a framework for managing docs-as-code repositories.

## Directory structure

This is an overview of our Jekyll directory structure:

```plaintext
{% raw %}
_docs/
├── _developer_guide/                         // developer page
│   ├── platform_wide/                        // navigational folders. mimics url path
│   │   ├── analytics_overview.md             // analytics_overview article
│   │   └── ...
│   ├── platform_wide.md                      // navigation config file. uses same name as the folder
│   └── ...
├── _help/                                    // help page
│   └── ...
├── _hidden/                                  // hidden page
│   └── ...
├── _home/                                    // documents home page
│   └── ...
├── _partners/                                // partners home page
│   └── ...
├── _site_pages/                              // site home page. contain site specific pages.
│   ├── index.md                              // docs/ home page (ie docs/index.html)
│   └── ...
├── _includes/
│   ├── archive/                              // old documentation includes
│   ├── analytics.html                        // html  header code for analytics ie braze, gtm, marketo
│   ├── feedback.html                         // footer feedback code. "Was this page helpful?"
│   ├── header_search.html                    // Algolia nav search html code
│   ├── header.html                           // top navigational header code
│   ├── html_include.html                     // html include code declaration for title, scripts, css, etc
│   ├── left_nav_menu.html                    // html for left nav bar. Includes status.io page and makes call to left nav plugin
│   ├── search_page.html                      // html for search page.
│   └── youtubue.html                         // youtube embed code
├── _layouts/
│   ├── bare.html                             // most basic of layouts. doesn't include any header or footer
│   ├── basic.html                            // only includes header and footer code.
│   ├── blank_config.html                     // for config pages. doesn't contain any content.
│   ├── broken_page.html                      // 404 page layout
│   ├── default.html                          // basic page, no footer
│   ├── dev_guide.html                        // developer guide page. uses default
│   ├── doc_guide.html                        // documentations home page. uses default
│   ├── documents.html                        // main content wrapper with left nav, footer etc. uses default
│   ├── partner_page.html                     // partner guide page. uses default
│   ├── redirect.html                         // bare bone page for redirecting urls
│   ├── self_help.html                        // help page. uses default
│   └── user_guide.html                       // user guide page. uses default
├── _plugins/
│   ├── alert_tag.rb                          // alert liquid tag plugin.
│   ├── algolia_hooks.rb                      // custom algolia plugin to index pages, and preprocessing prior to indexing. 
│   ├── alias_generator.rb                    // plugin to duplicate page as an alias.
│   ├── alloy_partner.rb                      // plugin to pull partner json from website for inlining. 
│   ├── details_tag.rb                        // details liquid tag plugin.
│   ├── image_buster.rb                       // image buster plugin. ensure images are not cached.
│   ├── jekyll_asset_pipeline.rb              // scss interpreter and css/js compressor
│   ├── jekyll-pwa-plugin.rb                  // offline javascript service worker
│   ├── permalink.rb                          // allows for custom tag in permalink.
│   └── urlnavmenu_gnerator.rb                // customer plugin to generate left nav based on url hierarchy 
├── Archive/                                  // Old site reference
│   ├── academy/                              // old academy page.
│   │   └──  _site/                           // static site
│   │      ├── 404.html                       // new site 404 page
│   │      └── ...
│   └── documentation/                        // old documentation page.
│       └──  _site/                           // static site
│          ├── 404.html                       // new site 404 page
│          ├── redirect.js                    // javascript file to redirect old site to new site
│          └── ...
├── assets/                                   // assets page
│      ├── css/                               // scss pages
│      ├── fonts/
│      ├── img/                         
│      ├── img_archive/                       // images from old page                         
│      └── js/
├── config/                                   // config files
│      ├── nginx.conf.erb                     // nginx config page. for redirects, and other server configs.
│      └── puma.rb
├── public/                                   // folder for serving up default local page
│      └── index.html                         // default local host page. ie http://localhost:4000
├── swagger/                                  // swagger pages
│      ├── braze_swagger.json                 // swagger braze files
│      └── ...
├── config.yml                                // site config file
├── app.json                                  // heroku build config
├── config.ru                                 // rails config file 
├── Gemfile                                   // ruby require packages
├── Procfile                                  // heroku process file (local)
├── Procfile.web                              // heroku process file (web)
├── proxy.rb                                  // local ruby proxy file
├── Rakefile                                  // rake config file
└── Readme.md                                 // git readme file
{% endraw %}
```

## Markdown

Articles are written in [Markdown syntax](http://daringfireball.net/projects/markdown/) as .md files housed within the `_docs/` directory. Jekyll uses [kramdown](http://kramdown.gettalong.org/) to parse Markdown files from plain text into HTML. [Configuration for Markdown parsers](http://jekyllrb.com/docs/configuration/#markdown-options) can be set in `_config.yml`.

## Collections

Articles are organized into section folders (i.e., `_docs/`), and each section folder is defined as a [Jekyll collection](http://jekyllrb.com/docs/collections/). Collections can be thought of as groupings of Jekyll posts that can be given their own unique properties.  Files within`_docs/` will mimic the url structure unless they have a permalinks config value or are`hidden` pages.

Each collection holds relevant articles. For example:

```plaintext
/_docs/_developer_guide/platform_integration_guides/ios/initial_sdk_setup/initial_sdk_setup.md
```

The live url will be based on the collections url. For example:

```plaintext
https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/initial_sdk_setup/
```

## YAML front matter and liquid templating

To be recognized and processed by Jekyll, a file requires YAML Front Matter. Front matter must be the first thing in the file and must take the form of valid YAML set between triple-dashed lines. Here is an example of the front matter in `/_docs/_developer_guide/platform_integration_guides/ios/initial_sdk_setup/initial_sdk_setup.md`:

```yaml
---
nav_title: Set Up
platform: iOS
page_order: 0
search_rank: 5
---
```

Front matter can be empty as well, if you want Jekyll to recognize the file but don't care to actually set any variables:

```yaml
---
---
```

Within a file's front matter, you can set [predefined variables](http://jekyllrb.com/docs/frontmatter/#predefined-global-variables) as well as [custom ones](http://jekyllrb.com/docs/frontmatter/#custom-variables). For each file with front matter, Jekyll makes a variety of data available via the [Liquid templating system](https://github.com/Shopify/liquid/wiki). All front matter variables will be available via Liquid tags, both further down in the file and in any layouts or includes that reference the given page. Therefore, in `Creating_a_Segment.md`, `{% raw %}{{ page.title }}{% endraw %}` would render to "Creating a Segment."

More information on front matter variables as data can be found on the [Jekyll Variables documentation](http://jekyllrb.com/docs/variables/) and [Front Matter](https://jekyllrb.com/docs/front-matter/).

## Sections

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

<style>
table td {
    word-wrap: break-word;
}
</style>
<table>
<thead>
    <tr>
        <th style="width: 15%; text-align: left;">YAML tag</th>
        <th style="width: 15%; text-align: left;">Type</th>
        <th style="width: 70%; text-align: left;">Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td><code>nav_title</code></td>
        <td>String</td>
        <td>The name that should show up in the navigation sidebar.</td>
    </tr>
    <tr>
        <td><code>config_only</code></td>
        <td>Boolean</td>
        <td>Set to <code>true</code> to prevent the page from opening, so it will only be used as a dropdown in the navigation bar.</td>
    </tr>
    <tr>
        <td><code>layout</code></td>
        <td>String</td>
        <td>Use <code>blank_config</code> which may redirect to the home page so a broken link will not appear.</td>
    </tr>
    <tr>
        <td><code>page_order</code></td>
        <td>Numeric</td>
        <td>Defines the order the page should show up in (ascending order).</td>
    </tr>
</tbody>
</table>

> TODO: Move this to a different doc:

_If the page should be clickable and have content, then `config_only` can be removed, and `documents` layout may be used._

## Pages

Let's take a look at the YAML front matter for`/_docs/_developer_guide/platform_integration_guides/ios/push_notifications/customization.md`:

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

<table>
<thead>
    <tr>
        <th style="width: 15%; text-align: left;">YAML tag</th>
        <th style="width: 15%; text-align: left;">Type</th>
        <th style="width: 70%; text-align: left;">Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td><code>layout</code></td>
        <td>String</td>
        <td>Defines that the "Customization" page uses <code>documents.html</code>. Otherwise, it will use the layout as defined in the <code>_configs.yaml</code> file.</td>
    </tr>
    <tr>
        <td><code>nav_title</code></td>
        <td>String</td>
        <td>Defines a custom title for the left nav.</td>
    </tr>
    <tr>
        <td><code>page_order</code></td>
        <td>Integer</td>
        <td>Defines the order the page should show up on the left nav.</td>
    </tr>
    <tr>
        <td><code>search_rank</code></td>
        <td>Integer</td>
        <td>Defines the search rank for indexing.</td>
    </tr>
    <tr>
        <td><code>platform</code></td>
        <td>String</td>
        <td>Defines a custom platform YAML config.</td>
    </tr>
</tbody>
</table>


## Custom YAML tags

Here's a list of some custom yaml tags supported by most layouts (but not all):

<table>
<thead>
    <tr>
        <th style="width: 15%; text-align: left;">YAML tag</th>
        <th style="width: 15%; text-align: left;">Type</th>
        <th style="width: 70%; text-align: left;">Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td><code>config_only</code></td>
        <td>Boolean</td>
        <td>For use mainly for left nav. If set to true, then do not show in the left nav as a link.</td>
    </tr>
    <tr>
        <td><code>redirect_to</code></td>
        <td>String</td>
        <td>For use to redirect the page to another page.</td>
    </tr>
    <tr>
        <td><code>alias</code></td>
        <td>String</td>
        <td>For use to have another page redirect to this page. Does not affect the left nav plugin, so a nav link will not be generated.</td>
    </tr>
    <tr>
        <td><code>hidden</code></td>
        <td>Boolean</td>
        <td>If set to true, will not show up as a nav link.</td>
    </tr>
    <tr>
        <td><code>hide_toc</code></td>
        <td>Boolean</td>
        <td>If set to true, hide the right hand ToC list.</td>
    </tr>
    <tr>
        <td><code>hide_nav</code></td>
        <td>Boolean</td>
        <td>If set to true, hide the left hand nav sidebar.</td>
    </tr>
    <tr>
        <td><code>hide_bottom_nav</code></td>
        <td>Boolean</td>
        <td>If set to true, hide bottom page navigation.</td>
    </tr>
    <tr>
        <td><code>hide_feedback</code></td>
        <td>Boolean</td>
        <td>If set to true, hide the feedback option.</td>
    </tr>
</tbody>
</table>


## Layouts

Pages are rendered using the HTML files stored in the`/_docs/_layouts/` directory. Each page has a global `layout` variable in its front matter, which specifies which layout file to use.


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

## Includes

Includes are small page fragments in the `/_docs/_includes/` directory which can be included in multiple places on the site via the include tag. For example:

```plaintext
{% raw %}{% multi_lang_include header.html %}{% endraw %}
```

Like Jekyll pages, articles and layouts, these page fragments can be populated via Liquid templating. Includes in combination with Liquid templating can be extremely useful in preventing redundancy.

How to use include formatting:

1. Create a file in the `includes/archive` folder.
2. Add your content to the markdown file, no introductory YAML/metadata needed.
3. In the files you want to reference the alert, include `{% raw %}{% multi_lang_include archive/alert_name.md %}{% endraw %}`
