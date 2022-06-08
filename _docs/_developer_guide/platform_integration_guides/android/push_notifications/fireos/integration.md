---
nav_title: Integration
article_title: Push Integration for FireOS
platform: FireOS
page_order: 0
page_type: solution
description: "This article walks you through how to integrate Braze push notifications in your FireOS application."
channel: push

---

# Integration

A push notification is an out-of-app alert that appears on the user's screen when an important update occurs. Push notifications are a valuable way to provide your users with time-sensitive and relevant content to re-engage them with your app.

ADM (Amazon Device Messaging) is not supported on non-Amazon devices. To test Kindle push, you must have a [FireOS device][32]. Check out our [help article][8] for additional best practices.

Braze sends push notifications to Amazon devices using [Amazon Device Messaging (ADM)][14].

## Step 1: Enable ADM

1. Create an account with the [Amazon Apps & Games Developer Portal][10] if you have not already done so.
2. Obtain [OAuth credentials (Client ID and Client Secret) and an ADM API key][11].
3. Enable **Automatic ADM Registration Enabled** in the Unity Braze Configuration window. 
  - Alternatively, you may add the following line to your `res/values/braze.xml` file to enable ADM registration:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```

## Step 2: Update AndroidManifest.xml

In your app's AndroidManifest.xml, add Amazon's namespace to the `<>manifest</>` tag:

```xml
  xmlns:amazon="http://schemas.amazon.com/apk/res/android"
```

Next, declare permissions required to support ADM by adding `<>permission</>` and `<>uses-permission</>` elements after the `<>manifest</> element`:

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:amazon="http://schemas.amazon.com/apk/res/android"
    package="[YOUR PACKAGE NAME]"
    android:versionCode="1"
    android:versionName="1.0">

  <!-- This permission ensures that no other application can intercept your ADM messages. -->
  <permission
    android:name="[YOUR PACKAGE NAME].permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="[YOUR PACKAGE NAME].permission.RECEIVE_ADM_MESSAGE" />

   <!-- This permission allows your app access to receive push notifications from ADM. -->
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <!-- ADM uses WAKE_LOCK to keep the processor from sleeping when a message is received. -->
  <uses-permission android:name="android.permission.WAKE_LOCK" />
    ...
  </manifest>
```

Next, declare that your app uses the device's ADM feature and that your app is designed to remain functional without ADM present on the device (`android:required="false"`) by adding an `amazon:enable-feature` element to the manifest's application element. It is safe to set `android:required` as `"false"` because Braze ADM code degrades gracefully when ADM is not present on the device:

  ```xml
  ...
  <application
    android:icon="@drawable/ic_launcher"
    android:label="@string/app_name"
    android:theme="@style/AppTheme">

    <amazon:enable-feature android:name="com.amazon.device.messaging" android:required="false"/>
  ...
  ```

Lastly, add intent filters to handle `REGISTRATION` and `RECEIVE` intents from ADM within your Braze broadcast receiver's `AndroidManifest.xml` file. Immediately after `amazon:enable-feature`, add the following elements:

```xml
<receiver android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver" android:permission="com.amazon.device.messaging.permission.SEND">
  <intent-filter>
      <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
      <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
      <category android:name="com.yourapp.packagename" />
  </intent-filter>
</receiver>
```

## Step 3: Store your ADM API key

First, save your ADM API key to a file named `api_key.txt` and save it in your project's [`Assets/Plugins/Android/assets`][54] folder. Next, [obtain an ADM API Key for your app][11].

Amazon will not recognize your key if `api_key.txt` contains any white space characters, such as a trailing line break.

## Step 4: Add deep links

#### Enabling automatic deep link opening

To enable Braze to automatically open your app and any deep links when a push notification is clicked, set `com_braze_handle_push_deep_links_automatically` to `true` in your `braze.xml`:

```
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

If you would like to custom handle deep links, you will need to create a `BroadcastReceiver` that listens for push received and opened intents from Braze. See [Custom handling push receipts and opens][52] in the Android push documentation for more information.

## Step 5: Add Client Secret and Client ID to Braze dashboard

Lastly, you must add the Client Secret and Client ID you obtained in [Step 1][2] to the Braze dashboard's **Manage Settings** page.

![][34]

## Manual push registration

Braze does not recommend using manual registration, but if you need to handle ADM registration yourself, add the following in your [braze.xml][12]:

```xml
<!-- This will disable automatic registration for ADM via the Braze SDK-->
<bool name="com_braze_push_adm_messaging_registration_enabled">false</bool>
```
Next, use [registerPushToken][37] to pass your user's ADM `registration_id` to Braze:

```java
Braze.getInstance(context).registerPushToken(registration_id);
```

## ADM extras

Users may send custom key-value pairs with a Kindle push message as `extras` for [deep linking][29], tracking URLs, etc. Unlike in Android push, Kindle push users may not use Braze reserved keys as keys when defining `extra` key-value pairs.

Reserved Keys Include:

- `_ab`
- `a`
- `cid`
- `p`
- `s`
- `t`
- `ttl`
- `uri`

If a Kindle reserved key is detected, Braze returns `Status Code 400: Kindle Push Reserved Key Used`.

[2]: #step-1-enable-adm
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/troubleshooting/
[10]: https://developer.amazon.com/public
[11]: https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials
[12]: https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/03-setting-up-adm
[14]: https://developer.amazon.com/public/apis/engage/device-messaging
[29]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/
[32]: https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm
[34]: {% image_buster /assets/img_archive/fire_os_dashboard.png %}
[37]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy/-appboy/register-push-token.html
[52]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#custom-handling-for-push-receipts-opens-dismissals-and-key-value-pairs
