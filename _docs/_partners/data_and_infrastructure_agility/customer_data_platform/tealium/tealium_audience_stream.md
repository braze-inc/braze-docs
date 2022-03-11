---
nav_title: Tealium AudienceStream
article_title: Tealium AudienceStream
page_order: 2.1
alias: /partners/tealium_audience_stream/
description: "This article outlines the partnership between Braze and Tealium, a universal data hub that enables you to connect mobile, web, and alternative data to other third-party sources."
page_type: partner
search_tag: Partner

---

# Tealium AudienceStream

> Tealium [AudienceStream](https://community.tealiumiq.com/t5/Customer-Data-Hub/Introduction-to-AudienceStream/ta-p/16087) is an Omnichannel customer segmentation and real-time action engine. AudienceStream takes the data that flows into EventStream and creates visitor profiles representing the most important attributes of your customers' engagement with your brand. 

The Braze and Tealium integration leverages AudienceStream visitor profiles. Shared behaviors segment these profiles to create sets of visitors with common traits, known as audiences. These audiences can help fuel your marketing technology stack in real-time via connectors. 

{% alert important %}
Please note that Tealium AudienceStreams and EventStreams are batched according to Braze specifications so that our customers do not run the risk of exceeding the [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) rate limit. Please contact Braze [support]({{site.baseurl}}/braze_support/) or your CSM if you have any questions. 
{% endalert %}

## Prerequisites

| Name | Description |
| ---- | ----------- |
| Tealium account | A [Tealium account](https://my.tealiumiq.com/) with both server and client-side access is required to take advantage of this partnership. |
| REST API Key | A Braze REST API key with `users.track` and `users.delete` permissions. <br><br>This can be created within **Braze Dashboard** > **Developer Console** > **REST API Key** > **Create New API Key**|
| [Braze REST Endpoint][6] | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Set up attributes and badges

#### Understanding attributes

The first step in using AudienceStream is to create attributes. Attributes allow you to define the important characteristics that represent a visitor's habits, preferences, actions, and engagement with your brand. 

**Visit Attributes**: Visit attributes relate to the user's current visit (or session). The data stored in these attributes persist for the length of the visit. Some example visit attributes include:
- Visit Duration (Number)
- Current Browser (String)
- Current Device (String)
- Page View Count (Number)

**Visitor Attributes**: Visitor attributes relate to the current user. The data stored in these attributes persist for the lifetime of the user. Some example visitor attributes include: 
- Lifetime Order Value (Number)
- First Name (String)
- Birthdate (Date)
- Purchases Brands (Tally)

Visit [Tealium][1] for a full list of available data types.

##### Attribute enrichments

Once you identify your desired attributes, you can configure them with [enrichments](https://community.tealiumiq.com/t5/Getting-Started-with/Attributes-Enrichments/ta-p/25786) - business rules that determine when and how to update the values of attributes. Each data type offers its own selection of enrichments for manipulating the attribute's value. This is associated with the "WHEN" setting. The following options are available for each visit and visitor attribute:

- New Visitor: occurs the first time a visitor comes to your site.
- New Visit: occurs on a new visit by a visitor.
- Any Event: occurs on any event.
- Visit Ended: occurs when a visit ends.

#### Badges

Badges are special visitor attributes that represent valuable behavior patterns. Badges are assigned or removed from visitors based on the logic of their enrichments. This logic usually combines multiple conditions to capture visitor segments or sets a threshold for when a particular value is reached.

#### Attribute and badge example

{% tabs local %}
{% tab Attribute %}

Looking at the visitor attribute `Lifetime Order Value`, this attribute calculates the cumulative amount spent by the customer for all completed orders. To set up Lifetime Order Value in your Tealium account, follow the instructions below:

1. Navigate to **AudienceStream > Visitor/Visit Attributes** and click **Add Attribute**.
2. Select the scope as **Visitor** and click **Continue**.
3. Select the data type **Number** and click **Continue**.
4. Enter the name of the attribute, "Lifetime Order Value".
5. Click **Add Enrichment** and select **Increment or Decrement Number**.
6. Select the attribute containing the value to increment by (order_total).
7. Leave the "WHEN" set to "Any Event".
8. Click **Save**, then **Finish**.

Now, all customers will have a Lifetime Order Value attribute tied to them.

{% endtab %}
{% tab Badge %}

You may create badges that help you classify and target your users by certain attributes they share. For the example below, we create a VIP Badge for users with a lifetime value of over $500.

1. Navigate to **AudienceStream > Visitor/Visit Attributes** and click **Add Attribute**.
2. Select the scope as **Visitor** and click **Continue**.
3. Select the data type **Badge** and click **Continue**.
4. Enter the name of the badge, "VIP".
5. Click **Add Enrichment** and select **Assign Badge**.
6. Create a rule for badge assignment by selecting **Create Rule**. Assign a title to this rule, and using the previous attribute created, set the rule to "...has attribute **Lifetime Order Value greater than 500**".
7. Leave the "WHEN" set to "Any Event".
8. Click **Save**, and then **Finish**.

{% endtab %}
{% endtabs %}

### Step 2: Create an audience

From the Tealium home page, select **Audience** under **AudienceStream** from the left side of the page. Here, you can create an audience of users with common attributes you select. 

First, name your audience, and then take some time to think about what attributes would be applicable for the type of audience you are trying to create. For example, to create an audience of VIP cart abandoners, you could create an audience of visitors who have the **VIP badge** and **Cart Abandoner badge** assigned.

Make sure to **Save / Publish** your connector once finished.

### Step 3: Create an event connector

A connector is an integration between Tealium and another vendor used to transmit data. These connectors contain actions that represent their partner's supported APIs. 

1. From the left sidebar in Tealium under **Server-Side**, navigate to **AudienceStream > Audience Connectors**.
2. Select the blue **+ Add Connector** button to look through the connector marketplace. In the new dialogue box that appears, use the spotlight search to find the **Braze** connector.
3. To add this connector, click the **Braze** connector tile. Once clicked, you can view the connection summary and a list of the required information, supported actions, and configuration instructions. The configuration comprises four steps: source, configuration, action, and summary.

#### Source

In the **Source** dialogue that appears, select the audience you created in the previous step and a trigger that you feel is appropriate for your situation. You also have the option to toggle on the frequency cap to control how often this action triggers. 

#### Configuration

Next, a **Configuration** dialogue will appear. Select **Add Connector** at the bottom of the page. Name your connector and provide your Braze API endpoint and Braze REST API key here.

![Create Configuration]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

If you have created a connector before, you may optionally use an existing from the available connector list and modify it to fit your needs with the pencil icon or delete it with the trash icon. 

After you have selected a connector to link this audience, click **Done** to continue.

#### Action

Next, name your connector action and select an action type that will send data according to the mapping you configure. Here, you will map Braze attributes to Tealium attribute names. Depending on which action type you choose, there will be a varied selection of fields required by Tealium. Listed below are examples and explanations of these fields.

{% alert important %}
**Note that not all fields offered are required**. <br>If you wish to skip over a field, Tealium requires that you **minimize it** before continuing onto the next step.

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

![Track User Example]({% image_buster /assets/img/tealium/track_user_example.png %}){: style="max-width:80%"}

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

Your connector now displays in the list of connectors on your Tealium home page.

Make sure to **Save / Publish** your connector once finished. The actions you configured will now fire when the trigger connections are met. 

### Step 4: Test your Tealium connector

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

[1]: https://community.tealiumiq.com/t5/Getting-Started-with/Attributes/ta-p/25785
[15]: {% image_buster /assets/img/tealium/create_configuration.png %}
[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[21]: https://community.tealiumiq.com/t5/Getting-Started-with/Trace/ta-p/25797
[17]: {% image_buster /assets/img/tealium/save_publish.png %}