---
nav_title: Replacing an image
page_order: 1
noindex: true
---

# Replacing an existing image

> Learn how to add images, replace images, and remove images on Braze Docs. For general information about images, see [About our framework]().

{% multi_lang_include contributing/prerequisites.md %}

## Replace an existing image

When updating an image, replace the old image with a new image of the same name by following this flow:

1. Delete the image.
2. `git add .`
3. `git status` and confirm the image was deleted.
4. Add the new image.
5. `git add .` again.
6. `git status` again and confirm the image was modified.

## Remove an existing image

> TODO: make this more of a note/callout, not a section with it's own heading.

Don’t delete an existing image if you remove its reference from an article or replace it with an image of a different name. Those images are still being referenced in other language versions of the docs, so removing the file can completely break, for example, the French site. The Braze docs team audits the image repository on a regular cadence to remove images that aren’t being referenced anymore.
