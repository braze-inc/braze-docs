---
page_order: 0
nav_title: SDK Integration
article_title: Integrating the Braze Android SDK
description: Learn how to integrate the Braze Android SDK.
---

# Integrating the Braze Android SDK

> Learn how to integrate the Braze Android SDK. To learn more about the SDK in general, see [Getting started: Integration overview]({{site.baseurl}}/developer_guide/getting_started/integration_overview/).

## Integrating the SDK

### Step 1: Integrate the UI library (optional)

Although skipping this step is possible, it is not recommended. You must integrate the Braze UI library to use push notifications, in-app messaging, and Content Cards.

In your Android Studio project, add the `android-sdk-ui` dependency to your app's `build.gradle`. If you're using any location or Braze Geofence functionality, also include `android-sdk-location` in your app's `build.gradle`.

{% alert important %}
If you're using a non-native Android SDK (for example, Flutter, Cordova, Unity, etc.), that SDK already has the `android-sdk-ui` dependency for the correct version of the Android SDK. Do not update that version manually.
{% endalert %}

```gradle
dependencies {
  implementation "com.braze:android-sdk-ui:+"
  implementation "com.braze:android-sdk-location:+"
}
```

The following example shows where to place the dependency line in your `build.gradle`. Note that the version used in the example uses an old version. Visit [Braze Android SDK releases](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md) for the most up-to-date version of the Braze Android SDK.

![Android studio displaying the "build.gradle", with the dependency code added to the end of the file.]({% image_buster /assets/img_archive/androidstudio2.png %})

Be sure to perform a Gradle sync to build your project and incorporate the [dependency additions](#add-braze-dependency).

![A banner in Android Studio stating: "Gradle files have changed since last project sync. A project sync may be necessary for the IDE to work properly. Sync Now."]({% image_buster /assets/img_archive/androidstudio3.png %})

### Step 2: Configure the Braze SDK in braze.xml

{% alert note %}
As of December 2019, custom endpoints are no longer given out, if you have a pre-existing custom endpoint, you may continue to use it. For more details, refer to our <a href="{{site.baseurl}}/api/basics/#endpoints">list of available endpoints</a>.
{% endalert %}

Next, create a `braze.xml` file in your project's `res/values` folder. If you are on a specific data cluster or have a pre-existing custom endpoint, you need to specify the endpoint in your `braze.xml` file as well. 

The contents of that file should resemble the following code snippet. Make sure to substitute `YOUR_APP_IDENTIFIER_API_KEY` with the identifier found in the **Manage Settings** page of the Braze dashboard. Log in at [dashboard.braze.com](https://dashboard.braze.com) to find your [cluster address]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

### Step 3: Add required permissions to AndroidManifest.xml

Next, add the following permissions to your `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
With the release of Android M, Android switched from an install-time to a runtime permissions model. However, both of these permissions are normal permissions and are granted automatically if listed in the app manifest. For more information, visit Android's [permission documentation](https://developer.android.com/training/permissions/index.html).
{% endalert %}

### Step 4: Enable user session tracking

Calls to `openSession()`, `closeSession()`,[`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html), and `InAppMessageManager` registration are optionally handled automatically.

To register activity lifecycle callbacks, add the following code to the `onCreate()` method of your `Application` class:

{% tabs local %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
  }
}
```

{% endtab %}
{% endtabs %}

See our SDK reference documentation for more information on the parameters available for [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

### Step 5: Enable location tracking

To enable Braze location collection, update your `braze.xml` file to include `com_braze_enable_location_collection` and ensure its value is set to `true`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Starting with Braze Android SDK version 3.6.0, Braze location collection is disabled by default.
{% endalert %}

### Step 6: Test session tracking (optional)

If you experience issues while testing, enable [verbose logging](#enabling-logs), then use logcat to detect missing `openSession` and `closeSession` calls in your activities.

1. In Braze, go to **Overview**, select your app, then in the **Display Data For** dropdown choose **Today**.
    ![The "Overview" page in Braze, with the "Display Data For" field set to "Today".]({% image_buster /assets/img_archive/android_sessions.png %})
2. Open your app, then refresh the Braze dashboard. Verify that your metrics have increased by 1.
3. Navigate through your app and verify that only one session has been logged to Braze.
4. Send the app to the background for at least 10 seconds, then bring it to the foreground. Verify that a new session was logged.

## Optional configurations

### Google Advertising ID

The [Google Advertising ID (GAID)](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en) is an optional user-specific, anonymous, unique, and resettable ID for advertising, provided by Google Play services. GAID gives users the power to reset their identifier, opt-out of interest-based ads within Google Play apps, and provides developers with a simple, standard system to continue to monetize their apps.

The Google Advertising ID is not automatically collected by the Braze SDK and must be set manually via the [`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) method.

{% tabs local %}
{% tab JAVA %}

