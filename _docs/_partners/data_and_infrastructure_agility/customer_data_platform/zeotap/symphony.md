---
nav_title: Zeotap Symphony
description: "This reference article outlines the partnership between Braze and Zeotap, a next-generation customer data platform that provides identity resolution, insights, and enrichment."
page_type: partner
search_tag: Partner
page_order: 30
---

# Symphony

## Overview
Braze is a customer engagement platform that offers customer-centric interactions between consumers and brands in real-time. It allows the client to power personalised messaging across mobile, SMS, email, web and more.
The Braze integration allows the client to create real-time orchestrations and run email/push notification campaigns.

{% alert note %}
To create email marketing campaigns, onboard the raw emails to Zeotap by mapping them to Email Raw in the Zeotap Catalogue.
{% endalert %}

The following use cases give an understanding of how the integration works between Zeotap and Braze:
- Send First Name and Last Name through Zeotap, based on which clients can send personalized emails through Braze
- Send Custom Event or a Purchase event in real-time through Zeotap, based on which clients can create campaign triggers within Braze to target their customers

## Integration Methods for Braze
This section provides information about the two methods through which clients can integrate with Braze:

### Method 1
In this method, you have to perform the following tasks:
1. Integrate the Braze SDK on your website or app.
2. Integrate Braze with Zeotap through Symphony.

Note
- Only `User traits` must be mapped to the respective Braze fields under the **Data To Send** tab. If you map the `Event` and `Purchase` attributes, it leads to duplication of events within Braze.
- Map `External ID` to `User ID` that was configured while setting up the Braze SDK.

Use Case - With the integration successfully set as mentioned above, you can create Email and Push notification campaigns based on custom attributes sent to Braze through Symphony.

### Method 2
In this method, you can integrate Braze with Zeotap through Symphony.

Note
- The Braze UI features such as in-app messaging, news feed, content cards or push notifications are not supported in this method.
- Zeotap recommends that you map `hashed email` available in Zeotap Catalogue to the `External ID`.

Use Case - With the integration successfully set as mentioned above, you can only create email campaigns based on custom attributes sent to Braze through Symphony.

## Data flow to Braze and Supported Identifiers

Braze records different attributes using their [user track](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) API. The following points summarise the data flow:

1. Zeotap sends user profile attributes, custom attributes, custom events and purchases fields.
2. Client maps all the relevant Zeotap Catalogue fields to the Braze fields under the **Data To Send** tab.
3. The data is then uploaded to Braze.

You can find details about the different attributes under the **Data To Send** section.

### Prerequisites
Ensure that you have the following details available before starting the integration:
- Client Name
- API Key
- Instance

#### Client Name
This is your client name for your Braze account. You can find it by navigating to the Braze Console as shown in the screenshot below.

#### API Key

This is the API Key associated with the Braze account. You can find it in the Braze Console under **Settings > Developer Console > Rest API Keys**.

Your account might already have an existing API key available in this section. However, the User Data Permissions are required for the API key to work. If the existing key does not have the required permissions, create a new key as mentioned below.

1. Click **Create New API key**.
2. Enter the **API Key Name** and the other details. Once generated, the API key is available under the **Identifier** column as shown below.

#### Instance

Braze manages a number of different instances for dashboard and REST Endpoints. Once your account is provisioned, it is logged in to one of the URLs mentioned below. Select the correct instance from the drop-down menu based on the mapping mentioned below.

| Instance | Dashboard URL | REST Endpoint |
| --- | --- | --- |
| US-01 | https://dashboard-01.braze.com | https://rest.iad-01.braze.com |
| US-02 | https://dashboard-02.braze.com | https://rest.iad-02.braze.com |
| US-03 | https://dashboard-03.braze.com | https://rest.iad-03.braze.com |
| US-04 | https://dashboard-04.braze.com | https://rest.iad-04.braze.com |
| US-05 | https://dashboard-05.braze.com | https://rest.iad-05.braze.com |
| US-06 | https://dashboard-06.braze.com | https://rest.iad-06.braze.com |
| US-08 | https://dashboard-08.braze.com | https://rest.iad-08.braze.com |
| EU-01 | https://dashboard-01.braze.eu | https://rest.fra-01.braze.eu |
| EU-02 | https://dashboard-02.braze.eu | https://rest.fra-02.braze.eu |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Destination Setup

