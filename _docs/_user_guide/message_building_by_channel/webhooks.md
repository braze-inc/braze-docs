---
nav_title: Webhooks
article_title: Webhooks
page_order: 4
layout: dev_guide
alias: /about_webhooks/
guide_top_header: "Webhooks"
guide_top_text: "Webhooks are a common way for applications to communicate—to share data in real time. In this day and age, we rarely have one standalone application that can do everything. Most of the time, you're working in many different apps or systems that are specialized to perform certain tasks, and these apps all need to be able to communicate with one another. That's where webhooks come in. <br><br> A webhook is an automated message from one system to another after a certain criteria has been met. In Braze, this criteria is usually the triggering of a custom event. <br><br>At its core, a webhook is an event-based method for two separate systems to take effective action based on data transmitted in real time. That message contains instructions that tells the receiving system when and how to perform a specific task. Because of this, webhooks can provide you with more dynamic and flexible access to data and programmatic functionality, and empower you to set up customer journeys that streamline processes."
description: "This landing page is home to webhooks. Here, you can find articles on creating webhooks, creating webhook templates, and Braze-to-Braze webhooks."
channel:
  - webhooks
search_rank: 3
guide_featured_title: "Section articles"
guide_featured_list:
- name: Creating a Webhook
  link: /docs/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Creating a Webhook Template
  link: /docs/user_guide/message_building_by_channel/webhooks/webhook_template/
  image: /assets/img/braze_icons/table.svg
- name: Braze-to-Braze Webhooks
  link: /docs/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/
  image: /assets/img/braze_icons/switch-horizontal-01.svg
- name: Reporting
  link: /docs/user_guide/message_building_by_channel/webhooks/reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Troubleshooting Webhook Requests 
  link: /docs/help/help_articles/api/webhook_connected_content_errors/
  image: /assets/img/braze_icons/check-square-broken.svg
---

## [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"}Use cases

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
- Endless "If This Then That" ([IFTTT](https://ifttt.com/about)) recipes—for instance, if a customer signs into the app via email, then that address can automatically be configured into Salesforce.

## Anatomy of a webhook

A webhook consists of the following parts.

| Part of Webhook | Description |
| --- | --- |
| [HTTP method](#methods) | Like APIs, webhooks need request methods. These are given to the URL the webhook hits, and tells the endpoint what to do with the information given. There are four HTTP methods you can specify: POST, GET, PUT, and DELETE. |
| HTTP URL | The URL address of your webhook endpoint. The endpoint is the place where you'll be sending the information that you're capturing in the webhook. |
| Request body | This part of the webhook contains the information that you're communicating to the endpoint. The request body can be JSON key-value pairs or raw text. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Example webhook with an HTTP method, HTTP URL, and request body.]({% image_buster /assets/img_archive/webhook_anatomy.png %})

### HTTP methods {#methods}

The following table describes the four different HTTP methods you can specify in your webhook.

| HTTP method | Description |
| ----------- | ----------- |
| POST | This method writes new information on the receiving server. A common example of the POST method in real world application is a [contact form](https://www.braze.com/company/contact) on a website. Whatever information you put into the form becomes part of a request body and is sent to a receiver. This is most common method used when sending data.
| GET | This method retrieves existing information, as opposed to writing new information. By definition, a GET request does not support a request body. This is the most common method used when asking for data from a server. For example, consider the [`/segments/list` endpoint]({{site.baseurl}}/api/endpoints/export/segments/get_segment/). If you were to make a GET request, it would return a list of your segments.
| PUT | This method updates information on the endpoint, replacing any existing information with what's in the request body. 
| DELETE | This method deletes the resource in the HTTP URL. 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Webhooks in Braze

In Braze, you can create a webhook as a webhook campaign, API campaign, or Canvas component.

{% tabs %}
{% tab Webhook Campaign %}

1. In the Braze dashboard, go to **Campaigns**.
2. Click **Create Campaign** and select **Webhook**.

Refer to [Creating a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) for more information.

{% endtab %}
{% tab API Campaign %}

1. In the Braze dashboard, go to **Campaigns**.
2. Click **Create Campaign** and select **API Campaign**.
3. Click **Add Messages** and select **Webhook**.
4. Format your API call to include a [webhook object]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/).

Refer to [Creating a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) for more information.

{% endtab %}
{% tab Canvas Component %}

1. In your Canvas, create a new component.
2. In the **Message** section of your component, select **Webhook**.

Refer to [Creating a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) for more information.

{% endtab %}
{% endtabs %}

## Webhook error handling and rate limiting

When Braze receives an error response from a webhook call, we automatically adjust that webhook's sending behavior based on these response headers:

- `Retry-After`
- `X-Rate-Limit-Limit`
- `X-Rate-Limit-Remaining`
- `X-Rate-Limit-Reset`

These headers help us interpret rate limits and adjust sending speed accordingly to avoid further errors. We also implement an exponential backoff strategy for retries, which helps reduce the risk of overwhelming your servers by spacing out retry attempts over time.

If we detect that the majority of webhook requests to a specific host are failing, we will temporarily defer all send attempts to that host. Then, we will resume sending after a defined cooldown period, allowing your system to recover.


