---
nav_title: Read and Unread Indicators
article_title: News Feed Read and Unread Indicators for Web
platform: Web
page_order: 2
page_type: reference
description: "This article covers how to interact with News Feeds via the Braze SDK."
channel: news feed

---

# Read and unread indicators

Braze provides an unread and read indicator on News Feed cards as shown in the following image:

![A News Feed card showing an image of a watch along with some text. In the upper corner of the text is a blue or grey triangle that indicates if a card has been read or not. A blue triangle signifies that a card has been read.][25]

## Disabling the indicators

In order to disable this functionality add the following style to your CSS:

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```

[25]: {% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %}
