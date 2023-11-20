---
nav_title: Managing images
article_title: Managing images
page_order: 1
noindex: true
---

# Managing images

> TODO

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

## Updating an existing image

When updating an image, replace the old image with a new image of the same name by following this flow:

1. Delete the image.
2. `git add .`
3. `git status` and confirm the image was deleted.
4. Add the new image.
5. `git add .` again.
6. `git status` again and confirm the image was modified.

## Removing an existing image

Don’t delete an existing image if you remove its reference from an article or replace it with an image of a different name. Those images are still being referenced in other language versions of the docs, so removing the file can completely break, for example, the French site. The Braze docs team audits the image repository on a regular cadence to remove images that aren’t being referenced anymore.
