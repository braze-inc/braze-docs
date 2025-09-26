---
nav_title: Generating a preview
article_title: Generating a preview
description: "Learn how to generate a local site preview, so you can see how your work would look on Braze Docs."
page_order: 5 
noindex: true
---

# Generating a preview

> Learn how to generate a local site preview, so you can see how your work would look on Braze Docs.

{% multi_lang_include contributing/prerequisites.md %}

## Generating the preview

### Step 1: Checkout a branch

In your terminal, check out a branch to use for your site preview.

```bash
git checkout BRANCH_NAME
```

Replace `BRANCH_NAME` with the name of one of your branches or another person's branch. Your command should be similar to the following:

```bash
git checkout BD-2346-fixing-typo-swift
```

### Step 2: Start a local server

When you start a local server, the files in your [current branch](#step-1-checkout-a-branch) are used to you build a local preview of Braze Docs. To start a local server using your current branch, run the following command in your `braze-docs` directory.

{% raw %}
```bash
# for 'en' language:
rake

# for other langauges:
rake es
rake fr
rake ja
rake ko
rake pt_br

# to render content in '{% markdown_embed %}' tags:
MARKDOWN_API=true rake

# to render tiles on partner landing pages:
PARTNER_API=true rake

# to render both APIs:
MARKDOWN_API=true PARTNER_API=true rake
```
{% endraw %}

{% alert note %}
Prepending `MARKDOWN_API=true` to your rake command let's you preview content within a `{% markdown_embed %}` tag, such as the content on the [Developer Guide: Changelogs]({{site.baseurl}}/developer_guide/changelogs/) page. Prepending `PARTNER_API=true` let's you render the tiles on a partner landing page, such as [Technology Partners]({{site.baseurl}}/partners/home/).
{% endalert %}

The output will be similar to the following:

```bash
== Sinatra (v3.0.4) has taken the stage on 4000 for development with backup from Puma
Puma starting in single mode...
* Puma version: 6.3.1 (ruby 3.2.2-p225) ("Mugi No Toki Itaru")
*  Min threads: 8
*  Max threads: 32
*  Environment: development
*          PID: 16158
* Listening on http://127.0.0.1:4000
...
```

### Step 3: Open your site preview

By default, your site preview will be generated on localhost [`http://127.0.0.1:4000`](http://127.0.0.1:4000). To open your site preview, open the link in your web browser.

![An example site preview running in a web browser.]({% image_buster /assets/img/contributing/styling_examples/home.png %})

### Step 4: Stop your local server

To stop your local server, reopen the terminal and press <kbd>Control</kbd> + <kbd>C</kbd>.

## Updating the preview

In most cases, your site preview will update automatically when you make changes to the files in `braze-docs`. When this happens, your terminal will output a message similar to the following:

```bash
Asset Pipeline: Processing 'javascript_asset_tag' manifest 'global'
Asset Pipeline: Saved 'global-128fd02b54e35ea79fcb21ea460fac06.js' to '/Users/alex-lee/braze-docs/_site/assets'
                    ...done in 1.940883 seconds.
```

To see these updates in your browser, refresh the page.

{% alert tip %}
You can refresh the page in your browser by pressing <kbd>Command</kbd> + <kbd>R</kbd> on macOS, or <kbd>Control</kbd> + <kbd>R</kbd> on Windows.
{% endalert %}

However, there are cases when your site preview will **not** be automatically updated, such as when:

- A file or directory name is changed
- A new file or directory is added
- The content of a file in the `_includes` directory is edited 

To see these updates, you'll need to [stop your local server](#step-4-stop-your-local-server) and [start it again](#step-2-start-a-local-server).
