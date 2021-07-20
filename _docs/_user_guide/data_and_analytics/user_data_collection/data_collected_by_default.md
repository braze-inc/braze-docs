---
nav_title: Default and Minimum Data Collection
page_order: 1
page_type: reference
description: "This reference article addresses the data that is collected by default from the Braze SDK."
tool: Dashboard
---

# Default and Minimum Data Collection

Braze is designed to allow for flexible data collection via our SDKs and APIs. The Braze SDK can be integrated in three ways:
- __Personalized Integration__; integrators have flexibility to collect data in addition to Automatically Collected Data.
- __Automatically Collected Integration__; integrators can benefit from automatically captured data (this includes all the Minimum Integration data) without integrating additional data.
- __Minimum Integration__; integrators can disable Automatically Collected Data to only receive data that is strictly necessary to enable communication with the Braze Services. 

## Personalized Integration 

To make the most out of the Braze Platform functionality, integrators most commonly implement the Braze SDKs and log [Custom Attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/), [Custom Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) and [Purchase Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/) that are pertinent to their business on top of Automatically Collected Data (including Minimum Integration). 

A personalized integration allows for a customised communication that is relevant to the user experience. 

## Automatically Collected Data

Listed below are the automatically captured data generated and received by Braze when an integrator initializes the SDK; this includes properties found in the Minimum Integration table.

| Attribute | Platform | Description | Why it's Collected |
| --------- | -------- | ----------- | ------------------ |
| Browser Name | Web | Name of the browser. | Used to ensure messages are only sent to compatible browsers. It can also be used for browser-based segmentation. |
| Time Zone | Web, iOS, Android | Device/browser time zone. | Used to ensure messages are sent at the appropriate time, according to each user’s local time zone. |
| Resolution | Web, iOS, Android | Device/browser resolution. | It can optionally be used for device-based message targeting. |
| Language | Web, iOS, Android | Device/browser language. | Used to translate messages to a user’s preferred language. |
| User Agent | Web | The [User agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent). | Used to ensure messages are only sent to compatible devices. It can also be used within segmentation. |
| Device Locale | iOS, Android | The default locale of the device. | Used to translate messages to a user’s preferred language. |
| Device Model | iOS, Android | The specific hardware of the device. | Used to ensure messages are only sent to compatible devices. It can also be used within segmentation. |
| Device Wireless Carrier | iOS, Android | The mobile carrier. | It can optionally be used for message targeting. |
| IDFA | iOS | The advertiser identifier. | This value is only sent to Braze when (1) users opt-in, and (2) the IDFA is set in the Braze SDK integration. |
| Country | Web, iOS, Android | Country | Automatically captured via IP Address. It can be used to target messages based on location. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

All the above fields can be disabled to allow for a Minimum Integration: 
- Android: [whitelisting fields](https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/enums/DeviceKey.html) 
- iOS: [whitelisting fields](https://github.com/Appboy/appboy-ios-sdk/blob/16e893f2677af7de905b927505d4101c6fb2091d/AppboyKit/headers/AppboyKitLibrary/Appboy.h#L181)
- Web: [whitelisting fields](https://js.appboycdn.com/web-sdk/2.3/doc/module-appboy.html#toc2)

### Minimum Integration

Listed below is the strictly necessary data generated and received by Braze when an integrator chooses to initialize the SDK for communication and disable automatically captured data. These elements are non-configurable and are essential in out-of-the-box platform functions. 

| Attribute | Platform | Description | Why it's Collected |
| --------- | -------- | ----------- | ------------------ |
| OS and OS Version | Web, iOS, Android | Current reported device/browser and device/browser version. | Used to ensure messages are only sent to compatible devices. It can also be used within segmentation to target users to upgrade app versions. |
| IDFV | iOS | Device Identifier. | Used to identify anonymous users, differentiate users' devices, and ensure messages are sent to the correct intended device. |
| Device ID | Web, iOS, Android | Device Identifier, an out-of-the-box randomly generated string. | Used to identify anonymous users, differentiate users' devices, and ensure messages are sent to the correct intended device. |
| Session ID & Session Timestamp | Web, iOS, Android | Session Identifier, an out-of-the-box randomly generated string and Session Timestamp. | Used to determine whether the user is starting a new or existing session and to determine re-eligibility of messages intended for this user.<br><br>Certain messaging channels such as in-app messages and Content Cards are synchronized to the device upon session start. Our backend will then use data related to when it last contacted Braze’s servers (which the device stores and sends back) to know if the user is eligible for any new messages.|
| SDK Version | Web, iOS, Android | The current SDK Version. | Used to ensure messages are only sent to compatible devices and to ensure no disruption of the service. |
| App-version-name / App-version-code | Web, iOS, Android | App Version Name. | Used to ensure messages related to app version compatibility are sent to the correct devices. It can be used to notify users of service disruption or bugs. |
| SDK Message Interaction Data | Web iOS, Android | Push Direct Opens, In-App Message Interactions, Content Card Interactions | Used for quality control purposes like checking that a message was received and that sending isn’t duplicated.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

The Braze backend/service generates metrics calculated on SDK data (eg total number of sessions conversion events, [Random Bucket Numbers]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/), etc.) and message interaction data related to non-SDK message (i.e., SMS sends), and derived information, i.e., an uninstall from a push bounce. For clarity, this calculated data is not tracked by the SDK but generated by the Braze Services, and exporting a User Profile will display both tracked data and generated data.

{% alert important %}
If you are interested in minimal data collection and integrate with mParticle and Segment on:
- Mobile Platforms: You must manually update the code for these configurations. mParticle and Segment do not offer a way to do this through their platform. 
- Web: Braze integration must be done natively to allow for Minimum Integration configuration. mParticle and Segment do not offer a way to do this through their platform. 

{% endalert %} 