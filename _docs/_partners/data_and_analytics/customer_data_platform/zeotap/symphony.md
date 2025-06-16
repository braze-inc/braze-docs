---
nav_title: Zeotap Symphony
description: "This reference article outlines the partnership between Braze and Zeotap, a next-generation customer data platform that provides identity resolution, insights, and enrichment."
page_type: partner
search_tag: Partner
page_order: 2 
---

# Zeotap Symphony

The Braze and Zeotap Symphony integration allows you to create real-time orchestrations and run email and push notification campaigns.

- Send first and last names through Zeotap, based on which users can send personalized emails through Braze.
- Send custom events or a purchase event in real-time through Zeotap, based on which users can create campaign triggers within Braze to target their customers

{% alert note %}
To create email marketing campaigns, onboard the raw emails to Zeotap by mapping them to `Email Raw` in the Zeotap Catalogue.
{% endalert %}

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Client Name | This is your client name for your Braze account. You can find it by navigating to the Braze Console. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Instance | Your Braze instance can be obtained from your Braze onboarding manager or can be found on the [API overview page]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integration

This section provides information about the two methods you can integrate with Braze:

### Method 1
In this method, you have to perform the following tasks:
1. Integrate the Braze SDK on your website or app.
2. Integrate Braze with Zeotap through Symphony.

- `User traits` must be mapped to the respective Braze fields under the **Data To Send** tab. If you map the `Event` and `Purchase` attributes, it leads to the duplication of events within Braze.
- Map `External ID` to `User ID` configured while setting up the Braze SDK.

When the integration is successfully set, you can create email and push notification campaigns based on custom attributes sent to Braze through Symphony.

### Method 2
In this method, you can integrate Braze with Zeotap through Symphony.

- This method does not support the Braze UI features such as in-app messaging, Content Cards, or push notifications.
- Zeotap recommends mapping the `hashed email` available in Zeotap Catalogue to the `External ID`.

When the integration is successfully set, you can only create email campaigns based on custom attributes sent to Braze through Symphony.

## Data flow to Braze and supported identifiers

The data will flow from Zeotap to Braze using the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). The following points summarize the data flow:

1. Zeotap sends user profile attributes, custom attributes, custom events, and purchase fields.
2. You maps all the relevant Zeotap Catalogue fields to the Braze fields under the **Data To Send** tab.
3. The data is then uploaded to Braze.

