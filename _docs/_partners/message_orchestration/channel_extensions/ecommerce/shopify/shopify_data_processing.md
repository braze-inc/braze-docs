---
nav_title: Data Processing
article_title: "Shopify Data Processing"
description: "This reference article outlines how Shopify data processing is deal with, including supported events, user syncing, advanced settings, and more."
page_type: partner
search_tag: Partner
alias: "/shopify_processing/"
page_order: 3
---

# Data processing

> Once the app installation is complete, Braze automatically creates your webhook and ScriptTag integration with Shopify. See the following table for more details on how the supported Shopify events map to Braze custom events and custom attributes.

## Supported Shopify events

{% tabs local %}
{% tab Shopify Events %}
| Event Name | Braze Event Type | Triggered When... | Event Source |
| --- | --- | --- | --- |
| `shopify_product_viewed` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)| Product views will trigger when products are fully visible on the Shopify store to the customer. | ScriptTag integration |
| `shopify_product_clicked` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Product clicks will trigger as soon as the customer clicks into the product information page. | ScriptTag integration |
| `shopify_abandoned_cart` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | As soon as a customer adds items to their cart, Braze will store the cart token ID. <br><br>The default Abandoned Cart Delay is set at 1 hour. Meaning, after 1 hour of cart abandonment where no updates have been made to the cart, Braze will then trigger the event. You can update your Abandoned Cart Delay within **Advanced Settings**. | ScriptTag integration |
| `shopify_abandoned_checkout` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Checkout updates webhook's trigger when a customer adds or removes items from their cart AND proceeds further into the checkout process including adding their personal information.<br><br>Braze will listen to the inbound Shopify checkout update webhooks and trigger the `shopify_abandoned_checkout` custom event when that checkout is considered abandoned. The Abandoned Checkout Delay is set to 1 hour but is configurable within the **Advanced Settings** section on the Shopify partner page. | Shopify webhooks |
| `shopify_created_order` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Order create events trigger:<br><br>Automatically after a customer has completed a purchase from your Shopify store.<br>**OR**<br>Manually through the [orders](https://help.shopify.com/en/manual/orders/create-orders) section of your Shopify account.| Shopify webhooks |
| Purchase | [Braze Purchase Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/) | An order create event is received from Shopify and the products ordered are mapped to Braze Purchase Events. | Shopify webhooks |
| `shopify_paid_order` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Order paid events will trigger when an order's payment status is changed to paid. An order is in paid status after a credit card payment has been captured or when an order using a manual payment method is marked as paid. | Shopify webhooks |
| `shopify_partially_fulfilled_order` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Partially fulfilled order events will trigger when some of the line items in an order are fulfilled successfully. | Shopify webhooks |
| `shopify_fulfilled_order` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Fulfilled order events will trigger when the fulfillment of all of the line items in a fulfillment order is successful. | Shopify webhooks |
| `shopify_cancelled_order` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Canceled order events will trigger when a customer creates an order but then cancels the order before fulfillment. | Shopify webhooks |
| `shopify_created_refund` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Created refunds events are triggered when a customer is provided a refund for their order, whether a partial refund or a complete refund.<br><br> A refund can also be triggered when a Shopify account admin manually processes the refund in Shopify. | Shopify webhooks |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% endtab %}
{% tab Example Payload %}
{% subtabs local %}
{% subtab Viewed Product %}
```json
{
  "name": "shopify_product_viewed",
  "properties": {
      "id": 5971657097407,
      "title": "Example T-Shirt",
      "price": 1999,
      "vendor": "Acme",
      "images": [
          "//cdn.shopify.com/s/files/1/0503/3849/6703/products/green-t-shirt.jpg?v=1603397913"
      ]
  }
}
```
{% endsubtab %}
{% subtab Clicked Product %}
```json
{
    "name": "shopify_product_clicked",
    "properties": {
        "id": 5971657097407,
        "title": "Example T-Shirt",
        "price": 1999,
        "vendor": "Acme",
        "images": [
            "//cdn.shopify.com/s/files/1/0503/3849/6703/products/green-t-shirt.jpg?v=1603397913"
        ]
    }
}
```
{% endsubtab %}
{% subtab Abandoned Cart %}
```json
{
    "name": "shopify_abandoned_cart",
    "time": "2022-10-14T15:08:31.571Z",
    "properties": {
      "cart_id": "163989958f6b0de13f3b4f702fa5ee0d",
      "line_items": [
        {
          "price": 60,
          "product_id": 7110622675033,
          "properties": null,
          "quantity": 1,
          "sku": null,
          "title": "Spinach Surprise Smoothie - 12 Pack",
          "variant_id": 40094740545625,
          "vendor": "Jennifer's Juice"
        }
      ]
    },
    "braze_id": "63497b3ca3eabd0053380451"
  }

```
{% endsubtab %}
{% subtab Checkout Abandoned %}
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
    "price": "199.00",
    "properties": {},        
    "product_id": 632910392,
        "quantity": 1,
        "sku": "IPOD2008PINK",
        "title": "IPodNano-8GB",
        "variant_id": 40094740545625,
        "variant_title": "Pink iPod Nano 8 GB",
        "vendor": "Apple",
      }
    ],
    "abandoned_checkout_url": "https://checkout.local/690933842/checkouts/123123123/recover?key=example-secret-token",
    "checkout_id": "123123123"
  }
}
```
{% endsubtab %}
{% subtab Order Created %}
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
        "variant_id": 40094740545625,
        "variant_title": "Pink iPod Nano 8 GB",
        "vendor": null,
        "name": "IPodNano-8GB",
        "properties": [],
        "price": "199.00"
      },
      {
        "product_id": 632910393,
        "quantity": 1,
        "sku": "IPOD2008SILVER",
        "title": "IPodNano-8GB",
        "variant_id": 40094740545626,
        "variant_title": "Silver iPod Nano 8 GB",
        "vendor": null,
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
{% subtab Purchase %}
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
    "variant_id": 40094740545626,
    "variant_title": "Silver iPod Nano 8 GB",
    "vendor": null,
    "properties": []
  }
}
```
{% endsubtab %}
{% subtab Order Paid %}
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
        "variant_id": 40094740549876,
        "variant_title": null,
        "vendor": "partners-demo",
        "name": "LED High Tops",
        "properties": [],
        "price": "80.00",
        "fulfillment_status": null
      }
    ],
  }
}
```
{% endsubtab %}
{% subtab Order Partially Fulfilled %}
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
        "variant_id": 40094740549876,
        "variant_title": "",
        "vendor": "partners-demo",
        "name": "Dark Denim Top",
        "properties": [],
        "price": "60.00",
        "fulfillment_status": "fulfilled"
      }
    ],
    "shipping": [
      {
        "title": "Standard",
        "price": "0.00"
      }
    ],
    "total_price": "130.66",
    "confirmed": true,
    "total_discounts": "0.00",
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
            "price": "60.00",
            "product_id": 6143032066239,
            "properties": [],
            "quantity": 1,
            "requires_shipping": true,
            "sku": null,
            "title": "Dark Denim Top",
            "variant_id": 40094740549876,
            "variant_title": "",
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
{% subtab Order Fulfilled %}
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
   "variant_id": 40094740549876,
        "variant_title": "Small Dark Denim Top",

        "vendor": "partners-demo",
        "name": "Dark Denim Top",
        "properties": [],
        "price": "60.00",
        "fulfillment_status": "fulfilled"
      }
    ],
    "shipping": [
      {
        "title": "Standard",
        "price": "0.00"
      }
    ],
    "total_price": "130.66",
    "confirmed": true,
    "total_discounts": "0.00",
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
            "price": "60.00",
            "product_id": 6143032066239,
            "quantity": 1,
            "requires_shipping": true,
            "sku": null,
            "title": "Dark Denim Top",
            "variant_id": 40094740549876,
            "variant_title": "Small Dark Denim Top",
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
{% subtab Order Cancelled %}
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
        "variant_id": 40094740549876,
        "variant_title": "",
        "vendor": "partners-demo",
        "name": "LED High Tops",
        "properties": [],
        "price": "80.00",
        "fulfillment_status": null
      }
    ],
    "shipping": [
      {
        "title": "Standard",
        "price": "0.00"
      }
    ],
    "total_price": "141.54",
    "confirmed": true,
    "total_discounts": "0.00",
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
{% subtab Refund Created %}
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
        "variant_id": 40094740549876,
        "variant_title": "",
        "vendor": "partners-demo",
        "properties": [],
        "price": "80.00"
      },
      {
        "quantity": 1,
        "product_id": 6143032852671,
        "sku": null,
        "title": "Chequered Red Shirt",
        "variant_id": 40094796619876,
        "variant_title": "",
        "vendor": "partners-demo",
        "properties": [],
        "price": "50.00"
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
| `shopify_tags`  | This attribute corresponds to the [customer tags](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types) set by Shopify admins. |
| `shopify_total_spent` | This attribute tracks the total amount spent on a store and is only supported for users imported through the [Historical Backfill]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_backfill/) feature. |
| `shopify_order_count` | This attribute tracks the total number of orders made in a store and is only supported for users imported through the Historical Backfill feature. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Example Payload %}
{% subtabs local %}
{% subtab Shopify Tags %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "shopify_tags": "VIP_customer",
      "shopify_total_spent": "60.00",
      "shopify_order_count": "3"
    }
  ]
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Supported Shopify standard attributes

- Email
- First Name
- Last Name
- Phone
- City
- Country

{% alert note %}
Braze will only update supported Shopify custom attributes and Braze standard attributes if there is a difference in data from the existing user profile. For example, if the inbound Shopify data contains a first name of Bob and Bob already exists as a first name on the Braze user profile, Braze will not trigger an update, and you will not be charged a data point.
{% endalert %}

## Shopify advanced settings

#### Update abandoned cart and abandoned checkout delay

By default, Braze will automatically set the delay to trigger the `shopify_abandoned_checkout` and `shopify_abandoned_cart` events to one hour of inactivity. You can set the Abandoned Delay for each event from 5 minutes up to 24 hours by selecting the dropdown and then selecting Set Delay on the Shopify partner page.

![Option in Advanced Settings to set abandoned cart and checkout delay.][10]{: style="max-width:40%;"}

#### Set your preferred product identifier

If you have included Braze purchase events within your Shopify integration setup, by default, Braze will set the Shopify Product ID as the `product_id` used within Braze's purchase event. This will be used when you filter for products purchased in Y days or personalize content in your message using Liquid.

You can also choose to set either the SKU or Product Title from Shopify instead of the Shopify Product ID through advanced settings.

![Option in Advanced Settings to specify a field to use as your product identifier within the Braze purchase event.][12]{: style="max-width:40%;"}

## Shopify user syncing

Braze will update existing user profiles or create new ones for leads, sign-ups, and account registrations captured in your Shopify store. User profile data can be collected from the following methods in Shopify but is not limited to:

- Customer creates an account
- Customer email or phone is collected in a Shopify pop-up form
- Customer email is collected on your store from Shopify's footer
- Customer email or phone number is collected through a third-party tool connected to Shopify

Braze will first attempt to map the supported Shopify data to any existing user profiles using the customer's email address or phone number.

**Anonymous users**<br>
- If the email address or phone number is associated with an existing anonymous user profile or alias-only profile, we sync the Shopify data to that user. 
  - For existing alias-only profiles, we'll add the Shopify alias object for that user.
- If the email address or phone number is **not** associated with a user profile in Braze, Braze generates an alias-only user with a Shopify alias object. 
  - If these alias-only users eventually become identified, Braze customers must assign an external ID to the alias-only profile by calling the [`/users/identify` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). 

**Identified users**<br>
- As the customers proceed into the checkout process, Braze will check to see if the inputted email address, phone number, or their Shopify Customer ID matches an [identified user profile]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles). If there is a match, Braze will sync the Shopify user data to that profile. 
- If the email address or phone number is associated with multiple identified user profiles, Braze syncs the Shopify data to the one with the most recent activity.  

If Braze does not find a match for the email address or phone number, we will create a new user profile with the supported Shopify data.

{% alert important %}
Some of the user data and events collected by the Shopify integration will count towards your data point usage. Refer to our [data point policy]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/) for more information.
{% endalert %}

### The Web SDK and Shopify webhooks

<br>**Anonymous users**
1. With the Web SDK integration, you will begin tracking sessions for your Shopify customers. If your store visitors are guests (i.e., anonymous), Braze will capture the `device_id` for that particular customer's session.
2. As the customer progresses to checkout and provides additional identifiable information like email or phone number, Braze will capture the relevant Shopify user data via Shopify webhooks.
3. In this process, Braze will effectively match the user by the same `device_id` for the same session and merge all of the user data captured from both the Web SDK and Shopify webhooks into a single user profile in Braze.<br>Braze will also assign the Shopify customer ID as the [user alias]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases) on the user profile:

```json
{
  "user_aliases" :
    { 
      "alias_name" : "4306250531001", 
      "alias_label" : "shopify_customer_id" },
 { 
      "alias_name" : example@email.com 
      "alias_label" : "shopify_email" },
 { 
      "alias_name" : "1234567890", 
      "alias_label" : "shopify_phone" }
}
```

**Identified users**<br>
- As the customers proceed into the checkout process, Braze will check to see if the inputted email address, phone number, or their Shopify Customer ID matches an [identified user profile]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles). If there is a match, Braze will sync the Shopify user data to that profile using our [merge functionality](#user-profile-merging). 
- If the email address or phone number is associated with multiple identified user profiles, Braze syncs the Shopify data to the one with the most recent activity.  

## User reconciliation outside of checkout flow

The Shopify integration reconciles your user’s device ID and personal information when they reach the checkout flow and perform any Shopify webhook events here. Outside of the checkout flow, to support user reconciliation via your Shopify sign-up and login flow, you can execute the following Javascript function within your `theme.liquid` file:

```
reconcileEmail(<email address>);
```

This will cause the anonymous user on the web to be associated with the given email address, which you will supply. For example, if the user enters their email address into a sign-up or login field, you should ensure this is being passed. Once this function is called, any other Shopify events referencing the given email address will be assigned to the same Braze user.

{% alert note %}
Braze has a no-code solution to implement this function automatically on your Shopify store. If you’re interested in this beta feature, contact your customer success manager or account manager.
{% endalert %}

### User profile merging

Braze will merge the following fields on the anonymous user created from our Shopify integration to the identified user when we find a match on one of these identifiers, Shopify customer ID, email, or phone number. Note this user data merging functionality is only available in the Shopify integration.
- First name
- Last name
- Email
- Gender
- Date of birth
- Phone number
- Time zone
- Home city
- Country
- Language
- Custom attributes
- Custom event and purchase event data (excluding event properties, count, and first date and last date timestamps)
- Custom event and purchase event properties for "X times in Y days" segmentation (where X<=50 and Y<=30)
- Push tokens
- Message history

Any of the following fields found on the anonymous user to the identified user:
- Custom event and purchase event count and first date and last date timestamps
  - These merged fields will update "for X events in Y days" filters. For purchase events, these filters include "number of purchases in Y days" and "money spent in last Y days".

{% alert warning%}
Session data is not yet supported as part of our merging process.
{% endalert %}

## GDPR

Concerning personal data submitted to Braze services by or on behalf of its customers, Braze is the data processor, and our customers are the data controllers. Accordingly, Braze processes such personal data solely at the instruction of our customers and, when applicable, notifies our customers of data subject requests. As the data controllers, our customers respond directly to Data subject requests. As part of the Braze platform's Shopify integration, Braze automatically receives [Shopify's GDPR webhooks](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app). However, Braze customers are ultimately responsible for responding to data subject requests from their Shopify customers through the use of [Braze SDKs]({{site.baseurl}}/developer_guide/home/) or [REST APIs]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) in accordance with our [GDPR compliance]({{site.baseurl}}/help/dp-technical-assistance/) policies.



[10]: {% image_buster /assets/img/Shopify/checkout_cart_delay.png %}
[12]: {% image_buster /assets/img/Shopify/shopify_advanced_settings_product_identifier.png %} 
