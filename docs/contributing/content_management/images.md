
# Manage images

> Learn how to add, modify, and remove images on Braze Docs. For general information about images, see [About content management](../content_management.md#images).

<!--
## Prerequisites

If you haven't already, review [Documentation feedback](https://www.braze.com/docs/feedback/) for how to reach the docs team. Full authoring guides for contributors with repository access live under `docs/contributing/` in the braze-docs repo.
-->


## Adding a new image

### Step 1: Add the image file

In your text editor, open `assets` > `img`. Generally, your new image should be added to the same directory as the other images on your page. However, you may use your best judgment. Confirm your new image follows the [Braze Docs Style Guide](../style_guide.md), then add the PNG file to the relevant subdirectory.

```bash
braze-docs
└── assets
    └── img
        └── DIRECTORY
            └── FILE.png
```

Replace the following:

| Placeholder | Description                                                                               |
|-------------|-------------------------------------------------------------------------------------------|
| `DIRECTORY` | The name of the relevant directory. If there's no relevant directory, you may create one. |
| `FILE`      | The name of the file including the file extension.                                        |


Your image file should be similar to the following:

```bash
braze-docs
└── assets
    └── img
        └── contributing 
            └── github_home_page.png
```

### Step 2: Link to the image

> [!IMPORTANT]
> Since Liquid's `{% tab %}` tag does not support reference-style links, only in-line links are documented below. Existing reference links will continue to work, but are no longer recommended.



In your Markdown file, link to your new image using the in-line syntax.
```markdown
![ALT_TEXT.](../../../assets/img/DIRECTORY/IMAGE.png)
```
Replace the following:

| Placeholder | Description                                                                                                             |
|-------------|-------------------------------------------------------------------------------------------------------------------------|
| `ALT_TEXT`  | The alt text for the image. This is required to make Braze Docs equally accessible for those using screen readers. |
| `IMAGE`     | The relative path to your image starting from the `img` directory.                                                      |


Your in-line image should be similar to the following:
```markdown
![The form for creating a new pull request on GitHub.](../../../assets/img/contributing/getting_started/github_pull_request.png)
```
### Step 3: Set the image's maximum width (optional)

You can set the image's maximum width by appending the following Liquid code to your image link:
```markdown

```
Replace `NUMBER` with the maximum width you'd like to set as a percentage. Your image link should be similar to the following:
```markdown
![The form for creating a new pull request on GitHub.](../../../assets/img/contributing/getting_started/github_pull_request.png)```
## Updating an image

### Step 1: Find the original reference

Open the relevant Markdown file and look for the old [in-line](images.md#step-2-link-to-the-image) or [reference-style](images.md#step-2-link-to-the-image) image link, which will be similar the following.
```markdown
../../../assets/img/DIRECTORY/IMAGE.png
```
### Step 2: Update the image

When updating an existing image, you can either add a new image file or replace the existing image file. Be sure your new image follows the [Braze Docs Style Guide](../style_guide.md).

- **Overwrite existing file (recommended):** Use this method if the original image depicts accurate content, but is visually out-of-date, such as an image depicting old branding. This method reduces the total number of images stored in the Braze Docs repository.
- **Add new file:** Use this method if the original image depicts completely out-of-date content, such as an image depicting a deprecated feature or workflow.

### Overwrite existing file

Rename your new image to match the name of the original image. In the following example, see how the image file names are identical.

- **Original file name:** `getting_started_with_github_select_start3.png`
- **New file name:** `getting_started_with_github_select_start3.png`

Next, add your new image to the same directory as the original image. If asked, confirm you'd like to overwrite the image. Your image file should be similar to the following:

```bash
braze-docs
└── assets
    └── img
        └── contributing 
            └── getting_started_with_github_select_start3.png
```

---

### Add new file

Generally, your new image should be added to the same directory as the other images on this page, however you may use your best judgment. When you're ready, add the PNG file to the relevant location in `assets/img/`.

> [!WARNING]
> Do not delete the old image file when you add your new one.



```bash
braze-docs
└── assets
    └── img
        └── DIRECTORY
            └── FILE.png
```

Replace the following:

| Placeholder | Description                                                                               |
|-------------|-------------------------------------------------------------------------------------------|
| `DIRECTORY` | The name of the relevant directory. If there's no relevant directory, you may create one. |
| `FILE`      | The name of the file including the file extension.                                        |


Your image file should be similar to the following:

```bash
braze-docs
└── assets
    └── img
        └── contributing 
            └── github_home_page.png
```

After your image is added to the relevant directory, you can link to this image using the [in-line](images.md#step-2-link-to-the-image) or [reference-style](images.md#step-2-link-to-the-image) syntax.



## Removing an image

To remove an image, open the relevant Markdown file and remove the [in-line](images.md#step-2-link-to-the-image) or [reference-style](images.md#step-2-link-to-the-image) image link. Do not delete the image file from the repository.

> [!WARNING]
> When an image file is deleted, that image will break for other Braze Docs language translations.


