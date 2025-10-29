---
nav_title: cloudinary
article_title: cloudinary
description: "This reference article outlines the partnership between Braze and cloudinary."
alias: /partners/cloudinary/
page_type: partner
search_tag: Partner
---

# Cloudinary

> Cloudinary is the ideal image and video platform to manage, edit, optimize and deliver images and video on a massive scale to any campaign across channels and customer journeys.

## About this integration

Connecting Cloudinary to Braze empowers brands to access visual media stored in Cloudinary Assets for use in Braze messaging channels. With Cloudinary’s dynamic links, marketers can select and customize images and videos in real time based on end user attributes in Braze. Together, Cloudinary and Braze make it easy to craft visually stunning, highly personalized campaigns that tell every product’s story and deliver one-of-a-kind experiences at scale.

This guide outlines four possible integration paths between Cloudinary and Braze. The goal is to enable dynamic, contextual, and personalized asset delivery for Braze Campaigns and Canvasses through Cloudinary's media management and image and video capabilities. 

The integration paths outlined below are not exhaustive. They primarily rely on modifying asset links manually copied from Cloudinary’s Media Library’s, to illustrate how Braze Personalisation can be combined with Cloudinary’s dynamic delivery at scale. 

{% alert important %}
More advanced integration paths, including leveraging [Connected Content]({{site.baseurl}}/docs/user_guide/personalization_and_dynamic_content/connected_content) to call Cloudinary’s [Admin API](https://cloudinary.com/documentation/admin_api#banner) are possible, but the approach will vary between customers. Contact your Cloudinary and Braze CSM for guidance with Connected Content
{% endalert %}



## Prerequisites

Before you start, you need the following:

| Requirements     | Description |                        
|-----------------------|-----------------|
| Cloudinary Account  | A [Cloudinary Account](https://cloudinary.com/users/register_free) is required to take advantage of this partnership  |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Integration: Campaign Asset Selection via Cloudinary DAM

The most direct way to leverage images and videos directly from Cloudinary's DAM when setting up a Braze campaigns and canvasses is to pull the URL from Cloudinary’s Media Library’s Asset page.




{% alert important %}f_auto and q_auto are examples of Cloudinary’s Transformations. The full range of Cloudinary Transformations offers deeper levels of customization of the behaviour and appearance for [image](https://cloudinary.com/documentation/image_transformations#banner) and [video](https://cloudinary.com/documentation/video_manipulation_and_delivery#banner) assets.

>For more information on modifying a Cloudinary Asset link to include Transformations, please [review Cloudinary’s documentation](https://cloudinary.com/documentation/image_transformations#transformation_url_structure).
{% endalert %}

### For Images and Gifs

<ul>
     <li>Copy the URL to the image or Gif from the Cloudinary DAM. Cloudinary > Assets > Media Library > Assets > Copy URL</li>
    <li>Create the image tag in HTML,  add f_auto,q_auto to the copied url to optimize the image or Gif as shown below  </li>
</ul>

```bash
<img src="https://res.cloudinary.com/demo/image/upload/v1678993440/f_auto,q_auto/cld-sample.jpg" alt="Summer Campaign">
</img>
```

### For Videos
<ul>
<li>Copy the URL to the image or Gif from the Cloudinary DAM. Cloudinary > Assets > Media Library > Assets > Copy URL</li>
<li>Create the video tag in HTML, add f_auto,q_auto to the copied url to automatically optimize the format and quality of the video as shown below</li>    
</ul>

```bash
<video class="video" autoplay muted playsinline controls>
  <source src="https://res.cloudinary.com/demo/video/upload/v1651840278/f_auto,q_auto/samples/cld-sample-video.mp4">
</video>
```

Refer [to this documentation](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/traditional/customize/video) for specific Android and iOS considerations 

## Integration: Transforming Video to Gifs for emails

The `f_auto:animated` transformation allows users to automatically convert video assets to gifs. This is of particular value if the email channel is being used in Braze, as gifs are optimized to reduce email payloads, which, if too high, can cause deliverability issues. 

### Setup
<ul>
<li>Copy the URL for the video from the Cloudinary DAM</li>
<li>Create the image tag and add f_auto:animated,fl_lossy to reduce the size of the gif and pick the best animated format for the client.</li>
<li>Also add c_scale,w_nnn (to correspond to the desired width of the gif in the email layout)</li>
<li>And finally, e_loop to loop the animation</li>
</ul>

```bash
https://res.cloudinary.com/demo/video/upload/c_scale,w_500,e_loop/f_auto:animated,fl_lossy/samples/cld-sample-video.gif
```
## Integration: Dynamic campaign asset selection based on targeting attributes

This enables dynamic media personalization at scale by intelligently selecting the best asset for each user based on their attributes in real time. When a campaign message is sent from Braze, standard and custom attributes in braze can be inserted as parameters into a Cloudinary dynamic link using liquid tags. This could be user specific data such as language, or customer tier. Cloudinary then uses these attributes to determine which campaign asset best fits that user, automatically returning the correct image or video through its transformation and delivery pipeline. This ensures recipients see assets that’re contextually relevant and brand approved.

Under the hood, Cloudinary organizes campaign assets using [tags](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#tags) and [Structured Metadata (SMD)](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#structured_metadata) to make them searchable. Each campaign asset is grouped under a campaign tag (for example, `spring_launch`) and enriched with structured metadata fields that correspond to Braze attributes like `language=en or tier=gold`. When Braze calls the Cloudinary link, a [Custom Function](https://cloudinary.com/documentation/custom_functions#javascript_filters) processes the incoming attributes, searches for the asset with matching tags and metadata, and returns the best-fit match. If an exact match isn’t found, the function automatically selects a fallback or “next best” option, ensuring continuity in every experience. Once the asset is selected, Cloudinary’s transformation layer (e.g. `f_auto`, `q_auto`) optimizes the media for delivery. This combination of tagging, metadata, and custom functions gives developers a flexible, API-driven way to automate personalized asset delivery.

See [this github repo](https://github.com/cloudinary-devs/braze-personalization) created by Cloudinary, for instructions and an example custom function for asset selection and fall back options for a given campaign. For more guidance on the creation and application of Custom Functions, contact your Cloudinary support team.
### Setup

<ul>
<li>Setup the tag and the metadata for assets in Cloudinary as described here</li>
<li>Upload your custom function to the cloudinary DAM</li>
<li>Create the cloudinary URL for the desired tag as documented here. This is the core of the dynamic URL.   </li>
<li>Based on the URL for the tag, create the dynamic image tag incorporating Braze attributes and the custom function as shown below in the example</li>
</ul>

The example below presumes that assets in cloudinary have two SMD fields defined, “locale” and “audience”, populated with the expected values corresponding to Braze attributes. Further, assets required for the campaign have been given the ‘samples’ tag, and the custom function `segmentedBanner.js` has been uploaded into the cloudinary account. 

```bash
Example: 
//Use appropriate Braze attributes
{% assign audience = {{custom_attribute.${sample_audience_identifier}}} %} 
{% assign locale = {{${language}}}%} 
//The URL for the 'samples' tag used in the campaign: https://papish.cloudinary.us/image/list/v1690000000/samples.json 

//The dynamic image url. 
<img src="https://papish.cloudinary.us/image/list/f_auto,q_auto/$locale_#{locale}/$audience_!{audience}!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/campaigns/samples.json" alt="Banner"> 

Output URL for users with audience 'internal' and locale 'en':
https://papish.cloudinary.us/image/list/f_auto,q_auto/$locale_!en!/$audience_!Internal!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json

Output URL for users with audience 'external' and locale 'es':
https://papish.cloudinary.us/image/list/$locale_!es!/$audience_!External!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json

Fallback image:
https://papish.cloudinary.us/image/list/$locale_!unknown!/$audience_!unknown!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json

```

## Integration: Personalized Image Generation

Cloudinary’s [Text Overlay Transformations](https://cloudinary.com/documentation/accessible_media_visual_audio_clarity#text_overlays_on_images_and_videos) can be used to leverage user data from Braze directly within a Cloudinary Asset. More guidance on how Transformation parameters can be used to design an asset can be offered by Cloudinary, our example demonstrates how the `l_text` transformations can be used to insert a users name onto an asset. 

Further customisation can be achieved by leveraging Liquid tags when developing campaigns and canvases to determine what text should populate the “l_text” parameters.

```bash

{% assign first_name = {{${first_name}}}%} 
{% assign second_name = {{${last_name}}}%} 

<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20{{first_name}}%20{{second_name}}%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">

Output URL Example: 

<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20John%20Smith%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">

```



