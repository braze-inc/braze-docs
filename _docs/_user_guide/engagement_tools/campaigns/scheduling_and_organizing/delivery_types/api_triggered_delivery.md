---
nav_title: API Triggered Delivery
page_order: 2

tools: campaigns
page_type: reference
description: "This reference article gives an overview of different ways to go about scheduling a campaign."
---

# API Triggered Campaigns (Server Triggered Campaigns)

API Triggered Campaigns are ideal for more advanced transactional use-cases. Braze API Triggered Campaigns allow marketers to manage campaign copy, multivariate testing, and re-eligibility rules within the Braze dashboard while triggering the delivery of that content from their own servers and systems. The API request to trigger the message can also include additional data to be templated into the message in real-time.

## Setting up an API Triggered Campaign

Setting up an API Triggered Campaign is easy. First, create a new multi-channel or single-channel campaign (with multivariate testing).

{% alert note %}
An API Triggered Campaign is different from an [API Campaign]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns).
{% endalert %}

![API Triggered Creation Step][45]

Next, simply configure your copy and notifications the same way as you would were it a normally scheduled notification and select "API Triggered Delivery". For more information on the triggering of these campaigns from your server please see the documentation section on [API Triggered Campaigns][42].

![API Triggered Delivery Step][37]

## Using the Templated Content Included With an API request

In addition to triggering the message, you can also include content with the API request to be templated into the message within the `trigger_properties` object. This content can be referenced in the body of the message by saying something like
``{% raw %} {{ api_trigger_properties.${ some_value_included_with_request }}} {% endraw %}``.
See the following social notification example use-case for additional context:

![Social Example Delivery Window][38]

For information regarding triggering messages with API Triggered Delivery, please see [this section of our technical documentation][39].

## Re-eligibility with API Triggered Campaigns

The number of times a user receives an API triggered campaign can be limited using re-eligibility settings, meaning the user will receive the campaign only once, or once in a given window, regardless of how many times the API trigger is fired.

For example, if you are using an API triggered campaign to send the user a campaign about an item they recently viewed, you can limit the campaign to send a maximum of one message a day regardless of how many items they viewed while firing the API trigger for each item. On the other hand, if your API triggered campaign is transactional, you will want to make sure that the user receives the campaign every time they do the transaction by setting the delay to 0 minutes:

![Re-eligibility settings][43]



[3]: {% image_buster /assets/img_archive/time_based.png %}
[5]: #local-time-zone-campaigns
[7]: {{site.baseurl}}/help/best_practices/user_onboarding/#user-onboarding
[8]: {{site.baseurl}}/user_guide/intelligence/intelligent_timing/
[9]: {% image_buster /assets/img_archive/schedule_designated.png %}
[10]: {% image_buster /assets/img_archive/schedule_immediately.png %}
[14]: {% image_buster /assets/img_archive/schedule_intelligent.png %}
[17]: {% image_buster /assets/img_archive/schedule_triggered1.png %}
[18]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[19]: {% image_buster /assets/img_archive/schedule_triggered22.png %}
[20]: {% image_buster /assets/img_archive/schedule_triggered32.png %}
[21]: {% image_buster /assets/img_archive/schedule_triggered43.png %}
[22]: #use-cases-2
[24]: {% image_buster /assets/img_archive/ReEligible.png %}
[25]: {{site.baseurl}}/help/faqs/#how-does-local-time-zone-delivery-work
[26]: #why-did-a-user-not-receive-my-triggered-campaign
[27]: {% image_buster /assets/img_archive/schedule_triggered5.png %}
[28]: {% image_buster /assets/img_archive/schedule_triggered6.png %}
[29]: {{site.baseurl}}/help/best_practices/in-app_messages/in-app_message_behavior/#in-app-message-delivery-rules
[30]: {{site.baseurl}}/help/best_practices/user_onboarding/#user-onboarding
[31]: {% image_buster /assets/img_archive/schedule_triggered_next_available.png %}
[32]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[33]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/campaign_connector/#campaign-connector
[34]: {% image_buster /assets/img_archive/customEventProperties.png %}
[34]: {% image_buster /assets/img_archive/customEventProperties.png %}
[37]: {% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %}
[38]: {% image_buster /assets/img_archive/api_trigger_photo_social_example_1.png %}
[39]: {{site.baseurl}}/developer_guide/rest_api/messaging/#sending-messages-via-api-triggered-delivery
[41]: {% image_buster /assets/img_archive/schedule_triggered7.png %}
[42]: {{site.baseurl}}/developer_guide/rest_api/messaging/#sending-messages-via-api-triggered-delivery
[43]: {% image_buster /assets/img_archive/api-trigger-reeligible.png %}
[45]: {% image_buster /assets/img_archive/api_triggered_creation_step.png %}
[46]: {{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns
[47]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign
[48]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties
[49]: {{site.baseurl}}/help/help_articles/campaigns_and_canvas/not_triggering/
[50]: {% image_buster /assets/img_archive/schedule_triggered8.png %}