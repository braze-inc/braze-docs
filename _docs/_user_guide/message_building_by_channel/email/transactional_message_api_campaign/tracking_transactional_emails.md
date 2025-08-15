---
nav_title: Tracking transactional emails
article_title: Tracking Transactional Emails
page_order: 1
description: "This reference article covers how to set up real-time tracking for transactional email campaigns."
page_type: reference
tool:
  - Campaigns
channel: email

---

# Tracking transactional emails

> This page describes how to set up real-time tracking for [transactional email campaigns]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/). For more information about the endpoint itself, refer to [Send transactional emails using API-triggered delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/).

When you send transactional emails—like order confirmations or password resets—it’s essential to know whether they reach your customers. With Braze transactional HTTP event postbacks, you’ll get real-time insights into the status of every transactional email, so you can act quickly if there’s an issue.

Use this feature to:

- **Monitor your emails in real-time:** Immediately see if messages are sent, processed, delivered, or encounter issues.
- **Respond proactively:** Retry messages, switch to another channel like SMS, or use fallback systems to make sure your communications are delivered.

## Tracking your transactional emails

{% multi_lang_include http_event_postback.md %}


