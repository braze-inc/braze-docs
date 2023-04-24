---
nav_title: SDK Overview for Marketers
article_title: SDK Overview for Marketers
page_order: 3
page_type: reference
description: "This onboarding reference article covers the basics of the Braze SDK."

---

# SDK overview for marketers

The Braze SDK makes it easy to collect session data, identify users, and record purchases and custom events through your website or app. You can also use the SDK to engage with your users by sending in-app messages and push notifications directly from the Braze dashboard.

Are you a developer looking for a technical rundown of the SDK? Check out our [developer overview][1], instead.

In brief, the Braze SDK:
* Collects and syncs user data into a consolidated user profile
* Captures marketing engagement data and custom data specific to your business
* Powers push notifications, in-app messages, and Content Card messaging channels

More on this functionality below.

## What is an SDK?
A software development kit (SDK) is a set of pre-made tools&mdash;just small blocks of code&mdash;that can be added to digital applications to support new capabilities. The Braze SDK is used to send and get information to and from your app or site. It's designed to provide essential functionality right from the start: creating user profiles, logging custom events, triggering push notifications, etc. 

Because this functionality comes default from Braze, your developers are freed up to focus on your core business. Without an SDK, every Braze client would have to create all the infrastructure and tools for data processing, segmentation logic, delivery options, anonymous user handling, campaign analytics, and a lot more completely from scratch. That would take a lot longer and be way more of a pain than the hour or so it takes to incorporate our SDK.

## Implementation

To incorporate an SDK into your app or site, someone will need to add the SDK's code into the larger overall code base powering that application. This means your Engineering team will be involved, essentially tying our apps together so that information and actions flow between them. But although your developers are involved, the SDK is designed to be light-weight and user-friendly to integrate. 

For the sake of saving you time and ensuring a smooth integration, we recommend you and your Engineering team set up your custom events, custom attributes, and the SDK at the same time. Learn more about the steps that your Marketing and Engineering teams will need to think through together by reading our [implementation article][4]. 

## Data aggregation

The Braze SDK automatically captures immense amounts of data at the user level, making it easy to see key metrics for your app and user base. You will group similar apps into a single app group on your dashboard. For example, you will group the iOS and Android versions of your app into the same app group, allowing you to see the collected data from users across both platforms. This gives you a more complete view of your users across web and mobile channels. See the article on the [Overview page][3] for more information.

## In-app messaging

The SDK makes it easy to compose and send in-app messages to directly engage with users. You can choose to send slideup, modal, or full-screen messages based on your campaign strategy. For more information on composing an in-app message, see our page on [creating an in-app message][8].

## Push notifications

![Push displayed on a web browser][11]{: style="float:right;max-width:35%;margin-left:20px;border:0;"}

Push notifications are another great option to engage with your users, and are especially useful to handle time-sensitive calls to action. Mobile push notifications appear on your users' device, and web push notifications appear even when your site is not open. For specifics on using push notifications, see our [push notification article][5].

Users of your website or app need to opt-in to receive push notifications. See [push priming][13] for more details. 

## Segmentation and delivery rules

By default, a campaign containing in-app messages will be sent to all versions of the app in that app group. For example, the message will send to both web and mobile users. To send an in-app message exclusively to web or mobile, you will need to segment your campaign accordingly, which is supported by default through the Braze SDK. 

You can create a segment of your web users by selecting only your website’s app icon in the **Apps Used** section of a segment.

![Segment Details page with web app selected][10]

This will allow you to target users based on their behavior in an intelligent way. If you wanted to target web users to encourage them to download your mobile app, you’d create this segment as your target audience. If you wanted to send a messaging campaign that included a mobile in-app message but not a web message, you would simply uncheck your website’s icon in your segment.

## What integrations does Braze have?
Braze offers a version of our SDK for many platforms (web, Android, iOS, Flutter, React Native, and more), but they all operate essentially the same way. So if you see a reference to, say, the "Web SDK," it's just the version of the Braze SDK intended for your website.

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
[![Android]({% image_buster /assets/img/android.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) |[<i class="fa-brands fa-apple" style="font-size:60px;vertical-align: middle;"></i>]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/){: style="max-width:30%;margin-right:15px;border:0"} [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/) | [<i class="fas fa-globe" style="font-size:60px;vertical-align: middle;"></i>]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/){: style="max-width:30%;margin-right:15px;border:0"} [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)  

All integrations   | &nbsp;  |  &nbsp;
----------- |---------------- | --------------------
[![Cordova Android]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/android/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova Android]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/android/) | [![Cordova iOS]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/ios/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/ios/) | [![Flutter Android and iOS]({% image_buster /assets/img/flutter_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/flutter/flutter_sdk_integration/){: style="max-width:20%;margin-top:5%;border:0" class="noimgborder"}  [Flutter Android and iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/flutter/flutter_sdk_integration/)
[![React Native]({% image_buster /assets/img/reactnative_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/) | [![tvOS]({% image_buster /assets/img/tvos_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/tvos/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [tvOS]({{site.baseurl}}/developer_guide/platform_integration_guides/tvos/initial_sdk_setup/) | [![MacOS]({% image_buster /assets/img/macOS_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/macOS/initial_sdk_setup/){: style="max-width:40%;margin-top:15%;border:0" class="noimgborder"}  [MacOS]({{site.baseurl}}/developer_guide/platform_integration_guides/macOS/initial_sdk_setup/)
[![Unity Android]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/android/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity Android]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/android/) | [![Unity iOS]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/) | [![Xamarin]({% image_buster /assets/img/xamarin.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/){: style="max-width:35%;margin-top:5%;border:0" class="noimgborder"}  [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/) 
[![Roku]({% image_buster /assets/img/roku.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/) | [![Unreal Engine]({% image_buster /assets/img/unreal.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unreal_engine/initial_sdk_setup/){: style="max-width:30%;margin-right:15px;border:0" class="noimgborder"}  [Unreal Engine]({{site.baseurl}}/developer_guide/platform_integration_guides/unreal_engine/initial_sdk_setup/)


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/
[3]: {{site.baseurl}}/user_guide/data_and_analytics/your_analytics_dashboards/understanding_your_app_usage_data/
[4]: {{site.baseurl}}/user_guide/onboarding_with_braze/integration/#the-technical-side-of-the-integration-process
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/push/about/
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[7]: {% image_buster /assets/img_archive/app_group_list.png %}
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[10]: {% image_buster /assets/img_archive/web-users-segment.png %}
[11]: {% image_buster /assets/img_archive/web_push_macbook.png %}
[13]: {{site.baseurl}}user_guide/message_building_by_channel/push/push_primer_messages/