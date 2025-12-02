---
nav_title: Cloudinary
article_title: Cloudinary
description: "This reference article outlines the partnership between Braze and cloudinary."
alias: /partners/cloudinary/
page_type: partner
search_tag: Partner
---

# Cloudinary

> [Cloudinary](https://www.cloudinary.com?utm_source=braze_partner_page) is an image and video platform used to manage, edit, optimize, and deliver images and video at scale to any campaign across channels and customer journeys. When integrated and enabled, Cloudinary's media management powers dynamic, contextual, and personalized asset delivery for your Braze campaigns and Canvases. 

## About this integration

Connecting Cloudinary to Braze gives brands access to visual media stored in Cloudinary Assets for use in Braze messaging channels. With Cloudinary’s dynamic links, you can select and customize images and videos in real time based on Braze user attributes. Together, Cloudinary and Braze support crafting visually rich, personalized campaigns that tell each product’s story and deliver one-of-a-kind experiences at scale.

This page outlines four possible, but not exhaustive, integration methods between Cloudinary and Braze. These integration methods primarily rely on modifying asset links manually copied from Cloudinary’s Media Library. 

{% alert important %}
More advanced integration methods, including using [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) to call Cloudinary’s [Admin API](https://cloudinary.com/documentation/admin_api#banner) are possible, but the approach will vary between customers. Contact your Cloudinary and Braze customer success manager for guidance.
{% endalert %}

## Prerequisites

| Requirements     | Description |                        
|-----------------------|-----------------|
| Cloudinary Account  | A [Cloudinary Account](https://cloudinary.com/users/register_free?utm_source=braze+docs+page) is required to take advantage of this partnership  |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Integration methods

{% alert tip %}
Some of these integration methods use the `f_auto` and `q_auto` Cloudinary Transformations, which offer deeper customization of the behavior and appearance for [image](https://cloudinary.com/documentation/image_transformations#banner) and [video](https://cloudinary.com/documentation/video_manipulation_and_delivery#banner) assets. For more information on modifying a Cloudinary asset link to include Transformations, refer to [Transformation URL structure](https://cloudinary.com/documentation/image_transformations#transformation_url_structure).
{% endalert %}

{% tabs %}
{% tab Cloudinary DAM %}

## Select campaign assets through Cloudinary DAM

The most direct way to use images and videos directly from Cloudinary's DAM in your Braze campaigns and Canvases is to pull the URL from the Cloudinary Media Library's **Asset** page.

![A grid view of Cloudinary's Image Asset Library, with the top right of one of the images highlighted, showing a "Copy URL" tooltip.]({% image_buster /assets/img/cloudinary/one.png %})

### Images and GIFs setup

1. Copy the image or GIF URL from the DAM in Cloudinary by going to **Assets** > **Media Library** > **Assets** > **Copy URL**.
2. Create the image tag in HTML, then add `f_auto,q_auto` to the copied URL to optimize the image or GIF.

#### Example image URL

{% raw %}
```bash
<img src="https://res.cloudinary.com/demo/image/upload/v1678993440/f_auto,q_auto/cld-sample.jpg" alt="Summer Campaign">
</img>
```
{% endraw %}

### Videos setup

1. Copy the image or GIF link from the DAM in Cloudinary by going to **Assets** > **Media Library** > **Assets** > **Copy URL**.
2. Create the video tag in HTML, then add `f_auto,q_auto` to the copied URL to automatically optimize the format and quality of the video.

#### Example video URL

{% raw %}
```bash
<video class="video" autoplay muted playsinline controls>
  <source src="https://res.cloudinary.com/demo/video/upload/v1651840278/f_auto,q_auto/samples/cld-sample-video.mp4">
</video>
```
{% endraw %}

Refer to [Video]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/video/) for specific Android and iOS considerations. 

{% endtab %}
{% tab Convert videoes into GIFs %}

## Convert videoes to GIFs for emails

Use the `f_auto:animated` [Cloudinary Transformation](https://cloudinary.com/documentation/image_transformations/) to automatically convert video assets to GIFs. This is of particular value if you're using the Braze email channel, as GIFs are optimized to reduce email payloads, which, if too high, can cause deliverability issues. 

### Conversion setup

1. Copy the video URL from the Cloudinary DAM.
2. Create the image tag and add `f_auto:animated,fl_lossy` to reduce the GIF size and pick the best animated format for the client.
3. Add `c_scale,w_nnn` to correspond to the desired GIF width in the email layout.
4. Add `e_loop` to loop the animation.

#### Example GIF URL

{% raw %}
```
https://res.cloudinary.com/demo/video/upload/c_scale,w_500,e_loop/f_auto:animated,fl_lossy/samples/cld-sample-video.gif
```
{% endraw %}

{% endtab %}
{% tab Target attributes %}

## Dynamically select campaign assets based on targeting attributes

This integration method enables dynamic media personalization by intelligently selecting the best asset for each user based on their attributes in real time. 

If you include Liquid tags as parameters in a Cloudinary link within a Braze campaign message, when the message is sent, the associated Braze attributes will dynamically replace the Liquid tags. This could be user-specific data such as language or customer tier. Cloudinary will then use those attributes to determine which campaign asset best fits that user, and automatically return the correct image or video. This results in recipients only receiving assets that are contextually relevant and brand approved.

### How it works

Cloudinary organizes campaign assets using [tags](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#tags) and [Structured Metadata (SMD)](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#structured_metadata) to make them searchable. 

Each campaign asset is grouped under a campaign tag (for example, `spring_launch`) and enriched with structured metadata fields that correspond to Braze attributes like `language=en` or `tier=gold`. When Braze calls the Cloudinary link, a [Custom Function](https://cloudinary.com/documentation/custom_functions#javascript_filters) processes the incoming attributes, searches for the asset with matching tags and metadata, and then returns the best fitting match. 

If an exact match isn’t found, the function automatically selects a fallback or “next best” option for continuity in every experience. When the asset is selected, Cloudinary’s transformation layer (for example, `f_auto` or `q_auto`) optimizes the media for delivery. This combination of tagging, metadata, and custom functions gives developers a flexible, API-driven way to automate personalized asset delivery.

{% alert tip %}
Refer to Cloudinary's [`braze-personalization` GitHub repo](https://github.com/cloudinary-devs/braze-personalization) for instructions on creating and applying custom functions, and an example custom function for asset selection and fallback options for a given campaign. For more guidance, contact your Cloudinary support team.
{% endalert %}

### Prerequisites

To enable dynamic asset selection, Cloudinary must be able to return a set of assets based on tags and metadata. If the list delivery type is restricted, Cloudinary cannot provide the dynamic list needed for personalized asset selection in Braze campaigns.
- Unrestrict the list delivery type: Open the Security Settings in your Cloudinary Console, and clear the Resource list item under Restricted image types.

### Dynamic selection setup

1. Set up the tag and the metadata for assets in Cloudinary.
2. Upload your custom function to the Cloudinary DAM.
3. Create the Cloudinary URL for the desired tag.
4. Using the tag URL as a base, add dynamic image Liquid tags to incorporate Braze attributes and the custom function.

#### Example URL

This example presumes that assets in Cloudinary have two defined SMD fields (“locale” and “audience”) populated with the expected values corresponding to Braze attributes. Also, assets required for the campaign have been given the "samples" tag, and the custom function `segmentedBanner.js` has been uploaded into the Cloudinary account. 

{% raw %}
```bash

// Use the appropriate Braze attributes.
{% assign audience = {{custom_attribute.${sample_audience_identifier}}} %} 
{% assign locale = {{${language}}}%} 

// The URL for the "samples" tag used in the campaign is https://papish.cloudinary.us/image/list/v1690000000/samples.json, which is the base for the dynamic image URL.
<img src="https://papish.cloudinary.us/image/list/f_auto,q_auto/$locale_#{locale}/$audience_!{audience}!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/campaigns/samples.json" alt="Banner"> 
```
{% endraw %}

##### Output URLs

- Output URL for users with audience `internal` and locale `en`: 
```
https://papish.cloudinary.us/image/list/f_auto,q_auto/$locale_!en!/$audience_!Internal!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```
- Output URL for users with audience `external` and locale `es`: 
```
https://papish.cloudinary.us/image/list/$locale_!es!/$audience_!External!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```
- Fallback image URL: 
```
https://papish.cloudinary.us/image/list/$locale_!unknown!/$audience_!unknown!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```

{% endtab %}
{% tab Personalized image generation %}

## Personalized image generation

Cloudinary’s [Text Overlay Transformations](https://cloudinary.com/documentation/accessible_media_visual_audio_clarity#text_overlays_on_images_and_videos/) use user data from Braze directly within a Cloudinary asset. 

The following example demonstrates how the `l_text` Transformation can be used to insert a user's name onto an asset. Further customization can be achieved by leveraging Liquid tags when developing campaigns and Canvases to determine what text should populate the `l_text` parameters.

For more guidance on how Transformation parameters can be used to design an asset, contact your Cloudinary support team.

### Example `l_text` Transformation

{% raw %}
```bash
{% assign first_name = {{${first_name}}}%} 
{% assign second_name = {{${last_name}}}%} 

<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20{{first_name}}%20{{second_name}}%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">
```
{% endraw %}

#### Example output URL

{% raw %}
```bash
<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20John%20Smith%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">
```
{% endraw %}

![A white church with a blue roof overlooking the sea, in the top left of the image the words "John Smith" are imposed on an opage dark great rectangle.]({% image_buster /assets/img/cloudinary/two.png %})

```
{% endtab %}
{% endtabs %}
