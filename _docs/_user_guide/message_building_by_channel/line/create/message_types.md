---
nav_title: Message Types
article_title: LINE Message Types
page_order: 1
description: "This article covers the different types of LINE messages."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
hidden: true
permalink: /line/create/message_types/
---

# LINE message types

> This article covers the LINE message types you can compose, including aspects and li,itations, and is part of the LINE beta collection. [Return to the main page](https://www.braze.com/docs/line/).

{% alert important %}
LINE access is in beta and only available in select Braze packages. Reach out to your account manager or customer success manager to get started.
{% endalert %}

When you compose a LINE message, you can drag-and-drop message types into the composer and then customize them.

![][5]

## Text

A text message can contain up to 5,000 characters.

![][1]

## Image

![][2]

An image can be added through the [Media Library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) or a URL.

### URL image

Use URL images for use cases such as:
- Liquid dynamic images 
- Connected content 
- Braze catalogs

| **Image specifications** | **Recommended properties** |
|--------------------------|----------------------------|
| Image file URL length | 2,000 characters maximum  |
| Image format          | PNG, JPEG             |
| File size     |  10&nbsp;MB maximum |
{: .reset-td-br-1 .reset-td-br-2}

## Rich messages (image map)

![][3]

## Card-based (carousel)

![][4]

[1]: {% image_buster /assets/img/line/line_text_message.png %}
[2]: {% image_buster /assets/img/line/line_image_message.png %}
[3]: {% image_buster /assets/img/line/line_rich_message.png %}
[4]: {% image_buster /assets/img/line/line_card_message.png %}
[5]: {% image_buster /assets/img/line/line_message_types.png %}
