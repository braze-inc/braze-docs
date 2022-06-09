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
| `shopify_product_viewed` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)| Product views will trigger when products are fully visible on the Shopify store to the customer.<br><br>The products that are viewed need to have an associated link that goes to the product page or other instance of the store. |
| `shopify_product_clicked` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Product clicks will trigger as soon as the customer clicks on the product information page. |
| `shopify_abandoned_checkout` | [Custom Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) | Shopify checkout updates a webhook's trigger when a customer adds or removes items from their cart AND proceeds further into the checkout process, including adding their personal information.<br><br>Braze will listen to the inbound Shopify checkout update webhooks and trigger the `shopify_abandoned_checkout` custom event when that checkout is considered abandoned. The Abandoned Checkout Delay is set to **1 hour** but is configurable within the **Advanced Settings** section on the Shopify partner page. |
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
{% subtab Viewed Product Event %}
{% endsubtab %}
{% subtab Clicked Product Event %}
{% endsubtab %}
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
Braze will only update supported Shopify custom attributes and Braze standard attributes if there is a difference in data from the existing user profile. For example, if the inbound Shopify data contains a first name of Bob and Bob already exists as a first name on the Braze user profile, Braze will not trigger an update, and the customer will not be charged a data point.
{% endalert %}

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

[22]: {% image_buster /assets/img/Shopify/shopify_integration11.png %}  
[22]: {% image_buster /assets/img/Shopify/shopify_segmentation2.png %} 
[23]: {% image_buster /assets/img/Shopify/shopify_segmentation3.png %} 
[14]: {% image_buster /assets/img/Shopify/shopify_segmentation4.png %}   
[26]: {% image_buster /assets/img/Shopify/shopify_integration17.png %}
