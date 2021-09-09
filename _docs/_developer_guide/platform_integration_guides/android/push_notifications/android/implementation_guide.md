---
nav_title: Advanced Implementation (Optional)
article_title: Advanced Push Notification Implementation for Android (Optional)
platform: Android
page_order: 29
description: "This advanced implementation guide covers how to customize the layout of push notifications to display user-specific information within your messages. Also included is an example use case built by our team, accompanying code snippets, and guidance on logging analytics."
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

The behavior of push notifications in Android depends on whether your application is in the foreground or background. When your application is in the background state, notifications will be added to the notification tray. When the user touches to expand the notification to bring it to the foreground, your application will have a chance to display additional information and customize the experience. While implementing push in this way may be unfamiliar to some, one of our well-known features at Braze, [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), are a prime example of using custom view components to create an engaging experience!

#### Requirements

Android imposes some limitations on what components can be used to implement custom notification views. Notification view layouts must _only_ contain View objects that are compatible with the [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews) framework.

### Personalized Push Notifications

Push notifications can display user-specific information inside a content extension. The example below shows a push notification after a user has completed a specific task (Braze LAB course) and is now encouraging users to expand this notification to check their progress. The information provided here is user-specific and can be fired off as a session is completed or specific user action is taken by leveraging an API trigger. 

![Personalized Push Dashboard Example][6]{: style="max-width:60%;border:0"}

#### Dashboard Configuration

To set up a personalized push in the dashboard, you must register the specific category you would like to be displayed. Set the appropriate user attributes you would like the message to show within the key-value pairs using standard Liquid. These views can be personalized based on specific user attributes of a specific user profile.

![Personalized Push Dashboard Example][5]{: style="max-width:60%;"}


[5]: {% image_buster /assets/img/push_implementation_guide/push5.png %}
[6]: {% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}