You can find details about the different attributes under the [Data To Send](#data-to-send-tab) section.

## Destination setup

After applying filters or adding a condition for your users in Symphony, you can activate them in Braze under **Send to Destinations**. A new window opens, where you can set up your destination. You can use an existing destination from the list of **Available Destinations** or create a new one.

#### Add new destination
Perform the following steps to add a new destination:
1. Select **Add New Destination**.
2. Search for **Braze**.
3. Add the **Client Name**, **API Key**, and **Instance** and save the destination.

The destination is created and made available under **Available Destinations**.

#### Add workflow-level inputs
After creating a destination, next, you have to add workflow-level inputs, as mentioned below.
1. Choose the destination from the list of available destinations using the search feature.
2. The **Client Name**, **API Key**, and **Instance** fields are automatically populated based on the value you entered while creating the destination.
3. Enter the **Audience Name** you want to create for this workflow node. This is sent as a **Custom Attribute** to Braze.
4. Complete the Catalog to Destination mapping under the **Data To Send** tab. You can find details on how to perform the mapping below.

#### Data to send tab
The **Data To Send** tab allows the you to map the Zeotap Catalogue fields to the Braze fields that can be sent to Braze. The mapping can be done in one of the following ways:
- **Static Mapping** - There are certain fields that Zeotap automatically maps to the relevant Braze fields like email, phone, first name, last name, and so on.<br>
- **Dropdown Selection** - Map the relevant fields ingested in Zeotap to the Braze fields provided in the dropdown menu.<br>![Various user traits set in Zeotap, such as language, city, birthday, and more.]({% image_buster /assets/img/zeotap/zeotap7.png %}){: style="max-width:70%;"}<br>
- **Custom Data Input** - Add custom data mapped to the relevant Zeotap field and send to Braze.<br>![Selecting "loyalty_points" as the user trait in Zeotap.]({% image_buster /assets/img/zeotap/zeotap8.png %}){: style="max-width:70%;"}

## Supported attributes
You can find details of all the Braze fields in this section.

| Braze Field | Mapping Type | Description |
| --- | --- | --- |
| External ID | Dropdown selection | This is the persistent `User ID` you defined by Braze to track users across devices and platforms. We recommend that you map `User ID` to `External ID`; otherwise, Zeotap may send email as a user alias.<br><br>Zeotap recommends that you map the `hashed email` available in the Zeotap Catalogue to the `External ID`.|
| Email | Static Mapping | This is mapped to `Email Raw` in the Zeotap Catalogue. |
| Phone | Static Mapping | This is mapped to `Mobile Raw` in the Zeotap Catalogue.<br><br>• Braze accepts phone numbers in `E.164` format. Zeotap does not perform any transformation. Hence, you are required to ingest the phone numbers in the prescribed format. For more information, refer to [User phone numbers]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/). |
| First Name | Static Mapping | This is mapped to `First Name` in the Zeotap Catalogue. |
| Last Name | Static Mapping | This is mapped to `Last Name` in the Zeotap Catalogue. |
| Gender | Static Mapping | This is mapped to `Gender` in the Zeotap Catalogue. |
| Custom Event Name | Static Mapping | This is mapped to `Event Name` in the Zeotap Catalogue.<br><br>Both Custom Event Name and Custom Event Timestamp must be mapped to capture custom events in Braze. The custom event cannot be processed if either one is not mapped. For more information, refer to [event object]({{site.baseurl}}/api/objects_filters/event_object#what-is-the-event-object). |
| Custom Event Timestamp | Static Mapping | This is mapped to the `Event Timestamp` in the Zeotap Catalogue.<br><br>Both Custom Event Name and Custom Event Timestamp must be mapped to capture custom events in Braze. The custom event cannot be processed if either one is not mapped. For more information, refer to [event object]({{site.baseurl}}/api/objects_filters/event_object#what-is-the-event-object). |
| Email Subscribe | Dropdown Selection | Onboard an `Email Marketing Preference` field and map to it.<br><br>Zeotap sends the following three values:<br>• `opted_in` - Indicates that the user has explicitly registered for email marketing preference<br>• `unsubscribed` - Indicates that the user has explicitly opted out of email messages<br>• `subscribed` - Indicates that the user has neither opted-in nor opted-out. |
| Push Subscribe | Dropdown Selection | Onboard a `Push Marketing Preference` field and map to it.<br><br>Zeotap sends the following three values:<br>• `opted_in` - Indicates that the user has explicitly registered for push marketing preference<br>• `unsubscribed` - Indicates that the user has explicitly opted out of push messages.<br>• `subscribed` - Indicates that the user has neither opted-in nor opted out |
| Email Open Tracking Enable | Dropdown Selection | Map the relevant `Marketing Preference` field.<br><br>When set to true, it enables an open tracking pixel to be added to all future emails sent to this user. |
| Email Click Tracking Enable | Dropdown Selection | Map the relevant `Marketing Preference` field.<br><br>When set to true, it enables click tracking for all links within all future emails sent to this user. |
| Product ID | Dropdown selection | • Identifier for a purchase action `(Product Name/Product Category)`. For more details, refer to [purchase object]({{site.baseurl}}/api/objects_filters/purchase_object/).<br>• Onboard the relevant attribute to the Zeotap Catalogue and map to it.<br><br>`Product ID`, `Currency`, and `Price` must be mapped mandatorily to capture purchase events in Braze. The purchase event cannot go through if any of the three is missed. For more information, refer to [purchase object]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-object). |
| Currency | Dropdown selection | • Currency attribute for purchase action.<br>• Supported format is `ISO 4217 Alphabetic Currency Code`.<br>• Onboard correctly formatted Currency Data to the Zeotap Catalogue and maps to it.<br><br>`Product ID`, `Currency`, and `Price` must be mapped mandatorily to capture purchase events in Braze. The purchase event cannot go through if any of the three is missed. |
| Price | Dropdown selection | • Price attribute for purchase action.<br>• Onboard the relevant attribute to the Zeotap Catalogue and map to it.<br><br>`Product ID`, `Currency`, and `Price` must be mapped mandatorily to capture purchase events in Braze. The purchase event cannot go through if any of the three is missed. |
| Quantity | Dropdown selection | • Quantity attribute for purchase action.<br>• Onboard the relevant attribute to the Zeotap Catalogue and map to it. |
| Country | Dropdown selection | Map to the `Country` Catalogue field you are onboarding. |
| City | Dropdown selection | Map to the `City` Catalogue field you are onboarding. |
| Language | Dropdown selection | • The accepted format is `ISO-639-1` standard (for example, en).<br>• Onboard correctly formatted language and map to it. |
| Date of Birth | Dropdown selection | Map to the `Date of Birth` field you are onboarding. |
| Custom Attribute | Custom Data Input | Map any user attribute to a custom data input, which is then sent to Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Viewing data on Braze console

After you have mapped the relevant attributes to be sent and published in the workflow, the events start flowing to Braze based on the criteria defined. You can search by email ID or external ID on the Braze console.

![]({% image_buster /assets/img/zeotap/zeotap6.jpg %})

Various attributes come under different sections of the user dashboard within Braze.
- The **Profile** tab contains the user attributes.
- The **Custom Attributes** tab contains the custom attributes defined by the user.
- The **Custom Events** tab contains the custom event defined by the user.
- The **Purchases** tab contains the purchases done over a period of time by the user.

## Campaign creation

Users can create campaigns within Braze and activate users in real-time or based on the scheduled time. Campaigns can be triggered based on the actions performed by the user (custom event, purchase) or user attributes.

