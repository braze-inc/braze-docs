---
nav_title: Initial SDK Setup
article_title: Initial SDK Setup for React Native
platform: React Native
page_order: 1
description: "This reference introduces the React Native SDK and explains how to integrate it natively on Android and iOS."
search_rank: 1
---

# Initial SDK setup

Installing the Braze React Native SDK provides basic analytics functionality and lets you integrate in-app messages and Content Cards for both iOS and Android with just one codebase.

You will need to complete installation steps on both platforms separately.

To complete the installation, you will need the [App Identifier API key]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) as well as the [SDK endpoint]({{site.baseurl}}/api/basics/#endpoints). Both are located under **Manage Settings** in the dashboard.

## Step 1: Integrate the Braze library

{% alert note %}
Braze React Native SDK v1.38.0+ requires at least React Native v0.64+. Braze React Native SDK is not yet compatible with the new React Native architecture.
{% endalert %}

{% tabs local %}
{% tab bash %}
```bash
npm install @braze/react-native-sdk
```
{% endtab %}
{% tab yarn %}
```bash
yarn add @braze/react-native-sdk
```
{% endtab %}
{% endtabs %}

## Step 2: Complete native setup

{% tabs %}
{% tab Expo %}

#### Step 2.1: Install the Braze Expo plugin

Ensure that your version of the Braze React Native SDK is at least 1.37.0. Then, install the Braze Expo plugin.

```bash
expo install @braze/expo-plugin
```

#### Step 2.2: Add the plugin to your app.json

In your `app.json`, add the Braze Expo Plugin. You can provide the following configuration options:

| Method                                    | Type     | Description                                                                                                                                            |
| ------------------------------------------| ---------| -------------------------------------------------------------------------------------------------------------------------------------------------------|
| `androidApiKey`                           | string   |  Required. The API key for your Android application.                                                                                                   |
| `iosApiKey`                               | string   |  Required. The API key for your iOS application.                                                                                                       |
| `baseUrl`                                 | string   |  Required. The [SDK endpoint]({{site.baseurl}}/api/basics/#endpoints) for your application.                                                            |
| `enableBrazeIosPush`                      | boolean  |  iOS only. Whether to use Braze to handle push notifications on iOS. Introduced in React Native SDK v1.38.0 and Expo Plugin v0.4.0.                    |
| `enableFirebaseCloudMessaging`            | boolean  |  Android only. Whether to use Firebase Cloud Messaging for push notifications. Introduced in React Native SDK v1.38.0 and Expo Plugin v0.4.0.          |
| `firebaseCloudMessagingSenderId`          | string   |  Android only. Your Firebase Cloud Messaging sender ID. Introduced in React Native SDK v1.38.0 and Expo Plugin v0.4.0.                                 |
| `sessionTimeout`                          | integer  |  The Braze session timeout for your application in seconds.                                                                                            |
| `enableSdkAuthentication`                 | boolean  |  Whether to enable the [SDK Authentication](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication) feature.   |
| `logLevel`                                | integer  |  The log level for your application. The default log level is 8 and will minimally log info. To enable verbose logging for debugging, use log level 0. |
| `minimumTriggerIntervalInSeconds`         | integer  |  The minimum time interval in seconds between triggers. Defaults to 30 seconds.                                                                        |
| `enableAutomaticLocationCollection`       | boolean  |  Whether automatic location collection is enabled (if the user permits).                                                                               |
| `enableGeofence`                          | boolean  |  Whether geofences are enabled.                                                                                                                        |
| `enableAutomaticGeofenceRequests`         | boolean  |  Whether geofence requests should be made automatically.                                                                                               |
| `dismissModalOnOutsideTap`                | boolean  |  iOS only. Whether a modal in-app message will be dismissed when the user clicks outside of the in-app message.                                        |
| `androidHandlePushDeepLinksAutomatically` | boolean  |  Android only. Whether the Braze SDK should automatically handle push deep links.                                                                      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Example configuration:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "baseUrl": "YOUR-SDK-ENDPOINT",
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
        }
      ],
    ]
  }
}
```

#### Step 2.3: Build and run your application

Prebuilding your application will generate the native files necessary for the Braze SDK to work.

```bash
expo prebuild
```

Run your application as specified in the [Expo docs](https://docs.expo.dev/workflow/customizing/). Note that making any changes to the configuration options will require you to prebuild and run the application again.

{% endtab %}
{% tab Android %}

#### Step 2.1a: Add our repository

In your top-level project `build.gradle`, add the following as repositories under `allprojects` > `repositories` and `buildscript` > `dependencies`:

```gradle
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}

