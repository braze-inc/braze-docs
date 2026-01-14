---
nav_title: Narvar
article_title: Narvar
description: "Learn how to integrate Narvar with Braze."
alias: /partners/narvar/
page_type: partner
search_tag: Partner
---

# Narvar

> Narvar is a post-purchase platform that enhances customer loyalty through order tracking, delivery updates, and returns management. The Braze and Narvar integration enables brands to leverage Narvar’s notification events to trigger messages directly from Braze, keeping customers informed with timely updates.

## Prerequisites

| Requirement           | Description                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|
| Narvar Account        | A Narvar account is required to take advantage of this partnership.                           |
| Braze REST API key    | A Braze REST API key with `messages.send` permission. This can be created in the Braze dashboard from **Settings** > **API Keys**.                                            |
| Braze REST endpoint   | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), which depends on the URL for your Braze instance.         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Supported features

|Type|Supported features|
|-------|----------|
| Notifications | \- Delivery Anticipation<br>\- Carrier Delay<br>\- Delivered Standard |
| Channels | Push Notifications |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
If you’re interested in additional notification types or channels, please contact your Braze and Narvar CSM.
{% endalert %}

## Integration Details

For each notification event, Narvar initiates a request to the Braze [`/messaging/send`]({{site.baseurl}}/api/endpoints/messaging) endpoint to deliver a push message to each opted-in consumer.

Narvar is responsible for configuring the push notification payloads for each message. Currently, Narvar does not have a built-in design interface for push notifications, so their team will collaborate with your team to determine and define payload requirements. These payloads can be customized to the same extent as those sent through your own system, including support for variable content placeholders, such as order data and consumer details.

## Getting Started with the Braze-Narvar Integration

1. **Contact your Narvar CSM** to express interest in the integration.
2. **Designate Braze environments** for staging and production.
3. **Generate API Key** in Braze for Narvar’s use.
4. **Generate Campaign Key(s)** in Braze as needed.
5. **Provide API and Campaign keys** to Narvar through a secure one-time link.
6. **Share Push Notification Payload Details** to finalize setup.
