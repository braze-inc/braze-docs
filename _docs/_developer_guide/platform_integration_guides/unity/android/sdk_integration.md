---
nav_title: SDK Integration
platform: Unity
subplatform: Android
page_order: 0
---
# SDK Integration

Installing the Braze SDK will provide you with the ability to collect analytics and engage users with push messages and native in-app messages.

## Step 1: Choosing A Braze Unity Package

The Braze [`.unitypackage`][26] bundles native bindings for the Android and iOS platforms, along with a Unity C# interface.

There are several Braze Unity packages available for download at [Braze Unity Releases Page][16]:
 
{% include archive/unity/unitypackage_descriptions.md%}

## Step 2: Importing a Braze Unity Package

1. In the Unity Editor, import the package into your Unity project by navigating to `Assets > Import Package > Custom Package`.
2. Click "Import".

Alternatively, follow the Unity instructions for [Importing Asset packages][26] for a more detailed guide on importing custom Unity packages. 

Braze also provides the option of [customizing and exporting the Unity package][22].

{% alert note %}
If you only wish to import the Android plugin, deselect the `Plugins/iOS` subdirectory when importing the Braze `.unitypackage`.
{% endalert %}

## Step 3: Updating your AndroidManifest.xml

Android Unity projects require an [`AndroidManifest.xml`][29] to be present to run the application. Additionally, Braze requires several additions to your [`AndroidManifest.xml`][29] in order to function.

### Part 1: Configuring the AndroidManifest.xml

If your app does not have an `AndroidManifest.xml`, you can use the following as a template. Otherwise, if you already have an `AndroidManifest.xml`, ensure that any missing sections below are added to your existing `AndroidManifest.xml`.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.appboy.unity.AppboyUnityPlayerActivity" 
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

    <!-- A Braze specific FirebaseMessagingService used to handle push notifications. -->
    <service android:name="com.appboy.AppboyFirebaseMessagingService"
      android:exported="false">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>

    <!-- BroadcastReceiver used to forward certain Braze push notification events to Unity -->
    <receiver android:name="com.appboy.unity.AppboyUnityPushBroadcastReceiver" android:exported="false" >
      <intent-filter>
        <action android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.intent.APPBOY_PUSH_RECEIVED" />
        <action android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.intent.APPBOY_NOTIFICATION_OPENED" />
        <action android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.intent.APPBOY_PUSH_DELETED" />
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

> Your `AndroidManifest.xml` should exist under `Assets/Plugins/Android/AndroidManifest.xml`. Please see [the Unity AndroidManifest documentation][29] for more information.

