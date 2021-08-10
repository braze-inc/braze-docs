---
nav_title: Segment
page_order: 1
alias: /partners/segment/

description: "This article outlines the partnership between Braze and Segment, a customer data platform that collects and routes information between sources in your marketing stack."
page_type: partner

---
# About Segment  

{% include video.html id="RfOHfZ34hYM" align="right" %}

> [Segment][5]{:target="_blank"} is a data analytics hub that allows you to track your users and route that data to a wide variety of user analytics providers, such as Braze.

We offer [both](#integration-options) a side-by-side SDK integration for your Android, iOS, and web applications and a server-to-server integration for your backend services so that you can start building richer user profiles.

If you're looking for information on the Currents integration with Segment, [click here]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/). If you're looking for more information about [Segment Personas]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/), which allows you to build segments in Segment and pass over to Braze as a custom attribute against a user profile.

## Setup Overview

To get going with your Segment/Braze integration,
1. Take note of and prepare for your integration by [adhering to the requirements and prerequisites](#prerequisites).
2. Set up [Braze as a Destination](#connection-settings) in accordance with [your chosen integration type](#integration-options).
3. If you're a new-to-Braze customer, you can relay historical data to Braze using [Segment Replays](#segment-replays).
4. Set up [mappings](#methods) for your integration.
5. [Test your integration](#step-3-test-your-integration) to ensure data is flowing smoothly between Braze and Segment.

## Prerequisites

| Requirement| Origin| Access| Description|
| ---| ---| ---|
| Segment Account & Account Information | Segment | [https://app.segment.com/login](https://app.segment.com/login){:target="_blank"} | You must have an active Segment Account to utilize their services with Braze. |
| Installed Source and Segment Source Libraries | Segment | [https://segment.com/docs/sources/](https://segment.com/docs/sources/){:target="_blank"} | The origin of any data sent into Segment, such as mobile apps, websites, or backend servers. <br> <br> You must install the libraries into your app, site, or server before being able to set up a successful `Source -> Destination` flow.
| Braze SDK Integration | Braze | For more details regarding Braze's SDKs, please refer to our [iOS][34], [Android][35] and [Web][38] documentation. | Braze must be successfully installed onto your app or site. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Step 1: Configure Braze Settings in Segment {#connection-settings}

![Destination Connection Settings]({% image_buster /assets/img/segment_destination_braze.png %}){: style="float:right;height:50%;width:50%;margin-left:15px;"} After successfully setting up your Braze and Segment integrations individually, you'll need to configure [Braze as a destination from Segment](https://segment.com/docs/destinations/){:target="_blank"}. You'll have many options to customize the flow of data between Braze and Segment using the connection settings described in the chart below.

| Name| Description |
|---|---|
| App Identifier| Previously called the API Key. Found in the [Developer Console](https://dashboard.braze.com/app_settings/developer_console) under the `API Settings` tab. |
| REST API Key| Previously called the "App Group Identifier". Found in the [Developer Console](https://dashboard.braze.com/app_settings/developer_console) under the `API Settings` tab. |
| API Endpoint| Find and enter your [Braze SDK Endpoint]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/) in our documentation. <br> <br> Format without the `https` as `sdk.iad-01.braze.com`. |
| Appboy Datacenter| Your Braze cluster. Select and input your [Braze Instance]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/) from the drop down. |
| Log Purchase when Revenue is present | Choose when to log purchases. |
| Braze REST API Endpoint| Find and enter your [Braze REST Endpoint]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/) in our documentation. Make sure to include the `https` so it looks like `https://rest.iad-01.braze.com`. |
|Safari Website Push ID| Safari requires a Website Push ID to send push. [More on this here]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-5-configure-safari-push). |
|Braze Web SDK Version| Which version of the Braze Web SDK you have integrated. You should have found this out during your initial integration process, but if you're unsure, reach out to your account manager or Braze support. |
{: .reset-td-br-1 .reset-td-br-2}

{% details Additional Connection Settings you might see during your integration. %}
|Name|Options | Description|
|---|---|---|
|Allow Crawler Activity| On/Off (True/False) | Web Crawlers are automatic programs that visit websites, read then, and collect information that might be important for a search engine index. You can either allow or disallow this from your integrated web page or app. Braze disallows this by default. |
|Automatically Send In-App Messages| On/Off (True/False) | Braze automatically enables you to send push to your users upon proper integration. |
|Do Not Load Font Awesome| On/Off (True/False) | Braze uses FontAwesome for our in-app message icons, but you may disallow this feature at any time. |
|Enable HTML In-App Messages| On/Off (True/False) | Enables Braze platform users to write HTML in-app messages. More information in the [JS Docs](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.initialize).|
|Enable Logging| On/Off (True/False) | [Log to the JavaScript](https://js.appboycdn.com/web-sdk/2.0/doc/module-appboy.html#.setLogger) console by default. |
|Minimum Interval Between Trigger Actions In Seconds| Any Number | By default, trigger actions will only fire if 30 seconds have elapsed since the last trigger action. |
|Open In-App Messages in New Tab | On/Off (True/False) | By default, links from in-app message clicks load in the current tab or a new tab as specified in the Braze platform. |
|Open News Feed Cards in New Tab | On/Off (True/False) | By default, links from News Feed cards or Content Cards load in the current tab or a new tab as specified in the Braze platform. |
|Session Timeout In Seconds| Any Number | By default, sessions time out after 30 minutes of inactivity. |
|Track All Pages | On/Off (True/False) | Sends all [Segment page calls](https://segment.com/docs/spec/page/){:target="_blank"} to Braze as Page Events.|
|Track Only Named Pages | On/Off (True/False) | Sends all [named Segment page calls](https://segment.com/docs/spec/page/){:target="_blank"} to Braze
|Update Existing Users Only| On/Off (True/False) | This only applies to Server Side integrations. This determines whether or not all users vs. existing users will be updated. This defaults to `false`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% enddetails %}

<br>

## Step 2A: Choose Integration Type and Implement {#integration-options}

You can integrate Segment's Web source (Analytics.js) and native client-side libraries with Braze using either a side-by-side ("Device-mode") integration or a server-to-server ("Cloud-mode") integration.

| Integration | Details |
| ----------- | ------- |
| [Side-by-Side / Device-mode](#side-by-side-sdk-integration) | Maps Segment's SDK to Braze's, allowing access to deeper features and more comprehensive usage of Braze than the server-to-server integration. |
| [Server-to-Server / Cloud-mode](#server-to-server-integration) | Forwards data from Segment to Braze's [user/track endpoint]({{site.baseurl}}/api/endpoints/user_data?redirected=true#user-track-endpoint). |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
You can learn more about Segment's integration options (Connection Modes), including the benefits of each, [here](https://segment.com/docs/destinations/#connection-modes){:target="_blank"}.
{% endalert %}

### Side-by-Side SDK Integration

Also called "Device-mode", this integration maps Segment's SDK and [methods](#methods) to Braze's, allowing access to deeper features and more comprehensive usage of Braze than the server-to-server integration.

{% tabs %}
{% tab Android %}

See and set up [mappings](#methods) to Segment's SDK for [Android](https://github.com/appboy/appboy-segment-android) on Braze's Github.

To complete the side-by-side integration, please refer to Segment's detailed instructions for [Android](https://segment.com/docs/connections/destinations/catalog/braze/#android){:target="_blank"}.

{% endtab %}
{% tab iOS %}

See and set up [mappings](#methods) to Segment's SDK for [iOS](https://github.com/appboy/appboy-segment-ios){:target="_blank"} on Braze's Github.

To complete the side-by-side integration, please refer to Segment's detailed instructions for [iOS](https://segment.com/docs/connections/destinations/catalog/braze/#ios){:target="_blank"}.

{% endtab %}
{% tab Web or Javascript %}

See and set up [mappings](#methods) to Segment's SDK for [Web / Analytics.js (Segment's JavaScript SDK)](https://github.com/segmentio/analytics.js-integrations/tree/master/integrations/appboy) on Braze's Github.

For Braze's Web SDK, [Segment's Analytics.js library](https://github.com/segmentio/analytics.js-integrations/tree/master/integrations/appboy) dynamically pulls in and initializes our Web SDK when you add Braze as a destination on your Segment dashboard. However, to use Braze's browser notification capabilities, please refer to Segment's [Web](https://segment.com/docs/connections/destinations/catalog/braze/#web){:target="_blank"} documentation.

{% endtab %}
{% endtabs %}

### Server-to-Server Integration

Also called "Cloud-mode", this integration forwards data from Segment to Braze's REST API.

This integration is **only** used in association with Segment's [server-side libraries][36], such as their Ruby or Go SDKs.

Enable the integration by setting your [App Group's REST API Key][39] and Braze's [REST API endpoint][40] for your corresponding data center (cluster) in your [Connection Settings on Segment's dashboard](#connection-settings).

Similar to the side-by-side integration, you will need to map Segment [methods](#methods) to Braze.

Unlike the side-by-side integration, however, the server-to-server integration does **not** support any of Braze's UI features, such as in-app messaging, News Feed, or push notifications.

Some [automatically captured][25] data is only available through the side-by-side integration. The following data is __not available via the server-to-server integration__:
- Sessions
- First Used App
- Last Used App

#### Enabling Push Notifications

Currently, Braze's server-to-server integration with Segment __does not__ support methods for push tokens. In order to enable push notifications in Braze, you must import push tokens via the [User Attribute Object][18] of our [User Data][19] REST API. You can also rely on the [side-by-side integration](#side-by-side-sdk-integration) for push token capture and mapping.


## Step 2B: Map Methods {#methods}

Braze supports the [Identify](https://segment.com/docs/spec/identify/){:target="_blank"}, [Track](https://segment.com/docs/spec/track/){:target="_blank"}, and [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page){:target="_blank"} (web) Segment methods; however, our REST APIs require you to include a [user ID][41]{:target="_blank"} when making these calls. Braze also supports custom attribute mapping using Segment's [Group](https://segment.com/docs/spec/group/){:target="_blank"} method.

### Identify

When you [identify](https://segment.com/docs/connections/destinations/catalog/braze/#identify){:target="_blank"} a user, we will record information for that user with `userId` as the External User ID.

| Segment Field | Braze Field |
| ------------- | ----------- |
| `firstName` | `first_name`
| `lastName` | `last_name`
| `birthday` | `dob`|
| `avatar` | `image_url`|
| `address.city` | `home_city`|
| `address.country` | `country` |
| `gender` | `gender` |
{: .reset-td-br-1 .reset-td-br-2}

All other traits will be recorded as [custom attributes][14].

| Segment Method | Braze Method | Example <br> `segment` > `braze`|
|---|---|---|
| Identify with User ID    | Set External ID    | analytics.identify("dawei");    appboy.changeUser("dawei")
| Identify with Reserved Traits    | Set User Attributes |     analytics.identify({email: "dawei@braze.com"});    appboy.getUser().setEmail("dawei@braze.com");
| Identify with Custom Traits    | Set Custom Attributes |     analytics.identify({fav_cartoon: "Naruto"});    appboy.getUser().setCustomAttribute("fav_cartoon": "Naruto");
| Identify with User ID and Traits |    Set External ID and Attribute | Combine methods above. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}


{% alert important %}
When passing user attribute data, please be sure that you are only passing values for attributes that have changed since the last update. This will ensure that you do not unnecessarily consume data points towards your allotment.
{% endalert %}

### Group

When you call _group_ in Segment, we will record a custom attribute with the name `ab_segment_group_<groupId>`, where `groupId` is the group's ID in the method's parameters. For example, if the group's ID is `1234`, then the custom attribute name will be `ab_segment_group_1234`. The value of the custom attribute will be set to `true`.

### Track

When you _track_ an event, we will record that event as a [custom event][13] using the name provided.

| Segment Method | Braze Method | Example <br> `segment` > `braze`|
|---|---|---|
| [Track](https://segment.com/docs/spec/track/){:target="_blank"} | Logged as a [Custom Event][13]. | `analytics.track("played_game");` > `appboy.logCustomEvent("played_game");`|
| [Track with Properties](https://segment.com/docs/spec/track/){:target="_blank"} | Logged as [Event Property]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties). | `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` > `appboy.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [Track with Product](https://segment.com/docs/spec/track/){:target="_blank"} | Logged as a [Purchase Event]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/logging_purchases/). | `analytics.track("purchase", {products: [product_id: "ab12", price: 19]});` > `appboy.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Order Completed {order-completed}

When you _track_ an event with the name `Order Completed` using the format described in Segment's [ECommerce API][4]{:target="_blank"}, we will record the products you've listed as [purchases][28].

### Page {#page}

The [page](https://segment.com/docs/spec/page/){:target="_blank"} call lets you record whenever a user sees a page of your website, along with any optional properties about the page.

| Segment Method | Braze Method | Example <br> `segment` > `braze`|
|---|---|---|
| [Page](https://segment.com/docs/spec/page/){:target="_blank"} __without name__    | Logged as a [Custom Event][13] |    `analytics.page();` >     `appboy.logCustomEvent("Loaded a Page");` |
| [Page](https://segment.com/docs/spec/page/){:target="_blank"} __with name__ |    Logged as a [Custom Event][13]    | `analytics.page("Home");`    > `appboy.logCustomEvent("Viewed Home Page");` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Step 3: Test Your Integration

Most of your [Overview][27] metrics (lifetime sessions, MAU, DAU, Stickiness, Daily Sessions, and Daily Sessions per MAU) will be blank even if Braze is receiving data from Segment.

You can view your data in the [Custom Events][22] or [Revenue][28] pages, or by [creating a segment][23]. The **Custom Events** page of the dashboard allows you to view custom event counts over time. Note that you will not be able to use [formulas][24] that include MAU and DAU statistics.

If you're sending purchase data to Braze (see [Order Completed](#order-completed)), the [Revenue][28] page allows you to view data on revenue or purchases over specific periods of time or your app's total revenue.

[Creating a segment][26] allows you to filter your users based on custom event data and custom attribute data.

{% alert important %}
If you use a server-to-server integration, filters related to automatically collected session data (such as "first used app" and "last used app") will not work. If you want to use these in your Segment/Braze integration, please use a side-by-side integration.
{% endalert %}

## User Deletion & Suppression 

If you need to delete or suppress users, note that [Segment's User Delete feature](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to){:target="_blank"} __is__ mapped to our [Users/Delete endpoint]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint). Please note that verification of these deletions could take up to 30 days.

You must ensure that that you select a common user identifier between Braze and Segment ( as in the user ID or external ID). Once you've initiated a deletion request with Segment, you will then be able to see the status and how it impacts each of your Destinations.


## Segment Replays

Segment provides a service to clients to "Replay" all historical data to a new technology partner. New Braze customers who want to import all relevant historical data can do so through Segment.

Segment will connect to our [users/track endpoint]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) to import user data into Braze on behalf of the client.

{% alert important %}
If users do not have an external ID, they will not be imported into Braze, as our users/track endpoint requires a user ID if a Braze ID or user alias is not provided. Currently, Segment does not map to Braze's Braze ID or user alias, so all anonymous data will not be "replayed" over.
{% endalert %}

## Best Practices

{% details Review Use Cases To Avoid Data Overages. %}

Segment __does not__ have a limit on the number of data elements clients send to them. Segment allows you to send all or turn on which events you will send to Braze. Rather than sending all of your events using Segment, we suggest that you review use cases with your marketing and editorial teams to determine which events you will send to Braze to avoid data overages.

{% enddetails %}

{% details Understand the Difference between ‘Custom API Endpoint’ vs ‘Custom REST API Endpoint’. %}

| Braze Terminology | Segment Equivalent |
| ----------------- | ------------------ |
| Braze SDK Endpoint | Custom API Endpoint |
| Braze REST Endpoint | Custom REST API Endpoint |
{: .reset-td-br-1 .reset-td-br-2}

Your Braze API Endpoint (called the "Custom API Endpoint" in Segment) is the SDK endpoint that Braze sets up for your SDK (for example, `sdk.iad-03.braze.com`). Your Braze REST API Endpoint (called the "Custom REST API Endpoint" in Segment) is the REST API Endpoint (for example, `https://rest.iad-03.braze.com`)
{% enddetails %}

{% details Ensure ‘Custom API Endpoint’ is Input into Segment Correctly. %}

| Braze Terminology | Segment Equivalent |
| ----------------- | ------------------ |
| Braze SDK Endpoint | Custom API Endpoint |
| Braze REST Endpoint | Custom REST API Endpoint |
{: .reset-td-br-1 .reset-td-br-2}

To ensure that you input your Braze SDK Endpoint correctly, the proper format must be followed. Your Braze SDK endpoint must not include `https://` (for example, `sdk.iad-03.braze.com`), or else the Braze integration will break. This is required because Segment automatically prepends your endpoint with `https://`, resulting in Braze initializing with invalid endpoint `https://https://sdk.iad-03.braze.com`.

{% enddetails %}

{% details Ensure API Key is Input Correctly. %}

> ‘App Identifier’ vs. ‘REST API Key’

The ‘App Identifier’ is the App API Key found in the `Manage Settings` or `Developer Console` page on the Braze Dashboard. This field is necessary for SDK integrations to work. The ‘REST API Key’ is the dashboard REST API Key for making API calls. Make sure the key has permission to access `users/track` endpoint.

{% enddetails %}


{% details Certain Data Not Mapping to Braze. %}

Segment allows for different data types and structures, which can lead to issues where data will not pass from Segment to Braze as expected.

Scenarios where data will not pass as expected:
1. Arrays or nested objects in event properties.
  - Segment allows for arrays or nested objects within the properties of their track events, which map to either Braze custom or purchase event properties. Since our properties don't support those data types, we will silently reject those calls.
2. Passing anonymous data server-to-server.
  - Customers may use Segment's server-to-server libraries to funnel anonymous data to other systems.

  {% enddetails %}


{% details Customization of Braze Initialization. %}

There are several different ways that Braze can be customized: [push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/), [in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/overview/), [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/overview/), and initialization. With a side-by-side integration you can still customize push, in-app messages, and Content Cards as you would with a direct Braze integration.

However, customizing when the Braze SDK is integrated or specifying initialization configurations may be difficult and sometimes not possible. This is because Segment will initialize the Braze SDK for you when the Segment initialization occurs.

{% enddetails %}



[4]: https://segment.com/docs/spec/ecommerce/v2/
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
