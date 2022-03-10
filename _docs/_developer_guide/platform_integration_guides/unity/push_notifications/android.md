---
nav_title: Android
article_title: Android Push Notifications for Unity
platform: 
  - Unity
  - Android
channel: push
page_order: 1
description: "This reference article covers the Android push notification integration for the Unity platform."

---

# Push notifications

These instructions are for integrating push with [Firebase Cloud Messaging (FCM)][9].

See our [Unity ADM][64] documentation for ADM integration instructions.

## Step 1: Enable Firebase

To get started, follow the [Firebase Unity setup documentation][11].

{% alert note %}
Integrating the Firebase Unity SDK may cause your `AndroidManifest.xml` to be overridden. If that occurs, make sure to revert it to the original.
{% endalert %}

## Step 2: Set your Firebase credentials

You need to input your Firebase Server Key and Sender ID into the Braze dashboard. To do this, log in to the [Firebase Developers Console][58] and select your Firebase project. Next, select **Cloud Messaging** under **Settings** and copy the Server Key and Sender ID:<br>![][59]

In Braze, select your Android app on the **App Settings** page under **Manage Settings**. Next, enter your Firebase Server Key in the **Firebase Cloud Messaging Server Key** field and Firebase Sender ID in the **Firebase Cloud Messaging Sender** ID field.

![][15]

## Step 3: Implement automatic push integration

The Braze SDK can automatically handle push registration with the Firebase Cloud Messaging Servers to have devices receive push notifications.

![The Unity editor shows the Braze configuration options. In this editor, the "Automate Unity Android Integration", "Push Notification Firebase Push", "Push Configuration Handle Push Deeplinks Automatically", "Push Configuration Push Notification HTML Rendering Enabled", and "Set Push Deleted/Opened/Received Listeners" are set. The fields "Firebase Sender ID", "Small/Large Icon Drawable", "Default Notification Accent Color" are also provided.][62]

- **Automatic Firebase Cloud Messaging Registration Enabled**<br> Instructs the Braze SDK to automatically retrieve and send an FCM push token for a device. 
- **Firebase Cloud Messaging Sender ID**<br> The Sender ID from your Firebase console.
- **Handle Push Deeplinks Automatically**<br> Whether the SDK should handle opening deep links or opening the app when push notifications are clicked.
- **Small Notification Icon Drawable**<br>The drawable should be displayed as the small icon whenever a push notification is received. The notification will use the application icon as the small icon if no icon is provided.

## Step 4: Set push listeners

If you would like to pass push notification payloads to Unity or take additional steps when a user receives a push notification, Braze provides the option of setting push notification listeners.

In Braze, select your Android app on the **App Settings** page under **Manage Settings**. Next, enter your Firebase Server Key in the **Push Notification Settings** field and Firebase Sender ID in the **Push Notification Settings** ID field.

#### Push received listener

The push received listener is fired when a user receives a push notification. To send the push payload to Unity, set the name of your game object and push the received listener callback method under the **Set Push Received Listener**.

#### Push opened listener

The push opened listener is fired when a user launches the app by clicking on a push notification. To send the push payload to Unity, set the name of your game object and push opened listener callback method under the **Set Push Opened Listener**.

#### Push deleted listener (Android only)

The push deleted listener is fired when a user swipes away or dismisses a push notification. To send the push payload to Unity, set the name of your game object and push deleted listener callback method under the **Set Push Deleted Listener**.

#### Push listener implementation example

The following example implements the `BrazeCallback` game object using a callback method name of `PushNotificationReceivedCallback`, `PushNotificationOpenedCallback`, and `PushNotificationDeletedCallback` respectively.

![This implementation example graphic shows the Braze configuration options mentioned above and a C# code snippet.][63]

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);   
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);   
#endif  
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);  
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);   
#endif  
  }

  void PushNotificationDeletedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationDeletedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification dismissed: " + pushNotification);  
#endif
  }
}
```

### Implementation example

The sample project in the [Braze Unity SDK repository][13] contains a full working sample app that includes FCM.

## Deep linking to in-app resources

Although Braze can handle standard deep links (such as website URLs, Android URIs, etc.) out of the box, creating custom deep links requires an additional Manifest setup.

For setup guidance, visit [Deep Linking to In-App Resources][26].

[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/troubleshooting/
[9]: https://firebase.google.com/docs/cloud-messaging/
[11]: https://firebase.google.com/docs/unity/setup
[12]: https://firebase.google.com/docs/android/setup
[13]: https://github.com/Appboy/appboy-unity-sdk/tree/master/unity-samples
[15]: {% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey"
[26]: https://developer.android.com/training/app-links/deep-linking
[58]: https://console.firebase.google.com/
[59]: {% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey"
[61]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/advanced_use_cases
[62]: {% image_buster /assets/img/unity/android/unity_android_push_settings_config.png %} "Android Push Settings"
[63]: {% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Android Full Listener Example"
[64]: {{site.baseurl}}/developer_guideplatform_integration_guides/unity/push_notifications/adm_push_notifications/