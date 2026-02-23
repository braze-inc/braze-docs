---
nav_title: Image copy style guide
article_title: Image Copy Style Guide
description: "Guidelines for creating and styling images in Braze Docs."
page_order: 1
noindex: true
---

# Image copy style guide

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

**Image Styling Tools:** Use [Skitch](https://evernote.com/products/skitch) (available free through Evernote) for applying image styling (blurring, emphasizing image components, cropping).

**Don't embed important text inside images:** Avoid embedding text inside images as not all users can read English text (and page translation tools do not translate images). This text should be provided in the article. Provide alt text for images for maximum accessibility for users.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/embed_text_do.png %}" alt="Example of correctly not embedding text in an image."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/embed_text_dont.png %}" alt="Example of incorrectly embedding text in an image."></td></tr>
</tbody>
</table>
{:/}

**Optimize placement and sizing:** Whenever possible, place images near relevant text and be mindful to use image styling markdown to resize larger images. For some content, this should be done by [anchoring text to the left or right side of the page]({{site.baseurl}}/home/styling_test_page/#image-test) depending on the image and the space available. 

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/optimize_placement_do.png %}" alt="Example of correctly optimizing image placement."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/optimize_placement_dont.png %}" alt="Example of incorrectly optimizing image placement."></td></tr>
</tbody>
</table>
{:/}

**Cropping**: Crop relevant sections closely. Unless necessary, do not include the left navigation bar and instead include navigation directions in the article. This limits the number of images that need to be changed when UI changes occur. 

{% alert note %}

If you are going to capture a dashboard element, crop without including the border. See [Cropping Images continued](#cropping-continued) for expanded examples.

{% endalert %}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_do_1.png %}" alt="Example of a properly cropped image."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_dont_1.png %}" alt="Example of an incorrectly cropped image."></td></tr>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_do_2.png %}" alt="Example of a properly cropped image."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_dont_2.png %}" alt="Example of an incorrectly cropped image."></td></tr>
</tbody>
</table>
{:/}

**Censorship**: Blur sensitive information like names, emails, and API keys. Blurring can be done through Skitch.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/censorship_do.png %}" alt="Example of correct blurring."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/censorship_dont.png %}" alt="Example of incorrect blurring."></td></tr>
</tbody>
</table>
{:/}

**Emphasizing Components of Images:** Do not emphasize components of images unless necessary. Use blue squares (the most colorblind-friendly option) with a thin-medium thickness to highlight different components of images, this can be done through skitch. Make sure the "highlighted sections" do not obstruct the normal UI. Absolutely no skitch arrows

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_do_1.png %}" alt="Example of correctly emphasizing components in an image."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_dont_1.png %}" alt="Example of incorrectly emphasizing components in an image."></td></tr>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_do_2.png %}" alt="Example of correctly emphasizing components in an image."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_dont_2.png %}" alt="Example of incorrectly emphasizing components in an image."></td></tr>
</tbody>
</table>
{:/}

**Cropping Explanation continued** {#cropping-continued}
Because Braze docs already add a border to each image, omit borders in a section screenshot. We are looking for a clean crop. The border can be left in if there are components that live outside or within the border, see the third image for example.

**Do:**
![Example of correctly cropping an image.]({% image_buster /assets/img/contributing/style_guide/cropping_do_3.png %})

**Don't:**  
![Example of incorrectly cropping an image.]({% image_buster /assets/img/contributing/style_guide/cropping_dont_3.png %})
  
**Do:**  
![Example of correctly cropping an image.]({% image_buster /assets/img/contributing/style_guide/cropping_do_4.png %})
