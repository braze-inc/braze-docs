---
nav_title: Tealium
page_order: 1
alias: /partners/tealium2/

description: "This article outlines the partnership between Braze and Tealium, a universal data hub that enables you to connect mobile, web, and alternative data to other third-party sources."
page_type: partner

---

# About Tealium

> Tealium is a universal data hub and customer data platform that enables you to connect mobile, web, and alternative data to other third-party sources. Tealium’s connection to Braze enables a data flow of custom events, user attributes, and purchases that empower you to act on your data in real-time.

Braze offers [both](#integration-options) a side-by-side SDK integration for your Android, iOS, and web applications and a server-to-server integration for your backend services so that you can start building richer user profiles.

## Understanding the EventStream

Tealium EventStream is a data collection and API hub that sits at the center of your data. EventStream handles the entire data supply chain from setup and installation to identifying, validating, and enhancing incoming user data. EventStream takes real-time action with event feeds and connectors. Listed below are the features that make up the [EventStream](https://community.tealiumiq.com/t5/Customer-Data-Hub/Introduction-to-EventStream/ta-p/20387#toc-hId--2077371752).  
- Data Sources (Installation and Data Collection)
- Live Events (Real-time Data Inspection)
- Event Specifications and Attributes (Data Layer Requirements and Validation)
- Event Feeds (Filtered Event Types)
- Event Connectors (API Hub Actions)

## Tealium AudienceStream
Tealium AudienceStream is an Omnichannel customer segmentation and real-time action engine. AudienceStream takes the data that flows into EventStream and creates visitor profiles that represent the most important attributes of your customers' engagement with your brand. To read more about how to set up Tealium AudienceStream, check out our [documentation]().

## Set Up Overview

To get going with your Tealium/Braze integration,
1. Take note of and prepare for your integration by [adhering to the requirements and pre-requisites](#pre-requisites).
2. Pick your integration type.
4. Set up [mappings](#methods) for your integration.
5. [Test your integration](#step-3-test-your-integration) to ensure data is flowing smoothly between Braze and Tealium.

## Pre-Requisites

| Requirement| Origin| Access| Description|
| ---| ---| ---|
| Tealium Account & Account Information | Tealium | [https://my.tealiumiq.com/](https://my.tealiumiq.com/) | You must have an active Tealium Account with both Server and Client-Side Access to utilize their services with Braze. |
| Install Source and Tealium Source Libraries | Tealium | [Tealium Source Libraries](https://community.tealiumiq.com/t5/Customer-Data-Hub/Data-Sources/ta-p/17933) | The origin of any data sent into Tealium, such as mobile apps, websites, or backend servers.<br><br>You must install the libraries into your app, site, or server before being able to set up a successful Tealium Connector |
| Braze SDK Integration | Braze | For more details regarding Braze's SDKs, please refer to our [iOS][1], [Android][2] and [Web][3] documentation | Braze must successfully be installed onto your app or site |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Choose your Integration Type

| Integration | Details |
| ----------- | ------- |
| [Side-by-Side](#side-by-side-sdk-integration) | Maps Tealiums's SDK to Braze's, allowing access to deeper features and more comprehensive usage of Braze than the server-to-server integration. |
| [Server-to-Server](#server-to-server-integration) | Forwards data from Tealium to Braze's [users/track endpoint]({{site.baseurl}}/api/endpoints/user_data?redirected=true#user-track-endpoint). |
{: .reset-td-br-1 .reset-td-br-2}

## Side-by-Side SDK Integration

### Remote Commands

Remote Commands is a feature of the Tealium iOS and Android libraries that allows native code to be triggered with the Tealium iQ Tag Management.

The Braze integration uses the native Braze SDK, a remote command module that wraps the Braze methods, and the Braze Remote Command tag that translates event tracking into native Braze calls. This solution leverages the convenience of Tag Management to configure a native Braze implementation without having to add vendor-specific code to your app.

### Tealium's Side-by Side Integrations with Braze
- [iOS](https://docs.tealium.com/platforms/remote-commands/integrations/braze/) 
- [Android](https://docs.tealium.com/platforms/remote-commands/integrations/braze/)
- [Web](https://community.tealiumiq.com/t5/Client-Side-Tags/Braze-Web-SDK-Tag-Setup-Guide/ta-p/20106)

## Server-to-Server Integration

This integration forwards data from Tealium to Braze's REST API. Similar to the side-by-side integration, you may need to map Tealium methods to Braze.

### Pre-Requisites

| Name | Description |
| ---- | ----------- |
| REST API Key | A Braze REST API Key with `users.track` permissions. <br><br>This can be created within the __Braze Dashboard__ -> __Developer Console__ -> __REST API Key__ -> __Create New API Key__ |
| Tealium Account & Account Information | You must have an active Tealium Account with both Server and Client Side Access to utilize their services with Braze. |
{: .reset-td-br-1 .reset-td-br-2}

### Step 1: Add a Connector in Tealium

![Connector MarketPlace][5]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

A connector is an integration between Tealium and another vendor that is used to transmit data. These connectors contain actions that represent the vendor's supported APIs. We can create a connector between Tealium and Braze by locating and configuring the Braze Connector.

1. From the left sidebar within Tealium under `Server-Side`, navigate to __EventStream__ -> __Event Connectors__<br>
For visitor data connectors, go to __AudienceStream__ -> __Audience Connectors__
2. Select the blue `+ Add Connector` button to look through the Connector Marketplace.
2. In the new dialogue box that appears, use the spotlight search to find the Braze Connector.
3. To add this connector, click the Braze Connector Tile. <br>Once clicked, you can view the connection summary, here Tealium provides a list of the required information, supported actions, and configuration instructions. <br><br> Click __Continue__ to begin configuring.

### Step 2: Configure your Connector Settings

The Braze Tealium connector setup is composed of four steps: Source, Configuration, Action, and Summary.

#### Step 2a: Set Up Source

Tealium requires that you first set up a valid source of data for your connector to draw from. 

__Setting up Your Data Source__
1. From the left sidebar within Tealium under `Server-Side`, navigate to __Sources__ -> __Data Sources__
2. Click the __+ Add Data Source__ Button
3. Locate __HTTP API__ platform within the available catagories, and name your HTTP API APP, this is a required field.<br><br>![Data Source][6]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
4. From the __Event Specifications__ Options, choose the event specs you would like to include. Event specifications help you identify the event names and required attributes to track in your installation. These specifications will be applied to incoming events. <br><br>Take some time to think about what data is most valuable to you and which specifications seem most appropriate for your use case. Note that you also have the option of creating custom event specifications, check out the [Tealium documentation][19] to learn more. <br><br>![Event Specs][7]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
5. The next dialogue advances to the __Get Code step__. This displays the data source key and installation code. The base code and event tracking code provided here serve as your installation guide. Download the provided PDF if you wish to share these instructions with your team. <br><br>![Get Code][8]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>
6. Click __Save & Continue__ <br><br>![Data Source Summary][9]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
7. Once saved, you will now be able to view your saved source as well as add or remove event specs. <br><br>![Connector][18]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>From the detailed data source view you can perform the following actions:
- View and copy the data source key
- View installation instructions
- Return to the Get Code page
- Add or remove event specifications
- View live events related to an event specification
- And more...<br>
8. ![Save/Publish][17]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}Lastly, make sure to Save and Publish. If you do not save and publish your data source you will not be able to find it when configuring your Braze connector.

For further instruction on setting up and editing your data source, check out [here](https://community.tealiumiq.com/t5/Customer-Data-Hub/Data-Sources/ta-p/17933).

#### Step 2b: Configure Braze Connector Source

Once configured, navigate back to the Braze Connector and select your data source. 

1. From the Data Source Dropdown list, select the Braze data source you created.
2. Next, from the Event Feed drop-down list, select an event specification you would like to configure.
3. Name this action and click __Continue__.

#### Step 2c: Configuration
![Create Configuration][15]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

Next, a __Create Configuration__ dialogue will appear. Here, you must fill in certain values requested by Tealium and Braze:

| Name | Description |
| ---- | ----------- |
| Name | The name of the Connector | 
| REST API Key | A Braze REST API Key with __users.track__ permissions. <br><br>This can be set within the __Braze Dashboard -> Developer Console -> REST API Keys -> Create New API Key__ |
{: .reset-td-br-1 .reset-td-br-2}

If you have created a connector before, you may optionally use an existing from the available connector list and modify it to fit your needs with the pencil icon or delete it with the trash icon. 

#### Step 2d: Action

Next, you must select a connector action. A connector action sends data according to the mapping that gets configured. The Braze connector allows you to map Braze attributes to Tealium attribute names. 

1. From the __Add Action__ dialogue, select one of the actions to set up.
2. Depending on which action you chose, there will be a varied selection of fields required by Tealium. Listed below are examples and explanations of these fields.

{% alert important %}
__Note that not all fields offered are required__. <br>If you wish to skip over a field, Tealium requires that you minimize it before continuing onto the next step.

![Minimize]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:80%"}
{% endalert %}

{% tabs local %}
{% tab Track User - User %}

__Action: Track User - Users__

This action allows you to track and map user attributes like those in the Braze User Attributes Object. To read more about the User Attributes Object, check out [our documentation](https://www.braze.com/docs/api/objects_filters/user_attributes_object/).

| Parameters | Description |
| ---------- | ----------- |
| User ID | Use this field to map the Tealium User ID field to its Braze Equivalent. <br><br>- If importing Push Tokens, External ID and Braze ID should not be specified.<br>- If specifying a user alias, Alias Name and Alias Label should both be set. |
| User Attribute | Use Braze's existing User Profile Attribute names to update user profile values in the Braze Dashboard or add your own custom attribute data to the user profiles. |
| Modify User Attributes | Integer attributes may be incremented by positive or negative integers.<br>Array attributes may be modified by adding or removing values from existing arrays. |
| User Attributes Update Strategy | Choose a strategy for updating or creating User Attributes. <br><br>- Selecting `Update Only` will only update existing user profiles. <br>- Selecting `Create or Update` will create or update a user profile as needed. |
{: .reset-td-br-1 .reset-td-br-2}

![Track User]({% image_buster /assets/img/tealium/track_user_user.png %})

{% endtab %}
{% tab Track User - Event %}

__Action: Track User - Event__

This action allows you to track and map event attributes like those in the Braze Event Object. To read more about the Braze Event Object, check out [our documentation](https://www.braze.com/docs/api/objects_filters/event_object/).

| Parameters | Description |
| ---------- | ----------- |
| User ID | Use this field to map the Tealium User ID field to its Braze Equivalent. <br><br>- If importing Push Tokens, External ID and Braze ID should not be specified.<br>- If specifying a user alias, Alias Name and Alias Label should both be set. |
| Event Attributes | An Event represents a single occurrence of a Custom Event by a particular user at the designated time value.<br><br>If sending an Event Object, __Name (tealium_event)__, and __Time (Last event timestamp)__ are both required. | 
| Event Attributes Strategy | Choose a strategy for updating or creating Event Attributes. <br><br>- Selecting `Update Only` will only update existing user profiles. <br>- Selecting`Create or Update` will create or update a user profile as needed. |
{: .reset-td-br-1 .reset-td-br-2}

![Track Event]({% image_buster /assets/img/tealium/track_user_event.png %})

{% endtab %}
{% tab Track User - Purchase %}

__Action: Track User - Purchase__

This action allows you to track and map user purchase attributes like those in the Braze Purchase Object. To read more about the Braze Purchase Object, check out our [Documentation](https://www.braze.com/docs/api/objects_filters/purchase_object/).

| Parameters | Description |
| ---------- | ----------- |
| User ID | Use this field to map the Tealium User ID field to its Braze Equivalent. <br><br>- If importing Push Tokens, External ID and Braze ID should not be specified.<br>- If specifying a user alias, Alias Name and Alias Label should both be set. |
| Purchase Attributes | A Purchase represents a single purchase by a particular user at a particular time.<br><br> If sending a purchase, the __Product ID (braze_product_id), Currency (currency), Price (product_list_price)__, and __Time (Last event timestamp)__ attributes are required. |
| Purchase Attributes Update Strategy | Choose a strategy for updating or creating Purchase Attributes. <br><br>- Selecting `Update Only` will only update existing user profiles. <br>- Selecting `Create or Update` will create or update a user profile as needed. |
{: .reset-td-br-1 .reset-td-br-2}

![Track Purchases]({% image_buster /assets/img/tealium/track_user_purchase.png %})

{% endtab %}
{% tab Track User (Advanced) %}

__Action: Track User (Advanced)__

This action allows you to track user, event, and purchase attributes all in one action.

| Parameters | Description |
| ---------- | ----------- |
| User ID | Use this field to map the Tealium User ID field to its Braze Equivalent. <br><br>- If importing Push Tokens, External ID and Braze ID should not be specified.<br>- If specifying a user alias, Alias Name and Alias Label should both be set. |
| User Attributes | Use Braze's existing User Profile Attribute names to update user profile values in the Braze Dashboard or add your own custom attribute data to the user profiles. |
| Modify User Attributes | Integer attributes may be incremented by positive or negative integers.<br>Array attributes may be modified by adding or removing values from existing arrays. |
| User Attributes Update Strategy | Choose a strategy for updating or creating User Attributes. <br><br>- Selecting `Update Only` will only update existing user profiles. <br>- Selecting `Create or Update` will create or update a user profile as needed. |
| Event Attributes | An Event represents a single occurrence of a Custom Event by a particular user at the designated time value.<br><br>If sending an Event Object, __Name (tealium_event)__, and __Time (Last event timestamp)__ are both required. |
| Event Attributes Update Strategy | Choose a strategy for updating or creating Event Attributes. <br><br>- Selecting `Update Only` will only update existing user profiles. <br>- Selecting `Create or Update` will create or update a user profile as needed. |
| Purchase Attributes | A Purchase represents a single purchase by a particular user at a particular time.<br><br> If sending a purchase, the __Product ID (braze_product_id), Currency (currency), Price (product_list_price)__, and __Time (Last event timestamp)__ attributes are required. |
| Purchase Attributes Update Strategy | Choose a strategy for updating or creating Purchase Attributes. <br><br>- Selecting `Update Only` will only update existing user profiles. <br>- Selecting `Create or Update` will create or update a user profile as needed. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}

{% tab Delete User %}

__Action: Delete Users__

This action allows you to delete users from the Braze Dashboard. To read more about the Braze /users/delete endpoint this action maps to, check out [our documentation](https://www.braze.com/docs/api/endpoints/user_data/post_user_delete/).

| Parameters | Description |
| ---------- | ----------- |
| User ID | Use this field to map the Tealium User ID field to it's Braze Equivalent. <br><br>- If specifying a user alias, Alias Name and Alias Label should both be set. |
{: .reset-td-br-1 .reset-td-br-2}

![Track Purchases]({% image_buster /assets/img/tealium/track_user_delete.png %})

{% endtab %}
{% endtabs %}

Select __Continue__.

#### Step 2e: Summary

Here, you can view the summary of the connector you created. If you would like to modify the options you chose, select __Back__ to edit or __Finish__ to complete.

![Connector Summary][16]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}

Your connector now displays in the list of connectors on your Tealium Home page. 

![Connector][13]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}

#### Step 2f: Save and Publish
![Save/Publish][17]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}
The actions you configured will now fire when the trigger connections are met. The data populates, in real-time as each action fires. 

### Step 3: Test your Tealium Connector

After your connector is up and running, you should test it to make sure it's working properly. The most simple way to test this is to use the Tealium __Trace Tool__.

1. Start a new trace. This can be done by selecting Trace on the left sidebar under `Server-Side` options.
2. Examine the real-time log.
3. Check for the action you want to validate by clicking __Actions Triggered__ entry to expand.
4. Look for the action you want to validate and view the log status. 

For more detailed instructions on how to implement Tealium's Trace tool, check out their [Trace documentation][21]. 

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[4]: https://community.tealiumiq.com/t5/Customer-Data-Hub/About-Connectors/ta-p/17389
[5]: {% image_buster /assets/img/tealium/braze_connector_marketplace.png %}
[6]: {% image_buster /assets/img/tealium/data_source.png %}
[7]: {% image_buster /assets/img/tealium/event_specs.png %}
[8]: {% image_buster /assets/img/tealium/get_code.png %}
[9]: {% image_buster /assets/img/tealium/summary.png %}
[10]: {% image_buster /assets/img/tealium/track_user_event.png %}
[11]: {% image_buster /assets/img/tealium/track_user_purchase.png %}
[12]: {% image_buster /assets/img/tealium/track_user_delete.png %}
[13]: {% image_buster /assets/img/tealium/summary_list.png %}
[14]: {% image_buster /assets/img/tealium/track_user_user.png %}
[15]: {% image_buster /assets/img/tealium/create_configuration.png %}
[16]: {% image_buster /assets/img/tealium/connector_summary.png %}
[17]: {% image_buster /assets/img/tealium/save_publish.png %}
[18]: {% image_buster /assets/img/tealium/braze_connection.png %}
[19]: https://community.tealiumiq.com/t5/Customer-Data-Hub/Event-Specifications/ta-p/19329#toc-hId--2078027338
[20]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[21]: https://community.tealiumiq.com/t5/Customer-Data-Hub/Trace/ta-p/12058