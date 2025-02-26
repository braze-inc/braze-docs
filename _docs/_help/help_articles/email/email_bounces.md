---
nav_title: Email Bounces
article_title: Email Bounces
page_order: 0
page_type: solution
description: "This help article clarifies the difference between hard bounces and soft bounces."
channel: email
---

# Email bounces

What do you do when a message from your email campaign bounces back from your users' email addresses? First, let's define and troubleshoot the two types of email bounces: hard bounces and soft bounces. 

## Hard bounces

{% multi_lang_include metrics.md metric='Hard Bounce' %}

For more information, see [Hard bounce]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#hard-bounce).

## Soft bounces

{% multi_lang_include metrics.md metric='Soft Bounce' %} 

If an email receives a soft bounce, we will usually retry within 72 hours, but the number of retry attempts varies from receiver to receiver.

While soft bounces aren't tracked in your campaign analytics, you can monitor the soft bounces in the [Message Activity Log][3]. Here, you can also see the reason for the soft bounces and understand possible discrepancies between the "sends" and "deliveries" for your email campaigns.

To learn more about managing your email subscriptions and campaigns, check out [Best practices for email][2].

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on May 2, 2024_

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices
[3]: {{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/