After you have applied filters or added a condition for your users in Symphony, you can activate them in Braze under **Send to Destinations**. A new window opens, where you can set up your destination. You can use an already existing destination from the list of **Available Destinations** or create a new one.

### Add New Destination
Perform the following steps to add a new destination:
1. Click **Add New Destination**.
2. Search for **Braze**.
3. Add the **Client Name**, **API Key** and **Instance** (that you received above) and save the destination.

The destination is created and made available under **Available Destinations**.

### Add Workflow Level Inputs
After creating a destination, next, you have to add workflow-level inputs as mentioned below.
1. Choose the destination from the list of available destinations by using the search feature.
2. The **Client Name**, **API Key** and **Instance** fields are automatically populated based on the value that you had entered while creating the destination.
3. Enter the **Audience Name** that you want to create for this node of the workflow. This is sent as a **Custom Attribute** to Braze.
4. Under the **Data To Send** tab, complete the Catalogue to Destination mapping. You can find details on how to perform the mapping below.

### Data To Send Tab
The **Data To Send** tab allows the clients to map the Zeotap Catalogue fields to the Braze fields that can be sent to Braze. The mapping can be done in one of the following ways:
- **Static Mapping** - There are certain fields that Zeotap automatically maps to the relevant Braze fields like Email, Phone, First Name, Last Name and so on.
- **Drop-down Selection** - The clients can map the relevant fields ingested in Zeotap to the Braze fields provided in the drop-down menu.
- **Custom Data Input** - The clients can also add custom data that can be mapped to the relevant Zeotap field and sent to Braze.

## Supported Attributes
You can find details of all the Braze fields in this section.

