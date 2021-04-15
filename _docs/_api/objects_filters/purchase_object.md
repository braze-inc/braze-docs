---
nav_title: "Purchase Object"
page_order: 8

page_type: reference

platform:
  - API
tool:
  - Campaigns
  - Canvas
  - Dashboard

description: "This article explains the different components of a purchase object, how to use it correctly, and examples to draw from."
---

# Purchase Object Specification

> This article explains the different components of a purchase object, how to use it correctly, best practices, and examples to draw from.

## What is a Purchase Object?

A Purchase Object is an object that gets passed through the API when a purchase has been made. Each Purchase Object is located within a purchase array, with each object being a single purchase by a particular user at a particular time. The purchase object has many different fields that allow Braze's backend to store and use this information for customization, data collection, and personalization.

### Purchase Object

```json
{
  // One of "external_id" or "user_alias" or "braze_id" is required.
  "external_id" : (optional, string) External User ID,
  "user_alias" : (optional, User Alias Object), User Alias,
  "braze_id" : (optional, string) Braze User Identifier,
  "app_id" : (optional, string) see App Identifier below,
  // Please see product_id naming conventions below for clarification.
  "product_id" : (required, string), identifier for the purchase, e.g. Product Name or Product Category,
  "currency" : (required, string) ISO 4217 Alphabetic Currency Code,
  //Revenue from a purchase object is calculated as the product of quantity and price.
  "price" : (required, float) value in the base currency unit (e.g. Dollars for USD, Yen for JPY),
  "quantity" : (optional, integer) the quantity purchased (defaults to 1, must be <= 100 -- currently, Braze treats a quantity _X_ as _X_ separate purchases with quantity 1),
  "time" : (required, datetime as string in ISO 8601), Time of purchase,
  // Properties stored here are only valid for 30 days.
  // Please see purchase object explanation below for clarification.
  "properties" : (optional, Properties Object) properties of the event,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
}
```
- [ISO 4217 Currency Code Wiki][20]

## Purchase Product_ID

Within the purchase object, The `product_id` is an identifier for the purchase, e.g Product Name or Product Category
- Braze allows you to store a max of 5000 `product_id`s in the dashboard.
- `product_id` max is 255 characters

### Product_ID Naming Conventions
At Braze, we offer some general naming conventions for the purchase object `product_id`.
When choosing `product_id`, Braze suggests using simplistic names such as the product name or product category with the intention of grouping all logged items by this `product_id`.

## Purchase Properties Object
Custom events and purchases may have event properties. The “properties” values should be an object where the keys are the property names and the values are the property values. Property names must be non-empty strings less than or equal to 255 characters, with no leading dollar signs. Property values can be integers, floats, booleans, datetimes (as strings in ISO8601 or yyyy-MM-dd'T'HH:mm:ss:SSSZ format), or strings less than or equal to 255 characters.

### Purchase Properties
Purchase properties __do not__ persist and aren't saved on a user's profile. These properties can, however, be used to trigger messages and for personalization using Liquid, also allowing you to segment (up to 30 days) based on these properties. Braze allows you to "save" these properties for 30 days by turning on this feature flipper to keep these properties alive and useable for message personalization. To turn on this feature in your own app group, contact your customer service manager.

While uncommon, if you require these properties to persist past the 30-day limit, contact your Customer Success Manager, or, see our webhooks suggestion below to see how you can incorporate webhooks to save these properties as custom attributes.

### Purchase Property Naming Conventions

It is important to note that this feature is enabled __per product__, not per purchase. For example, if a customer has a high volume of distinct products, but each has the same properties, segmenting becomes rather meaningless, 

In this instance, this is why when setting the data structures, we recommend using product names at a "group-level" instead of something granular. For example, a train ticket company should have products for "single trip", "return trip", "multi-city", and not specific transactions such as "transaction 123", "transaction 046", etc. Or for example, with the purchase event 'food', properties would be best set as "cake" and "sandwich".

### Example Purchase Object
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

## Purchase Objects, Event Objects, and Webhooks

Using the example provided above, we can see that someone bought a backpack with the properties: color, monogram, checkout duration, size, and brand. While we cannot go into a campaign and segment the users based on these properties, we can use these properties strategically by using them in the form of a receipt, to send a custom message through a channel using Liquid. For example, "Hello __Ann F.__, Thanks for purchasing that __red, medium backpack__ for __$40.00__! Thanks for shopping at __Backpack Locker__!"

If you do want to save, store and track properties to segment with, you need to set them up as custom attributes. This can be done with the power of webhooks! Using webhooks, you can tell Braze to "listen" for whenever a purchase event happens and then set up the webhook so that it parses the properties and saves them as custom attributes. Now that these properties are custom attributes, we can see and segment these properties in the dashboard.

For info on how to set up webhooks, check out our [Webhook][1] documentation.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[20]: http://en.wikipedia.org/wiki/ISO_4217 "ISO 4217 Currency Code"
