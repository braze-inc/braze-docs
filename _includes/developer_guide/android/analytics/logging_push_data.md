## Logging data with the Braze API (recommended)

You can log analytics in real-time by making calls to the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). To log analytics, send the `braze_id` value from the Braze dashboard to identify which user profile to update.

![Personalized Push dashboard Example]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:79%;"}

## Manually logging data

Depending on the details of your payload, you can log analytics manually within your `FirebaseMessagingService.onMessageReceived` implementation or your startup activity. Keep in mind, your `FirebaseMessagingService` subclass must finish execution within 9 seconds of invocation to avoid being [flagged or terminated](https://firebase.google.com/docs/cloud-messaging/android/receive) by the Android system.