```java
new Thread(new Runnable() {
  @Override
  public void run() {
    try {
      AdvertisingIdClient.Info idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext());
      Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.getId(), idInfo.isLimitAdTrackingEnabled());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}).start();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Thread(Runnable {
  try {
    val idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext())
    Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.id, idInfo.isLimitAdTrackingEnabled)
  } catch (e: Exception) {
    e.printStackTrace()
  }
}).start()
```

{% endtab %}
{% endtabs %}

{% alert important %}
Google requires the Advertising ID to be collected on a non-UI thread.
{% endalert %}

### Logging

By default, the Braze Android SDK log level is set to `INFO`. You can [suppress these logs](#suppressing-logs) or [set a different log level](#enabling-logs), such as `VERBOSE`, `DEBUG`, or `WARN`.

#### Enabling logs

To help troubleshoot issues in your app, or reduce turnaround times with Braze Support, you'll want to enable verbose logs for the SDK. When you send verbose logs to Braze Support, ensure they begin as soon as you launch your application and end far after your issue occurs.

Keep in mind, verbose logs are only intended for your development environment, so you'll want to disable them before releasing your app.

{% alert important %}
Enable verbose logs before any other calls in `Application.onCreate()` to ensure your logs are as complete as possible.
{% endalert %}

{% tabs local %}
{% tab Application %}
To enable logs directly in your app, add the following to your application's `onCreate()` method before any other methods.

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.MIN_LOG_LEVEL);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.MIN_LOG_LEVEL
```
{% endsubtab %}
{% endsubtabs %}

Replace `MIN_LOG_LEVEL` with the **Constant** of the log level you'd like to set as your minimum log level. Any logs at a level `>=` to your set `MIN_LOG_LEVEL` will be forwarded to Android's default [`Log`](https://developer.android.com/reference/android/util/Log) method. Any logs `<` your set `MIN_LOG_LEVEL` will be discarded.

| Constant    | Value          | Description                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Logs the most detailed messages for debugging and development.            |
| `DEBUG`     | 3              | Logs descriptive messages for debugging and development.                  |
| `INFO`      | 4              | Logs informational messages for general highlights.                       |
| `WARN`      | 5              | Logs warning messages for identifying potentially harmful situations.     |
| `ERROR`     | 6              | Logs error messages for indicating application failure or serious issues. |
| `ASSERT`    | 7              | Logs assertion messages when conditions are false during development.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

For example, the following code will forward log levels `2`, `3`, `4`, `5`, `6`, and `7` to the `Log` method.

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab xml %}
To enable logs in the `braze.xml`, add the following to your file:

```xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

Replace `MIN_LOG_LEVEL` with the **Value** of the log level you'd like to set as your minimum log level. Any logs at a level `>=` to your set `MIN_LOG_LEVEL` will be forwarded to Android's default [`Log`](https://developer.android.com/reference/android/util/Log) method. Any logs `<` your set `MIN_LOG_LEVEL` will be discarded.

| Constant    | Value          | Description                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Logs the most detailed messages for debugging and development.            |
| `DEBUG`     | 3              | Logs descriptive messages for debugging and development.                  |
| `INFO`      | 4              | Logs informational messages for general highlights.                       |
| `WARN`      | 5              | Logs warning messages for identifying potentially harmful situations.     |
| `ERROR`     | 6              | Logs error messages for indicating application failure or serious issues. |
| `ASSERT`    | 7              | Logs assertion messages when conditions are false during development.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

For example, the following code will forward log levels `2`, `3`, `4`, `5`, `6`, and `7` to the `Log` method.

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

#### Verifying verbose logs

To verify that your logs are set to `VERBOSE`, check if `V/Braze` occurs somewhere in your logs. If it does, then verbose logs have been successfully enabled. For example:

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

#### Suppressing logs

The default log level for the Braze Android SDK is `INFO`. To suppress all logs for the Braze Android SDK, call `BrazeLogger.SUPPRESS` in your application's `onCreate()` method _before_ any other methods.

{% tabs local %}
{% tab JAVA %}
```java
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```
{% endtab %}
{% endtabs %}

### Multiple API keys

The most common use case for multiple API keys is separating API keys for debug and release build variants.

To easily switch between multiple API keys in your builds, we recommend creating a separate `braze.xml` file for each relevant [build variant](https://developer.android.com/studio/build/build-variants.html). A build variant is a combination of build type and product flavor. By default, new Android projects are configured with [`debug` and `release` build types](http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types) and no product flavors.

For each relevant build variant, create a new `braze.xml` in the `src/<build variant name>/res/values/` directory. When the build variant is compiled, it will use the new API key.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

{% alert tip %}
To learn how to set up the API key in your code, see [Runtime configuration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/).
{% endalert %}

### R8 and ProGuard

[Code shrinking](https://developer.android.com/studio/build/shrink-code) configuration is automatically included with your Braze integration.

Client apps that obfuscate Braze code must store release mapping files for Braze to interpret stack traces. If you want to continue to keep all Braze code, add the following to your ProGuard file:

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```
