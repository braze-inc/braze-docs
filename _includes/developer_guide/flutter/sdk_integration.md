## About the Flutter Braze SDK

After you integrate the Braze Flutter SDK on Android and iOS, you'll be able to use the Braze API within your [Flutter apps](https://flutter.dev/) written in Dart. This plugin provides basic analytics functionality and lets you integrate in-app messages and Content Cards for both iOS and Android with a single codebase.

## Integrating the Flutter SDK

### Prerequisites

Before you integrate the Braze Flutter SDK, you'll need to complete the following:

| Prerequisite | Description |
| --- | --- |
| Braze API app identifier | To locate your app's identifier, go to **Settings** > **APIs and Identifiers** > **App Identifiers**. For more information see, [API Identifier Types]({{site.baseurl}}/api/identifier_types/#app-identifier).|
| Braze SDK endpoint | Your SDK endpoint URL (for example, `sdk.<cluster>.braze.com`). Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).|
| Flutter SDK | Install the official [Flutter SDK](https://docs.flutter.dev/get-started/install) and ensure it meets the Braze Flutter SDK's [minimum supported version](https://github.com/braze-inc/braze-flutter-sdk#requirements). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Step 1: Integrate the Braze library

Add the Braze Flutter SDK package from the command line. This will add the appropriate line to your `pubspec.yaml`.

```bash
flutter pub add braze_plugin
```

### Step 2: Complete native SDK setup

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

#### Android

Create a `braze.xml` file in your project's `android/res/values` folder. The API key and endpoint are provided at runtime from Dart, so they are not required in this file. Add any other native configurations you need:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- API key and endpoint are not required here. They are set at runtime via Dart. -->
</resources>
```

Add the required permissions to your `AndroidManifest.xml` file:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

#### iOS

In the `application(_:didFinishLaunchingWithOptions:)` method, call `BrazePlugin.configure(_:postInitialization:)` to store your configuration. The Braze instance is created later when `initialize()` is called from Dart. The API key and endpoint are not set here.

{% subtabs %}
{% subtab SWIFT %}

Add the Braze SDK imports at the top of the `AppDelegate.swift` file:

```swift
import BrazeKit
import braze_plugin
```

```swift
override func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  BrazePlugin.configure(
    { configuration in
      configuration.logger.level = .info
      // Set other non-API-key configurations here, such as:
      // configuration.push.automation = true
      // configuration.sessionTimeout = 60
    },
    postInitialization: { braze in
      // Optional: customize the Braze instance after creation.
    }
  )

  return true
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Import the Braze SDK at the top of the `AppDelegate.m` file:

```objc
@import BrazeKit;
@import braze_plugin;
```

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [BrazePlugin configure:^(BRZConfiguration *configuration) {
    configuration.logger.level = BRZLoggerLevelInfo;
    // Set other non-API-key configurations here, such as:
    // configuration.push.automation = ...
    // configuration.sessionTimeout = 60;
  } postInitialization:^(Braze *braze) {
    // Optional: customize the Braze instance after creation.
  }];

  return YES;
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
`BrazePlugin.configure()` only stores your configuration. No Braze instance exists until `initialize()` is called from Dart, so do not call any Braze SDK methods in the AppDelegate after `configure()`.
{% endalert %}

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

{% alert tip %}
Upgrading to 18.0.0? See [Migrating from `initBraze` to `initialize`](#migrating-from-initbraze-to-initialize) for a step-by-step checklist.
{% endalert %}

#### Android

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

#### iOS

{% subtabs %}
{% subtab SWIFT %}
Add the Braze SDK imports at the top of the `AppDelegate.swift` file:
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
Import the Braze SDK at the top of the `AppDelegate.m` file:
```objc
@import BrazeKit;
@import braze_plugin;
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

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

Import the plugin and create a single instance of `BrazePlugin`:

```dart
import 'package:braze_plugin/braze_plugin.dart';

final BrazePlugin braze = BrazePlugin();
```

Then call `initialize()` with your Braze API app identifier (API key) and SDK endpoint to create the Braze instance. When you call `initialize()` determines how the SDK behaves at startup.

#### Standard initialization

To initialize the SDK when your app starts, call `initialize()` in `initState()`:

```dart
@override
void initState() {
  super.initState();
  braze.initialize("<BRAZE_API_KEY>", "<BRAZE_SDK_ENDPOINT>");
}
```

#### Delayed initialization

To defer SDK initialization until a later point in the session—for example, after the user grants consent or completes login—call `initialize()` when you're ready:

```dart
void onUserConsent() {
  braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

{% alert warning %}
Push notifications and deep links received before `initialize()` is called are not processed on iOS. On Android, deep links from push notifications do not resolve while the SDK is waiting to be initialized. If your app relies on push or deep links at launch, use [standard initialization](#standard-initialization) instead.
{% endalert %}

#### Platform-specific API keys

If your Android and iOS apps use different API keys, use platform detection:

```dart
import 'dart:io' show Platform;

if (Platform.isAndroid) {
  braze.initialize("<ANDROID_API_KEY>", "<BRAZE_ENDPOINT>");
} else if (Platform.isIOS) {
  braze.initialize("<IOS_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

#### Re-initialization

You can call `initialize()` multiple times to re-initialize the SDK with a different API key and endpoint mid-session. Each call tears down the previous Braze instance and creates a new one.

{% alert important %}
To avoid undefined behaviors, only allocate and use a single instance of the `BrazePlugin` in your Dart code. All SDK method calls made before `initialize()` are ignored on iOS, so call `initialize()` before using any other Braze methods.
{% endalert %}

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

To import the plugin into your Dart code, use the following:

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

Then, initialize an instance of the Braze plugin by calling `new BrazePlugin()` like in [our sample app](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart).

{% alert important %}
To avoid undefined behaviors, only allocate and use a single instance of the `BrazePlugin` in your Dart code.
{% endalert %}

{% endtab %}
{% endtabs %}

## Migrating from `initBraze` to `initialize`

Starting with Flutter SDK 18.0.0, `BrazePlugin.initBraze()` is deprecated. To migrate to the new `configure` + `initialize` pattern:

1. **iOS:** In your `AppDelegate.swift`, replace `BrazePlugin.initBraze(configuration)` with `BrazePlugin.configure(_:postInitialization:)`. Remove the `static var braze` property and the `AppDelegate.braze = braze` assignment, as the plugin manages the Braze instance internally.
2. **iOS:** Remove any manual channel subscription or in-app message data-forwarding code (for example, `braze.contentCards.subscribeToUpdates`, `braze.featureFlags.subscribeToUpdates`, or custom `inAppMessagePresenter` subscription hooks). The plugin now sets up these subscriptions automatically. Optional customization of the in-app message presenter using `postInitialization` is still supported; see [Customize in-app message presentation]({{site.baseurl}}/developer_guide/in-app_messages/customization/#flutter).
3. **Android:** Remove `com_braze_api_key` and `com_braze_custom_endpoint` from your `braze.xml`. Keep other configuration entries such as FCM sender ID and push settings.
4. **Dart:** Add `braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>")` after creating your `BrazePlugin` instance.

{% alert note %}
`BrazePlugin.initBraze()` still works in 18.0.0 but is deprecated. Existing integrations using `initBraze()` continue to function, and channel subscriptions are set up automatically regardless of which initialization method you use.
{% endalert %}

## Testing the integration

You can verify that the SDK is integrated by checking session statistics in the dashboard. If you run your application on either platform, you should see a new session in the dashboard (in the **Overview** section).

Open a session for a particular user by calling the following code in your app.

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

```dart
BrazePlugin braze = BrazePlugin();
braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
braze.changeUser("{some-user-id}");
```

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

{% endtab %}
{% endtabs %}

Search for the user with `{some-user-id}` in the dashboard under **Audience** > **Search Users**. There, you can verify that session and device data have been logged.

