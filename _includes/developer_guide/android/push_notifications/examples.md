# Implementation examples

> This optional and advanced implementation guide covers ways to leverage a custom FirebaseMessagingService subclass to get the most out of your push messages. Included is a custom use case built by our team, accompanying code snippets, and guidance on logging analytics. Visit our Braze Demo Repository [here](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Note that this implementation guide is centered around a Kotlin implementation, but Java snippets are provided for those interested.

## Custom notification layout

Braze notifications are sent as [data messages](https://firebase.google.com/docs/cloud-messaging/concept-options), which means that your application will always have a chance to respond and perform behavior accordingly, even in the background (in contrast to notification messages, which can be handled automatically by the system when your app is in the background). As such, your application will have a chance to customize the experience by, for example displaying personalized UI elements within the notification delivered to the notification tray. While implementing push in this way may be unfamiliar to some, one of our well-known features at Braze, [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), are a prime example of using custom view components to create an engaging experience!

{% alert important %}
Android imposes some limitations on what components can be used to implement custom notification views. Notification view layouts must _only_ contain View objects compatible with the [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews) framework.
{% endalert %}

## Personalized push notifications

Push notifications can display user-specific information inside a custom view hierarchy. In the following example, an API-trigger is used to send personalized push notification to a user so they can track check their current progress after completing a specific task in the app.

![Personalized Push dashboard Example]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

To set up a personalized push in the dashboard, register the specific category you want to be displayed, then set any relevant user attributes you'd like to display using Liquid.

![Personalized Push dashboard Example]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

## Logging analytics

You can log analytics using either of the following methods, however we recommend using the Braze API.

{% tabs local %}
{% tab Braze API %}
You can log analytics in real-time by making calls to the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). To log analytics, send the `braze_id` value from the Braze dashboard to identify which user profile to update.

![Personalized Push dashboard Example]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:80%;"}
{% endtab %}

{% tab Manual %}
Depending on the details of your payload, you can log analytics manually within your `FirebaseMessagingService.onMessageReceived` implementation or your startup activity. Keep in mind, your `FirebaseMessagingService` subclass must finish execution within 10 seconds of invocation to avoid being [flagged or terminated](https://firebase.google.com/docs/cloud-messaging/android/receive) by the Android system.
{% endtab %}
{% endtabs %}
