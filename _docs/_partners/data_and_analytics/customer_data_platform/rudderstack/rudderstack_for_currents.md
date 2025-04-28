---
nav_title: RudderStack for Currents
article_title: RudderStack for Currents
description: "This article outlines the partnership between Braze Currents and RudderStack, an open-source customer data infrastructure that offers a seamless Braze integration for your Android, iOS, and web applications."
page_type: partner
tool: Currents
search_tag: Partner

---

# RudderStack for Currents

> [RudderStack](https://www.rudderstack.com/) enables you to collect, transform, and activate your customer data across your stack, leveraging your cloud data warehouse as the central source of truth. This article gives an overview of how to set up a connection between Braze Currents and RudderStack.

The Braze and RudderStack integration allows you to leverage Braze Currents to export your Braze events to RudderStack to drive deeper analytics.

## Prerequisites

| Requirement | Description |
| --- | --- |
| RudderStack account | A [RudderStack account](https://app.rudderstack.com/login) is required to take advantage of this partnership. |
| Braze destination | We suggest having [set up Braze as a destination]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack/#integration) in RudderStack. |
| Currents | To export data back into RudderStack, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Create a data source for Braze within RudderStack

First, you must create a Braze source on the RudderStack web app. Instructions for creating a data source can be found on the [RudderStack](https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/braze-currents/) site.

Once completed, RudderStack will provide a webhook URL, including the write key, which you will need to use in the next step. You can find the webhook URL in the **Settings** tab of your Braze source.

### Step 2: Create Current

In Braze, navigate to **Currents > + Create Current > RudderStack Export**. Provide an integration name, contact email, RudderStack webhook URL (which goes in the key field), and RudderStack region. 

### Step 3: Export events

Next, select the events you would like to export. Lastly, click **Launch Current**

All events sent to RudderStack will include the user’s `external_user_id`. At this time, Braze does not send event data to RudderStack for users who do not have their `external_user_id` set.

## Integration details

Braze supports exporting all data listed in the [Currents event glossaries]({{site.baseurl}}/user_guide/data/braze_currents/) to RudderStack.

The payload structure for exported data is the same as the payload structure for custom HTTP connectors, which can be viewed in the [examples repository for custom HTTP connectors](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).