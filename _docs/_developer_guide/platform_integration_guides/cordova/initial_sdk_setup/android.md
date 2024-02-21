---
nav_title: Android and FireOS
article_title: Initial Android SDK Setup for Cordova
platform: 
  - Cordova
  - Android
  - FireOS
page_order: 0
page_type: reference
description: "This article covers initial SDK setup steps for Android and FireOS apps running on Cordova."
search_rank: 1
---

# Initial SDK Android setup

> This reference article covers how to install the Braze Android SDK for Cordova. 

Download the SDK from [GitHub][1] and run the following from the root of your project:

```
cordova plugin add path_to_repo/braze-cordova-sdk
```

Alternatively, if you are running Cordova 6 or later, you could install directly from GitHub:

```
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```

## Configure the plugin

In your `config.xml`, add a `preference` element under the android `platform` element that contains your Braze API key with the name `com.braze.api_key` and optionally, a custom API endpoint with the name `com.braze.android_api_endpoint`:

```xml
<platform name="android">
    <preference name="com.braze.api_key" value="YOUR_API_KEY" />
    <preference name="com.braze.android_api_endpoint" value="CUSTOM_API_ENDPOINT" />
</platform>
```

## Setting extra configuration

The Cordova Android SDK also allows for various other settings to be configured via the `config.xml` file:

