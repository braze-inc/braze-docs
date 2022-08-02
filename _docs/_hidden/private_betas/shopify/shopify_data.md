---
nav_title: Shopify Data in Braze
article_title: "Shopify Data in Braze"
description: "This article outlines how to use Shopify data in Braze for personalization and segmentation."
page_type: partner
search_tag: Partner
permalink: "/shopify_data/"
hidden: true

---

# Shopify data in Braze

## Shopify webhooks

Braze offers a turnkey solution to support abandoned checkout, purchase, and post-purchase lifecycle campaigns through [Shopify webhooks](https://shopify.dev/api/admin-rest/2022-04/resources/webhook#top). Depending on which events you select during your onboarding process, Braze determines which Shopify event topics to subscribe to. As soon as you have successfully onboarded your Shopify store, Braze will instantly receive your Shopify customer activity.

### Supported Shopify events

{% tabs local %}
{% tab Shopify Events %}
| Event Name | Braze Event Type | Triggered When... |
| --- | --- | --- |
| `shopify_product_viewed` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)| Product views will trigger when products are fully visible on the Shopify store to the customer. |
| `shopify_product_clicked` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Product clicks will trigger as soon as the customer clicks into the product information page. |
| `shopify_abandoned_cart` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | As soon as a customer adds items to their cart, Braze will store the cart token ID. <br><br>The default Abandoned Cart Delay is set at 1 hour. Meaning, after 1 hour of cart abandonment where no updates have been made to the cart, Braze will then trigger the event. You can update your Abandoned Cart Delay within **Advanced Settings**. | 
| `shopify_abandoned_checkout` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Checkout updates webhook’s trigger when a customer adds or removes items from their cart AND proceeds further into the checkout process including adding their personal information.<br><br>Braze will listen to the inbound Shopify checkout update webhooks and trigger the `shopify_abandoned_checkout` custom event when that checkout is considered abandoned. The Abandoned Checkout Delay is set to 1 hour but is configurable within the **Advanced Settings** section on the Shopify partner page. |
| `shopify_created_order` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Order create events trigger:<br><br>Automatically after a customer has completed a purchase from your Shopify store.<br>**OR**<br>Manually through the [orders](https://help.shopify.com/en/manual/orders/create-orders) section of your Shopify account.|
| Purchase | [Braze Purchase Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/) | Shopify's order create event immediately triggers a Braze purchase event. |
| `shopify_paid_order` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Order paid events will trigger when an order's payment status is changed to paid. An order is in paid status after a credit card payment has been captured or when an order using a manual payment method is marked as paid. |
| `shopify_partially_fulfilled_order` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Partially fulfilled order events will trigger when some of the line items in an order are fulfilled successfully. |
| `shopify_fulfilled_order` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Fulfilled order events will trigger when the fulfillment of all of the line items in a fulfillment order is successful. |
| `shopify_cancelled_order` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Canceled order events will trigger when a customer creates an order but then cancels the order before fulfillment. |
| `shopify_created_refund` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Created refunds events are triggered when a customer is provided a refund for their order, whether a partial refund or a complete refund.<br><br> A refund can also be triggered when a Shopify account admin manually processes the refund in Shopify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

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
    "name" => "shopify_abandoned_cart",
    "time" => "2021-10-01T21:12:15.773Z",
    "properties" => {
      "cart_id"=>"eeafa272cebfd4b22385bc4b645e762c",
      "line_items" => [
        {
          "product_id" => 788032119674292922,
          "quantity" => 3,
          "sku" => "example-shirt-s",
          "title" => "Example T-Shirt - ",
          "vendor" => "Acme",
          "properties" => {},
          "price" => "19.99",
        },
      ],
    }
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
    "title": "IPodNano-8GB",
    "variant_title": "nil",
    "vendor": "nil",
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
        "vendor": "partners-demo",
        "properties": [],
        "price": "80.00"
      },
      {
        "quantity": 1,
        "product_id": 6143032852671,
        "sku": null,
        "title": "Chequered Red Shirt",
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
| `shopify_accepts_marketing` | This custom attribute corresponds to the email marketing opt-in status that is captured on the checkout page. |
| `shopify_sms_consent` | This custom attribute corresponds to the SMS marketing opt-in status that is captured on the checkout page. |
| `shopify_tags`  | This attribute corresponds to the [customer tags](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types) set by Shopify admins. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Example Payload %}
{% subtabs local %}
{% subtab SMS Consent %}
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
{% subtab Accepts Marketing (Email) %}
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
{% subtab Tags %}
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
Braze will only update supported Shopify custom attributes and Braze standard attributes if there is a difference in data from the existing user profile. For example, if the inbound Shopify data contains a first name of Bob and Bob already exists as a first name on the Braze user profile, Braze will not trigger an update, and the customer will not be charged a data point.
{% endalert %}

## User reconciliation

#### The Web SDK and Shopify webhooks

