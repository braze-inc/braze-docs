## Integrating the Android SDK

### Step 1: Update your `build.gradle`

In your `build.gradle`, add [`mavenCentral()`](https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api.artifacts.dsl/-repository-handler/maven-central.html) to your list of repositories.

```kotlin
repositories {
  mavenCentral()
}
```

Next, add Braze to your dependencies.

{% tabs local %}
{% tab base only %}
If you don't plan on using Braze UI components, add the following code to your `build.gradle`. Replace `SDK_VERSION` with the current version of your Android Braze SDK. For the full list of versions, see [Changelogs]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android).

```kotlin
dependencies {
    implementation 'com.braze:android-sdk-base:SDK_VERSION' // (Required) Adds dependencies for the base Braze SDK.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endtab %}

{% tab with ui components %}
If you plan on using Braze UI components later, add the following code to your `build.gradle`.  Replace `SDK_VERSION` with the current version of your Android Braze SDK. For the full list of versions, see [Changelogs]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android).

```kotlin
dependencies {
    implementation 'com.braze:android-sdk-ui:SDK_VERSION' // (Required) Adds dependencies for the Braze SDK and Braze UI components. 
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endtab %}
{% endtabs %}

### Step 2: Configure your `braze.xml`

{% alert note %}
As of December 2019, custom endpoints are no longer given out, if you have a pre-existing custom endpoint, you may continue to use it. For more details, refer to our <a href="{{site.baseurl}}/api/basics/#endpoints">list of available endpoints</a>.
{% endalert %}

Create a `braze.xml` file in your project's `res/values` folder. If you are on a specific data cluster or have a pre-existing custom endpoint, you need to specify the endpoint in your `braze.xml` file as well. 

The contents of that file should resemble the following code snippet. Make sure to substitute `YOUR_APP_IDENTIFIER_API_KEY` with the identifier found in the **Manage Settings** page of the Braze dashboard. Log in at [dashboard.braze.com](https://dashboard.braze.com) to find your [cluster address]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

### Step 3: Add permissions to `AndroidManifest.xml`

Next, add the following permissions to your `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
With the release of Android M, Android switched from an install-time to a runtime permissions model. However, both of these permissions are normal permissions and are granted automatically if listed in the app manifest. For more information, visit Android's [permission documentation](https://developer.android.com/training/permissions/index.html).
{% endalert %}

### Step 4: Enable delayed initialization (optional)

To use delayed initialization, the minimum Braze SDK version is required:

{% sdk_min_versions android:38.0.0 %}

{% alert note %}
While delayed initialization is enabled, all network connections will be canceled, and the Braze SDK will not pass data to the Braze servers.
{% endalert %}

#### Step 4.1: Update your `braze.xml`

Delayed initialization is disabled by default. To enable, use one of the following options:

{% tabs %}
{% tab Braze XML file %}
In your project's `braze.xml` file, set `com_braze_enable_delayed_initialization` to `true`.

```xml
<bool name="com_braze_enable_delayed_initialization">true</bool>
```
{% endtab %}

{% tab At runtime %}
To enable delayed initialization at runtime, use the following method.

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Step 4.2: Configure push analytics (optional)

When delayed initialization is enabled, push analytics are queued by default. However, you can choose to [explicitly queue](#explicitly-queue-push-analytics) or [drop](#drop-push-analytics) push analytics instead.

##### Explicitly queue {#explicitly-queue-push-analytics}

To explicitly queue push analytics, choose one of the following options:

{% tabs %}
{% tab Braze XML file %}
In your `braze.xml` file, set `com_braze_delayed_initialization_analytics_behavior` to `QUEUE`:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">QUEUE</string>
```
{% endtab %}

{% tab At runtime %}
Add `QUEUE` to your [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html) method:

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

##### Drop {#drop-push-analytics}

To drop push analytics, choose one of the following options:

{% tabs %}
{% tab Braze XML file %}
In your `braze.xml` file, set `com_braze_delayed_initialization_analytics_behavior` to `DROP`: 

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">DROP</string>
```
{% endtab %}

{% tab At runtime %}
Add `DROP` to [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html) method:

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Step 4.3: Manually initialize the SDK

After your chosen delay period, use the [`Braze.disableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-delayed-initialization.html) method to manually initialize the SDK.

{% tabs local %}
{% tab JAVA %}

```java
Braze.disableDelayedInitialization(context);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.disableDelayedInitialization(context)
```

{% endtab %}
{% endtabs %}

### Step 5: Enable user session tracking

