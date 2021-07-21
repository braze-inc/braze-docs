---
nav_title: Initial SDK Setup
platform: React Native
page_order: 1
description: "This reference introduces React Native SDK and explain how to integrate it natively on Android and iOS."
---

# Initial SDK Setup

Installing the Braze React Native SDK provides basic analytics functionality and lets you integrate In-App Messages and Content Card messages for both platforms with just one code base.

It is necessary to complete installation steps in both platform separately.

## Step 1: Integrate the Braze Library

Add Braze React Native SDK package.

```bash
npm install react-native-appboy-sdk
# or using yarn
# yarn add react-native-appboy-sdk
```

Follow the steps below to complete the installation on both platforms.

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
<!-- 
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
``` -->

### iOS

```
cd ios && pod install
```

## Step 3: Usage

Once installed, you can `import` the library in your React Native code:
```javascript
import ReactAppboy from 'react-native-appboy-sdk';
```


[1]: https://www.braze.com/docs/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/ "Android SDK Install"
[2]: https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/ "iOS SDK Install"
