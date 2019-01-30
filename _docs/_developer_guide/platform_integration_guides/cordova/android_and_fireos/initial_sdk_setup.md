---
nav_title: Initial SDK Setup
platform: Cordova
subplatform: Android and FireOS
page_order: 0
---
# Initial SDK Setup

Download the SDK from [github][1] and run `cordova plugin add path_to_repo/appboy-cordova-sdk` from the root your project.

Alternatively, if you are running Cordova 6 or earlier, you could install directly from github, like `cordova plugin add https://github.com/appboy/appboy-cordova-sdk#master`.

### Configure the plugin

In your config.xml, add a `preference` element under the android `platform` element that contains your Braze API key with the name `com.appboy.api_key`:

```
    <platform name="android">
        <preference name="com.appboy.api_key" value="YOUR_API_KEY" />
        ...
    </platform>
```

### Setting Extra Configuration

The Cordova Android SDK also allows for various other settings to be configured via the config.xml file:

```
<platform name="android">
    <preference name="com.appboy.android_small_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.appboy.android_large_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.appboy.android_notification_accent_color" value="str_ACCENT_COLOR_INTEGER" />
    <preference name="com.appboy.android_default_session_timeout" value="str_SESSION_TIMEOUT_INTEGER" />
    <preference name="com.appboy.android_handle_push_deep_links_automatically" value="true"/"false" />
    <preference name="com.appboy.android_log_level" value=LOG_LEVEL_INTEGER />
    <preference name="com.appboy.firebase_cloud_messaging_registration_enabled" value="true"/"false" />
    <preference name="com.appboy.android_fcm_sender_id" value="str_YOUR_FCM_SENDER_ID" />
</platform>
```

See the [Android Cordova Plugin][2] for more details.


> Due to how the Cordova 8.0.0+ framework handles preferences, entirely numerical preferences like sender IDs must be prefixed with `str_` in order to be properly read by the SDK. An example is included below:

```
<platform name="android">
    <preference name="com.appboy.firebase_cloud_messaging_registration_enabled" value="true" />
    <preference name="com.appboy.android_fcm_sender_id" value="str_64422926741" />
</platform>
```


### Customized Setup

Note that this plugin can be forked and modified for custom implementations. Find the platform-specific native source code in the `/plugin/src` directory, the javascript interface in the `/plugin/www` directory, and the main configuration file at `/plugin`.

Users that check their platform directory into version control (enabling them to make permanent code edits there) will be able to further leverage Braze's UI elements by calling them directly from their platform specific project.

#### Removing automatic push setup (Android)

To remove automatic push registration on Android set the `com.appboy.firebase_cloud_messaging_registration_enabled` value in the plugin `config.xml` to false.

### Initial Setup Complete

Once the initial setup is complete, you can access the `AppboyPlugin` javascript interface in your app.

[1]: https://github.com/Appboy/appboy-cordova-sdk
[2]: https://github.com/Appboy/appboy-cordova-sdk/blob/master/src/android/AppboyPlugin.java