When you enable user session tracking, calls to `openSession()`, `closeSession()`,[`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html), and `InAppMessageManager` registration can be handled automatically.

To register activity lifecycle callbacks, add the following code to the `onCreate()` method of your `Application` class. 

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

For the list of available parameters, see [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

{% endtab %}
{% endtabs %}

## Testing session tracking

{% alert tip %}
You can also use the [SDK Debugger]({{site.baseurl}}/developer_guide/debugging) to diagnose SDK issues.
{% endalert %}

If you experience issues while testing, enable [verbose logging](#android_enabling-logs), then use logcat to detect missing `openSession` and `closeSession` calls in your activities.

1. In Braze, go to **Overview**, select your app, then in the **Display Data For** dropdown choose **Today**.
    ![The "Overview" page in Braze, with the "Display Data For" field set to "Today".]({% image_buster /assets/img_archive/android_sessions.png %})
2. Open your app, then refresh the Braze dashboard. Verify that your metrics have increased by 1.
3. Navigate through your app and verify that only one session has been logged to Braze.
4. Send the app to the background for at least 10 seconds, then bring it to the foreground. Verify that a new session was logged.

## Optional configurations

### Runtime configuration

To set your Braze options in code rather than your `braze.xml` file, use [runtime configuration](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). If a value exists in both places, the runtime value will be used instead. After all required settings are supplied at runtime, you can delete your `braze.xml` file.

In the following example, a [builder object](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) is created and then passed to [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). Note that only some of the available runtime options are shown&#8212;refer to our [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) for the full list.

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Looking for another example? Check out our [Hello Braze sample app](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java).
{% endalert %}

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
suspend fun fetchAndSetAdvertisingId(
  context: Context,
  scope: CoroutineScope = GlobalScope
) {
  scope.launch(Dispatchers.IO) {
    try {
      val idInfo = AdvertisingIdClient.getAdvertisingIdInfo(context)
      Braze.getInstance(context).setGoogleAdvertisingId(
        idInfo.id,
        idInfo.isLimitAdTrackingEnabled
      )
    } catch (e: Exception) {
      e.printStackTrace()
    }
  }
}
```

{% endtab %}
{% endtabs %}

{% alert important %}
Google requires the Advertising ID to be collected on a non-UI thread.
{% endalert %}


### Location tracking

To enable Braze location collection, set `com_braze_enable_location_collection` to `true` in your `braze.xml` file:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Starting with Braze Android SDK version 3.6.0, Braze location collection is disabled by default.
{% endalert %}

### Logging

By default, the Braze Android SDK log level is set to `INFO`. You can [suppress these logs](#android_suppressing-logs) or [set a different log level](#android_enabling-logs), such as `VERBOSE`, `DEBUG`, or `WARN`.

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

To suppress all logs for the Braze Android SDK, set the log level to `BrazeLogger.SUPPRESS` in your application's `onCreate()` method _before_ any other methods.

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

To easily switch between multiple API keys in your builds, we recommend creating a separate `braze.xml` file for each relevant [build variant](https://developer.android.com/studio/build/build-variants.html). A build variant is a combination of build type and product flavor. By default, new Android projects are configured with [`debug` and `release` build types](https://developer.android.com/reference/tools/gradle-api/8.3/null/com/android/build/api/dsl/BuildType) and no product flavors.

For each relevant build variant, create a new `braze.xml` in the `src/<build variant name>/res/values/` directory. When the build variant is compiled, it will use the new API key.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

{% alert tip %}
To learn how to set up the API key in your code, see [Runtime configuration]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android).
{% endalert %}

### Exclusive in-app message TalkBack

In adherence to the [Android accessibility guidelines](https://developer.android.com/guide/topics/ui/accessibility), the Braze Android SDK offers Android Talkback by default. To ensure that only the contents of in-app messages are read out loud—without including other screen elements like the app title bar or navigation—you can enable exclusive mode for TalkBack.

To enable exclusive mode for in-app messages:

{% tabs local %}
{% tab Braze XML %}
```xml
<bool name="com_braze_device_in_app_message_accessibility_exclusive_mode_enabled">true</bool>
```
{% endtab %}

{% tab Kotlin %}
```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```
{% endtab %}

{% tab Java %}
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```
{% endtab %}
{% endtabs %}

### R8 and ProGuard

[Code shrinking](https://developer.android.com/build/shrink-code) configuration is automatically included with your Braze integration.

Client apps that obfuscate Braze code must store release mapping files for Braze to interpret stack traces. If you want to continue to keep all Braze code, add the following to your ProGuard file:

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```
