---
nav_title: Shopify
alias: /partners/shopify/
description: ""
page_type: partner
---

# Shopify

> [Shopify](https://www.shopify.com/) is a leading global commerce company, providing trusted tools to start, grow, market, and manage a retail business of any size. Shopify makes commerce better for everyone with a platform and services that are engineered for reliability while delivering a better shopping experience for consumers everywhere. 

Our Shopify integration will allow brands to seamlessly connect their Shopify store with Braze to pass select Shopify webhooks into Braze. Leverage Braze's cross-channel strategies and Canvas to retarget your users with abandoned checkout messaging to nudge customers to complete their purchase, or retarget users based on their previous purchases. 

# Pre-Requisites

| Requirement | Origin | Access | Description |
| ----------- | ------ | ------ | ----------- |
| Shopify store | Shopify | [https://www.shopify.com](https://www.shopify.com) | You will need to have an active Shopify store.<br><br>Please note that at this time, you will only be able to connect one Shopify store per app group. |
| Install Braze's Shopify App | Braze | Shopify integration page within Braze | You will need to begin setting up your integration with Shopify through Braze. We will walk you through a seamless onboarding process to install Braze's unlisted Shopify app.<br><br>For more details, check out our step-by-step guide below. |
| Event Property Segmentation enabled | Braze | Please reach out to your Customer Manager | To ensure you can segment your Shopify events properties, please work with your Customer Success Manager to either enable or confirm that you have event property segmentation enabled for your dashboard. |
| Nested Event Property support enabled | Braze | Please reach out to your Customer Success Manager | To ensure that you have nested event property support for your nested Shopify events, please work with your Customer Success Manager to either enable or confirm that you have this enhancement enabled for your dashboard. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

# Integration Overview

With Braze's turnkey Shopify integration, you will be able to:
- Seamlessly connect your Shopify store within Braze
- Allow Braze to ingest and process the following Shopify webhook event:
	- Order Create
	- Checkout Update
- Sync Shopify user profiles into Braze

## Enable the Shopify Integration

### Step 1: Locate Shopify within the Dashboard
From the Braze dashboard go to the Technology Partners section and then search __Shopify__. On the Shopify partner page, select __Begin Setup__ to start the integration process.

![Shopify][2]{: style="max-width:70%;"}

### Step 2: Shopify Setup
You will be prompted by Braze's setup guide. Within this flow, you will need to enter your __Shopify store name__, review the __Shopify webhook events__ we will begin ingestion once the integration is connected, and take you to Shopify's marketplace to download Braze's unlisted Shopify app. Once you select __Install Unlisted App__, you will be redirected back to the Braze dashboard.
#### Shopify Setup within Braze
![Shopify][3]{: style="max-width:80%;"}

#### Unlisted App within Shopify
![Shopify][7]{: style="max-width:60%;"}

### Step 3: Verify Completion
That's it! The status of your integration will appear in the Data Import section of the Shopify partner page. You will be notified via email once the Braze app has successfully installed and the webhook creation is complete. In addition, the __Connection Pending__ status will be updated to __Connected__ and will display the timestamp of when the connection started.

![Shopify][8]{: style="max-width:80%;"}
![Arrow][4]{: style="max-width:80%;border:0;margin-bottom:5px;"}
![Shopify][9]{: style="max-width:80%;"}
![Arrow][4]{: style="max-width:80%;border:0;margin-bottom:5px;"}
![Shopify][10]{: style="max-width:80%;"}

## Shopify Event Processing

Once the app installation is complete, Braze will automatically create your webhook integration with Shopify. See the table below for more details on how the supported Shopify webhook will map to Braze custom events and custom attributes.

### Shopify Webhook Event - Checkout Update

| Braze Event Mappings | Braze Event / Attribute Type | Event Properties / Array Items | 
| ------- | ------- | ------- |
| `shopify_abandoned_checkout` | Custom Event | - `abandoned_checkout_url`<br>- `checkout_id`<br>- `discount_codes`<br>- `line_items`<br>- `total_discounts`<br>- `total_price` |
| `shopify_checkout_product_ids` | Custom Attibute Array | Array of product IDs from the most recent `shopify_abandoned_checkout` event |
| `shopify_checkout_product_names` | Custom Attribute Array | Array of product names from the most recent `shopify_abandoned_checkout` event |
| `shopify_checkout_product_skus` | Custom Attribute Array | Array of product SKUs from the most recent `shopify_abandoned_checkout` event |
| `shopify_checkout_product_titles` | Custom Attribute Array | Array of product titles from the most recent `shopify_abandoned_checkout` event |
| `shopify_checkout_product_variants` | Custom Attribute Array | Array of product variants from the most recent `shopify_abandoned_checkout` event |
| `shopify_checkout_product_vendors` | Custom Atrribute Array | Array of product vendors from the most recent `shopify_abandoned_checkout` event |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

> __Checkout update events will Trigger after...__<br>- Adds/remove items from their cart<br>AND<br>- Proceeds further into the checkout process including adding their personal information.<br><br>Braze will listen to Shopify's checkout update webhooks and determine that a checkout is abandoned after __1 hour__ of checkout/cart inactivity. Nested event properties from the checkout update event will be logged as custom attributes for the Shopify beta to be used for segmentation.

### Shopify Webhook Event - Order Create

| Braze Event Mappings | Braze Event / Attribute Type | Event Properties / Array Items | Triggered when... |
| ------- | ------- | ------- | ------ |
| `shopify_order_created` | Custom Event | - `confirmed`<br>- `discount_codes`<br>- `line_items`<br>- `order_id`<br>- `order_number`<br>- `order_status_url`<br>- `total_discounts`<br>- `total_price` |Order create events will trigger: <br>- Automatically after customer has completed a purchase from your Shopify store.<br><br>OR<br><br>Manually through the Orders section of your Shopify account. |
| Purchase | Purchase Event | - `product id` (Shopify's product id)<br>- `quantity`<br>- `currency`<br>- `line price`<br>- `properties`<br>- `title`<br>- `variant title`<br>- `vendor`<br>- `name`<br>- `SKUs` | Shopify's order create event will also immediately trigger a Braze purchase event. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Shopify User Syncing

or the supported Shopify events, Braze will map the inbound events to Braze user profiles using the customer's email address. 

__Identified User Profiles__<br>
- If the email address is associated with an identified user profile, Braze will sync the Shopify data to that user
- If the email address is associated with multiple identified user profiles, Braze will sync the Shopify data to the one with the most recent activity 

__Alias Only Users__<br>
- If the email address is not associated with a user profile in Braze, Braze will generate an alias-only user with a Shopify alias object (see below). 
	- Note: If these alias-only users eventually become identified, Braze customers will need to assign an external ID to the alias-only profile by calling the Users Identify endpoint. 

### What Braze Syncs
Braze will sync the following attributes on the user profile only if there was a change.

| Braze Standard Attributes | Braze Custom Attributes | Alias Object |
| ------- | ------- | ------- |
| - Email<br>- First Name<br>- Last Name<br>- Phone<br>- City<br>- Country | - `shopify_accepts_marketing`<br>- `shopify_tags` | - alias_label: the user's Shopify customer ID<br>- alias_value: `SHOPIFY_CUSTOMER_ID_ALIAS` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Using Shopify Data in Braze

### Segmentation
If you are looking to segment by custom event properties, please ensure that you go to the __Manage App Group__ page and __Enable Filtering__ for all of the relevant event properties. Please note that for custom event property storage, you will only be able to segment on a custom event property for the past 30 days. For more details see [here](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage).

![Shopify][11]{: style="max-width:60%;"}

You should be able to filter Shopify's events with all of the [existing custom filters](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_events/) in Segmentation. 

![Shopify][12]{: style="max-width:60%;"}

In addition, you'll be able to use Braze's breadth of purchase filter to create segments of users based on:
- first/last purchase
- first/last purchase for a specific app
- products they have previously purchased within the last 30 days
- the number of purchase they made

![Shopify][13]{: style="max-width:60%;"}
![Shopify][14]{: style="max-width:60%;"}

### Personalization using Connected Content

You may have some use cases for personalization to template in additional information including product images. You can deepen the level of personalization with Shopify by using Braze's Connected Content feature. 

#### Step 1: Navigate to Apps
Go to your Shopify's admin page listed under Apps.
![Shopify][15]

#### Step 2: Enable Private App Development
If you haven't already, please ensure that you have enabled private app development on your store.
![Shopify][16]{: style="max-width:60%;"}
![Shopify][17]{: style="max-width:60%;"}

#### Step 3: Create a Private App
Create a private app in order to generate your Shopify access token.
![Shopify][18]{: style="max-width:70%;"}

#### Step 4: Enter Credentials
Once you have successfully created your private app, you will then be provided with your API credentials and keys. For your Connected Content calls, you will need to use the __Password__ value as the __X-Shopify-Access-Token__ in your requests 
![Shopify][19]{: style="max-width:70%;"}

## GDPR

With respect to Personal Data submitted to Braze Services by or on behalf of its customers, Braze is the Data Processor and our customers are the Data Controllers. Accordingly, Braze processes such Personal Data solely at the instruction of our customers, and, when applicable, notify our customers of Data Subject requests. Our customers, as the Data Controllers, respond directly to Data Subject requests. As part of the Braze platform's Shopify integration, Braze will automatically receive [Shopify's GDPR webhooks](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app). However, Braze customers will ultimately be responsible for responding to Data Subject requests from their Shopify customers through the use of [Braze SDKs](https://www.braze.com/docs/developer_guide/home/) or [REST APIs](https://www.braze.com/docs/api/endpoints/user_data/#user-track-endpoint) in accordance with our [GDPR compliance](https://www.braze.com/docs/help/gdpr_compliance/) policies.

[1]: {% image_buster /assets/img/Shopify/shopify_integration1.png %} 
[2]: {% image_buster /assets/img/Shopify/shopify_integration2.png %} 
[3]: {% image_buster /assets/img/Shopify/shopify_integration3-6.png %}
[4]: {% image_buster /assets/img/Shopify/arrow.jpeg %}
[7]: {% image_buster /assets/img/Shopify/shopify_integration7.png %} 
[8]: {% image_buster /assets/img/Shopify/shopify_integration8.png %} 
[9]: {% image_buster /assets/img/Shopify/shopify_integration9.png %} 
[10]: {% image_buster /assets/img/Shopify/shopify_integration10.png %} 
[11]: {% image_buster /assets/img/Shopify/shopify_segmentation1.png %} 
[12]: {% image_buster /assets/img/Shopify/shopify_segmentation2.png %} 
[13]: {% image_buster /assets/img/Shopify/shopify_segmentation3.png %} 
[14]: {% image_buster /assets/img/Shopify/shopify_segmentation4.png %} 
[15]: {% image_buster /assets/img/Shopify/shopify_connected_content1.png %} 
[16]: {% image_buster /assets/img/Shopify/shopify_connected_content2.png %} 
[17]: {% image_buster /assets/img/Shopify/shopify_connected_content3.png %} 
[18]: {% image_buster /assets/img/Shopify/shopify_connected_content4.png %} 
[19]: {% image_buster /assets/img/Shopify/shopify_connected_content5.png %} 
[20]: {% image_buster /assets/img/Shopify/shopify_troubleshooting1.png %} 
[21]: {% image_buster /assets/img/Shopify/shopify_troubleshooting2.png %} 


