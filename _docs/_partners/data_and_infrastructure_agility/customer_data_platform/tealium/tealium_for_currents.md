---
nav_title: Tealium for Currents
article_title: Tealium for Currents
page_order: 3
alias: /partners/tealium_for_currents/
description: "This reference article outlines the partnership between Braze Currents and Tealium, a customer data platform that collects and routes information between sources in your marketing stack."
page_type: partner
tool: Currents
search_tag: Partner

---

# Tealium for Currents

> [Tealium](https://www.tealium.com) is a customer data platform that collects and routes information from multiple sources to a variety of other locations in your marketing stack.

The Braze and Tealium integration allows you to seamlessly control the flow of information between the two systems. With Currents, you can also connect data to Tealium to make it actionable across the entire growth stack. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Tealium EventStream or Tealium AudienceStream | A [Tealium account](https://my.tealiumiq.com/) is required to take advantage of this partnership. |
| Currents | In order to export data back into Tealium, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
| Tealium URL | These can be obtained by navigating to your Tealium dashboard and copying the ingestion URL.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Create a data source for Braze within Tealium

Instructions for creating a data source can be found on the [Tealium](https://docs.tealium.com/server-side/data-sources/webhooks/braze-currents/) site. When completed, Tealium will provide a data source URL to copy, which you will use in the next step.

### Step 2: Create Current

In Braze, navigate to **Currents > + Create Current > Tealium Export**. Provide an integration name, contact email, and your Tealium URL. Next, select what you want to track from the list of available events. Lastly, click **Launch Current**

All events sent to Tealium will include the user's `external_user_id`. At this time, Braze does not send event data to Tealium for users who do not have their `external_user_id` set.

{% alert important %}
It's important to keep your Tealium URL up to date. If your connector's URL is incorrect, Braze will be unable to send events. If this persists for more than **48 hours**, the connector's events will be dropped, and data will be permanently lost.
{% endalert %}

## Integration details

Braze supports exporting all data listed in the [Currents event glossaries]({{site.baseurl}}/user_guide/data/braze_currents/) (including all properties in both [message engagement]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) and [customer behavior]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) events) to Tealium.

The payload structure for exported data is the same as the payload structure for custom HTTP connectors, which can be viewed in the [examples repository for custom HTTP connectors](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).