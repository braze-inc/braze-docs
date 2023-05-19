---
nav_title: Email Bounces
article_title: Email Bounces
page_order: 0
page_type: solution
description: "This help article clarifies the difference between hard bounces and soft bounces."
channel: email
---

# Email bounces

What do you do when the message from your email campaign is bounced back from your users' email addresses? First, let's define and troubleshoot the two types of email bounces: hard bounces and soft bounces. 

## Hard bounces

When an email message hard bounces, the email address is either invalid or does not exist. When this occurs, Braze marks the email address as invalid but does not update the user's [subscription status][1]. At this point, Braze will not attempt to send messages to these email addresses marked as invalid.

## Soft bounces

Soft bounces occur when your recipient's email address is valid or when the email message reaches the recipient's email server, but the message was rejected for a temporary issue. These temporary issues may occur when:
- Your recipient's inbox is full
- The message is too large for your recipient's inbox  
- An email server was down

While soft bounces aren't tracked in your campaign analytics, you can monitor the soft bounces in the **Message Activity Log** tab in the **Developer Console**. 

{% alert note %}
If you are using our [updated navigation]({{site.baseurl}}/navigation), you can find the **Message Activity Log** at **Settings** > **Setup and Testing** > **Message Activity Log**.
{% endalert %}

Here, you can also see the reason for the soft bounces and understand possible discrepancies between the "sends" and "deliveries" for your email campaigns.

To learn more about managing your email subscriptions and campaign, check out [Best practices for email][2].

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on November 16, 2022_

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices