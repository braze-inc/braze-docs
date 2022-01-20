---
nav_title: Segment Personas
article_title: Segment Personas
page_order: 1.3
alias: /partners/segment_personas/

description: "This article outlines the partnership between Braze and Segment, a customer data platform that collects and routes information between sources in your marketing stack."
page_type: partner
search_tag: Partner

---

# Segment Personas

{% include video.html id="RfOHfZ34hYM" align="right" %}

> This article will give an overview of the connection between [Braze and Segment Personas](https://segment.com/docs/destinations/braze/#personas), as well as describe requirements and processes for proper implementation and usage.

The Braze and Segment integration allows you use [Personas](https://segment.com/docs/personas/), Segment's built-in audience builder, to create segments of users based on data you have already collected across various sources. These users will then be assigned [custom attributes](({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/)) that can be used to create Braze segments to use in campaign and Canvas retargeting.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Segment account | A [Segment account](https://app.segment.com/login) is required to take advantage of this partnership. |
| Braze destination | You must have already [set up Braze as a destination]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/) in your Segment integration. | This includes providing the correct Braze data center and REST API key in your [connection settings]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/#connection-settings). |
{: .reset-td-br-1 .reset-td-br-2}

## Computed Traits and Audiences

Computed traits and audiences can be sent to Braze as custom attributes or custom events.
- Traits and audiences sent using the `identify` call will appear in Braze as custom attributes.
- Traits and audiences sent using the `track` call will appear in Braze as custom events.

You can choose which method to use (or choose to use both) when you connect the computed trait to the Braze destination.

### Identify calls

You can send computed traits and audiences to Braze as `identify` calls to create custom attributes in Braze. For example, if you have a Personas computed trait for “Last Product Viewed Item,” that would be named “last_product_viewed_item” in the user’s Braze profile under __Custom Attributes__.

### Track calls

You can send computed traits and audiences to Braze as `track` calls to create custom events in Braze. For example, if a user has a computed trait for “Last Product Viewed Item” and the trait is connected to Braze and configured to send track calls, it will appear on users Braze profiles under __Custom Events__.


## Sync time

Though the default setting for the Braze to Segment Personas connection is `Realtime`, there are some filters that will disqualify the persona from syncing in real-time, including some time-based filters which restrict your audience's size at the time of message send.

## Segment debugger testing

Segment's dashboard provides a "Debugger" feature that allows customers to test whether data from a "Source" is transferring to a "Destination" as expected.

This feature connects to Braze's [users/track endpoint]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint), meaning that it can only be used for identified users (users who already have a user ID for their Braze user profile).

Before you can access and use Segment Personas, you must have already [set up Braze as a destination]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/) your Segment integration, including inputting the correct "Appboy Data Center" and "Braze REST API Key" into your destination [Connection Settings]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/#connection-settings)

This will not work for a side-by-side Braze integration. If you haven't inputted the correct Braze REST API information, then no server data will go through.
