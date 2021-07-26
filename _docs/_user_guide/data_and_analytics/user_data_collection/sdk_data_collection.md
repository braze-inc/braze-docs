---
nav_title: SDK Data Collection
page_order: 1
page_type: reference
description: "This reference article addresses the data that is collected by the SDK through a personalized integration, automatically collected integration, and minimum integration."
tool: Dashboard
---

# SDK Data Collection Options

Braze is designed to allow for flexible data collection via our SDKs and APIs. The Braze SDK can be integrated in three ways:
- __Personalized Integration__; integrators have the flexibility to collect data in addition to Automatically Collected Data.
- __Automatically Collected Integration__; integrators can benefit from automatically captured data (this includes all the Minimum Integration data) without integrating additional data.
- __Minimum Integration__; integrators can disable Automatically Collected Data to only receive data that is strictly necessary to enable communication with the Braze Services. 

## Personalized Integration 

To make the most out of the Braze Platform functionality, integrators most commonly implement the Braze SDKs and log [Custom Attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes), [Custom Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#logging-custom-events) and [Purchase Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#logging-purchase-events) that are pertinent to their business on top of Automatically Collected Data (including Minimum Integration). 

A personalized integration allows for customized communication that is relevant to the user experience. 

## Automatically Collected Integration

Listed below are the automatically captured data generated and received by Braze when an integrator initializes the SDK; this includes properties found in the Minimum Integration table.

| Attribute | Platform | Description | Why it's Collected |
| --------- | -------- | ----------- | ------------------ |
| Browser Name | Web | Name of the browser. | Used to ensure messages are only sent to compatible browsers. It can also be used for browser-based segmentation. |
| Time Zone | Android, iOS, Web | Device/browser time zone. | Used to ensure messages are sent at the appropriate time, according to each user’s local time zone. |
| Resolution | Android, iOS, Web | Device/browser resolution. | It can optionally be used for device-based message targeting. |
| Language | Android, iOS, Web | Device/browser language. | Used to translate messages to a user’s preferred language. |
| User Agent | Web | [User agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent). | Used to ensure messages are only sent to compatible devices. It can also be used within segmentation. |
| Device Locale | Android, iOS | The default locale of the device. | Used to translate messages to a user’s preferred language. |
| Device Model | Android, iOS | The specific hardware of the device. | Used to ensure messages are only sent to compatible devices. It can also be used within segmentation. |
| Device Wireless Carrier | Android, iOS | The mobile carrier. | It can optionally be used for message targeting. |
| IDFA | iOS | The advertiser identifier. | This value is only sent to Braze when (1) users opt-in, and (2) the IDFA is set in the Braze SDK integration. |
| Country | Android, iOS, Web | Country | Identified via IP Address Geolocation. It can be used to target messages based on location. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

All the above fields can be disabled to allow for a Minimum Integration: 
- Android: [device-level fields](https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/enums/DeviceKey.html), [allowlist documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/android/storage/)
- iOS: [device-level fields](https://github.com/Appboy/appboy-ios-sdk/blob/16e893f2677af7de905b927505d4101c6fb2091d/AppboyKit/headers/AppboyKitLibrary/Appboy.h#L181), [allowlist documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/storage/)
- Web: [device-level fields](https://js.appboycdn.com/web-sdk/2.3/doc/module-appboy.html#toc2), [allowlist documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/web/cookies_and_storage/#device-properties)

## Minimum Integration

Listed below is the strictly necessary data generated and received by Braze when an integrator chooses to initialize the SDK for communication and disable automatically captured data. These elements are non-configurable and are essential in out-of-the-box platform functions. 

| Attribute | Platform | Description | Why it's Collected |
| --------- | -------- | ----------- | ------------------ |
| OS and OS Version | Android, iOS, Web | Currently reported device/browser and device/browser version. | Used to ensure messages are only sent to compatible devices. It can also be used within segmentation to target users to upgrade app versions. |
| IDFV | iOS | Device identifier. | Used to identify anonymous users, differentiate users' devices, and ensure messages are sent to the correct intended device. |
| Device ID | Android, iOS, Web | Device identifier, an out-of-the-box randomly generated string. | Used to identify anonymous users, differentiate users' devices, and ensure messages are sent to the correct intended device. |
| Session ID & Session Timestamp | Android, iOS, Web | Session identifier, an out-of-the-box randomly generated string and session timestamp. | Used to determine whether the user is starting a new or existing session and to determine re-eligibility of messages intended for this user.<br><br>Certain messaging channels such as in-app messages and Content Cards are synchronized to the device upon session start. Our backend will then use data related to when it last contacted Braze’s servers (which the device stores and sends back) to know if the user is eligible for any new messages.|
| SDK Version | Android, iOS, Web | Current SDK version. | Used to ensure messages are only sent to compatible devices and to ensure no disruption of the service. |
| App-Version-Name /<br> App-Version-Code | Android, iOS, Web | App version name. | Used to ensure messages related to app version compatibility are sent to the correct devices. It can be used to notify users of service disruption or bugs. |
| SDK Message Interaction Data | Android, iOS, Web | Push direct opens, in-app message interactions, Content Card interactions. | Used for quality control purposes like checking that a message was received and that sending isn’t duplicated.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

The Braze backend/service generates metrics calculated on SDK data (e.g., total number of sessions conversion events, [Random Bucket Numbers]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/), etc.) message interaction data related to non-SDK message (i.e., SMS sends), and derived information, i.e., an uninstall from a push bounce. For clarity, this calculated data is not tracked by the SDK but generated by the Braze Services, and exporting a User Profile will display both tracked data and generated data.

{% alert important %}
If you are interested in the Minimum Integration only, and you integrate with mParticle, Segment, Tealium, or GTM, please note the following:
- __Mobile Platforms__: You must manually update the code for these configurations. mParticle and Segment do not offer a way to do this through their platform. 
- __Web__: Braze integration must be done natively to allow for Minimum Integration configuration. Tag managers do not offer a way to do this through their platform. 

{% endalert %} 