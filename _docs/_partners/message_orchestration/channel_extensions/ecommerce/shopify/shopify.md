---
nav_title: Shopify
article_title: "Shopify"
description: "This article outlines the partnership with Braze and Shopify, a global commerce company that allows you to seamlessly connect their Shopify store with Braze to pass select Shopify webhooks into Braze. Leverage Braze's cross-channel strategies and Canvas to nudge customers to complete their purchases, or retarget users based on their previous purchases."
page_type: partner
search_tag: Partner

---

# Shopify

> [Shopify](https://www.shopify.com/) is a leading global commerce company providing trusted tools to start, grow, market, and manage a retail business of any size. Shopify makes commerce better for everyone with a platform and services engineered for reliability while delivering a better shopping experience for consumers everywhere. 

The Shopify and Braze integration allow brands to connect their Shopify store seamlessly to pass select Shopify webhooks into Braze. Leverage Braze's cross-channel strategies and Canvas to retarget your users with abandoned checkout messaging to nudge customers to complete their purchase or retarget users based on their previous purchases. 

<!--
For some Canvas and Campaign examples, check out our guide here. 
-->

## Prerequisites

All Braze customers looking to utilize the Shopify integration must sign Braze's Shopify order form. Reach out to your account executive for more details.

This integration will create alias user profiles if we are unable to match Shopify data using the email or phone number ([see here for more details on Shopify user reconciliation](#shopify-user-syncing)). Consult with your development teams around the downstream impacts and need to merge these user profiles as part of your user lifecycle before you enable the integration. 

| Requirement | Description |
| ----------- | ----------- |
| Shopify store | You must have an active [Shopify](https://www.shopify.com) store.<br><br>Note that at this time, you are only able to connect one Shopify store per app group. |
| Event property segmentation enabled | To ensure you can segment your Shopify events properties, you must work with your customer success manager or [Braze support]({{site.baseurl}}/braze_support/) to confirm that you have event property segmentation enabled for your dashboard. |
| Nested custom event property support in segment extensions | This will be enabled with the Shopify integration.<br><br>You will be given access to this feature to filter Shopify nested custom event properties for up to 365 days within Segment Extensions. |
| Nested custom event property support for message triggering | This will be enabled with the Shopify integration.<br><br>You will be given access to this feature to trigger campaigns and Canvases using the nested properties within Shopify customer events. |
| Nested custom attribute support | This will be enabled with the Spotify integration.<br><br>You will be given access to this feature to receive Shopify marketing opt-in custom attributes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Integration

With Braze's turnkey Shopify integration, you can:
- Seamlessly connect your Shopify store within Braze
- Allow Braze to ingest and process the following Shopify webhook events:
  - Order create
  - Checkout update
- Sync Shopify user profiles into Braze

### Step 1: Locate Shopify within the dashboard
In Braze, go to the **Technology Partners** section and then search **Shopify**. On the Shopify partner page, select **Begin Setup** to start the integration process.

![Shopify][2]{: style="max-width:80%;"}

### Step 2: Shopify setup
Next, you are prompted by Braze's setup wizard. Within this flow, you must enter your **Shopify Store Name**, review the **Shopify Webhook Events** (ingestion begins once the integration is connected), and visit the Shopify marketplace to download Braze's unlisted Shopify app. Once you select **Install Unlisted App**, you will be redirected to the Braze dashboard.

#### Shopify setup within Braze
<br>![Shopify][3]{: style="max-width:80%;"}

#### Install Braze's Shopify application
<br>![Shopify][7]{: style="max-width:60%;"}

### Step 3: Verify completion
That's it! The status of your integration appears in the **Data Import** section of the Shopify partner page. Once the Braze app has been successfully installed, and the webhook creation is complete, you will be notified via email. In addition, the **Connection Pending** status will be updated to **Connected** and will display the timestamp of when the connection was established.

![Shopify][8]{: style="max-width:80%;"}
![Arrow][4]{: style="max-width:80%;border:0;margin-bottom:5px;"}
![Shopify][9]{: style="max-width:80%;"}
![Arrow][4]{: style="max-width:80%;border:0;margin-bottom:5px;"}
![Shopify][10]{: style="max-width:80%;"}

## Shopify event processing

Once the app installation is complete, Braze automatically creates your webhook integration with Shopify. See the following table for more details on how the supported Shopify webhook events map to Braze custom events and custom attributes.

### Supported Shopify events

{% tabs local %}
{% tab Shopify Events %}
| Event Name | Braze Event Type | Triggered When... |
| --- | --- | --- |
| `shopify_abandoned_checkout` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Shopify checkout updates webhook's trigger when a customer adds or removes items from their cart AND proceeds further into the checkout process including adding their personal information.<br><br>Braze will listen to the inbound Shopify checkout update webhooks and trigger the `shopify_abandoned_checkout` custom event when that checkout is considered abandoned after **1 hour** of checkout or cart activity. |
| `shopify_created_order` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Order create events trigger:<br><br>Automatically after a customer has completed a purchase from your Shopify store.<br>**OR**<br>Manually through the [orders](https://help.shopify.com/en/manual/orders/create-orders) section of your Shopify account.|
| Purchase | [Braze Purchase Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/) | Shopify's order create event also immediately triggers a Braze purchase event.<br><br>_Note: the Braze `product_id` field will include the Shopify product id._ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Example Payload %}
{% subtabs local %}
{% subtab Checkout Abandoned Event %}
```json
{
  "name": "shopify_abandoned_checkout",
  "time": "2020-09-10T18:53:37-04:00",
  "properties": {
    "applied_discount": {
      "amount": "30.00",
      "title": "XYZPromotion",
      "description": "Promotionalitemforblackfriday."
    },
    "discount_code": "30_DOLLARS_OFF",
    "total_price": "398.00",
    "line_items": [
      {
        "product_id": 632910392,
        "quantity": 1,
        "sku": "IPOD2008PINK",
        "title": "IPodNano-8GB",
        "vendor": "Apple",
        "properties": "nil",
        "price": "199.00"
      }
    ],
    "abandoned_checkout_url": "https://checkout.local/690933842/checkouts/123123123/recover?key=example-secret-token",
    "checkout_id": "123123123"
  }
}

```
{% endsubtab %}
{% subtab Order Created Event %}
```json
{
  "name": "shopify_created_order",
  "time": "2020-09-10T18:53:45-04:00",
  "properties": {
    "total_discounts": "5.00",
    "total_price": "403.00",
    "discount_codes": [],
    "line_items": [
      {
        "product_id": 632910392,
        "quantity": 1,
        "sku": "IPOD2008PINK",
        "title": "IPodNano-8GB",
        "vendor": "nil",
        "name": "IPodNano-8GB",
        "properties": [],
        "price": "199.00"
      },
      {
        "product_id": 632910392,
        "quantity": 1,
        "sku": "IPOD2008PINK",
        "title": "IPodNano-8GB",
        "vendor": "nil",
        "name": "IPodNano-8GB",
        "properties": [],
        "price": "199.00"
      }
    ],
    "order_id": 820982911946154500,
    "confirmed": false,
    "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
    "order_number": 1234,
    "cancelled_at": "2020-09-10T18:53:45-04:00",
    "shipping": [
      {
        "title": "Standard",
        "price": "10.00"
      },
      {
        "title": "Expedited",
        "price": "25.00"
      }
    ],
    "tags": "heavy"
  }
}
```
{% endsubtab %}
{% subtab Purchase Event %}
```json
{
  "product_id": 632910392,
  "currency": "USD",
  "price": "199.00",
  "time": "2020-09-10T18:53:45-04:00",
  "quantity": 1,
  "source": "shopify",
  "properties": {
    "name": "IPodNano-8GB",
    "sku": "IPOD2008PINK",
    "title": "IPodNano-8GB",
    "variant_title": "nil",
    "vendor": "nil",
    "properties": []
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Supported Shopify custom attributes
{% tabs local %}
{% tab Shopify Custom Attributes %}
| Attribute Name | Description |
| --- | --- |
| `shopify_accepts_marketing` | This custom attribute corresponds to the email marketing opt-in status that is captured on the checkout page. |
| `shopify_sms_consent` | This custom attribute corresponds to the SMS marketing opt-in status that is captured on the checkout page. |
| `shopify_tags`  | This attribute corresponds to the [customer tags](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types) set by Shopify admins. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Example Payload %}
{% subtabs local %}
{% subtab Shopify SMS Consent %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "shopify_sms_consent": {
        "state": "subscribed",
        "opt_in_level": "single_opt_in",
        "collected_from": "other"
      }
    }
  ]
}
```
{% endsubtab %}
{% subtab Shopify Accepts Marketing (Email) %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "shopify_accepts_marketing": true
    }
  ]
}
```
{% endsubtab %}
{% subtab Shopify Tags %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "shopify_tags": "VIP_customer"
    }
  ]
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Supported Shopify standard attributes

- Email
- First Name
- Last Name
- Phone
- City
- Country

{% alert note %}
Braze will only update supported Shopify custom attributes, and Braze standard attributes if there is a difference in data from the existing user profile. For example, if the inbound Shopify data contains a first name of Bob and Bob already exists as a first name on the Braze user profile, Braze will not trigger an update, and the customer will not be charged a data point.
{% endalert %}

## Shopify user syncing

Braze will map the supported Shopify data to user profiles using the customer's email address or phone number. 

**Identified User Profiles**<br>
- If the email address or phone number is associated with an [identified user profile]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles), Braze syncs the Shopify data to that user.
- If the email address or phone number is associated with multiple identified user profiles, Braze syncs the Shopify data to the one with the most recent activity.

**Anonymous Users**<br>
- If the email address or phone number is associated with an existing anonymous user profile or alias-only profile, we sync the Shopify data to that user. 
  - For existing alias-only profiles, we'll add the Shopify alias object for that user.
- If the email address or phone number is **not** associated with a user profile in Braze, Braze generates an alias-only user with a Shopify alias object. 
  - If these alias-only users eventually become identified, Braze customers must assign an external ID to the alias-only profile by calling the [Users Identify endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). 

## Using Shopify data in Braze
Once you've completed your integration, take a look at our next Shopify [article]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/use_cases/) to learn how to use Shopify data in Braze for personalization and segmentation in your campaigns and Canvases.

## Troubleshooting

{% details Why is my Shopify app install still pending? %}
Your install may still be pending for one of the following reasons: 
  - When Braze is setting up your Shopify webhooks
  - When Braze is communicating with Shopify

If your app installation is pending for 1 hour, Braze will fail the installation and you will be prompted to Retry Setup.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration8.png %}){: style="max-width:80%;"}
{% enddetails %}

{% details Why did my Shopify app install fail? %}
Your install may have failed for one of the following reasons: 
  - Braze could not reach Shopify
  - Braze failed to process the request 
  - Your Shopify access token is invalid 
  - The Braze Shopify app was deleted from your Shopify admin page

If this happens, you will be able to select **Retry Setup** and start the installation process again.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration16.png %}){: style="max-width:80%;"}
{% enddetails %}

{% details How do I uninstall the Braze application from my Shopify store? %}
You will need to go to your Shopify admin page located under **Apps**. You will then see an option to delete the Braze application<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration12.png %}){: style="max-width:80%;"}
{% enddetails %}

## GDPR

Concerning personal data submitted to Braze services by or on behalf of its customers, Braze is the data processor, and our customers are the data controllers. Accordingly, Braze processes such personal data solely at the instruction of our customers and, when applicable, notifies our customers of data subject requests. As the data controllers, our customers respond directly to Data subject requests. As part of the Braze platform's Shopify integration, Braze automatically receives [Shopify's GDPR webhooks](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app). However, Braze customers are ultimately responsible for responding to data subject requests from their Shopify customers through the use of [Braze SDKs]({{site.baseurl}}/developer_guide/home/) or [REST APIs]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) in accordance with our [GDPR compliance]({{site.baseurl}}/help/dp-technical-assistance/) policies.

[2]: {% image_buster /assets/img/Shopify/shopify_integration2.png %} 
[3]: {% image_buster /assets/img/Shopify/shopify_integration3-6.gif %}
[4]: {% image_buster /assets/img/Shopify/arrow.jpeg %}
[7]: {% image_buster /assets/img/Shopify/shopify_integration7.png %} 
[8]: {% image_buster /assets/img/Shopify/shopify_integration8.png %} 
[9]: {% image_buster /assets/img/Shopify/shopify_integration9.png %} 
[10]: {% image_buster /assets/img/Shopify/shopify_integration10.png %} 
