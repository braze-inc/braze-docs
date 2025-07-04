---
nav_title: SDK Overview 
article_title: SDK Overview 
page_order: 9
page_type: reference
description: "This reference article covers the basics of the Braze SDK."
---

# SDK overview 

> The Braze SDK makes it easy to collect session data, identify users, and record purchases and custom events through your website or app. You can also use the SDK to engage with your users by sending in-app messages and push notifications directly from the Braze dashboard.

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

The Braze SDK automatically captures immense amounts of data at the user level, making it easy to see key metrics for your app and user base. You will group similar apps into a single workspace on your dashboard. For example, you will group the iOS and Android versions of your app into the same workspace, allowing you to see the collected data from users across both platforms. This gives you a more complete view of your users across web and mobile channels. See the article on the [Home page]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/) for more information.

## In-app messaging

The SDK makes it easy to compose and send in-app messages to engage with users directly. You can choose to send slideup, modal, or fullscreen messages based on your campaign strategy. For more information on composing an in-app message, see our page on [creating an in-app message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/).

![Push displayed on a web browser]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## Push notifications

Push notifications are another great option to engage with your users and are especially useful to handle time-sensitive calls to action. Mobile push notifications appear on your users' devices, and web push notifications appear even when your site is not open. For specifics on using push notifications, see our [push notification article]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/).

Users of your website or app need to opt-in to receive push notifications. See [push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) for more details. 

## Segmentation and delivery rules

By default, a campaign containing in-app messages will be sent to all versions of the app in that workspace. For example, the message will send to both web and mobile users. To send an in-app message exclusively to web or mobile, you will need to segment your campaign accordingly, which is supported by default through the Braze SDK. 

You can create a segment of your web users by setting **Apps and websites targeted** to **Users from specific apps**, then select only your website for the **Specific Apps**.

![Segment Details page with web app in focus]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

This will allow you to target users based on their behavior in an intelligent way. If you wanted to target web users to encourage them to download your mobile app, you'd create this segment as your target audience. If you wanted to send a messaging campaign that included a mobile in-app message but not a web message, you would uncheck your website's icon in your segment.

## What integrations does Braze have?
Braze offers a version of our SDK for many platforms (web, Android, iOS, Flutter, React Native, and more), but they all operate essentially the same way. So, if you see a reference to, say, the "Web SDK," it's just the version of the Braze SDK intended for your website.

<style>
table th:nth-child(1) {
width: 33%;
}
table th:nth-child(2) {
width: 33%;
}
table th:nth-child(3) {
width: 33%;
}
table td {
word-break: break-word;
text-align: center;
}
</style>
Featured integrations   | &nbsp;  |  &nbsp;
----------- |---------------- | --------------------
[![Android]({% image_buster /assets/img/braze_icons/android.svg %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) |[![iOS]({% image_buster /assets/img/braze_icons/apple.svg %})]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift){: style="max-width:20%;margin-right:15px;border:0" class="noimgborder"} [iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) |[![Web]({% image_buster /assets/img/braze_icons/globe-02.png %})]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web){: style="max-width:25%;margin-right:15px;border:0" class="noimgborder"} [Web]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)  

All integrations   | &nbsp;  |  &nbsp;
----------- |---------------- | --------------------
[![Cordova Android]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=android){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=android) | [![Cordova iOS]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=ios){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=ios) | [![Flutter Android and iOS]({% image_buster /assets/img/flutter_icon.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=flutter){: style="max-width:20%;margin-top:5%;border:0" class="noimgborder"}  [Flutter Android and iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=flutter)
[![React Native]({% image_buster /assets/img/reactnative_icon.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [React Native]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native) | [![tvOS]({% image_buster /assets/img/tvos_icon.png %})]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/tvos/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [tvOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/tvos/initial_sdk_setup/) | [![MacOS]({% image_buster /assets/img/macOS_icon.png %})]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/macOS/initial_sdk_setup/){: style="max-width:40%;margin-top:15%;border:0" class="noimgborder"}  [MacOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/macOS/initial_sdk_setup/)
[![Unity Android]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity) | [![Unity iOS]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity) | [![Xamarin]({% image_buster /assets/img/xamarin.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=xamarin){: style="max-width:35%;margin-top:5%;border:0" class="noimgborder"}  [Xamarin]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=xamarin) 
[![Roku]({% image_buster /assets/img/roku.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=roku){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [Roku]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=roku) | [![Unreal Engine]({% image_buster /assets/img/unreal.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unreal%20engine){: style="max-width:30%;margin-right:15px;border:0" class="noimgborder"}  [Unreal Engine]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unreal%20engine)

