---
nav_title: Initial SDK Setup
article_title: Initial SDK Setup for Flutter
platform: Flutter
page_order: 1
description: "This reference introduces the Flutter SDK and explains how to integrate it natively on Android and iOS."

---

# Initial SDK setup

Follow these instructions to install the [Braze Flutter SDK][1] that contains a package to allows integrators to use Braze APIs in [Flutter apps][2] written in Dart. This plugin provides basic analytics functionality and lets you integrate in-app messages and Content Cards for both iOS and Android with a single codebase.

You will need to complete installation steps on both platforms separately.

To complete the installation, you will need the [App Identifier API key][3] as well as the [SDK endpoint][4]. Both are located in the **Developer Console** under **Settings** in the dashboard.

Before following the steps below, please install and set up [the Flutter SDK][5].

### Requirements
* Dart SDK 2.0.0+
* Flutter SDK 1.10.0+

## Step 1: Integrate the Braze library

Add the Braze Flutter SDK package from the command line.

```bash
flutter pub add braze_plugin
```

This will add the appropriate line to your `pubspec.yaml`.

## Step 2: Complete native setup

{% tabs %}
{% tab Android %}

To connect to Braze servers, create a `braze.xml` file in your project's `android/res/values` folder. Paste the following code and replace the API key and endpoint with your values:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_appboy_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_appboy_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

Add the required permissions to your `AndroidManifest.xml` file:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% endtab %}

{% tab iOS %}

{% subtabs global %}
{% subtab SWIFT %}
Add Appboy SDK import at the top of the `AppDelegate.swift` file:
```swift
import Appboy_iOS_SDK
```

In the same file, add the following snippet within the `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` method:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY", in:application, withLaunchOptions:launchOptions)
```
{% endsubtab %}
{% subtab OBJC %}
Add Appboy SDK import at the top of the `AppDelegate.m` file:
```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

In the same file, add the following snippet within the `application:didFinishLaunchingWithOptions` method:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions];
```
{% endsubtab %}
{% endsubtabs %}

Then, add your SDK Endpoint in the `Info.plist` file. It is located in the `ios` project folder. If you're working in Xcode:

1. Add a row with the name `Braze` and type of `Dictionary`.
2. To that Dictionary, add a row with the name `Endpoint`, type `String` and as a value, input your [SDK endpoint][6].

Otherwise, add the following elements to the file:

```xml
<key>Braze</key>
  <dict>
    <key>Endpoint</key>
    <string>sdk.your-endpoint.com</string>
  </dict>
```

{% endtab %}
{% endtabs %}

## Step 3: Usage

To import the plugin into your Dart code, use:

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

Then, initialize an instance of the Braze plugin by calling `new BrazePlugin()` like in [our sample app][7].

## Test your basic integration

At this point, you can verify that the SDK is integrated by checking session statistics in the dashboard. If you run your application on either platform, you should see a new session in dashboard (in the **Overview** section).

You can open a session for a particular user by calling the following code in your app.

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("some-user-id");
```

Then, search for the user with `some-user-id` in the dashboard under **User Search**. There, you can verify that session and device data have been logged.

[1]: https://pub.dev/packages/braze_plugin
[2]: https://flutter.dev/
[3]: {{site.baseurl}}/api/api_key/#the-app-identifier-api-key
[4]: {{site.baseurl}}/api/basics/#endpoints
[5]: https://docs.flutter.dev/get-started/install
[6]: {{site.baseurl}}/api/basics/#endpoints
[7]: https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart
