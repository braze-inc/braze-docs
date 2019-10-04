---
nav_title: SDK Integration
platform: Unity
subplatform: Android
page_order: 0
---
# SDK Integration

Installing the Braze SDK will provide you with the ability to collect analytics and engage users with push messages and native in-app messages. Unity requires [the same support library version as the base Android SDK](https://github.com/Appboy/appboy-android-sdk#version-support).

## Step 1: Importing the Braze Unity Package

As of SDK v.1.8.0, the native Unity functionality and iOS libraries for Braze’s Unity plugin are bundled as a Unity package.

1. To import the provided Braze Unity package into your project, download the package associated with the [most recent SDK release][16]. There are two options:
	- `Appboy.unitypackage`
		- This package bundles the Braze Android and iOS SDKs as well as the [SDWebImage][17] dependency for the iOS SDK, which is required for proper functionality of Braze's In-App Messaging and News Feed features on iOS. The SDWebImage framework is used for downloading and displaying images, including GIFs. If you intend on utilizing full Braze functionality, download and import this package.
	- `Appboy-nodeps.unitypackage`
		- This package only bundles the Braze Android and iOS SDKs and the accompanying C# interface, which provides native Unity functionality for Braze's iOS plugin.
2. In the Unity Editor, import the package into your Unity project by navigating to Assets > Import Package > Custom Package.
3. Deselect any files you do not wish to import.
  - If you already have your own `AndroidManifest.xml`, please remember to uncheck the `AndroidManifest.xml` file during package importing to avoid overwriting your existing file. Plase refer to this file as a template for needed permissions in [here](https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Android/AndroidManifest.xml) on our public GitHub repo.
  - If you only wish to import the Android plugins, you only need to check the `Appboy` and `Android` subdirectories.
4. Click "Import".

Alternatively, Braze also provides the option of [customizing and exporting the Unity package][22].

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
	| __YES__ | `Assets/Plugins/Appboy/AppboyBinding.cs` | `/<your-project>/Assets/Plugins` |
	| __YES__ | `Assets/Plugins/Android` | `/<your-project>/Assets/Plugins/Android` |

## Step 2: Adding Your Bundle Identifier

### Part 1: Identifying Replacement Targets
To find all of the locations that must be modified to fully configure Braze for Android, run the following from the root directory of your Unity project:

```bash
grep -r REPLACE Assets/Plugins/
```

**Example output with successful plugin transfer:**

```bash
Android/AndroidManifest.xml:  <package="REPLACE_WITH_YOUR_BUNDLE_IDENTIFIER" android:versionCode="1" android:versionName="0.0">
Android/AndroidManifest.xml:  <uses-permission android:name="REPLACE_WITH_YOUR_BUNDLE_IDENTIFIER.permission.RECEIVE_ADM_MESSAGE" />
Android/AndroidManifest.xml:        <category android:name="REPLACE_WITH_YOUR_BUNDLE_IDENTIFIER" />
Android/AndroidManifest.xml:        <category android:name="REPLACE_WITH_YOUR_BUNDLE_IDENTIFIER" />
Android/AndroidManifest.xml:        <action android:name="REPLACE_WITH_YOUR_BUNDLE_IDENTIFIER.intent.APPBOY_NOTIFICATION_OPENED" />
Android/res/values/appboy.xml:  <string name="com_appboy_api_key">REPLACE_WITH_YOUR_APPBOY_API_KEY</string>
Android/res/values/appboy.xml:  <string translatable="false" name="com_appboy_firebase_cloud_messaging_sender_id">REPLACE_WITH_YOUR_FCM_SENDER_ID</string>
```

### Part 2: Replacing the Placeholders with your Bundle Identifier

1. Find your `Bundle Identifier` within Unity.
	- Click File -> Build Settings -> Player Settings -> Android Tab
	- The Player Settings pane looks like this in Unity 4:
	![Unity Bundle Identifier][2]

2. Open AndroidManifest.xml and find/replace all instances of `REPLACE_WITH_YOUR_BUNDLE_IDENTIFIER` with your `Bundle Identifier`.
	- Your `Bundle Identifier` is usually in the form `com.unity.appname`.
	- All Activity classes registered in your AndroidManifest.xml file should be fully integrated with the Braze Android SDK. If you add your own Activity class, you must follow Braze's usual [integration instructions][9] to ensure that analytics are being collected.

3. In `Plugins/Android/res/values/appboy.xml` replace all instances of `REPLACE_WITH_YOUR_APPBOY_API_KEY` with your Braze API key. Your API Key can be found in the [App Settings page of the Braze Dashboard][3]

4. To enable FCM push notifications, insert your FCM Sender ID from Google into the same `appboy.xml` configuration file. If you don't have a FCM Sender ID yet, you'll need to follow the FCM setup instructions from Google. Once you have the ID, change `REPLACE_WITH_YOUR_FCM_SENDER_ID` to your FCM Sender ID. Since the FCM Sender ID is a number, you shouldn't surround the value with quotes. Your ID should look something like `134664038331`.  For more information on integrating FCM, please visit our [FCM push integration instructions][12].

5. If it is not present already, make sure `AppboyOverlayActivity` is declared in your `AndroidManifest.xml`.

```
<activity android:name="com.appboy.unity.AppboyOverlayActivity" android:theme="@style/Appboy.Theme.Transparent" />
```

6. If the following lines are not present already, add the following lines to declare the Braze WebView and News Feed activities.  These will allow you to handle web urls and deep links to the News Feed via push and in-app messages:

```
<activity android:name="com.appboy.ui.AppboyWebViewActivity" android:theme="@android:style/Theme" />
<activity android:name="com.appboy.ui.activities.AppboyFeedActivity" android:theme="@android:style/Theme" />
```

## Advanced Android Integration Options

### Extending Braze's Unity Player

The default AndroidManifest.xml file provided has one Activity class registered, `com.appboy.unity.AppboyUnityPlayerActivity`.  This class is integrated with the Braze SDK and extends `UnityPlayerActivity` with session handling, in-app message registration, push notification analytics logging, and more.  

If you are creating your own custom `UnityPlayerActivity` in a library or plugin project, you will need to extend Braze's `AppboyUnityPlayerActivity` to integrate your custom functionality with Braze.

>  Before beginning work on extending `AppboyUnityPlayerActivity`, follow our instructions for integrating Braze into your Unity project.

1. Add the Braze Android SDK as a dependency to your library or plugin project as described in the first three steps of our [Android Studio integration instructions][14].

2. Integrate our Unity `.aar`, which contains Braze's Unity-specific functionality, to your Android library project you are building for Unity.  The `.aar` is available from our [public repo][15].  Once our Unity library is successfully integrated, modify your `UnityPlayerActivity` to extend `AppboyUnityPlayerActivity`.  

3. Export your library or plugin project and drop it into `/<your-project>/Assets/Plugins/Android` as normal.  Do not include any Braze source code in your library or plugin as they will already be present in `/<your-project>/Assets/Plugins/Android`.

4. Edit your `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` to specify your `AppboyUnityPlayerActivity` subclass as the main activity.

You should now be able to package an `.apk` from the Unity IDE that is fully integrated with Braze and contains your custom `UnityPlayerActivity` functionality.

### Prime 31 Compatibility

In order to use the Braze Unity plugin with Prime31 plugins, edit your project's `AndroidManifest.xml` to use the Prime31 compatible Activity classes. Change all references of
`com.appboy.unity.AppboyUnityPlayerActivity` to `com.appboy.unity.prime31compatible.AppboyUnityPlayerActivity`

### Disabling Native In-App Message Display

In-app messages from Braze's servers are automatically displayed natively.  To disable this functionality, set `com_appboy_inapp_show_inapp_messages_automatically` to `false` in your Unity project's `appboy.xml`.

### Amazon ADM Push

Braze supports integrating [Amazon ADM push][10] into Unity apps.  If you would like to integrate Amazon ADM push, create a file called `api_key.txt` containing your ADM api key and place it in the `Plugins/Android/assets/` folder.  For more information on integrating Amazon ADM with Braze, please visit our [ADM push integration instructions][11].

### Registering Unity GameObject as Listeners
Unity GameObjects must be registered as listeners in in your Unity project's `appboy.xml` to be notified of incoming in-app messages.

#### In-App Message GameObject Listeners
The Unity GameObject to be notified when an in-app message is received.
    `com_appboy_inapp_listener_game_object_name`
    `com_appboy_inapp_listener_callback_method_name`

**Sample appboy.xml Snippet:**

```xml
<string name="com_appboy_inapp_listener_game_object_name"></string>
<string name="com_appboy_inapp_listener_callback_method_name"></string>
```

## SDK Integration Complete

Braze should now be collecting data from your application and your basic integration should be complete. Please see the following sections in order to enable custom event tracking, push messaging, the news-feed and the complete suite of Braze features.

[1]: https://github.com/appboy/appboy-unity-sdk
[2]: {% image_buster /assets/img_archive/UnityBundleIdentifier.png %}
[3]: https://dashboard-01.braze.com/app_settings/app_settings/settings
[4]: {{ site.baseurl }}/app_group_configuration "dashboard setup api keys"
[5]: #clone-unity
[6]: #copy-plugins
[7]: #add-bundle-id
[9]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/
[10]: https://developer.amazon.com/public/apis/engage/device-messaging
[11]: {{ site.baseurl }}/developer_guide/platform_integration_guides/fireos/push_notifications/
[12]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/push_notifications/integration/
[13]: #android-advanced
[14]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/#using-android-studio
[15]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Android/libs/appboy-unity.aar
[16]: #extending-native
[17]: #prime-31
[18]: #adm-push
[19]: #game-objects
[20]: #inapp-disabling-native
[21]: https://github.com/Appboy/appboy-android-sdk/tree/master/android-sdk-ui/assets
[22]: {{ site.baseurl }}/developer_guide/platform_integration_guides/unity/z_advanced_use_cases/customizing_the_unity_package/#customizing-the-unity-package
