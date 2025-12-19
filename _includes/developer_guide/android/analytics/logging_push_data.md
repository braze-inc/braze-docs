## Logging data with the Braze API (recommended)

If you're handling push notifications with custom code instead of using the Braze SDK's default notification handling, you can log analytics in real-time by making calls to the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). 

### Step 1: Pass the Braze ID in your push payload

To identify which user profile to update, include the `braze_id` value as a key-value pair in your push notification payload when creating the campaign in the Braze dashboard.

![Personalized Push dashboard Example]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:79%;"}

### Step 2: Extract the Braze ID and call the API

In your custom notification handler, extract the `braze_id` from the notification payload and make a server-side call to the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to log the appropriate event (such as push opened, push received, or a custom event). You'll need to send this request from your server using your Braze REST API key.

The `/users/track` endpoint can identify users using either `braze_id` or `external_id`. For example, to log a push open event using the `braze_id`:

```json
{
  "events": [
    {
      "braze_id": "abc123xyz",
      "name": "push_notification_opened",
      "time": "2024-01-01T00:00:00Z"
    }
  ]
}
```

Alternatively, if you have the user's `external_id`, you can use that instead of `braze_id` in your API call.

## Manually logging data

Alternatively, depending on the details of your payload, you can log analytics manually within your `FirebaseMessagingService.onMessageReceived` implementation or your startup activity by calling the appropriate Braze SDK methods directly (such as `Braze.logPushNotificationOpened()`). Keep in mind, your `FirebaseMessagingService` subclass must finish execution within 9 seconds of invocation to avoid being [flagged or terminated](https://firebase.google.com/docs/cloud-messaging/android/receive) by the Android system.
