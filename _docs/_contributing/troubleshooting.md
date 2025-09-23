---
nav_title: Troubleshooting
article_title: Troubleshooting
description: "Troubleshooting steps for common issues you may experience while contributing to Braze Docs."
page_order: 9
noindex: true
toc_headers: h2
---

# Troubleshooting

> If you're having trouble contributing to Braze Docs, review these common issues first. If the issue you're experiencing isn't listed, [let us know](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=issue&projects=&template=report_an_issue.md&title=) so we can add it here.

## Redirect isn't working

{% multi_lang_include contributing/troubleshooting/redirects.md %}

## Preview deployment returns a 404

If your [GitHub preview deployment]({{site.baseurl}}/contributing/generating_a_preview/) builds successfully but returns a 404 response, there may be an issue with an image or Liquid tag in your Markdown file.

!["Example error 404 response after opening a preview deployment in GitHub."]({% image_buster /assets/img/contributing/github/build_preview_404.png %}){: style="max-width:55%;"}

To fix this issue, review each image and Liquid tag in your file.

{% tabs local %}
{% tab Image references %}
Verify that each image reference follows our [image reference syntax]({{site.baseurl}}/contributing/content_management/images/). For example:

{% raw %}
```markdown
![Braze Docs on GitHub.]({% image_buster /assets/img/contributing/github_homepage.png %})
```
{% endraw %}

Each image reference must use the exact path and filename for that image. For example:

```bash
braze-docs
└── assets
    └── img
        └── contributing 
            └── github_homepage.png
```

{% endtab %}

{% tab Opening and closing tags %}
Check that there's no mismatch between your opening and closing tags. For example, {% raw %}`{% tab %}`{% endraw %} tags need the same number of opening and closing tags:

{% raw %}
```plaintext
{% tabs %}                # Opening tag for tab group.
{% tab Tab One %}         # Opening tag for tab one.
Content for tab one.
{% endtab %}              # Closing tag for tab one.

{% tab Tab Two %}         # Opening tag for tab two.
Content for tab two.
{% endtab %}              # Closing tag for tab two.
{% endtabs %}             # Closing tag for tab group.
```
{% endraw %}

{% alert tip %}
For more Liquid tag examples, see [Styling examples]({{site.baseurl}}/contributing/styling_examples).
{% endalert %}
{% endtab %}

{% tab Raw tags %}
If you're documenting actual Liquid code in your Markdown file, ensure each codeblock is surrounded in [Liquid raw tags](https://shopify.dev/docs/api/liquid/tags/raw).

{% subtabs local %}
{% subtab Raw tag %}
<code>
&#123;% raw %} &#123;% endraw %}
</code>
{% endsubtab %}