allprojects {
    repositories {
        maven { url "https://appboy.github.io/appboy-android-sdk/sdk" }
    }
}
```

This will add the Braze SDK repository source and Kotlin to your project.

#### Step 2.1b: Configure the Braze SDK

To connect to Braze servers, create a `braze.xml` file in your project's `res/values` folder. Paste the following code and replace the API key and endpoint with your values:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

Add the required permissions to your `AndroidManifest.xml` file:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

#### Step 2.1c: Implement user session tracking

The calls to `openSession()` and `closeSession()` are handled automatically.
Add the following code to the `onCreate()` method of your `MainApplication` class:

{% subtabs global %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

#### Step 2.1d: Handle intent updates

If your MainActivity has `android:launchMode` set to `singleTask`, add the following code to your `MainActivity` class:

{% subtabs global %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

#### Step 2.1: Install pods

Since React Native automatically links the libraries to the native platform, you can install the SDK with the help of CocoaPods.

From the root folder of the project:

```bash
cd ios && pod install
```

#### Step 2.2: Configure the Braze SDK

{% subtabs global %}
{% subtab SWIFT %}

Import the Braze SDK at the top of the `AppDelegate.swift` file:
```swift
import BrazeKit
import braze_react_native_sdk
```

In the `application(_:didFinishLaunchingWithOptions:)` method, replace the API key and endpoint with your app's values. Then, create the Braze instance using the configuration, and create a static property on the `AppDelegate` for easy access:

```swift
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
    // Setup Braze bridge
    let moduleInitializer = BrazeReactBridge() as? RCTBridgeDelegate
    let bridge = RCTBridge(
        delegate: moduleInitializer,
        launchOptions: launchOptions)
    let rootView = RCTRootView(
        bridge: bridge,
        moduleName: "<YOUR_PROJECT_NAME>",
        initialProperties: nil)
    self.bridge = rootView.bridge

    // Configure views in the application
    window = UIWindow(frame: UIScreen.main.bounds)
    let rootViewController = UIViewController()
    rootViewController.view = rootView
    window?.rootViewController = rootViewController
    window?.makeKeyAndVisible()

    // Setup Braze
    let configuration = Braze.Configuration(
        apiKey: "<BRAZE_API_KEY>",
        endpoint: "<BRAZE_ENDPOINT>")
    // - Enable logging and customize the configuration here
    configuration.logger.level = .info
    let braze = BrazeReactBridge.initBraze(configuration)
    AppDelegate.braze = braze

    return true
}

// MARK: - AppDelegate.braze

static var braze: Braze? = nil
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Import the Braze SDK at the top of the `AppDelegate.m` file:
```objc
#import <BrazeKit/BrazeKit-Swift.h>
#import "BrazeReactBridge.h"
```

In the `application:didFinishLaunchingWithOptions:` method, replace the API key and endpoint with your app's values. Then, create the Braze instance using the configuration, and create a static property on the `AppDelegate` for easy access:

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze bridge
  id<RCTBridgeDelegate> moduleInitializer = [[BrazeReactBridge alloc] init];
  RCTBridge *bridge = [[RCTBridge alloc] initWithDelegate:moduleInitializer
                                            launchOptions:launchOptions];
  RCTRootView *rootView = [[RCTRootView alloc] initWithBridge:bridge
                                                   moduleName:@"<YOUR_PROJECT_NAME>"
                                            initialProperties:nil];
  self.bridge = rootView.bridge;

  // Configure views in the application
  self.window = [[UIWindow alloc] initWithFrame:[UIScreen mainScreen].bounds];
  UIViewController *rootViewController = [UIViewController new];
  rootViewController.view = rootView;
  self.window.rootViewController = rootViewController;
  [self.window makeKeyAndVisible];

  // Setup Braze
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                                                    endpoint:@"<BRAZE_ENDPOINT>"];
  // - Enable logging and customize the configuration here
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

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

Once installed, you can `import` the library in your React Native code:

```javascript
import Braze from "@braze/react-native-sdk";
```

Reference our [sample project](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) for more details.

## Test your basic integration

At this point, you can verify that the SDK is integrated by checking session statistics in the dashboard. If you run your application on either platform, you should see a new session in dashboard (in the **Overview** section).

You can start a session for a particular user by calling the following code in your app.

```javascript
Braze.changeUser("userId");
```

For example, you can assign the user ID at the startup of the app:

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.changeUser("some-user-id");
  }, []);

  return (
    <div>
      ...
    </div>
  )
```

You can then search for the user with `some-user-id` in the dashboard under [User Search][user-search]. There, you can verify that session and device data have been logged.


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/ "Android SDK Install"
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/ "iOS SDK Install"
[user-search]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search#using-user-search
