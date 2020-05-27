---
nav_title: Tealium
page_order: 1
alias: /partners/tealium2/

description: "This article outlines the partnership between Braze and Tealium, a universal data hub that enables you to connect mobile, web, and alternative data to other third-party sources."
page_type: partner

---

# About Tealium

> Tealium is a universal data hub and customer data platform that enables you to connect mobile, web and alternative data to other third-party sources.

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
| Tealium Account & Account Information | Tealium | https://my.tealiumiq.com/ | You must have an active Tealium Account with both Server and Client Side Access to utilize their services with Braze. |
| Install Source and Tealium Source Libraries | Tealium | https://community.tealiumiq.com/t5/Customer-Data-Hub/Data-Sources/ta-p/17933 | The origin of any data sent into Tealium, such as mobile apps, websites, or backend servers.<br><br>You must install the libraries into your app, site, or server before being able to set up a successful Tealium Connector |
| Braze SDK Integration | Braze | For more details regarding Braze's SDKs, please refer to our [iOS][1], [Android][2] and [Web][3] documentation | Braze must successfully be installed onto your app or site |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Tealium EventStream 
Tealium EventStream is a data collection and API hub that sits at the center of your data. EventStream handles the entire data supply chain from setup and installation, to identifying, validating, and enhancing incoming user data. EventStream takes real-time action with event feeds and connectors. Listed below are the features that make up the [EventStream](https://community.tealiumiq.com/t5/Customer-Data-Hub/Introduction-to-EventStream/ta-p/20387#toc-hId--2077371752).  
- Data Sources (Installation and Data Collection)
- Live Events] (Real-time Data Inspection)
- Event Specifications and Attributes (Data Layer Requirements and Validation)
- Event Feeds (Filtered Event Types)
- Event Connectors (API Hub Actions)

## Tealium AudienceStream
Tealium AudienceStream is an Omnichannel customer segmentation and real-time action engine. AudienceStream takes the data that flows into EventStream and creates visitor profiles that represent the most important attributes of your customers' engagement with your brand. These visitor profiles are segmented by shared behaviors to create audiences, sets of visitors with common traits. These audiences fuel your marketing technology stack in real-time via connectors. For more information on AudeinceStream, check out the Tealium Documentation [here](https://community.tealiumiq.com/t5/Customer-Data-Hub/Introduction-to-AudienceStream/ta-p/16087).

## Step 1: Configure Braze Settings in Tealium

## Step 2a: Choose Integration Type and Implement

### Side-by-Side SDK Integration

