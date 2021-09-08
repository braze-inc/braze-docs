---
nav_title: Advanced Implementation (Optional)
article_title: Advanced Push Notification Implementation for Android (Optional)
platform: Android
page_order: 29
description: "This advanced implementation guide covers how to customize the layout of push notification to display user-specific information within your messages. Also included is an example use case built by our team, accompanying code snippets, and guidance on logging analytics."
channel:
  - push
---

<br>
{% alert important %}
Looking for the out-of-the-box Push developer integration guide? Find it [here]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/).
{% endalert %}

# Push Notification Implementation Guide

> This optional and advanced implementation guide covers ways to leverage a custom FirebaseMessagingService subclass to get the most out of your push messages. Included is a custom use case built by our team, accompanying code snippets, and guidance on logging analytics. Visit our Braze Demo Repository [here](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Please note that this implementation guide is centered around a Kotlin implementation, but Java snippets are provided for those interested.

## Custom Notification Layout

When your application is in the background state, the notification will simply be added to the notification tray. But when you're application is in the foreground, it is possible to override the default layout displayed to the user to display personalized information.

The behavior of push notifications in Android depend on whether your application is in the foreground or background. When in background, the notification is delivered to the notification tray. When the user touches to expand the notification, your application will have a chance to display additional intformation and customize the experience. When your application is in the foreground, your application has the opportunity to decide what, if anything to display. While implementing push in this way may be unfamiliar to some, one of our well-known features at Braze, [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), are a prime example of using custom view components to create an egaging experience!

#### Requirements:

Android imposes some limitations on what components can be used to implement custom notification views. Notification view layouts must _only_ contain View objects that are compatible with the [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews) framework.


### Personalized Push Notifications
![Personalized Push Dashboard Example][6]{: style="float:right;max-width:40%;margin-left:15px;border:0"}

Push notifications can display user-specific information inside a content extension. The example to the right shows a push notification after a user has completed a specific task (Braze LAB course) and is now encouraged to expand this notification to check their progress. The information provided here is user-specific and can be fired off as a session is completed or specific user action is taken by leveraging an API trigger. 

#### Dashboard Configuration

To set up a personalized push in the dashboard, you must register the specific category you would like to be displayed, and then within the key-value pairs using standard Liquid, set the appropriate user attributes you would like the message to show. These views can be personalized based on specific user attributes of a specific user profile.

![Personalized Push Dashboard Example][5]{: style="max-width:60%;"}


[1]: {% image_buster /assets/img/push_implementation_guide/push1.png %}
[3]: {% image_buster /assets/img/push_implementation_guide/push3.png %}
[5]: {% image_buster /assets/img/push_implementation_guide/push5.png %}
[6]: {% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}
[8]: {% image_buster /assets/img/push_implementation_guide/push8.png %}
[9]: {% image_buster /assets/img/push_implementation_guide/push9.png %}
[12]: {% image_buster /assets/img/push_implementation_guide/push12.png %}
[13]: {% image_buster /assets/img/push_implementation_guide/push13.png %}
[14]: {% image_buster /assets/img/push_implementation_guide/push14.png %}
[15]: {% image_buster /assets/img/push_implementation_guide/push15.png %}
[16]: {% image_buster /assets/img/push_implementation_guide/push16.png %}
[17]: {% image_buster /assets/img/push_implementation_guide/push17.png %}
[18]: {% image_buster /assets/img/push_implementation_guide/push18.png %}
[19]: {% image_buster /assets/img_archive/add_app_groups.png %}
