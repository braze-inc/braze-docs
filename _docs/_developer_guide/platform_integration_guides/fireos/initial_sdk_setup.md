---
nav_title: Initial SDK Setup
platform: FireOS
page_order: 0

---
# Initial SDK Setup

Installing the Braze SDK will provide you with basic analytics functionality as well as working in-app messages with which you can engage your users.

## Android SDK Integration

### Step 1: Integrate the Braze Library
The Braze Android SDK can optionally be integrated without UI components. However, Content Cards, News Feed, and In-App Messaging will be rendered inoperable unless you pass the custom data to a UI solely of your design. Additionally, push notifications will not work because our push handling code is in the UI library. Please note that these UI elements are open source and [fully customizable][1]. We strongly recommend the integration of these features. Please refer to [Braze Docs][2] for the benefits of using the Braze Content Cards, News Feed, and In-App Message UI.

#### Basic Integration
In order to access Braze's messaging features, you must integrate the UI library. Please see the following directions to integrate the UI library depending on your IDE:

#### Using Android Studio

##### Step 1: Add our repository

In your top-level project `build.gradle`, add:

```
maven { url "https://appboy.github.io/appboy-android-sdk/sdk" }
maven { url "https://maven.google.com" }
```

as repositories under `allprojects` -> `repositories`.

For example:

```
allprojects {
  repositories {
    jcenter()
    maven { url "https://appboy.github.io/appboy-android-sdk/sdk" }
    maven { url "https://maven.google.com" }
  }
}
```

Alternatively, you may install the `android-sdk-ui` as an AAR file to your local maven repository. See the [SDK Readme][37] for details.

> See the [Android Support Library Setup instructions][65] for more information on the google maven repository.

##### Step 2: Add Braze dependency

See the following example in our [Hello Appboy example project][45]:

<script src="https://gist-it.appspot.com/https://github.com/Appboy/appboy-android-sdk/blob/master/hello-appboy/build.gradle?slice=1:5&footer=minimal"></script>

The below example shows where to place the dependency line in your `build.gradle`. Note that the version used in the example below uses an old version. Please visit [Braze Android SDK Releases][60] for the most up to date version of the Braze Android SDK.

![MavenScreen2][32]

##### Step 3: Perform Gradle Sync

Be sure to perform a Gradle Sync to build your project and incorporate the dependency additions noted above.

![GradleSync][38]

### Step 2: Configure the Braze SDK in braze.xml

{% alert note %}
Note that as of December 2019, custom endpoints are no longer given out, if you have a pre-existing custom endpoint, you may continue to use it. For a list of our available endpoints, <a href="{{site.baseurl}}/api/basics/#endpoints">click here</a>.
{% endalert %}

Now that the libraries have been integrated, you have to create an `braze.xml` file in your project's `res/values` folder. If you are on a [specific data cluster][66] or have a pre-existing custom endpoint, you need to specify the [endpoint][67] in your `braze.xml` file as well. The contents of that file should resemble the following code snippet:

>  Be sure to substitute the API key found within the App Settings page of the Braze dashboard for `REPLACE_WITH_YOUR_API_KEY`. To find out your specific cluster please ask your Customer Success Manager or email [open a support ticket][support].

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_appboy_api_key">REPLACE_WITH_YOUR_API_KEY</string>
<string translatable="false" name="com_appboy_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

### Step 3: Add Required Permissions to Android Manifest
Now that you've added your API key, you need to add the following permissions to your `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

>  With the release of Android M, Android switched from an install-time to a runtime permissions model. However, both of these permissions are normal permissions and are granted automatically if listed in the app manifest. For more information, visit Android's [permission documentation][46].

### Step 4: Tracking User Sessions in Android

#### Activity Lifecycle Callback Integration (API 14+)

{% alert warning %}
Our minimum supported version is `API 16`.
{% endalert %}

This feature is supported on API 14 and above. Calls to `openSession()`, `closeSession()`,[`ensureSubscribedToInAppMessageEvents()`][64], and `InAppMessageManager` registration are optionally handled automatically. See the [HelloBraze sample application][62] for a full example.

##### Instructions
Add the following code to the `onCreate()` method of your Application class:

```java
registerActivityLifecycleCallbacks(new AppboyLifecycleCallbackListener());
```

You may refer to the following example inside Hello Appboy:

![ActivityLifecycleCallbackIntegration][58]

The first argument instructs the listener to handle `openSession()` and `closeSession()` calls.
The second argument instructs the listener to handle `registerInAppMessageManager()` and `unregisterInAppMessageManager()` calls.

See the [javadoc][63] for more information. Please note that any non-standard manual session integration is not fully supported.

### Step 5: Custom Endpoint Setup {#step-5-optional-custom-endpoint-setup}

{% alert note %}
Note that as of December 2019, custom endpoints are no longer given out, if you have a pre-existing custom endpoint, you may continue to use it. For a list of our available endpoints, <a href="{{site.baseurl}}/api/basics/#endpoints">click here</a>.
{% endalert %}

Your Braze representative should have already advised you of the [correct endpoint]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/).

To update the default endpoint in your integration of the Braze SDKs please add the following code to your `braze.xml`:

```
<string translatable="false" name="com_appboy_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
```

SDK Endpoint configuration via `braze.xml` is available starting with Braze Android SDK v2.1.1.

### Step 6: Enable Location Tracking

If you would like to enable Braze location collection, update your `braze.xml` file to include `com_appboy_enable_location_collection` and ensure its value is set to `true`.

```xml
<bool name="com_appboy_enable_location_collection">true</bool>
```

