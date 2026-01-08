---
nav_title: "Purchase object"
article_title: API Purchase Object
page_order: 8
page_type: reference
description: "This reference article explains the different components of a purchase object, how to use it correctly, and examples to draw from."

---

# Purchase object

> This article explains the different components of a purchase object, how to use it correctly, best practices, and examples to draw from.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

## What is a purchase object?

A purchase object is an object that gets passed through the API when a purchase has been made. Each purchase object is located within a purchase array, with each object being a single purchase by a particular user at a particular time. The purchase object has many different fields that allow the Braze backend to store and use this information for customization, data collection, and personalization.

### Object body

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required.
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  // See the following product_id naming conventions for clarification.
  "product_id" : (required, string) identifier for the purchase, for example, Product Name or Product Category,
  "currency" : (required, string) ISO 4217 Alphabetic Currency Code,
  //Revenue from a purchase object is calculated as the product of quantity and price.
  "price" : (required, float) value in the base currency unit (for example, Dollars for USD, Yen for JPY),
  "quantity" : (optional, integer) the quantity purchased (defaults to 1, must be <= 100 -- currently, Braze treats a quantity _X_ as _X_ separate purchases with quantity 1),
  "time" : (required, datetime as string in ISO 8601) Time of purchase,
  // See the following purchase object explanation for clarification.
  "properties" : (optional, Properties Object) properties of the event,
  // Setting this flag to true puts the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
}
```

- [External user ID]({{site.baseurl}}/api/basics/#user-ids)
- [App identifier]({{site.baseurl}}/api/identifier_types/)
- [ISO 4217 Currency Code Wiki](http://en.wikipedia.org/wiki/ISO_4217)
- [ISO 8601 Time Code Wiki](https://en.wikipedia.org/wiki/ISO_8601)

## Purchase product ID

Within the purchase object, the `product_id` is an identifier for the purchase (such as `Product Name` or `Product Category`):

- Braze allows you to store up to 5,000 `product_id`s in the dashboard.
- The `product_id` can be up to 255 characters.

### Naming conventions

At Braze, we offer some general naming conventions for the purchase object `product_id`. When choosing `product_id`, Braze suggests using simplistic names such as the product name or product category (instead of SKUs) with the intention of grouping all logged items by this `product_id`.

This helps make products easier to identify for segmentation and triggering.

### Log purchases at the order level

If you want to log purchases at the order level instead of the product level, you can use order name or order category as the `product_id` (such as `Online Order` or `Completed Order`).

For example, to log purchases at the order level in the Web SDK:

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99, },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99, }
        ]
      }
    }
  ]
}
```

## Purchase properties object

Custom events and purchases may have event properties. The "properties" values should be an object where the keys are the property names and the values are the property values. Property names must be non-empty strings less than or equal to 255 characters, with no leading dollar signs.

Property values can be any of the following data types:

| Data Type | Description |
| --- | --- |
| Numbers | As either [integers](https://en.wikipedia.org/wiki/Integer) or [floats](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booleans |  |
| Datetimes | Formatted as strings in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) or `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format. Not supported within arrays. |
| Strings | 255 characters or fewer. |
| Arrays | Arrays cannot include datetimes. |
| Objects | Objects are ingested as strings. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Event property objects that contain array or object values can have an event property payload of up to 50&nbsp;KB.

### Purchase properties

[Purchase properties]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties) can be used to trigger messages and for personalization using Liquid, also allowing you to segment based on these properties.

#### Naming conventions

It's important to note that this feature is turned on **per product**, not per purchase. For example, if a you have a high volume of distinct products, but each has the same properties, segmenting may be more unnecessary.

In this instance, we recommend using product names at a "group-level" instead of transaction-level identifiers when setting data structures. For example, a train ticket company should have products for "single trip", "return trip", "multi-city", and not specific transactions such as "transaction 123" or "transaction 046". As another example, with the purchase event "food", properties would be best set as "cake" and "sandwich".

{% alert important %}
Note that products can be added through the Braze REST API. For example, if you send a call to the `/users/track` endpoint and include a new purchase ID, Braze automatically creates a product in the **Data Settings** > **Products** section of the dashboard.
{% endalert %}

### Example purchase object

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "backpack",
      "currency" : "USD",
      "price" : 40.00,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "color" : "red",
        "monogram" : "ABC",
        "checkout_duration" : 180,
        "size" : "Large",
        "brand" : "Backpack Locker"
      }
    },
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pencil",
      "currency" : "USD",
      "price" : 2.00,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "number" : 2,
        "sharpened" : true
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pen",
      "currency" : "USD",
      "price" : 2.50,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "color" : "blue",
      }
    }
  ]
}
```

### Purchase objects, event objects, and webhooks

Using the example provided, we can see that someone bought a backpack with the properties: color, monogram, checkout duration, size, and brand. We can then create segments with these properties by using [purchase event properties]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties) or send custom messages through a channel using Liquid. For example, "Hello **Ann F.**, Thanks for purchasing that **red, medium backpack** for **$40.00**! Thanks for shopping at **Backpack Locker**!"

If you do want to save, store and track properties to segment with, you need to set them up as custom attributes. This can be done using [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), which allow you to target users based on custom event or purchase behavior stored for the lifetime of that user profile.


