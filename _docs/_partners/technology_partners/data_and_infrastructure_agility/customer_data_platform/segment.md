---
nav_title: Segment
page_order: 1
alias: /partners/segment/
---
# About Segment  

{% include youtube.html id="RfOHfZ34hYM" align="right" %}

[Segment][5] is a data analytics hub that allows you to track your users and route that data to a wide variety of user analytics providers, such as Braze.

We offer [both](#integration-options) a side-by-side SDK integration for your Android, iOS and web applications and a server-to-server integration for your backend services so that you can start building richer user profiles.

If you're looking for information on the Currents integration with Segment, [click here]({{ site.baseurl }}/partners/technology_partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/). If you're looking for more information about [Segment Personas]({{ site.baseurl }}/partners/technology_partners/data_and_infrastructure_agility/customer_data_platform/segment_personas/), which allows you to build segments in Segment and pass over to Braze as a Custom Attribute against a user profile.

## Pre-Requisites

| Requirement| Origin| Access| Description|
| ---| ---| ---|
| Segment Account & Account Information | Segment | [https://app.segment.com/login](https://app.segment.com/login) | You must have an active Segment Account to utilize their services with Braze. |
| Installed Source and Segment Source Libraries | Segment | [https://segment.com/docs/sources/](https://segment.com/docs/sources/) | The origin of any data sent into Segment, such as mobile apps, websites, or backend servers. <br> <br> You must install the the libraries into your app, site, or server before being able to set up a successful `Source -> Destination` flow.
| Destinations | Segment | [https://segment.com/docs/destinations/](https://segment.com/docs/destinations/) | Places that receive data from Segment for storage, analysis, or action - like Braze! <br> <br> Braze must be successfully installed into your app or site. |
| Braze SDK Integration | Braze | For more details regarding Braze's SDKs, please refer to our [iOS][34], [Android][35] and [Web][38] documentation. | Braze must be successfully installed onto your app or site. |

## Step 1: Configure Braze Settings in Segment {#connection-settings}

![Destination Connection Settings]({% image_buster /assets/img/segment_destination_braze.png %}){: height="50%" width="50%" align="right"} When configuring [Braze as a destination from Segment](https://segment.com/docs/destinations/), you'll have many options to customize the flow of data between Braze and Segment using [Connection Settings](#connection-settings). 

| Name| Description |
|---|---|
| App Identifier| Previously called the API Key. Found in the Developer Console. |
| REST API Key| Previously called the "App Group Identifier". Found in the Developer Console. <br> <br> __The REST API Key is not required for the Side-by-Side Integration.__ |
| API Endpoint| Find and enter your [Braze SDK Endpoint]({{ site.baseurl }}/user_guide/administrative/access_braze/braze_instances/) in our documentation (`sdk.iad-01.braze.com`). |
| Appboy Datacenter| Select your [Braze Instance]({{ site.baseurl }}/user_guide/administrative/access_braze/braze_instances/) from the drop down. |
| Log Purchase when Revenue is present | Choose when to log purchases. |
| Braze REST API Endpoint| Find and enter your [Braze REST Endpoint]({{ site.baseurl }}/user_guide/administrative/access_braze/braze_instances/) in our documentation (`rest.iad-01.braze.com`). |
|Safari Website Push ID| Safari requires a Website Push ID to send push. [More on this here]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-5-configure-safari-push). |
|Braze Web SDK Version| Which version of the Braze Web SDK you have integrated. You should have found this out during your initial integration process, but if you're unsure, reach out to your account manager or Braze support. |

{% details Additional Connection Settings you might see during your integration. %}
|Name|Options | Description|
|---|---|---|
|Allow Crawler Activity| On/Off (True/False) | Web Crawlers are automatic programs that visit websites, read then, and collect information that might be important for a search engine index. You can either allow or disallow this from your integrated web page or app. Braze disallows this by default. |
|Automatically Send In-App Messages| On/Off (True/False) | Braze automatically enables you to send push to your users upon proper integration. |
|Do Not Load Font Awesome| On/Off (True/False) | Braze uses FontAwesome for our in-app message icons, but you may disallow this feature at any time. |
|Enable HTML In-App Messages| On/Off (True/False) | Enables Braze platform users to write HTML in-app messages. More information in the [JS Docs](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.initialize).|
|Enable Logging| On/Off (True/False) | [Log to the Javascript](https://js.appboycdn.com/web-sdk/2.0/doc/module-appboy.html#.setLogger) console by default. |
|Minimum Interval Between Trigger Actions In Seconds| Any Number | By default, trigger actions will only fire if 30 seconds have elapsed since the last trigger action. |
|Open In-App Messages in New Tab | On/Off (True/False) | By default, links from in-app message clicks load in the current tab or a new tab as specified in the Braze platform. |
|Open News Feed Cards in New Tab | On/Off (True/False) | By default, links from news feed cards or content cards load in the current tab or a new tab as specified in the Braze platform. |
|Session Timeout In Seconds| Any Number | By default, sessions time out after 30 minutes of inactivity. |
|Track All Pages | On/Off (True/False) | Sends all [Segment page calls](https://segment.com/docs/spec/page/) to Braze as Page Events.|
|Track Only Named Pages | On/Off (True/False) | Sends all [named Segment page calls](https://segment.com/docs/spec/page/) to Braze
|Update Existing Users Only| On/Off (True/False) | This only applies to Server Side integrations. This determines whether or not all users vs. existing users will be updated. This defaults to `false`. |
{% enddetails %}

<br>

{% alert note %}
The keys you are required to input in Segment's dashboard can be found in the [Developer Console](https://dashboard.braze.com/app_settings/developer_console) under the `API Settings` tab.

<br>

![Braze Developer Console - API Settings]({% image_buster /assets/img_archive/dashboard_keys_locations.png %})

{% endalert %}


## Step 2: Choose Integration Type and Implement {#integration-options}

You can integrate Segment's Web source (Analytics.js) and native client-side libraries with Braze using either a side-by-side ("Cloud-mode") integration, or a server-to-server ("Device-mode") integration.

| Integration | Details |
| ----------- | ------- |
| [Side-by-Side / Cloud-mode](#side-by-side-sdk-integration) | Maps Segment's SDK to Braze's, allowing access to deeper features and a more comprehensive usage of Braze than the server-to-server integration. |
| [Server-to-Server / Device-mode](#server-to-server-integration) | Forwards data from Segment to Braze's [user/track endpoint]({{ site.baseurl }}/api/endpoints/user_data?redirected=true#user-track-endpoint). |

{% alert note %}
You can learn more about Segment's integration options (Connection Modes), including the benefits of each, [here](https://segment.com/docs/destinations/#connection-modes).
{% endalert %}

### Side-by-Side SDK Integration

Also called "Cloud-mode", this integration maps Segment's SDK to Braze's, allowing access to deeper features and a more comprehensive usage of Braze than the server-to-server integration.

{% tabs local %}
{% tab Android %}

mappings of Segment's SDK for [Android][31] on Github

To complete the side-by-side integration, please refer to Segment's detailed instructions for [Android][29].

{% endtab %}
{% tab iOS %}

mappings of Segment's SDK for [iOS][32] on Github

To complete the side-by-side integration, please refer to Segment's detailed instructions for [iOS][30].

{% endtab %}
{% tab "Web / Javascript" %}

mappings of Segment's SDK for [Web / Analytics.js (Segment's Javascript SDK)][33] on Github

For Braze's Web SDK, [Segment's Analytics.js library][33] dynamically pulls in and initializes our Web SDK when you add Braze as a destination on your Segment dashboard. However, to use Braze's browser notification capabilities, please refer to Segment's [Web][37] documentation.

{% endtab %}
{% endtabs %}

{% alert important %}
For the side-by-side integration, inputting the "Braze REST API Key" into your [Braze's Connection Settings](#connection-settings) in the Segment Dashboard is **not** necessary.
{% endalert %}

### Methods

Braze supports the _identify_, _track_, and _group_ methods; however, our REST APIs require you to include a [user ID][41] when making these calls.

#### Identify

When you _identify_ a user, we will record information for that user with `userId` as the External User ID. Segment's special traits recognized as Braze's standard user profile fields (in parentheses) are `firstName` (`first_name`), `lastName` (`last_name`), `birthday` (`dob`), `avatar` (`image_url`), `address.city` (`home_city`), `address.country` (`country`), and `gender` (`gender`). All other traits will be recorded as [custom attributes][14].

>  When passing user attribute data, please be sure that you are only passing values for attributes that have changed since the last update. This will ensure that you do not unnecessarily consume data points towards your allotment.

#### Track

When you _track_ an event, we will record that event as a [custom event][13] using the name provided.

##### Completed Order

When you _track_ an event with the name `Completed Order` using the format described in Segment's [ECommerce API][4], we will record the products you've listed as [purchases][12].

#### Group

When you call _group_, we will record a custom attribute with the name `ab_segment_group_<groupId>`, where `groupId` is the group's ID in the method's parameters. For example, if the group's ID is `1234`, then the custom attribute name will be `ab_segment_group_1234`. The value of the custom attribute will be set to `true`.


### Server-to-Server Integration

Also called "Device-mode", this integration forwards data from Segment to Braze's REST API.

This integration is **only** used in association with Segment's [server-side libraries][36], such as their Ruby or Go SDKs.

Enable the integration by setting your [App Group's REST API Key][39] and Braze's [REST API endpoint][40] for your corresponding data center in your [Connection Settings on Segment's dashboard](#connection-settings).

![Segment's Go Integration][43]

Similar to the side-by-side integration, three Segment [methods](#methods) map to Braze:

- Identify = Setting user IDs, attributes and custom attributes
- Track = Logging custom events and purchases
- Page/Screen = Logging page/screen views as custom events

Unlike the side-by-side integration, however, the server-to-server integration does **not** support any of Braze's UI features, such as in-app messaging, News Feed, or push notifications.

#### Enabling Push Notifications

Currently, Braze's server-to-server integration with Segment __does not__ support methods for push tokens. In order to enable push notifications in Braze, you must import push tokens via the [User Attribute Object][18] of our [User Data][19] REST API.

## Step 3: Test Your Integration

Some [automatically captured][25] data is only available through the side-by-side integration. The following data is __not available via the server-to-server integration__:

- Sessions
- First Used App
- Last Used App

Consequently, most of your [app usage dashboard][27] (lifetime sessions, MAU, DAU, Stickiness, Daily Sessions and Daily Sessions per MAU) will be blank even if Braze is receiving data from Segment.

You can view your data in the [custom event dashboard][22], the [revenue dashboard][28] or by [creating a segment][23]. The custom event dashboard allows you to view custom event counts over time. Note that you will not be able to use [formulas][24] that include MAU and DAU statistics.

If you're sending purchase data to Braze (see [Completed Order][1]), the [revenue dashboard][28] allows you to view data on revenue or purchases over specific periods of time or your app's total revenue.

[Creating a segment][26] allows you to filter your users based on custom event data and custom attribute data. Note that filters related to automatically collected session data (such as "first used app" and "last used app") will not work.

## Best Practices

### Review Use Cases To Avoid Data Overages

Segment __does not__ have a limit on the number of data elements clients send to them. Segment allows you to send all or turn on which events you will send to Braze. Rather than sending all of your events using Segment, we suggest that you review use cases with your marketing and editorial teams to determine which events you will send to Braze to avoid data overages.

### Understand the Difference between ‘Custom API Endpoint’ vs ‘Custom REST API Endpoint’

{% alert important %}
Braze no longer provides _custom_ endpoints or instances. Please see our Instance documentation for more information and to see which instances, SDK endpoints, and REST endpoints you have available to you.
{% endalert %}

Your Braze API Endpoint (called the "Custom API Endpoint" in Segment) is the endpoint that Braze sets up for your SDK (for example, `sdk.iad-03.braze.com`). Your Braze REST API Endpoint (called the "Custom REST API Endpoint" in Segment) is the REST API Endpoint

### Ensure ‘Custom API Endpoint’ is Input into Segment Correctly

Ensure that you input your proper API Endpoint in the proper format (for example, `customer.iad-03.braze.com`) into the Segment dashboard.

The Braze integration will break if it has been entered as the Custom REST API Endpoint (for example: `sdk.iad-03.braze.com`), as Segment will automatically add `https://` to the beginning of the endpoint for you, resulting in Braze initializing with the custom endpoint of `https://https://sdk.iad-03.braze.com`.

### Ensure API Key is Input Correctly

> ‘App Identifier’ vs. ‘REST API Key’

The ‘App Identifier’ is the App API Key found in the `Manage App Group` or `Developer Console` page on the Braze Dashboard. This field is necessary for SDK integrations to work. The ‘REST API Key’ is the dashboard Rest API Key for making API calls. Make sure the key has permission to access `users/track` endpoint.

### Certain Data Not Mapping to Braze

Segment allows for different data types and structures, which can lead to issues where data will not pass from Segment to Braze as expected.

Scenarios where data will not pass as expected:
1. Arrays or nested objects in event properties.
  - Segment allows for arrays or nested objects within the properties of their track events, which map to either Braze custom or purchase event properties. Since our properties don't support those data types, we will silently reject those calls.
2. Passing anonymous data server-to-server.
  - Customers may use Segment's server-to-server libraries to funnel anonymous data to other systems.

### Customization of Braze Initialization

There are several different ways that Braze can be customized: [push]({{ site.baseurl }}/user_guide/message_building_by_channel/push/creating_a_push_message/), [in-app messages]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/overview/), [Content Cards]({{ site.baseurl }}/user_guide/message_building_by_channel/content_cards/overview/), and initialization. With a side-by-side integration you can still customize push, in-app messages, and Content Cards as you would with a direct Braze integration.

However, customizing when the Braze SDK is integrated or specifying initialization configurations may be difficult and sometimes not possible. This is because Segment will initialize the Braze SDK for you when the Segment initialization occurs.




[1]: {{ site.baseurl }}/partners/technology_partners/data_and_infrastructure_agility/customer_data_platform/segment_integration/#completed-order
[2]: https://segment.com/docs/
[3]: https://segment.com/docs/destinations/appboy/
[4]: https://segment.com/docs/spec/ecommerce/v2/
[5]: https://segment.com
[11]: https://segment.com/docs/destinations/braze/
[12]: {{ site.baseurl }}/user_guide/data_and_analytics/exporting_dashboard_data/#revenue-data
[13]: {{ site.baseurl }}/user_guide/data_and_analytics/user_data_collection/#user-data-collection
[14]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_attributes/
[15]: {% image_buster /assets/img_archive/Segment_App_Usage.png %}
[16]: {% image_buster /assets/img_archive/Custom_Events_Segment.png %}
[18]: {{ site.baseurl }}/developer_guide/rest_api/user_data/#user-attributes-object-specification
[19]: {{ site.baseurl }}/developer_guide/rest_api/user_data/#user-data
[22]: {{ site.baseurl }}/user_guide/data_and_analytics/exporting_dashboard_data/#custom-event-data
[23]: {{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[24]: {{ site.baseurl }}/user_guide/data_and_analytics/creating_a_formula/#creating-a-formula
[25]: {{ site.baseurl }}/user_guide/data_and_analytics/user_data_collection/#user-data-collection
[26]: {{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[27]: {{ site.baseurl }}/user_guide/data_and_analytics/your_reports/viewing_and_understanding_segment_data/#viewing-and-understanding-segment-data
[28]: {{ site.baseurl }}/user_guide/data_and_analytics/exporting_dashboard_data/#revenue-data
[29]: https://segment.com/docs/destinations/appboy/#android
[30]: https://segment.com/docs/destinations/appboy/#ios
[31]: https://github.com/appboy/appboy-segment-android
[32]: https://github.com/appboy/appboy-segment-ios
[33]: https://github.com/segment-integrations/analytics.js-integration-appboy
[34]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
[35]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/
[36]: https://segment.com/docs/sources/#server
[37]: https://segment.com/docs/destinations/appboy/#web
[38]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[39]: {{ site.baseurl }}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[40]: {{ site.baseurl }}/developer_guide/rest_api/basics/#endpoints
[41]: https://segment.com/docs/spec/identify/#user-id
[42]: {% image_buster /assets/img_archive/segment_destination_ui.png %}
[43]: {% image_buster /assets/img_archive/segment_go_integration.png %}
[44]: {% image_buster /assets/img_archive/dashboard_keys_locations.png %}
[45]: https://dashboard.braze.com/app_settings/developer_console
