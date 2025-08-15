---
nav_title: "About push notifications"
article_title: About Push notifications
page_order: 0
page_type: reference
description: "This reference article gives a brief overview of push, provides resources to get started with push messages, and notes some regulations."
channel:
  - Push

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-push){: style="float:right;width:120px;border:0;" class="noimgborder"}About push notifications

> Push notifications are wonderful for time-sensitive calls to action, as well as re-engaging users who haven't come into the app in a while. Successful push campaigns drive the user directly to content and demonstrate the value of your application.

Keep in mind that users need to opt-in to push to receive your messages, which means it's a good idea to use in-app messages to explain to your customers why you want to send them push notifications, and how enabling push will benefit them. This process is called [push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

![Push message example across Apple products.]({% image_buster /assets/img/red-dress.gif %}){: height="400px"}  ![Push message example from Stopwatch on an iPhone home screen that reads: "Hello! This is an iOS Push".]({% image_buster /assets/img/ios_push.png %}){: height="400px"}

To see more examples of push notifications, check out our [Case Studies](https://www.braze.com/customers).

## Potential use cases

Push notifications are a great tool for attracting new users and making re-engagement campaigns. Here are some examples of common push message use cases.

| Use Case | Explanation |
| -------- | ----------- |
| Initial Onboarding | Until users take the initial steps toward using your app (such as registering an account), their value is severely limited. Use push notifications to urge users to complete these steps so they can begin using your app in full. |
| First Purchases | After users are comfortable using your app, you can use push notifications to help convert them into in-app purchasers. |
| New Features | Push notifications can be effective in notifying disengaged users about new features that might attract them back to your app. |
| Time Sensitive Offers | If you have a clock ticking on an offer, sometimes push is a great way to let your users know about it before it expires. These messages generally carry a high sense of urgency and are optimal for reminding recently-lapsed users about your app.<br><br> For example, suppose your app is a game and you offer your users an in-game currency bonus if they maintain a streak of playing the game daily. Alerting a user that that streak is in danger of being broken could be a reasonable push if they've exceeded a certain number of days. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For more information on re-engaging lapsed users, see our [Quick Wins]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) page on the topic.

## Prerequisites to use push

Before you can create and send any push messages using Braze, you need to work with your developers to integrate push into your website or app. For detailed steps, refer to our integration guides for each platform:

- [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## Push message regulations

Because push messages are an intrusive type of messaging that goes directly to your customer's phone or browser, there are guidelines for sending push messages via apps and sites.

### Mobile push regulations for apps

{% alert important %}
Your push messages must fall within the guidelines of the Apple App Store and Google's Play Store policies, specifically regarding using push messages as advertisements, spam, promotions, and more.
{% endalert %}

|Apple App Store Policies|
|---|
|[3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) Unacceptable: (i) Creating an interface for displaying third-party apps, extensions, or plug-ins similar to the App Store or as a general-interest collection.| 
|[4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) Push Notifications must not be required for the app to function, and should not be used to send sensitive personal or confidential information. Push Notifications should not be used for promotions or direct marketing purposes unless customers have explicitly opted in to receive them via consent language displayed in your app’s UI, and you provide a method in your app for a user to opt out from receiving such messages.|
|[4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) You may not monetize built-in capabilities provided by the hardware or operating system, such as Push Notifications, the camera, or the gyroscope; or Apple services and technologies, such as Apple Music access, iCloud storage, or Screen Time APIs.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

|Google Play Store Policy|
|---|
|[Unauthorized Use or Imitation of System Functionality](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) We don't allow apps or ads that mimic or interfere with system functionality, such as notifications or warnings. System-level notifications may only be used for an app's integral features, such as an airline app that notifies users of special deals, or a game that notifies users of in-game promotions.|
{: .reset-td-br-1 role="presentation" }

