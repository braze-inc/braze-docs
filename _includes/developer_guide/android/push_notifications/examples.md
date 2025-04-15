{% multi_lang_include developer_guide/prerequisites/android.md %} You'll also need to [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

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