| Method                                         | Description                                                                                                                                            |
| -----------------------------------------------| -------------------------------------------------------------------------------------------------------------------------------------------------------|
| `api_key`                                      | Sets the API key for your application. |
| `android_api_endpoint`                         | Sets the [SDK endpoint]({{site.baseurl}}/api/basics/#endpoints) for your application. |
| `android_small_notification_icon`              | Sets the notification small icon. |
| `android_large_notification_icon`              | Sets the notification large icon. |
| `android_notification_accent_color`            | Sets the notification accent color using a hexadecimal representation. |
| `android_default_session_timeout`              | Sets the Braze session timeout for your application in seconds. Defaults to 10 seconds. |
| `android_handle_push_deep_links_automatically` | Sets whether the Braze SDK should automatically handle push deep links. |
| `android_log_level`                            | Sets the log level for your application. The default log level is 4 and will minimally log info. To enable verbose logging for debugging, use log level 2. |
| `firebase_cloud_messaging_registration_enabled`| Sets whether to use Firebase Cloud Messaging for push notifications. |
| `android_fcm_sender_id`                        | Sets the Firebase Cloud Messaging sender ID. |
| `enable_location_collection`                   | Sets whether the automatic location collection is enabled (if the user permits). |
| `geofences_enabled`                            | Sets whether geofences are enabled. |
| `android_disable_auto_session_tracking`        | Sets whether to disable the Android Cordova plugin from automatically tracking sessions. |
| `sdk_authentication_enabled`                   | Sets whether to enable the [SDK Authentication](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication) feature. |
| `trigger_action_minimum_time_interval_seconds` | Sets the minimum time interval in seconds between triggers. Defaults to 30 seconds. |
| `is_session_start_based_timeout_enabled`       | Sets whether the session timeout behavior to be based either on session start or session end events. |
| `default_notification_channel_name`            | Sets the user-facing name as seen via `NotificationChannel.getName` for the Braze default `NotificationChannel`. |
| `default_notification_channel_description`     | Sets the user-facing description as seen via `NotificationChannel.getDescription` for the Braze default `NotificationChannel`. |
| `does_push_story_dismiss_on_click`             | Sets whether a Push Story is automatically dismissed when clicked. |
| `is_fallback_firebase_messaging_service_enabled`| Sets whether the use of a fallback Firebase Cloud Messaging Service is enabled. |
| `fallback_firebase_messaging_service_classpath`| Sets the classpath for the fallback Firebase Cloud Messaging Service. |
| `is_content_cards_unread_visual_indicator_enabled`| Sets whether the Content Cards unread visual indication bar is enabled. |
| `is_firebase_messaging_service_on_new_token_registration_enabled`| Sets whether the Braze SDK will automatically register tokens in `com.google.firebase.messaging.FirebaseMessagingService.onNewToken`. |
| `is_push_deep_link_back_stack_activity_enabled` | Sets whether Braze will add an activity to the back stack when automatically following deep links for push. |
| `push_deep_link_back_stack_activity_class_name` | Sets the activity that Braze will add to the back stack when automatically following deep links for push. |
| `should_opt_in_when_push_authorized` | Sets if Braze should automatically opt-in the user when push is authorized. |

Example configuration:

```xml
<platform name="android">
    <preference name="com.braze.android_small_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_large_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_notification_accent_color" value="str_ACCENT_COLOR_INTEGER" />
    <preference name="com.braze.android_default_session_timeout" value="str_SESSION_TIMEOUT_INTEGER" />
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true"/"false" />
    <preference name="com.braze.android_log_level" value="str_LOG_LEVEL_INTEGER" />
    <preference name="com.braze.firebase_cloud_messaging_registration_enabled" value="true"/"false" />
    <preference name="com.braze.android_fcm_sender_id" value="str_YOUR_FCM_SENDER_ID" />
    <preference name="com.braze.enable_location_collection" value="true"/"false" />
    <preference name="com.braze.geofences_enabled" value="true"/"false" />
    <preference name="com.braze.android_disable_auto_session_tracking" value="true"/"false" />
    <preference name="com.braze.sdk_authentication_enabled" value="true"/"false" />
    <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="str_MINIMUM_INTERVAL_INTEGER" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false"/"true" />
    <preference name="com.braze.default_notification_channel_name" value="DEFAULT_NAME" />
    <preference name="com.braze.default_notification_channel_description" value="DEFAULT_DESCRIPTION" />
    <preference name="com.braze.does_push_story_dismiss_on_click" value="true"/"false" />
    <preference name="com.braze.is_fallback_firebase_messaging_service_enabled" value="true"/"false" />
    <preference name="com.braze.fallback_firebase_messaging_service_classpath" value="FALLBACK_FIREBASE_MESSAGING_CLASSPATH" />
    <preference name="com.braze.is_content_cards_unread_visual_indicator_enabled" value="true"/"false" />
    <preference name="com.braze.is_firebase_messaging_service_on_new_token_registration_enabled" value="true"/"false" />
    <preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true"/"false" />
    <preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="DEEPLINK_BACKSTACK_ACTIVITY_CLASS_NAME" />
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true"/"false" />
</platform>
```

See [Android Cordova plugin][2] for more details.

### Numerical preference example

Due to how the Cordova 8.0.0+ framework handles preferences, entirely numerical preferences like sender IDs must be strings prefixed with `str_` in order to be properly read by the SDK, like in the following example:

```xml
<platform name="android">
    <preference name="com.braze.android_fcm_sender_id" value="str_64422926741" />
    <preference name="com.braze.android_default_session_timeout" value="str_10" />
</platform>
```

### Boolean preference example

Boolean preferences are read by the SDK using `true` and `false` keywords as a string representation, like in the following example:

```xml
<platform name="android">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false" />
</platform>
```

## Customized setup

This plugin can be forked and modified for custom implementations. Find the platform-specific native source code in the `/plugin/src` directory, the JavaScript interface in the `/plugin/www` directory, and the main configuration file at `/plugin`.

Users that check their platform directory into version control (enabling them to make permanent code edits there) will be able to further leverage Braze UI elements by calling them directly from their platform-specific project.

### Removing automatic push setup (Android)

To remove automatic push registration on Android set the following configuration preferences:

```xml
<platform name="android">
    <preference name="com.braze.firebase_cloud_messaging_registration_enabled" value="false" />
</platform>
```

### Location collection and geofences

To enable location collection and Braze Geofences, use the [`geofence-branch`][3] instead of the default `master` branch. By default, the Braze SDK disables location collection and Braze Geofences. Additionally, use the following preferences configuration:

```xml
<platform name="android">
    <preference name="com.braze.enable_location_collection" value="true" />
    <preference name="com.braze.geofences_enabled" value="true" />
</platform>
```

The geofence-branch can be added to your Cordova project with the following:

```
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```

### Delaying automatic session tracking

Set `<preference name="com.braze.android_disable_auto_session_tracking" value="true" />` in your `config.xml` to disable the Android Cordova plugin from automatically tracking sessions. To start tracking sessions, call `BrazePlugin.startSessionTracking()`. Note that this will not retroactively track sessions and will only start tracking sessions starting from the next `Activity.onStart()`.

## Initial setup complete

Once the initial setup is complete, you can access your app's `BrazePlugin` JavaScript interface.

[1]: https://github.com/braze-inc/braze-cordova-sdk
[2]: https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/android/BrazePlugin.kt
[3]: https://github.com/braze-inc/braze-cordova-sdk/tree/geofence-branch
