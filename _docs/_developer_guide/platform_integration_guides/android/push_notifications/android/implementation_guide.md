---
nav_title: Advanced Implementation Guide (Optional)
article_title: Advanced Push Notification Implementation for Android (Optional)
platform: Android
page_order: 29
description: "This advanced implementation guide covers how to customize the layout of push notifications to display user-specific information within your messages. Also included is an example use case built by our team, accompanying code snippets, and guidance on logging analytics."
channel:
  - push
---

<br>
{% alert important %}
Looking for the basic push notification developer integration guide? Find it [here]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/).
{% endalert %}

# Advanced implementation guide

> This optional and advanced implementation guide covers ways to leverage a custom FirebaseMessagingService subclass to get the most out of your push messages. Included is a custom use case built by our team, accompanying code snippets, and guidance on logging analytics. Visit our Braze Demo Repository [here](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Note that this implementation guide is centered around a Kotlin implementation, but Java snippets are provided for those interested.

## Custom notification layout

Braze notifications are sent as [data messages](https://firebase.google.com/docs/cloud-messaging/concept-options), which means that your application will always have a chance to respond and perform behavior accordingly, even in the background (this is in contrast to notification messages, which can be handled automatically by the system when your app is in the background). As such, your application will have a chance to customize the experience by, for example displaying personalized UI elements within the notification delivered to the notification tray. While implementing push in this way may be unfamiliar to some, one of our well-known features at Braze, [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), are a prime example of using custom view components to create an engaging experience!

#### Requirements

Android imposes some limitations on what components can be used to implement custom notification views. Notification view layouts must _only_ contain View objects compatible with the [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews) framework.

### Personalized push notifications

Push notifications can display user-specific information inside a custom view hierarchy. The following example shows a push notification after a user has completed a specific task (Braze Learning course) and is now encouraged to expand this notification to check their progress. The information provided here is user-specific and can be fired off as a session is completed or specific user action is taken by leveraging an API trigger. 

![Personalized Push dashboard Example]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

#### Dashboard configuration

To set up a personalized push in the dashboard, you must register the specific category you want to be displayed. Set the appropriate user attributes you want the message to show within the key-value pairs using standard Liquid. These views can be personalized based on specific user attributes of a specific user profile.

![Personalized Push dashboard Example]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

##### Ready to log analytics?
Visit the [following section](#logging-analytics) to better understand how the flow of data should look.

## Logging analytics

### Logging with the Braze API (recommended)

Logging analytics can only be done in real-time with the help of the customer's server hitting our [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). To log analytics, send down the `braze_id` value in the key-value pairs field (as seen in the following screenshot) to identify which user profile to update.

![Personalized Push dashboard Example]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:80%;"}

### Logging manually 

Logging manually can be achieved by logging whatever elements you wish from either within your `FirebaseMessagingService.onMessageReceived` implementation or from within your startup activity, based on the extras present in the payload. However, an important caveat to remember is that your `FirebaseMessagingService` subclass _must_ finish execution within 10 seconds of invocation to avoid being [flagged or terminated](https://firebase.google.com/docs/cloud-messaging/android/receive) by the Android system. 


