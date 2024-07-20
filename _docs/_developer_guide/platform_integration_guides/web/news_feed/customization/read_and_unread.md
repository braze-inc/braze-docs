---
nav_title: Read and Unread Indicators
article_title: News Feed Read and Unread Indicators for Web
platform: Web
page_order: 2
page_type: reference
description: "This article covers how to set read and unread indicators in your News Feed cards via the Braze SDK."
channel: news feed

---

# Read and unread indicators

> This article covers how to set read and unread indicators in your News Feed cards via the Braze SDK.

{% alert note %}
News Feed is being deprecated. Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. Check out the [migration guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) for more.
{% endalert %}

Braze provides an unread and read indicator on News Feed cards as shown in the following image:

![A News Feed card showing an image of a watch along with some text. In the upper corner of the text is a blue or gray triangle that indicates if a card has been read or not. A blue triangle signifies that a card has been read.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

## Disabling the indicators

In order to disable this functionality add the following style to your CSS:

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```

[25]: {% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %}
