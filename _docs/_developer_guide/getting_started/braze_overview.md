---
nav_title: Braze Overview
article_title: Braze Overview
page_order: 1
description: ""

---

# Braze overview

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eget nunc lobortis mattis aliquam faucibus purus in. Ac turpis egestas sed tempus urna et. Amet risus nullam eget felis eget. 

At a very high level, Braze aggregates and allows you to act on your data. 

## Braze in your ecosystem

Braze works in the context of something we call our vertically integrated stack. This idea reflects how data gets into Braze, is transformed, and ultimately acted on through our various channels.

![Braze has different layers. In total, is comprised of the SDK, the API, and Partner Integrations. These each contribute parts of a data ingestion layer, a classification layer, an orchestration layer, a personalization layer, action layer, and an export layer. The action layer has various channels, including push, in-app messages, connected content, webhook, SMS, and email][1]

The [Braze SDK](#sdk) helps collect and sync user data across platforms to a consolidated user profile. The SDK automatically collects session data, device info and push tokens. The SDK is also responsible for tracking the engagement analytics (for example, clicking a push notification), and perhaps most importantly, it’s also responsible for ingesting your custom data, such as custom attributes and high-value events that are specific to your business and industry.

The SDK is key not only for data ingestion, but it’s also responsible for the action layer. It displays and handles messaging channels like in-app messages, push notifications, and Content Cards your marketers create in the dashboard.

The [REST API](#rest-api) supplements the SDK by providing additional functionality. With the API you can sync offline high-value information like orders, coupons, or other data happening outside of your app, as well as maintain email opt-in/opt-out and tons of other data. 

Lastly, Braze has [50+ technology partnership integrations](#partner-ecosystem), or "alloys" as we call them. Braze makes it easy to sync data from our partner integrations to your systems, providing your marketing team with attribution functionality, data augmentation, and audience insights. 

Let's dig into each layer, one at a time.

### Data ingestion

Our customer data platform (CDP) partners (such as Segment, mParticle or Tealium) are another route you can take to get data into Braze. At a high level, our CDP partners generally alloy you to integrate "side-by-side," where our SDK is deployed alongside theirs, or "server-to-server," where they pass data through our REST API endpoints. In both scenarios, the integration will have some pre-built mapping and functions where an action through your CDP ripples to Braze.

To get started on pulling your existing data into Braze, see [Historical Data Ingestion][3].

### Classification

The classification layer enables you to dynamically classify and build audiences, called [segments][4], based on data passing through Braze. Build dynamic audiences of users based on the information ingested via Braze SDK, sent from your database through our API, or enriched by any of our partners.

### Orchestration

The orchestration layer allows your Marketing team to design of user journeys based on your user data and prior engagement. Specifically, this is done through creating [campaigns][5] and [Canvases][6]. This work is mostly done through our dashboard interface, but you also have the option to launch [campaigns through the API][7].  

### Personalization

The personalization layer represents Braze’s ability to deliver dynamic content in your messages. By using Liquid, an open-source personalization language, you can not only dynamically pull in existing data to display the message tailored to each recipient, but you can also use conditional logic and make API calls to bring in data from your desired endpoints at the time of send.

#### Connected Content

An important part of the personalization layer is called Connected Content. Connected Content allows you to insert any information accessible via API directly into the messages you are sending, for example a push notification, or an email. Connected Content allows for pulling content either directly from your web server, or from publicly or privately accessible APIs (for example, contextualizing a push notification based on the current weather). Learn more about [Connected Content][8].

{% alert tip %}
The data you bring in with Connected Content will not cost you any data points, but it will also not be saved on the user’s profile. See the [data](#data) section for basics about managing these factors.
{% endalert %}

### Action

The action layer is the actual sending of your campaigns and Canvas journey steps. The purpose of the action layer is to send the right message to the right user at the right time, based on the data available through all of the layers previously discussed.

#### Messaging channels

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eget nunc lobortis mattis aliquam faucibus purus in. Ac turpis egestas sed tempus urna et. Amet risus nullam eget felis eget. Ac tortor dignissim convallis aenean et tortor. Curabitur vitae nunc sed velit dignissim. Euismod in pellentesque massa placerat. Viverra justo nec ultrices dui sapien eget mi.

#### Webhooks

Tortor vitae purus faucibus ornare suspendisse sed nisi lacus. Amet mauris commodo quis imperdiet massa. Blandit cursus risus at ultrices mi tempus. Vivamus at augue eget arcu dictum varius. Egestas egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate.

#### Transactional endpoints

The action layer is also built to be used with transactional APIs. For example, you can have your backend tell Braze when to send the messages and campaigns your marketers designed in the dashboard, and just trigger them according to your backend logic. An example of transactional API messages might be password resets or shipping confirmations. 

### Export

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

## Data

### Types of data

* 

### User profile

### Data points

## SDK

### Integration

### Customization

## REST API

We have tons of purpose-built endpoints, as well as sample requests and responses in our [documentation][2].

### Endpoints

### Objects

### Postman

### Important considerations
Rate limiting
Send requests in bulk when possible
Add the x-braze-bulk header to bulk uploads
Allow for latency when exporting
Incorporate retry logic
Make use of threaded requests
Restrict user data uploads to delta values only

## Partner Ecosystem

## QA resources

### Test toolkit

### Braze's Production Readiness Assessment

### Event User Log

## Next steps
Integration article in User Guide
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