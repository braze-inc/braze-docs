---
nav_title: API-Triggered Delivery
article_title: API-Triggered Delivery
page_order: 2
page_type: reference
description: "This reference article describes how to schedule an API-triggered campaign."
tool: Campaigns
platform: API

---

# API-Triggered Campaigns 

API-triggered campaigns or server-trigger campaigns are ideal for more advanced transactional use-cases. Braze API-triggered campaigns allow marketers to manage campaign copy, multivariate testing, and re-eligibility rules within the Braze dashboard while triggering the delivery of that content from their own servers and systems. The API request to trigger the message can also include additional data to be templated into the message in real-time.

## Setting up an API-Triggered Campaign

Setting up an API-triggered campaign takes a few quick steps. First, create a new multichannel or single-channel campaign (with multivariate testing).

{% alert note %}
An API-triggered campaign is different from an [API campaign]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns).
{% endalert %}

Next, configure your copy and notifications the same way as you would were it a normally scheduled notification and select __API-Triggered Delivery__. For more information on the triggering of these campaigns from your server, please see the endpoint documentation section on [API-triggered campaign sending]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).

![API-Triggered Delivery Step][37]

## Using the Templated Content Included with an API Request

In addition to triggering the message, you can also include content with the API request to be templated into the message within the `trigger_properties` object. This content can be referenced in the body of the message by saying something like
``{% raw %} {{ api_trigger_properties.${ some_value_included_with_request }}} {% endraw %}``.
See the following social notification example use case for additional context:

![Social Example Delivery Window][38]{: style="max-width:70%;"}

## Re-eligibility with API-Triggered Campaigns

The number of times a user receives an API-triggered campaign can be limited using re-eligibility settings, meaning the user will receive the campaign only once or once in a given window, regardless of how many times the API trigger is fired.

For example, if you are using an API-triggered campaign to send the user a campaign about an item they recently viewed, you can limit the campaign to send a maximum of one message a day regardless of how many items they viewed while firing the API trigger for each item. On the other hand, if your API-triggered campaign is transactional, you will want to make sure that the user receives the campaign every time they do the transaction by setting the delay to 0 minutes:

![Re-eligibility settings][43]


[37]: {% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %}
[38]: {% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}
[39]: {{site.baseurl}}/developer_guide/rest_api/messaging/#sending-messages-via-api-triggered-delivery
[42]: {{site.baseurl}}/developer_guide/rest_api/messaging/#sending-messages-via-api-triggered-delivery
[43]: {% image_buster /assets/img_archive/api_triggered_reeligible.png %}