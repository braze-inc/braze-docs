---
nav_title: mParticle
page_order: 0
alias: /partners/mparticle/

description: "This article outlines the partnership between Braze and mParticle, a customer data platform that collects and routes information between sources in your marketing stack."
page_type: partner

---
# About mParticle

{% include video.html id="Njhqwd36gZM" align="right" %}

> mParticle's customer data platform empowers you to do more with your data. Sophisticated marketers use mParticle to orchestrate data across their entire growth stack, enabling them to win in key moments of the customer journey.

You can improve your data flow by marrying mParticle and Braze for a seamless way to control the flow of information between systems. What's more, with Currents, Braze's real-time data export, connect data to mParticle, and make it actionable across the entire growth stack.

If you're looking for information on the Currents integration with mParticle, [click here]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mparticle_for_currents/).

## Pre-Requisites

| Requirement| Origin| Access| Description|
| ---| ---| ---|
| mParticle Account & Account Information | mParticle | https://app.mparticle.com/login | You must have an active mParticle Account to utilize their services with Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

If you want to connect your mobile and web apps to Braze, then you will need to use the [embedded kit integration][5] below.

If you have backend data outside of your apps, then you’ll want to use the Server API integration to pipe that data into Braze.

Please note that regardless of approach, it is necessary to integrate the mParticle embedded kit.

## Embedded Kit Integration

Through the embedded kit integration, mParticle and Braze’s SDK will both be present on your application. Unlike a direct Braze integration, however, mParticle takes care of calling the majority of Braze SDK code for you. Any mParticle methods you use to track user data will automatically be mapped to Braze’s SDK. These mappings of mParticle’s SDK for [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) and [Web](https://github.com/Appboy/integration-appboy) are open source and can be found on [mParticle’s GitHub page](https://github.com/mparticle-integrations).  

The embedded SDK integration allows you to take advantage of our full suite of features (Push, In-app Messages, News Feed, and all relevant message analytics tracking).

### 1. Integrate the mParticle SDKs

Integrate the appropriate mParticle SDKs into your app based on your platform needs:

* [mParticle for Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle for iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle for Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

### 2. Complete mParticle's Braze Event Kit Integration

mParticle's [Braze Event Kit Integration Guide](https://docs.mparticle.com/integrations/braze/event/#kit-integration) will walk you through custom mParticle:Braze alignment instructions based on your messaging needs (Push, Location Tracking, etc.).

### 3. Integrate the Braze SDK

Integrate the appropriate Braze SDKs into your app based on your messaging needs.

| Messaging Need | Details |
|---|---|
| In-App Messaging | Works automatically when the Braze Event Kit Integration (above) is completed successfully. |
| News Feed / Content Cards | Implemented directly via Braze SDK ([iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/overview/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/overview/), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/overview/)).
| Push for Android | Follow the [mParticle Android Push Notification Integration Documentation](https://docs.mparticle.com/developers/sdk/android/push-notifications). |
| Push for iOS | Follow the [Braze iOS Push Notification Integration Documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/). |
|Push for Web | Works automatically when the Braze Event Kit Integration (above) is completed successfully. |
{: .reset-td-br-1 .reset-td-br-2}

### 4. Configure your mParticle dashboard to enable the Braze Kit.

![mParticle Event Config UI][3]

| Name | Description |
|---|---|
| API Key | Found in Developer Console under Settings. |
| External Identity Type | The mParticle User Identity type to forward as an External ID to Braze. We recommend leaving this to the default value, Customer ID. |
| Braze Instance | Select Custom. |
| Custom SDK Endpoint | Given to you by your Braze support or account representative. For example: `sdk.api.braze.com`. If you were not given a custom API Endpoint, leave this setting blank. |
|Custom REST Endpoint | Given to you by your Braze support or account representative. For example: `rest.iad.braze.com`. If you know which Braze Instance you’re on, you can find your endpoint [here]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
| Custom JavaScript Endpoint | Same as Custom SDK endpoint. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
API keys will be different for each platform (iOS, Android, and Web).
{% endalert %}

## Server API Integration

This is an add-on to route your backend data to Braze if you’re using mParticle’s Server-Side SDKs (e.g. Ruby, Python, etc.). To set up this server-to-server integration with Braze, please follow mParticle’s documentation [here](https://docs.mparticle.com/guides/platform-guide/connections/).

### Connections Settings for your Braze Output

These settings are located in mParticle’s “Connections” tab under “Connect”. You will need to add Braze as an output.

![mParticle Connections Setting][4]


The App Group REST API Key required to input in mParticle’s dashboard can be found in the [Developer Console][1]  under the 'API Settings' tab.

![Braze Developer Console - API Settings][2]

Custom REST Endpoint: Set this to your relevant [REST API endpoint]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). This should match the “Custom REST Endpoint” field in the Event Configuration for Braze found in your mParticle Dashboard in the “Setup” tab under “Outputs”.

{% alert warning %}

On Data Mapping - Not all data types that are supported on mParticle are supported by Braze.

[Custom Event Properties]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) support string, numeric, boolean, or Date objects. It does not support arrays or nested objects.

[Custom Attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) support string, numerical, boolean, date objects and arrays, but does  not support objects or nested objects.  


{% endalert %}

[1]: https://dashboard.braze.com/app_settings/developer_console
[2]: {% image_buster /assets/img_archive/dashboard_keys_locations.png %}
[3]: {% image_buster /assets/img_archive/mParticle_event_config.png %}
[4]: {% image_buster /assets/img_archive/mParticle_connections.png %}
[5]: #embedded-kit-integration
