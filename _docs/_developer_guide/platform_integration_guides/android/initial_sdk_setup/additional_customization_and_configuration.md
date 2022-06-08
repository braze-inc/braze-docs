---
nav_title: Other SDK Customizations
article_title: Other SDK Customizations for Android and FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "This article covers additional customization and configuration options such as verbose logging, suppressing logging, and how to implement multiple API keys."

---

# Additional customization and configuration

## Using R8/ProGuard with Braze
[Code shrinking][50] configuration is automatically included with your Braze integration.

Client apps that obfuscate Braze code must store release mapping files for Braze to interpret stack traces. If you would like to continue to keep all Braze code, add the following to your ProGuard file:

```
-keep class bo.app.** { *; }
-keep class com.appboy.** { *; }
```

## Enabling verbose logging {#android-verbose-logging}

Verbose logs from the Braze SDK are essential to a fast turnaround on support issues. These logs should not be modified for clarity; long log files are preferred. Verbose logging is only intended for development environments and should not be enabled in a released application. Logs sent to our support team should begin as soon as the application is launched and end well after the observed issue occurs.

To enable verbose logging on the Braze Android SDK:

{% tabs %}
{% tab JAVA %}

```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeLogger.setLogLevel(Log.VERBOSE)
```

{% endtab %}
{% endtabs %}

{% alert important %}
Verbose logs should be enabled as early as possible in your `Application.onCreate()`, before any other calls to the SDK to guarantee as much logging as possible.
{% endalert %}

To know if your obtained logs are verbose, look for `V/Braze` somewhere in your logs. For example:

`2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started`

### Suppressing Braze SDK logging

The default log level for the Braze Android SDK is `INFO`.

To change the Braze log level, call [`BrazeLogger.setLogLevel()`][70] with one of the [`android.util.Log`][54] constants or `BrazeLogger.SUPPRESS`. For example:

{% tabs %}
{% tab JAVA %}

```java
// Suppress all logs
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Suppress all logs
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```

{% endtab %}
{% endtabs %}

## Multiple API keys

The most common use case for multiple API keys is separating API keys for debug and release build variants.

To easily switch between multiple API keys in your builds, we recommend creating a separate `braze.xml` file for each relevant [build variant][3]. A build variant is a combination of build type and product flavor. Note that by default, [a new Android project is configured with `debug` and `release` build types][8] and no product flavors.

For each relevant build variant, create a new `braze.xml` for it in `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

When the build variant is compiled, it will use the new API key.

See the [runtime configuration][69] documentation for setting an API key in code.

[3]: https://developer.android.com/studio/build/build-variants.html
[8]: http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types
[50]: https://developer.android.com/studio/build/shrink-code
[54]: https://developer.android.com/reference/android/util/Log.html
[69]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/
[70]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.support/-braze-logger/log-level.html
