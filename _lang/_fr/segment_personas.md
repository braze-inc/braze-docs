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

> This article will give an overview of [the connection between Braze and Segment Personas](https://segment.com/docs/destinations/braze/#personas), as well as describe requirements and process for proper implementation and usage.

If you're looking for information on the Currents integration with Segment, refer to [Segment for Currents]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/). If you're looking for our regular integration (side-by-side or server-to-server) with Segment, refer to [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/).

## About Segment Personas

[Personas](https://segment.com/docs/personas/) is Segment's built-in audience builder. You can go to your Segment Dashboard and create segments of users based on data you have already collected across various sources.

From there, these segments will be assigned a [custom attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) in a Braze user profile (only for users who already have user IDs) that designates whether they fall into a certain audience or not.

## Requirements

Before you can access and use Segment Personas, you must have already [set up Braze as a destination]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/) your Segment integration, including inputting the correct "Appboy Data Center" and "Braze REST API Key" into your destination [Connection Settings]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/#connection-settings).

## Sync time

Though the default setting for the Braze to Segment Personas connection is `Realtime`, there are some filters that will disqualify the persona from syncing in real-time, including some time-based filters which restrict your audience's size at the time of message send.

## Segment debugger testing

Segment's dashboard provides a "Debugger" feature that allows customers to test whether data from a "Source" is transferring to a "Destination" as expected.

This feature connects to Braze's [users/track endpoint]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint), meaning that it can only be used for identified users (users who already have a user ID for their Braze user profile).

Before you can access and use Segment Personas, you must have already [set up Braze as a destination]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/) your Segment integration, including inputting the correct "Appboy Data Center" and "Braze REST API Key" into your destination [Connection Settings]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/#connection-settings)


This will not work for a side-by-side Braze integration. If you haven't inputted the correct Braze REST API information, then no server data will go through.