{% alert important %}
Starting with Braze Android SDK version 3.6.0 Braze location collection is disabled by default.
{% endalert %}

### SDK Integration Complete
Braze will now be able to collect [specified data from your application]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/overview/) and your basic integration should be complete.

Please see the following sections in order to enable [custom event tracking]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events), [push messaging]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/), the [news feed]({{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/overview/) and the [complete suite]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) of Braze features.

## Test Your Basic Integration

### Confirm Session Tracking Is Working
At this point, you should have session tracking working in your Braze integration.  To test this, go to **Overview**, select your application from the selected app name dropdown (defaulted to "All Apps"), and set **Display Data For** to "Today". Then open your app and refresh the page - your main metrics should all have increased by 1.

![Sessions working][55]

You should continue to test your integration by navigating through your application and ensuring that only one session has been logged.  Then, background the app for at least 10 seconds and bring it to the foreground again - by default a new session is created if the app is foregrounded after more than 10 seconds not in the foreground (backgrounded or closed).  Once you've done this, confirm that another session was logged.

### Debugging Session Tracking
If session tracking is behaving unexpectedly, turn on [Verbose Logging][56] and observe your app while you reproduce session triggering steps.  Observe Braze statements in the logcat to detect where you may have missed logging `openSession` and `closeSession` calls in your activities.

### Confirm Device Data is Collected
At this point, you should also have default device data collection working in your app.  To observe this working correctly navigate to the `Devices & Carriers` section of your dashboard, select your application from the select box (defaulted to `All Apps`), and set `Display Data For` to be `Today`.

![Android Device Data][57]

## Additional Customization and Configuration

### Using Proguard with Braze
[Proguard][50] configuration is automatically included with your Braze integration.

Client apps that Proguard Braze code must store release mapping files for Braze to interpret stack traces. If you would like to continue to keep all Braze code, add the following to your Proguard configuration:

```
-keep class bo.app.** { *; }
-keep class com.appboy.** { *; }
```

If you are integrating Baidu Cloud Push with Braze, add:

```
-dontwarn com.baidu.**
-keep class com.baidu.** { *; }
```

### Braze Log Level

The default Log Level for the Braze Android SDK is `INFO`. This level includes push payload logs and basic Braze server communication logs.

To change the Braze Log Level, call `AppboyLogger.setLogLevel()` with one of the [`android.util.Log`][54] priority constants or `AppboyLogger.SUPPRESS`. For example:

```java
// Change log level to VERBOSE
AppboyLogger.setLogLevel(Log.VERBOSE);

// Suppress logs
AppboyLogger.setLogLevel(AppboyLogger.SUPPRESS);
```

#### Verbose Logging

When debugging Braze behavior, set the Log level to `Verbose` before your first call to Braze, preferably in your `Application.onCreate()`. This Log level contains every log made by the Braze SDK. This is only intended to be used in development environments and should not be set in a released application.

>  If the Braze API Key from the "App Settings" page is not present in `braze.xml` then an error message is logged to the Android logcat.

>  If required permissions `ACCESS_NETWORK_STATE` and `INTERNET` are not declared in the manifest, an error message is logged to the Android logcat.

### Multiple API Keys

The most common use case for multiple API keys is separating API keys for debug and release build variants.

To easily switch between multiple API keys in your builds, we recommend creating a separate `braze.xml` file for each relevant [build variant][3]. A build variant is a combination of build type and product flavor. Note that by default, [a new Android project is configured with `debug` and `release` build types][8] and no product flavors.

For each relevant build variant, create a new `braze.xml` for it in `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_appboy_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

When the build variant is compiled, it will use the new API key.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/#news-feed-customization
[2]: {{site.baseurl}}/user_guide/introduction/
[3]: https://developer.android.com/studio/build/build-variants.html
[8]: http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types
[32]: {% image_buster /assets/img_archive/androidstudio2.png %}
[37]: https://github.com/Appboy/appboy-android-sdk/blob/master/README.md
[38]: {% image_buster /assets/img_archive/androidstudio3.png %}
[45]: https://github.com/Appboy/appboy-android-sdk/blob/master/hello-appboy/build.gradle#L4
[46]: https://developer.android.com/training/permissions/index.html
[50]: https://developer.android.com/tools/help/proguard.html
[54]: https://developer.android.com/reference/android/util/Log.html
[55]: {% image_buster /assets/img_archive/android_sessions.png %}
[56]: {{site.baseurl}}/developer_guide/Platform_Integration_Guides/FireOS/Initial_SDK_Setup/#verbose-logging
[57]: {% image_buster /assets/img_archive/android_device_data.png %}
[58]: {% image_buster /assets/img_archive/activity_lifecycle_callback_integration.png %}
[60]: https://github.com/Appboy/appboy-android-sdk/releases
[62]: https://github.com/Appboy/appboy-android-sdk/blob/master/hello-appboy/src/main/java/com/appboy/helloworld/HelloAppboyApplication.java
[63]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/AppboyLifecycleCallbackListener.html#AppboyLifecycleCallbackListener-boolean-boolean-
[64]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#ensureSubscribedToInAppMessageEvents-android.content.Context-
[65]: https://developer.android.com/topic/libraries/support-library/setup.html#add-library
[66]: {{site.baseurl}}/developer_guide/eu01_us3_sdk_implementation_differences/overview/
[67]: {{site.baseurl}}/developer_guide/eu01_us3_sdk_implementation_differences/overview/#sdk-implementation
[support]: {{site.baseurl}}/support_contact/
