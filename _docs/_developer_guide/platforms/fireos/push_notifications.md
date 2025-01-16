---
page_order: 1
nav_title: Push Notifications
article_title: "Push notifications for the Braze Swift SDK"
description: "This landing page is home to all things Android push notifications."
---

# Push notifications

> With push notifications, you can re-engage your app users by sending time-sensitive and relevant content directly to their device screen&#8212;even if their app is closed. When you're finished integrating push for your app, be sure to check out our [push best practices]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/).

{% alert important %}
If your Android push integration is already set up, and you're looking to migrate from Google's deprecated Cloud Messaging API, see [Migrating to the Firebase Cloud Messaging API]({{site.baseurl}}/developer_guide/platforms/android/push_notifications/migrating_to_firebase_cloud_messaging/).
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/android.md %}

## Built-in features

The following features are built into the Braze Android SDK. To use any other push notification features, you will need to [set up push notifications](#setting-up-push-notifications) for your app.

|Feature|Description|
|-------|-----------|
|Push Stories|FireOS Push Stories are built into the Braze Android SDK by default. To learn more, see [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Amazon Device Messaging (ADM)

Braze sends push notifications to Amazon devices using [Amazon Device Messaging (ADM)](https://developer.amazon.com/public/apis/engage/device-messaging). Keep in mind, ADM is not supported on non-Amazon devices, so in order to test Kindle push, you must have a [FireOS device](https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm). For best practices, see [Troubleshooting Push Notifications]({{site.baseurl}}/developer_guide/platforms/fireos/push_notifications/troubleshooting/).

## Setting up push notifications

### Step 1: Enable ADM

1. Create an account with the [Amazon Apps & Games Developer Portal](https://developer.amazon.com/public) if you have not already done so.
2. Obtain [OAuth credentials (Client ID and Client Secret) and an ADM API key](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. Enable **Automatic ADM Registration Enabled** in the Unity Braze Configuration window. 
  - Alternatively, you may add the following line to your `res/values/braze.xml` file to enable ADM registration:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```

### Step 2: Update `AndroidManifest.xml`

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

  <!-- This permission verifies that no other application can intercept your ADM messages. -->
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

Finally, add intent filters to handle `REGISTRATION` and `RECEIVE` intents from ADM within your Braze `AndroidManifest.xml` file. Immediately after `amazon:enable-feature`, add the following elements:

```xml
    <receiver
      android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver"
      android:exported="true"
      android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
        <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
        <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />

        <category android:name="${applicationId}" />
      </intent-filter>
    </receiver>
```

### Step 3: Store your ADM API key

First, save your ADM API key to a file named `api_key.txt` and save it in your project's [`Assets/Plugins/Android/assets`][54] folder. Next, [obtain an ADM API Key for your app](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).

Amazon will not recognize your key if `api_key.txt` contains any white space characters, such as a trailing line break.

### Step 4: Add deep links

To enable Braze to automatically open your app and any deep links when a push notification is clicked, set `com_braze_handle_push_deep_links_automatically` to `true` in your `braze.xml`:

```
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

If you want to custom handle deep links, you will need to create a push callback that listens for push received and opened intents from Braze. See [Custom handling push receipts and opens]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback) in the Android push documentation for more information.

### Step 5: Upload client secret and ID to Braze

In Braze, go to **Manage Settings** and upload the client secret and ID [you downloaded earlier](#step-1-enable-adm).

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})

### Step 6: Send a test message (optional)

To send a message, use the command line to make a POST request to the [`/messages/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/).

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer BRAZE_API_KEY" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "OPTIONAL_KEY":"OPTIONAL_VALUE"
      }
    }
  }
}' https://{REST_API_ENDPOINT_URL}/messages/send
```

Replace the following:

| Placeholder              | Description                                                                                                          | Required?        |
|--------------------------|----------------------------------------------------------------------------------------------------------------------|-------------------|
| `BRAZE_API_KEY`      | For your Braze API key, go to **Settings** > **API Keys**. Ensure the key is authorized to send messages via the [`/messages/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). | Yes   |
| `EXTERNAL_USER_ID`       | For an external user ID, go to **Search Users** > and find a user to use for testing.                                                                               | Yes  |
| `REST_API_ENDPOINT_URL` | Use the endpoint that matches the [Braze Instance]({{site.baseurl}}/api/basics/#endpoints) you're using. | Yes   |
| `OPTIONAL_KEY`              | The key for any optional data you want to send with the push notification, such as a URL or additional parameters. | Optional   |
| `OPTIONAL_VALUE`            | The value for any optional data you want to send with the push notification, such as a URL or additional parameters. | Optional  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Manual push registration

Braze does not recommend registering push notifications manually, but if you need to handle ADM registration yourself, add the following in your [braze.xml](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/03-setting-up-adm):

```xml
<!-- This will disable automatic registration for ADM via the Braze SDK-->
<bool name="com_braze_push_adm_messaging_registration_enabled">false</bool>
```
Next, use [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html) to pass your user's ADM `registration_id` to Braze:

{% tabs local %}
{% tab Java %}

```java
Braze.getInstance(context).setRegisteredPushToken(registration_id);
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).registeredPushToken = registration_id
```

{% endtab %}
{% endtabs %}

## ADM key-value pairs

Users may send custom key-value pairs with a Kindle push message as `extras` for [deep linking]({{site.baseurl}}/developer_guide/platforms/android/push_notifications/deep_linking/), tracking URLs, etc. Unlike in Android push, Kindle push users may not use Braze reserved keys as keys when defining `extra` key-value pairs.

If a Kindle reserved key is detected, Braze returns `Status Code 400: Kindle Push Reserved Key Used`.

<table style="width: 250px; border-collapse: collapse;">
    <thead>
        <tr>
            <th>Reserved Keys</th>
        </tr>
    </thead>
    <tbody>
        <tr><td><code>_ab</code></td></tr>
        <tr><td><code>a</code></td></tr>
        <tr><td><code>cid</code></td></tr>
        <tr><td><code>p</code></td></tr>
        <tr><td><code>s</code></td></tr>
        <tr><td><code>t</code></td></tr>
        <tr><td><code>ttl</code></td></tr>
        <tr><td><code>uri</code></td></tr>
    </tbody>
</table>
