---
nav_title: Customer behavior and user events
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "This glossary lists the various Customer Behavior and User Events that Braze can track and send to chosen Data Warehouses using Currents."
tool: Currents
search_rank: 7
---

Contact your Braze representative or open a [support ticket]({{site.baseurl}}/braze_support/) if you need access to additional event entitlements. If you can't find what you need on this page, check out our [Message Engagement Events Library]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) or our [Currents sample data examples](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explanation of customer behavior and user event structure and platform values %}

### Event structure

This customer behavior and user events breakdown shows what type of information is generally included in a customer behavior or user event. With a solid understanding of its components, your developers and business intelligence strategy team can use the incoming Currents event data to make data-driven reports and charts, and take advantage of other valuable data metrics.

![Breakdown of a user event showing a purchase event with the listed properties grouped by user-specific properties, behavior-specific properties, and device-specific properties]({% image_buster /assets/img/customer_engagement_event.png %})

Customer behavior and user events are comprised of **user-specific** properties, **behavior-specific** properties, and **device-specific** properties.

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
Storage schemas apply to the flat file event data we send to data warehouse storage partners (such as Google Cloud Storage, Amazon S3, and Microsoft Azure Blob Storage). Some event and destination combinations listed here are not yet generally available. For information on which events are supported by various partners, refer to our list of [available partners]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) and check their respective pages.<br><br>Additionally, note that Currents will drop events with excessively large payloads of greater than 900&nbsp;KB.
{% endalert %}