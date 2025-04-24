## About push notifications for Android TV

![]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

While not a native feature, Android TV push integration is made possible by leveraging the Braze Android SDK and Firebase Cloud Messaging to register a push token for Android TV. It is, however, necessary to build a UI to display the notification payload after it is received.

## Prerequisites

To use this feature, you'll need to complete the following:

- [Integrate the Braze Android SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)
- [Set up push notifications for the Braze Android SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)

## Setting up push notifications

To set up push notifications for Android TV:

1. Create a custom view in your app to display your notifications.
2. Create a [custom notification factory]({{site.baseurl}}/developer_guide/push_notifications/customization#customization-display). This will override the default SDK behavior and allow you to manually display the notifications. By returning `null`, this will prevent the SDK from processing and will require custom code to display the notification. After these steps have been completed, you can start sending push to Android TV!<br><br>
3. (Optional) To track click analytics effectively, set up click analytics tracking. This can be achieved by creating a [push callback]({{site.baseurl}}/developer_guide/push_notifications/customization#push-callback) to listen for Braze push opened and received intents.

{% alert note %}
These notifications **will not persist** and will only be visible to the user when the device displays them. This is due to Android TV's notification center not supporting historical notifications.
{% endalert %} 

## Testing Android TV push notifications

To test if your push implementation is successful, send a notification from the Braze dashboard as you would normally for an Android device.

- **If the application is closed**: The push message will display a toast notification on the screen.
- **If the application is open**: You have the opportunity to display the message in your own hosted UI. We recommend following the UI styling of our Android Mobile SDK in-app messages.

## Best practices

For marketers using Braze, launching a campaign to Android TV will be identical to launching a push to Android mobile apps. To target these devices exclusively, we recommend selecting the Android TV App in segmentation.

The delivered and clicked response returned by FCM will follow the same convention as a mobile Android device; therefore, any errors will be visible in the message activity log.
