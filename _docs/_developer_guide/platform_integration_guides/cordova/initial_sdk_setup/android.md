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

In your `config.xml`, add a `preference` element under the android `platform` element that contains your Braze API key with the name `com.braze.api_key`:

```xml
<platform name="android">
    <preference name="com.braze.api_key" value="YOUR_API_KEY" />
</platform>
```

## Setting extra configuration

The Cordova Android SDK also allows for various other settings to be configured via the `config.xml` file:

```xml
<platform name="android">
    <preference name="com.braze.android_small_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_large_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_notification_accent_color" value="str_ACCENT_COLOR_INTEGER" />
    <preference name="com.braze.android_default_session_timeout" value="str_SESSION_TIMEOUT_INTEGER" />
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true"/"false" />
    <preference name="com.braze.android_log_level" value=LOG_LEVEL_INTEGER />
    <preference name="com.braze.firebase_cloud_messaging_registration_enabled" value="true"/"false" />
    <preference name="com.braze.android_fcm_sender_id" value="str_YOUR_FCM_SENDER_ID" />
    <preference name="com.braze.enable_location_collection" value="true"/"false" />
    <preference name="com.braze.geofences_enabled" value="true"/"false" />
    <preference name="com.braze.android_disable_auto_session_tracking" value="true"/"false" />
</platform>
```

See [Android Cordova plugin][2] for more details.

### Numerical preference example

Due to how the Cordova 8.0.0+ framework handles preferences, entirely numerical preferences like sender IDs must be prefixed with `str_` in order to be properly read by the SDK, like in the following example:

```xml
<platform name="android">
    <preference name="com.braze.firebase_cloud_messaging_registration_enabled" value="true" />
    <preference name="com.braze.android_fcm_sender_id" value="str_64422926741" />
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
