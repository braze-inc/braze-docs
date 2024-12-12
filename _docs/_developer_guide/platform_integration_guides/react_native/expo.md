---
nav_title: Using Expo
article_title: Using the Braze Expo Plugin
platform: React Native
page_order: 6
description: "This article covers how to configure the Braze SDK using the Expo plugin."

---

# Using the Braze Expo Plugin

> This article covers how to set up and configure the Braze Expo plugin in your React Native app.

Braze offers ways to configure the SDK behavior via a separate [Expo plugin](https://github.com/braze-inc/braze-expo-plugin) you can add to your React Native app on top of the React Native SDK. This plugin requires that you have the base Braze React Native SDK integrated into your project.

## Setup

#### Step 1: Install the Braze Expo plugin

Ensure that your version of the Braze React Native SDK is at least 1.37.0. Refer [here](https://github.com/braze-inc/braze-expo-plugin?tab=readme-ov-file#version-support) for the full version support table. Install the Braze Expo plugin with the following command:

```bash
expo install @braze/expo-plugin
```

#### Step 2: Add the plugin to your app.json

In your `app.json`, add the Braze Expo Plugin. You can provide the following configuration options:

| Method                                        | Type    | Description                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | string  | Required. The [API key]({{site.baseurl}}/api/identifier_types/) for your Android application, located in your Braze dashboard under **Manage Settings**. |
| `iosApiKey`                                   | string  | Required. The [API key]({{site.baseurl}}/api/identifier_types/) for your iOS application, located in your Braze dashboard under **Manage Settings**.     |
| `baseUrl`                                     | string  | Required. The [SDK endpoint]({{site.baseurl}}/api/basics/#endpoints) for your application, located in your Braze dashboard under **Manage Settings**.    |
| `enableBrazeIosPush`                          | boolean | iOS only. Whether to use Braze to handle push notifications on iOS. Introduced in React Native SDK v1.38.0 and Expo Plugin v0.4.0.                       |
| `enableFirebaseCloudMessaging`                | boolean | Android only. Whether to use Firebase Cloud Messaging for push notifications. Introduced in React Native SDK v1.38.0 and Expo Plugin v0.4.0.             |
| `firebaseCloudMessagingSenderId`              | string  | Android only. Your Firebase Cloud Messaging sender ID. Introduced in React Native SDK v1.38.0 and Expo Plugin v0.4.0.                                    |
| `sessionTimeout`                              | integer | The Braze session timeout for your application in seconds.                                                                                               |
| `enableSdkAuthentication`                     | boolean | Whether to enable the [SDK Authentication](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication) feature.      |
| `logLevel`                                    | integer | The log level for your application. The default log level is 8 and will minimally log info. To enable verbose logging for debugging, use log level 0.    |
| `minimumTriggerIntervalInSeconds`             | integer | The minimum time interval in seconds between triggers. Defaults to 30 seconds.                                                                           |
| `enableAutomaticLocationCollection`           | boolean | Whether automatic location collection is enabled (if the user permits).                                                                                  |
| `enableGeofence`                              | boolean | Whether geofences are enabled.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | Whether geofence requests should be made automatically.                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | iOS only. Whether a modal in-app message will be dismissed when the user clicks outside of the in-app message.                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Android only. Whether the Braze SDK should automatically handle push deep links.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Android only. Sets whether the text content in a push notification should be interpreted and rendered as HTML using `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | string  | Android only. Sets the Android notification accent color.                                                                                                |
| `androidNotificationLargeIcon`                | string  | Android only. Sets the Android notification large icon.                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Android only. Sets the Android notification small icon.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | iOS only. Whether the user should automatically be prompted for push permissions on app launch.                                                          |
| `enableBrazeIosRichPush`                      | boolean | iOS only. Whether to enable rich push features for iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | iOS only. Whether to enable Braze Push Stories for iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | iOS only. The app group used for iOS Push Stories.                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Example configuration:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "baseUrl": "YOUR-SDK-ENDPOINT",
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories"
        }
      ],
    ]
  }
}
```

#### Step 3: Build and run your application

Prebuilding your application will generate the native files necessary for the Braze Expo plugin to work.

```bash
expo prebuild
```

Run your application as specified in the [Expo docs](https://docs.expo.dev/workflow/customizing/). Note that making any changes to the configuration options will require you to prebuild and run the application again.
