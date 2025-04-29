{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Setting up push notification

### Step 1: Set up the platform

{% tabs %}
{% tab Android %}
#### Step 1.1: Enable Firebase

To get started, follow the [Firebase Unity setup documentation](https://firebase.google.com/docs/unity/setup).

{% alert note %}
Integrating the Firebase Unity SDK may cause your `AndroidManifest.xml` to be overridden. If that occurs, make sure to revert it to the original.
{% endalert %}

#### Step 1.2: Set your Firebase credentials

You need to input your Firebase Server Key and Sender ID into the Braze dashboard. To do this, log in to the [Firebase Developers Console](https://console.firebase.google.com/) and select your Firebase project. Next, select **Cloud Messaging** under **Settings** and copy the Server Key and Sender ID:<br>![]({% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey")

In Braze, select your Android app on the **App Settings** page under **Manage Settings**. Next, enter your Firebase Server Key in the **Firebase Cloud Messaging Server Key** field and Firebase Sender ID in the **Firebase Cloud Messaging Sender** ID field.

![]({% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey")
{% endtab %}

{% tab Swift %}
#### Step 1.1: Verify integration method

Braze provides a native Unity solution for automating iOS push integrations. If you you'd like to set up and manage your integration manually instead, see [Swift: Push Notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

Otherwise, continue to the next step.

{% alert note %}
Our automatic push notification solution takes advantage of iOS 12's Provisional Authorization feature and is not available to use with the native push prompt pop-up.
{% endalert %}
{% endtab %}

{% tab Amazon Device Messaging %}
#### Step 1.1: Enable ADM

1. Create an account with the [Amazon Apps & Games Developer Portal](https://developer.amazon.com/public) if you have not already done so.
2. Obtain [OAuth credentials (Client ID and Client Secret) and an ADM API key](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. Enable **Automatic ADM Registration Enabled** in the Unity Braze Configuration window. 
  - Alternatively, you may add the following line to your `res/values/braze.xml` file to enable ADM registration:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```
{% endtab %}
{% endtabs %}

### Step 2: Configure push notifications

{% tabs %}
{% tab Android %}
#### Step 2.1: Configure push settings

The Braze SDK can automatically handle push registration with the Firebase Cloud Messaging Servers to have devices receive push notifications. In Unity, enable **Automate Unity Android Integration**, then configure the following **Push Notification** settings.

| Setting                                | Description                                                                                                                                              |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Automatic Firebase Cloud Messaging Registration Enabled | Instructs the Braze SDK to automatically retrieve and send an FCM push token for a device.                                                                |
| Firebase Cloud Messaging Sender ID     | The Sender ID from your Firebase console.                                                                                                                |
| Handle Push Deeplinks Automatically    | Whether the SDK should handle opening deep links or opening the app when push notifications are clicked.                                                  |
| Small Notification Icon Drawable       | The drawable should be displayed as the small icon whenever a push notification is received. The notification will use the application icon as the small icon if no icon is provided. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab Swift %}
#### Step 2.1: Upload your APNs token

{% multi_lang_include developer_guide/swift/apns_token.md %}

#### Step 2.2: Enable automatic push

Open the Braze Configuration Settings in the Unity Editor by navigating to **Braze > Braze Configuration**.

Check **Integrate Push With Braze** to automatically register users for push notifications, pass push tokens to Braze, track analytics for push opens, and take advantage of our default push notification handling.

#### Step 2.3: Enable background push (optional)

Check **Enable Background Push** if you want to enable `background mode` for push notifications. This allows the system to wake your application from the `suspended` state when a push notification arrives, enabling your application to download content in response to push notifications. Checking this option is required for our uninstall tracking functionality.

![The Unity editor shows the Braze configuration options. In this editor, the "Automate Unity iOS integration", "Integrate push with braze", and "Enable background push" are enabled.]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

#### Step 2.4: Disable automatic registration (optional)

Users who have not yet opted-in to push notifications will automatically be authorized for push upon opening your application. To disable this feature and manually register users for push, check **Disable Automatic Push Registration**.

- If **Disable Provisional Authorization** is not checked on iOS 12 or later, the user will be provisionally (silently) authorized to receive quiet push. If checked, the user will be shown the native push prompt.
- If you need to configure exactly when the prompt is shown at runtime, disable automatic registration from the Braze configuration editor and use `AppboyBinding.PromptUserForPushPermissions()` instead.

![The Unity editor shows the Braze configuration options. In this editor, the "Automate Unity iOS integration", "integrate push with braze", and "disable automatic push registration" are enabled.]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})
{% endtab %}

{% tab Amazon Device Messaging %}
#### Step 2.1: Update `AndroidManifest.xml`

If your app does not have an `AndroidManifest.xml`, you can use the following as a template. Otherwise, if you already have an `AndroidManifest.xml`, ensure that any of the following missing sections are added to your existing `AndroidManifest.xml`.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />
  <permission
    android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE" />
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity" 
      android:label="@string/app_name" 
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen" 
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <receiver android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver" android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
          <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
          <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
          <category android:name="REPLACE_WITH_YOUR_PACKAGE_NAME" />
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

#### Step 2.2: Store your ADM API key

First, [generate an ADM API Key for your app](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials), then save the key to a file named `api_key.txt` and add it in your project's [`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) directory.

{% alert important %}
Amazon will not recognize your key if `api_key.txt` contains any white space characters, such as a trailing line break.
{% endalert %}

Next, in your `mainTemplate.gradle` file, add the following:

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

#### Step 2.3: Add ADM Jar

The required ADM Jar file may be placed anywhere in your project according to the [Unity JAR documentation](https://docs.unity3d.com/Manual/AndroidJARPlugins.html).

#### Step 2.4: Add Client Secret and Client ID to your Braze dashboard

Lastly, you must add the Client Secret and Client ID you obtained in [Step 1](#unity_step-1-enable-adm) to the Braze dashboard's **Manage Settings** page.

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})
{% endtab %}
{% endtabs %}

### Step 3: Set push listeners

{% tabs %}
{% tab Android %}
#### Step 3.1: Enable push received listener

The push received listener is fired when a user receives a push notification. To send the push payload to Unity, set the name of your game object and push the received listener callback method under the **Set Push Received Listener**.

#### Step 3.2: Enable push opened listener

The push opened listener is fired when a user launches the app by clicking on a push notification. To send the push payload to Unity, set the name of your game object and push opened listener callback method under the **Set Push Opened Listener**.

#### Step 3.3: Enable push deleted listener

The push deleted listener is fired when a user swipes away or dismisses a push notification. To send the push payload to Unity, set the name of your game object and push deleted listener callback method under the **Set Push Deleted Listener**.

#### Push listener example

The following example implements the `BrazeCallback` game object using a callback method name of `PushNotificationReceivedCallback`, `PushNotificationOpenedCallback`, and `PushNotificationDeletedCallback` respectively.

![This implementation example graphic shows the Braze configuration options mentioned in the preceding sections and a C# code snippet.]({% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Android Full Listener Example")

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
{% endtab %}

{% tab Swift %}
#### Step 3.1: Enable push received listener

The push received listener is fired when a user receives a push notification while actively using the application (such as when the app is foregrounded). Set the push received listener in the Braze configuration editor. If you need to configure your game object listener at runtime, use `AppboyBinding.ConfigureListener()` and specify `BrazeUnityMessageType.PUSH_RECEIVED`.

![The Unity editor shows the Braze configuration options. In this editor, the "Set Push Received Listener" option is expanded, and the "Game Object Name" (AppBoyCallback) and "Callback Method Name" (PushNotificationReceivedCallback) are provided.]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

#### Step 3.2: Enable push opened listener

The push opened listener is fired when a user launches the app by clicking on a push notification. To send the push payload to Unity, set the name of your game object and push opened listener callback method under the **Set Push Opened Listener** option:

![The Unity editor shows the Braze configuration options. In this editor, the "Set Push Received Listener" option is expanded, and the "Game Object Name" (AppBoyCallback) and "Callback Method Name" (PushNotificationOpenedCallback) are provided.]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

If you need to configure your game object listener at runtime, use `AppboyBinding.ConfigureListener()` and specify `BrazeUnityMessageType.PUSH_OPENED`.

#### Push listener example

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
{% endtab %}

{% tab Amazon Device Messaging %}
By updating your `AndroidManifest.xml` in the [previous step](#unity_step-21-update-androidmanifestxml), push listeners were automatically set up when you added the following lines. So, no further setup is required.

```xml
<action android:name="com.amazon.device.messaging.intent.RECEIVE" />
<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
```

{% alert note %}
To learn more about ADM push listeners, see [Amazon: Integrate Amazon Device Messaging](https://developer.amazon.com/docs/video-skills-fire-tv-apps/integrate-adm.html).
{% endalert %}
{% endtab %}
{% endtabs %}

## Optional configurations

{% tabs %}
{% tab Android %}
#### Deep linking to in-app resources

Although Braze can handle standard deep links (such as website URLs, Android URIs, etc.) by default, creating custom deep links requires an additional Manifest setup.

For setup guidance, visit [Deep Linking to In-App Resources](https://developer.android.com/training/app-links/deep-linking).

#### Adding Braze push notification icons

To add push icons to your project, create an Android Archive (AAR) plug-in or Android library that contains the icon image files. For steps and information, refer to Unity's documentation: [Android Library Projects and Android Archive plug-ins](https://docs.unity3d.com/Manual/AndroidAARPlugins.html).
{% endtab %}

{% tab Swift %}
#### Push token callback

To receive a copy of Braze device tokens from the OS, set a delegate using `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`.
{% endtab %}

{% tab Amazon Device Messaging %}
There are no optional configurations for ADM at this time.
{% endtab %}
{% endtabs %}
