---
nav_title: Tealium
page_order: 1
alias: /partners/tealium/

description: "This article outlines the partnership between Braze and Tealium, a universal data hub that enables you to connect mobile, web, and alternative data to other third-party sources."
page_type: partner

---

# About Tealium

> Tealium is a universal data hub that enables you to connect mobile, web, and alternative data to other third-party sources.

Tealium’s connection to Braze enables a data flow of custom events, user attributes, and purchases that empower you to act on your data in real-time.

We offer [both](#integration-options) a side-by-side SDK integration for your Android, iOS, and web applications and a server-to-server integration for your backend services so that you can start building richer user profiles.

## Set Up Overview

To get going with your Tealium/Braze integration,
1. Take note of and prepare for your integration by [adhering to the requirements and pre-requisites](#pre-requisites).
2. Set up [Braze as a Destination](#connection-settings) in accordance with [your chosen integration type](#integration-options).
3. If you're a new-to-Braze customer, you can relay historical data to Braze using [Segment Replays](#segment-replays).
4. Set up [mappings](#methods) for your integration.
5. [Test your integration](#step-3-test-your-integration) to ensure data is flowing smoothly between Braze and Segment.

## Pre-Requisites

| Requirement| Origin| Access| Description|
| ---| ---| ---|
| Tealium Account & Account Information | Tealium | https://my.tealiumiq.com/ | You must have an active Tealium Account to utilize their services with Braze. |
| Braze SDK Integration | Braze | For more details regarding Braze's SDKs, please refer to our [iOS][1], [Android][2] and [Web][3] documentation | Braze must successfully be installed onto your app or site |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## Side-by-Side SDK Integration


| Integration | Details |
| ----------- | ------- |
| [Side-by-Side / Device-mode](#side-by-side-sdk-integration) | Maps Segment's SDK to Braze's, allowing access to deeper features and a more comprehensive usage of Braze than the server-to-server integration. |
| [Server-to-Server / Cloud-mode](#server-to-server-integration) | Forwards data from Segment to Braze's [user/track endpoint]({{site.baseurl}}/api/endpoints/user_data?redirected=true#user-track-endpoint). |
{: .reset-td-br-1 .reset-td-br-2}


{% tabs %}
{% tab Android %}

See and set up [mappings](#methods) to Segment's SDK for [Android](https://github.com/appboy/appboy-segment-android) on Braze's Github.

To complete the side-by-side integration, please refer to Tealiums's detailed instructions for [Android](https://docs.tealium.com/platforms/remote-commands/integrations/braze/).

{% endtab %}
{% tab iOS %}

See and set up [mappings](#methods) to Segment's SDK for [iOS](https://github.com/appboy/appboy-segment-ios) on Braze's Github.

To complete the side-by-side integration, please refer to Tealiums's detailed instructions for [iOS](https://docs.tealium.com/platforms/remote-commands/integrations/braze/).

{% endtab %}
{% tab Web or Javascript %}

See and set up [mappings](#methods) to Segment's SDK for [Web / Analytics.js (Segment's JavaScript SDK)](https://github.com/segment-integrations/analytics.js-integration-appboy) on Braze's Github.

For Braze's Web SDK, [Segment's Analytics.js library](https://github.com/segment-integrations/analytics.js-integration-appboy) dynamically pulls in and initializes our Web SDK when you add Braze as a destination on your Segment dashboard. However, to use Braze's browser notification capabilities, please refer to Segment's [Web](https://community.tealiumiq.com/t5/Client-Side-Tags/Braze-Web-SDK-Tag-Setup-Guide/ta-p/20106) documentation.

{% endtab %}

{% alert important %}
For the side-by-side integration, inputting the "Braze REST API Key" into your [Braze's Connection Settings](#connection-settings) in the Segment Dashboard is **not** necessary.
{% endalert %}

## Server-to-Server Integration

This integration forwards data from Tealium to Braze's REST API. 

Similar to the side-by-side integration, you will need to map Segment [methods](#methods) to Braze.

Unlike the side-by-side integration, however, the server-to-server integration does **not** support any of Braze's UI features, such as in-app messaging, News Feed, or push notifications.


## Step 1: Configure Braze Settings in Tealium {#connection-settings}


| Name | Description |
| Tealium Username and Password | You will need your Tealium Username and Password to 


### Add a Connector in Tealium

1. In the leftside bar, go to __EventStream__ -> __Event Connectors__
For visitor data connectors, go to __AudienceStream__ -> __Audience Connectors__
2. In the left sidebar, use spotlight search to find the Braze Connector.
3. To add this connector, click the Braze Connector Tile. <br>Once clicked, you can view the connectory summary, here Tealium provides a list of required information, supported actions, vendor documentation and configuration instructions. <br><br> Click Continue.

### Configure your Connector Settings

#### Part 1: Source

1. From the Data Source Dropdown list, select the Braze data source.
2. Next, from the Event Feed drop-down lsit, select an event specification.
3. Name this action and click __Add Connector__.

#### Part 2: Configuration
Next a __Create Configure__ window will appear, here you must fill in certain Values requested by Tealium and Braze:
| Name | Description |
| ---- | ----------- |
| Username | 
| Password | 

(Optional) Add another connector to use the same configuration, wdit the connector settings by clicking the pencil icon, or delete the connector by clikceing the trash icon.

Click Continue. 

#### Part 3: Action

1. From the __Add Action__ dialogue, select an action from the drop-down list. 

Available actions include:


2. Complete the required field for the action selected, using pre-populated drop-down lists where available. 

When done, required fields for an item display __Completed__ on the right. 

3. Expand each section to compelte any optional fields desired.

Click Continue.


#### Part 4: Summary

Here you can view the summary for the connector you created. If you would like to modify the options you chose, select __Back__ or select __Finish__ to complete.


Your connector now display sin the list of connectors on your Tealium Home pagee. 


#### Part 5: Save and Publish

The actions you configured will noe fire when the trigger connections are met. The data populates, in real-time as each action fires. 


#### Part 6: Map Attributes (Optional)

A connector action sends data according to the mapping cpnfigured. Som connectors offer the ability to map the vendor atrribute to Tealium names.... Maybe not required....

### Test your Tealium Connector

After your connector is up and running, you should test it to make sure it's working properly. The most simple way to test this is to use a __Trace Tool__.

1. Start a new trace.
2. Examine the real-time log.
3. Check for the action you want to validate by clicking __Actions Triggered__ entry to expand.
4. Look for the action you want to validate and view the log status. 

To learn more about Tealium connector, cheack out the Tealium documentation, [here][4].


Tealium Connector Actions

| Action Name | AudienceStream | EventStream |
| ----------- | -------------- | ----------- |
| Track User by External ID | Yes | Yes |
| Track User by User Alias | Yes | Yes |
| Delete User by External User ID | Yes | Yes |
| Delete User by User Alias | Yes | Yes |


REST API Keys
API keys are used to authenticate an API call. 
When you create a new REST API Key, you need to gve it access to specific endpoints. This connector requires an API Key that has the User Data (users.track) permission to record user attributes, custom events, and purchases.

Action Settings - Parameters and Options

__Action - Track User by External ID__
| Parameters | Description |
| ---------- | ----------- |
| Endpoint URL | (Required) This endpoint can be used to record custom events, user attributes and purcahses for users. Your endpoint will coorepsond to your Braze instance, [check here][5] for more information |
| External ID | The External ID serves as a unique user identifier for whom you are submitting data. This identifier should be the same as the one you set in the Braze mobile SDK in order to avoid creating multiple profiles for the same user. External IDs that Braze is unaware of will return a non-fatal error. See Server Responses for details. |
| User Attributes | An API request with any fields in the Attributes Object will create or update an attribute of that name with the given value on the specified user profile.<br>Use the Braze User Profile Field names or your own custom attribute data. For more Information, [see here](https://www.braze.com/documentation/REST_API/#user-track-request).


__Action - Track User by User Alias__
| Parameters | Description |
| ---------- | ----------- |
| Endpoint URL | (Required) This endpoint can be used to record custom events, user attributes and purcahses for users. Your endpoint will coorepsond to your Braze instance, [check here][5] for more information |
| User Alias Value | Map the actual identifier value for Alias. Example: "Bobby". An Alias serves as an alternative unique user identifier. Use aliases to identify users along different dimensions than your core user ID. When using a User Alias, the "Update Only" mode is always true. |
| User Alias Label | The Label for the Alias, Example: "my_internal_ids". An Alias serves as an alternative unique user identifier. Use aliases to identify users along different dimensions than your core user ID. When using a User Alias, "Update Only" mode is always true. |
| User Attributes | An API request with any fields in the Attributes Object will create or update an attribute of that name with the given value on the specified user profile.<br>Use the Braze User Profile Field names or your own custom attribute data. For more Information, [see here](https://www.braze.com/documentation/REST_API/#user-track-request).


__Action - Delete User by External ID or Braze ID__
| Parameters | Description |
| ---------- | ----------- |
| Endpoint URL | (Required) This endpoint can be used to record custom events, user attributes and purcahses for users. Your endpoint will coorepsond to your Braze instance, [check here][5] for more information |
| External ID | External ID of the user to delete. Must include either External ID or Braze ID. |
| Braze ID | Braze ID of the user to delete. Must include either External ID or Braze ID. |


__Action - Delete User by User Alias__
| Parameters | Description |
| ---------- | ----------- |
| Endpoint URL | (Required) This endpoint can be used to record custom events, user attributes and purcahses for users. Your endpoint will coorepsond to your Braze instance, [check here][5] for more information |
| Alias Name | The Alias name of the user to be deleted. |
| Alias Label | The Alias label of the user to be deleted. |




[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[4]: https://community.tealiumiq.com/t5/Customer-Data-Hub/About-Connectors/ta-p/17389
[5]:
