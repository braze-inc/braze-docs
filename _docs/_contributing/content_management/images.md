---
nav_title: Images
article: Images
description: "Learn how to add, modify, and remove images on Braze Docs."
page_order: 2
noindex: true
---

# Images

> Learn how to add, modify, and remove images on Braze Docs. For general information about images, see [Content Management]({{site.baseurl}}/contributing/content_management/#images).

{% multi_lang_include contributing/prerequisites.md %}

## Adding a new image

### Step 1: Upload the image file

In your text editor, open `assets` > `img`. Generally, your new image should be added to the same directory as the other images on your page. However, you may use your best judgment. Confirm your new image follows the [Braze Docs Style Guide]({{site.baseurl}}/contributing/style_guide/), then add the PNG file to the relevant subdirectory.

![A text editor with the file tree open and a new image added to the 'img' directory.]()

### Step 2: Link to the image

When linking to your new image, you can either use in-line or reference-style syntax. In-line syntax prioritizes clarity, while reference-style syntax prioritizes readability.

{% tabs local %}
{% tab in-line %}
In your Markdown file, link to your new image using the in-line syntax.

{% raw %}
```markdown
![ALT_TEXT.]({% image_buster /assets/img/DIRECTORY/IMAGE.png %})
```
{% endraw %}

Replace the following:

| Placeholder | Description                                                                                                             |
|-------------|-------------------------------------------------------------------------------------------------------------------------|
| `ALT_TEXT`  | The alt text for the image. This is required to ensure Braze Docs is equally accessible for those using screen readers. |
| `IMAGE`     | The relative path to your image starting from the `img` directory.                                                      |
{: .reset-td-br-1 .reset-td-br-2}

Your in-line image should be similar to the following:

{% raw %}
```markdown
![The form for creating a new pull request on GitHub.]({% image_buster /assets/img/contributing/getting_started/github_pull_request.png %})
```
{% endraw %}
{% endtab %}

{% tab reference-style %}
In your Markdown file, link to your new image using the reference-style syntax.

{% raw %}
```markdown
![ALT_TEXT.][REFERENCE_NUMBER]
```
{% endraw %}

Replace the following:

| Placeholder        | Description                                                                                                             |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
| `ALT_TEXT`         | The alt text for the image. This is required to ensure Braze Docs is equally accessible for those using screen readers. |
| `REFERENCE_NUMBER` | Assign any positive integer that's not already assigned to another reference-style link on this page.                   |
{: .reset-td-br-1 .reset-td-br-2}

Your in-line image should be similar to the following:

{% raw %}
```markdown
![The form for creating a new pull request on GitHub.][10]
```
{% endraw %}

At the bottom of the page, add your reference.

{% raw %}
```markdown
[REFERENCE_NUMBER]: {{site.baseurl}}SHORT_URL
```
{% endraw %}

Replace the following:

| Placeholder        | Description                                             |
|--------------------|---------------------------------------------------------|
| `REFERENCE_NUMBER` | The number of the reference you'd like to link to.      |
| `IMAGE` | The relative path to your image starting from the `img` directory. |
{: .reset-td-br-1 .reset-td-br-2}

Your links should be similar to the following:

{% raw %}
```markdown
[10]: {% image_buster /assets/img/contributing/getting_started/github_pull_request.png %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Updating an image



### Step 1: Find the original reference

Open the relevant Markdown file and look for the old [in-line]({{site.baseurl}}/contributing/content_management/images/?tab=in-line#step-2-link-to-the-image) or [reference-style]({{site.baseurl}}/contributing/content_management/images/?tab=reference-style#step-2-link-to-the-image) image link, which will be similar the following.

{% raw %}
```markdown
{% image_buster /assets/img/DIRECTORY/IMAGE.png %}
```
{% endraw %}

### Step 2: Update the image

When updating an existing image, you can either add a new image file or replace the existing image file. Be sure your new image follows the [Braze Docs Style Guide]({{site.baseurl}}/contributing/style_guide/).

- **Add new file:** Use this method if the original image depicts completely out-of-date content, such as an image depicting a deprecated feature or workflow.
- **Overwrite existing file:** Use this method if the original image depicts accurate content, but is visually out-of-date, such as an image depicting a technology partner's old branding. Always use this method when possible as it reduces the total number of images stored in the Braze Docs repository.

{% tabs local %}
{% tab add new file%}
Generally, your new image should be added to the same directory as the other images on this page, however you may use your best judgment. When you're ready, add the PNG file to the relevant location in `assets/img/`.

{% alert warning %}
Do not delete the old image file when you add your new one.
{% endalert %}

![A text editor with the file tree open and a new image added to the 'img' directory.]()

Link to your image using the [in-line]({{site.baseurl}}/contributing/content_management/images/?tab=in-line#step-2-link-to-the-image) or [reference-style]({{site.baseurl}}/contributing/content_management/images/?tab=reference-style#step-2-link-to-the-image) syntax.
{% endtab %}

{% tab overwrite existing file %}
Rename your new image to match the name of the original image. In the following example, see how the image file names are identical.

- **Original file name:** `getting_started_with_github_select_start3.png`
- **New file name:** `getting_started_with_github_select_start3.png`

Next, add your new image to the same directory as the original image. If asked, confirm you'd like to overwrite the image.

![A text editor asking the user to confirm they would like to overwrite the existing file.]()
{% endtab %}
{% endtabs %}

## Removing an image

To remove an image, open the relevant Markdown file and remove the [in-line]({{site.baseurl}}/contributing/content_management/images/?tab=in-line#step-2-link-to-the-image) or [reference-style]({{site.baseurl}}/contributing/content_management/images/?tab=reference-style#step-2-link-to-the-image) image link.

{% alert warning %}
Do not delete the image file from the repository.
{% endalert %}
