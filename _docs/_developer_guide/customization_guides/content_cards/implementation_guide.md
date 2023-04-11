---
nav_title: Extending Content Cards
article_title: Extending Content Cards
page_order: 3
description: "This advanced implementation guide covers Content Card code considerations with three use cases built by our team."
channel:
  - content cards

---

# Extending Content Cards

This article provides three examples of more advanced use cases for Content Cards. Each use case offers a explanation and a look into how Content Card variables may look and be used in the Braze dashboard:
- [Content Cards as supplemental content](#content-cards-as-supplemental-content)
- [Content Cards in a message center](#content-cards-in-a-message-center)
- [Interactive Content Cards](#interactive-content-cards)

{% alert important %}
Looking for the basic Content Card developer integration guide? Find it [here]({{site.baseurl}}/docs/developer_guide/home).
{% endalert %}

## Content Cards as supplemental content

![][1]{: style="float:right;max-width:25%;margin-left:15px;border:0;"}

You can seamlessly blend Content Cards into an existing feed, allowing data from multiple feeds to load simultaneously. This creates a cohesive, harmonious experience with Braze Content Cards and existing feed content.

The example to the right shows a `UICollectionView` with a hybrid list of items that are populated via local data and Content Cards powered by Braze. With this, Content Cards can be indistinguishable alongside existing content.

### Dashboard configuration

This Content Card is delivered by an API-triggered campaign with API-triggered key-value pairs. This is ideal for campaigns where the card's values depend on external factors to determine what content to display to the user. Note that `class_type` should be known at set-up time.

![The key-value pairs for the supplemental Content Cards use case. In this example, different aspects of the card such as "tile_id", "tile_deeplink", and "tile_title" are set using Liquid.][2]{: style="max-width:60%;"}

## Content Cards in a message center

Content Cards can be used in a message center format where each message is its own card. Each message in the message center is populated via a Content Card payload, and each card contains additional key-value pairs that power on-click UX. In the following example, one message directs you to an arbitrary custom view, while another opens to a webview that displays custom HTML.

![][3]{: style="border:0;"}{: style="max-width:80%;border:0"}

### Dashboard configuration

For the following message types, the key-value pair `class_type` should be added to your dashboard configuration. The values assigned here are arbitrary but should be distinguishable between class types. These key-value pairs are the key identifiers that the application looks at when deciding where to go when the user clicks on an abridged inbox message.

{% tabs local %}
{% tab Arbitrary custom view message (full page) %}

The key-value pairs for this use case include:

- `class_type` set as `message_full_page`
- `message_header` set as `Full Page`

![]({% image_buster /assets/img/cc_implementation/full_page.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Webview message (HTML) %}

The key-value pairs for this use case include:

- `class_type` set as `message_webview`
- `message_header` set as `HTML`
- `message_title` set as a string with your content.

This message also looks for an HTML key-value pair, but if you are working with a web domain, a URL key-value pair is also valid.

![]({% image_buster /assets/img/cc_implementation/html_webview.png %}){: style="max-width:60%;"}

{% endtab %}
{% endtabs %}

![An interactive Content Card showing a 50 percent promotion appear in the botton left corner of the screen. Once clicked, a promotion will be applied to the cart.][4]{: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"} 

## Interactive Content Cards
<br>
Content Cards can be leveraged to create dynamic and interactive experiences for your users. In the example to the right, we have a Content Card pop-up appear at checkout providing users last-minute promotions. 

Well-placed cards like this are a great way to give users a "nudge" toward specific user actions. 

### Dashboard configuration

The dashboard configuration for interactive Content Cards is quick and straightforward. The key-value pairs for this use case include a `discount_percentage` set as the desired discount amount and `class_type` set as `coupon_code`. These key-value pairs are how type-specific Content Cards get filtered and displayed on the checkout screen.

![][5]{: style="max-width:70%;"} 

[1]: {% image_buster /assets/img/cc_implementation/supplementary.png %}
[2]: {% image_buster /assets/img/cc_implementation/supplementary_content.png %}
[3]: {% image_buster /assets/img/cc_implementation/message_center.png %}
[4]: {% image_buster /assets/img/cc_implementation/discount2.png %}
[5]: {% image_buster /assets/img/cc_implementation/discount.png %}