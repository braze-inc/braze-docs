---
nav_title: Push Notifications
article_title: Push Notifications for Flutter
platform: Flutter
page_order: 2
description: "This article covers implementing and testing push notifications on Flutter."
channel: push

---

# Push notifications integration

> This reference article covers how to set push notifications for Flutter. Integrating push notifications requires setting up each native platform separately. Follow the respective guides listed to finish the installation.

## Step 1: Complete the initial setup

{% tabs %}
{% tab Android %}
### Step 1.1: Register for push

Register for using Google’s Firebase Cloud Messaging (FCM) API. For a full walkthrough, refer to the following steps from the [Native Android push integration guide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/):

1. [Add Firebase to your project]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-add-firebase-to-your-project).
2. [Add Cloud Messaging to your dependencies]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-2-add-cloud-messaging-to-your-dependencies).
3. [Create a service account]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-3-create-a-service-account).
4. [Generate JSON credentials]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-generate-json-credentials).
5. [Upload your JSON credentials to Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-upload-your-json-credentials-to-braze).

### Step 1.2: Add your Google Sender ID

First, go to Firebase Console, open your project, then select <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **Project settings**.

![The Firebase project with the "Settings" menu open.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Select **Cloud Messaging**, then under **Firebase Cloud Messaging API (V1)**, copy the **Sender ID** to your clipboard.

![The Firebase project's "Cloud Messaging" page with the "Sender ID" highlighted.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

Next, open your project's `app.json` file and set your `firebaseCloudMessagingSenderId` property to the Sender ID in your clipboard. For example:

```
"firebaseCloudMessagingSenderId": "693679403398"
```

### Step 1.3: Add the path to your Google Services JSON

In your project's `app.json` file, add the path to your `google-services.json` file. This file is required when setting `enableFirebaseCloudMessaging: true` in your configuration.

```json
{
  "expo": {
    "android": {
      "googleServicesFile": "PATH_TO_GOOGLE_SERVICES"
    },
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "enableBrazeIosPush": true,
          "enableFirebaseCloudMessaging": true,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true
        }
      ],
    ]
  }
}
```
{% endtab %}

{% tab iOS %}
### Step 1.1: Upload APNs certificates

Generate an Apple Push Notification service (APNs) certificate and uploaded it to the Braze dashboard. For a full walkthrough, see [Uploading your APNs certificate]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-upload-your-apns-certificate).

### Step 1.2: Add push notification support to your app

Complete one of the following native integration guides:

- [Swift only](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications/)
- [Swift or Objective-C]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration)

{% endtab %}
{% endtabs %}

## Step 2: Listen for push notification events (optional)

You can subscribe to events where Braze has detected and handled an incoming push notification. In your application, call `subscribeToPushNotificationEvents()` and pass in a code block to be executed once a push event is triggered.

{% alert note %}
Braze push notification events are available on both Android and iOS. Due to platform differences, iOS will only detect Braze push events when a user has interacted with a notification.
{% endalert %}

```dart
// Create stream subscription
StreamSubscription pushEventsStreamSubscription;

pushEventsStreamSubscription = braze.subscribeToPushNotificationEvents((BrazePushEvent pushEvent) {
  print("Push Notification event of type ${pushEvent.payloadType} seen. Title ${pushEvent.title}\n and deeplink ${pushEvent.url}");
  // Handle push notification events
});

// Cancel stream subscription
pushEventsStreamSubscription.cancel();
```

#### Push notification event fields

{% alert note %}
Because of platform limitations on iOS, the Braze SDK can only process push payloads while the app is in the foreground. Listeners will only trigger for the `push_opened` event type on iOS after a user has interacted with a push.
{% endalert %}

For a full list of push notification fields, refer to the table below:

| Field Name         | Type      | Description |
| ------------------ | --------- | ----------- |
| `payload_type`     | String    | Specifies the notification payload type. The two values that are sent from the Braze Flutter SDK are `push_opened` and `push_received`.  Only `push_opened` events are supported on iOS. |
| `url`              | String    | Specifies the URL that was opened by the notification. |
| `use_webview`      | Boolean   | If `true`, URL will open in-app in a modal webview. If `false`, the URL will open in the device browser. |
| `title`            | String    | Represents the title of the notification. |
| `body`             | String    | Represents the body or content text of the notification. |
| `summary_text`     | String    | Represents the summary text of the notification. This is mapped from `subtitle` on iOS. |
| `badge_count`      | Number   | Represents the badge count of the notification. |
| `timestamp`        | Number | Represents the time at which the payload was received by the application. |
| `is_silent`        | Boolean   | If `true`, the payload is received silently. For details on sending Android silent push notifications, refer to [Silent push notifications on Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications). For details on sending iOS silent push notifications, refer to [Silent push notifications on iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/). |
| `is_braze_internal`| Boolean   | This will be `true` if a notification payload was sent for an internal SDK feature, such as geofences sync, Feature Flag sync, or uninstall tracking. The payload is received silently for the user. |
| `image_url`        | String    | Specifies the URL associated with the notification image. |
| `braze_properties` | Object    | Represents Braze properties associated with the campaign (key-value pairs). |
| `ios`              | Object    | Represents iOS-specific fields. |
| `android`          | Object    | Represents Android-specific fields. |
{: .reset-td-br-1 .reset-td-br-2}

## Step 3: Test displaying push notifications

Once you've configured push notifications in the native layer, follow these steps to test your push integration.

{% alert note %}
As of Xcode 14, you can test remote push notifications on an iOS simulator.
{% endalert %}

1. Set an active user in the Flutter application. To do so, initialize your plugin by calling `braze.changeUser('your-user-id')`.
2. Head to **Campaigns** and create a new push notification campaign. Choose the platforms that you'd like to test.
3. Compose your test notification and head over to the **Test** tab. Add the same `user-id` as the test user and click **Send Test**.
4. You should receive the notification on your device shortly. You may need to check in the Notification Center or update Settings if it doesn't display.
