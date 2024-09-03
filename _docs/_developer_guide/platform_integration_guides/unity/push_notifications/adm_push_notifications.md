---
nav_title: Amazon Device Messaging
article_title: Amazon Device Messaging Push Notifications for Unity
platform: 
  - Unity
  - Android
page_order: 2
description: "This reference article covers the Amazon Android push notification integration for the Unity platform."
channel: push

---

# Amazon Device Messaging

> This reference article covers the Amazon Android push notification integration for the Unity platform.

A push notification is an out-of-app alert that appears on the user's screen when an important update occurs. Push notifications are a valuable way to provide your users with time-sensitive and relevant content or to re-engage them with your app.

ADM (Amazon Device Messaging) is not supported on non-Amazon devices. To test Kindle push, you must have a [FireOS device](https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm). Check out the [help section]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/troubleshooting/) for additional best practices.

Braze sends push notifications to Amazon devices using [Amazon Device Messaging (ADM)](https://developer.amazon.com/public/apis/engage/device-messaging).

## Step 1: Enable ADM

1. Create an account with the [Amazon Apps & Games Developer Portal](https://developer.amazon.com/public) if you have not already done so.
2. Obtain [OAuth credentials (Client ID and Client Secret) and an ADM API key](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. Enable **Automatic ADM Registration Enabled** in the Unity Braze Configuration window. 
  - Alternatively, you may add the following line to your `res/values/braze.xml` file to enable ADM registration:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```

## Step 2: Update Unity AndroidManifest.xml

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

## Step 3: Store your ADM API key

First, [obtain an ADM API Key for your app](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).  Next, save your ADM API key to a file named `api_key.txt` and save it in your project's [`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) folder.

Amazon will not recognize your key if `api_key.txt` contains any white space characters, such as a trailing line break.

In your `mainTemplate.gradle` file, add the following:

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

## Step 4: Add ADM Jar

The required ADM Jar file may be placed anywhere in your project according to the [Unity JAR documentation](https://docs.unity3d.com/Manual/AndroidJARPlugins.html).

## Step 5: Add Client Secret and Client ID to your Braze dashboard

Lastly, you must add the Client Secret and Client ID you obtained in [Step 1](#step-1-enable-adm) to the Braze dashboard's **Manage Settings** page.

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})

