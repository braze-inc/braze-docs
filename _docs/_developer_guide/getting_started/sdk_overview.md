---
nav_title: SDK Overview
article_title: SDK Overview for Developers
description: "This onboarding reference article provides a technical overview for developers of the Braze SDK. It discusses default analytics tracked by the SDK, blocking automatic data collection, and the live SDK version of your app."
page_order: 0
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}SDK overview for developers

> Before you begin to integrate the Braze SDKs, you may find yourself wondering what exactly you're building and integrating. You may be curious about how you can customize the SDK to further to meet your needs. This article can help you answer all of your SDK questions. 

Are you a marketer looking for a basic rundown of the SDK? Check out our [marketer overview]({{site.baseurl}}/user_guide/getting_started/web_sdk/), instead.

In brief, the Braze SDK:
* Collects and syncs user data into a consolidated user profile
* Automatically collects session data, device info, and push tokens
* Captures marketing engagement data and custom data specific to your business
* Powers push notifications, in-app messages, and Content Card messaging channels

## App performance

Braze should have no negative impact on your app's performance.

The Braze SDKs have a very small footprint. We automatically change the rate that we flush user data depending on the quality of the network, in addition to allowing manual network control. We automatically batch API requests from the SDK to make sure that data is logged quickly while maintaining maximum network efficiency. Lastly, the amount of data sent from the client to Braze within each API call is extremely small.

## SDK compatibility

The Braze SDK is designed to be very well-behaved, and not interfere with other SDKs present in your app. If you are experiencing any issues you think might be due to incompatibility with another SDK, reach out to Braze Support.

## Default analytics and session handling

Certain user data is collected automatically by our SDK—for example, First Used App, Last Used App, Total Session Count, Device OS, etc. If you follow our integration guides to implement our SDKs, you will be able to take advantage of this [default data collection]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/). Checking this list can help you avoid storing the same information about users more than once. With the exception of session start and session end, all other automatically tracked data do not log data points.

{% alert note %}
All of our features are configurable, but it's a good idea to fully implement the default data collection model.

<br>If necessary for your use case, you can [limit the collection of certain data](#blocking-data-collection) after the integration is complete. 
{% endalert %}

## Data upload and download

The Braze SDK caches data (sessions, custom events, etc.) and uploads it periodically. Only after the data has been uploaded will the values be updated on the dashboard. The upload interval takes into account the state of the device and is governed by the quality of the network connection:

|Network Connection Quality |    Data Flush Interval|
|---|---|
|Great    |10 Seconds|
|Good    |30 Seconds|
|Poor    |60 Seconds|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

If there is no network connection, data is cached locally on the device until the network connection is re-established. When the connection is re-established, the data will be uploaded to Braze.

Braze sends data to the SDK at the beginning of a session based on which segments the user falls into at the time of the session. The new in-app messages will not be updated during the session. However, user data during the session will be continually processed as it is sent from the client. For example, a lapsed user (last used the app more than 7 days ago) will still receive content targeted at lapsed users on their first session back in the app.

## Blocking data collection

It is possible (though not suggested) to block the automatic collection of certain data from your SDK integration, or allowlist processes that do so. 

Blocking data collection is not recommended because removing analytical data reduces your platform's capacity for personalization and targeting. For example:

- If you choose not to fully integrate for location on one of the SDKs, you will not be able to personalize your messaging based on language or location. 
- If you choose not to integrate for time zone, you might not be able to send messages within a user's time zone. 
- If you choose to not integrate for specific device visual information, message content might not be optimized for that device.

We highly recommend completely integrating the SDKs to take full advantage of our product's capabilities.

{% tabs %}
{% tab Web SDK %}

You may either simply not integrate certain parts of the SDK, or use [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) for a user. This method will sync data logged prior to when `disableSDK()` was called, and will cause all subsequent calls to the Braze Web SDK for this page and future page loads to be ignored. If you wish to resume data collection at a later point in time, you can use the [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) method in the future to resume data collection. You can learn more about this in our [Disabling Web Tracking]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=web) article.

{% endtab %}
{% tab Android SDK %}

You can use [`setDeviceObjectAllowlist`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html?query=fun%20setDeviceObjectAllowlist(deviceObjectAllowlist:%20EnumSet%3CDeviceKey%3E):%20BrazeConfig.Builder) to configure the SDK to only send a subset of the device object keys or values according to a set allowlist. This must be enabled via [`setDeviceObjectAllowlistEnabled`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html?query=fun%20setDeviceObjectAllowlistEnabled(enabled:%20Boolean):%20BrazeConfig.Builder).

{% alert important %}
An empty allowlist will result in **no** device data being sent to Braze.
{% endalert %}

{% endtab %}
{% tab Swift SDK %}

You can assign a set of eligible fields to [`configuration.devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) on your `Braze.Configuration` to specify an allowlist for device fields that are collected by the SDK. The full list of fields is defined in [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty). To turn off the collection of all device fields, set the value of this property to an empty set (`[]`).

{% alert important %}
By default, all fields are collected by the Braze Swift SDK. Removing some device properties may disable SDK features.
{% endalert %}

For more usage details, refer to [Storage]({{site.baseurl}}/developer_guide/storage/?tab=swift) in the Swift SDK documentation.

{% endtab %}
{% endtabs %}

## What version of the SDK am I on?

You can use the dashboard to see the SDK version of a particular app by visiting **Settings > App Settings**. The **Live SDK Version** lists the highest Braze SDK version used by your most recent live application for at least 5% of your users.

![An app named Swifty in a workspace. The Live SDK version is 6.6.0.]({% image_buster /assets/img/live-sdk-version.png %}){: style="max-width:80%"} 

{% alert tip %}
If you have an iOS app, you can confirm that you are using the [Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) instead of the legacy [Objective-C iOS SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/) if your **Live SDK Version** is equal to or higher than 5.0.0, which was the first released version of the Swift SDK.
{% endalert %}

