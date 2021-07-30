---
nav_title: Initial SDK Setup
platform: React Native
page_order: 1
description: "This reference introduces React Native SDK and explain how to integrate it natively on Android and iOS."
---

# Initial SDK Setup

Installing the Braze React Native SDK provides basic analytics functionality and lets you integrate In-App Messages and Content Card messages for both platforms with just one code base.

It is necessary to complete installation steps in both platform separately.

You will need the App Identifier Braze SDK API key as well as the endpoint. Both are located in the `Developer Console` under `Settings` in the Dashboard. You can read more about the API keys in the API documentation.

## Step 1: Integrate the Braze Library

Add Braze React Native SDK package.

```bash
npm install react-native-appboy-sdk
# or using yarn
# yarn add react-native-appboy-sdk
```

## Step 2: Complete Native Setup

### Android

#### Add Our Repository

In your top-level project `build.gradle`, add the following as repositories under `allprojects` -> `repositories`:

```gradle
allprojects {
  repositories {
    ...
    maven { url "https://appboy.github.io/appboy-android-sdk/sdk" }
  }
}
```

#### Configure the Braze SDK

To connect to Braze servers, create a `braze.xml` file in your project's `res/values` folder. Paste the following code and replace the API key and endpoint with your values:

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

#### Implement User Session Tracking

The calls to `openSession()` and `closeSession()` are handled automatically.
Add the following code to the `onCreate()` method of your Application class in the `MainApplication.java` file:

```java
import com.appboy.AppboyLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new AppboyLifecycleCallbackListener());
}
```

### iOS

Since React Native automatically links the libraries to the native platform, you can install the SDK with the help of CocoaPods.

#### Install Pods

From the root folder of the project:

```bash
cd ios && pod install
```

#### Configure the Braze SDK

In the `AppDelegate.m` file, add the following snippet within the
`application:didFinishLaunchingWithOptions` method:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

Then, add your SDK Endpoint in the `Info.plist` file. It is located in the `ios` project folder. If you're working in Xcode:

1. Add a row with the name `Braze` and type of `Dictionary`
2. To that Dictionary, add a row with the name `Endpoint`, type `String` and as a value, input your endpoint.
3. 
Otherwise, add the following elements to the file:

```xml
<key>Braze</key>
  <dict>
    <key>Endpoint</key>
    <string>sdk.your-endpoint.com</string>
  </dict>
```

## Step 3: Usage

Once installed, you can `import` the library in your React Native code:

```javascript
import ReactAppboy from "react-native-appboy-sdk";
```

## Test Your Basic Integration

At this point, you can verify that the SDK is integrated by checking session statistics in the Dashboard. If you run your application on either platform, you should see a new session in Dashboard (in the `Overview` section).

You can open a session for a particular user by calling the following code in your app.

```javascript
ReactAppboy.changeUser("some-user-id");
```

For example, you can assign the user ID at the startup of the app:

```javascript
import React, { useEffect } from "react";
import ReactAppboy from "react-native-appboy-sdk";

const App = () => {
  useEffect(() => {
    ReactAppboy.changeUser("some-user-id");
  }, []);

  return (
    <div>
      ...
    </div>
  )
```

You can then search for the user with `some-user-id` in the Dashboard under `User Search`. There, you can verify that session and device data has been logged.


[1]: https://www.braze.com/docs/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/ "Android SDK Install"
[2]: https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/ "iOS SDK Install"
