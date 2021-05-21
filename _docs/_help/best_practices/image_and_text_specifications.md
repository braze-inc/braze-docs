---
nav_title: Image and Text Specifications
page_order: 7

page_type: reference
description: "This article includes tips and tricks for ensuring your images and text are rendered just right."
tool: Media
---
# Image and Text Specifications

## Tips and Tricks for Rendering

For every and any channel you use to communicate with your users, here are some of Braze’s recommendations to help you ensure your images and text are rendered just right.

### General Tips

### In-App Messages

#### Images

In general, Braze recommends using images that fit into a 16:10 screen.

- __All images must be less than 5MB.__
- We only accept `PNG`, `JPG`, and `GIF` file types.
- We recommend hosting images in the [Braze Media Library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) to enable the Braze SDK to download assets from our CDN for offline message display.
- For full-screen messages, follow our guidelines for [Image Safe Zone]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone).
<br><br>
{% tabs %}
  {% tab Full-Screen %}
  [Further details for full-screens]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen)

  | Layout | Asset Size | Notes |
  |--- | --- | --- |
  | Image + Text | 6:5 aspect ratio<br>Hi-Res 1200 x 1000px<br> Min. 600 x 500px | Cropping can occur on all sides, but the image will always fill the top 50% of the viewport |
  | Image Only | 3:5 aspect ratio<br>Hi-Res 1200 x 2000px<br> Min. 600 x 1000px | Cropping can occur on the left and right edges on taller devices |
  {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}


{% endtab %}
{% tab Modal %}

  [Further details for modals]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/modal)

  | Layout | Asset Size | Notes |
  |--- | --- | ------ |
  | Image + Text | 29:10 aspect ratio<br>Hi-Res 1200 x 415px<br> Min. 600 x 205px | Tall images will scale down and be horizontally centered. Wide images will be clipped on the left and right edges. |
  | Image Only | Nearly any aspect ratio<br>Hi-Res up to 1200 x 2000px<br> Min. 600 x 600px | The message will resize to fit images of most aspect ratios. |
  {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Slideup %}

[Further details for slideups]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup)

| Layout | Asset Size | Notes |
|--- | --- | --- |
| Image + Text | 1:1 aspect ratio<br>Hi-Res 150 x 150px<br> Min. 50 x 50px | Images of various aspect ratios will fit into a square image container, without cropping. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% endtabs %}

#### Text

While there are no limits to how many characters of text you can include in an in-app message (as well as buttons, headline, main body, etc.) we recommend that you avoid too much text in in-app messages because they make can require users expand and scroll the message.

### Native Mobile Push Notifications

#### Images

**Image Type** | **Recommended Image Size** | **Max Image Size** | **File Types**
--- | --- | --- | ---
(iOS) 2:1 *Recommended* | 500KB | 5MB | PNG, JPG, GIF
(Android) Push Icon | 500KB | 5MB | PNG, JPG
(Android) Expanded Notification | 500KB | 5MB | PNG, JPG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

#### Text

**Message Type** | **Max Message Length**
--- | ---
(iOS) Lock Screen | 110 Characters
(iOS) Notification Center | 110 Characters
(iOS) Banner Alert | 63 Characters
(Android) Lock Screen | 49 Characters
(Android) Notification Drawer | 597 Characters
{: .reset-td-br-1 .reset-td-br-2}

#### Payload Size

**Platform** | **Size**
--- | ---
pre iOS 8 | 0.256 KB
post iOS 8 | 2 KB
Android (FCM) | 4 KB
{: .reset-td-br-1 .reset-td-br-2}

### Web Push Notifications

#### Images

| **Browser** | **Recommended Icon Size**
| --- | ---
Chrome | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | Icons not configurable on a per-campaign basis
Opera | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2}

| **Browser** | **Platform** | **Large Image Size**
| --- | --- | ---
Chrome | macOS | N/A
Chrome | Android | 2 : 1 aspect ratio
Chrome | Windows | 360 ≥ x 240
Firefox | macOS| N/A
Safari | macOS | N/A
Opera | macOS | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Text

| **Browser** | **Platform** | **Maximum Title Length**  | **Maximum Message Body Length**
| --- | --- | --- | ---
Chrome | macOS | 35 | 50
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
Opera | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### News Feed Specifications

#### Images

**Type** | **Aspect Ratio** | **Recommended Image Size** | **Max Image Size** | **File Types**
--- | --- | --- | --- | ---
Classic Card | 1:1 (110 pixels wide minimum) | 500KB | 1MB | PNG, JPG, GIF
Captioned Image Card | 4:3 (600 pixels wide minimum) | 500KB | 1MB | PNG, JPG, GIF
Banner Card | 6:1 (600 pixels wide mimimum) | 500KB | 1MB | PNG, JPG, GIF
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### MMS

#### Images

**Image Specifications** | **Recommended Properties**
--- | ---
Size | 5MB maximum
File Types | PNG, JPG, GIF
{: .reset-td-br-1 .reset-td-br-2}


### Email

#### Images

**Image Specifications** | **Recommended Properties**
--- | ---
Size | 5MB maximum
Width | (Header: 600 pixels maximum) (Body: 480 pixels maximum)
File Types | PNG, JPG, GIF
{: .reset-td-br-1 .reset-td-br-2}

#### Text

**Text Specifications** | **Recommended Properties**
--- | ---
Subject Line Length | 35 characters maximum (for optimal mobile display) (6 to 10 words)
Sender Name Length | 25 characters maximum (for optimal mobile display)
Pre-Header Length | 85 characters maximum
{: .reset-td-br-1 .reset-td-br-2}

#### Size

**Email Type** | **Recommendations**
--- | ---
Text Only | 25KB maximum
Text With Images | 60KB maximum
Email Width | 600 pixels maximum
{: .reset-td-br-1 .reset-td-br-2}
