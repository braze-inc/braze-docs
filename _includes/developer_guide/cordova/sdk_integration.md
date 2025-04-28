## Integrating the Cordova SDK

### Prerequisites

Before you start, verify your environment is supported by the [latest Braze Cordova SDK version](https://github.com/braze-inc/braze-cordova-sdk?tab=readme-ov-file#minimum-version-requirements).

### Step 1: Add the SDK to your project

If you're on Cordova 6 or later, you can add the SDK directly from GitHub. Alternatively, you can download a ZIP of the [GitHub repository](https://github.com/braze-inc/braze-cordova-sdk) and add the SDK manually.

{% tabs local %}
{% tab geofence disabled %}
If you don't plan on using location collection and geofences, use the `master` branch from GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```
{% endtab %}

{% tab geofence enabled %}
If you plan on using location collection and geofences, use the `geofence-branch` from GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```
{% endtab %}
{% endtabs %}

{% alert tip %}
You can switch between `master` and `geofence-branch` at anytime by repeating this step.
{% endalert %}

### Step 2: Configure your project

Next, adding the following preferences to the `platform` element in your project's `config.xml` file.

{% tabs %}
{% tab ios %}
```xml
<preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.ios_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}

{% tab android %}
```xml
<preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.android_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}
{% endtabs %}

Replace the following:

| Value                 | Description                                                                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `BRAZE_API_KEY`       | Your [Braze REST API key]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys).              |
| `CUSTOM_API_ENDPOINT` | A custom API endpoint. This endpoint is used to route your Braze instance data to the correct App Group in your Braze dashboard. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

The `platform` element in your `config.xml` file should be similar to the following:

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% endtabs %}

## Platform-specific syntax

The following section covers the platform-specific syntax when using Cordova with iOS or Android.

### Integers

{% tabs %}
{% tab ios %}
Integer preferences are read as string representations, like in the following example:

```xml
<platform name="ios">
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_session_timeout" value="5" />
</platform>
```
{% endtab %}

{% tab android %}
Due to how the Cordova 8.0.0+ framework handles preferences, integer-only preferences (such as sender IDs) must be set to strings prepended with `str_`, like in the following example:

```xml
<platform name="android">
    <preference name="com.braze.android_fcm_sender_id" value="str_64422926741" />
    <preference name="com.braze.android_default_session_timeout" value="str_10" />
</platform>
```
{% endtab %}
{% endtabs %}

### Booleans

{% tabs %}
{% tab ios %}
Boolean preferences are read by the SDK using `YES` and `NO` keywords as a string representation, like in the following example:

```xml
<platform name="ios">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
{% endtab %}

{% tab android %}
Boolean preferences are read by the SDK using `true` and `false` keywords as a string representation, like in the following example:

```xml
<platform name="android">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false" />
</platform>
```
{% endtab %}
{% endtabs %}

## Optional configurations {#optional}

You can add any of the following preferences to the `platform` element in your project's `config.xml` file:

{% tabs %}
{% tab ios %}
| Method                                            | Description                                                                                                                                                                                                                                           |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ios_api_key`                                     | Sets the API key for your application.                                                                                                                                                                                                                |
| `ios_api_endpoint`                                | Sets the [SDK endpoint]({{site.baseurl}}/api/basics/#endpoints) for your application.                                                                                                                                                                 |
| `ios_disable_automatic_push_registration`         | Sets whether automatic push registration should be disabled.                                                                                                                                                                                          |
| `ios_disable_automatic_push_handling`             | Sets whether automatic push handling should be disabled.                                                                                                                                                                                              |
| `ios_enable_idfa_automatic_collection`            | Sets whether the Braze SDK should automatically collect the IDFA information. For more information, see [the Braze IDFA method documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/). |
| `enable_location_collection`                      | Sets whether the automatic location collection is enabled (if the user permits). The `geofence-branch`                                                                                                                                                |
| `geofences_enabled`                               | Sets whether geofences are enabled.                                                                                                                                                                                                                   |
| `ios_session_timeout`                             | Sets the Braze session timeout for your application in seconds. Defaults to 10 seconds.                                                                                                                                                               |
| `sdk_authentication_enabled`                      | Sets whether to enable the [SDK Authentication]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication) feature.                                                                                              |
| `display_foreground_push_notifications`           | Sets whether push notifications should be displayed while the application is in the foreground.                                                                                                                                                       |
| `ios_disable_un_authorization_option_provisional` | Sets whether `UNAuthorizationOptionProvisional` should be disabled.                                                                                                                                                                                   |
| `trigger_action_minimum_time_interval_seconds`    | Sets the minimum time interval in seconds between triggers. Defaults to 30 seconds.                                                                                                                                                                   |
| `ios_push_app_group`                              | Sets the app group ID for iOS push extensions.                                                                                                                                                                                                        |
| `ios_forward_universal_links`                     | Sets if the SDK should automatically recognize and forward universal links to the system methods.                                                                                                                                                     |
| `ios_log_level`                                   | Sets the minimum logging level for `Braze.Configuration.Logger`.                                                                                                                                                                                      |
| `ios_use_uuid_as_device_id`                       | Sets if a randomly generated UUID should be used as the device ID.                                                                                                                                                                                    |
| `ios_flush_interval_seconds`                      | Sets the interval in seconds between automatic data flushes. Defaults to 10 seconds.                                                                                                                                                                  |
| `ios_use_automatic_request_policy`                | Sets whether the request policy for `Braze.Configuration.Api` should be automatic or manual.                                                                                                                                                          |
| `should_opt_in_when_push_authorized`              | Sets if a user’s notification subscription state should automatically be set to `optedIn` when push permissions are authorized.                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert tip %}
For more detailed information, see [GitHub: Braze iOS Cordova plugin](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m).
{% endalert %}
{% endtab %}

{% tab android %}
| Method                                                            | Description                                                                                                                                                                                   |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `android_api_key`                                                 | Sets the API key for your application.                                                                                                                                                        |
| `android_api_endpoint`                                            | Sets the [SDK endpoint]({{site.baseurl}}/api/basics/#endpoints) for your application.                                                                                                         |
| `android_small_notification_icon`                                 | Sets the notification small icon.                                                                                                                                                             |
| `android_large_notification_icon`                                 | Sets the notification large icon.                                                                                                                                                             |
| `android_notification_accent_color`                               | Sets the notification accent color using a hexadecimal representation.                                                                                                                        |
| `android_default_session_timeout`                                 | Sets the Braze session timeout for your application in seconds. Defaults to 10 seconds.                                                                                                       |
| `android_handle_push_deep_links_automatically`                    | Sets whether the Braze SDK should automatically handle push deep links.                                                                                                                       |
| `android_log_level`                                               | Sets the log level for your application. The default log level is 4 and will minimally log info. To enable verbose logging for debugging, use log level 2.                                    |
| `firebase_cloud_messaging_registration_enabled`                   | Sets whether to use Firebase Cloud Messaging for push notifications.                                                                                                                          |
| `android_fcm_sender_id`                                           | Sets the Firebase Cloud Messaging sender ID.                                                                                                                                                  |
| `enable_location_collection`                                      | Sets whether the automatic location collection is enabled (if the user permits).                                                                                                              |
| `geofences_enabled`                                               | Sets whether geofences are enabled.                                                                                                                                                           |
| `android_disable_auto_session_tracking`                           | Disable the Android Cordova plugin from automatically tracking sessions. For more information, see [Disabling automatic session tracking](#cordova_disable-automatic-session-tracking) |
| `sdk_authentication_enabled`                                      | Sets whether to enable the [SDK Authentication]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication) feature.                                      |
| `trigger_action_minimum_time_interval_seconds`                    | Sets the minimum time interval in seconds between triggers. Defaults to 30 seconds.                                                                                                           |
| `is_session_start_based_timeout_enabled`                          | Sets whether the session timeout behavior to be based either on session start or session end events.                                                                                          |
| `default_notification_channel_name`                               | Sets the user-facing name as seen via `NotificationChannel.getName` for the Braze default `NotificationChannel`.                                                                              |
| `default_notification_channel_description`                        | Sets the user-facing description as seen via `NotificationChannel.getDescription` for the Braze default `NotificationChannel`.                                                                |
| `does_push_story_dismiss_on_click`                                | Sets whether a Push Story is automatically dismissed when clicked.                                                                                                                            |
| `is_fallback_firebase_messaging_service_enabled`                  | Sets whether the use of a fallback Firebase Cloud Messaging Service is enabled.                                                                                                               |
| `fallback_firebase_messaging_service_classpath`                   | Sets the classpath for the fallback Firebase Cloud Messaging Service.                                                                                                                         |
| `is_content_cards_unread_visual_indicator_enabled`                | Sets whether the Content Cards unread visual indication bar is enabled.                                                                                                                       |
| `is_firebase_messaging_service_on_new_token_registration_enabled` | Sets whether the Braze SDK will automatically register tokens in `com.google.firebase.messaging.FirebaseMessagingService.onNewToken`.                                                         |
| `is_push_deep_link_back_stack_activity_enabled`                   | Sets whether Braze will add an activity to the back stack when automatically following deep links for push.                                                                                   |
| `push_deep_link_back_stack_activity_class_name`                   | Sets the activity that Braze will add to the back stack when automatically following deep links for push.                                                                                     |
| `should_opt_in_when_push_authorized`                              | Sets if Braze should automatically opt-in the user when push is authorized.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert tip %}
For more detailed information, see [GitHub: Braze Android Cordova plugin](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/android/BrazePlugin.kt).
{% endalert %}
{% endtab %}
{% endtabs %}

The following is an example `config.xml` file with additional configurations:

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO"/"YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO"/"YES" />
    <preference name="com.braze.ios_enable_idfa_automatic_collection" value="YES"/"NO" />
    <preference name="com.braze.enable_location_collection" value="NO"/"YES" />
    <preference name="com.braze.geofences_enabled" value="NO"/"YES" />
    <preference name="com.braze.ios_session_timeout" value="5" />
    <preference name="com.braze.sdk_authentication_enabled" value="YES"/"NO" />
    <preference name="com.braze.display_foreground_push_notifications" value="YES"/"NO" />
    <preference name="com.braze.ios_disable_un_authorization_option_provisional" value="NO"/"YES" />
    <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="30" />
    <preference name="com.braze.ios_push_app_group" value="PUSH_APP_GROUP_ID" />
    <preference name="com.braze.ios_forward_universal_links" value="YES"/"NO" />
    <preference name="com.braze.ios_log_level" value="2" />
    <preference name="com.braze.ios_use_uuid_as_device_id" value="YES"/"NO" />
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_use_automatic_request_policy" value="YES"/"NO" />
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES"/"NO" />
</platform>
```
{% endtab %}

{% tab android %}
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
{% endtab %}
{% endtabs %}

## Disabling automatic session tracking (Android only) {#disable-automatic-session-tracking}

By default, the Android Cordova plugin automatically tracks sessions. To disable automatic session tracking, add the following preference to the `platform` element in your project's `config.xml` file:

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

To start tracking sessions again, call `BrazePlugin.startSessionTracking()`. Keep in mind, only sessions started after the next `Activity.onStart()` will be tracked.
