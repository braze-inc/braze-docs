---
nav_title: Initial SDK Setup
platform: Cordova
subplatform: iOS
page_order: 0
---
# Initial SDK Setup

Installing the Braze SDK will provide you with analytics functionality, as well as push and in-app messages.

{% alert update %}
As of SDK version 2.1.0, use of the iOS SDK requires XCode 8 or above.
{% endalert %}

### Step 1: Get the SDK

Download the SDK from [Github][1] and run the following from the root your project:

```
cordova plugin add path_to_repo/appboy-cordova-sdk/
```

Alternatively, if you are running Cordova 6 or later, you could install directly from Github:

```
cordova plugin add https://github.com/appboy/appboy-cordova-sdk#master
```

### Configure the plugin

In your config.xml, add a `preference` element under the iOS `platform` element that contains your Braze API key with the name `com.appboy.api_key`:

```
    <platform name="ios">
        <preference name="com.appboy.api_key" value="YOUR_API_KEY" />
        ...
    </platform>
```

Set up your applications to have the appropriate certificates for push, via the [iOS push documentation][2].

#### Removing Automatic Push Setup (iOS)

If you want to turn off iOS automatic push registration, add the preference `com.appboy.ios_disable_automatic_push_registration` with a value of `true`.

### Initial Setup Complete

Once the initial setup is complete, you can access the `AppboyPlugin` javascript interface in your app.

[1]: https://github.com/Appboy/appboy-cordova-sdk
[2]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
