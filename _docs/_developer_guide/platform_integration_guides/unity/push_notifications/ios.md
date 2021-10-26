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

# Push notifications

## Step 1: Choose automatic or manual push integration

Braze provides a native Unity solution for automating iOS push integrations.

- If you would prefer instead to complete the integration manually by modifying your built Xcode project, please follow our [native iOS Push instructions][8].
- If you are transitioning from a manual integration to an automated one, follow the instructions on [Transitioning from Manual to Automated Integration][2].
- Our automatic push notification solution takes advantage of iOS 12's Provisional Authorization feature and is not available to use with the native push prompt pop-up.

## Step 2 (Optional): Implement automatic push integration

### Configure push notifications

Follow the instructions in our [iOS Push Notification Configuration documentation][8] to configure Braze using a `.p8` or `.p12` file.

### Enable automatic push integration

In the Unity Editor, open the Braze Configuration Settings by navigating to "Braze" > "Braze Configuration".

![enable push notification][24]

Check "Integrate Push With Braze" to automatically register users for push notifications, pass push tokens to Braze, track analytics for push opens, and take advantage of Braze's default push notification handling.

![Integrate Push With Braze][27]

### (Optional): Enable background push

Check "Enable Background Push" if you would like to enable `background mode` for push notifications. This allows the system to wake your application from the `suspended` state when a push notification arrives, enabling your application to download content in response to push notifications. Checking this option is required for Braze's uninstall tracking functionality.

![Enabling Background Push][29]

### (Optional): Disable automatic registration

Users who have not yet opted-in to push notifications will automatically be authorized for push upon opening your application. To disable this feature and manually register users for push, check "Disable Automatic Push Registration".

- If "Disable Provisional Authorization" is not checked, on iOS 12 and above, the user will be provisionally (silently) authorized to receive quiet push. If checked, the user will be shown the native push prompt.

- If you need to configure exactly when the prompt is shown at runtime, disable automatic registration from the Braze configuration editor and use `AppboyBinding.PromptUserForPushPermissions()` instead.

![Disable Automatic Push Registration][28]

## Step 3: Set push listeners

If you would like to pass push notification payloads to Unity or take additional steps when a user receives a push notification, Braze provides the option of setting push notification listeners.

### Push received listener

The Push Received listener is fired when a user receives a push notification while they are actively using the application (i.e., the app is foregrounded). Set the push received listener in the Braze configuration editor.

![Push Received Listener][30]

- If you need to configure your game object listener at runtime, use `AppboyBinding.ConfigureListener()` and specify `BrazeUnityMessageType.PUSH_RECEIVED`.

### Push opened listener

The Push Opened listener is fired when a user launches the app by clicking on a push notification. To send the push payload to Unity, set the name of your Game Object and Push Opened listener callback method under the "Set Push Opened Listener" foldout, like so:

![Push Opened Listener][31]


- If you need to configure your game object listener at runtime, use `AppboyBinding.ConfigureListener()` and specify `BrazeUnityMessageType.PUSH_OPENED`.

### Push listener implementation example

The following example implements the `AppboyCallback` game object using a callback method name of `PushNotificationReceivedCallback` and `PushNotificationOpenedCallback` respectively.

![Game Object Linking][32]

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

To receive a copy of device tokens that Braze receives from the OS, set a delegate using `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`.

### Other features

To implement advanced features such as deep links, badge counts, and custom sounds, visit our [native iOS Push instructions][8].

[1]: #manual-push-integration
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/#transitioning-from-manual-to-automated-integration-ios
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/
[9]: https://developer.apple.com/ios/manage/overview/index.action "iOS Provisioning Portal"
[10]: {% image_buster /assets/img_archive/ios_provisioning.png %} "pushNotification2.png"
[11]: {% image_buster /assets/img_archive/AppleProvisioningOptions.png %} "AppleProvisioningOptions.png"
[12]: {% image_buster /assets/img_archive/push_cert_gen.png %} "pushNotification3.png"
[15]: https://github.com/Appboy/appboy-unity-sdk/blob/master/unity-samples/iOS/Roll-A-Ball-Ios/Classes/UnityAppController.mm "sample AppController.mm"
[24]: {% image_buster /assets/img_archive/Enable_push_capabilities.png %}
[27]: {% image_buster /assets/img/unity/ios/unity_ios_api_key.png %}
[28]: {% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %}
[29]: {% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %}
[30]: {% image_buster /assets/img/unity/ios/unity_ios_push_received.png %}
[31]: {% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %}
[32]: {% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %}
