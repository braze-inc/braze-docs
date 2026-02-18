---
nav_title: Flybuy
article_title: Flybuy
alias: /partners/flybuy/
description: "This reference article outlines the partnership between Braze and Flybuy, a location services platform, to add location intelligence to your operations and marketing capabilities."
page_type: partner
search_tag: Partner

---

# Flybuy

> [Flybuy](https://www.flybuy.com/) by Radius Networks is the leading omnichannel location platform leveraging AI-powered technology to optimize speed of service across pickup, delivery, drive-thru, and dine-in. Through its integrated Marketing Suite, Flybuy also enables brands to deliver hyper-targeted, moment-based messages, helping to drive engagement, increase check size, and support broader loyalty initiatives.

_This integration is maintained by Flybuy._

## About the integration

Flybuy delivers rich user-intelligence events into Braze, empowering brands to send hyper-relevant, location-aware messages with the highest level of personalization. When a user generates an event in Flybuy, custom events with rich user attributes are delivered to Braze. These events and attributes can be used to power omnichannel operations and trigger proximity-based messages.

## Prerequisites

The following is required before you enable the integration:

| Requirement | Description |
|---|---|
| Flybuy account | A Flybuy account with at least one project. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

To enable the integration, complete the following steps:

1. In the Flybuy Merchant portal, navigate to the **Project Info** and click **Events Engine**.
2. Click **Add a Destination** and then select **Braze**.
3. Add your Braze API Key and Endpoint, and select the events you want enabled.
4. Click **Finish Setup**.

{% alert important %}
Flybuy maps `loyalty_id` to the Braze `external_id` for logged-in users.
{% endalert %}

## Use cases

- [Pickup](https://www.flybuy.com/flybuypickup), [Delivery](https://www.flybuy.com/flybuydelivery), [Drive-Thru](https://www.flybuy.com/flybuydrivethru)
- [Table Service](https://www.flybuy.com/flybuytableservice)
- [Hotel Mobile Check-In and Ordering](https://www.flybuy.com/industries/hospitality)
- [Marketing Suite](https://www.flybuy.com/flybuy-marketing-suite)

## Event- and attribute-based trigger examples

Custom events and custom attributes can be used to power a variety of personalized experiences.

### Build an audience segment of customers who had a bad pickup experience

For example, target any customer who rated their pickup experience less than 5 stars.

![Segment for bad pickup experience]({% image_buster /assets/img/flybuy/flybuy1.png %})

### Trigger an alert when a customer enters a virtual pickup area

Send a personalized SMS targeting customers without a loyalty account to download the app and create a loyalty account.

![Trigger an alert when a customer enters a virtual pickup area]({% image_buster /assets/img/flybuy/flybuy2.png %})

![Trigger an alert when a customer enters a virtual pickup area message]({% image_buster /assets/img/flybuy/flybuy2a.png %})

### Build an audience segment of customers who had a long wait time

For example, target any customer who had a wait time of over two minutes upon exiting a virtual store premise.

![Build an audience segment of customers who had a long wait time]({% image_buster /assets/img/flybuy/flybuy3.png %})

### Trigger a course correction alert when a customer is headed to the wrong location

Send a push notification to customers when they are headed or have arrived at a location different from where they placed their order.

### Deliver special offers based on trip milestones

For example, send a special offer when a VIP customer arrives at their favorite locations.

### Build an audience segment of customers who were missing items in their order

For example, target any customer who commented that items were missing in their digital order.

For more details on APIs and SDKs, see the [Flybuy Developer Documentation](https://www.radiusnetworks.com/developers/flybuy/#/).