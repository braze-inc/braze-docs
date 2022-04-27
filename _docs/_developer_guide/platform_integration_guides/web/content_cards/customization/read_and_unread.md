---
nav_title: Read & Unread Indicators
article_title: Content Card Read & Unread Indicators for Web
page_order: 2
platform: Web
channel: content cards
page_type: reference
description: "This reference article covers Content Card read and unread indicators in your web application."

---

# Read and unread indicators

Braze provides indicators on Content Cards as shown in the following screenshots:

|Indicator|Example |
|---|---|
| Read | ![A web content card without a blue line beneath the card signifying it has been read.][2] |
| Unread | ![A web content card with a blue line beneath the card signifying it has not been read.][3] |
{: .reset-td-br-1 .reset-td-br-2}

## Changing colors

To change the color of the unread indicator of a card, add custom CSS to your webpage. For example, changing it to green with the following CSS:

```css
.ab-unread-indicator { background-color: green !important; }
```

## Disabling the indicators

In order to disable this functionality, add the following style to your `css`:

```css
.ab-unread-indicator { display: none; }
```

[2]:{% image_buster /assets/img_archive/readcontentcard.png %}
[3]:{% image_buster /assets/img_archive/unreadcontentcard.png %}
