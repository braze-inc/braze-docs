---
nav_title: Tealium AudienceStream
page_order: 2.1
alias: /partners/tealium_audience_stream/

description: "This article outlines the partnership between Braze and Tealium, a universal data hub that enables you to connect mobile, web, and alternative data to other third-party sources."
page_type: partner

---

# Tealium AudienceStream

> Tealium AudienceStream is an Omnichannel customer segmentation and real-time action engine. AudienceStream takes the data that flows into EventStream and creates visitor profiles that represent the most important attributes of your customers' engagement with your brand. 

Tealium AudienceStream visitor profiles are segmented by shared behaviors to create audiences, sets of visitors with common traits. These audiences fuel your marketing technology stack in real-time via connectors. For more information on AudienceStream, check out the Tealium Documentation [here](https://community.tealiumiq.com/t5/Customer-Data-Hub/Introduction-to-AudienceStream/ta-p/16087).

## Pre-Requisites

| Name | Description |
| ---- | ----------- |
| REST API Key | A Braze REST API Key with `users.track` permissions. <br><br>This can be created within the __Braze Dashboard__ -> __Developer Console__ -> __REST API Key__ -> __Create New API Key__ |
| Tealium Account & Account Information | You must have an active Tealium Account with both Server and Client-Side Access to utilize AudienceStream with Braze. |
| [Braze REST Endpoint][6] | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Please note that Tealium AudienceStreams and EventStreams are batched according to Braze specifications so that our customers do not run the risk of exceeding the [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) rate limit. 
{% endalert %}

## Step 1: Set up Attributes and Badges

### Understanding Attributes

The first step in using AudienceStream is to create attributes. Attributes allow you to define the important characteristics that represent a visitor's habits, preferences, actions, and engagement with your brand. 

__Visit Attributes__: Visit attributes relate to the current visit (or session) of the user. The data stored in these attributes persist for the length of the visit. Some example visit attributes:
- Visit Duration (Number)
- Current Browser (String)
- Current Device (String)
- Page View Count (Number)

__Visitor Attributes__: Visitor attributes relate to the current user. The data stored in these attributes persist for the lifetime of the user. Some example visitor attributes would be: 
- Lifetime Order Value (Number)
- First Name (String)
- Birthdate (Date)
- Purchases Brands (Tally)

To look at a full list of data types, check out this [Tealium documentation][1].

### Attribute Enrichments

Once you identify your desired attributes, you can configure them with enrichments -  business rules that determine when and how to update the values of attributes. Each data type offers its own selection of enrichments for manipulating the attribute's value. This is associated with the "WHEN" setting. The following options are available for each visit and visitor attribute:

- New Visitor – occurs the first time a visitor comes to your site
- New Visit – occurs on a new visit by a visitor
- Any Event – occurs on any event
- Visit Ended – occurs when a visit ends

### Badges

Badges are special visitor attributes that represent interesting behavior patterns. Badges are assigned or removed from visitors based on the logic of their enrichments. This logic usually combines multiple conditions into one to capture visitor segments or sets a threshold for when a particular value is reached.

### Attribute and Badge Example

{% tabs local %}
{% tab Attribute %}

Looking at the visitor attribute `Lifetime Order Value`, this visitor attribute calculates the cumulative amount spent by the customer for all completed orders. To set up Lifetime Order Value in your Tealium Account, follow the instructions below.

1. Navigate to __AudienceStream -> Visitor/Visit Attributes__ and click __Add Attribute__.
2. Select the scope as __Visitor__ and click __Continue__.
3. Select the data type __Number__ and click __Continue__.
4. Enter the name of the attribute, "Lifetime Order Value".
5. Click __Add Enrichment__ and select __Increment or Decrement Number__.
6. Select the attribute containing the value to increment by (order_total).
7. Leave the "WHEN" set to "Any Event".
8. Click __Save__, then __Finish__.

Now, all customers will have a Lifetime Order Value attribute tied to them.

{% endtab %}
{% tab Badge %}

Next, you may create badges that help you classify and target your users by certain attributes they share. For the example below, we will be creating a VIP Badge for users who have a lifetime value of over $500.

1. Navigate to __AudienceStream -> Visitor/Visit Attributes__ and click __Add Attribute__.
2. Select the scope as __Visitor__ and click __Continue__.
3. Select the data type __Badge__ and click __Continue__.
4. Enter the name of the badge, "VIP".
5. Click __Add Enrichment__ and select __Assign Badge__.
6. Create a rule for badge assignment by selecting __Create Rule__.
7. Assign a title to this rule, and using the previous attribute created, set the rule to "...has attribute __Lifetime Order Value greater than 500__"
8. Leave the "WHEN" set to "Any Event".
9. Click __Save__, then __Finish__.

{% endtab %}
{% endtabs %}

To read more about Attributes and Badges, check out the [Tealium documentation](https://community.tealiumiq.com/t5/Getting-Started-with/Attributes-Enrichments/ta-p/25786). 

## Step 2: Create an Audience

From the Tealium customer data hub main page, select __Audience__ under __AudienceStream__ from the left side of the page. Here you will be able to create an audience of users that have common attributes you select. 

First, name your audience and then take some time to think about what kind of attributes would be applicable for the type of audience you are trying to create. For example, to create an audience of VIP cart abandoners, you could create an audience of visitors who have the __VIP badge__ a __Cart Abandoner badge__ assigned.

## Step 3: Create an Audience Connector

From the main page, select __Audience Connector__ under __AudienceStream__. Here you can create and configure your connector. From the Audience Connector page, select __+ Add Connector__, look up __Braze__, and select __Braze__ as the connector type. 

### Select Source

In the new window that appears, you will now be able to select the audience that you created in the previous step, as well as select a trigger that you feel is appropriate for your situation. You also have the option to the toggle on frequency cap to control how often this action triggers. 

### Configuration

![Create Configuration][15]{: style="float:right;max-width:30%;margin-left:15px;margin-bottom:15px;"}

Next, a __Configuration__ dialogue will appear. Here, you must select __Add Connector__ and fill in certain values requested by Tealium and Braze:

If you have created a connector before, you may optionally use an existing from the available connector list and modify it to fit your needs with the pencil icon or delete it with the trash icon. 

After you have selected a connector to link this audience to click done and continue. 

### Action

Next, you must select a connector action. A connector action sends data according to the mapping that you configure. The Braze connector allows you to map Braze Attributes to Tealium attribute names. 

1. From the __Action__ dialogue, select one of the actions to set up.
2. Depending on which action you chose, there will be a varied selection of fields required by Tealium. Listed below are examples and explanations of these fields.

{% alert important %}
__Note that not all fields offered are required__. <br>If you wish to skip over a field, Tealium requires that you __minimize it__ before continuing onto the next step.

![Minimize]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:80%"}
{% endalert %}

{% tabs local %}
{% tab Track User %}

This action allows you to track user, event, and purchase attributes all in one action.

| Parameters | Description |
| ---------- | ----------- |
| User ID | Use this field to map the Tealium User ID field to its Braze Equivalent. <br><br>- If importing Push Tokens, External ID and Braze ID should not be specified.<br>- If specifying a user alias, Alias Name and Alias Label should both be set. <br><br>For more information, check out the Braze [/users/track endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). |
| User Attributes | Use Braze's existing User Profile field names to update user profile values in the Braze Dashboard or add your own custom attribute data to the user profiles.<br><br>- By default new users will be created if one does not exist.<br>- By setting `Update Existing Only` to `true` only existing users will be updated and no new user will be created.<br><br>To read more about the User Attributes Object, check out our [documentation]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| Modify User Attributes | Use this field to increment or decrement certain user attributes<br><br>- Integer attributes may be incremented by positive or negative integers.<br>- Array attributes may be modified by adding or removing values from existing arrays. |
| Event Attributes | An Event represents a single occurrence of a Custom Event by a particular user at the designated time value. Use this field to track and map event attributes like those in the Braze Event Object. <br><br>- Event Attribute `Name` is required for every mapped event.<br>- Event attribute `Time` is automatically set to now unless explicitly mapped. <br>- By default, new events will be created if one does not exist. By setting `Update Existing Only` to `true` only existing events will be updated and no new event will be created.<br>-  Map Array type attributes to add multiple events. Array type attributes must be of equal length.<br>- Single value attributes can be used and will apply to each event.<br><br>To read more about the Braze Event Object, check out our [documentation]({{site.baseurl}}/api/objects_filters/event_object/). |
| Purchase Attributes | Use this field to track and map user purchase attributes like those in the Braze Purchase Object.<br><br>- Purchase attributes `Product ID`, `Currency` and `Price` are required for every mapped purchase.<br>- Purchase attribute `Time` is automatically set to now unless explicitly mapped.<br>- By default, new purchases will be created if one does not exist. By setting `Update Existing Only` to `true` only existing purchases will be updated and no new purchase will be created.<br>- Map Array type attributes to add multiple purchase items. Array type attributes must be of equal length.<br>- Single value attributes can be used and will apply to each item.<br><br>To read more about the Braze Purchase Object, check out our [documentation]({{site.baseurl}}/api/objects_filters/purchase_object/)|
{: .reset-td-br-1 .reset-td-br-2}

![Track User Example]({% image_buster /assets/img/tealium/track_user_example.jpg %}){: style="max-width:70%"}

{% endtab %}
{% tab Delete User %}

This action allows you to delete users from the Braze Dashboard.

| Parameters | Description |
| ---------- | ----------- |
| User ID | Use this field to map the Tealium User ID field to it's Braze Equivalent. <br><br>- Map one or more user ID attributes. When multiple IDs are specified, the first non-blank value is picked based on the following priority order: External ID, Braze ID, Alias Name & Alias Label.<br>- When specifying a user alias, Alias Name and Alias Label should both be set.<br><br>For more information, see the Braze [/users/delete endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/). |
{: .reset-td-br-1 .reset-td-br-2}

![Delete Users]({% image_buster /assets/img/tealium/track_user_delete.png %}){: style="max-width:70%"}

{% endtab %}
{% endtabs %}

Select __Continue__.

### Save and Publish
![Save/Publish][17]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}
The actions you configured will now fire when the trigger connections are met. The data populates, in real-time as each action fires. 

## Step 4: Test your Tealium Connector

After your connector is up and running, you should test it to make sure it's working properly. The most simple way to test this is to use the Tealium __Trace Tool__.

1. Start a new trace. This can be done by selecting Trace on the left sidebar under `Server-Side` options.
2. Examine the real-time log.
3. Check for the action you want to validate by clicking __Actions Triggered__ entry to expand.
4. Look for the action you want to validate and view the log status. 

For more detailed instructions on how to implement Tealium's Trace tool, check out their [Trace documentation][21]. 

## Potential Data Point Overages

There are three primary ways that you might accidentally hit data overages when integrating Braze through Tealium. 

#### __Insufficient Data Logging__
Tealium does not send Braze deltas of user attributes. For example, if you have an EventStream action that tracks a user's first name, email, and cell phone number, Tealium will send all three attributes to Braze anytime the action is triggered. Tealium won't be looking for what changed or was updated and send only that information.<br><br> 
__Solution__: <br>You can check your own backend to assess whether an attribute has changed or not and if so, call Tealiums’s relevant methods to update the user profile. __This is what users who integrate Braze directly usually do.__ <br>__OR__<br> If you don't store your own version of a user profile in your backend, and can’t tell if attributes change or not, you can use AudienceStream to track user attribute changes.

#### __Sending Irrelevant Data__
If you have multiple EventStream that target the same event feed, __all actions enabled for that connector__ will automatically fire anytime a single action is triggered, __this could also result in data being overwritten in Braze.__<br><br>
__Solution__: <br>Set up a separate event specification or feed to track each action. <br>__OR__<br> Disable actions(or connectors) that you do not want to fire by using the toggles in the Tealium dashboard.

#### __Initalizing Braze too Early__
Users integrating with Tealium using the Braze Web SDK Tag may see a dramatic increase in their MAU. __If Braze is initialized on page load, Braze will create an anonymous profile every time a web user navigates to the website for the first time.__ Some may want to only track user behavior once users have completed some action, such as "Signed In" or "Watched Video" in order to lower their MAU count. <br><br>
__Solution__: <br>Set up Load Rules to determine exactly when and where a Tag loads on your site. You can learn more about Load Rules and how to set them up in the [Tealium Learning Center](https://community.tealiumiq.com/t5/Customer-Data-Hub/Building-an-Audience/ta-p/11881).


[1]: https://community.tealiumiq.com/t5/Getting-Started-with/Attributes/ta-p/25785
[15]: {% image_buster /assets/img/tealium/create_configuration.png %}
[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[21]: https://community.tealiumiq.com/t5/Getting-Started-with/Trace/ta-p/25797
[17]: {% image_buster /assets/img/tealium/save_publish.png %}