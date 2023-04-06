---
nav_title: Architectural overview
article_title: Getting started&#58; Architectural Overview
page_order: 1
description: ""

---

# Getting started: Architectural overview

> Braze provides a comprehensive user engagement solution for your mobile and web applications. This article is a good place to start if you're just starting with Braze and trying to get a technical overview. Links from this article connect out into a broad overview of essential Braze topics.

The Braze platform, powered by the SDK, the REST API, and partner integrations, allows you to aggregate and act on your data. It does this in the context of something we call our vertically integrated stack. Let's dig into each layer, one at a time.

![Braze has different layers. In total, is comprised of the SDK, the API, and Partner Integrations. These each contribute parts of a data ingestion layer, a classification layer, an orchestration layer, a personalization layer, action layer, and an export layer. The action layer has various channels, including push, in-app messages, connected content, webhook, SMS, and email][1]{: style="display:block;margin:auto;" }

The [Integration overview article][13] covers the components of the Braze platform in more detail. 

## Data ingestion

At a very high level, data is collected and funneled into Braze by the SDK and API. Braze gathers this data from several sources. 

![][14]

1. Backend data sources can feed both historical and asynchronous data to Braze through our REST API.
2. The Braze SDK automatically captures first party data from frontend data sources, such as users' mobile devices.
3. Connected Content allows you to insert any information accessible via API directly into the messages you are sending, such as a push notifications or emails. Connected Content allows you to pull content either directly from your web server or from APIs. Learn more about [Connected Content][8].
4. Braze's partner integrations make it easy to supplement your data feeds through message personalization, orchestration, analytics, and more.
5. Lastly, we have backend messaging services that power your transactional use cases when data lives outside of Braze. 

To get started on pulling your existing data into Braze, see [Historical Data Ingestion][3].

### Customer data platform partners
Our customer data platform (CDP) partners (such as Segment, mParticle or Tealium) are another route you can take to get data into Braze. At a high level, our CDP partners generally alloy you to integrate "side-by-side," where our SDK is deployed alongside theirs, or "server-to-server," where they pass data through our REST API endpoints. In both scenarios, the integration will have some pre-built mapping and functions where an action through your CDP ripples to Braze.

## Classification

The classification layer enables you to dynamically classify and build audiences, called [segments][4], based on data passing through Braze. Build dynamic audiences of users based on the information ingested via Braze SDK, sent from your database through our API, or enriched by any of our partners.

## Orchestration

The orchestration layer allows your Marketing team to design of user journeys based on your user data and prior engagement. Specifically, this is done through creating [campaigns][5] and [Canvases][6]. This work is mostly done through our dashboard interface, but you also have the option to launch [campaigns through the API][7].  

## Personalization

The personalization layer represents Braze’s ability to deliver dynamic content in your messages. By using Liquid, an open-source personalization language, you can not only dynamically pull in existing data to display the message tailored to each recipient, but you can also use conditional logic and make API calls to bring in data from your desired endpoints at the time of send.

## Action

The action layer is the actual sending of your campaigns and Canvas journey steps. The purpose of the action layer is to send the right message to the right user at the right time, based on the data available through all of the layers previously discussed.

### Messaging channels

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eget nunc lobortis mattis aliquam faucibus purus in. Ac turpis egestas sed tempus urna et. Amet risus nullam eget felis eget. Ac tortor dignissim convallis aenean et tortor. Curabitur vitae nunc sed velit dignissim. Euismod in pellentesque massa placerat. Viverra justo nec ultrices dui sapien eget mi.

### Webhooks

Tortor vitae purus faucibus ornare suspendisse sed nisi lacus. Amet mauris commodo quis imperdiet massa. Blandit cursus risus at ultrices mi tempus. Vivamus at augue eget arcu dictum varius. Egestas egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate.

### Transactional endpoints

The action layer is also built to be used with transactional APIs. For example, you can have your backend tell Braze when to send the messages and campaigns your marketers designed in the dashboard, and just trigger them according to your backend logic. An example of transactional API messages might be password resets or shipping confirmations. 

## Export

Finally, throughout the process, Braze has an export layer that allows you to extract through the API, as a CSV report, or by streaming our raw data feed, Currents.

