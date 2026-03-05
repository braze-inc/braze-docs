---
nav_title: Transactional email
article_title: Transactional email
page_order: 4
page_type: landing
channel:
  - email
search_rank: 3
description: "Send transactional emails for critical, time-sensitive notifications triggered by API calls in Braze."
---

# Transactional email

> Transactional emails are purpose-built for sending automated, non-promotional messages to facilitate an agreed-upon transaction between you and your customers. Use transactional email campaigns in Braze to send critical, time-sensitive notifications triggered by API calls, such as order confirmations, password resets, and shipping updates.

## Prerequisites

Transactional email is only available as part of select Braze packages. Contact your Braze customer success manager or open a [support ticket]({{site.baseurl}}/braze_support/) for more details.

Before you start, make sure you have the following:

- Completed [email setup]({{site.baseurl}}/user_guide/channels/email/email_setup/), including IP and domain configuration, authentication, and IP warming
- A **Braze REST API key** with the `transactional.send` permission

## Use cases

Transactional email is designed for sending non-promotional, service-triggered messages. Common use cases include the following:

| Use case | Explanation |
| --- | --- |
| Order confirmations | Confirm that a customer's purchase has been received and is being processed. |
| Password resets | Deliver secure, time-sensitive links for customers to reset their account credentials. |
| Shipping notifications | Notify customers when their order has shipped, including tracking information and estimated delivery dates. |
| Account alerts | Send critical account-related notifications, such as payment failures, subscription changes, or security alerts. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## How transactional email differs from marketing email

Transactional emails are sent through a dedicated Braze [transactional HTTP API]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/), which is optimized for speed and reliability. Unlike marketing emails, transactional emails:

- Don't require a user to be opted in to marketing communications
- Are triggered by API calls rather than scheduled or action-based triggers
- Support near-real-time delivery for time-sensitive content

## Next steps

- [Create a transactional email]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email/)
- [Tracking]({{site.baseurl}}/user_guide/channels/transactional_email/tracking/)
