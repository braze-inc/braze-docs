---
nav_title: iOS
article_title: Push Notifications for Unity
platform:
  - Unity
  - iOS
channel: push
ex_push_payload: archive/apple/push_payload.json
page_order: 1
description: "This reference article covers iOS push notification integration for the Unity platform."

---

# iOS push notification integration

> This reference article covers iOS push notification integration for the Unity platform.

## Step 1: Choose automatic or manual push integration

Braze provides a native Unity solution for automating iOS push integrations.

- If you would prefer to complete the integration manually by modifying your built Xcode project, follow our [native iOS push instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/).
- If you are transitioning from a manual integration to an automated one, follow the instructions on [Transitioning to an automated integration]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/#transitioning-from-manual-to-automated-integration-ios).
- Our automatic push notification solution takes advantage of iOS 12's Provisional Authorization feature and is not available to use with the native push prompt pop-up.

## Step 2: Implement automatic push integration

### Configure push notifications

Follow our [iOS push notification configuration documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) to configure Braze using a `.p8` file.

### Enable automatic push integration

Open the Braze Configuration Settings in the Unity Editor by navigating to **Braze > Braze Configuration**.

Check **Integrate Push With Braze** to automatically register users for push notifications, pass push tokens to Braze, track analytics for push opens, and take advantage of our default push notification handling.

### Enable background push (optional)

Check **Enable Background Push** if you want to enable `background mode` for push notifications. This allows the system to wake your application from the `suspended` state when a push notification arrives, enabling your application to download content in response to push notifications. Checking this option is required for our uninstall tracking functionality.

![The Unity editor shows the Braze configuration options. In this editor, the "Automate Unity iOS integration", "Integrate push with braze", and "Enable background push" are enabled.]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

### Disable automatic registration (optional)

Users who have not yet opted-in to push notifications will automatically be authorized for push upon opening your application. To disable this feature and manually register users for push, check **Disable Automatic Push Registration**.

- If **Disable Provisional Authorization** is not checked on iOS 12 or later, the user will be provisionally (silently) authorized to receive quiet push. If checked, the user will be shown the native push prompt.
- If you need to configure exactly when the prompt is shown at runtime, disable automatic registration from the Braze configuration editor and use `AppboyBinding.PromptUserForPushPermissions()` instead.

![The Unity editor shows the Braze configuration options. In this editor, the "Automate Unity iOS integration", "integrate push with braze", and "disable automatic push registration" are enabled.]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})

## Step 3: Set push listeners

If you want to pass push notification payloads to Unity or take additional steps when a user receives a push notification, Braze provides the option of setting push notification listeners.

### Push received listener

The push received listener is fired when a user receives a push notification while actively using the application (such as when the app is foregrounded). Set the push received listener in the Braze configuration editor. If you need to configure your game object listener at runtime, use `AppboyBinding.ConfigureListener()` and specify `BrazeUnityMessageType.PUSH_RECEIVED`.

![The Unity editor shows the Braze configuration options. In this editor, the "Set Push Received Listener" option is expanded, and the "Game Object Name" (AppBoyCallback) and "Callback Method Name" (PushNotificationReceivedCallback) are provided.]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

### Push opened listener

The push opened listener is fired when a user launches the app by clicking on a push notification. To send the push payload to Unity, set the name of your game object and push opened listener callback method under the **Set Push Opened Listener** option:

![The Unity editor shows the Braze configuration options. In this editor, the "Set Push Received Listener" option is expanded, and the "Game Object Name" (AppBoyCallback) and "Callback Method Name" (PushNotificationOpenedCallback) are provided.]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

If you need to configure your game object listener at runtime, use `AppboyBinding.ConfigureListener()` and specify `BrazeUnityMessageType.PUSH_OPENED`.

### Push listener implementation example

The following example implements the `AppboyCallback` game object using a callback method name of `PushNotificationReceivedCallback` and `PushNotificationOpenedCallback`, respectively.

![This implementation example graphic shows the Braze configuration options mentioned in the preceding sections and a C# code snippet.]({% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %})

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
}
```

## Advanced features

### Push token callback

To receive a copy of Braze device tokens from the OS, set a delegate using `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`.

### Other features

To implement advanced features such as deep links, badge counts, and custom sounds, visit our [native iOS push instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/).

