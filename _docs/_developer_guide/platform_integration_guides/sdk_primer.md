---
nav_title: SDK Primer
page_order: 0
hidden: true
---

# SDK Primer

Before you begin to integrate the Braze SDKs, you may find yourself wondering what exactly you're building and integrating. Further, you may find yourself curious about how you can customize it further to meet your needs. This article can help you answer all of your SDK questions.

## Feature Set Defaults

If you follow our integration guides to implement our SDKs, you will be able to take advantage of our default features, listed below.

{% alert note %}
All our our features are configurable, but it would not be advantageous to avoid these in your integration.
{% endalert %}

| Configuration | Role | Applicable Platforms |
|---|---|---|
| Session Start <br> `session_start` | Collects information on when your app is opened by your user. | All |
| Session End <br> `session_end` | Collects information on when your app is closed by your user. | All |
| Device Objects | Collects device information to enable successful delivery of messages. | All |

### Device Properties

{% tabs %}
{% tab Web SDK %}

These properties are collected by the Web SDK upon proper integration.

| Name | Description | Example |
|---|---|---|
| BROWSER | The name of the browser. | Chrome |
| BROWSER_VERSION | The version of the browser. | 59.234.1234 |
| OS | The name of the operating system. | Android |
| RESOLUTION | The screen resolution of the device. | 1024x768 |
| LANGUAGE | The language the browser is set to use. | en-us |
| TIME_ZONE | The time zone of the device. | America/New_York |
| USER_AGENT | The user agent string of the browser. <br> See the [Mozilla developer docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) for more information. | Mozilla/<version> (<system-information>) <platform> (<platform-details>) <extensions>
 {% endtab %}
 {% tab Android SDK %}

These properties are collected by the Android SDK upon proper integration.

| Name | Description | Example |
|---|---|---|
| ANDROID_VERSION <br> `os_version` | The version of the Android OS installed on the device. | Android 9.0 Pie (API 28) |
| CARRIER | The mobile carrier.
| MODEL | The specific hardware of the device
| RESOLUTION | Device resolution as "<width>x<height>".
| LOCALE | The default locale of the device. The format of this key is "en_US" or "language_COUNTRY".
| TIMEZONE <br> `time_zone` | The device time zone.
| NOTIFICATIONS_ENABLED <br> `remote_notification_enabled` | Whether this app has notifications enabled.

{% endtab %}
{% tab iOS SDK %}

These properties are collected by the iOS SDK upon proper integration.

| Name | Description | Example |
|---|---|---|
| Device Resolution <br> `ABKDeviceOptionResolution`| The device's reported resolution. |  |
| Device Carrier <br> `ABKDeviceOptionCarrier`| The reported mobile carrier. | Verizon |
| Device Locale <br> `ABKDeviceOptionLocale`| The default locale of the device. |
| Device Model <br> `ABKDeviceOptionModel`| Device resolution as "<width>x<height>".
| Device OS Version <br> `ABKDeviceOptionOSVersion` | The version of the iOS OS installed on the device. |
| Device IDFV <br> `ABKDeviceOptionIDFV`| .
| Device IDFA <br> `ABKDeviceOptionIDFA`| .
| Device Push Enabled <br> `ABKDeviceOptionPushEnabled`| Whether this app has push notifications enabled.
| Device Timezone <br> `ABKDeviceOptionTimezone`| The reported timezone of the device.
| Device Push Authorization Status <br> `ABKDeviceOptionPushAuthStatus`| Whether this app has push authorization for the device.
| Device Ad Tracking Enabled <br> `ABKDeviceAdTrackingEnabled`| Whether this app has Ad Tracking enabled.

{% endtab %}
{% endtabs %}

## SDK vs. API

Why choose between the two? When used in tandem, our product works best for you
