---
nav_title: Tealium for Currents
article_title: Tealium for Currents
page_order: 0.5
alias: /partners/tealium_for_currents/
description: "This article outlines the partnership between Braze Currents and Tealium, a customer data platform that collects and routes information between sources in your marketing stack."
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
| Tealium EventStream and/or Tealium AudienceStream | A [Tealium account](https://my.tealiumiq.com/) is required to take advantage of this partnership. |
| Currents | In order to export data back into mParticle, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
| Tealium URL | These can be obtained by navigating to your Tealium dashboard and copying the ingestion URL .|
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Create a Data Source for Braze within Tealium

Instructions for this step are documented [here](https://community.tealiumiq.com/t5/Customer-Data-Hub/Data-Sources/ta-p/17933#toc-hId--270626666). At the end, Tealium will provide a Data Source URL to copy, which you will use in the next step.

### Step 2: Create Current

In Braze, navigate to **Currents > + Create Current > Create Tealium Export**. Provide an integration name,  contact email and the Tealium URL from Step 1. Next, select what you want to track from the list of available events. Lastly, click **Launch Current**

{% alert important %}
It's important to keep your Tealium URL up to date; if your connector's credentials expire, the connector will stop sending events. If this persists for more than **48 hours**, the connector's events will be dropped and data will be permanently lost.
{% endalert %}

All events sent to Tealium will include the user's `external_user_id`. At this time, Braze does not send event data for users who do not have their `external_user_id` set.

## Integration details

All data listed in the [Currents Event Glossaries]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#nav_top_dataandanalytics_brazec urrents_eventglossary), including all fields in both [Message Engagement Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) and [Customer Behavior and User Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/).




