---
nav_title: Segment
article_title: Segment
page_order: 1
alias: /partners/segment/
description: "This article outlines the partnership between Braze and Segment, a customer data platform that collects and routes information between sources in your marketing stack."
page_type: partner
search_tag: Partner

---

# Segment  

{% include video.html id="RfOHfZ34hYM" align="right" %}

> [Segment][5] is a customer data platform that helps you collect, clean, and activate your customer data. 

The Braze and Segment integration allows you to track your users and route data to a wide variety of user analytics providers. Segment allows you to:
- Sync [Segment Personas]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/) (cohorts) to Braze for use in Braze campaign and Canvas segmentation.
- [Import data across the two platforms](#integration-options). We offer a side-by-side SDK integration for your Android, iOS, and web applications and a server-to-server integration for your backend services.
- [Connect data to Segment through Currents]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/). 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Segment account | A [Segment account](https://app.segment.com/login) is required to take advantage of this partnership. |
| Installed source and Segment source [libraries](https://segment.com/docs/sources/) | The origin of any data sent into Segment, such as mobile apps, websites, or backend servers.<br><br>You must install the libraries into your app, site, or server before being able to set up a successful `Source > Destination` flow. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Integration

To integrate Braze and Segment, you must set [Braze as a Destination](#connection-settings) in accordance with [your chosen integration type](#integration-options). If you're a new-to-Braze customer, you can relay historical data to Braze using [Segment Replays](#segment-replays). Next, you must set up [mappings](#methods), and [test your integration](#step-3-test-your-integration) to ensure smooth data flow between Braze and Segment.

### Step 1: Configure Braze settings in Segment {#connection-settings}

After successfully setting up your Braze and Segment integrations individually, you'll need to configure Braze as a [destination](https://segment.com/docs/destinations/) from Segment. You'll have many options to customize the data flow between Braze and Segment using the connection settings described in the chart below.

In Segment, navigate to **Destinations > Braze > Receiving from [platform]**.

![]({% image_buster /assets/img/segment_destination_braze.png %})

Next, provide the following fields in the configuration page:
- **App identifer**: Previously called the API key. Found in the Braze **Developer Console** under **Settings**.
- **App group REST API key**:  Braze REST API key with `users/track` permissions. This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**
- **Braze SDK endpoint**: Your SDK endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/api/basics/#endpoints).
- **Braze REST endpoint**: Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/api/basics/#endpoints).
- **Appboy datacenter**: Specify which instance your Braze data will be forwarded to.
- **Log purchase when revenue is present**: Choose when to log purchases.
- **Safari website push ID**: Safari requires a [website push ID]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-5-configure-safari-push) to send push.
- **Braze web SDK version**: Indicate which version of the braze web SDK you have integrated. If you are unsure, reach out to your account manager or Braze [support]({{site.baseurl}}/braze_support/).

{% details Additional connection settings %}

|Name|Options | Description|
|---|---|---|
|Allow crawler activity| On/Off (True/False) | Web Crawlers are automatic programs that visit websites, read them, and collect information that might be important for a search engine index. You can either allow or disallow this from your integrated web page or app. Braze disallows this by default. |
|Automatically send in-app messages| On/Off (True/False) | Braze automatically enables you to send push to your users upon proper integration. |
|Do not load font awesome| On/Off (True/False) | Braze uses FontAwesome for our in-app message icons, but you may disallow this feature at any time. |
|Enable HTML in-app messages| On/Off (True/False) | Enables Braze platform users to write HTML in-app messages. More information in the [JS Docs](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.initialize).|
|Enable logging| On/Off (True/False) | [Log to the JavaScript](https://js.appboycdn.com/web-sdk/2.0/doc/module-appboy.html#.setLogger) console by default. |
|Minimum interval between trigger actions in seconds| Any Number | By default, trigger actions will only fire if 30 seconds have elapsed since the last trigger action. |
|Open in-app messages in new tab | On/Off (True/False) | By default, links from in-app message clicks load in the current tab or a new tab specified in the Braze platform. |
|Open News Feed cards in new tab | On/Off (True/False) | By default, links from News Feed cards or Content Cards load in the current tab or a new tab as specified in the Braze platform. |
|Session timeout in seconds| Any Number | By default, sessions time out after 30 minutes of inactivity. |
|Track all pages | On/Off (True/False) | Sends all [Segment page calls](https://segment.com/docs/spec/page/) to Braze as Page Events.|
|Track only named pages | On/Off (True/False) | Sends all [named Segment page calls](https://segment.com/docs/spec/page/) to Braze
|Update existing users only| On/Off (True/False) | This only applies to Server Side integrations. This determines whether or not all users or existing users will be updated. This defaults to `false`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% enddetails %}

### Step 2: Choose integration type and implement {#integration-options}

You can integrate Segment's web source (Analytics.js) and native client-side libraries with Braze using either a side-by-side ("Device-mode") integration or a server-to-server ("Cloud-mode") integration.

| Integration | Details |
| ----------- | ------- |
| [Side-by-side<br>"Device-mode"](#side-by-side-sdk-integration) | Maps Segment's SDK to Braze's, allowing access to deeper features and more comprehensive usage of Braze than the server-to-server integration. |
| [Server-to-server<br>"Cloud-mode"](#server-to-server-integration) | Forwards data from Segment to Braze's [user/track endpoint]({{site.baseurl}}/api/endpoints/user_data?redirected=true#user-track-endpoint). |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
You can learn more about Segment's integration options (connection modes), including the benefits of each, [here](https://segment.com/docs/destinations/#connection-modes).
{% endalert %}

#### Side-by-side SDK integration

Also called "device-mode", this integration maps Segment's SDK and [methods](#methods) to Braze's, allowing access to deeper features and more comprehensive usage of Braze than the server-to-server integration.

{% tabs %}
{% tab Android %}

See and set up [mappings](#methods) to Segment's SDK for [Android](https://github.com/appboy/appboy-segment-android) on Braze's Github.

To complete the side-by-side integration, please refer to Segment's detailed instructions for [Android](https://segment.com/docs/connections/destinations/catalog/braze/#android).

{% endtab %}
{% tab iOS %}

See and set up [mappings](#methods) to Segment's SDK for [iOS](https://github.com/appboy/appboy-segment-ios) on Braze's Github.

To complete the side-by-side integration, please refer to Segment's detailed instructions for [iOS](https://segment.com/docs/connections/destinations/catalog/braze/#ios).

{% endtab %}
{% tab Web or Javascript %}

See and set up [mappings](#methods) to Segment's SDK for [Web / Analytics.js (Segment's JavaScript SDK)](https://github.com/segmentio/analytics.js-integrations/tree/master/integrations/appboy) on Braze's Github.

For Braze's Web SDK, [Segment's Analytics.js library](https://github.com/segmentio/analytics.js-integrations/tree/master/integrations/appboy) dynamically pulls in and initializes our Web SDK when you add Braze as a destination on your Segment dashboard. However, to use Braze's browser notification capabilities, please refer to Segment's [Web](https://segment.com/docs/connections/destinations/catalog/braze/#web) documentation.

{% endtab %}
{% endtabs %}

#### Server-to-server integration

Also called "Cloud-mode", this integration forwards data from Segment to Braze's REST API.

This integration is **only** used in association with Segment's [server-side libraries][36], such as their Ruby or Go SDKs.

Enable the integration by setting your [app group's REST API key][39] and Braze's [REST API endpoint][40] for your corresponding data center (cluster) in your [connection settings on Segment's dashboard](#connection-settings).

Similar to the side-by-side integration, you will need to map Segment [methods](#methods) to Braze.

However, unlike the side-by-side integration, the server-to-server integration does **not** support any of Braze's UI features, such as in-app messaging, News Feed, or push notifications.

Some [automatically captured][25] data is only available through side-by-side integration. The following data is **not available via the server-to-server integration**:
- Sessions
- First Used App
- Last Used App

##### Enabling push notifications

Currently, Braze's server-to-server integration with Segment **does not** support methods for push tokens. In order to enable push notifications in Braze, you must import push tokens via the [user attribute object][18] of our [user data][19] REST API. You can also rely on the [side-by-side integration](#side-by-side-sdk-integration) for push token capture and mapping.


### Step 3: Map methods {#methods}

Braze supports the [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page) (web), [Identify](https://segment.com/docs/spec/identify/), and [Track](https://segment.com/docs/spec/track/), and Segment methods; however, our REST APIs require you to include a [user ID][41] when making these calls. Braze also supports custom attribute mapping using Segment's [Group](https://segment.com/docs/spec/group/) method.

{% tabs local %}
{% tab Page %}
#### Page {#page}

The [page](https://segment.com/docs/spec/page/) call lets you record whenever a user sees a page of your website, along with any optional properties about the page.

| Segment method | Braze method | Example |
|---|---|---|
| [Page](https://segment.com/docs/spec/page/) without name | Logged as a [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) | Segment: `analytics.page();`<br>Braze: `appboy.logCustomEvent("Loaded a Page");` |
| [Page](https://segment.com/docs/spec/page/) with name | Logged as a [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events)    | Segment: `analytics.page("Home")`;<br>Braze: `appboy.logCustomEvent("Viewed Home Page");` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% endtab %}

{% tab Identify %}
#### Identify

When you [identify](https://segment.com/docs/connections/destinations/catalog/braze/#identify) a user, we will record information for that user with `userId` as the external user ID.

| Segment field | Braze field |
| ------------- | ----------- |
| `firstName` | `first_name`
| `lastName` | `last_name`
| `birthday` | `dob`|
| `address.city` | `home_city`|
| `address.country` | `country` |
| `gender` | `gender` |
{: .reset-td-br-1 .reset-td-br-2}

All other traits will be recorded as [custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/).

| Segment method | Braze method | Example |
|---|---|---|
| Identify with user ID | Set external ID | Segment:  `analytics.identify("dawei");`<br>Braze: `appboy.changeUser("dawei")` |
| Identify with reserved traits | Set user attributes | Segment: `analytics.identify({email: "dawei@braze.com"});`<br> Braze: `appboy.getUser().setEmail("dawei@braze.com");`
| Identify with custom traits | Set custom attributes | Segment: `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze: `appboy.getUser().setCustomAttribute("fav_cartoon": "Naruto")`;
| Identify with user ID and traits | Segment: Set External ID and Attribute | Combine preceding methods. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert important %}
When passing user attribute data, check that you only pass values for attributes that have changed since the last update. This will ensure that you do not unnecessarily consume data points towards your allotment.
{% endalert %}
{% endtab %}

{% tab Track %}
#### Track

When you _track_ an event, we will record that event as a [custom event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) using the name provided.

| Segment method | Braze method | Example |
|---|---|---|
| [Track](https://segment.com/docs/spec/track/) | Logged as a [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events). | Segment: `analytics.track("played_game");` <br>Braze: `appboy.logCustomEvent("played_game");`|
| [Track with properties](https://segment.com/docs/spec/track/) | Logged as [Event Property]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties). | Segment: `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Braze: `appboy.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [Track with product](https://segment.com/docs/spec/track/) | Logged as a [Purchase Event]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/logging_purchases/). | Segment: `analytics.track("purchase", {products: [product_id: "ab12", price: 19]});` <br>Braze: `appboy.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

##### Order completed {#order-completed}

When you _track_ an event with the name `Order Completed` using the format described in Segment's [ECommerce API](https://segment.com/docs/spec/ecommerce/v2/), we will record the products you've listed as [purchases]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).
{% endtab %}

{% tab group %}
#### Group

When you call _group_ in Segment, we will record a [custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) with the name `ab_segment_group_<groupId>`, where `groupId` is the group's ID in the method's parameters. For example, if the group's ID is `1234`, then the custom attribute name will be `ab_segment_group_1234`. The value of the custom attribute will be set to `true`.

| Segment method | Braze method | Example |
|---|---|---|
| [Group users](https://segment.com/docs/connections/spec/group/) | Set custom attribute | Segment:  `analytics.group("12345");`<br>Braze: `appboy.getUser().setCustomAttribute("ab_segment_group_1234": true)`; |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% endtabs %}

### Step 4: Test your integration

Most of your [overview][27] metrics (lifetime sessions, MAU, DAU, stickiness, daily sessions, and daily sessions per MAU) will be blank even if Braze is receiving data from Segment.

You can view your data in the [custom events][22] or [revenue][28] pages, or by [creating a segment][23]. The dashboard's **Custom Events** page allows you to view custom event counts over time. Note that you will not be able to use [formulas][24] that include MAU and DAU statistics.

If you're sending purchase data to Braze (see order completed in the **Track** tab of [Step 3](#methods)), the [revenue][28] page allows you to view data on revenue or purchases over specific periods or your app's total revenue.

[Creating a segment][26] allows you to filter your users based on the custom event and attribute data.

{% alert important %}
If you use a server-to-server integration, filters related to automatically collected session data (such as "first used app" and "last used app") will not work. Use a side-by-side integration if you want to use these in your Segment and Braze integration.
{% endalert %}

## User deletion and suppression 

If you need to delete or suppress users, note that [Segment's user delete feature](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to) **is** mapped to the Braze [users/delete endpoint]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint). Please note that verification of these deletions could take up to 30 days.

You must ensure that you select a common user identifier between Braze and Segment (as in the user ID or external ID). Once you've initiated a deletion request with Segment, you will then be able to see the status and how it impacts each of your Destinations.

## Segment replays

Segment provides a service to clients to "Replay" all historical data to a new technology partner. New Braze customers who want to import all relevant historical data can do so through Segment.

Segment will connect to our [Users Track endpoint]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) to import user data into Braze on behalf of the client.

{% alert important %}
If users do not have an external ID, they will not be imported into Braze. Our users/track endpoint requires a user ID if a Braze ID or user alias is not provided. Currently, Segment does not map to Braze's Braze ID or user alias, so all anonymous data will not be "replayed" over.
{% endalert %}

## Best practices

{% details Review use cases to avoid data overages. %}

Segment **does not** limit the number of data elements clients send to them. Segment allows you to send all or decide which events you will send to Braze. Rather than sending all of your events using Segment, we suggest you review use cases with your marketing and editorial teams to determine which events you will send to Braze to avoid data overages.

{% enddetails %}

{% details Understand the difference between the custom API endpoint and the custom REST API endpoint. %}

| Braze terminology | Segment equivalent |
| ----------------- | ------------------ |
| Braze SDK endpoint | Custom API endpoint |
| Braze REST endpoint | Custom REST API endpoint |
{: .reset-td-br-1 .reset-td-br-2}

Your Braze API Endpoint (called the "Custom API Endpoint" in Segment) is the SDK endpoint that Braze sets up for your SDK (for example, `sdk.iad-03.braze.com`). Your Braze REST API Endpoint (called the "Custom REST API Endpoint" in Segment) is the REST API Endpoint (for example, `https://rest.iad-03.braze.com`)
{% enddetails %}

{% details Ensure ‘custom API endpoint’ is input into Segment correctly. %}

| Braze terminology | Segment equivalent |
| ----------------- | ------------------ |
| Braze SDK endpoint | Custom API endpoint |
| Braze REST endpoint | Custom REST API endpoint |
{: .reset-td-br-1 .reset-td-br-2}

The proper format must be followed to ensure that you input your Braze SDK Endpoint correctly. Your Braze SDK endpoint must not include `https://` (for example, `sdk.iad-03.braze.com`), or else the Braze integration will break. This is required because Segment automatically prepends your endpoint with `https://`, resulting in Braze initializing with invalid endpoint `https://https://sdk.iad-03.braze.com`.

{% enddetails %}

{% details Certain data is not mapping to braze. %}

Segment allows for different data types and structures, leading to issues where data will not pass from Segment to Braze as expected.

Scenarios where data will not pass as expected:
1. Arrays or nested objects in event properties.
  - Segment allows for arrays or nested objects within the properties of their track events, which map to either Braze custom or purchase event properties. Since our properties don't support those data types, we will silently reject those calls.
2. Passing anonymous data server-to-server.
  - Customers may use Segment's server-to-server libraries to funnel anonymous data to other systems.

{% enddetails %}

{% details Customization of Braze initialization. %}

There are several different ways that Braze can be customized: [push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/), [in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/overview/), [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/overview/), and initialization. With a side-by-side integration you can still customize push, in-app messages, and Content Cards as you would with a direct Braze integration.

However, customizing when the Braze SDK is integrated or specifying initialization configurations may be difficult and sometimes not possible. This is because Segment will initialize the Braze SDK for you when the Segment initialization occurs.

{% enddetails %}

[5]: https://segment.com
[13]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events
[14]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[18]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification
[19]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[22]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data/#custom-event-data
[23]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[24]: {{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula/#creating-a-formula
[25]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection
[26]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[27]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/understanding_your_app_usage_data/
[28]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data
[34]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[36]: https://segment.com/docs/sources/#server
[38]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[39]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[40]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[41]: https://segment.com/docs/spec/identify/#user-id