---
nav_title: Initial SDK Setup
article_title: Initial SDK Setup for React Native
platform: React Native
page_order: 1
description: "This reference introduces the React Native SDK and explains how to integrate it natively on Android and iOS."

---

# Initial SDK setup

Installing the Braze React Native SDK provides basic analytics functionality and lets you integrate in-app messages and Content Cards for both iOS and Android with just one codebase.

You will need to complete installation steps on both platforms separately.

To complete the installation, you will need the [App Identifier API key]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) as well as the [SDK endpoint]({{site.baseurl}}/api/basics/#endpoints). Both are located under **Manage Settings** in the dashboard.

## Step 1: Integrate the Braze library

Add the Braze React Native SDK package.

```bash
npm install react-native-appboy-sdk
# or using yarn
# yarn add react-native-appboy-sdk
```

## Step 2: Complete native setup

{% tabs %}
{% tab Android %}

#### Step 2.1a: Add our repository

In your top-level project `build.gradle`, add the following as repositories under `allprojects` > `repositories`:

```gradle
allprojects {
  repositories {
    ...
    maven { url "https://appboy.github.io/appboy-android-sdk/sdk" }
  }
}
```

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

#### Step 2.2a: Install pods

Since React Native automatically links the libraries to the native platform, you can install the SDK with the help of CocoaPods.

From the root folder of the project:

```bash
cd ios && pod install
```

#### Step 2.2b: Configure the Braze SDK


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

Then, add your SDK Endpoint in the `Info.plist` file. It is located in the `ios` project folder. If you're working in Xcode:

1. Add a row with the name `Braze` and type of `Dictionary`.
2. To that Dictionary, add a row with the name `Endpoint`, type `String` and as a value, input your [SDK endpoint]({{site.baseurl}}/api/basics/#endpoints). 

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

Once installed, you can `import` the library in your React Native code:

```javascript
import ReactAppboy from "react-native-appboy-sdk";
```

## Test your basic integration

At this point, you can verify that the SDK is integrated by checking session statistics in the dashboard. If you run your application on either platform, you should see a new session in dashboard (in the **Overview** section).

You can open a session for a particular user by calling the following code in your app.

```javascript
ReactAppboy.changeUser("user-id");
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

You can then search for the user with `some-user-id` in the dashboard under **User Search**. There, you can verify that session and device data have been logged.


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/ "Android SDK Install"
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/ "iOS SDK Install"