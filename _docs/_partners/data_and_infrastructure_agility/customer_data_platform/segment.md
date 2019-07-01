---
nav_title: Segment
page_order: 3
alias: /partners/segment/
---
# About Segment

Braze is dedicated to creating partner integrations that allow you to send data from multiple sources to your Dashboard. [Segment][10] is an analytics data hub that allows you to track your users and route that data to a wide variety of user analytics providers, such as Braze. We offer both a side-by-side SDK integration for your Android, iOS and web applications and a server-to-server [integration][11] for your backend services so that you can start building richer user profiles.

If you're looking for information on the Currents integration with Segment, [click here]({{ site.baseurl }}/partners/technology_partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/).

# Pre-Requisites

| Requirement| Origin| Access| Description|
| ---| ---| ---|
| Segment Account & Account Information | Segment | https://app.segment.com/login | You must have an active Segment Account to utilize their services with Braze. |

## Braze Settings in Segment

When configuring Braze from Segment, you'll have many options to customize the flow of data between Braze and Segment.

### Connection Settings

|Name| Description |
|---|---|
|App Identifier| Once called the API Key. Found in the Developer Console. |
|REST API Key| Once called the "App Group Identifier". Found in the Developer Console. |
|Custom API Endpoint| Given to you by your Braze support or account representative. For example: `https://sdk.api.braze.com`. If you were not given a custom API Endpoint, leave this setting blank. |
|Appboy Datacenter| This is your [Braze Instance]({{ site.baseurl }}/user_guide/administrative/access_braze/braze_instances/). Select it from the drop down. |
|Custom REST API Endpoint| Given to you by your Braze support or account representative. For example: `https://rest.iad.braze.com`. If you were not given a custom API Endpoint, leave this setting blank. |
|Safari Website Push ID| Safari requires a Website Push ID to send push. [More on this here]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-5-configure-safari-push). |
|Braze Web SDK Version| Which version of the Braze Web SDK you have integrated. You should have found this out during your initial integration process, but if you're unsure, reach out to your account manager or Braze support. |

### Optional Settings

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
|Update Existing Users Only| On/Off (True/False) | This only applies to Server Side integrations. This determines whether or not all users vs. existing users will be updated. This defaults to false. |

# Side-by-Side SDK Integration

Braze's side-by-side integration maps Segment's SDK to ours, allowing access to deeper features and a more comprehensive usage of Braze than the server-to-server integration. These mappings of Segment's SDK for [Android][31], [iOS][32] and [Analytics.js][33] (Segment's Javascript SDK) are open source and can be found on our GitHub page.

To complete the side-by-side integration, please refer to Segment's detailed instructions for [Android][29] and [iOS][30]. For Braze's Web SDK, Segment's Analytics.js library dynamically pulls in and initializes our Web SDK when you add Braze as a destination on your Segment dashboard. However, to use Braze's browser notification capabilities, please refer to Segment's [Web][37] documentation.

{% alert important %}
If you are given a custom endpoint for your Braze integration, be sure to add the custom endpoint to the "Custom API Endpoint" and your correct "Braze Datacenter" on your Braze destination settings found in Segment's dashboard. For the side-by-side integration, the "REST API Key" is **not** necessary.
{% endalert %}

![Segment's Dashboard UI][42]

The keys required to input in Segment's dashboard can be found in the [Developer Console][45] under the 'API Settings' tab.

![Braze Developer Console - API Settings][44]

For more details regarding Braze's SDKs, please refer to our [iOS][34], [Android][35] and [Web][38] documentation.

# Server-to-Server Integration {#segment-1}

The server-to-server integration forwards data from Segment to Braze's REST API. This integration is **only** used in association with Segment's [server-side libraries][36], such as their Ruby or Go SDKs. Enable the integration by setting your [App Group's REST API Key][39] and Braze's [REST API endpoint][40] for your corresponding data center in your destination settings on Segment's dashboard.

![Segment's Go Integration][43]

Unlike the side-by-side integration, however, the server-to-server integration does not support any of Braze's UI features, such as in-app messaging, News Feed, Feedback or push notifications.

## Getting Started

Once the Segment library is [integrated with your server][6], and Braze is added as a [destination][7] on your Segment dashboard, you can begin routing data.

Braze supports the _identify_, _track_, and _group_ methods; however, our REST APIs require you to include a [user ID][41] when making these calls.

## Identify

When you _identify_ a user, we will record information for that user with `userId` as the External User ID. Segment's special traits recognized as Braze's standard user profile fields (in parentheses) are `firstName` (`first_name`), `lastName` (`last_name`), `birthday` (`dob`), `avatar` (`image_url`), `address.city` (`home_city`), `address.country` (`country`), and `gender` (`gender`). All other traits will be recorded as [custom attributes][14].

>  When passing user attribute data, please be sure that you are only passing values for attributes that have changed since the last update. This will ensure that you do not unnecessarily consume data points towards your allotment.

## Track

When you _track_ an event, we will record that event as a [custom event][13] using the name provided.

### Completed Order

When you _track_ an event with the name `Completed Order` using the format described in Segment's [ECommerce API][9], we will record the products you've listed as [purchases][12].

## Group

When you call _group_, we will record a custom attribute with the name `ab_segment_group_<groupId>`, where `groupId` is the group's ID in the method's parameters. For example, if the group's ID is `1234`, then the custom attribute name will be `ab_segment_group_1234`. The value of the custom attribute will be set to true.

## Enabling Push Notifications {#segment-2}

Currently, Braze's server-to-server integration with Segment does not support methods for push tokens. In order to enable push notifications in Braze, you must import push tokens via the [User Attribute Object][18] of our [User Data][19] REST API.

## How To Tell If You're Receiving Data From Segment

Some [automatically captured][25] data is only available through the side-by-side integration. The following data is not available via the server-to-server integration:

- Sessions
- First Used App
- Last Used App

Consequently, most of your [app usage dashboard][27] (lifetime sessions, MAU, DAU, Stickiness, Daily Sessions and Daily Sessions per MAU) will be blank even if Braze is receiving data from Segment.

You can view your data in the [custom event dashboard][22], the [revenue dashboard][28] or by [creating a segment][23]. The custom event dashboard allows you to view custom event counts over time. Note that you will not be able to use [formulas][24] that include MAU and DAU statistics.

If you're sending purchase data to Braze (see [Completed Order][4]), the [revenue dashboard][28] allows you to view data on revenue or purchases over specific periods of time or your app's total revenue.

[Creating a segment][26] allows you to filter your users based on custom event data and custom attribute data. Note that filters related to automatically collected session data (such as "first used app" and "last used app") will not work.



[4]: {{ site.baseurl }}/partners/technology_partners/data_and_infrastructure_agility/customer_data_platform/segment_integration/#completed-order
[6]: https://segment.com/docs/
[7]: https://segment.com/docs/destinations/appboy/
[9]: https://segment.com/docs/spec/ecommerce/v2/
[10]: https://segment.com
[11]: https://segment.com/docs/integrations/appboy/
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