The Braze API provides [endpoints][9] that allow you to programmatically export aggregate campaign, Canvas, and app group level analytics, as well as to export individual user data. This data can be exported for audiences and segments of any size. 

The [CSV option][10] easily allows your team members to export the aggregate level data directly from the dashboard.

{% alert tip %}
While the CSV export has a starting limit of 500,000 rows, the APIs do not have a limit in this regard.
{% endalert %}

[Currents][11] is a granular streaming export that continuously feeds other destinations of your stack. Currents is the per user per event raw data feed that exports data every 5 minutes, or every 15,000 events, whichever comes first. Examples of some downstream destinations for Currents would be Segment, S3, Redshift and Mixpanel, among others. 

## Putting it all together 

As an example of all these layers working together, the SDK's action layer will deliver and display push notifications, in-app messages, and Content Cards. Meanwhile, the SDK is also collecting all of the user engagement data from these messages. Perhaps at the same time, you might also be feeding Braze user data from your servers or partner integrations. All of this data is funneled back into the SDK for future classification. The personalization layer is dynamically customizing these messages with all of this iterative data from the stack, and maybe even fetching data that still lives in your backend or through publicly accessible APIs with Connected Content. 

![Messaging channels such as push notifications and in-app messages are displayed on user's devices, then imported back into the stack through the SDK feedback loop. Currents and export APIs stream data into customer data sources. The customer's backend triggers the action layer through transactional APIs. Connected Content takes data from customer data sources and pulls it into the personalization layer. Partner data sources are imported into the stack as well.][12]

## Data model

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eget nunc lobortis mattis aliquam faucibus purus in. Ac turpis egestas sed tempus urna et. Amet risus nullam eget felis eget. Ac tortor dignissim convallis aenean et tortor. Curabitur vitae nunc sed velit dignissim. Euismod in pellentesque massa placerat. Viverra justo nec ultrices dui sapien eget mi.

### Data upload and download

The Braze SDK caches data (sessions, custom events, etc.) and uploads it periodically. Only after the data has been uploaded will the values be updated on the dashboard. The upload interval takes into account the state of the device and is governed by the quality of the network connection:

|Network Connection Quality |    Data Flush Interval|
|---|---|
|Great    |10 Seconds|
|Good    |30 Seconds|
|Poor    |60 Seconds|
{: .reset-td-br-1 .reset-td-br-2}

If there is no network connection, data is cached locally on the device until the network connection is re-established. When the connection is re-established, the data will be uploaded to Braze.

Braze sends data to the SDK at the beginning of a session based on which segments the user falls into at the time of the session. The new in-app messages will not be updated during the session. However, user data during the session will be continually processed as it is sent from the client. For example, a lapsed user (last used the app more than 7 days ago) will still receive content targeted at lapsed users on their first session back in the app.

### Session length and data flushing

Tortor vitae purus faucibus ornare suspendisse sed nisi lacus. Amet mauris commodo quis imperdiet massa. Blandit cursus risus at ultrices mi tempus. Vivamus at augue eget arcu dictum varius. Egestas egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate.

### Session timeout customization 

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eget nunc lobortis mattis aliquam faucibus purus in. Ac turpis egestas sed tempus urna et. Amet risus nullam eget felis eget. Ac tortor dignissim convallis aenean et tortor. 

#### Manually flushing data 

Amet mauris commodo quis imperdiet massa. Blandit cursus risus at ultrices mi tempus. Vivamus at augue eget arcu dictum varius. Egestas egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate.

## Next steps
Learning to Use Braze 

Architectural overview

Example use cases 

[1]: {% image_buster /assets/img/getting_started/braze-ecosystem.png %}
[2]: {{site.baseurl}}/api/home
[3]: {{site.baseurl}}/developer_guide/getting_started/historical_data
[4]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[5]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/getting_started
[6]: {{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/the_basics/
[7]: {{site.baseurl}}/api/api_campaigns#api-campaigns
[8]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content
[9]: {{site.baseurl}}/api/endpoints/export
[10]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data
[11]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents
[12]: {% image_buster /assets/img/getting_started/braze-ecosystem-in-action.png %}
[13]: {{site.baseurl}}/developer_guide/getting_started/platform_overview/integration_overview
[14]: {% image_buster /assets/img/getting_started/braze-data-layers.png %}