---
nav_title: SDK 101
page_order: 0
---

# SDK 101

Before you begin to integrate the Braze SDKs, you may find yourself wondering what exactly you're building and integrating. Further, you may find yourself curious about how you can customize it further to meet your needs. This article can help you answer all of your SDK questions.

## Feature Set Defaults

If you follow our integration guides to implement our SDKs, you will be able to take advantage of our [default data collection]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#automatically-collected-data).

{% alert note %}
All of our features are configurable, but it would not be advantageous to avoid these in your integration. For example, if you choose not to fully integrate for location on one of the SDKs, you will not be able to personalize your messaging based on language or location. However, if necessary, it is possible to [block the default collection of certain data, as well as whitelist processes that do so](#blocking-data-collection).
{% endalert %}

### Device Properties

{% tabs %}
{% tab Web SDK %}

These properties are collected by the Web SDK upon proper integration.

| Name | Description  |
|---|---|
| BROWSER | The name of the browser.  |
| BROWSER_VERSION | The version of the browser. |
| OS | The name of the operating system.  |
| RESOLUTION | The screen resolution of the device. The format of this value is "`<width>`x`<height>`".  |
| LANGUAGE | The language the browser is set to use.  |
| TIME_ZONE | The time zone of the device.  |
| USER_AGENT | The user agent string of the browser. <br> See the [Mozilla developer docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) for more information. |
{: .reset-td-br-1 .reset-td-br-2}

 {% endtab %}
 {% tab Android SDK %}

These properties are collected by the Android SDK upon proper integration.

| Name | Description |
|---|---|
| ANDROID_VERSION <br> `os_version` | The version of the Android OS installed on the device. |
| CARRIER | The mobile carrier. |
| MODEL | The specific hardware of the device. | 
| RESOLUTION | The screen resolution of the device. The format of this value is "`<width>`x`<height>`". |
| LOCALE | The default locale of the device. The format of this value is "`<language>`_`<COUNTRY>`" (e.g. "en_US"). |
| TIMEZONE <br> `time_zone` | The device time zone. |
| NOTIFICATIONS_ENABLED <br> `remote_notification_enabled` | Whether this app has notifications enabled.|
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab iOS SDK %}

These properties are collected by the iOS SDK upon proper integration.

| Name | Description |
|---|---|
| Device Resolution <br> `ABKDeviceOptionResolution`| The screen resolution of the device. The format of this value is "`<width>`x`<height>`". |  
| Device Carrier <br> `ABKDeviceOptionCarrier`| The reported mobile carrier. |
| Device Locale <br> `ABKDeviceOptionLocale`| The default locale of the device. |
| Device Model <br> `ABKDeviceOptionModel`| The specific hardware of the device.
| Device OS Version <br> `ABKDeviceOptionOSVersion` | The version of the iOS OS installed on the device. |
| Device IDFV <br> `ABKDeviceOptionIDFV`| Device identifier for vendors. |
| Device IDFA <br> `ABKDeviceOptionIDFA`| (if supplied) Device identifier for advertisers. |
| Device Push Enabled <br> `ABKDeviceOptionPushEnabled`| Whether this app has push notifications enabled.
| Device Timezone <br> `ABKDeviceOptionTimezone`| The reported timezone of the device.
| Device Push Authorization Status <br> `ABKDeviceOptionPushAuthStatus`| Whether this app has push authorization for the device.
| Device Ad Tracking Enabled <br> `ABKDeviceAdTrackingEnabled`| Whether this app has Ad Tracking enabled. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

## Blocking Data Collection

It is possible, though not suggested, to block the automatic collection of certain data from your SDK integrations. As we stated above, not fully integrating our SDKs can reduce the capabilities of personalization and targeting.

For example, if you choose not to fully integrate for location on one of the SDKs, you will not be able to personalize your messaging based on language or location. If you choose not to integrate for timezone, you might not be able to send messages within a user's timezone. If you choose to not integrate for specific device visual information, message content might not be optimized for that device.

We highly recommend fully integrating the SDKs to take full advantage of our product's capabilties.

### Web SDK

You may either simply not integrate certain parts of the SDK, or use [`stopWebTracking`](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.stopWebTracking) for a user. This method will sync data logged prior to when `stopWebTracking()` was called, and will cause all subsequent calls to the Braze Web SDK for this page and future page loads to be ignored. If you wish to resume data collection at a later point in time, you can use the [`resumeWebTracking()`](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.resumeWebTracking) method in the future to resume data collection. You can learn more about this in our [Disabling Web Tracking]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/disabling_tracking/) article.

### Android SDK

You can use [`setDeviceObjectAllowlist`](https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/configuration/AppboyConfig.Builder.html#setDeviceObjectAllowlist-java.util.EnumSet-) to configure to only send a subset of the device object keys or values according to a set allowlist. This must be enabled via [`setDeviceObjectAllowlistEnabled`](https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/configuration/AppboyConfig.Builder.html#setDeviceObjectAllowlistEnabled-boolean-).

{% alert important %}
An empty allowlist will result in __no__ device data being sent to Braze.
{% endalert %}

### iOS SDK

You can use [`ABKDeviceWhitelistKey;`](https://github.com/Appboy/appboy-ios-sdk/blob/4e26a9a3ba7a86c9bc6bd8080deed1e97e7bf53a/AppboyKit/headers/AppboyKitLibrary/Appboy.h#L108) to specify a whitelist for device fields that are collected by the SDK. Fields are defined in `ABKDeviceOptions`. To turn off all fields, set the value of this key to `ABKDeviceOptionNone`.

{% alert important %}
By default, all fields are collected by the Braze iOS SDK.
{% endalert %}
