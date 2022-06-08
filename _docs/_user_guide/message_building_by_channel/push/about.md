---
nav_title: "About Push"
article_title: About Push
page_order: 0
page_type: reference
description: "This reference article gives a brief overview of push, provides resources to get started with push messages, and notes some regulations."
channel:
  - Push

---

# About push notifications

> This reference article gives a brief overview of push, provides resources to get started with push messages, and notes some regulations. For more on push notifications, check out our [Braze Learning course](https://learning.braze.com/messaging-channels-push)!

Push notifications are wonderful for time-sensitive calls to action, as well as re-engaging users who haven't come into the app in a while. Successful push campaigns drive the user directly to content and demonstrate the value of your application. 

Keep in mind that users need to opt-in to push to receive your messages, which means it's a good idea to use in-app messages to explain to your customers why you want to send them push notifications, and how enabling push will benefit them. This process is called [push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/create_push_primer/).

![Push message example across Apple products.][1]{: height="400px"}  ![Push message example from Stopwatch on an iPhone home screen that reads: "Hello! This is an iOS Push".][2]{: height="400px"}

To see more examples of push notifications, check out our [Case Studies][8].

## Potential use cases

Push notifications are a great tool for attracting new users and making re-engagement campaigns. Here are some examples of common push message use cases. 

| Use Case | Explanation |
| -------- | ----------- |
| Initial Onboarding | Until users take the initial steps towards using your app (such as registering an account), their value is severely limited. Use push notifications to urge users to complete these steps so they can begin using your app in full. |
| First Purchases | After users are comfortable using your app, you can use push notifications to help convert them into in-app purchasers. |
| New Features | Push notifications can be effective in notifying disengaged users about new features that might attract them back to your app. |
| Time Sensitive Offers | If you have a clock ticking on an offer, sometimes push is a great way to let your users know about it before it expires. These messages generally carry a high sense of urgency and are optimal for reminding recently-lapsed users about your app.<br><br> For example, suppose your app is a game and you offer your users an in-game currency bonus if they maintain a streak of playing the game daily. Alerting a user that that streak is in danger of being broken could be a reasonable push if they've exceeded a certain number of days. |
{: .reset-td-br-1 .reset-td-br-2}

For more information on re-engaging lapsed users, see our [Quick Wins][23] page on the topic.

## Prerequisites to use push

Before you can create and send any push messages using Braze, you need to work with your developers to integrate push into your website or app. For detailed steps, refer to our integration guides for each platform:

- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/)

## Push message regulations

Because push messages are an intrusive type of messaging that goes directly to your customer's phone or browser, there are guidelines for sending push messages via apps and sites.

### Mobile push regulations for apps

{% alert important %}
Your push messages must fall within the guidelines of the Apple App Store and Google's Play Store policies, specifically regarding using push messages as advertisements, spam, promotions, and more.
{% endalert %}

|Apple App Store Policies|
|---|
|[4.5.4][7] Push Notifications must not be required for the app to function, and should not be used for advertising, promotions, or direct marketing purposes or to send sensitive personal or confidential information.|
|[3.2.2][9] (i) Creating an interface for displaying third-party apps, extensions, or plug-ins similar to the App Store or as a general-interest collection. (ii) Monetizing built-in capabilities provided by the hardware or operating system, such as push notifications, the camera, or the gyroscope; or Apple services, such as Apple Music access or iCloud storage.|
{: .reset-td-br-1 .reset-td-br-2}

|Google Play Store Policy|
|---|
|[Unauthorized Use or Imitation of System Functionality][10] We don't allow apps or ads that mimic or interfere with system functionality, such as notifications or warnings. System-level notifications may only be used for an app’s integral features, such as an airline app that notifies users of special deals, or a game that notifies users of in-game promotions.|
{: .reset-td-br-1}

## Image and text specifications

For best results, refer to the following image size and message length guidelines when crafting your push messages. There may be some variance depending on the presence of an image, the notification state (iOS) and display setting of the user’s device, as well as the size of the device. When in doubt, keep your copy short and sweet.

### Native mobile push notifications

{% tabs local %}
{% tab Images %}

**Image Type** | **Recommended Image Size** | **Max Image Size** | **File Types**
--- | --- | --- | ---
(iOS) 2:1 *Recommended* | 500KB | 5MB | PNG, JPG, GIF
(Android) Push icon | 500KB | 5MB | PNG, JPG
(Android) Expanded notification | 500KB | 5MB | PNG, JPG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endtab %}
{% tab Text %}

| Message Type | Recommended Message Length (Text only) | Recommended Message Length (Rich)
--- | ---
(iOS) Lock Screen | 160 characters | 130 characters
(iOS) Notification Center | 160 characters | 130 characters
(iOS) Banner Alert | 80 characters | 65 characters
(Android) Lock Screen | 49 characters | N/A
(Android) Notification Drawer | 597 characters | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

Wondering how many characters you can use in an iOS push notification without it being truncated? Check out our [iOS character count guidelines]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count).

{% endtab %}
{% tab Payload Size %}

**Platform** | **Size**
--- | ---
pre iOS 8 | 0.256 KB
post iOS 8 | 2 KB
Android (FCM) | 4 KB
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

### Web push notifications

{% tabs local %}
{% tab Images %}

| **Browser** | **Recommended Icon Size**
| --- | ---
Chrome | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | Icons not configurable on a per-campaign basis
Opera | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2}

| **Browser** | **Platform** | **Large Image Size**
| --- | --- | ---
Chrome | macOS | N/A
Chrome | Android | 2 : 1 aspect ratio
Chrome | Windows | 360 ≥ x 240
Firefox | macOS| N/A
Safari | macOS | N/A
Opera | macOS | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Text %}

| **Browser** | **Platform** | **Maximum Title Length**  | **Maximum Message Body Length**
| --- | --- | --- | ---
Chrome | macOS | 35 | 50
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
Opera | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/red-dress.gif %}
[2]: {% image_buster /assets/img/ios_push.png %}
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
[8]: https://www.braze.com/customers
[7]: https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services
[9]: https://developer.apple.com/app-store/review/guidelines/#unacceptable
[10]: https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories
[23]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
