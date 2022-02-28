---
nav_title: Tealium
article_title: Tealium
page_order: 2
alias: /partners/tealium/
description: "This article outlines the partnership between Braze and Tealium, a universal data hub that enables you to connect mobile, web, and alternative data to other third-party sources."
page_type: partner
search_tag: Partner

---

# Tealium

> [Tealium](https://tealium.com/) is a universal data hub and customer data platform composed of EventStream, AudienceStream, iQ Tag Management that enables you to connect mobile, web, and alternative data from third-party sources. Tealium’s connection to Braze enables a data flow of custom events, user attributes, and purchases that empower you to act on your data in real-time.

![Tealium Overview][22]{: style="border:0;"}

The Braze and Tealium integration allows you to track your users and route data to various user analytics providers. Tealium allows you to:
- Sync Tealium audiences with [AudienceStream]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_audience_stream/) to Braze for use in personalizing Braze campaigns and Canvases or building segments.
- [Import data across platforms](#choose-your-integration-type). Braze offers both a [side-by-side](#side-by-side-sdk-integration) SDK integration for your Android, iOS, and web applications and a [server-to-server](#server-to-server-integration) integration that can be used within any platform that can report event data.<br><br>

{% tabs %}
{% tab EventStream %}
Tealium EventStream is a data collection and API hub that sits at the center of your data. EventStream handles the entire data supply chain from setup and installation to identifying, validating, and enhancing incoming user data. EventStream takes real-time action with event feeds and connectors. Listed below are the features that make up the [EventStream](https://community.tealiumiq.com/t5/Customer-Data-Hub/Introduction-to-EventStream/ta-p/20387#toc-hId--2077371752).
- Data sources (installation and data collection)
- Live events (real-time data inspection)
- Event specifications and attributes (data layer requirements and validation)
- Event feeds (filtered event types)
- Event connectors (API hub actions)

{% endtab %}
{% tab AudienceStream %}

Tealium AudienceStream is an omnichannel customer segmentation and real-time action engine. AudienceStream takes the data that flows into EventStream and creates visitor profiles that represent the most important attributes of your customers' engagement with your brand. Check out our documentation on how to set up [AudienceStream]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_audience_stream/).

{% endtab %}
{% endtabs %}

{% alert important %}
Tealium offers both batch and non-batch connector actions. The non-batch connector should be used when real-time requests are important to the use case, and there are no concerns about hitting Braze's API rate limit specifications. Please contact Braze Support or your CSM if you have any questions. 

For batch connectors requests are queued until one of the following thresholds is met:
- Max number of requests: 75
- Max time since oldest request: 10 minutes
- Max size of requests: 1 MB

Note: by default Tealium does not batch consent events (subscription preferences) or user deletion events.
{% endalert %}

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Tealium account | A [Tealium account](https://my.tealiumiq.com/) with both server and client-side access is required to take advantage of this partnership. |
| Installed source and Tealium source [libraries](https://community.tealiumiq.com/t5/Customer-Data-Hub/Data-Sources/ta-p/17933) | The origin of any data sent into Tealium, such as mobile apps, websites, or backend servers.<br><br>You must install the libraries into your app, site, or server before being able to set up a successful Tealium connector. |
| Braze REST and SDK endpoint | Your REST or SDK endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/api/basics/#endpoints). |
| Braze app identifier key | (Side-by-side only) Your app identifier key. <br><br>This can be found within the **Braze Dashboard > Manage Settings > API Key**. |
| REST API Key | (Server-to-server only) A Braze REST API key with `users.track` and `users.delete` permissions. <br><br>This can be created within **Braze Dashboard > Developer Console > REST API Key > Create New API Key**.|
{: .reset-td-br-1 .reset-td-br-2}

## Choose your integration type

| Integration | Details |
| ----------- | ------- |
| [Side-by-side](#side-by-side-sdk-integration) | Uses Tealium’s SDK to translate events into Braze’s native calls, allowing access to deeper features and more comprehensive usage of Braze than the server-to-server integration.<br><br>If you plan on using Braze remote commands note that Tealium does not support all Braze methods (e.g., Content Cards). To use a Braze method that isn’t mapped through a corresponding remote command, you will have to invoke the method by adding native Braze code to your codebase.|
| [Server-to-server](#server-to-server-integration) | Forwards data from Tealium to Braze’s REST API endpoints.<br><br>Does not support Braze UI features such as in-app messaging, News Feed, Content Cards, or push notifications. There also exists automatically captured data, such as device-level fields, that are not available through this method.<br><br>Consider a side-by-side integration if you wish to use these features.|
{: .reset-td-br-1 .reset-td-br-2}

## Side-by-side SDK integration

### Remote commands

Remote commands allow you to trigger code in your apps by using a tag in Tealium iQ Tag Management - which collects, controls, and delivers event data from mobile applications allowing you to configure a native Braze implementation without having to add Braze-specific code to your apps. Instead, the Braze remote command module will automatically install and build the required Braze libraries. To use Braze mobile remote command, you will need Tealium libraries installed in your apps.

Using remote commands, the Braze and Tealium SDKs work in tandem, allowing you to make calls from the Tealium SDK - through the Braze servers - to Braze. **The Braze SDK will continue to handle all message rendering and analytics tracking**.

### Mobile remote commands

Tealium offers two ways to integrate Mobile Remote Command, there is no loss of functionality between integration types and the underlying native code is identical:

#### Remote Command Tag
Remote commands Tag allows clients to trigger code in their apps by using a tag set up in Tealium iQ Tag Management UI.
| Pros | Cons |
| ---- | ---- |
| Easily modify the mappings and data being sent to the remote command using the Tealium iQ UI. This allows us to send additional data or events to a 3rd party SDK once the app is already in the app store, without the client having to update the app. | The Tag Management module in the app relies on a hidden webview to process JavaScript. |
{: .reset-td-br-1 .reset-td-br-2}

#### JSON Configuration File. 
This is Tealium's recommended approach as [noted here](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#how-it-works) in their documentation. 
| Pros | Cons |
| ---- | ---- |
| Using the JSON method eliminates the need to have a hidden webview in the app, and greatly reduces memory consumption. | The JSON file can be hosted remotely or locally within the customer's app. | At the moment, there is no UI to manage this, so it requires a bit of extra effort.<br><br>Note: Tealium is working on adding a management UI that will solve this issue and bring the same level of flexibility to JSON remote commands as they have with the iQ Tag management version |
{: .reset-td-br-1 .reset-td-br-2}

Use Braze mobile remote command data mappings to set default user attributes and custom attributes and track purchases and custom events. It will also allow you to track location and social data on Twitter and Facebook - like the number of followers or friends a user has. Check out the remote command chart to see the corresponding Braze methods.

![Remote command mappings][23]{: style="max-width:60%;"}

You can find more details on how to set up Braze mobile remote command, as well as an overview of supported methods in the Tealium developer [documentation](https://community.tealiumiq.com/t5/Client-Side-Tags/Braze-Mobile-Remote-Command-Tag-Setup-Guide/ta-p/32828).
- [Remote command](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#json-template)
- [Remote command tag](https://community.tealiumiq.com/t5/Client-Side-Tags/Braze-Mobile-Remote-Command-Tag-Setup-Guide/ta-p/32828)

{% alert important %}
Braze mobile remote commands do not support all Braze methods and messaging channels (e.g., Content Cards). To use a Braze method that isn't mapped through a corresponding remote command, you will have to invoke the method directly by adding native Braze code to your codebase.
{% endalert%}

### Braze Web SDK tag

Use the Braze Web SDK Tag to deploy Braze’s Web SDK to your website. [Tealium iQ Tag Management](https://community.tealiumiq.com/t5/iQ-Tag-Management/Introduction-to-iQ-Tag-Management/ta-p/15883) Management  allows customers to add Braze as a tag within the Tealium dashboard to track visitor activity. Tags are typically used by marketers to understand the efficacy of online advertising, email marketing, and site personalization.

1. In Tealium, navigate to **iQ [Tag Management](https://community.tealiumiq.com/t5/iQ-Tag-Management/Tags/ta-p/5016) > Tags > + Add Tag > Braze Web SDK**.
2. In the Tag Configuration dialogue box, enter the API Key (your Braze app identifier key), Base URL (Braze SDK endpoint), and Braze Web SDK code version](https://github.com/Appboy/appboy-web-sdk/blob/master/CHANGELOG.md). You can also choose to enable logging to log information in the web console for debugging purposes.
3. In the [Load Rules]((https://community.tealiumiq.com/t5/iQ-Tag-Management/Load-Rules/ta-p/5098) dialogue box, choose "Load on All Pages" or select **Create Rule** to determine when and where to load an instance of this tag on your site.
4. In the **[Data Mappings](https://community.tealiumiq.com/t5/iQ-Tag-Management/Data-Mappings/ta-p/10645#mapping_data_sources)** dialogue box, select **Create Mappings** to map Tealium data to Braze. The destination variables for the Braze Web SDK tag are built into the **Data Mapping** tab for the tag. The [following tables](https://community.tealiumiq.com/t5/Client-Side-Tags/Braze-Web-SDK-Tag-Setup-Guide/ta-p/20106#toc-hId--2077373923) list the available destination categories and describe each destination name.
5. Select **Finish**.

### Side-by-side integrations resources

- iOS remote command: [Tealium documentation](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [Tealium Github repository](https://github.com/Tealium/tealium-ios-braze-remote-command)
- Android remote command: [Tealium documentation](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [Tealium Github repository](https://github.com/Tealium/tealium-android-braze-remote-command)
- Web SDK tag: [Tealium documentation](https://community.tealiumiq.com/t5/Client-Side-Tags/Braze-Web-SDK-Tag-Setup-Guide/ta-p/20106)

## Server-to-server integration

This integration forwards data from Tealium to the Braze REST API.

Server-to-server integration does not support Braze UI features like in-app messaging, News Feed, Content Cards, or push notifications. There also exists automatically captured data (such as device-level fields) that are not available through this method.

If you wish to use this data and these features, consider our [side-by-side]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#side-by-side-sdk-integration) SDK integration.

### Step 1: Set up a Source

Tealium requires that you first set up a valid data source for your connector to draw from.
1. From the left sidebar in Tealium under **Server-Side**, navigate to **Sources > Data Sources > + Add Data Source**.
2. Locate your desired platform within the available categories, and name your source, this is a required field.<br>![Data Source][6]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
3. From the **Event Specifications** options, choose the [event specs](https://community.tealiumiq.com/t5/Customer-Data-Hub/Event-Specifications/ta-p/19329) you would like to include. Event specifications help you identify the event names and required attributes to track in your installation. These specifications will be applied to incoming events.<br>![Event Specs][7]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>Take some time to think about what data is most valuable to you and which specifications seem most appropriate for your use case. [Custom event specifications][19] are also available. <br>
4. The next dialogue advances to the **Get Code** step. The base code and event tracking code provided here serve as your installation guide. Download the provided PDF if you wish to share these instructions with your team. Select **Save & Continue** once finished.<br>![Get Code][8]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>
5. You will now be able to view your saved source as well as add or remove event specs. <br>![Connector][18]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>From the detailed data source view you can perform the following actions:
- View and copy the data source key
- View installation instructions
- Return to the **Get Code** page
- Add or remove event specifications
- View live events related to an event specification
- And more...<br>
6. Lastly, select **Save / Publish** found at the top of the page. If you do not publish your source, you will be unable to find it when configuring your Braze connector.

For further instruction on setting up and editing your data source, check out [Data soures](https://community.tealiumiq.com/t5/Customer-Data-Hub/Data-Sources/ta-p/17933).

### Step 2: Create an event connector

A connector is an integration between Tealium and another vendor used to transmit data. These connectors contain actions that represent their partner's supported APIs. 

1. From the left sidebar in Tealium under **Server-Side**, navigate to **EventStream > Event Connectors**.
2. Select the blue **+ Add Connector** button to look through the connector marketplace. In the new dialogue box that appears, use the spotlight search to find the **Braze** connector.
3. To add this connector, click the **Braze** connector tile. Once clicked, you can view the connection summary and a list of the required information, supported actions, and configuration instructions. Configuration comprises four steps: source, configuration, action, and summary.

#### Source

Once the source has been configured, navigate back to the Braze connector page under **EventStream > Event Connectors > + Add Conncetor > Braze**. 

In the dialogue that opens, select the data source you just built, and under **Event Feed**, select **All Events** or a specific event spec, if needed. Click **Continue**.

#### Configuration

Next, select **Add Connector** at the bottom of the page. You must name your connector and provide your Braze API endpoint and Braze REST API key here.

![Create Configuration][15]{: style="max-width:70%;"}

If you have created a connector before, you may optionally use an existing one from the available connector list and modify it to fit your needs with the pencil icon or delete it with the trash icon. 

#### Action

Next, name your connector action and select an action type that will send data according to the mapping you configure. Here, you will map Braze attributes to Tealium attribute names. Depending on which action type you choose, there will be a varied selection of fields required by Tealium. Listed below are examples and explanations of these fields.

{% alert important %}
**Note that not all fields offered are required**. <br>If you wish to skip over a field, Tealium requires that you minimize it before continuing onto the next step.

![Minimize]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:80%"}
{% endalert %}

{% tabs local %}
{% tab Track User %}

This action allows you to track user, event, and purchase attributes all in one action.

| Parameters | Description |
| ---------- | ----------- |
| User ID | Use this field to map the Tealium user ID field to its Braze equivalent. <br><br>- External ID and Braze ID should not be specified if importing push tokens.<br>- If specifying a user alias, the alias name and alias label should be set. <br><br>For more information, check out the Braze [/users/track endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). |
| User attributes | Use Braze's existing user profile field names to update user profile values in the Braze dashboard or add your own custom [user attribute]({{site.baseurl}}/api/objects_filters/user_attributes_object/) data to the user profiles.<br><br>- By default, new users will be created if one does not exist.<br>- By setting **Update Existing Only** to `true`, only existing users will be updated, and no new user will be created. |
| Modify user attributes | Use this field to increment or decrement certain user attributes<br><br>- Integer attributes may be incremented by positive or negative integers.<br>- Array attributes may be modified by adding or removing values from existing arrays. |
| Event attributes | An event represents a single occurrence of a custom event by a particular user at a timestamp. Use this field to track and map event attributes like those in the Braze [event object]({{site.baseurl}}/api/objects_filters/event_object/). <br><br>- Event attribute `Name` is required for every mapped event.<br>- Event attribute `Time` is automatically set to now unless explicitly mapped. <br>- By default, new events will be created if one does not exist. By setting `Update Existing Only` to `true`, only existing events will be updated, and no new event will be created.<br>-  Map array type attributes to add multiple events. Array type attributes must be of equal length.<br>- Single value attributes can be used and applied to each event. |
| Purchase attributes | Use this field to track and map user purchase attributes like those in the Braze [purchase object]({{site.baseurl}}/api/objects_filters/purchase_object/).<br><br>- Purchase attributes `Product ID`, `Currency` and `Price` are required for every mapped purchase.<br>- Purchase attribute `Time` is automatically set to now unless explicitly mapped.<br>- By default, new purchases will be created if one does not exist. By setting `Update Existing Only` to `true`, only existing purchases will be updated, and no new purchase will be created.<br>- Map array type attributes to add multiple purchase items. Array type attributes must be of equal length.<br>- Single value attributes can be used and will apply to each item.|
{: .reset-td-br-1 .reset-td-br-2}

![Track User Example]({% image_buster /assets/img/tealium/track_user_example.jpg %}){: style="max-width:80%"}

{% endtab %}
{% tab Delete User %}

This action allows you to delete users from the Braze dashboard.

| Parameters | Description |
| ---------- | ----------- |
| User ID | Use this field to map the Tealium User ID field to it's Braze Equivalent. <br><br>- Map one or more user ID attributes. When multiple IDs are specified, the first non-blank value is picked based on the following priority order: External ID, Braze ID, Alias Name & Alias Label.<br>- When specifying a user alias, Alias Name and Alias Label should both be set.<br><br>For more information, see the Braze [/users/delete endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/). |
{: .reset-td-br-1 .reset-td-br-2}

![Delete Users]({% image_buster /assets/img/tealium/track_user_delete.png %}){: style="max-width:70%"}

{% endtab %}
{% endtabs %}

Select **Continue**.

#### Summary

View the summary of the connector you created. If you would like to modify your chosen options, select **Back** to edit or **Finish** to complete.

![Connector Summary][16]{: style="max-width:80%;"}

Your connector now displays in the list of connectors on your Tealium home page. <br>![Connector][13]{: style="max-width:80%;"}

Make sure to **Save / Publish** your connector once finished. The actions you configured will now fire when the trigger connections are met. 

### Step 3: Test your Tealium connector

After your connector is up and running, you should test it to ensure it's working properly. The most simple way to test this is to use the Tealium **Trace Tool**.

1. To start a new trace, select **Trace** on the left sidebar under **Server-Side** options.
2. Examine the real-time log.
3. Check for the action you want to validate by clicking the **Actions Triggered** entry to expand.
4. Look for the action you want to validate and view the log status. 

For more detailed instructions on implementing Tealium's Trace tool, check out their [trace documentation][21]. 

## Potential data point overages

There are three primary ways that you might accidentally hit data overages when integrating Braze through Tealium:

#### Insufficient data logging
Tealium does not send Braze deltas of user attributes. For example, if you have an EventStream action that tracks a user's first name, email, and cell phone number, Tealium will send all three attributes to Braze anytime the action is triggered. Tealium won't be looking for what changed or was updated and send only that information.<br><br> 
**Solution**: <br>You can check your backend to assess whether an attribute has changed or not, and if so, call Tealium’s relevant methods to update the user profile. **This is what users who integrate Braze directly usually do.** <br>**OR**<br> If you don't store your own version of a user profile in your backend and can’t tell if attributes change or not, you can use AudienceStream to track user attribute changes.

#### Sending irrelevant data
If you have multiple EventStreams that target the same event feed, **all actions enabled for that connector** will automatically fire anytime a single action is triggered, **this could also result in data being overwritten in Braze.**<br><br>
**Solution**: <br>Set up a separate event specification or feed to track each action. <br>**OR**<br> Disable actions(or connectors) that you do not want to fire by using the toggles in the Tealium dashboard.

#### Initializing Braze too early
Users integrating with Tealium using the Braze Web SDK tag may see a dramatic increase in their MAU. **If Braze is initialized on page load, Braze will create an anonymous profile every time a web user navigates to the website for the first time.** Some may want to only track user behavior once users have completed some action, such as "Signed In" or "Watched Video", to lower their MAU count. <br><br>
**Solution**: <br>Set up load rules to determine exactly when and where a tag loads on your site. You can learn more about load rules and how to set them up in the [Tealium learning center](https://community.tealiumiq.com/t5/Customer-Data-Hub/Building-an-Audience/ta-p/11881).

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[5]: {% image_buster /assets/img/tealium/braze_connector_marketplace.png %}
[6]: {% image_buster /assets/img/tealium/data_source.png %}
[7]: {% image_buster /assets/img/tealium/event_specs.png %}
[8]: {% image_buster /assets/img/tealium/get_code.png %}
[9]: {% image_buster /assets/img/tealium/summary.png %}
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[13]: {% image_buster /assets/img/tealium/summary_list.png %}
[15]: {% image_buster /assets/img/tealium/create_configuration.png %}
[16]: {% image_buster /assets/img/tealium/connector_summary.png %}
[17]: {% image_buster /assets/img/tealium/save_publish.png %}
[18]: {% image_buster /assets/img/tealium/braze_connection.png %}
[19]: https://community.tealiumiq.com/t5/Customer-Data-Hub/Event-Specifications/ta-p/19329#toc-hId--2078027338
[21]: https://community.tealiumiq.com/t5/Customer-Data-Hub/Trace/ta-p/12058
[22]: {% image_buster /assets/img/tealium/tealium_overview.png %}
[23]: {% image_buster /assets/img/tealium/remote_mappings.png %}