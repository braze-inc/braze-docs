---
nav_title: Push
article_title: Push
page_order: 4
layout: dev_guide
guide_top_header: "Push"
guide_top_text: "Push notifications are a tried-and-true way to send time-sensitive calls to action through mobile or web, as well as re-engage users who haven't come into the app in a while. They drive the user directly to content and demonstrate the value of your application. Push notifications are useful for driving users to a specific place, but you should use them wisely. <br><br> Read any of the following articles or check out our [Push Braze Learning course](https://learning.braze.com/messaging-channels-push) to learn who you can send a push to, how to send it, and what advanced push capabilities Braze offers. For examples of push notifications, check out our [customer stories](https://www.braze.com/customers)."
description: "This landing page is home to push messages. Here, you can find articles on push types, push registration, push enablement, push primers, push reporting, and more."
channel:
  - push

guide_featured_title: "Popular articles"
guide_featured_list:
- name: Push Types
  link: /docs/user_guide/message_building_by_channel/push/types/
  image: /assets/img/braze_icons/list.svg
- name: Push Registration
  link: /docs/user_guide/message_building_by_channel/push/push_registration/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: Push Enablement and Subscription
  link: /docs/user_guide/message_building_by_channel/push/users_and_subscriptions/
  image: /assets/img/braze_icons/users-01.svg
- name: Creating a Push Message
  link: /docs/user_guide/message_building_by_channel/push/creating_a_push_message/
  image: /assets/img/braze_icons/edit-05.svg

guide_menu_title: "More articles"
guide_menu_list:
- name: Advanced Options
  link: /docs/user_guide/message_building_by_channel/push/advanced_push_options/
  image: /assets/img/braze_icons/settings-01.svg
- name: Push Primers
  link: /docs/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
  image: /assets/img/braze_icons/phone-02.svg
- name: Reporting
  link: /docs/user_guide/message_building_by_channel/push/push_reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Android Options
  link: /docs/user_guide/message_building_by_channel/push/android/
  image: /assets/img/braze_icons/android.svg
- name: iOS Options
  link: /docs/user_guide/message_building_by_channel/push/ios/
  image: /assets/img/braze_icons/apple.svg
- name: Web Push
  link: /docs/user_guide/message_building_by_channel/push/web/
  image: /assets/img/braze_icons/monitor-01.svg
- name: Best Practices
  link: /docs/user_guide/message_building_by_channel/push/best_practices/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: Locales in Messaging
  link: /docs/user_guide/message_building_by_channel/push/using_locales/
  image: /assets/img/braze_icons/translate-01.svg
- name: Common Push Error Messages
  link: /docs/user_guide/message_building_by_channel/push/push_error_codes/
  image: /assets/img/braze_icons/alert-triangle.svg
- name: Troubleshooting
  link: /docs/user_guide/message_building_by_channel/push/troubleshooting/
  image: /assets/img/braze_icons/annotation-question.svg
- name: Frequently Asked Questions
  link: /docs/user_guide/message_building_by_channel/push/faq/
  image: /assets/img/braze_icons/annotation-question.svg
---

## [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-push){: style="float:right;width:120px;border:0;" class="noimgborder"}Use cases

![Push message example across Apple products.]({% image_buster /assets/img/red-dress.gif %}){: height="400px"}  ![Push message example from Stopwatch on an iPhone home screen that reads: "Hello! This is an iOS Push".]({% image_buster /assets/img/ios_push.png %}){: height="400px"}

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

## Push priming

Keep in mind that users need to opt-in to push to receive your messages, which means it's a good idea to use in-app messages to explain to your customers why you want to send them push notifications, and how enabling push will benefit them. This process is called [push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Push message regulations

Because push messages are an intrusive type of messaging that goes directly to your customer's phone or browser, there are guidelines for sending push messages through apps and sites.

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
