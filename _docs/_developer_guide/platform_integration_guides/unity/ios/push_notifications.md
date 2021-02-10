---
nav_title: Push Notifications
platform: Unity
subplatform: iOS
ex_push_payload: archive/apple/push_payload.json
page_order: 1
---
# Push Notifications

A push notification is an out-of-app alert that appears on the user's screen when an important update occurs. Push notifications are a valuable way to provide your users with time-sensitive and relevant content or to re-engage them with your app.

Sample push notification:

![Sample Push][19]

Check out [push troubleshooting documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/troubleshooting/) for additional best practices.

## Step 1: Configure the Apple Developer Settings

1. Navigate to the [iOS Provisioning Portal][9]
2. Select Identifiers > App IDs in the left sidebar

    ![iOSPush3][10]

3. Select your application
4. If push notifications are not enabled, click Edit to update the app settings
  ![AppleProvisioningOptions][11]
5. Tick the Enable check box and click Create Certificate under the Production SSL Certificate
  ![iOSPush3][12]
6. Follow the instructions from the SSL certificate assistant. You should now see a green status to indicate that push is enabled. You must update your provisioning profile for the app after you create your SSL certificates. A simple "Refresh" in the organizer will accomplish this.

## Step 2: Export Your Push Certificate

1. Download the production push certificate that you just created and open it with the Keychain Access application
2. In Keychain Access, click on My Certificates and locate your push certificate private key
3. Export it as a `.p12` file and use a temporary, unsecure password (you will need this password when uploading your certificate to Braze)
4. Navigate to the [App Settings page][13] in the dashboard and upload your production certificate.
 ![push upload example][14]
 >  You can upload either your development or universal push certificates to the dashboard for your distribution provisioning profile apps, but you can only have one active at a time. As such, if you wish to do repeated testing of push notifications once your app goes live in the App Store, we recommend setting up a separate App Group or App for the development version of your app.

## Step 3: Customize Push Notification Settings

Braze provides a native Unity solution for automating the Unity iOS push notification integration. To take advantage of this option, please ensure that you have followed the Initial SDK Setup steps on [setting your Braze API key][7] through Unity.

- If you would prefer instead to complete the integration manually by modifying your built Xcode project, please follow the [Manual Push Integration instructions][1].
- If you are transitioning from a manual integration to an automated one, please follow the instructions on [Transitioning from Manual to Automated Integration][2] before following the rest of these steps.

### Step 1: Open Braze Configuration Settings

In the Unity Editor, open the Braze Configuration Settings by navigating to Braze > Braze Configuration.

### Step 2: Integrating Push With Braze

Check "Integrate Push With Braze" to automatically register users for push notifications, pass push tokens to Braze, track analytics for push opens, and take advantage of Braze's default push notification handling.

![Integrate Push With Braze][27]

Users who have not yet opted-in to push notifications will be prompted to opt-in upon opening your application. To disable the automatic opt-in prompt and manually register users for push, see [Disabling Automatic Push Registration][6] below.

>  If you do not check this option, you will not be able to send your users push notifications from the Braze dashboard without following the [manual push notification integration][1] instructions.

#### Disabling Automatic Push Registration

Check "Disable Automatic Push Registration" if you would like to manually register users with APNs (Apple Push Notification Service). Unity provides [NotificationServices.RegisterForNotifications][5] to do this from Unity.

![Disable Automatic Push Registration][28]

>  If you check this option, make sure that you are registering users for push notifications EVERY time the application runs after users have granted push permissions to your app. Apps need to re-register with APNs as [device tokens can change arbitrarily][4].

#### Enabling Background Push

Check "Enable Background Push" if you would like to enable [background mode][4] for push notifications. This allows the system to wake your application from the [Suspended][3] state when a push notification arrives, enabling your application to download content in response to push notifications. Checking this option is required for Braze's uninstall tracking functionality.

![Enabling Background Push][29]

>  If you build your Xcode project with "Enable Background Push" checked and then later uncheck this option, you will need to either manually disable background push or choose "Replace" when rebuilding your iOS project. You can manually disable background push by removing `remote-notifications` from the `UIBackgroundModes` array in your Info.plist.

### Step 3: Setting Push Listeners

If you would like to pass push notification payloads to Unity or take additional steps when a user receives a push notification, Braze provides the option of setting push notification listeners.

#### Push Received Listener

The Push Received listener is fired when a user receives a push notification while they are actively using the application (i.e., the app is foregrounded). To send the push payload to Unity, set the name of your Game Object and Push Received listener callback method under the "Set Push Received Listener" foldout, like so:

![Push Received Listener][30]

#### Push Opened Listener

The Push Opened listener is fired when a user launches the app by clicking on a push notification. To send the push payload to Unity, set the name of your Game Object and Push Opened listener callback method under the "Set Push Opened Listener" foldout, like so:

![Push Opened Listener][31]

#### Push Listener Implementation Example

The following example implements the `AppboyCallback` game object using a callback method name of `PushNotificationReceivedCallback` and `PushNotificationOpenedCallback` respectively. These methods are implemented in a file called `MainMenu.cs` and is a script linked to that game object. Every script attached to the game object that has an `PushNotificationReceivedCallback` or `PushNotificationOpenedCallback` function will be called.

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

## Manual Push Integration

### Step 1: Update Application Code