{% subtab Example usage %}
<code>
&#123;% raw %}<br>
&#96;``<br>
&#123;% alert note %}<br>
Looking for sample code? Check out [our apps](&#123;&#123;site.baseurl}}/developer_guide/samples/)!<br>
&#123;% endalert %}<br>
&#96;``<br>
&#123;% endraw %}<br>
</code>
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Cross-reference link returns a 404

If a [cross-reference link]({{site.baseurl}}/contributing/content_management/cross_referencing/) on your page (such as `{% raw %}[Braze Developer Guide]({{site.baseurl}}/developer_guide/home){% endraw %}`) returns a 404 page, check the URL for the following string.

```plaintext
%7B%7Bsite.baseurl%7D%7D
```

A URL containing this string will be similar to the following:

```plaintext
https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/%7B%7Bsite.baseurl%7D%7D/user_guide/administrative/app_settings/message_activity_log_tab
```

If you find this string in the URL, one or more of your cross-reference links are surrounded in [Liquid raw tags](https://shopify.dev/docs/api/liquid/tags/raw).

{% tabs local %}
{% tab Liquid raw tag %}
<code>
&#123;% raw %} &#123;% endraw %}
</code>
{% endtab %}
{% endtabs %}

Move these tags so that they're only surrounding the Liquid content you want to display as raw.

{% tabs local %}
{% tab before %}
<code>
&#123;% raw %} Learn how to use Liquid's <code>&#123;&#123; page_title }} tag. For more information, see [Liquid tags](&#123;&#123;site.baseurl}}/contributing/liquid/). &#123;% endraw %}
</code>
{% endtab %}

{% tab after %}
<code>
Learn how to use Liquid's &#123;% raw %} &#123;&#123; page_title }} &#123;% endraw %} tag. For more information, see [Liquid tags](&#123;&#123;site.baseurl}}/contributing/liquid/).
</code>
{% endtab %}
{% endtabs %}

## Conflict: Destination is shared by multiple files

If `rake` throws the following warning, this means that two or more files are sharing the same [`permalink` YAML value]({{site.baseurl}}/contributing/yaml_front_matter/metadata/#permalink).

```bash
Conflict: The following destination is shared by multiple files.
                    The written file may end up with unexpected contents.
                    /Users/USERNAME/braze-docs/_site/api_usage/index.html
                     - /Users/USERNAME/braze-docs/_docs/_developer_guide/platforms/android.md
                     - /Users/USERNAME/braze-docs/_docs/_developer_guide/platforms/firos.md
```

{% alert note %}
Although the warning appears after running `rake`, it's actually generated by Jekyll, our static-site generator. For more information, refer to [Jekyll GitHub: Issue #8522](https://github.com/jekyll/jekyll/issues/8522).
{% endalert %}

To fix this, change the `permalink` value of one of the files, so they're no longer set to the same URL. For example:

{% tabs local %}
{% tab Before %}
In `_docs/_developer_guide/platforms/android.md`:
```markdown
---
nav_title: Android
permalink: /docs/developer_guide/best_sdk
---

# The Android Braze SDK

> Get started with the Braze Android SDK!
```

In `_docs/_developer_guide/platforms/fireos.md`:
```markdown
---
nav_title: FireOS
permalink: /docs/developer_guide/best_sdk
---

# The FireOS Braze SDK

> Get started with the Braze Android SDK!
```
{% endtab %}

{% tab After %}
In `_docs/_developer_guide/platforms/android.md`:
```markdown
---
nav_title: Android
permalink: /docs/developer_guide/best_sdk
---

# The Android Braze SDK

> Get started with the Braze Android SDK!
```

In `_docs/_developer_guide/platforms/fireos.md`:
```markdown
---
nav_title: FireOS
permalink: /docs/developer_guide/second_best_sdk
---

# The FireOS Braze SDK

> Get started with the Braze Android SDK!
```
{% endtab %}
{% endtabs %}

## Can't choose `braze-inc/braze-docs` as a base repository {#missing-base-repository}

If `braze-inc/braze-docs` is missing from the list of available base branches when [making a change in GitHub]({{site.baseurl}}/contributing/your_first_contribution/#step-2-make-a-change), there may be an issue with the origin of your forked repository.

![The 'Choose a Base Repository' dropdown in GitHub after selecting 'compare across forks'.]({% image_buster /assets/img/contributing/github/choose_base_repository.png %}){: style="max-width:85%;"}

### Step 1: Verify the fork's origin

Go to [your forked repository]({{site.baseurl}}/contributing/home/#step-3-fork-the-repository) and verify it was forked from `braze-inc/braze-docs`. If it isn't, you'll need to delete this fork and create a new one.

![An example forked repository, correctly showing "fork from braze-inc/braze-docs".]({% image_buster /assets/img/contributing/github/correct_forked_from.png %}){: style="max-width:85%;"}

### Step 2: Delete the old fork

{% alert warning %}
Deleted forks cannot be restored. Be sure to back up the work that's only accessible through your old fork.
{% endalert %}

In your old fork, go to **Settings** > **General**. Under **Danger Zone**, select **Delete this repository** and follow the on-screen instructions.

![The list of options found in a GitHub repository's "Danger Zone".]({% image_buster /assets/img/contributing/github/delete_repository.png %}){: style="max-width:65%;"}

### Step 3: Create a new fork

Go back to the official [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs), then select **Fork** to create a new fork.

![The Braze Docs GitHub repository showing "Fork".]({% image_buster /assets/img/contributing/github/fork_the_repository.png %}){: style="max-width:75%;"}

Keep the default settings, then select **Create fork**. Now you'll be able to choose `braze-inc/braze-docs` as the base repository when [making changes in GitHub]({{site.baseurl}}/contributing/your_first_contribution/#step-2-make-a-change).

![The Braze Docs GitHub repository showing "Create fork".]({% image_buster /assets/img/contributing/github/create_a_new_fork.png %}){: style="max-width:75%;"}
