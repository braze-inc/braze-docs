---
nav_title: Tealium AudienceStream
page_order: 1
alias: /partners/tealium_audience_stream/

description: "This article outlines the partnership between Braze and Tealium, a universal data hub that enables you to connect mobile, web, and alternative data to other third-party sources."
page_type: partner

---

# Tealium AudienceStream

Tealium AudienceStream is an Omnichannel customer segmentation and real-time action engine. AudienceStream takes the data that flows into EventStream and creates visitor profiles that represent the most important attributes of your customers' engagement with your brand. These visitor profiles are segmented by shared behaviors to create audiences, sets of visitors with common traits. These audiences fuel your marketing technology stack in real-time via connectors. For more information on AudienceStream, check out the Tealium Documentation [here](https://community.tealiumiq.com/t5/Customer-Data-Hub/Introduction-to-AudienceStream/ta-p/16087).

## Pre-Requisites

| Name | Description |
| ---- | ----------- |
| REST API Key | A Braze REST API Key with `users.track` permissions. <br><br>This can be created within the __Braze Dashboard__ -> __Developer Console__ -> __REST API Key__ -> __Create New API Key__ |
| Tealium Account & Account Information | You must have an active Tealium Account with both Server and Client Side Access to utilize their services with Braze. |
| [Braze REST Endpoint][6] | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |

## Understanding Attributes

Attributes allow you to define the important characteristics that represent a visitor's habits, preferences, actions, and engagement with your brand.

__Visit Attributes__
Visit attributes relate to the current visit (or session) of the user. The data stored in these attributes persists for the length of the visit. Some example visit attributes:
- Visit Duration (Number)
- Current Browser (String)
- Current Device (String)
- Page View Count (Number)

__Visitor Attributes__
Visitor attributes relate to the current user. The data stored in these attributes persist for the lifetime of the user. Some example visitor attributes would be: 
- Lifetime Order Value (Number)
- First Name (String)
- Bithdate (Date)
- Purchases Brands (Tally)

To look at a full list of data types, check out this [Tealium documentation][1].

## Enrichments
Once you identify you desired sttributes, you will configure them with enrichments, rules that determine when and how to update the values of attributes. Each data type offers its own selection of enrichments for manipulating the attribute's vlaue. 


## Step 0: Create Attributes

The first step in using AudienceStream is to create attributes. 




## Step 1: Create Audience

From the Tealium customer data hub main page, select __Audience__ under __Audience Stream__ from the left side of the page. Here you will be able to create an audience of users that have common attributes you select. 

First, name your audience and then take some time to think about what kind of attributes would be applicable for the type of audience you are trying to create. For example, to create an audience of visitors that frequently use your service, you could create an audience of returning visitors, or perhaps visitors that have an average of more than 2 visits per week.  

## Step 2: Create an Audience Connector

From the main page, select __Audience Connector__ under AudienceStream. Here you can create and configure your connector. 

From the Audience Connector page select "+ Add Connector", and select "Braze (formerly Appboy)" as the connector type. 

### Step 2a: Select Source

In the new window that appears, you will now be able to select the audience that you created in the previous step, as well as select a trigger that you feel is appropriate for your situation. You also have the option to the toggle on frequency cap to control how often this action triggers. Lastly, name this action. 


### Step 2b: Configuration

![Create Configuration][15]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

Next, a __Create Configuration__ dialogue will appear. Here, you must fill in certain values requested by Tealium and Braze:

| Name | Description |
| ---- | ----------- |
| Name | The name of the Connector | 
| REST API Key | A Braze REST API Key with __users.track__ permissions. <br><br>This can be set within the __Braze Dashboard -> Developer Console -> REST API Keys -> Create New API Key__ |
| [Braze REST Endpoint][6] | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

If you have created a connector before, you may optionally use an existing from the available connector list and modify it to fit your needs with the pencil icon or delete it with the trash icon. 

After you have selected a connector to link this audience to, click done and continue. 

#### Step 2c: Action

Next, you must select a connector action. A connector action sends data according to the mapping that gets configured. The Braze connector allows you to map Braze attributes to Tealium attribute names. 

1. From the __Add Action__ dialogue, select one of the actions to set up.
2. Depending on which action you chose, there will be a varied selection of fields required by Tealium. Listed below are examples and explanations of these fields.

{% alert important %}
__Note that not all fields offered are required__. <br>If you wish to skip over a field, Tealium requires that you __minimize it__ before continuing onto the next step.

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

![Track User]({% image_buster /assets/img/tealium/audience_stream/track_user_user.png %})

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

![Track Event]({% image_buster /assets/img/tealium/audience_stream/track_user_event.png %})

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

![Track Purchases]({% image_buster /assets/img/tealium/audience_stream/track_user_purchase.png %})

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

![Track Purchases]({% image_buster /assets/img/tealium/audience_stream/track_user_delete.png %})

{% endtab %}
{% endtabs %}

Select __Continue__.

#### Step 2d: Summary

Here, you can view the summary of the Audience Connector you created. If you would like to modify the options you chose, select __Back__ to edit or __Finish__ to complete.

![Connector Summary][16]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}

Your connector now displays in the list of connectors on your Tealium Home page. 

![Connector][13]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}

#### Step 2e: Save and Publish
![Save/Publish][17]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}
The actions you configured will now fire when the trigger connections are met. The data populates, in real-time as each action fires. 

### Step 3: Test your Tealium Connector

After your connector is up and running, you should test it to make sure it's working properly. The most simple way to test this is to use the Tealium __Trace Tool__.

1. Start a new trace. This can be done by selecting Trace on the left sidebar under `Server-Side` options.
2. Examine the real-time log.
3. Check for the action you want to validate by clicking __Actions Triggered__ entry to expand.
4. Look for the action you want to validate and view the log status. 

For more detailed instructions on how to implement Tealium's Trace tool, check out their [Trace documentation][21]. 


[1]: https://community.tealiumiq.com/t5/Getting-Started-with/Attributes/ta-p/25785
[15]: {% image_buster /assets/img/tealium/create_configuration.png %}
[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[21]: https://community.tealiumiq.com/t5/Getting-Started-with/Trace/ta-p/25797
[16]: {% image_buster /assets/img/tealium/connector_summary.png %}
[13]: {% image_buster /assets/img/tealium/summary_list.png %}
[17]: {% image_buster /assets/img/tealium/save_publish.png %}





