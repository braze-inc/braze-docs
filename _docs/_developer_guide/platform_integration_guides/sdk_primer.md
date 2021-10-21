---
nav_title: SDK 101
page_order: 0
---

# SDK 101

Before you begin to integrate the Braze SDKs, you may find yourself wondering what exactly you're building and integrating. Further, you may find yourself curious about how you can customize it further to meet your needs. This article can help you answer all of your SDK questions.

## App performance

Braze should have no negative impact on your app’s performance.

The Braze SDKs have a very small footprint. We automatically change the rate that we flush user data depending on the quality of the network, in addition to allowing manual network control. We automatically batch API requests from the SDK to make sure that data is logged quickly while maintaining maximum network efficiency. Lastly, the amount of data sent from the client to Braze within each API call is extremely small.

## Feature set defaults

If you follow our integration guides to implement our SDKs, you will be able to take advantage of our [default data collection]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#automatically-collected-data).

{% alert note %}
All of our features are configurable, but it would not be advantageous to avoid these in your integration. 

<br>For example, if you choose not to fully integrate for location on one of the SDKs, you will not be able to personalize your messaging based on language or location. If necessary, it is possible to [block the default collection of certain data, as well as allowlist processes that do so](#blocking-data-collection).
{% endalert %}

### Device properties

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
| Device Timezone <br> `ABKDeviceOptionTimezone`| The reported time zone of the device.
| Device Push Authorization Status <br> `ABKDeviceOptionPushAuthStatus`| Whether this app has push authorization for the device.
| Device Ad Tracking Enabled <br> `ABKDeviceAdTrackingEnabled`| Whether this app has Ad Tracking enabled. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

## Data upload and download

The Braze SDK caches data (sessions, custom events, etc) and uploads it periodically. Only after the data has been uploaded will the values be updated on the dashboard. The upload interval takes into account the state of the device and is governed by the quality of the network connection:

|Network Connection Quality |    Data Flush Interval|
|---|---|
|Great    |10 Seconds|
|Good    |30 Seconds|
|Poor    |60 Seconds|
{: .reset-td-br-1 .reset-td-br-2}

If there is no network connection, data is cached locally on the device until the network connection is re-established. When the connection is re-established, the data will be uploaded to Braze.

Braze sends data to the SDK at the beginning of a session based on which segments the user falls into at the time of the session. The News Feed or new in-app messages will not be updated during the session. However, user data during the session will be continually processed as it is sent from the client. For example, a lapsed user (last used the app more than 7 days ago) will still receive content targeted at lapsed users on their first session back in the app.

## Blocking data collection

It is possible, though not suggested, to block the automatic collection of certain data from your SDK integrations. As we stated above, not fully integrating our SDKs can reduce the capabilities of personalization and targeting.

For example, if you choose not to fully integrate for location on one of the SDKs, you will not be able to personalize your messaging based on language or location. If you choose not to integrate for time zone, you might not be able to send messages within a user's time zone. If you choose to not integrate for specific device visual information, message content might not be optimized for that device.

We highly recommend fully integrating the SDKs to take full advantage of our product's capabilties.

### Web sdk

You may either simply not integrate certain parts of the SDK, or use [`stopWebTracking`](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.stopWebTracking) for a user. This method will sync data logged prior to when `stopWebTracking()` was called, and will cause all subsequent calls to the Braze Web SDK for this page and future page loads to be ignored. If you wish to resume data collection at a later point in time, you can use the [`resumeWebTracking()`](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.resumeWebTracking) method in the future to resume data collection. You can learn more about this in our [Disabling Web Tracking]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/disabling_tracking/) article.

### Android sdk

You can use [`setDeviceObjectAllowlist`](https://appboy.github.io/appboy-android-sdk/javadocs/) to configure to only send a subset of the device object keys or values according to a set allowlist. This must be enabled via `setDeviceObjectAllowlistEnabled`.

{% alert important %}
An empty allowlist will result in __no__ device data being sent to Braze.
{% endalert %}

### iOS sdk

You can pass an `appboyOptions` value for `ABKDeviceAllowlistKey` to specify an allowlist for device fields that are collected by the SDK. Fields are defined in `ABKDeviceOptions`. To turn off the collection of all device fields, set the value of this key to `ABKDeviceOptionNone`.

To specify allowlisted device fields, assign the bitwise OR of desired fields to `ABKDeviceAllowlistKey` in the `appboyOptions` object passed to `startWithApiKey`.

{% alert important %}
By default, all fields are collected by the Braze iOS SDK.
{% endalert %}

## SDK compatibility

Braze's SDK is designed to be very well-behaved, and not interfere with other SDKs present in your mobile app. If you are experiencing any issues you think might be due to incompatibility with another mobile SDK, please reach out to Braze Support.

Additionally, the Braze iOS SDK fully supports RubyMotion apps.