- Add the code below to your `application:didRegisterForRemoteNotificationsWithDeviceToken` method

  ```objc
  [[Appboy sharedInstance] registerDeviceToken:deviceToken];
  ```
- Call the registerForRemoteNotificationTypes: in your `application:didFinishLaunchingWithOptions`: method

  ```objc
    [[UIApplication sharedApplication] registerForRemoteNotificationTypes:
              (UIRemoteNotificationTypeAlert |
               UIRemoteNotificationTypeBadge |
               UIRemoteNotificationTypeSound)];
    [[AppboyUnityManager sharedInstance] addPushReceivedListenerWithObjectName:@"Your Unity Game Object Name" callbackMethodName:@"Your Unity Call Back Method Name"];
    [[AppboyUnityManager sharedInstance] addPushOpenedListenerWithObjectName:@"Your Unity Game Object Name" callbackMethodName:@"Your Unity Call Back Method Name"];
  ```
- In your app delegate, add the code below to your `application:didReceiveRemoteNotification` method:

#### Method to Count Opens while Foregrounded

Braze will use this code to determine if a push notification was opened. If the app is foregrounded and a push notification comes in, Braze will still count the open.

```objc
[[AppboyUnityManager sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo];
```

#### Alternate Method to Disregard Opens while Foregrounded

If you don't want to count opens for pushes that come in while the app is foregrounded use the following method instead:

```objc
UIApplicationState state = [application applicationState];
if (state != UIApplicationStateActive) {
 [[AppboyUnityManager sharedInstance] registerApplication:application
                 didReceiveRemoteNotification:userInfo];
}
```

### Step 2: Verify Code Modifications

Verify the code modifications you made against this [sample AppController.mm][15] file.

## Push Customization

### iOS Badge Counts

>  If badge counts are enabled, Braze will only clear the badge count when the app is opened directly from a Braze push notification. This is to avoid interfering with any other badges stemming from other notifications within the app.

### Manually Clearing the Badge Count

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

### Sample Braze Apple Push Payload

When Braze sends a push notification, the payload will look like this. You should avoid handling a top-level dictionary called `ab` in your application:

{% include {{ page.ex_push_payload}} %}

## Custom Sounds and Push

### Step 1: Hosting the Sound in the App

Custom push notification sounds must be hosted locally within the main bundle of the client application. The following audio data formats are accepted:

- Linear PCM
- MA4
- µLaw
- aLaw

You can package the audio data in an aiff, wav, or caf file. Then, in Xcode, add the sound file to your project as a nonlocalized resource of the application bundle.

You may use the afconvert tool to convert sounds. For example, to convert the 16-bit linear PCM system sound Submarine.aiff to IMA4 audio in a CAF file, use the following command in the Terminal application:

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

You can inspect a sound to determine its data format by opening it in QuickTime Player and choosing Show Movie Inspector from the Movie menu.

Custom sounds must be under 30 seconds when played. If a custom sound is over that limit, the default system sound is played instead.

### Step 2: Providing the Dashboard with a Protocol URL for the Sound

Your sound must be hosted locally within the app. You must specify a Protocol URL which directs to the location of the sound file in the app within the "Sound" field pictured below:

![Push Notification Sound][16]

For additional information see the Apple Developer Documentation regarding ["Preparing Custom Alert Sounds"][17] as well as our resources regarding the use of ["Protocol URLs."][18]

## Deep Linking to In-App Resources

See our documentation on [Deep Linking in iOS][18].

[1]: #manual-push-integration
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/ios/sdk_integration/#transitioning-from-manual-to-automated-integration
[3]: https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/TheAppLifeCycle/TheAppLifeCycle.html#//apple_ref/doc/uid/TP40007072-CH2-SW3
[4]: https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html
[5]: https://docs.unity3d.com/ScriptReference/iOS.NotificationServices.RegisterForNotifications.html
[6]: #disabling-automatic-push-registration
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/ios/sdk_integration/#step-2-setting-your-api-key
[9]: https://developer.apple.com/ios/manage/overview/index.action "iOS Provisioning Portal"
[10]: {% image_buster /assets/img_archive/ios_provisioning.png %} "pushNotification2.png"
[11]: {% image_buster /assets/img_archive/AppleProvisioningOptions.png %} "AppleProvisioningOptions.png"
[12]: {% image_buster /assets/img_archive/push_cert_gen.png %} "pushNotification3.png"
[13]: https://dashboard-01.braze.com/app_settings/app_settings
[14]: {% image_buster /assets/img_archive/push_cert_upload.png %} "push upload example image"
[15]: https://github.com/Appboy/appboy-unity-sdk/blob/master/unity-samples/iOS/Roll-A-Ball-Ios/Classes/UnityAppController.mm "sample AppController.mm"
[16]: {% image_buster /assets/img_archive/sound_push_ios.png %}
[17]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html#//apple_ref/doc/uid/TP40008194-CH4-SW10
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#deep-links
[19]: {% image_buster /assets/img_archive/ios_push_sample.png %}
[27]: {% image_buster /assets/img/unity/ios/unity_ios_api_key.png %}
[28]: {% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %}
[29]: {% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %}
[30]: {% image_buster /assets/img/unity/ios/unity_ios_push_received.png %}
[31]: {% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %}
[32]: {% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %}