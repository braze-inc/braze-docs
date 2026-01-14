## About the React Native Braze SDK

Integrating the React Native Braze SDK provides basic analytics functionality and lets you integrate in-app messages and Content Cards for both iOS and Android with just one codebase.

## New Architecture compatibility

The following minimum SDK version is compatible with all apps using [React Native's New Architecture](https://reactnative.dev/docs/the-new-architecture/landing-page):

{% sdk_min_versions reactnative:2.0.1 %}

Starting with SDK version 6.0.0, Braze uses a React Native Turbo Module, which is compatible with both the New Architecture and legacy bridge architecture&#8212;meaning no additional setup is required.

{% alert warning %}
If your iOS app conforms to `RCTAppDelegate` and follows our previous `AppDelegate` setup, review the samples in [Complete native setup](#reactnative_step-2-complete-native-setup) to prevent any crashes from occurring when subscribing to events in the Turbo Module.
{% endalert %}

## Integrating the React Native SDK

### Prerequisites

To integrate the SDK, React Native version 0.71 or later is required. For the full list of supported versions, see our [React Native SDK GitHub repository](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

### Step 1: Integrate the Braze library

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

### Step 2: Choose a setup option

You can manage the Braze SDK using the Braze Expo plugin or through one of the native layers. With the Expo plugin, you can configure certain SDK features without writing code in any of the native layers. Choose whichever option best meets your app's needs.

{% tabs %}
{% tab Expo %}
#### Step 2.1: Install the Braze Expo plugin

Ensure that your version of the Braze React Native SDK is at least 1.37.0. For the full list of supported versions, check out the [Braze React Native repository](https://github.com/braze-inc/braze-expo-plugin?tab=readme-ov-file#version-support).

To install the Braze Expo plugin, run the following command:

```bash
npx expo install @braze/expo-plugin
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
| `iosUseUUIDAsDeviceId`                        | boolean | iOS only. Whether the device ID will use a randomly generated UUID.                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

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

Prebuilding your application will generate the native files necessary for the Braze Expo plugin to work.

```bash
npx expo prebuild
```

Run your application as specified in the [Expo docs](https://docs.expo.dev/workflow/customizing/). Keep in mind, if you make any changes to the configuration options, you'll be required to prebuild and run the application again.
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
  <string translatable="false" name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

Add the required permissions to your `AndroidManifest.xml` file:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
On Braze SDK version 12.2.0 or later, you can automatically pull in the android-sdk-location library by setting `importBrazeLocationLibrary=true` in your `gradle.properties` file .
{% endalert %}

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
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

#### Step 2.3: Configure the Braze SDK

{% subtabs local %}
{% subtab SWIFT %}

Import the Braze SDK at the top of the `AppDelegate.swift` file:
```swift
import BrazeKit
import braze_react_native_sdk
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

### Step 3: Import the library

Next, `import` the library in your React Native code. For more details, check out our [sample project](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject). 

```javascript
import Braze from "@braze/react-native-sdk";
```

### Step 4: Test the integration (optional)

To test your SDK integration, start a new session on either platform for a user by calling the following code in your app.

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

In the Braze dashboard, go to [User Search]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search#using-user-search) and look for the user with the ID matching `some-user-id`. Here, you can verify that session and device data were logged.
