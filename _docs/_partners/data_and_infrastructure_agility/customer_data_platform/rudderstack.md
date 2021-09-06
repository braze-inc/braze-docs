---
nav_title: RudderStack
article_title: RudderStack
page_order: 3
description: "This article outlines the partnership between Braze and RudderStack, an open-source customer data infrastructure that offers a seamless Braze integration for your Android, iOS, and web applications. With RudderStack, you can now send your in-app customer event data directly to Braze for contextual analysis."
alias: /partners/rudderstack/
page_type: partner
search_tag: Partner

---

# RudderStack

> [RudderStack][1] is an open-source Customer Data Infrastructure for collecting and routing customer event data to your preferred data warehouse and dozens of other analytics providers, such as Braze. It is enterprise-ready and offers a robust transformation framework to process your event data on the fly.

RudderStack offers a native SDK integration for your Android, iOS, and web applications, as well as a server-to-server integration for your backend services.  This way, you can send your in-app customer event data to Braze directly for contextual analysis.

## Setup Overview

Integrating RudderStack with Braze is very quick and easy. All you need to do is follow these steps:

1. Make sure all the integration prerequisites are followed and adhered to.
2. Choose your preferred type of integration and configure Braze as a destination in RudderStack.
3. Set up the required mappings for your integration.

## Step 1: Prerequisites

| Requirement | Origin | Access | Description |
|---|---|---|---|
| RudderStack Account | RudderStack | [https://app.rudderstack.com/][2] | A RudderStack account is required to set up the RudderStack-Braze integration. |
| Configured Source | RudderStack | [RudderStack Documentation][3] | A source is essentially the origin of any data sent to RudderStack, such as websites, mobile apps, or backend servers. You are required to configure the source before setting up Braze as a destination in RudderStack. |
| Braze SDK Integration with your device | Braze | To know more about using the Braze SDKs, refer to our documentation on the [web][4], [iOS][5], and [Android][6] platforms. | Braze must be set up on your website or app for the integration to be successful. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Step 2: Choose the Type of Integration

You can choose to integrate RudderStack's web and native client-side libraries with Braze using either a side-by-side ("Device Mode") integration or a server-to-server ("Cloud Mode") integration.

| Integration Type | Description |
|---|---|
| Side-by-Side / Device Mode | RudderStack will send the event data to Braze directly from your client (browser or mobile application). |
| Server-to-Server / Cloud Mode | The Braze SDK sends the event data directly to RudderStack, which is then transformed and routed to Braze. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %} 
Learn more about RudderStack's connection modes and the benefits of each [here](https://docs.rudderstack.com/get-started/rudderstack-connection-modes).
{% endalert %}

### Step 2.1a: Side-by-Side Integration (Device Mode)

With this mode, you can send your events to Braze using the Braze SDK set up on your website or mobile app.

