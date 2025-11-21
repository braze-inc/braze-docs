---
nav_title: Architectural overview
article_title: Architectural Overview
page_order: 3
description: "This article discusses the different parts and pieces of the Braze technology stack, with links to relevant articles."
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# Getting started: Architectural overview

> This article discusses the different parts and pieces of the Braze technology stack, with links to relevant articles. 

At a high level, Braze is about data. The Braze platform, powered by the SDK, the REST API, and partner integrations, allows you to aggregate and act on your data. 

![Braze has different layers. In total, it consists of the SDK, the API, the dashboard, and partner integrations. These each contribute parts of a data ingestion layer, a classification layer, an orchestration layer, a personalization layer, and an action layer. The action layer has various channels, including push, in-app messages, Connected Catalog, webhook, SMS, and email.]({% image_buster /assets/img/getting-started/braze_listen_understand_act.png %}){: style="display:block;margin:auto;" }

* [Data ingestion](#ingestion): Braze pulls in data from a variety of sources.
* [Classification](#classification): Your marketing team dynamically segments your user base using these metrics. 
* [Orchestration](#orchestration): Braze intelligently coordinates messages to different audience segments at the ideal time.
* [Action](#action): Your marketing team acts on the data, creating content through a variety of messaging channels such as SMS and email.
* [Personalization](#personalization): The data is transformed in real time with personalized information about your audience. 
* [Export](#exporting-data): Then, Braze tracks your users' engagement with this messaging and feeds it back into the platform, creating a loop. You get insights into this data through real-time reports and analytics.

This all works together to create successful interactions between your user base and your brand so that you can achieve your goals. Braze does all this in the context of something we call our vertically integrated stack. Let's dig into each layer, one at a time.

## Data ingestion {#ingestion}

Braze is built on a streaming data architecture leveraging Snowflake, Kafka, MongoDB, and Redis. Data from many sources can be loaded into Braze via SDK and API. The platform can handle any data in real time, regardless of how it’s nested or structured. Data in Braze is stored on the user profile. 

{% alert tip %}
Braze can track data for a user throughout their journey with you, from the time that they're anonymous to the time they're logged in to your app and known. User IDs, called `external_id`s in Braze, should be set for each of your users. These should be unchanging and accessible when a user opens the app, allowing you to track your users across devices and platforms. See the [User lifecycle article]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) for best practices.
{% endalert %}

![Braze imports backend data sources from the API, frontend data sources from the SDK, data warehouse data from Braze Cloud Data Ingestion, and from partner integrations. This data is exported through the Braze API ]({% image_buster /assets/img/getting-started/import-export.png %}){: style="display:block;margin:auto;" }

{% alert note %}
This person-centric user profile database allows for real-time, interactive speed. Braze pre-computes values when data arrives and stores the results in our lightweight document format for fast retrieval. And because the platform was designed this way from the ground up, it is ideal for most messaging use cases—especially combined with other data concepts like Connected Content, product catalogs, and nested attributes. 
{% endalert %}

### Backend data sources via the Braze API
Braze can pull data from user databases, offline transactions, and data warehouses through our [REST API]({{site.baseurl}}/api/endpoints/user_data). 

### Frontend data sources via Braze SDK
Braze automatically captures first-party data from frontend data sources, such as users' devices, by way of the [Braze SDK]({{site.baseurl}}/user_guide/getting_started/web_sdk/). The SDK handles new (anonymous) users and manages data on their user profile throughout their lifecycle. 

### Partner integrations
Braze has over 150 technology partners, which we call "Alloys." You can supplement your data feeds through a meaningfully robust network of [interoperable technologies and data APIs.]({{site.baseurl}}/partners/home) 

### Direct warehouse connection via Braze Cloud Data Ingestion
You can stream customer data from your data warehouse into the platform through [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/) in just a few minutes, allowing you to sync relevant user attributes, events, and purchases. The Cloud Data Ingestion integration supports complex data structures including nested JSON and arrays of objects.

Cloud Data Ingestion can sync data from Snowflake, Amazon Redshift, Databricks, and Google BigQuery.

## Classification {#classification}
The classification layer enables your team to dynamically classify and build audiences, called [segments]({{site.baseurl}}/user_guide/engagement_tools/segments), based on data passing through Braze. 

{% alert note %}
The classification, orchestration, and personalization layers are where your marketing team will do much of their work. They interface with these layers most often through the Braze dashboard, our web interface. Developers have a role in setting up and customizing these layers.
{% endalert %}

Many common types of user attributes, such as name, email, date of birth, country, and others are automatically tracked by the SDK by default. As a developer, you'll work with your team to define what additional, custom data makes sense to track for your use case. Your custom data will impact how your user base will be classified and segmented. You will set this data model up during the implementation process. 

Learn more about [automatically collected data and custom data]({{site.baseurl}}/developer_guide/analytics/).

## Orchestration {#orchestration}
The orchestration layer allows your marketing team to design user journeys based on your user data and prior engagement. This work is mostly done through our dashboard interface, but you also have the option to launch [campaigns through the API]({{site.baseurl}}/api/api_campaigns#api-campaigns). For example, you can have your backend tell Braze when to send the messages and campaigns your marketers designed in the dashboard, and trigger them according to your backend logic. An example of an API-triggered message might be password resets or shipping confirmations. 

{% alert note %}
API-triggered campaigns are ideal for more advanced transactional use-cases. They allow marketers to manage campaign copy, multivariate testing, and re-eligibility rules within the Braze dashboard while triggering the delivery of that content from your servers and systems. The API request to trigger the message can also include additional data to be templated into the message in real-time. 
{% endalert %}


### Feature flags
Braze allows you to remotely enable or disable functionality for a selection of users through [feature flags]({{site.baseurl}}/developer_guide/feature_flags/). This lets your marketers target the correct segment of your user base with messaging for features you haven't yet rolled out to your entire audience. But more than that, feature flags can be used to turn a feature on and off in production without additional code deployment or app store updates. This allows you to safely roll out new features with confidence.

## Personalization {#personalization}
The personalization layer represents the ability to deliver dynamic content in your messages. By using Liquid, a widely-used personalization language, your team can dynamically pull in existing data to display the message tailored to each recipient. Additionally, you can insert any information accessible on your webserver or via API directly into the messages you're sending, such as push notifications or emails, by using [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content). Connected Content builds on top of Liquid and uses familiar syntax.

And because this dynamic content is programmable, marketers can include computed values, responses from other calls, or product catalog items. After you've set these systems up during implementation, your marketing team can do this with little to no support from technical teams. 

## Action {#action}
The action layer enables your actual messaging to your users. The purpose of the action layer is to send the right message to the right user at the right time, based on the data available through all of the layers previously discussed. Messaging is done inside your app or site (such as sending in-app messages or through graphic elements like Content Card carousels and banners) or outside your app experience (such as sending push notifications or emails).

### Messaging channels
Braze was designed to handle an evolving technological landscape with its channel-agnostic, user-centric data model. The dashboard manages message delivery and transactional triggers. For example, your marketers can trigger an SMS message offering a coupon for one of your newly-opened storefronts when a user enters the geofence set near this location, or send a user an email to let them know their favorite show has a new season.

The [Braze SDK]({{site.baseurl}}/user_guide/getting_started/web_sdk/) powers additional messaging channels: push, in-app messages, and Content Cards. You integrate the SDK with your app or site to allow your marketing team to use the Braze dashboard to coordinate their campaigns across all supported messaging channels.

![]({% image_buster /assets/img/getting_started/channels.png %})

## Exporting data
Critically, all end-user interactions with Braze are tracked so you can measure your engagement and outreach. And after Braze has aggregated your data from all these sources, it can be exported back to your tech stack using a variety of tools, closing the loop.

### Currents
[Currents]({{site.baseurl}}/user_guide/data/braze_currents/) is an optional Braze add-on that provides a granular streaming export that continuously feeds other destinations of your stack. Currents is a per user per event raw data feed that exports data every five minutes, or every 15,000 events, whichever comes first. Examples of some downstream destinations for Currents would be Segment, S3, Redshift and Mixpanel, among others. 

### Snowflake data sharing
Snowflake’s [Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) functionality allows Braze to give you secure access to data on our Snowflake portal without worrying about workflow friction, failure points, and unnecessary costs that come with typical data provider relationships. All sharing is accomplished through Snowflake’s unique services layer and metadata store: no data is actually copied or transferred between accounts. This is an important concept because shared data does not take up any storage in a consumer account and, therefore, does not contribute to your monthly data storage charges. The only charges to consumers are for the computing resources (that is, virtual warehouses) used to query the shared data.

### Braze export APIs
The Braze API provides [endpoints]({{site.baseurl}}/api/endpoints/export) that allow you to programmatically export aggregate analytics, as well as to export individual user data. This data can be exported for audiences and segments of any size. 

### CSVs
Lastly, there is an option to download your aggregate-level data directly from the dashboard as a [CSV]({{site.baseurl}}/user_guide/data/export_braze_data/). The CSV option easily allows your team members to export data from Braze.

{% alert tip %}
While the CSV export has a base limit of 500,000 rows, the APIs do not have a limit in this regard.
{% endalert %}

## Putting it all together 
One of your users, let's call them Mel, just received your product announcement. Behind the scenes, all of the layers of the Braze platform worked together to make sure this process went smoothly. 

Mel's information was pulled into Braze from your legacy customer engagement platform through a CSV import. Every time Mel interacted with your app after integration, more data was added to her customer profile. 

Your product announcement was sent to all customers who liked a similar item in your app. You defined this data as a custom event. The SDK tracked this event and segmented your user base accordingly. Braze orchestrated the best time of day to send this announcement, and personalized the announcement by calling Mel by her preferred name. 

When Mel opens the announcement, she adds your new product to her wishlist. Braze tracks that she clicked the email automatically. The SDK tracks that she's wishlisted your new product. Each time they engage with your brand, you and your users are learning more about each other.

![]({% image_buster /assets/img/getting-started/putting-it-all-together.png %})



