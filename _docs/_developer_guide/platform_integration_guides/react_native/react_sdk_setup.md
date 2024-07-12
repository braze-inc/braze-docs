---
nav_title: Initial SDK Setup
article_title: Initial SDK Setup for React Native
platform: React Native
page_order: 1
description: "This reference introduces the React Native SDK and explains how to integrate it natively on Android and iOS."
search_rank: 1
---

# Initial SDK setup

> This reference article covers how to install the Braze SDK for React Native. Installing the Braze React Native SDK provides basic analytics functionality and lets you integrate in-app messages and Content Cards for both iOS and Android with just one codebase.

## Prerequisites and compatibility

To set up this SDK, React Native v0.71 or later is required. For the full list of supported versions, see our [React Native SDK GitHub repository](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

### React Native New Architecture Support

{% sdk_min_versions reactnative:2.0.1 %}

## Using Braze with the New Architecture

The Braze React Native SDK is compatible with any apps using the [React Native New Architecture](https://reactnative.dev/docs/the-new-architecture/landing-page) starting from SDK version 2.0.1+.

As of SDK version 6.0.0, Braze has been upgraded internally to a React Native Turbo Module, which can still be used with either the New Architecture or the legacy bridge architecture. Because the Turbo Module is backwards compatible, no migration steps are required other than the breaking changes mentioned in the [Changelog](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md) and requiring React Native v0.70+.

{% alert warning %}
If your iOS app conforms to `RCTAppDelegate` and was following our previous `AppDelegate` setup in this documentation, or in the Braze sample project, be sure to reference the samples in [Complete native setup](#step-2-complete-native-setup) to prevent any crashes from occurring when subscribing to events in the Turbo Module.
{% endalert %}

## Step 1: Integrate the Braze library

{% tabs local %}
{% tab npm %}
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

| Method                                        | Type    | Description                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | string  | Required. The [API key]({{site.baseurl}}/api/identifier_types/) for your Android application, located in your Braze dashboard under **Manage Settings**. |
| `iosApiKey`                                   | string  | Required. The [API key]({{site.baseurl}}/api/identifier_types/) for your iOS application, located in your Braze dashboard under **Manage Settings**.     |
| `baseUrl`                                     | string  | Required. The [SDK endpoint]({{site.baseurl}}/api/basics/#endpoints) for your application, located in your Braze dashboard under **Manage Settings**.    |
| `enableBrazeIosPush`                          | boolean | iOS only. Whether to use Braze to handle push notifications on iOS. Introduced in React Native SDK v1.38.0 and Expo Plugin v0.4.0.                       |
| `enableFirebaseCloudMessaging`                | boolean | Android only. Whether to use Firebase Cloud Messaging for push notifications. Introduced in React Native SDK v1.38.0 and Expo Plugin v0.4.0.             |
| `firebaseCloudMessagingSenderId`              | string  | Android only. Your Firebase Cloud Messaging sender ID. Introduced in React Native SDK v1.38.0 and Expo Plugin v0.4.0.                                    |
| `sessionTimeout`                              | integer | The Braze session timeout for your application in seconds.                                                                                               |
| `enableSdkAuthentication`                     | boolean | Whether to enable the [SDK Authentication](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication) feature.      |
| `logLevel`                                    | integer | The log level for your application. The default log level is 8 and will minimally log info. To enable verbose logging for debugging, use log level 0.    |
| `minimumTriggerIntervalInSeconds`             | integer | The minimum time interval in seconds between triggers. Defaults to 30 seconds.                                                                           |
| `enableAutomaticLocationCollection`           | boolean | Whether automatic location collection is enabled (if the user permits).                                                                                  |
| `enableGeofence`                              | boolean | Whether geofences are enabled.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | Whether geofence requests should be made automatically.                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | iOS only. Whether a modal in-app message will be dismissed when the user clicks outside of the in-app message.                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Android only. Whether the Braze SDK should automatically handle push deep links.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Android only. Sets whether the text content in a push notification should be interpreted and rendered as HTML using `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | string  | Android only. Sets the Android notification accent color.                                                                                                |
| `androidNotificationLargeIcon`                | string  | Android only. Sets the Android notification large icon.                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Android only. Sets the Android notification small icon.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | iOS only. Whether the user should automatically be prompted for push permissions on app launch.                                                          |
| `enableBrazeIosRichPush`                      | boolean | iOS only. Whether to enable rich push features for iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | iOS only. Whether to enable Braze Push Stories for iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | iOS only. The app group used for iOS Push Stories.                                                                                                       |

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
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories"
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

#### Step 2.1: Add our repository

In your top-level project `build.gradle`, add the following under `buildscript` > `dependencies`:

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

This will add Kotlin to your project.

#### Step 2.2: Configure the Braze SDK

To connect to Braze servers, create a `braze.xml` file in your project's `res/values` folder. Paste the following code and replace the API [key]({{site.baseurl}}/api/identifier_types/) and [endpoint]({{site.baseurl}}/api/basics/#endpoints) with your values:

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

#### Step 2.3: Implement user session tracking

The calls to `openSession()` and `closeSession()` are handled automatically.
Add the following code to the `onCreate()` method of your `MainApplication` class:

{% subtabs local %}
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

#### Step 2.4: Handle intent updates

If your MainActivity has `android:launchMode` set to `singleTask`, add the following code to your `MainActivity` class:

{% subtabs local %}
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

#### Step 2.1: (Optional) Configure Podfile for dynamic XCFrameworks

To import certain Braze libraries, such as BrazeUI, into an Objective-C++ file, you will need to use the `#import` syntax. Starting in version 7.4.0 of the Braze Swift SDK, binaries have an [optional distribution channel as dynamic XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), which are compatible with this syntax.

If you'd like to use this distribution channel, manually override the CocoaPods source locations in your Podfile. Reference the sample below and replace `{your-version}` with the relevant version you wish to import:

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

#### Step 2.2: Install pods

Since React Native automatically links the libraries to the native platform, you can install the SDK with the help of CocoaPods.

From the root folder of the project:

```bash
# To install using the React Native New Architecture
cd ios && RCT_NEW_ARCH_ENABLED=1 pod install

# To install using the React Native legacy architecture
cd ios && pod install
```

#### Step 2.3: Configure the Braze SDK

{% subtabs local %}
{% subtab SWIFT %}

Import the Braze SDK at the top of the `AppDelegate.swift` file:
```swift
import BrazeKit
```

In the `application(_:didFinishLaunchingWithOptions:)` method, replace the API [key]({{site.baseurl}}/api/identifier_types/) and [endpoint]({{site.baseurl}}/api/basics/#endpoints) with your app's values. Then, create the Braze instance using the configuration, and create a static property on the `AppDelegate` for easy access:

{% alert note %}
Our example assumes an implementation of [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), which provides a number of abstractions in the React Native setup. If you are using a different setup for your app, be sure to adjust your implementation as needed.
{% endalert %}

```swift
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(
        apiKey: "{BRAZE_API_KEY}",
        endpoint: "{BRAZE_ENDPOINT}")
    // Enable logging and customize the configuration here.
    configuration.logger.level = .info
    let braze = BrazeReactBridge.perform(
      #selector(BrazeReactBridge.initBraze(_:)),
      with: configuration
    ).takeUnretainedValue() as! Braze

    AppDelegate.braze = braze

    /* Other configuration */

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

In the `application:didFinishLaunchingWithOptions:` method, replace the API [key]({{site.baseurl}}/api/identifier_types/) and [endpoint]({{site.baseurl}}/api/basics/#endpoints) with your app's values. Then, create the Braze instance using the configuration, and create a static property on the `AppDelegate` for easy access:

{% alert note %}
Our example assumes an implementation of [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), which provides a number of abstractions in the React Native setup. If you are using a different setup for your app, be sure to adjust your implementation as needed.
{% endalert %}

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                                                    endpoint:@"{BRAZE_ENDPOINT}"];
  // Enable logging and customize the configuration here.
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  /* Other configuration */

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
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/ "iOS SDK Install"
[user-search]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search#using-user-search
