---
nav_title: December
page_order: 0
noindex: true
page_type: update
description: "This article contains release notes for December 2021."
alias: "/help/release_notes/2022/january/"
---
# December 2021

## Update to export users by segment endpoint

Beginning December 2021, the following changes take effect for the [Export users by segment endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/):

1. The `fields_to_export` field in this API request will be required. The option to default to all fields will be removed.
2. The fields for `custom_events`, `purchases`, `campaigns_received`, and `canvases_received` will only contain data from the last 90 days.

## New properties for Currents message engagement events

New properties have been added for select [message engagement events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/). This update applies to the following Currents message engagement events and all partners that use them:

- Add `LINK_ID`, `LINK_ALIAS` to:
  - Email Click (all destinations)
- Add `USER_AGENT` to:
  - Email Open
  - Email Click
  - Email Mark As Spam
- Add `MACHINE_OPEN` to:
  - Email Open

## New Liquid personalization tag

We now support targeting users who have foreground push enabled on their device with the following Liquid tags:

{% raw %}
- `{{most_recently_used_device.${foreground_push_enabled}}}`
- `{{targeted_device.${foreground_push_enabled}}}`
{% endraw %}

For more information, refer to [Supported personalization tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

## About webhooks

Webhooks are powerful, flexible tools—but they can be a bit confusing. If you're wondering what webhooks are and how you can use them in Braze, check out our new article on [About webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/).

## Amazon Personalize

Amazon Personalize is like having your very own all day Amazon machine learning recommendation system. Based on over 20 years of recommendation experience, Amazon Personalize enables you to improve customer engagement by powering real-time personalized product and content recommendations and targeted marketing promotions. 

If you'd like to learn more, visit our new [Amazon Personalize]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalized_recommendations/amazon_personalize) article to understand the use cases Amazon Personalize offers, data it works with, how to configure the service, and how to integrate it with Braze.

## New Braze partnerships

### Yotpo – eCommerce

The [Yotpo]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/yotpo/) and Braze integration allows you to dynamically pull and display star ratings, top reviews, and visual user-generated content on products within emails and other communication channels within Braze. You can also include customer-level loyalty data in emails and other communication methods to create a more personalized interaction, boosting sales and loyalty.

### Zeotap – Customer data platform

With the [Zeotap]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/zeotap/) and Braze integration, you can extend the scale and reach of your campaigns by syncing Zeotap customer segments to map Zeotap user data to Braze user accounts. You can then act on this data, delivering personalized target experiences to your users.