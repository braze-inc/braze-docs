---
nav_title: Message engagement events
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "This glossary lists the various Message Engagement Events that Braze can track and send to chosen Data Warehouses using Currents."
tool: Currents
search_rank: 6
---

Storage schemas apply to the flat file event data we send to Data Warehouse Storage partners (Google Cloud Storage, Amazon S3, and Microsoft Azure Blob Storage). For schemas that apply to the other partners, refer to our list of [available partners]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) and check their respective pages.

Contact your account manager or open a [support ticket]({{site.baseurl}}/braze_support/) if you need access to additional event entitlements. If you can't find what you need in this article, check out our [Customer Behavior Events Library]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) or our [Currents sample data examples](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explanation of message engagement event structure and platform values %}

### Event structure

This event breakdown shows what type of information is generally included in a message engagement event. With a solid understanding of its components, your developers and business intelligence strategy team can use the incoming Currents event data to make data-driven reports and charts, and take advantage of other valuable data metrics.

![Breakdown of a message engagement event showing an email unsubscribe event with the listed properties grouped by user-specific properties, campaign or Canvas tracking properties, and event-specific properties]({% image_buster /assets/img/message_engagement_event.png %})

Message engagement events are comprised of **user-specific** properties, **campaign/canvas tracking** properties, and **event-specific** properties.

### User ID schema

Note the naming conventions for user IDs.

| Braze schema | Currents schema | Description |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | The unique identifier that is automatically assigned by Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | The unique identifier of a user's profile that is set by the customer. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Platform values

Certain events return a `platform` value that specifies the platform of the user's device.
<br>The following table details the possible returned values:

| User device | Platform value |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% enddetails %}

{% alert important %}
Currents will drop events with excessively large payloads of greater than 900&nbsp;KB.
{% endalert %}

{% alert note %}
Objects related to Canvas Flow have IDs that can be used for grouping and translated to human-readable names through the [Export Canvas details endpoint]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/).
{% endalert %}

{% alert note %}
Certain fields might take longer to display their most recent state after a campaign or Canvas is updated. These fields are:
<ul>
  <li>"campaign_name"</li>
  <li>"canvas_name"</li>
  <li>"canvas_step_name"</li>
  <li>"conversion_behavior"</li>
  <li>"canvas_variation_name"</li>
  <li>"experiment_split_name"</li>
  <li>"message_variation_name"</li>
</ul>
If complete consistency is required, we recommend waiting an hour from the last update to these fields before sending out your messaging to your users.
{% endalert %}