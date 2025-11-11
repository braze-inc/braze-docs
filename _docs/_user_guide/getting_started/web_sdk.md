---
nav_title: SDK overview
article_title: SDK Overview 
page_order: 9
page_type: reference
description: "This reference article covers the basics of the Braze SDK."
---

# SDK overview 

> The Braze SDK collects session data, identifies users, and records purchases and custom events through your website or app. You can also use the SDK to engage users by sending in-app messages and push notifications directly from the Braze dashboard.

In brief, the Braze SDK:
* Collects and syncs user data into a consolidated user profile
* Captures marketing engagement data and custom data specific to your business
* Powers push notifications, in-app messages, and Content Card messaging channels

## What is an SDK?
A software development kit (SDK) is a set of pre-made tools&mdash;just small blocks of code&mdash;that can be added to digital applications to support new capabilities. The Braze SDK is used to send and get information to and from your app or site. It's designed to provide essential functionality right from the start: creating user profiles, logging custom events, triggering push notifications, etc. 

Because this functionality comes default from Braze, your developers are freed up to focus on your core business. Without an SDK, every Braze client would have to create all the infrastructure and tools for data processing, segmentation logic, delivery options, anonymous user handling, campaign analytics, and a lot more completely from scratch. That would take a lot longer and be way more of a pain than the hour or so it takes to incorporate our SDK.

## Implementation

To incorporate an SDK into your app or site, someone will need to add the SDK's code to the larger overall code base powering that application. This means your Engineering team will be involved, essentially tying our apps together so that information and actions flow between them. But although your developers are involved, the SDK is designed to be lightweight and user-friendly to integrate. 

For the sake of saving you time and ensuring a smooth integration, we recommend you and your Engineering team set up your custom events, custom attributes, and the SDK at the same time. Learn more about the steps that your Marketing and Engineering teams will need to think through together by reading our [implementation article]({{site.baseurl}}/user_guide/getting_started/integration/). 

## Data aggregation

The Braze SDK automatically captures user-level data, giving you key metrics for your app and user base. Group similar apps into a single workspace (for example, iOS and Android versions together) to view collected data across platforms and build a complete picture of user activity. See the article on the [Home page]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/) for more information.

## In-app messaging

Use the SDK to compose and send in-app messages directly. You can choose slideup, modal, or fullscreen messages based on your campaign strategy. For composition details, refer to [creating an in-app message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/).

![Push displayed on a web browser]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## Push notifications

Push notifications are another great option to engage with your users and are especially useful to handle time-sensitive calls to action. Mobile push notifications appear on your users' devices, and web push notifications appear even when your site is not open. For specifics on using push notifications, see our [push notification article]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/).

Users of your website or app need to opt-in to receive push notifications. See [push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) for more details. 

## Segmentation and delivery rules

By default, a campaign containing in-app messages will be sent to all versions of the app in that workspace. For example, the message will send to both web and mobile users. To send an in-app message exclusively to web or mobile, you will need to segment your campaign accordingly, which is supported by default through the Braze SDK. 

You can create a segment of your web users by setting **Apps and websites targeted** to **Users from specific apps**, then select only your website for the **Specific Apps**.

![Segment Details page with web app in focus]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

This will allow you to target users based on their behavior in an intelligent way. If you wanted to target web users to encourage them to download your mobile app, you'd create this segment as your target audience. If you wanted to send a messaging campaign that included a mobile in-app message but not a web message, you would uncheck your website's icon in your segment.

## Supported platforms

Braze provides SDKs for multiple platforms, like Web, Android, and Swift. For the complete list, see the [Braze Developer Guide]({{site.baseurl}}/developer_guide/home).
