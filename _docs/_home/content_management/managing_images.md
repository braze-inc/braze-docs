---
nav_title: Managing images
page_order: 2
noindex: true
---

# Managing images

> Learn how to add new images and work with existing images on Braze Docs. For general information about images, see [About our framework](../../../_docs/_home/about_our_framework.md).

{% multi_lang_include contributing/prerequisites.md %}

## Adding a new image

To add a new image to the documentation, or edit an existing image, please follow the guidelines in our [Image Styling Guide](https://docs.google.com/document/d/e/2PACX-1vRJSkwcjmjrTfLDagZccLpOMMyh5NN5SXRZSjz12cRAHbX4OrUmhvCmYpf_p5YB-9r4_jSOQLkicQIH/pub), then follow these steps:

1. Add the optimized image to the `/assets/img/` directory within the repository.
2. Add the image to the markdown file by doing something like the following with the image_buster tag:
  
    * image_buster adds a signature to the image URL to prevent image caching for updated images.

    ```plaintext
    {% raw %}
    ![alt text][1]

    [1]: {% image_buster /assets/img/image_name.png %}
    {% endraw %}
    ```

Image names should be all lowercase to prevent issues with linking. Image references are not case-agnostic.

## Working with existing images

{% alert warning %}
Do not delete images from the Braze Docs GitHub repository. If an image file is removed, other language translations referencing that image wll show a broken image instead.
{% endalert %}

When you're working with an existing image, you can either replace or update the image.

- **Replace:** The new image shows completely different content. Useful when you're updating a page that references a depricated feature. 
- **Update:** The new image is visually different, but the content is the same. Useful when you're updating a page for a company rebrand.

{% tabs %}
{% tab replace %}
To replace an image, [create a new branch]({{site.baseurl}}/home/github/creating_a_new_branch/), then open your page and look for the image's reference. It will mirror the following syntax:

{% raw %}
```markdown
{% image_buster /assets/img/DIRECTORY/IMAGE.png %}
```
{% endraw %}

Generally, your new image should be added to the same directory as the other images on this page, however you may use your best judgment. Confirm your new image follows our [Image Style Guide](), then add the PNG file to the relevant location in `assets/img/`. Remember not to delete the original image when you add your new one.

![A text editor with the file tree open and a new image added to the 'img' directory.]()

Link to your image using our [standard image syntax](#adding-a-new-image). {% multi_lang_include contributing/minis/creating_a_pull_request.md %}
{% endtab %}
{% tab update %}
To update an image, [create a new branch]({{site.baseurl}}/home/github/creating_a_new_branch/), then open your page and look for the image's reference. It will mirror the following syntax:

{% raw %}
```markdown
{% image_buster /assets/img/DIRECTORY/IMAGE.png %}
```
{% endraw %}

Confirm your new image follows our [Image Style Guide](), then save your image as a PNG and give it the same exact name as the original image. For example, if the original image is named `getting_started_with_github_select_start3.png`, your new image should also be named `getting_started_with_github_select_start3.png`. 

Next, add your new image to the same directory as the original image. Most text editors will ask you to confirm if you'd like to ovewrite the existing file because a file with this name already exists. Confirm you'd like to overwrite the image.

!["A text editor asking the user to confirm they would like to overwrite the existing file."]()

{% multi_lang_include contributing/minis/creating_a_pull_request.md %}
{% endtab %}
{% endtabs %}


