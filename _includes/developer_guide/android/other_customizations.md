---
nav_title: Other SDK Customizations
article_title: Other SDK customizations for Android and FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "This reference article covers additional customization and configuration options such as verbose logging, suppressing logging, and how to implement multiple API keys."

---

# Other SDK customizations for Android and FireOS

> This reference article covers additional customization and configuration options such as verbose logging, suppressing logging, and how to implement multiple API keys.

## Using R8/ProGuard with Braze

[Code shrinking](https://developer.android.com/studio/build/shrink-code) configuration is automatically included with your Braze integration.

Client apps that obfuscate Braze code must store release mapping files for Braze to interpret stack traces. If you want to continue to keep all Braze code, add the following to your ProGuard file:

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```

## Logging

By default, the Braze Android SDK log level is set to `INFO`. You can [suppress these logs](#suppressing-logs) or [set a different log level](#enabling-logs), such as `VERBOSE`, `DEBUG`, or `WARN`.

### Enabling logs {#enabling-logs}

To help troubleshoot issues in your app, or reduce turnaround times with Braze Support, you'll want to enable verbose logs for the SDK. When you send verbose logs to Braze Support, ensure they begin as soon as you launch your application and end far after your issue occurs.

Keep in mind, verbose logs are only intended for your development environment, so you'll want to disable them before releasing your app.

{% alert important %}
Enable verbose logs before any other calls in `Application.onCreate()` to ensure your logs are as complete as possible.
{% endalert %}

{% tabs local %}
{% tab Application %}
To enable logs directly in your app, add the following to your application's `onCreate()` method before any other methods.

{% subtabs %}
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

For example, the following code will forward log levels `2`, `3`, `4`, `5`, `6`, and `7` to the `Log` method.

{% subtabs %}
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

{% tab braze.xml %}
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

For example, the following code will forward log levels `2`, `3`, `4`, `5`, `6`, and `7` to the `Log` method.

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

### Verifying verbose logs

To verify that your logs are set to `VERBOSE`, check if `V/Braze` occurs somewhere in your logs. If it does, then verbose logs have been successfully enabled. For example:

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

### Suppressing logs

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

## Multiple API keys

The most common use case for multiple API keys is separating API keys for debug and release build variants.

To easily switch between multiple API keys in your builds, we recommend creating a separate `braze.xml` file for each relevant [build variant](https://developer.android.com/studio/build/build-variants.html). A build variant is a combination of build type and product flavor. Note that by default, [a new Android project is configured with `debug` and `release` build types](http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types) and no product flavors.

For each relevant build variant, create a new `braze.xml` for it in `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

When the build variant is compiled, it will use the new API key.

See the [runtime configuration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/) documentation for setting an API key in code.

## Accessibility

You can implement specific Android SDK accessibility features such as in-app message talkback into your Android or FireOS application. The Braze Android SDK follows the [Android accessibility guidelines](https://developer.android.com/guide/topics/ui/accessibility).

### In-app message talkback

In order to have Android Talkback/"VoiceOver" not read the contents behind an in-app message during display, enable the following SDK configuration:

{% tabs local %}
{% tab braze.xml %}

```xml
<bool name="com_braze_device_in_app_message_accessibility_exclusive_mode_enabled">true</bool>
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

{% endtab %}
{% tab JAVA %}

```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

{% endtab %}
{% endtabs %}

## Google Advertising ID (Android only)

The [Google Advertising ID](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en) is an optional user-specific, anonymous, unique, and resettable ID for advertising, provided by Google Play services, that allows users the power to reset their identifier, opt-out of interest-based ads within Google Play apps, and provides developers with a simple, standard system to continue to monetize their apps.

### Passing the Google Advertising ID to Braze

The Google Advertising ID is not automatically collected by the Braze SDK and must be set manually via the [`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) method.

{% alert important %}
Google requires the Advertising ID to be collected on a non-UI thread.
{% endalert %}

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