> All Activity classes registered in your `AndroidManifest.xml` file should be fully integrated with the Braze Android SDK. If you add your own Activity class, you must follow [Braze's Unity Activity integration instructions][34] to ensure that analytics are being collected.

### Part 2: Finding your Package Name 

- Click File -> Build Settings -> Player Settings -> Android Tab
- The Player Settings pane looks like this in Unity 2019:
![Unity Package Name][2]

### Part 3: Make Replacements in the AndroidManifest

In your `AndroidManifest.xml`, all instances of `REPLACE_WITH_YOUR_PACKAGE_NAME` should be replaced with your `Package Name` from the previous step.

## Step 4: Configure the SDK {#unity-static-configuration}
Braze provides a native Unity solution for automating the Unity Android integration. This solution modifies the built Gradle project using Unity's [`OnPostGenerateGradleAndroidProject`][35] and auto-generates a resource file called `/unity-android-resources/res/values/appboy-generated.xml` in your temporary `gradleOut` directory.

1. In the Unity Editor, open the Braze Configuration Settings by navigating to Braze > Braze Configuration.
2. Check the "Automate Unity Android Integration" box.
3. In the "Braze API Key" field, input your application's API key from the Braze Dashboard.

>  Your Braze API key can be found within the App Settings page of the Braze dashboard. To find out your specific cluster or endpoint, please ask your Customer Success Manager or [open a support ticket][30].

{% alert note %}
This automatic integration should not be used in conjunction with a manually created `braze.xml` file since the configuration values may conflict during project building.
{% endalert %}

## Advanced Android Integration Options

### Extending Braze's Unity Player {#extending-braze-unity-player}

The default `AndroidManifest.xml` file provided has one Activity class registered, [`AppboyUnityPlayerActivity`][32]. This class is integrated with the Braze SDK and extends `UnityPlayerActivity` with session handling, in-app message registration, push notification analytics logging, and more. See [this documentation][33] for more information on extending the `UnityPlayerActivity` class.

If you are creating your own custom `UnityPlayerActivity` in a library or plugin project, you will need to extend Braze's `AppboyUnityPlayerActivity` to integrate your custom functionality with Braze.

>  Before beginning work on extending `AppboyUnityPlayerActivity`, follow our instructions for integrating Braze into your Unity project.

1. Add the Braze Android SDK as a dependency to your library or plugin project as described in the first three steps of our [Android Studio integration instructions][14].

2. Integrate our Unity `.aar`, which contains Braze's Unity-specific functionality, to your Android library project you are building for Unity. The `appboy-unity.aar` (or `appboy-unity-jetified.aar` if using `androidX` dependencies) is available from our [public repo][15]. Once our Unity library is successfully integrated, modify your `UnityPlayerActivity` to extend `AppboyUnityPlayerActivity`.

3. Export your library or plugin project and drop it into `/<your-project>/Assets/Plugins/Android` as normal.  Do not include any Braze source code in your library or plugin as they will already be present in `/<your-project>/Assets/Plugins/Android`.

4. Edit your `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` to specify your `AppboyUnityPlayerActivity` subclass as the main activity.

You should now be able to package an `.apk` from the Unity IDE that is fully integrated with Braze and contains your custom `UnityPlayerActivity` functionality.

### Prime 31 Compatibility

In order to use the Braze Unity plugin with Prime31 plugins, edit your project's `AndroidManifest.xml` to use the Prime31 compatible Activity classes. Change all references of
`com.appboy.unity.AppboyUnityPlayerActivity` to `com.appboy.unity.prime31compatible.AppboyUnityPlayerActivity`

### Disabling Native In-App Message Display

In-app messages from Braze's servers are automatically displayed natively. To disable this functionality, set `com_appboy_inapp_show_inapp_messages_automatically` to `false` in your Unity project's `braze.xml`.

### Amazon ADM Push

Braze supports integrating [Amazon ADM push][10] into Unity apps. If you would like to integrate Amazon ADM push, create a file called `api_key.txt` containing your ADM API key and place it in the `Plugins/Android/assets/` folder.  For more information on integrating Amazon ADM with Braze, please visit our [ADM push integration instructions][11].

### Receiving In-App Message Data in Unity

Unity Game Objects may be registered in your Unity project's `braze.xml` to be notified of incoming in-app messages.

Sample `braze.xml` Snippet:

```xml
<string name="com_appboy_inapp_listener_game_object_name"></string>
<string name="com_appboy_inapp_listener_callback_method_name"></string>
```

The method `InAppMessageReceivedCallback` in our [sample callback code][8] shows an example of parsing incoming in-app message data.

```csharp
void InAppMessageReceivedCallback(string message) {
  Debug.Log("InAppMessageReceivedCallback message: " + message);
  IInAppMessage inApp = InAppMessageFactory.BuildInAppMessage(message);
  Debug.Log("In-app message received: " + inApp);
  // Here we are testing the Unity SDK by manually logging the in-app message's click and impression.
  // We should only log the click and impression when the in-app message isn't displayed by Appboy but in Unity.
  //inApp.LogClicked();
  //inApp.LogImpression();
  if (inApp is IInAppMessageImmersive) {
    IInAppMessageImmersive inAppImmersive = inApp as IInAppMessageImmersive;
    if (inAppImmersive.Buttons != null && inAppImmersive.Buttons.Count > 0) {
      // Here we are testing the Unity SDK by manually logging the in-app message's first button's click.
      // We should only log the button click when the in-app message isn't displayed by Appboy but in Unity.
      //inAppImmersive.LogButtonClicked(inAppImmersive.Buttons[0].ButtonID);
    }
  }
}
```

### Receiving Content Card Data in Unity

Unity Game Objects may be registered in your Unity project's `braze.xml` to be notified of incoming Content Cards.

Sample `braze.xml` Snippet:

```xml
<string name="com_appboy_content_cards_updated_listener_game_object_name"></string>
<string name="com_appboy_content_cards_updated_listener_callback_method_name"></string>
```

The method `ContentCardsReceivedCallback` in our [sample callback code][8] shows an example of parsing incoming Content Card data into our convenience wrapper class for Content Cards, [`ContentCard.cs`][23]. `ContentCard.cs` also supports logging analytics through its `LogImpression()` and `LogClick()` methods.

Sample code for parsing incoming Content Card data:

```csharp
void ExampleCallback(string message) {
  // Example of logging a Content Card displayed event
  AppboyBinding.LogContentCardsDisplayed();
  try {
    JSONClass json = (JSONClass)JSON.Parse(message);

    // Content Card data is contained in the `mContentCards` field of the top level object.
    if (json["mContentCards"] != null) {
      JSONArray jsonArray = (JSONArray)JSON.Parse(json["mContentCards"].ToString());
      Debug.Log(String.Format("Parsed content cards array with {0} cards", jsonArray.Count));

      // Iterate over the card array to parse individual cards.
      for (int i = 0; i < jsonArray.Count; i++) {
        JSONClass cardJson = jsonArray[i].AsObject;
        try {
          ContentCard card = new ContentCard(cardJson);
          Debug.Log(String.Format("Created card object for card: {0}", card));

          // Example of logging Content Card analytics on the ContentCard object 
          card.LogImpression();
          card.LogClick();
        } catch {
          Debug.Log(String.Format("Unable to create and log analytics for card {0}", cardJson));
        }
      }
    }
  } catch {
    throw new ArgumentException("Could not parse content card JSON message.");
  }
}
```

### Manually Copying Required Plugins

If you do not wish to import the Unity package, you may also manually copy the plugins into your Unity project.

1. Clone the [Braze Unity SDK Github project][1]

  ```bash
  git clone git@github.com:Appboy/appboy-unity-sdk.git
  ```
2. Copy the required Braze plugins into your Unity project

  | Are you using other plugins? | What to Copy | Where to Copy |
  | ---------------------------- | ------------ | ------------- |
  | __NO__ | the `Assets/Plugins` directory from the Unity SDK | the `Assets` folder of your Unity Project |
  | __YES__ | `Assets/Plugins/Appboy` | `/<your-project>/Assets/Plugins/Appboy` |
  | __YES__ | `Assets/Plugins/Android` | `/<your-project>/Assets/Plugins/Android` |

### Configure the SDK in XML {#unity-android-xml-configuration}

A static configuration file called `braze.xml` can be used to configure the Braze Android SDK. This file should exist under `Assets/Plugins/Android/res/values/braze.xml`.

#### Part 1: Adding The XML File

If your app does not have an `braze.xml`, you can use the following as a template. Otherwise, if you already have an `braze.xml`, ensure that any missing sections below are added to your existing `braze.xml`.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- General configuration -->
  <string name="com_appboy_api_key">REPLACE_WITH_YOUR_BRAZE_API_KEY</string>

  <!-- FCM Push Notification configuration (optional) -->
  <bool translatable="false" name="com_appboy_firebase_cloud_messaging_registration_enabled">true</bool>
  <string translatable="false" name="com_appboy_firebase_cloud_messaging_sender_id">REPLACE_WITH_YOUR_FCM_SENDER_ID</string>

  <!-- Push deep link configuration (optional) -->
  <bool name="com_appboy_handle_push_deep_links_automatically">true</bool> <!-- Whether to open push deep links from Braze automatically. -->

  <!-- In-app message configuration (optional) -->
  <bool name="com_appboy_inapp_show_inapp_messages_automatically">true</bool> <!-- Whether to display in-app messages from Braze using the Braze native UI. -->

  <!-- A custom endpoint, IF applicable. Please ask your Customer Success Manager if this applies to your integration -->
  <!-- <string translatable="false" name="com_appboy_custom_endpoint"></string> -->

  <!-- Optional -->
  <!-- <string name="com_appboy_inapp_listener_game_object_name"></string> --> <!-- The Unity game object to receive inapp messages. -->
  <!-- <string name="com_appboy_inapp_listener_callback_method_name"></string> --> <!-- The callback method to be called when an inapp message is received. -->
  <!-- <string name="com_appboy_feed_listener_game_object_name"></string> --> <!-- The Unity game object to receive the news feed. -->
  <!-- <string name="com_appboy_feed_listener_callback_method_name"></string> --> <!-- The callback method to be called when the news feed is received. -->
  <!-- <string name="com_appboy_content_cards_updated_listener_game_object_name"></string> --> <!-- The Unity game object to receive Content Cards. -->
  <!-- <string name="com_appboy_content_cards_updated_listener_callback_method_name"></string> --> <!-- The callback method to be called when Content Cards are received. -->
  <!-- <string name="com_appboy_push_received_game_object_name"></string> --> <!-- The Unity game object to receive push received messages. -->
  <!-- <string name="com_appboy_push_received_callback_method_name"></string> --> <!-- The callback method to be called when a push received message is received. -->
  <!-- <string name="com_appboy_push_opened_game_object_name"></string> --> <!-- The Unity game object to receive push opened messages. -->
  <!-- <string name="com_appboy_push_opened_callback_method_name"></string> --> <!-- The callback method to be called when a push opened message is received. -->
  <!-- <string name="com_appboy_push_deleted_game_object_name"></string> --> <!-- The Unity game object to receive push deleted messages. -->
  <!-- <string name="com_appboy_push_deleted_callback_method_name"></string> --> <!-- The callback method to be called when a push deleted message is received. -->

  <!--- Internal Braze Usage -->
  <string name="com_appboy_sdk_flavor">UNITY</string>
</resources>
```

#### Part 2: Make Replacements in braze.xml

* Replace `REPLACE_WITH_YOUR_BRAZE_API_KEY` with your Braze API Key.
* Replace `REPLACE_WITH_YOUR_FCM_SENDER_ID` with your Firebase Messaging Sender ID. Please see [Registering for Push][31] for more information.

>  Your Braze API key can be found within the App Settings page of the Braze dashboard. To find out your specific cluster or endpoint, please ask your Customer Success Manager or [open a support ticket][30].

#### Part 3: Configure ADM in braze.xml (optional)

If using ADM, please add the following to your `braze.xml`:

```xml
<bool name="com_appboy_push_adm_messaging_registration_enabled">true</bool> <!-- Whether or not Braze should handle registering the device to receive ADM push notifications. Default is false. -->
<bool translatable="false" name="com_appboy_firebase_cloud_messaging_registration_enabled">false</bool>
```

## SDK Integration Complete

Braze should now be collecting data from your application and your basic integration should be complete. Please see the following sections in order to enable custom event tracking, push messaging, the news-feed and the complete suite of Braze features.

[1]: https://github.com/appboy/appboy-unity-sdk
[2]: {% image_buster /assets/img_archive/UnityPackageName.png %}
[8]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/Tests/AppboyBindingTester.cs
[10]: https://developer.amazon.com/public/apis/engage/device-messaging
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/fireos/push_notifications/integration/
[14]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/
[15]: https://github.com/Appboy/appboy-unity-sdk/tree/master/Assets/Plugins/Android
[16]: https://github.com/Appboy/appboy-unity-sdk/releases
[22]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/Advanced_Use_Cases/customizing_the_unity_package/
[23]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/Cards/ContentCard.cs
[26]: https://docs.unity3d.com/Manual/AssetPackages.html
[29]: https://docs.unity3d.com/Manual/android-manifest.html
[30]: {{site.baseurl}}/support_contact/
[31]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/#registering-for-push
[32]: https://github.com/Appboy/appboy-android-sdk/blob/e67e09f785adeff075a5d7710e79f41ed3676a6a/android-sdk-unity/src/main/java/com/appboy/unity/AppboyUnityPlayerActivity.java
[33]: https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html
[34]: #extending-braze-unity-player
[35]: https://docs.unity3d.com/ScriptReference/Android.IPostGenerateGradleAndroidProject.html
