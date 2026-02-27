---
nav_title: Webhooks
article_title: Webhooks
page_order: 9
page_type: landing
alias: /about_webhooks/
description: "Connect your systems with webhooks in Braze, triggered by custom events to send data and programmatic messages to external endpoints."
channel:
  - webhooks
search_rank: 3
---

# Webhooks

> A webhook is an automated message from one system to another after certain criteria are met. In Braze, this criteria is usually the triggering of a custom event. Webhooks provide dynamic and flexible access to data and programmatic functionality, and empower you to set up customer journeys that streamline processes.

## Prerequisites

Webhooks availability depends on your Braze package. Contact your account manager or customer success manager to get started.

## Use cases

Webhooks are an excellent way to connect your systems together—after all, webhooks are how apps communicate. Here are some general scenarios where webhooks can be particularly useful:

- Sending data to and from Braze
- Sending messages to your customers via channels not directly supported by Braze
- Posting to Braze APIs

Some more specific use cases include the following:

- If a user unsubscribes from email, you could have a webhook update your analytics database or CRM with that same information, ensuring a holistic view of that user's behavior.
- Send [transactional messages]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) to users within Facebook Messenger or Line.
- Send direct mail to customers in response to their in-app and web activity by using webhooks to communicate with third-party services like [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/).
- If a gamer reaches a certain level or accrues a certain number of points, use webhooks and your existing API setup to send a character upgrade or coins directly to their account. If you send the webhook as part of a multichannel messaging campaign, you can send a push or other message to let the gamer know about the reward at the same time.
- If you're an airline, you can use webhooks and your existing API setup to credit a customer's account with a discount after they've booked a certain number of flights.
- Endless "If This Then That" ([IFTTT](https://ifttt.com/about)) recipes--for instance, if a customer signs into the app through email, then that address can automatically be configured into Salesforce.

## Webhook error handling and rate limiting

When Braze receives an error response from a webhook call, it automatically adjusts that webhook's sending behavior based on these response headers:

- `Retry-After`
- `X-Rate-Limit-Limit`
- `X-Rate-Limit-Remaining`
- `X-Rate-Limit-Reset`

These headers help Braze interpret rate limits and adjust sending speed accordingly to avoid further errors. Braze also implements an exponential backoff strategy for retries, which helps reduce the risk of overwhelming your servers by spacing out retry attempts over time.

If the majority of webhook requests to a specific host are failing, Braze temporarily defers all send attempts to that host. Sending resumes after a defined cooldown period, allowing your system to recover.

## Next steps

- [Create a webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)
- [Braze-to-Braze webhooks]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook/)
