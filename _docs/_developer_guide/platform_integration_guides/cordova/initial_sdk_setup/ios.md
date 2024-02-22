---
nav_title: iOS
article_title: Initial iOS SDK Setup for Cordova
platform: 
  - Cordova
  - iOS
page_order: 2
page_type: reference
description: "This article describes initial SDK setup steps for iOS apps running on Cordova."
search_rank: 2
---

# Initial SDK iOS Setup

> This reference article covers how to install the Braze iOS SDK for Cordova. 

Download the SDK from [GitHub][1] and run the following from the root your project:

```
cordova plugin add path_to_repo/braze-cordova-sdk/
```

Alternatively, if you are running Cordova 6 or later, you could install directly from GitHub:

```
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```

## Configure the plugin

In your `config.xml`, add a `preference` element under the iOS `platform` element that contains your Braze API key with the name `com.braze.api_key`:

```xml
<platform name="ios">
    <preference name="com.braze.api_key" value="YOUR_API_KEY" />
</platform>
```

Set up your applications to have the appropriate certificates for push, via the [iOS push documentation][2].

## Setting extra configuration

The Cordova iOS SDK also allows for various other settings to be configured via the `config.xml` file:

| Method                                         | Description                                                                                                                                            |
| -----------------------------------------------| -------------------------------------------------------------------------------------------------------------------------------------------------------|
| `api_key`                                      | Sets the API key for your application. |
| `ios_api_endpoint`                             | Sets the [SDK endpoint]({{site.baseurl}}/api/basics/#endpoints) for your application. |
| `ios_disable_automatic_push_registration`      | Sets whether automatic push registration should be disabled. |
| `ios_disable_automatic_push_handling`          | Sets whether automatic push handling should be disabled. |
| `ios_enable_idfa_automatic_collection`         | Sets whether the Braze SDK should automatically collect the IDFA information. |
| `enable_location_collection`                   | Sets whether the automatic location collection is enabled (if the user permits). |
| `geofences_enabled`                            | Sets whether geofences are enabled. |
| `ios_session_timeout`                          | Sets the Braze session timeout for your application in seconds. Defaults to 10 seconds. |
| `sdk_authentication_enabled`                   | Sets whether to enable the [SDK Authentication](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication) feature. |
| `display_foreground_push_notifications`        | Sets whether push notifications should be displayed while the application is in the foreground. |
| `ios_disable_un_authorization_option_provisional` | Sets whether `UNAuthorizationOptionProvisional` should be disabled. |
| `trigger_action_minimum_time_interval_seconds` | Sets the minimum time interval in seconds between triggers. Defaults to 30 seconds. |
| `ios_push_app_group` | Sets the app group ID for iOS push extensions. |
| `ios_forward_universal_links` | Sets if the SDK should automatically recognize and forward universal links to the system methods. |
| `ios_log_level` | Sets the minimum logging level for `Braze.Configuration.Logger`. |
| `ios_use_uuid_as_device_id` | Sets if a randomly generated UUID should be used as the device ID. |
| `ios_flush_interval_seconds` | Sets the interval in seconds between automatic data flushes. Defaults to 10 seconds. |
| `ios_use_automatic_request_policy` | Sets whether the request policy for `Braze.Configuration.Api` should be automatic or manual. |
| `should_opt_in_when_push_authorized` | Sets if a user’s notification subscription state should automatically be set to `optedIn` when push permissions are authorized. |

Example for setting extra configurations:

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

See [iOS Cordova plugin][3] for more details.

### Numerical preference example

Numerical preferences are read by the SDK as string representations, like in the following example:

```xml
<platform name="ios">
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_session_timeout" value="5" />
</platform>
```

### Boolean preference example

Boolean preferences are read by the SDK using `YES` and `NO` keywords as a string representation, like in the following example:

```xml
<platform name="ios">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```

## Customized setup

This plugin can be forked and modified for custom implementations. Find the platform-specific native source code in the `/plugin/src` directory, the JavaScript interface in the `/plugin/www` directory, and the main configuration file at `/plugin`.

Users that check their platform directory into version control (enabling them to make permanent code edits there) will be able to further leverage Braze UI elements by calling them directly from their platform-specific project.

### Removing automatic push setup (iOS)

If you want to turn off iOS automatic push registration, set the following configuration preferences:

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="YES" />
    ...
</platform>
```

### Location collection and geofences

To enable location collection and Braze Geofences, use the [`geofence-branch`][4] instead of the default `master` branch. By default, the Braze SDK disables location collection and Braze Geofences. Additionally, use the following preferences configuration:

```xml
<platform name="ios">
    <preference name="com.braze.enable_location_collection" value="YES" />
    <preference name="com.braze.geofences_enabled" value="YES" />
</platform>
```

The `geofence-branch` can be added to your Cordova project with the following:

```
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```

See [iOS Geofences][5] for more details.

### Optional IDFA collection

To enable the automatic collection of the [iOS IDFA][6], set the following configuration preference in your `config.xml`:

```xml
<platform name="ios">
    <preference name="com.braze.ios_enable_idfa_automatic_collection" value="YES" />
</platform>
```

## Initial setup complete

Once the initial setup is complete, you can access the `BrazePlugin` JavaScript interface in your app.

[1]: https://github.com/braze-inc/braze-cordova-sdk
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/
[3]: https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m
[4]: https://github.com/braze-inc/braze-cordova-sdk/tree/geofence-branch
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/locations_and_geofences/
[6]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/
