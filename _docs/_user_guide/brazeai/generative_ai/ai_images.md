---
nav_title: AI-Generated Images
article_title: Generating images with BrazeAI
page_order: 5
description: "Learn how to generate images for your media library using DALL·E 3, an AI system from OpenAI and a Braze third-party provider."
---

# Generating images with BrazeAI

> {% multi_lang_include generative_ai/ai_images.md %}

## How is my data used and sent to OpenAI? {#ai-policy} 

Between you and Braze, any images generated using DALL·E 3 are your intellectual property. Braze will not assert any claims of copyright ownership on such images and makes no warranty of any kind with respect to any AI-generated content or images.

To generate images, Braze will send your query to OpenAI's API Platform. All queries sent to OpenAI from Braze are anonymized, meaning that OpenAI will not be able to identify from whom the query was sent unless you include uniquely identifiable information in the input you provide. As detailed in [OpenAI’s API Platform Commitments](https://openai.com/policies/api-data-usage-policies), data sent to OpenAI’s API via Braze is not used to train or improve their models and will be deleted after 30 days. Please ensure that you adhere to OpenAI’s policies relevant to you, which may include its [Usage Policy](https://openai.com/policies/usage-policies) and its [Sharing & Publication Policy](https://openai.com/policies/sharing-publication-policy). Braze makes no warranty of any kind with respect to any AI-generated content.

## Generating an image

1. From your [media library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) in Braze, select <i class="fas fa-wand-magic-sparkles"></i> **AI Image Generator**.
2. Enter a description of the image you want to generate, up to 300 characters. The more detailed the description, the better your result. This feature only supports text input—uploading an image as a reference isn’t available.
3. Select **Generate Images**. It can take about a minute for images to generate.
4. Select <i class="fas fa-download" title="Add image to Media Library"></i> on the images you would like to add to your media library.

![AI image generator modal in the media library.]({% image_buster /assets/img_archive/media_library_dalle.png %}){: style="max-width:75%"}
