---
nav_title: Android
article_title: SDK Android Integration for Unity
platform: 
  - Unity
  - Android
page_order: 0
description: "This reference article covers the Android SDK integration for the Unity platform."

---

# SDK Android integration

Follow these instructions to get Braze running in your Unity application.

## Step 1: Choose your Braze Unity package

The Braze [`.unitypackage`][41] bundles native bindings for the Android and iOS platforms, along with a C# interface.

There are several Braze Unity packages available for download on the [Braze Unity releases page][42]:
 
- `Appboy.unitypackage`
    - This package bundles the Braze Android and iOS SDKs and the [SDWebImage][unity-1] dependency for the iOS SDK, which is required for the proper functionality of Braze's In-App Messaging, and Content Cards features on iOS. The SDWebImage framework is used for downloading and displaying images, including GIFs. If you intend on utilizing full Braze functionality, download and import this package.
- `Appboy-nodeps.unitypackage`
    - This package is similar to `Appboy.unitypackage` except for the [SDWebImage][unity-1] framework is not present. This package is useful if you do not want the SDWebImage framework present in your iOS app.

**iOS**: To see if you require the [SDWebImage][unity-1] dependency for your iOS project, visit the [iOS in-app message documentation][unity-4].<br>
**Android**: As of Unity 2.6.0, the bundled Braze Android SDK artifact requires  [AndroidX][unity-3] dependencies. If you were previously using a `jetified unitypackage`, then you can safely transition to the corresponding `unitypackage`.

## Step 2: Import the package

In the Unity Editor, import the package into your Unity project by navigating to **Assets > Import Package > Custom Package**. Next, click **Import**.

Alternatively, follow the [Unity asset package import][41] instructions for a more detailed guide on importing custom Unity packages. 

{% alert note %}
If you only wish to import the iOS or Android plugin, deselect the `Plugins/Android` or `Plugins/iOS` subdirectory when importing the Braze `.unitypackage`.
{% endalert %}

## Step 3: Updating your AndroidManifest.xml

Android Unity projects require an [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) to be present to run the application. Additionally, Braze requires several additions to your [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) to function.

### Configuring the AndroidManifest.xml

If your app does not have an `AndroidManifest.xml`, you can use the following as a template. Otherwise, if you already have an `AndroidManifest.xml`, ensure that any of the following missing sections are added to your existing `AndroidManifest.xml`.

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
    <service android:name="com.braze.push.BrazeFirebaseMessagingService"
      android:exported="false">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>

    <!-- BroadcastReceiver used to forward certain Braze push notification events to Unity -->
    <receiver android:name="com.appboy.unity.AppboyUnityPushBroadcastReceiver" android:exported="false" >
      <intent-filter>
        <action android:name="com.braze.push.intent.NOTIFICATION_OPENED" />
        <action android:name="com.braze.push.intent.NOTIFICATION_RECEIVED" />
        <action android:name="com.braze.push.intent.NOTIFICATION_DELETED" />
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