| Braze Field | Mapping Type | Description |
| --- | --- | --- |
| External ID | Dropdown selection | This is the persistent `User Id` defined by you that Braze uses to track users across devices and platforms. We recommend that you map `User ID` to `External ID`, otherwise Zeotap may send email as user alias.<br><br>Zeotap recommends that you map `hashed email` available in the Zeotap Catalogue to the `External ID`.|
| Email | Static Mapping | This is mapped to `Email Raw` in the Zeotap Catalogue. |
| Phone | Static Mapping | This is mapped to `Mobile Raw` in the Zeotap Catalogue.<br><br>Braze accepts phone numbers in `E.164` format, Zeotap does not perform any transformation, hence, you are required to ingest the phone numbers in the prescribed format. For more information, check [here](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/). |
| First Name | Static Mapping | This is mapped to `First Name` in the Zeotap Catalogue. |
| Last Name | Static Mapping | This is mapped to `Last Name` in the Zeotap Catalogue. |
| Gender | Static Mapping | This is mapped to `Gender` in the Zeotap Catalogue. |
| Custom Event Name | Static Mapping | This is mapped to `Event Name` in the Zeotap Catalogue.<br><br>Both Custom Event Name and Custom Event Timestamp must be mapped to capture custom events in Braze. If either one is not mapped, then the custom event cannot be processed. For more information, refer [here](https://www.braze.com/docs/api/objects_filters/event_object#what-is-the-event-object). |
| Custom Event Timestamp | Static Mapping | This is mapped to `Event Timestamp` in the Zeotap Catalogue.<br><br>Both Custom Event Name and Custom Event Timestamp must be mapped to capture custom events in Braze. If either one is not mapped, then the custom event cannot be processed. For more information, refer [here](https://www.braze.com/docs/api/objects_filters/event_object#what-is-the-event-object). |
| Email Subscribe | Dropdown Selection | Onboard an `Email Marketing Preference` field and map to it.<br><br>Zeotap sends the following three values:<br>- `opted_in` - Indicates that the user has explicitly registered for email marketing preference<br>- `unsubscribed` - Indicates that the user has explicitly opted out of email messages<br>- `subscribed` - Indicates that the user has neither opted-in nor opted-out. |
| Push Subscribe | Dropdown Selection | Onboard a `Push Marketing Preference` field and map to it.<br><br>Zeotap sends the following three values:<br>- `opted_in` - Indicates that the user has explicitly registered for push marketing preference<br>- `unsubscribed` - Indicates that the user has explicitly opted out of push messages.<br>`subscribed` - Indicates that the user has neither opted-in nor opted-out |
| Email Open Tracking Enable | Dropdown Selection | Map the relevant `Marketing Preference` field.<br><br>When set to true, it enables open tracking pixel from being added to all future emails sent to this user. |
| Email Click Tracking Enable | Dropdown Selection | Map the relevant `Marketing Preference` field.<br><br>When set to true, it enables click tracking for all links within all future emails sent to this user. |
| Product ID | Dropdown selection | Identifier for a purchase action `(Product Name/Product Category)`. For more details, refer [here](https://www.braze.com/docs/api/objects_filters/purchase_object/).<br><br>Onboard the relevant attribute to the Zeotap Catalogue and map to it.<br><br>`Product ID`, `Currency` and `Price` must be mapped mandatorily to capture purchase events in Braze. If any of the three is missed, then purchase event cannot go through. For more information, refer [this](https://www.braze.com/docs/api/objects_filters/purchase_object/#purchase-object) . |
| Currency | Dropdown selection | Currency attribute for purchase action.<br><r>Supported format is `ISO 4217 Alphabetic Currency Code`.<br><br>Onboard correctly formatted Currency Data to the Zeotap Catalogue and map to it.<br><br>`Product ID`, `Currency` and `Price` must be mapped mandatorily to capture purchase events in Braze. If any of the three is missed, then purchase event cannot go through. |
| Price | Dropdown selection | Price attribute for purchase action.<br><br>Onboard the relevant attribute to the Zeotap Catalogue and map to it.<br><br>`Product ID`, `Currency` and `Price` must be mapped mandatorily to capture purchase events in Braze. If any of the three is missed, then purchase event cannot go through. |
| Quantity | Dropdown selection | Quantity attribute for purchase action.<br>Onboard the relevant attribute to the Zeotap Catalogue and map to it. |
| Country | Dropdown selection | Map to the `Country` Catalogue field you are onboarding. |
| City | Dropdown selection | Map to the `City` Catalogue field you are onboarding. |
| Language | Dropdown selection | The accepted format is `ISO-639-1` standard (e.g., en). Onboard correctly formatted language and map to it. |
| Date of Birth | Dropdown selection | Map to the `Date of Birth` field you are onboarding. |
| Custom Attribute | Custom Data Input | Map any user attribute to a custom data input and it is then sent to Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Viewing Data on Braze console

After you have mapped the relevant attributes to be sent and published the workflow, the events start flowing to Braze based on the criteria defined. You can search by Email ID/External ID on the Braze console. The user dashboard appears as shown below.

As shown in the screenshot, various attributes come under different sections of the user dashboard within Braze.
- The **Profile** tab contains the user attributes.
- The **Custom Attributes** tab contains the custom attributes defined by the user.
- The **Custom Events** tab contains the custom event defined by the user.
- The **Purchases** tab contains the purchases done over a period of time by the user.

## Campaign Creation
Users can create campaigns within Braze and activate users in real time or based on the scheduled time. Campaigns can be triggered based on the actions performed by the user(custom event, purchase) or user attributes. You can find details in the screenshot below.



