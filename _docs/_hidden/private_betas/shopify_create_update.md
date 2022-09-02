---
nav_title: Shopify
permalink: /shopify_create_update/
hidden: true
---

# Shopify

> [Shopify](https://www.shopify.com/) is a leading global commerce company providing trusted tools to start, grow, market, and manage a retail business of any size. Shopify makes commerce better for everyone with a platform and services engineered for reliability while delivering a better shopping experience for consumers everywhere. 

The Shopify and Braze integration allow brands to connect their Shopify store seamlessly to pass select Shopify events and customers into Braze. Leverage Braze’s cross-channel strategies and Canvas to engage new leads, message new customers, or retarget your users with abandoned checkout messaging to nudge them to complete their purchase

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
| Nested custom attribute support | This will be enabled with the Spotify integration.<br><br>You will be given access to this feature to receive Shopify marketing opt-in custom attributes. |
| User permissions | You have to be either a:<br>• Store owner<br> • Staff<br>• Member with all **General** and **Online Store** settings, as well as these additional admin permissions selected:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Manage settings<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• View apps developed by staff and collaborators<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Manage and install apps and channels |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Integration

With Braze's turnkey Shopify integration, you can:
- Seamlessly connect your Shopify store within Braze
- Allow Braze to ingest and process Shopify user data
- Sync Shopify user profiles into Braze

### Step 1: Locate Shopify within the dashboard
In Braze, go to the **Technology Partners** section and then search **Shopify**. On the Shopify partner page, select **Begin Setup** to start the integration process.

![Data Import and Web SDK Installation section of the Shopify partner page in Braze.][2]{: style="max-width:80%;"}

### Step 2: Shopify setup
Next, you are prompted by Braze's setup wizard. Within this flow, you must enter your **Shopify Store Name**, review the **Shopify Webhook Events** (ingestion begins once the integration is connected), and visit the Shopify marketplace to download Braze's unlisted Shopify app. Once you select **Install Unlisted App**, you will be redirected to the Braze dashboard.

#### Shopify setup within Braze
<br>![Workflow of setting up Shopify within Braze by entering the store name and navigating to Shopify to install the Braze app.][3]{: style="max-width:80%;"}

#### Install Braze's Shopify application
<br>![Shopify app installation page, which lists the permissions the Braze app will have after installing.][7]{: style="max-width:60%;"}

### Step 3: Verify completion
That's it! The status of your integration appears in the **Data Import** section of the Shopify partner page. Once the Braze app has been successfully installed, and the webhook creation is complete, you will be notified via email. In addition, the **Connection Pending** status will be updated to **Connected** and will display the timestamp of when the connection was established.

![Data Import section showing connection pending and setup status pending.][8]{: style="max-width:80%;"}
![][4]{: style="max-width:80%;border:0;margin-bottom:5px;"}
![Data Import section showing connection pending and setup status successful.][9]{: style="max-width:80%;"}
![][4]{: style="max-width:80%;border:0;margin-bottom:5px;"}
![Data Import section showing successful connection. A timestamp displays when the connection was established, and there is a link to the connected storefront.][10]{: style="max-width:80%;"}

## Shopify data processing

Once the app installation is complete, Braze automatically creates your webhook integration with Shopify. See the following table for more details on how the supported Shopify webhook events map to Braze custom events and custom attributes.

### Supported Shopify events

{% tabs local %}
{% tab Shopify Events %}
| Event Name | Braze Event Type | Triggered When... |
| --- | --- | --- |
| `shopify_abandoned_checkout` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Shopify checkout updates a webhook's trigger when a customer adds or removes items from their cart AND proceeds further into the checkout process, including adding their personal information.<br><br>Braze will listen to the inbound Shopify checkout update webhooks and trigger the `shopify_abandoned_checkout` custom event when that checkout is considered abandoned. The abandonment default is set to **1 hour** but is configurable within the **Advanced Settings** section on the Shopify partner page. |
| `shopify_created_order` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Order create events trigger:<br><br>Automatically after a customer has completed a purchase from your Shopify store.<br>**OR**<br>Manually through the [orders](https://help.shopify.com/en/manual/orders/create-orders) section of your Shopify account.|
| Purchase | [Braze Purchase Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/) | Shopify's order create event also immediately triggers a Braze purchase event.<br><br>_Note: the Braze `product_id` field will include the Shopify Product ID._ |
| `shopify_paid_order` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Order paid events will trigger when an order’s payment status is changed to paid. An order is in paid status after a credit card payment has been captured, or when an order using a manually payment method is marked as paid. |
| `shopify_partially_fulfilled_order` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Partially fulfilled order events will trigger when some of the line items in an order are fulfilled successfully. |
| `shopify_fulfilled_order` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Fulfilled order events will trigger when the fulfillment of all of the line items in a fulfillment order is successful. |
| `shopify_cancelled_order` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Canceled order events will trigger when a customer creates an order but then cancels the order before fulfillment. |
| `shopify_created_refund` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Created refunds events are triggered when a customer is provided a refund, whether a partial refund or a complete refund, for their order. <br><br>In addition, a refund can also be triggered when a Shopify account admin manually processes the refund in Shopify. |
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
      "amount": 30,
      "title": "XYZPromotion",
      "description": "Promotionalitemforblackfriday."
    },
    "discount_code": "30_DOLLARS_OFF",
    "total_price": 398,
    "line_items": [
      {
        "product_id": 632910392,
        "quantity": 1,
        "sku": "IPOD2008PINK",
        "title": "IPodNano-8GB",
        "vendor": "Apple",
        "properties": "nil",
        "price": 199
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
    "total_discounts": 5,
    "total_price": 403,
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
        "price": 199.00
      },
      {
        "product_id": 632910392,
        "quantity": 1,
        "sku": "IPOD2008PINK",
        "title": "IPodNano-8GB",
        "vendor": "nil",
        "name": "IPodNano-8GB",
        "properties": [],
        "price": 199.00
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
        "price": 10
      },
      {
        "title": "Expedited",
        "price": 25
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
  "price": 199,
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
{% subtab Order Paid Event %}
```json
{
  "name": "shopify_paid_order",
  "time": "2022-05-23T13:52:38-04:00",
  "properties": {
    "order_id": 4444596371647,
    "line_items": [
      {
        "quantity": 1,
        "product_id": 6143033344191,
        "sku": null,
        "title": "LED High Tops",
        "vendor": "partners-demo",
        "name": "LED High Tops",
        "properties": [],
        "price": 80,
        "fulfillment_status": null
      }
    ],
    "shipping": [
      {
        "title": "Standard",
        "price": 0
      }
    ],
    "total_price": "141.54",
    "confirmed": true,
    "total_discounts": 0,
    "discount_codes": [],
    "order_number": 1092,
    "order_status_url": "https://test-store.myshopify.com/",
    "cancelled_at": null,
    "tags": "",
    "closed_at": null,
    "fulfillment_status": null,
    "fulfillments": []
  },
  "braze_id": "123abc123abc"
}
```
{% endsubtab %}
{% subtab Order Partially Fulfilled Event %}
```json
{
  "name": "shopify_partially_fulfilled_order",
  "time": "2022-05-23T14:43:34-04:00",
  "properties": {
    "order_id": 4444668657855,
    "line_items": [
      {
        "quantity": 1,
        "product_id": 6143032066239,
        "sku": null,
        "title": "Dark Denim Top",
        "vendor": "partners-demo",
        "name": "Dark Denim Top",
        "properties": [],
        "price": 60,
        "fulfillment_status": "fulfilled"
      }
    ],
    "shipping": [
      {
        "title": "Standard",
        "price": 0
      }
    ],
    "total_price": 130.66,
    "confirmed": true,
    "total_discounts": 0,
    "discount_codes": [],
    "order_number": 1093,
    "order_status_url": "https://test-store.myshopify.com/",
    "cancelled_at": null,
    "tags": "",
    "closed_at": null,
    "fulfillment_status": "partial",
    "fulfillments": [
      {
        "shipment_status": null,
        "status": "success",
        "tracking_company": "Other",
        "tracking_number": "123",
        "tracking_numbers": [
          "123"
        ],
        "tracking_url": "https://braze.com",
        "tracking_urls": [
          "https://braze.com"
        ],
        "line_items": [
          {
            "fulfillment_status": "fulfilled",
            "name": "Dark Denim Top",
            "price": 60,
            "product_id": 6143032066239,
            "properties": [],
            "quantity": 1,
            "requires_shipping": true,
            "sku": null,
            "title": "Dark Denim Top",
            "vendor": "partners-demo"
          }
        ]
      }
    ]
  },
  "braze_id": "abc123abc123"
}

```
{% endsubtab %}
{% subtab Order Fulfilled Event %}
```json
{
  "name": "shopify_fulfilled_order",
  "time": "2022-05-23T14:44:34-04:00",
  "properties": {
    "order_id": 4444668657855,
    "line_items": [
      {
        "quantity": 1,
        "product_id": 6143032066239,
        "sku": null,
        "title": "Dark Denim Top",
        "vendor": "partners-demo",
        "name": "Dark Denim Top",
        "properties": [],
        "price": 60,
        "fulfillment_status": "fulfilled"
      }
    ],
    "shipping": [
      {
        "title": "Standard",
        "price": 0
      }
    ],
    "total_price": 130.66,
    "confirmed": true,
    "total_discounts": 0,
    "discount_codes": [],
    "order_number": 1093,
    "order_status_url": "https://test-store.myshopify.com/",
    "cancelled_at": null,
    "tags": "",
    "closed_at": "2022-05-23T14:44:34-04:00",
    "fulfillment_status": "fulfilled",
    "fulfillments": [
      {
        "shipment_status": null,
        "status": "success",
        "tracking_company": "Other",
        "tracking_number": "456",
        "tracking_numbers": [
          "456"
        ],
        "tracking_url": "https://braze.com",
        "tracking_urls": [
          "https://braze.com"
        ],
        "line_items": [
          {
            "fulfillment_status": "fulfilled",
            "name": "Dark Denim Top",
            "price": 60,
            "product_id": 6143032066239,
            "quantity": 1,
            "requires_shipping": true,
            "sku": null,
            "title": "Dark Denim Top",
            "vendor": "partners-demo"
          }
        ]
      }
    ]
  },
  "braze_id": "123abc123abc"
}
```
{% endsubtab %}
{% subtab Order Cancelled Event %}
```json
{
  "name": "shopify_cancelled_order",
  "time": "2022-05-23T14:40:52-04:00",
  "properties": {
    "order_id": 4444596371647,
    "line_items": [
      {
        "quantity": 1,
        "product_id": 6143033344191,
        "sku": null,
        "title": "LED High Tops",
        "vendor": "partners-demo",
        "name": "LED High Tops",
        "properties": [],
        "price": 80,
        "fulfillment_status": null
      }
    ],
    "shipping": [
      {
        "title": "Standard",
        "price": 0
      }
    ],
    "total_price": 141.54,
    "confirmed": true,
    "total_discounts": 0,
    "discount_codes": [],
    "order_number": 1092,
    "order_status_url": "https://test-store.myshopify.com/",
    "cancelled_at": "2022-05-23T14:40:52-04:00",
    "tags": "",
    "closed_at": "2022-05-23T14:40:51-04:00",
    "fulfillment_status": null,
    "fulfillments": []
  },
  "braze_id": "123abc123abc"
}

```
{% endsubtab %}
{% subtab Refund Created Event %}
```json
{
  "name": "shopify_created_refund",
  "time": "2022-05-23T14:40:50-04:00",
  "properties": {
    "order_id": 4444596371647,
    "note": null,
    "line_items": [
      {
        "quantity": 1,
        "product_id": 6143033344191,
        "sku": null,
        "title": "LED High Tops",
        "vendor": "partners-demo",
        "properties": [],
        "price": 80
      },
      {
        "quantity": 1,
        "product_id": 6143032852671,
        "sku": null,
        "title": "Chequered Red Shirt",
        "vendor": "partners-demo",
        "properties": [],
        "price": 50
      }
    ]
  },
  "braze_id": "abc123abc123"
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

Braze will update existing user profiles or create new ones for leads, sign-ups, and account registrations being captured in your Shopify store. User profile data can be collected from the following methods in Shopify, but is not limited to:

- Customer creates an account
- Customer email or phone is collected in a Shopify pop-up form
- Customer email is collected on your store’s website footer
- Customer email or phone number is collected through a third-party tool connected to Shopify

Braze will first attempt to map the supported Shopify data to any existing user profiles using the customer’s email address or phone number.

**Identified User Profiles**<br>
- If the email address or phone number is associated with an [identified user profile]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles), Braze syncs the Shopify data to that user.
- If the email address or phone number is associated with multiple identified user profiles, Braze syncs the Shopify data to the one with the most recent activity.

**Anonymous Users**<br>
- If the email address or phone number is associated with an existing anonymous user profile or alias-only profile, we sync the Shopify data to that user. 
  - For existing alias-only profiles, we'll add the Shopify alias object for that user.
- If the email address or phone number is **not** associated with a user profile in Braze, Braze generates an alias-only user with a Shopify alias object. 
  - If these alias-only users eventually become identified, Braze customers must assign an external ID to the alias-only profile by calling the [Users Identify endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). 

If Braze does not find a match for the email address or phone number, we will then create a new user profile with the supported Shopify data.

{% alert important %}
Some of the user data and events collected by the Shopify integration will count towards your data point usage. Refer to our [data point policy](https://www.braze.com/docs/user_guide/onboarding_with_braze/data_points/) for more information.
{% endalert %}

## Using Shopify data in Braze
Once you've completed your integration, take a look at our next Shopify [article]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/use_cases/) to learn how to use Shopify data in Braze for personalization and segmentation in your campaigns and Canvases.

## Shopify advanced settings

### Update abandoned checkout delay

By default, Braze will automatically set the delay to trigger the `shopify_abandoned_checkout` event to one hour of inactivity. You can set the **Abandoned Checkout Delay** from 5 minutes up to 24 hours by selecting the dropdown and then selecting **Set Delay** on the Shopify partner page.

![Option in Advanced Settings to set a rule for how long after a user leaves their cart to trigger abandoned checkout.][11]{: style="max-width:40%;"}

### Set your preferred product identifier

If you have included Braze purchase events within your Shopify integration setup, by default Braze will set the Shopify Product ID as the `product_id` used within Braze’s purchase event. This will then be used when you filter for products purchased in Y days, or when personalizing content in your message using Liquid.

You can also choose to set either the SKU or Product Title from Shopify instead of the Shopify Product ID through advanced settings.

![Option in Advanced Settings to specify a field to use as your product identifier within the Braze purchase event.][12]{: style="max-width:40%;"}

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
Go to your Shopify admin page located under **Apps**. You will then see an option to delete the Braze application.<br><br>
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
[11]: {% image_buster /assets/img/Shopify/shopify_advanced_settings_abandoned_checkout_delay.png %} 
[12]: {% image_buster /assets/img/Shopify/shopify_advanced_settings_product_identifier.png %} 