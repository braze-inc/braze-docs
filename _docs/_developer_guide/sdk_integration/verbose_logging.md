---
page_order: 1.4
nav_title: Verbose Logging
article_title: Verbose logging
description: "Learn how to enable verbose logging for the Braze SDK, collect logs for troubleshooting, and share them with Braze Support."
---

# Verbose logging

> Verbose logging outputs detailed, low-level information from the Braze SDK, giving you visibility into how the SDK initializes, communicates with servers, and processes messaging channels like push, in-app messages, and Content Cards.

When something isn't working as expected—such as a push notification not arriving, an in-app message not displaying, or user data not syncing—verbose logs help you identify the root cause. Instead of guessing, you can see exactly what the SDK is doing at each step.

{% alert tip %}
If you want to debug without enabling verbose logging manually, you can use the [SDK Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging) to create debugging sessions directly in the Braze dashboard.
{% endalert %}

## When to use verbose logging

Turn on verbose logging when you need to:

- **Verify SDK initialization**: Confirm the SDK starts correctly with the right API key and endpoint.
- **Troubleshoot message delivery**: Check whether push tokens are registered, in-app messages are triggered, or Content Cards are synced.
- **Debug deep links**: Verify the SDK receives and opens deep links from push, in-app messages, or Content Cards.
- **Validate session tracking**: Confirm sessions start and end as expected.
- **Diagnose connectivity issues**: Inspect the network requests and responses between the SDK and Braze servers.

## Enabling verbose logging

{% alert important %}
Verbose logs are intended for development and testing environments only. Disable verbose logging before releasing your app to production to prevent sensitive information from being exposed.
{% endalert %}

{% tabs %}
{% tab Android %}

Enable verbose logging before any other SDK calls in your `Application.onCreate()` method to capture the most complete output.

**In code:**

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

**In `braze.xml`:**

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```

To verify that verbose logging is enabled, search for `V/Braze` in your Logcat output. For example:

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

For full details, see [Android SDK logging]({{site.baseurl}}/developer_guide/sdk_integration#android_enabling-logs).

{% endtab %}
{% tab Swift %}

Set the log level to `.debug` on your `Braze.Configuration` object during initialization.

{% subtabs %}
{% subtab SWIFT %}
```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.logger.level = .debug
let braze = Braze(configuration: configuration)
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                                                  endpoint:@"<BRAZE_ENDPOINT>"];
[configuration.logger setLevel:BRZLoggerLevelDebug];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```
{% endsubtab %}
{% endsubtabs %}

The `.debug` level is the most verbose and is recommended for troubleshooting. For full details, see [Swift SDK logging]({{site.baseurl}}/developer_guide/sdk_integration#swift_log-levels).

{% endtab %}
{% tab Web %}

Add `?brazeLogging=true` as a URL parameter, or enable logging during SDK initialization:

```javascript
braze.initialize('YOUR-API-KEY', {
    baseUrl: 'YOUR-SDK-ENDPOINT',
    enableLogging: true
});
```

You can also toggle logging after initialization:

```javascript
braze.toggleLogging();
```

Logs appear in the **Console** tab of your browser's developer tools. For full details, see [Web SDK logging]({{site.baseurl}}/developer_guide/sdk_integration#web_logging).

{% endtab %}
{% tab Unity %}

1. Open the Braze Configuration Settings by navigating to **Braze** > **Braze Configuration**.
2. Select the **Show Braze Android Settings** dropdown.
3. In the **SDK Log Level** field, enter `0`.

{% endtab %}
{% tab React Native %}

Set the log level during SDK configuration:

```javascript
const configuration = new Braze.BrazeConfiguration('YOUR-API-KEY', 'YOUR-SDK-ENDPOINT');
configuration.logLevel = Braze.LogLevel.Verbose;
```

{% endtab %}
{% endtabs %}

## Collecting logs

After you enable verbose logging, reproduce the issue you're troubleshooting, then collect the logs from your platform's console or debugging tool.

{% tabs %}
{% tab Android %}

Use **Logcat** in Android Studio to capture logs:

1. Connect your device or start an emulator.
2. In Android Studio, open **Logcat** from the bottom panel.
3. Filter by `V/Braze` or `D/Braze` to isolate Braze SDK output.
4. Reproduce the issue.
5. Copy the relevant logs and save them to a text file.

{% endtab %}
{% tab iOS %}

Use the **Console** app on macOS to capture logs:

1. Install the app on your device with verbose logging enabled.
2. Connect your device to your Mac.
3. Open the **Console** app and select your device from the **Devices** sidebar.
4. Filter logs by `Braze` or `BrazeKit` in the search bar.
5. Reproduce the issue.
6. Copy the relevant logs and save them to a text file.

{% endtab %}
{% tab Web %}

Use your browser's developer tools:

1. Open your browser's developer tools (usually **F12** or **Cmd+Option+I**).
2. Go to the **Console** tab.
3. Reproduce the issue.
4. Copy the console output and save it to a text file.

{% endtab %}
{% endtabs %}

{% alert tip %}
When collecting logs for Braze Support, start logging before launching your app and continue until well after the issue occurs. This helps capture the full sequence of events.
{% endalert %}

## Reading verbose logs

Verbose logs follow a consistent structure that helps you trace what the SDK is doing. To learn how to interpret log output for specific channels, including what key entries to look for and common troubleshooting patterns, see [Reading verbose logs]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs).

## Sharing logs with Braze Support

When you contact Braze Support with an SDK issue, include the following:

1. **Verbose log file**: A complete log capture from before app launch through the issue occurrence.
2. **Steps to reproduce**: A clear description of the actions that trigger the issue.
3. **Expected vs. actual behavior**: What you expected to happen and what happened instead.
4. **SDK version**: The version of the Braze SDK you're using.
5. **Platform and OS version**: For example, iOS 18.0, Android 14, or Chrome 120.