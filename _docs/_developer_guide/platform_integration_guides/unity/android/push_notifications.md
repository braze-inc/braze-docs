---
nav_title: Push Notifications
platform: Unity
subplatform: Android
page_order: 1
---
# Push Notifications

A push notification is an out-of-app alert that appears on the user's screen when an important update occurs. Push notifications are a valuable way to provide your users with time-sensitive and relevant content or to re-engage them with your app.

Sample push notification:

![Sample Push][23]

Check out [our troubleshooting section][8] for additional best practices.

Braze sends push notifications to Android devices using [Firebase Cloud Messaging (FCM)][9].

In order to integrate Braze push notifications into your app, you need to:

1. Enable Firebase
2. Configure your Android Manifest
3. Configure your appboy.xml
4. Set your API key on the Braze dashboard

## Step 1: Enable Firebase

To get started, follow the instructions at [Add Firebase to Your Android Project][12].

Next, add the Firebase Unity SDK to your app as described in the [Firebase Unity Setup Docs][11].

Note that integrating the Firebase Unity SDK may cause your `AndroidManifest.xml` to be overriden. If that occurs, make sure to revert it to its original self.

## Step 2: Configure your Android Manifest

Once you have setup your Firebase project, it is time to configure your Android Manifest with required permissions for Braze push.

1. Add the following permissions to your `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
```

## Step 3: Configure your appboy.xml

In order for a device to receive push notifications, it must register with the FCM server. The Braze SDK can handle the registration process for you.

- To tell Braze to handle registration automatically, add the following configuration to your `appboy.xml` file:

```xml
<!-- Whether or not Braze should handle registering the device to receive push notifications. Default is false. -->
<bool name="com_appboy_firebase_cloud_messaging_registration_enabled">true</bool>
```

- Add the following configuration element to your `appboy.xml` file and replace `REPLACE_WITH_YOUR_FCM_SENDER_ID` with your Firebase Sender ID:

```xml
<!-- Replace with your Firebase Sender ID -->
<string name="com_appboy_firebase_cloud_messaging_sender_id">REPLACE_WITH_YOUR_FCM_SENDER_ID</string>
```

- **Recommended** To instruct Braze to handle deep links from push automatically, add the following configuration to your `appboy.xml` file:

```xml
<!-- Whether to open push deep links from Braze automatically. -->
<bool name="com_appboy_handle_push_deep_links_automatically">true</bool>
```

- **Recommended**: Specify the drawable resource that should be displayed in the push notification in your appboy.xml file.

```xml
<!-- The drawable that should be displayed whenever a push notification is received. If no icon is given, the notification will use the application icon -->
<drawable name="com_appboy_push_small_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
```

- **Optional**: Braze will broadcast Intents whenever a push notification is received or opened. If you need to perform custom logic upon push notifications open or receipt, you may create and register a custom broadcast receiver to listen to and respond to these intents. The names of the actions are:

```
REPLACE_WITH_YOUR_PACKAGE_NAME.intent.APPBOY_PUSH_RECEIVED
REPLACE_WITH_YOUR_PACKAGE_NAME.intent.APPBOY_NOTIFICATION_OPENED
REPLACE_WITH_YOUR_PACKAGE_NAME.intent.APPBOY_PUSH_DELETED
```

## Step 4: Set Your Firebase Credentials

You need to input your Firebase Server Key and Sender ID into the Braze dashboard:

* On the app settings page (where your API keys are located), select your Android app.
* Enter your Firebase Server Key in the field labeled "Firebase Cloud Messaging Server Key" under the Push Notification Settings section.
* Enter your Firebase Sender ID in the field labeled "Firebase Cloud Messaging Sender ID" under the Push Notification Settings section.

![FCMKey][15]

If you're not familiar with the location of your Firebase Server Key and Sender ID, follow these steps:

1. Login to the [Firebase Developers Console][58]

2. Select your Firebase project

3. Select Cloud Messaging under Settings and copy the Server Key and Sender ID:
![FirebaseServerKey][59]

##### Implementation Example

The sample project in the [Braze Unity SDK repository][13] contains a full working sample app that includes FCM.

## Deep Linking to In-App Resources

Although Braze can handle standard deep links (such as website urls, Android uris, etc.) out of the box, creating custom deep links requires additional Manifest setup.

See Android's documentation on ["Deep Linking" to In-App Resources][26]

[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/troubleshooting/
[9]: https://firebase.google.com/docs/cloud-messaging/
[11]: https://firebase.google.com/docs/unity/setup
[12]: https://firebase.google.com/docs/android/setup
[13]: https://github.com/Appboy/appboy-unity-sdk/tree/master/unity-samples
[15]: {% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey"
[23]: {% image_buster /assets/img_archive/Push_Android_2.png %}
[26]: https://developer.android.com/training/app-links/deep-linking
[58]: https://console.firebase.google.com/
[59]: {% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey"
