## About the Flutter Braze SDK

After you integrate the Braze Flutter SDK on Android and iOS, you'll be able to use the Braze API within your [Flutter apps](https://flutter.dev/) written in Dart. This plugin provides basic analytics functionality and lets you integrate in-app messages and Content Cards for both iOS and Android with a single codebase.

## Integrating the Flutter SDK

### Prerequisites

Before you integrate the Braze Flutter SDK, you'll need to complete the following:

| Prerequisite | Description |
| --- | --- |
| Braze API app identifier | To locate your app's identifier, go to **Settings** > **APIs and Identifiers** > **App Identifiers**. For more information see, [API Identifier Types]({{site.baseurl}}/api/identifier_types/#app-identifier).|
| Braze REST endpoint | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).|
| Flutter SDK | Install the official [Flutter SDK](https://docs.flutter.dev/get-started/install) and ensure it meets the Braze Flutter SDK's [minimum supported version](https://github.com/braze-inc/braze-flutter-sdk#requirements). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Step 1: Integrate the Braze library

Add the Braze Flutter SDK package from the command line. This will add the appropriate line to your `pubspec.yaml`.

```bash
flutter pub add braze_plugin
```

### Step 2: Complete native SDK setup

{% tabs %}
{% tab Android %}

To connect to Braze servers, create a `braze.xml` file in your project's `android/res/values` folder. Paste the following code and replace the API identifier key and endpoint with your values:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
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

override func application(
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

### Step 3: Set up the plugin

To import the plugin into your Dart code, use the following:

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

Then, initialize an instance of the Braze plugin by calling `new BrazePlugin()` like in [our sample app](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart).

{% alert important %}
To avoid undefined behaviors, only allocate and use a single instance of the `BrazePlugin` in your Dart code.
{% endalert %}

## Testing the integration

You can verify that the SDK is integrated by checking session statistics in the dashboard. If you run your application on either platform, you should see a new session in dashboard (in the **Overview** section).

Open a session for a particular user by calling the following code in your app.

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

Search for the user with `{some-user-id}` in the dashboard under **Audience** > **Search Users**. There, you can verify that session and device data have been logged.

