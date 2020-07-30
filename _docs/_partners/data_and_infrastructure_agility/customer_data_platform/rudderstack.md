---
nav_title: RudderStack
page_order: 1

description: RudderStack offers a seamless Braze integration for your Android, iOS, and web applications. You can now send your in-app customer event data directly to Braze for contextual analysis.
alias: /partners/RudderStack/

page_type: partner
hidden: true
---

# RudderStack

[RudderStack][1] is an open-source Customer Data Infrastructure for collecting and routing customer event data to your preferred data warehouse and dozens of other analytics providers, such as Braze. It is enterprise-ready and offers a robust transformation framework to process your event data on the fly.

RudderStack offers a native SDK integration for your Android, iOS, and web applications, as well as a server-to-server integration for your backend services.  This way, you can send your in-app customer event data to Braze directly for contextual analysis.

## Setup Overview

Integrating RudderStack with Braze is very quick and easy. All you need to do is follow these steps:

<ol><li>Make sure all the integration prerequisites are followed and adhered to.</li><li>Choose your preferred type of integration and configure Braze as a destination in RudderStack.</li><li>Set up the required mappings for your integration.</li></ol>

### Step 1. Prerequisites

| Requirement | Origin | Access | Description |
|---|---|---|---|
| RudderStack account | RudderStack | [https://app.rudderstack.com/][2] | A RudderStack account is required to set up the RudderStack-Braze integration. |
| Configured source | RudderStack | [https://docs.rudderstack.com/how-to-guides/adding-source-and-destination-rudderstack][3] | A source is essentially the origin of any data sent to RudderStack, such as websites, mobile apps, or backend servers. You are required to configure the source before setting up Braze as a destination in RudderStack. |
| Braze SDK Integration with your device | Braze | To know more about using the Braze SDKs, refer to our documentation on the [web][4], [iOS][5], and [Android][6] platforms. | Braze must be set up on your website or app for the integration to be successful. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Step 2.1. Choose the Type of Integration

You can choose to integrate RudderStack's web and native client-side libraries with Braze using either a side-by-side ("Device Mode") integration or a server-to-server ("Cloud Mode") integration.

| Integration Type | Description |
|---|---|
| Side-by-Side / Device Mode | In this mode, RudderStack will send the event data to Braze directly from your client (browser or mobile application). |
| Server-to-Server / Cloud Mode | In this mode, the Braze SDK sends the event data directly to RudderStack, which is then transformed and routed to Braze. |
{: .reset-td-br-1 .reset-td-br-2}

{{site.data.alerts.note}} Learn more about RudderStack's connection modes and the benefits of each [here][7]. {{site.data.alerts.end}}

#### 2.1.1. Side-by-Side Integration (Device Mode)

In this mode, you can send your events to braze using the Braze SDK set up on your website or mobile app.

{% tabs %}
  {% tab Android %}
    Set up the mappings to the [RudderStack SDK for Android][8] on Braze's GitHub repository, as described in Step 3. <br>
    To complete the Device Mode integration, please refer to the detailed RudderStack instructions for [adding Braze to your Android project][11].
  {% endtab %}
  {% tab iOS %}
    Set up the mappings to the [RudderStack SDK for iOS][9] on Braze's GitHub repository, as described in Step 3. <br>
    To complete the Device Mode integration, please refer to the detailed RudderStack instructions for [adding Braze to your iOS project][11].
  {% endtab %}
  {% tab Web / JavaScript %}
    Set up the mappings to the [RudderStack SDK for JavaScript][10] on Braze's GitHub repository, as described in Step 3. <br>
    To learn more about how the web SDK works, please refer to the detailed RudderStack instructions on the [JavaScript SDK][12].
  {% endtab %}
{% endtabs %}

#### 2.1.2. Server-to-Server Integration (Cloud Mode)

In this mode, the Braze SDK sends the event data directly to RudderStack. RudderStack then transforms this data and routes it to Braze in the expected format. The transformation is done in the RudderStack backend.

To enable the integration, set up your App Group's REST API Key and Braze's REST API endpoint in your Connection Settings (Refer Step 2.2) on the RudderStack dashboard. You will also need to map the RudderStack methods to Braze (Refer Step 3).

{{site.data.alerts.note}} All of RudderStack's server-side SDKs (Java, Python, Node.js, Go, Ruby) support only Cloud Mode. This is because their server-side SDKs operate in the RudderStack backend, and cannot load any Braze-specific SDK. {{site.data.alerts.end}}

{% alert important %} The server-to-server integration does not support Braze's UI features, such as push notifications or in-app messaging. These features are, however, supported by the Device Mode integration. {%endalert%}

### Step 2.2. Configure Braze Settings in RudderStack

Once you've decided on the integration mode and successfully set up the source and the Braze SDK on your device, you will need to configure Braze as a destination in RudderStack. The setup is quite straightforward - you will need to enter the following required fields:

![Braze Settings][1]

| Name | Description |
|---|---|
| App Key | Can be found in the [Developer Console][13] under <b>App Settings</b> - <b>Manage App Group</b> |
| REST API Key | This needs to be created in the Braze dashboard under <b>App Settings</b> - [Developer Console][13] - <b>API Settings</b>. You can find the detailed instructions [here][14]. |
| Data Center | You will need to enter the Data Center details as provided by Braze. It is of the format `INSTANCE`, as explained in the [Braze Instances guide][15]. |
| Native SDK | You can enable or disable this option to use the Braze native SDK to send the events (use the Device Mode). |
{: .reset-td-br-1 .reset-td-br-2}

### Step 3. Using the Integration - Set Up the Mappings

Braze supports the RudderStack methods [identify][16], [track][16], and [page][16].

#### Identify
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

{{site.data.alerts.note}} All other traits will be recorded as [custom attributes][17]. {{site.data.alerts.end}}

You can read more about RudderStack's identify method in their [documentation][18].

#### Track

RudderStack's `track` method captures all the user activities, along with the properties associated with those activities.

You can read more about RudderStack's `track` method in their [documentation][19].

##### Order Completed
On using the [RudderStack eCommerce API][20] to call the track method for an event with the name `Order Completed`, RudderStack sends the products listed in that event to Braze as [`purchases`][21].

#### Page

RudderStack's `page` method allows you to record your website's page views. It also captures any other relevant information about that page.

You can read more about RudderStack's `page` method in their [documentation][22].


[1]: {% image_buster /assets/img/partner_file/Braze Settings.png %}
[1]: https://rudderstack.com/
[2]: https://app.rudderstack.com/
[3]: https://docs.rudderstack.com/how-to-guides/adding-source-and-destination-rudderstack
[4]: https://www.braze.com/docs/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[5]: https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
[6]: https://www.braze.com/docs/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[7]: https://docs.rudderstack.com/get-started/rudderstack-connection-modes
[8]: https://github.com/rudderlabs/rudder-integration-braze-android
[9]: https://github.com/rudderlabs/rudder-integration-braze-ios
[10]: https://github.com/rudderlabs/rudder-sdk-js
[11]: https://docs.rudderstack.com/destinations/braze#adding-device-mode-integration
[12]: https://docs.rudderstack.com/rudderstack-sdk-integration-guides/rudderstack-javascript-sdk
[13]: https://dashboard.braze.com/app_settings/developer_console
[14]: https://www.braze.com/docs/api/basics/?redirected=true#creating-and-managing-rest-api-keys
[15]: https://www.braze.com/docs/user_guide/administrative/access_braze/braze_instances/
[16]: https://docs.rudderstack.com/rudderstack-api-spec
[17]: https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/
[18]: https://docs.rudderstack.com/destinations/braze#identify
[19]: https://docs.rudderstack.com/destinations/braze#track
[20]: https://docs.rudderstack.com/rudderstack-api-spec/rudderstack-ecommerce-events-specification
[21]: https://www.braze.com/docs/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data
[22]: https://docs.rudderstack.com/destinations/braze#page

