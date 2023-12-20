---
nav_title: Adding a new image
page_order: 0
noindex: true
---

# Adding a new image

> Learn how to add images, replace images, and remove images on Braze Docs. For general information about images, see [About our framework]().

{% multi_lang_include contributing/prerequisites.md %}

## Add a new image

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
