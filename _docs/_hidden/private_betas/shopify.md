---
nav_title: Shopify
permalink: /partners/shopify/
description: ""
page_type: partner
hidden: true
---

# Shopify

> [Shopify](https://www.shopify.com/) is a leading global commerce company, providing trusted tools to start, grow, market, and manage a retail business of any size. Shopify makes commerce better for everyone with a platform and services that are engineered for reliability while delivering a better shopping experience for consumers everywhere. 

Our Shopify integration allows brands to seamlessly connect their Shopify store with Braze to pass select Shopify webhooks into Braze. Leverage Braze's cross-channel strategies and Canvas to retarget your users with abandoned checkout messaging to nudge customers to complete their purchase, or retarget users based on their previous purchases. 

## Prerequisites

| Requirement | Origin | Access | Description |
| ----------- | ------ | ------ | ----------- |
| Braze's Supplemental Terms for Shopify | Braze | Braze | Braze requires all customers that are looking to use the Shopify integration to sign supplemental terms for this integration. You will receive the supplemental terms for the Shopify integration from Customer Success Manager. |
| Shopify Store | Shopify | [https://www.shopify.com](https://www.shopify.com) | You must have an active Shopify store.<br><br>Please note that at this time, you are only able to connect __one__ Shopify store per app group. |
| Install Braze's Shopify App | Braze | Shopify integration page within Braze | You must set up your integration through our seamless onboarding process within Braze to install Braze's unlisted Shopify app.<br><br>For more details, check out our step-by-step guide below. |
| Segment Extension Beta Enabled | Braze | Please reach out to your Customer Success Manager | To ensure that you have the ability to create segments for custom events and custom event properties for up to 365 days, please work with your Customer Success Manager to either enable or confirm that you have this beta enabled for your dashboard. |
| Event Property Segmentation Enabled | Braze | Please reach out to your Customer Success Manager | To ensure you can segment your Shopify events properties, please work with your Customer Success Manager to confirm that you have event property segmentation enabled for your dashboard. |
| Nested Event Property Support Enabled | Braze | Please reach out to your Customer Success Manager | To ensure that you have nested event property support for your nested Shopify events, please work with your Customer Success Manager to either enable or confirm that you have this enhancement enabled for your dashboard. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Integration Overview

With Braze's turnkey Shopify integration, you are able to:
- Seamlessly connect your Shopify store within Braze
- Allow Braze to ingest and process the following Shopify webhook events:
	- Order Create
	- Checkout Update
- Sync Shopify user profiles into Braze

### Step 1: Locate Shopify within the Dashboard
From the Braze dashboard go to the Technology Partners section and then search __Shopify__. On the Shopify partner page, select __Begin Setup__ to start the integration process.

![Shopify][2]{: style="max-width:70%;"}

### Step 2: Shopify Setup
Next, you are prompted by Braze's setup wizard. Within this flow, you must enter your __Shopify store name__, review the __Shopify webhook events__ (ingestion begins once the integration is connected), and visit the Shopify marketplace to download Braze's unlisted Shopify app. Once you select __Install Unlisted App__, you will be redirected back to the Braze dashboard.
#### Shopify Setup within Braze
![Shopify][3]{: style="max-width:80%;"}

#### Unlisted App within Shopify
![Shopify][7]{: style="max-width:60%;"}

### Step 3: Verify Completion
That's it! The status of your integration appears in the Data Import section of the Shopify partner page. You will be notified via email once the Braze app has successfully installed and the webhook creation is complete. In addition, the __Connection Pending__ status will be updated to __Connected__ and will display the timestamp of when the connection was established.

![Shopify][8]{: style="max-width:80%;"}
![Arrow][4]{: style="max-width:80%;border:0;margin-bottom:5px;"}
![Shopify][9]{: style="max-width:80%;"}
![Arrow][4]{: style="max-width:80%;border:0;margin-bottom:5px;"}
![Shopify][10]{: style="max-width:80%;"}

## Shopify Event Processing

Once the app installation is complete, Braze automatically creates your webhook integration with Shopify. See the table below for more details on how the supported Shopify webhook events map to Braze custom events and custom attributes.

#### Shopify Webhook Event - Checkout Update

| Braze Event Mappings | Braze Event / Attribute Type | Event Properties / Array Items | 
| ------- | ------- | ------- |
| `shopify_abandoned_checkout` | Custom Event | - `abandoned_checkout_url`<br>- `checkout_id`<br>- `discount_codes`<br>- `line_items`<br>- `total_discounts`<br>- `total_price` |
| `shopify_checkout_product_ids` | Custom Attribute Array | Array of product IDs from the most recent `shopify_abandoned_checkout` event |
| `shopify_checkout_product_names` | Custom Attribute Array | Array of product names from the most recent `shopify_abandoned_checkout` event |
| `shopify_checkout_product_skus` | Custom Attribute Array | Array of product SKUs from the most recent `shopify_abandoned_checkout` event |
| `shopify_checkout_product_titles` | Custom Attribute Array | Array of product titles from the most recent `shopify_abandoned_checkout` event |
| `shopify_checkout_product_variants` | Custom Attribute Array | Array of product variants from the most recent `shopify_abandoned_checkout` event |
| `shopify_checkout_product_vendors` | Custom Atrribute Array | Array of product vendors from the most recent `shopify_abandoned_checkout` event |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

> __Checkout update events Trigger after a user...__<br>- Adds/remove items from their cart<br>AND<br>- Proceeds further into the checkout process including adding their personal information.<br><br>Braze listens to Shopify's checkout update webhooks and determines that a checkout is abandoned after __1 hour__ of checkout/cart inactivity. Nested event properties from the checkout update event are logged as custom attributes for the Shopify beta to be used for segmentation.

#### Shopify Webhook Event - Order Create

| Braze Event Mappings | Braze Event / Attribute Type | Event Properties / Array Items | Triggered when... |
| ------- | ------- | ------- | ------ |
| `shopify_order_created` | Custom Event | - `confirmed`<br>- `discount_codes`<br>- `line_items`<br>- `order_id`<br>- `order_number`<br>- `order_status_url`<br>- `total_discounts`<br>- `total_price` |Order create events trigger: <br><br> Automatically after customer has completed a purchase from your Shopify store.<br><br>OR<br><br>Manually through the [Orders](https://help.shopify.com/en/manual/orders/create-orders) section of your Shopify account. |
| `purchase` | Purchase Event | - `product id`<br>- `quantity`<br>- `currency`<br>- `line price`<br>- `properties`<br>--- `title`<br>--- `variant title`<br>--- `vendor`<br> --- `name`<br>--- `SKUs` | Shopify's order create event also immediately triggers a Braze purchase event. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Shopify User Syncing

For the supported Shopify events, Braze maps the inbound events to Braze user profiles using the customer's email address or phone number. 

__Identified User Profiles__<br>
- If the email address or phone number is associated with an [identified user profile]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles), Braze syncs the Shopify data to that user
- If the email address or phone number is associated with multiple identified user profiles, Braze syncs the Shopify data to the one with the most recent activity 

__Anonymous Users__<br>
- If the email address or phone number is associated with an existing anonymous user profile or alias-only profile, we sync the Shopify data to that user. 
	- Note: for existing alias-only profiles, we'll add the Shopify alias object for that user (see below).
- If the email address or phone number is __not__ associated with a user profile in Braze, Braze generates an alias-only user with a Shopify alias object. 
	- Note: If these alias-only users eventually become identified, Braze customers must assign an external ID to the alias-only profile by calling the [Users Identify endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). 

#### What Braze Syncs
Braze syncs the following attributes on the user profile only if there was a change.

| Braze Standard Attributes | Braze Custom Attributes | Alias Object |
| ------- | ------- | ------- |
| - Email<br>- First Name<br>- Last Name<br>- Phone<br>- City<br>- Country | - `shopify_accepts_marketing`<br>- `shopify_tags` | - `alias_label`: `(shopify_customer_id)`<br>- `alias_value`: `shopify_customer_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Using Shopify Data in Braze

### Segmentation

You can filter Shopify's events with all of the [existing custom filters]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) in Segmentation. 

![Shopify][12]{: style="max-width:60%;"}

In addition, you can also use Braze's breadth of purchase filter to create segments of users based on:
- First/last purchase
- First/last purchase for a specific app
- Products they have previously purchased within the last 30 days
- The number of purchase they made

![Shopify][13]{: style="max-width:80%;"}

![Shopify][14]{: style="max-width:80%;"}

_Note: If you are looking to segment by custom event properties, please ensure that you work with your Customer Success Manager to enable filtering for all relevant event properties that you'd like to use within segmentation and Liquid._ 

For the Shopify Abandoned Checkout event, you are also able to segment and Liquid template the items within your most recent abandoned cart for the following custom attributes: 
- `product IDs`
- `skus` 
- `name`
- `title`
- `variant`
- `vendor`

### Campaign and Canvas Triggering 

With Shopify custom events in Braze, you can trigger Canvases or campaigns like you normally would with any other [custom event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage). Here is an example below of a Canvas that triggers off of the Shopify Abandoned Checkout event within the Canvas entry criteria. 

![Shopify][5]

### Personalization using Liquid

If you have the Nested Event Property support enabled by your Customer Success Manager, you can Liquid template the event properties and nested event properties for the supported Shopify custom events. <br>Here is an example of Liquid templating the __product title__ from the Shopify Abandoned Checkout event:
{% raw %}
`{{event_properties.${line_items[0].title}}}`
{% endraw %}

## Troubleshooting

#### Why is my Shopify app install still pending? 
- Your install may still be pending for one of the following reasons: 
	- When Braze is setting up your Shopify webhooks
	- When Braze is communicating with Shopify
- If your app installation is pending for 1 hour, Braze will fail the installation and you will be prompted to Retry Setup.<br>
![Shopify][24]{: style="max-width:60%;"}

#### Why did my Shopify app install fail?
- Your install may have failed for one of the following reasons: 
	- Braze could not reach Shopify
	- Braze failed to process the request 
	- Your Shopify access token is invalid 
	- The Braze Shopify app was deleted from your Shopify admin page
- If this happens, you will be able to select __Retry Setup__ and start the installation process again.<br>
![Shopify][25]{: style="max-width:60%;"}

#### How do I uninstall the Braze application from my Shopify store? 
- You will need to go to your Shopify admin page located under __Apps__. You will then see an option to delete the Braze application<br>
![Shopify][6]{: style="max-width:50%;"}

## GDPR

With respect to Personal Data submitted to Braze Services by or on behalf of its customers, Braze is the Data Processor and our customers are the Data Controllers. Accordingly, Braze processes such Personal Data solely at the instruction of our customers, and, when applicable, notify our customers of Data Subject requests. Our customers, as the Data Controllers, respond directly to Data Subject requests. As part of the Braze platform's Shopify integration, Braze automatically receives [Shopify's GDPR webhooks](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app). However, Braze customers are ultimately responsible for responding to Data Subject requests from their Shopify customers through the use of [Braze SDKs]({{site.baseurl}}/developer_guide/home/) or [REST APIs]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) in accordance with our [GDPR compliance]({{site.baseurl}}/help/dp-technical-assistance/) policies.

[2]: {% image_buster /assets/img/Shopify/shopify_integration2.png %} 
[3]: {% image_buster /assets/img/Shopify/shopify_integration3-6.png %}
[4]: {% image_buster /assets/img/Shopify/arrow.jpeg %}
[5]: {% image_buster /assets/img/Shopify/shopify_integration11.png %} 
[6]: {% image_buster /assets/img/Shopify/shopify_integration12.png %} 
[7]: {% image_buster /assets/img/Shopify/shopify_integration7.png %} 
[8]: {% image_buster /assets/img/Shopify/shopify_integration8.png %} 
[9]: {% image_buster /assets/img/Shopify/shopify_integration9.png %} 
[10]: {% image_buster /assets/img/Shopify/shopify_integration10.png %} 
[12]: {% image_buster /assets/img/Shopify/shopify_segmentation2.png %} 
[13]: {% image_buster /assets/img/Shopify/shopify_segmentation3.png %} 
[14]: {% image_buster /assets/img/Shopify/shopify_segmentation4.png %} 
[24]: {% image_buster /assets/img/Shopify/shopify_integration15.png %} 
[25]: {% image_buster /assets/img/Shopify/shopify_integration16.png %} 