##### Anonymous users
1. With the Web SDK integration, you will begin tracking sessions for your Shopify customers. If your store visitors are guests (i.e., anonymous), Braze will capture the `device_id` for that particular customer's session.<br><br>
2. As the customer progresses through to checkout and provides additional identifiable information like email or phone number, Braze will capture the relevant Shopify user data via Shopify webhooks.<br><br>
3. In this process, Braze will effectively match the user by the same `device_id` for the same session and merge all of the user data captured from both the Web SDK and Shopify webhooks into a single user profile in Braze.<br><br>Braze will also assign the Shopify customer ID as the [user alias]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases) on the user profile:

```json
{
  "user_alias" :
    { 
      "alias_name" : "4306250531001", 
      "alias_label" : "shopify_customer_id" }
}
```

##### Identified users

- As the customers proceed into the checkout process, Braze will check to see if the inputted email address, phone number, or their Shopify Customer ID matches an [identified user profile]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles). If there is a match, Braze will sync the Shopify user data to that profile. 
- If the email address or phone number is associated with multiple identified user profiles, Braze syncs the Shopify data to the one with the most recent activity.

#### Shopify webhooks only
Braze will map the supported Shopify data to user profiles using the customer's email address or phone number. 

##### Identified user profiles

- If the email address or phone number is associated with an [identified user profile]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles) Braze syncs the Shopify data to that user.
- If the email address or phone number is associated with multiple identified user profiles, Braze syncs the Shopify data to the one with the most recent activity.

##### Anonymous users

- If the email address or phone number is associated with an existing anonymous user profile or alias-only profile, we sync the Shopify data to that user.
  - For existing alias-only profiles, we'll add the Shopify alias object for that user. 
- If the email address or phone number is not associated with a user profile in Braze, Braze generates an alias-only user with a Shopify alias object.
  - If these alias-only user eventually become identified, Braze customers must assign an external ID to the alias-only profile by calling the [users identify endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). 

## Personalization

Using nested object support for custom events, Braze Shopify customers can use Liquid template variables of the nested event properties. The following tables list the Liquid templating variables for each event.

{% tabs %}
{% tab Product Viewed %}
**Event**: `shopify_product_viewed`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Item SKU | `{{event_properties.${id}}}` |
| Item Title  | `{{event_properties.${title}}}` |
| Item Price | `{{event_properties.${price}}}` |
| Item Vendor | `{{event_properties.${vendor}}}` |
| Item Images | `{{event_properties.${images}}}` |

{% endraw %}
{% endtab %}

{% tab Product Clicked %}
**Event**: `shopify_product_clicked`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Item SKU | `{{event_properties.${id}}}` |
| Item Title  | `{{event_properties.${title}}}` |
| Item Price | `{{event_properties.${price}}}` |
| Item Vendor | `{{event_properties.${vendor}}}` |
| Item Images | `{{event_properties.${images}}}` |
{% endraw %}
{% endtab %}

{% tab Abandon Cart %}
**Event**: `shopify_abandoned_cart`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
{% endraw %}
{% endtab %}

