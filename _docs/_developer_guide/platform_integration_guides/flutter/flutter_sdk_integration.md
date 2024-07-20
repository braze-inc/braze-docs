---
nav_title: Initial SDK Setup
article_title: Initial SDK Setup for Flutter
platform: Flutter
page_order: 1
description: "This reference introduces the Flutter SDK and explains how to integrate it natively on Android and iOS."
search_rank: 1
---

# Initial SDK setup

> This reference article covers how to install the Braze SDK for Flutter. Follow these instructions to install the [Braze Flutter SDK](https://pub.dev/packages/braze_plugin) that contains a package to allows integrators to use Braze APIs in [Flutter apps](https://flutter.dev/) written in Dart.

This plugin provides basic analytics functionality and lets you integrate in-app messages and Content Cards for both iOS and Android with a single codebase.

{% alert note %}
You will need to complete installation steps on both platforms separately.
{% endalert %}

## Prerequisites

To complete the installation, you will need the [app identifier API key]({{site.baseurl}}/api/identifier_types/) as well as the [SDK endpoint]({{site.baseurl}}/api/basics/#endpoints). Both are located under **Manage Settings** in the dashboard.

Before following these steps, install and set up the [Flutter SDK](https://docs.flutter.dev/get-started/install). Ensure your machine and project are running the minimum required Flutter and Dart versions [noted here](https://github.com/braze-inc/braze-flutter-sdk#readme).

## Step 1: Integrate the Braze library

Add the Braze Flutter SDK package from the command line.

```bash
flutter pub add braze_plugin
```

This will add the appropriate line to your `pubspec.yaml`.

## Step 2: Complete native setup

{% tabs %}
{% tab Android %}

To connect to Braze servers, create a `braze.xml` file in your project's `android/res/values` folder. Paste the following code and replace the API identifier key and endpoint with your values:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
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
Add Braze SDK import at the top of the `AppDelegate.swift` file:
```swift
import BrazeKit
import braze_plugin
```

In the same file, create the Braze configuration object in the `application(_:didFinishLaunchingWithOptions:)` method and replace the API key and endpoint with your app's values. Then, create the Braze instance using the configuration, and create a static property on the `AppDelegate` for easy access:

```swift
static var braze: Braze? = nil

func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  // Setup Braze
  let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>"
  )
  // - Enable logging or customize configuration here
  configuration.logger.level = .info
  let braze = BrazePlugin.initBraze(configuration)
  AppDelegate.braze = braze

  return true
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}
Import `BrazeKit` at the top of the `AppDelegate.m` file:
```objc
@import BrazeKit;
```

In the same file, create the Braze configuration object in the `application:didFinishLaunchingWithOptions:` method and replace the API key and endpoint with your app's values. Then, create the Braze instance using the configuration, and create a static property on the `AppDelegate` for easy access:

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration =
      [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                      endpoint:@"<BRAZE_ENDPOINT>"];
  // - Enable logging or customize configuration here
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazePlugin initBraze:configuration];
  AppDelegate.braze = braze;

  [self.window makeKeyAndVisible];
  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

## Step 3: Usage

To import the plugin into your Dart code, use the following:

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

Then, initialize an instance of the Braze plugin by calling `new BrazePlugin()` like in [our sample app](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart).

## Test your basic integration

At this point, you can verify that the SDK is integrated by checking session statistics in the dashboard. If you run your application on either platform, you should see a new session in dashboard (in the **Overview** section).

You can open a session for a particular user by calling the following code in your app.

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

Then, search for the user with `{some-user-id}` in the dashboard under **Audience** > **Search Users**. There, you can verify that session and device data have been logged.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can search for users from **Users** > **User Search**.
{% endalert %}

[1]: https://pub.dev/packages/braze_plugin
[2]: https://flutter.dev/
[3]: {{site.baseurl}}/api/api_key/#the-app-identifier-api-key
[4]: {{site.baseurl}}/api/basics/#endpoints
[5]: https://docs.flutter.dev/get-started/install
[6]: https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart
[7]: https://github.com/braze-inc/braze-flutter-sdk#readme
