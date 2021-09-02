---
nav_title: "About Push"
article_title: About Push
page_order: 0
page_type: reference
description: "This reference article gives a brief overview of Push, provides resources to get started with push messages, and notes some regulations."
channel:
  - Push

---

# What are Push Messages?

> Push notifications are wonderful for time-sensitive calls to action, as well as re-engaging users who haven't come into the app in a while. Successful push campaigns drive the user directly to content and demonstrate the value of your application.

![Push Message Example][1]{: height="400px"}  ![Push Message Example][2]{: height="400px"}

_To see more examples of push notifications, check out our [Case Studies][8]._

## Potential Use Cases

Push Notifications are a great tool for attracting new users and making re-engagement campaigns. Here are some examples of common Push message use cases. 

| Use Case | Explanation |
| -------- | ----------- |
| Initial Onboarding | Until users take the initial steps towards using your app (such as registering an account), their value is severely limited. Use push notifications to urge users to complete these steps so they can begin using your app in full. |
| First Purchases | After users are comfortable using your app, you can use push notifications to help convert them into in-app purchasers. |
| New Features | Push notifications can be effective in notifying disengaged users about new features that might attract them back to your app. |
| Time Sensitive Offers | If you have a clock ticking on an offer, sometimes push is a great way to let your users know about it before it expires. These messages generally carry a high sense of urgency and are optimal for reminding recently-lapsed users about your app.<br><br> For example, suppose your app is a game and you offer your users an in-game currency bonus if they maintain a streak of playing the game daily. Alerting a user that that streak is in danger of being broken could be a reasonable push if they've exceeded a certain number of days. |
{: .reset-td-br-1 .reset-td-br-2}

For more information on re-engaging lapsed users, see our [Quick Wins][23] page on the topic.

> Push should be formatted in plain-text. Key-value pairs allow for [deep linking][3] to external URLs or in-app features.

## Push Message Regulations

Because push messages are an intrusive type of messaging, going directly to the user's phone or browser, there are guidelines for sending push messages via apps and sites.

### Mobile Push Regulations for Apps

{% alert important %}
Your push messages must fall within the guidelines of the Apple App Store and Google's Play Store policies, specifically regarding using push messages as advertisements, spam, promotions, and more.
{% endalert %}

|Apple App Store Policies|
|---|
|[4.5.4][9] Push Notifications must not be required for the app to function, and should not be used for advertising, promotions, or direct marketing purposes or to send sensitive personal or confidential information.|
|[3.2.2][9] (i) Creating an interface for displaying third-party apps, extensions, or plug-ins similar to the App Store or as a general-interest collection. (ii) Monetizing built-in capabilities provided by the hardware or operating system, such as Push Notifications, the camera, or the gyroscope; or Apple services, such as Apple Music access or iCloud storage.|
{: .reset-td-br-1 .reset-td-br-2}

|Google Play Store Policy|
|---|
|[We don’t allow apps or ads that mimic or interfere with system functionality, such as notifications or warnings.][10] System-level notifications may only be used for an app’s integral features, such as an airline app that notifies users of special deals, or a game that notifies users of in-game promotions.|
{: .reset-td-br-1}

## Image and Text Specifications

### Native Mobile Push Notifications

{% tabs local %}
{% tab Images %}

**Image Type** | **Recommended Image Size** | **Max Image Size** | **File Types**
--- | --- | --- | ---
(iOS) 2:1 *Recommended* | 500KB | 5MB | PNG, JPG, GIF
(Android) Push Icon | 500KB | 5MB | PNG, JPG
(Android) Expanded Notification | 500KB | 5MB | PNG, JPG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endtab %}
{% tab Text %}

**Message Type** | **Max Message Length**
--- | ---
(iOS) Lock Screen | 110 Characters
(iOS) Notification Center | 110 Characters
(iOS) Banner Alert | 63 Characters
(Android) Lock Screen | 49 Characters
(Android) Notification Drawer | 597 Characters
{: .reset-td-br-1 .reset-td-br-2}

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

### Web Push Notifications

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
[9]: https://developer.apple.com/app-store/review/guidelines/
[10]: https://developers.google.com/android/play-protect/mobile-unwanted-software
[23]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