{% tabs %}
  {% tab Android %}
    Set up the mappings to the [RudderStack SDK for Android](https://github.com/rudderlabs/rudder-integration-braze-android) on Braze's GitHub repository, as described in Step 3. <br>
    To complete the Device Mode integration, please refer to the detailed RudderStack instructions for [adding Braze to your Android project](https://docs.rudderstack.com/destinations/braze#adding-device-mode-integration).
  {% endtab %}
  {% tab iOS %}
    Set up the mappings to the [RudderStack SDK for iOS](https://github.com/rudderlabs/rudder-integration-braze-ios) on Braze's GitHub repository, as described in Step 3. <br>
    To complete the Device Mode integration, please refer to the detailed RudderStack instructions for [adding Braze to your iOS project](https://docs.rudderstack.com/destinations/braze#adding-device-mode-integration).
  {% endtab %}
  {% tab Web / JavaScript %}
    Set up the mappings to the [RudderStack SDK for JavaScript](https://github.com/rudderlabs/rudder-sdk-js) on Braze's GitHub repository, as described in Step 3. <br>
    To learn more about how the web SDK works, please refer to the detailed RudderStack instructions on the [JavaScript SDK](https://docs.rudderstack.com/rudderstack-sdk-integration-guides/rudderstack-javascript-sdk).
  {% endtab %}
{% endtabs %}

### Step 2.1b: Server-to-Server Integration (Cloud Mode)

With this mode, the Braze SDK sends the event data directly to RudderStack. RudderStack then transforms this data and routes it to Braze in the expected format. The transformation is done in the RudderStack backend.

To enable the integration, set up your App Group's REST API Key and Braze's REST API endpoint in your Connection Settings (Refer to Step 2.2) on the RudderStack dashboard. You will also need to map the RudderStack methods to Braze (Refer to Step 3).

{% alert note %} 
All of RudderStack's server-side SDKs (Java, Python, Node.js, Go, Ruby) support only Cloud Mode. This is because their server-side SDKs operate in the RudderStack backend, and cannot load any Braze-specific SDK. 
{% endalert %}

{% alert important %} The server-to-server integration does not support Braze's UI features, such as push notifications or in-app messaging. These features are, however, supported by the Device Mode integration. {% endalert %}

## Step 2.2: Configure Braze Settings in RudderStack

Once you've decided on the integration mode and successfully set up the source and the Braze SDK on your device, you will need to configure Braze as a destination in RudderStack. The setup is quite straightforward - you will need to enter the following required fields:

![Braze Settings][0]{: style="max-width:40%;margin-bottom:15px;"}

| Name | Description |
|---|---|
| App Key | Can be found in the [Dashboard][13] under <b> Settings</b> - <b>Manage Settings</b> |
| REST API Key | This needs to be created in the Braze dashboard under <b>Settings</b> - [Developer Console][13] - <b>API Settings</b>. You can find the detailed instructions [here][14]. |
| Data Center | You will need to enter the Data Center details as provided by Braze. It is of the format `INSTANCE`, as explained in the [Braze Instances guide][15]. |
| Native SDK | You can enable or disable this option to use the Braze native SDK to send the events (use the Device Mode). |
{: .reset-td-br-1 .reset-td-br-2}

## Step 3: Using the Integration - Set Up the Mappings

Braze supports the RudderStack methods [identify][16], [track][16], and [page][16].

### Identify
The RudderStack `identify` method associates a user to their actions. RudderStack captures a unique user ID and the optional traits associated with that user, such as name, email, IP address, etc.

The field mapping is done as per the table below:

| RudderStack Field | Braze Field |
|---|---|
| `firstName` | `first_name` |
| `lastName` | `last_name` |
| `birthday` | `dob` |
| `avatar` | `image_url` |
| `address.city` | `home_city` |
| `address.country` | `country` |
| `gender` | `gender` |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %} 
All other traits will be recorded as [custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/).
{% endalert %}

You can read more about RudderStack's identify method in their [documentation][18].

### Track

RudderStack's `track` method captures all the user activities, along with the properties associated with those activities.

You can read more about RudderStack's `track` method in their [documentation][19].

#### Order Completed
On using the [RudderStack eCommerce API][20] to call the track method for an event with the name `Order Completed`, RudderStack sends the products listed in that event to Braze as [`purchases`][21].

### Page

RudderStack's `page` method allows you to record your website's page views. It also captures any other relevant information about that page.

You can read more about RudderStack's `page` method in their [documentation][22].


[0]: {% image_buster /assets/img/RudderStack/braze_settings.png %}
[1]: https://rudderstack.com/
[2]: https://app.rudderstack.com/
[3]: https://docs.rudderstack.com/how-to-guides/adding-source-and-destination-rudderstack
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[13]: https://dashboard.braze.com/app_settings/developer_console
[14]: {{site.baseurl}}/api/basics/?redirected=true#creating-and-managing-rest-api-keys
[15]: {{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/
[16]: https://docs.rudderstack.com/rudderstack-api-spec
[18]: https://docs.rudderstack.com/destinations/braze#identify
[19]: https://docs.rudderstack.com/destinations/braze#track
[20]: https://docs.rudderstack.com/rudderstack-api-spec/rudderstack-ecommerce-events-specification
[21]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data
[22]: https://docs.rudderstack.com/destinations/braze#page