> Your `AndroidManifest.xml` should exist under `Assets/Plugins/Android/AndroidManifest.xml`. See the [Unity AndroidManifest documentation](https://docs.unity3d.com/Manual/android-manifest.html) for more information.

> All Activity classes registered in your `AndroidManifest.xml` file should be fully integrated with the Braze Android SDK. If you add your own Activity class, you must follow Braze's [Unity Activity integration instructions](#extending-braze-unity-player) to ensure that analytics are being collected.

{% alert note %}
Your final `AndroidManifest.xml` should only contain a single Activity with `"android.intent.category.LAUNCHER"` present.
{% endalert %}

### Update the AndroidManifest.xml with your package name

To find your package name, click **File > Build Settings > Player Settings > Android Tab**.
![]({% image_buster /assets/img_archive/UnityPackageName.png %})

In your `AndroidManifest.xml`, all instances of `REPLACE_WITH_YOUR_PACKAGE_NAME` should be replaced with your `Package Name` from the previous step.

## Step 4: Add gradle dependencies {#unity-android-gradle-configuration}

The following dependencies are required:

```groovy
implementation "org.jetbrains.kotlin:kotlin-stdlib:1.5.21"
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.5.2"

// Both are required if using the default Content Cards Activity on Android
implementation "androidx.swiperefreshlayout:swiperefreshlayout:+"
implementation "androidx.recyclerview:recyclerview:+"
```

The following list examples of how to add these dependencies using Unity tools:

##### [Custom Gradle template](https://docs.unity3d.com/Manual/android-gradle-overview.html)

```groovy
dependencies {
  implementation "org.jetbrains.kotlin:kotlin-stdlib:1.5.21"
  implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.5.2"
}
```
##### [External dependency manager for Unity](https://github.com/googlesamples/unity-jar-resolver)

```xml
<dependencies>
  <androidPackages>
    <androidPackage spec="org.jetbrains.kotlin:kotlin-stdlib:1.5.21" />
    <androidPackage spec="org.jetbrains.kotlinx:kotlinx-coroutines-android:1.5.2" />
  </androidPackages>
</dependencies>
```

## Step 5: Configure the SDK {#unity-static-configuration}

Braze provides a native Unity solution for automating the Unity Android integration. 

1. In the Unity Editor, open the Braze Configuration Settings by navigating to **Braze > Braze Configuration**.
2. Check the **Automate Unity Android Integration** box.
3. In the "Braze API Key" field, input your application's API key found in **Manage Settings** from the Braze dashboard.

{% alert note %}
This automatic integration should not be used with a manually created `braze.xml` file since the configuration values may conflict during project building. If you require a manual `braze.xml`, disable the automatic integration.
{% endalert %}

## Basic SDK integration complete

Braze should now be collecting data from your application, and your basic integration should be complete. Check out the following articles for more information on integrating push ([Android][53] and [iOS][50]), [in-app messages][34], [Content Cards][40], and [News Feed][35].

## Additional advanced implementation options

### Extending Braze's Unity player (Android) {#extending-braze-unity-player}

The example `AndroidManifest.xml` file provided has one Activity class registered, [`AppboyUnityPlayerActivity`](https://github.com/Appboy/appboy-android-sdk/blob/e67e09f785adeff075a5d7710e79f41ed3676a6a/android-sdk-unity/src/main/java/com/appboy/unity/AppboyUnityPlayerActivity.java). This class is integrated with the Braze SDK and extends `UnityPlayerActivity` with session handling, in-app message registration, push notification analytics logging, and more. See [Unity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html) for more information on extending the `UnityPlayerActivity` class.

If you are creating your own custom `UnityPlayerActivity` in a library or plugin project, you will need to extend Braze's `AppboyUnityPlayerActivity` to integrate your custom functionality with Braze. Before beginning work on extending `AppboyUnityPlayerActivity`, follow our instructions for integrating Braze into your Unity project.
1. Add the Braze Android SDK as a dependency to your library or plugin project as described in the [Braze Android SDK integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/).
2. Integrate our Unity `.aar`, which contains Braze's Unity-specific functionality, to your Android library project you are building for Unity. The `appboy-unity.aar` is available from our [public repo](https://github.com/Appboy/appboy-unity-sdk/tree/master/Assets/Plugins/Android). Once our Unity library is successfully integrated, modify your `UnityPlayerActivity` to extend `AppboyUnityPlayerActivity`.
3. Export your library or plugin project and drop it into `/<your-project>/Assets/Plugins/Android` as normal. Do not include any Braze source code in your library or plugin as they will already be present in `/<your-project>/Assets/Plugins/Android`.
4. Edit your `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` to specify your `AppboyUnityPlayerActivity` subclass as the main activity.

You should now be able to package an `.apk` from the Unity IDE that is fully integrated with Braze and contains your custom `UnityPlayerActivity` functionality.

[5]: #transitioning-from-manual-to-automated-integration
[34]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/news_feed/
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/
[41]: https://docs.unity3d.com/Manual/AssetPackages.html
[42]: https://github.com/Appboy/appboy-unity-sdk/releases
[50]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/
[53]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/
[unity-1]: https://github.com/SDWebImage/SDWebImage
[unity-2]: https://firebase.google.com/docs/unity/setup
[unity-3]: https://developer.android.com/jetpack/androidx
[unity-4]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/
