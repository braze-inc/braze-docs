---
nav_title: Integration Overview
article_title: Getting started&#58; Integration Overview
page_order: 3
description: ""

---

# Getting started: Integration overview

> Before you begin to integrate the Braze, you may find yourself wondering what exactly you're building and integrating. You may be curious about how you can customize Braze to further to meet your needs. This article can help you answer all of your SDK questions. You can also check out our [Technical Integration Checklists and Toolkits](https://learning.braze.com/technical-integration-checklists-and-toolkits) course on Braze Learning.

The Braze platform has three primary components in its logic layer: the SDK, and API, and partner integrations. Its presentation layer consists of a UI component called the [dashboard](#dashboard) that marketers and admins use to do their jobs.

The [Braze SDK](#sdk) helps collect and sync user data across platforms to a consolidated user profile. The SDK automatically collects session data, device info and push tokens. The SDK is also responsible for tracking the engagement analytics (for example, clicking a push notification), and perhaps most importantly, it’s also responsible for ingesting your custom data, such as custom attributes and high-value events that are specific to your business and industry.

The SDK is key not only for data ingestion, but it also displays and handles messaging channels like in-app messages, push notifications, and Content Cards your marketers create in the dashboard.

The [REST API](#rest-api) supplements the SDK by providing additional functionality. With the API you can sync offline high-value information like orders, coupons, or other data happening outside of your app, as well as maintain email opt-in/opt-out and tons of other data. 

Lastly, Braze has [50+ technology partnership integrations](#partner-ecosystem), or "alloys" as we call them. Braze makes it easy to sync data from our partner integrations to your systems, providing your marketing team with attribution functionality, data augmentation, and audience insights. 

## Dashboard user interface

The Braze dashboard is the UI component that gives access to all of the analytics and interactions at the heart of the Braze platform. This website displays graphs that are updated in real-time based upon a mix of [automatic and custom data you configure][2]. Marketers use the site to manage notifications, setup targeted messaging campaigns, and view analytics. Developers can use the dashboard to manage settings for integrating apps, such as API keys and push notification credentials.

## SDK

The Braze SDKs can be integrated into your mobile and web applications to provide powerful marketing, customer support, and analytics tools.

In brief, the Braze SDK:
* Automatically collects session data, device info, and push tokens
* Captures user data and custom data specific to your business into a consolidated user profile
* Powers push notifications, in-app messages, and Content Card messaging channels

### Integration  

The Braze SDK is designed to be very well-behaved, and not interfere with other SDKs present in your app. The Braze SDKs have a very small footprint. We automatically change the rate that we flush user data depending on the quality of the network, in addition to allowing manual network control. We automatically batch API requests from the SDK to make sure that data is logged quickly while maintaining maximum network efficiency. Lastly, the amount of data sent from the client to Braze within each API call is extremely small.

Our [integration guides][4] provide a step-by-step process for integrating the SDK with many different platforms.

#### Default analytics and session handling

Certain user data is collected automatically by our SDK&mdash;for example, First Used App, Last Used App, Total Session Count, Device OS, etc. If you follow our integration guides to implement our SDKs, you will be able to take advantage of this [default data collection][1]. 

{% alert note %}
All of our features are configurable, but we recommend fully implementing the default data collection model and not limiting the collection of data.
{% endalert %}

#### Messaging channels

The SDK powers Braze's messaging tools, allowing for multichannel communication with your users. Your marketing team will use these messaging channels to re-engage lost users, retain active users, and energize your brand ambassadors. 

![The push message editor displaying an example push message and title to be sent to the Android, iOS, and Web messaging channels.][5]

#### Data upload and download

The Braze SDK caches data (sessions, custom events, etc.) and uploads it periodically. Only after the data has been uploaded will the values be updated on the dashboard. The upload interval takes into account the state of the device and is governed by the quality of the network connection:

|Network Connection Quality |    Data Flush Interval|
|---|---|
|Great    |10 Seconds|
|Good    |30 Seconds|
|Poor    |60 Seconds|
{: .reset-td-br-1 .reset-td-br-2}

If there is no network connection, data is cached locally on the device until the network connection is re-established. When the connection is re-established, the data will be uploaded to Braze.

Braze sends data to the SDK at the beginning of a session based on which segments the user falls into at the time of the session. The new in-app messages will not be updated during the session. However, user data during the session will be continually processed as it is sent from the client. For example, a lapsed user (last used the app more than 7 days ago) will still receive content targeted at lapsed users on their first session back in the app.

### Customization
Channel-specific links

#### Crawl

#### Walk

#### Run



## REST API

We have tons of purpose-built endpoints, as well as sample requests and responses in our [documentation][3].

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


[1]: {{site.baseurl}}/developer_guide/getting_started/platform_overview/data_overview#automatically-collected-data 
[2]: {{site.baseurl}}/developer_guide/getting_started/platform_overview/data_overview
[3]: API
[4]: {{site.baseurl}}/developer_guide/home
[5]: {% image_buster /assets/img_archive/UOiOSPush.png %} "Example Push dashboard"