{% tab Abandon Checkout %}
**Event**: `shopify_abandoned_checkout`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Checkout ID | `{{event_properties.${checkout_id}}}` |
| Abandoned Card URL | `{{event_properties.${abandoned_checkout_url}}}` |
| Discount Code | `{{event_properties.${discount_code}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Discount Amount | `{{event_properties.${applied_discount}[0].amount}}` |
| Discount Title | `{{event_properties.${applied_discount}[0].title}}` |
| Discount Description | `{{event_properties.${applied_discount}[0].description}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
{% endraw %}

{% endtab %}
{% tab Created Order %}

**Event**: `shopify_created_order`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Discount Codes | `{{event_properties.${discount_codes}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
{% endraw %}

{% endtab %}
{% tab Purchase %}

**Event**: Purchase<br>
**Type**: [Braze Purchase Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title  | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
{% endraw %}

{% endtab %}
{% tab Order Paid %}
**Event**: `shopify_paid_order`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Discount Codes | `{{event_properties.${discount_codes}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
{% endraw %}
{% endtab %}

{% tab Partially Fulfilled Order %}
**Event**: `shopify_partially_fulfilled_order`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Closed Timestamp | `{{event_properties.${closed_at}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillment Shipment Status | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].status}}` |
| Fulfillment Tracking Company | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| Fulfillment Tracking Number | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| Fulfillment Tracking Numbers | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| Fulfillment Tracking URL | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| Fulfillment Tracking URLs | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Fulfillment Name | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Fulfillment Price | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Fulfillment Product ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Fulfillment Quantity | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Fulfillment Shipping | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Fulfillment SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Fulfillment Title | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fulfillment Vendor | `{{event_properties.${fulfillments}[0].line_items[0].vendor` | 
{% endraw %}
{% endtab %}

{% tab Fulfilled Order %}
**Event**: `shopify_fulfilled_order`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Closed Timestamp | `{{event_properties.${closed_at}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillment Shipment Status | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Status | `{{event_properties.${fulfillments}[0].status}}` |
| Fulfillment Tracking Company | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| Fulfillment Tracking Number | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| Fulfillment Tracking Numbers | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| Fulfillment Tracking URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| Fulfillment Tracking URLs | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Fulfillment Name | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Fulfillment Price | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Fulfillment Product ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Fulfillment Quantity | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Fulfillment Shipping | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Fulfillment SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Fulfillment Title | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fulfillment Vendor | `{{event_properties.${fulfillments}[0].line_items[0].vendor` | 
{% endraw %}
{% endtab %}

{% tab Cancelled Order %}
**Event**: `shopify_cancelled_order`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Discount Codes | `{{event_properties.${discount_codes}}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillments | `{{event_properties.${fulfillments}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Fulfillment Status | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
{% endraw %}
{% endtab %}


{% tab Created Refund %}
**Event**: `shopify_created_refund`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Order Note | `{event_properties.${note}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
{% endraw %}
{% endtab %}
{% endtabs %}

## Segmentation

You can filter Shopify's events with all of the [existing custom filters]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) in Segmentation. 

![Segment Details page for a Shopify_Test segment with the filter for the custom event "shopify_checkouts_abandon" highlighted.][22]{: style="max-width:80%;"}

In addition, you can also use Braze's breadth of purchase filter to create segments of users based on:
- First/last purchase
- First/last purchase for a specific app
- Products they have previously purchased within the last 30 days
- The number of purchases they made

![Segmentation filter for users that first made a purchase after October 17, 2020.][23]

![Searching for a specific product ID as a segmentation filter.][24]

{% alert note %}
If you are looking to segment by custom event properties, ensure that you work with your customer success manager or Braze [support]({{site.baseurl}}/braze_support/) to enable filtering for all relevant event properties that you'd like to use within segmentation and Liquid.
{% endalert %} 

## Campaign and Canvas triggering 

With Shopify custom events in Braze, you can trigger Canvases or campaigns like you normally would with any other [custom event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage). For example, you may create an Action-Based Canvas that triggers off of the Shopify `shopify_checkouts_abandon` event within the Canvas entry criteria. 

![Action-based Canvas that enters users who perform the custom event "shopify_checkouts_abandon".][22]

With Nested Object Support for Custom Event Properties, customers can now trigger campaigns and Canvases using a nested event property. The following is an example of triggering a campaign using a specific product from the `shopify_created_order` custom event.

![Action-based campaign that sends to users who perform the custom event "shopify_created_order" where the nested property "product_id" equals a specific number.][26]

## Shopify advanced settings

#### Update abandoned cart delay
By default, Braze will automatically set the delay to trigger the `shopify_abandoned_cart` event to one hour of inactivity. You can set the **Abandoned Cart Delay** from 5 minutes to 24 hours by selecting the dropdown and then selecting **Set Delay** on the Shopify partner page.

![Option in Advanced Settings to set a rule for how long after a user leaves their cart to trigger abandoned cart.][13]{: style="max-width:40%;"}

#### Update abandoned checkout delay

By default, Braze will automatically set the delay to trigger the `shopify_abandoned_checkout` event to one hour of inactivity. You can set the **Abandoned Checkout Delay** from 5 minutes up to 24 hours by selecting the dropdown and then selecting **Set Delay** on the Shopify partner page.

![Option in Advanced Settings to set a rule for how long after a user leaves their cart to trigger abandoned checkout.][11]{: style="max-width:40%;"}

#### Set your preferred product identifier

If you have included Braze purchase events within your Shopify integration setup, by default, Braze will set the Shopify Product ID as the Product ID used within Braze's purchase event. This will then be used when you filter for products purchased in Y days or personalize content in your message using Liquid.

You can also choose to set either the SKU or Product Title from Shopify instead of the Shopify Product ID through advanced settings.

![Option in Advanced Settings to specify a field to use as your product identifier within the Braze purchase event.][12]{: style="max-width:40%;"}

## GDPR

Concerning personal data submitted to Braze services by or on behalf of its customers, Braze is the data processor, and our customers are the data controllers. Accordingly, Braze processes such personal data solely at the instruction of our customers and, when applicable, notifies our customers of data subject requests. As the data controllers, our customers respond directly to Data subject requests. As part of the Braze platform's Shopify integration, Braze automatically receives [Shopify's GDPR webhooks](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app). However, Braze customers are ultimately responsible for responding to data subject requests from their Shopify customers through the use of [Braze SDKs]({{site.baseurl}}/developer_guide/home/) or [REST APIs]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) in accordance with our [GDPR compliance]({{site.baseurl}}/help/dp-technical-assistance/) policies.

[11]: {% image_buster /assets/img/Shopify/shopify_advanced_settings_abandoned_checkout_delay.png %} 
[12]: {% image_buster /assets/img/Shopify/shopify_advanced_settings_product_identifier.png %} 
[13]: {% image_buster /assets/img/Shopify/abandoned_cart_delay.png %} 


[22]: {% image_buster /assets/img/Shopify/shopify_integration11.png %}  
[22]: {% image_buster /assets/img/Shopify/shopify_segmentation2.png %} 
[23]: {% image_buster /assets/img/Shopify/shopify_segmentation3.png %} 
[24]: {% image_buster /assets/img/Shopify/shopify_segmentation4.png %}   
[26]: {% image_buster /assets/img/Shopify/shopify_integration17.png %}
