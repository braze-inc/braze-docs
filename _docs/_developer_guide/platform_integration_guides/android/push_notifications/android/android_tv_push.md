---
nav_title: Android TV Push
article_title: Android TV Push
platform: Android
page_order: 8
description: "This article shows how to implement and test Android TV Push."
channel:
  - push

---

# Android TV push
![]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

> While not a native feature, Android TV push integration is made possible by leveraging the Braze Android SDK and Firebase Cloud Messaging to register a push token for Android TV. It is, however, necessary to build a UI to display the notification payload after it is received.

## Implementation

1. **Integrate the Braze Android SDK**<br>
First, you must integrate the [Braze Android SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/?redirected=true) (If not already completed).<br><br>
2. **Integrate push notifications**<br>
Next, you must integrate [Android Push Notifications]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/) (If not already completed).<br><br>
3. **Create a custom toast view**<br>
Next, create a custom view in your app to display your notifications.<br><br>
4. **Create a custom notification factory**<br>
Lastly, you must create a [custom notification factory]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#custom-displaying-notifications). This will override the default SDK behavior and allow you to manually display the notifications. By returning `null`, this will prevent the SDK from processing and will require custom code to display the notification. After these steps have been completed, you can start sending push to Android TV!<br><br>
5. **Set up click analytics tracking (optional)**<br>
To track click analytics effectively, it is necessary to handle this manually, as Braze does not handle the display of the messages automatically. This can be achieved by creating a [push callback]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback) to listen for Braze push opened and received intents.

{% alert note %}
Note that these notifications **will not persist** and will only be visible to the user when the device displays them. This is due to Android TV's notification center not supporting historical notifications.
{% endalert %} 

## How to test push on Android TV

To test if your push implementation is successful, send a notification from the Braze dashboard as you would normally for an Android device.

- **If the application is closed**: The push message will display a toast notification in the corner of the screen.
![An Android TV displaying a push notification in the upper left corner of the screen.]({% image_buster /assets/img/android_tv.png %})
- **If the application is open**: You have the opportunity to display the message in your own hosted UI. We recommend following the UI styling of our Android Mobile SDK in-app messages.

## Additional information
For a marketing end user in Braze, launching a campaign to Android TV will be identical to launching a push to Android mobile apps. To target these devices exclusively, we recommend selecting the Android TV App in segmentation. 

The delivered and clicked response returned by FCM will follow the same convention as a mobile Android device; therefore, any errors will be visible in the message activity log.

[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/?redirected=true
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#custom-displaying-notifications
[9]: https://developer.android.com/guide/topics/ui/notifiers/toasts#CustomToastView
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/
[11]: {% image_buster /assets/img/android_tv.png %}
[12]: {% image_buster /assets/img/Television.png %}
