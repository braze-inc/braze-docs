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

Alternatively, if you are running Cordova 6 or later, you could install directly from Github:

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

### Removing automatic push setup

If you want to turn off iOS automatic push registration, set the following configuration preferences:

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="YES" />
    ...
</platform>
```

### Optional IDFA collection

To enable the automatic collection of the [iOS IDFA][3], set the following configuration preferences:

```xml
<platform name="ios">
    <preference name="com.braze.ios_enable_idfa_automatic_collection" value="YES" />
</platform>
```

### Location collection and geofences

To enable location collection and Braze Geofences, use the `geofence-branch` instead of the default `master` branch. By default, the Braze SDK disables location collection and Braze Geofences. Additionally, use the following preferences configuration:

```xml
<platform name="ios">
    <preference name="com.braze.enable_location_collection" value="true" />
    <preference name="com.braze.geofences_enabled" value="true" />
</platform>
```

The `geofence-branch` can be added to your Cordova project with the following:

```
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```

See [iOS Geofences][4] for more details.

### Initial setup complete

Once the initial setup is complete, you can access the `BrazePlugin` JavaScript interface in your app.

[1]: https://github.com/braze-inc/braze-cordova-sdk
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/
[3]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/locations_and_geofences/