| Integration | Details |
| ----------- | ------- |
| [Side-by-Side](#side-by-side-sdk-integration) | Maps Segment's SDK to Braze's, allowing access to deeper features and a more comprehensive usage of Braze than the server-to-server integration. |
| [Server-to-Server](#server-to-server-integration) | Forwards data from Segment to Braze's [user/track endpoint]({{site.baseurl}}/api/endpoints/user_data?redirected=true#user-track-endpoint). |
{: .reset-td-br-1 .reset-td-br-2}

#### Remote Commands

Remote Commands is a feature of the Tealium iOS and Android libraries that allows native code to be triggered with the Tealium iQ Tag Management.

The Braze integration uses the native Braze SDK, a remote command module that wraps the Braze methods, and the Braze Remote Command tag that translates event tracking into native Braze calls. This solution leverages the convenience of Tag Management to configure a native Braze implementation without having to add vendor-specific code to your app.

#### Tealium's Side-by Side Integrations with Braze
- [iOS](https://docs.tealium.com/platforms/remote-commands/integrations/braze/) 
- [Android](https://docs.tealium.com/platforms/remote-commands/integrations/braze/)
- [Web](https://community.tealiumiq.com/t5/Client-Side-Tags/Braze-Web-SDK-Tag-Setup-Guide/ta-p/20106)

### Server-to-Server Integration

This integration forwards data from Tealium to Braze's REST API. Similar to the side-by-side integration, you may need to map Tealium methods to Braze.

## Step 1: Configure Braze Settings in Tealium {#connection-settings}

Pre-Requisites

| Name | Description |
| ---- | ----------- |
| REST API Key | A Braze REST API Key with `users.track` permissions. <br><br>This can be created within the __Braze Dashboard__ -> __Developer Console__ -> __REST API Key__ -> __Create New API Key__ |

### Add a Connector in Tealium

![Connector MarketPlace][5]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

1. In the left sidebar, go to __EventStream__ -> __Event Connectors__<br>
For visitor data connectors, go to __AudienceStream__ -> __Audience Connectors__
2. In the left sidebar, use the spotlight search to find the Braze Connector.
3. To add this connector, click the Braze Connector Tile. <br>Once clicked, you can view the connection summary, here Tealium provides a list of the required information, supported actions, and configuration instructions. <br><br> Click __Continue__.

### Configure your Connector Settings

#### Part 1: Source

__Setting up Your Data Source__
1. From the Server Side on Tealium, navigate to __Sources__ -> __Data Source__
2. Click the __+ Add Data Source__ Button
3. Locate within the Catagories, __HTTP API__, name your HTTP API APP, this is a required field.![Data Source][6]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}
4. From the __Event Specifications__ Options, choose the event specs. Event specifications help you identify the event names and required attributes to track in your installation.![Event Specs][7]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}
5. The next dialogue advances to the __Get Code step__ and displays the data source key and installation code. Save this code as a PDF, because you will not be able to return to this window. ![Get Code][8]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}
Data Source Key, Base Code, and Event Tracking Code. 
6. Click Save and Continue. ![Data Sourrce Summary][9]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}
7. Save and Publish ![Save/Publish][17]{: style="max-width:40%;margin-left:15px;margin-bottom:15px;"}


Note: From the detailed data source view you can perform the following actions:
- View and copy the data source key
- View installation instructions
- Return to the Get Code page
- Add or remove event specifications
- View live events related to an event specification
- And more...

For further instruction on setting up and editing your data source, check out [here](https://community.tealiumiq.com/t5/Customer-Data-Hub/Data-Sources/ta-p/17933).


1. From the Data Source Dropdown list, select the Braze data source.
2. Next, from the Event Feed drop-down list, select an event specification.
3. Name this action and click __Add Connector__.

#### Part 2: Configuration
![Create Configuration][15]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

Next, a __Create Configure__ dialogue will appear. Here, you must fill in certain Values requested by Tealium and Braze:

| Name | Description |
| ---- | ----------- |
| Name | The name of the Connector | 
| REST API Key | A Braze REST API Key with users.track permissions. <br><br>This can be set within the Braze Dashboard -> Developer Console -> REST API Keys -> Create New API Key |

If you have created a connector before, you may optionally use one from the existing connector list and just modify it to fit your needs with the pencil icon or delete it with the trash icon. 

Click Continue. 

#### Part 3: Action

1. From the __Add Action__ dialogue, select one of the actions to set up.
2. Depending on which action you chose, there will be a varied selection of fields required by Tealium. Listed below are examples and explanations of these fields.

| Action Name | AudienceStream | EventStream |
| ----------- | -------------- | ----------- |
| Track User by External ID | Yes | Yes |
| Track User by User Alias | Yes | Yes |
| Delete User by External User ID | Yes | Yes |
| Delete User by User Alias | Yes | Yes |

{% details Track User by External ID %}

__Action - Track User by External ID__

| Parameters | Description |
| ---------- | ----------- |
| Endpoint URL | (Required) Your [Braze REST endpoint URL]({{site.baseurl}}/api/basics?redirected=true#endpoints). Your endpoint must be manually entered as custom text into the given drop-down box. |
| External ID | The External ID serves as a unique user identifier for whom you are submitting data. This identifier should be the same as the one you set in the Braze mobile SDK in order to avoid creating multiple profiles for the same user. <br><br> External IDs which Braze is unaware of will return a non-fatal error. See Server Responses for details. |
| User Attributes | An API request with any fields in the Attributes Object will create or update an attribute of that name with the given value on the specified user profile. Use the Braze User Profile Field names or your own custom attribute data. |

![Track User by External ID][11]{: style="max-width:40%;margin-left:15px;margin-bottom:15px;"}


{% enddetails %}

{% details Track User by User Alias %}

__Action - Track User by User Alias__

| Parameters | Description |
| ---------- | ----------- |
| Endpoint URL | (Required) Your [Braze REST endpoint]({{site.baseurl}}/api/basics?redirected=true#endpoints). Your endpoint will need to be manually entered as custom text into the given drop-down box. |
| User Alias Value | Map the actual identifier value for Alias. Example: "Bobby". An Alias serves as an alternative unique user identifier. Use aliases to identify users along different dimensions than your core user ID. <br><br>When using a User Alias, the "Update Only" mode is always true. |
| User Alias Label | The Label for the Alias, Example: "my_internal_ids". An Alias serves as an alternative unique user identifier. Use aliases to identify users along different dimensions than your core user ID. When using a User Alias, "Update Only" mode is always true. |
| User Attributes | An API request with any fields in the Attributes Object will create or update an attribute of that name with the given value on the specified user profile. Use the Braze User Profile Field names or your own custom attribute data. |

![Track User by Alias][13]{: style="max-width:40%;margin-left:15px;margin-bottom:15px;"}
![Track User by Alias][14]{: style="max-width:40%;margin-left:15px;margin-bottom:15px;"}


{% enddetails %}

{% details Delete User by External ID or Braze ID %}

__Action - Delete User by External ID or Braze ID__

| Parameters | Description |
| ---------- | ----------- |
| Endpoint URL | (Required) Your [Braze REST endpoint]({{site.baseurl}}/api/basics?redirected=true#endpoints). Your endpoint will need to be manually entered as custom text into the given drop-down box. |
| External ID | (Optional*) External ID of the user to delete. Must include either External ID or Braze ID. |
| Braze ID | (Optional*) Braze ID of the user to delete. Must include either External ID or Braze ID. |

![Delete User by External ID or Braze ID][12]{: style="max-width:40%;margin-left:15px;margin-bottom:15px;"}

{% enddetails %}

{% details Delete User by User Alias %}
__Action - Delete User by User Alias__

| Parameters | Description |
| ---------- | ----------- |
| Endpoint URL | (Required) Your [Braze REST endpoint]({{site.baseurl}}/api/basics?redirected=true#endpoints). Your endpoint will need to be manually entered as custom text into the given drop-down box. |
| Alias Name | The Alias name of the user to be deleted. |
| Alias Label | The Alias label of the user to be deleted. |

![Delete User by Alias][10]{: style="max-width:40%;margin-left:15px;margin-bottom:15px;"}

{% enddetails %}

When done, required fields for an item display __Completed__ on the right. 

Select __Continue__.

#### Part 4: Summary

Here you can view the summary for the connector you created. If you would like to modify the options you chose, select __Back__ or select __Finish__ to complete.

![Connector Summary][16]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

Your connector now displays in the list of connectors on your Tealium Home page. 

![Connector][18]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

#### Part 5: Save and Publish

The actions you configured will now fire when the trigger connections are met. The data populates, in real-time as each action fires. 

![Save/Publish][17]{: style="max-width:40%;margin-left:15px;margin-bottom:15px;"}

## Step 3: Test your Tealium Connector

After your connector is up and running, you should test it to make sure it's working properly. The most simple way to test this is to use a __Trace Tool__.

1. Start a new trace.
2. Examine the real-time log.
3. Check for the action you want to validate by clicking __Actions Triggered__ entry to expand.
4. Look for the action you want to validate and view the log status. 

To learn more about Tealium connector, check out the Tealium documentation, [here][4].

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[4]: https://community.tealiumiq.com/t5/Customer-Data-Hub/About-Connectors/ta-p/17389
[5]: {% image_buster /assets/img/tealium/braze_connector_marketplace.png %}
[6]: {% image_buster /assets/img/tealium/data_source.png %}
[7]: {% image_buster /assets/img/tealium/event_specs.png %}
[8]: {% image_buster /assets/img/tealium/get_code.png %}
[9]: {% image_buster /assets/img/tealium/summary.png %}
[10]: {% image_buster /assets/img/tealium/delete_user_by_alias.png %}
[11]: {% image_buster /assets/img/tealium/track_user_by_user_id.png %}
[12]: {% image_buster /assets/img/tealium/delete_user_by_external_id.png %}
[13]: {% image_buster /assets/img/tealium/track_user_by_alias.png %}
[14]: {% image_buster /assets/img/tealium/track_by_alias_pt2.png %}
[15]: {% image_buster /assets/img/tealium/create_configuration.png %}
[16]: {% image_buster /assets/img/tealium/connector_summary.png %}
[17]: {% image_buster /assets/img/tealium/save_publish.png %}
[18]: {% image_buster /assets/img/tealium/braze_connection.png %}