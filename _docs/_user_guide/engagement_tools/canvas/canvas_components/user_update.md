---
nav_title: User update
article_title: User Update 
alias: "/user_update/"
page_order: 12
page_type: reference
description: "This reference article covers the User Update component and how to use it in your Canvases."
tool: Canvas
---

# User Update 

> The User Update component allows you to update a user's attributes, events, and purchases in a JSON editor, so there's no need to include sensitive information like API keys.

## How this component works

![A User Update step named "Update loyalty" that updates an attribute "Is Premium Member" to "true".]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

When using this component in your Canvas, updates don't count toward your `/users/track` requests per minute rate limit. Instead, these updates are batched so Braze can process them more efficiently than a Braze-to-Braze webhook. Note that this component doesn't log [data points]({{site.baseurl}}/user_guide/data/data_points/) when being used to update non-billable data points (such as subscription groups).

After users enter the User Update step and it completes processing, they advance to the next step. This means any subsequent messaging that relies on these user updates is up-to-date when the next step is run.

## Creating a user update

Drag and drop the component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button at the bottom of the variant or step and select **User Update**. 

There are three options that allow you to update existing user profile information, add new information, or remove user profile information. All combined, the User Update steps in a workspace can update up to 200,000 user profiles per minute.

{% alert tip %}
You can also test the changes made with this component by searching for a user and applying the change to them. This will update the user.
{% endalert %}

## Updating custom attributes

To update or remove a custom attribute, select an attribute name from your list of attributes and enter the value.

![User Update step that updates the two attributes "Loyalty Member" and "Loyalty Program" to "true".]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

## Removing custom attributes

To remove a custom attribute, select an attribute name using the dropdown. You can switch to the [advanced JSON editor](#advanced-json-editor) to further edit. 

![User Update step that removes an attribute "Loyalty Member".]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### Increasing and decreasing values

The User Update step can increase or decrease an attribute value. Select the attribute, select **Increment By** or **Decrement By**, and enter a number. 

#### Track weekly progress

By incrementing a custom attribute that tracks an event, you can track the number of classes that a user has taken in a week. Using this component, the class count can reset at the start of the week and begin tracking again. 

![User Update step that increments the attribute "class_count" by one.]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### Updating an array of objects

An [array of objects]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) is a data-rich custom attribute stored on a user's profile. You can use it to create a history of the user's interactions with your brand and to create segments based on a calculated field, such as purchase history or total lifetime value.

Using the **Advanced JSON Editor** option, you can insert JSON to add items to or remove items from this array of objects.

#### Use case: Updating a user's wishlist

Track a user's wishlist so you can segment or personalize based on their saved items.

1. Create a custom attribute that is an array of objects, for example `wishlist`. Each object can include fields such as `product_id`, `product_name`, and `added_at`.
2. In the User Update step, open the **Advanced JSON Editor** and use the `$add` operation to append an item or the `$remove` operation to remove an item by value.

Example—adding an item to the wishlist:

{% raw %}
```json
{
  "attributes": [
    {
      "wishlist": {
        "$add": [
          {
            "product_id": "SKU-123",
            "product_name": "Wireless Headphones",
            "added_at": "{{$isoTimestamp}}"
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

To remove an item, use `"wishlist": { "$remove": [ { "product_id": "SKU-123", ... } ] }` with the same object structure so Braze can match and remove it.

#### Use case: Calculating the shopping cart total

Track when a user has items in their shopping cart, when they add new items or remove items, and what the total shopping cart value is. 

1. Create a custom array of objects called `shopping_cart`. The following example shows what this attribute may look like. Each item has a unique `product_id` that has additional data in its own nested array of objects, including `price`.

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": number,
         "shipping": number,
         "items_in_cart": number,
         "product_id": array,
         "gift": boolean,
         "discount_code": "enum",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

{:start="2"}
2. Create a [custom event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) named `add_item_to_cart` that is logged when a user adds an item to the basket. 
3. Create a Canvas that targets users who perform this custom event. Now, when a user adds an item to their cart, this Canvas is triggered. You can then target messaging directly to that user, offering coupon codes when they've reached a certain spend, abandoned their cart for a certain amount of time, or anything else that aligns with your use case. 

The `shopping_cart` attribute carries the total of many custom events: the total cost of all the items, the total number of items in the cart, if the shopping cart contains a gift, and so on. This can look something like the following:

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": 22.99,
         "shipping": 4.99,
         "items_in_cart": 2,
         "product_id": ["1001", "1002"],
         "gift": true,
         "discount_code": "flashsale1000",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

## Setting Canvas entry property as an attribute

You can use the user update step to persist a `canvas_entry_property`. Let’s say you have an event that triggers when an item is added to a cart. You can store the ID of the most recent item added to cart and use that for a remarketing campaign. Use the personalization feature to retrieve a Canvas entry property and store it in an attribute.

![User Update step that updates the attribute "most_recent_cart_item" with an item ID.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

### Personalization

To store the property of the trigger event for a Canvas as an attribute, use the personalization modal to extract and store the Canvas entry property. User Update also supports the following personalization features:

* [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 
* [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* [Entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/)
* Liquid logic (including [aborting messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/))
* Multiple attribute or event updates per object

{% alert warning %}
We recommend careful use of Connected Content Liquid personalization in User Update steps, as this step type has a rate limit of 200,000 requests per minute. This rate limit overrides the Canvas rate limit.
{% endalert %}

## Advanced JSON editor

Add an attribute, event, or purchase JSON object up to 65,536 characters to the JSON editor. A user's [global subscription]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) and [subscription group]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) state can also be set.

![]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

Using the JSON editor, you can also preview and test that the user profile is updated with your changes in the **Preview and test** tab. You can either select a random user or search for a specific user. Then, after sending a test to a user, view the user profile using the generated link.

![]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### Considerations

You don't need to include sensitive data like your API key while using the JSON editor, as this is automatically provided by the platform. The following fields should not be included in the JSON editor:
* External user ID
* API key
* Braze cluster URL
* Fields related to push token imports

{% alert important %}
Canvas properties (such as the `canvas_id`, `canvas_name`, and `canvas_variant_name` Liquid tags) are not supported in User Update steps.
{% endalert %}

{% raw %}
### Log custom events

Using the JSON editor, you can also log custom events. Note that this requires a timestamp in ISO format, so assigning a time and date with Liquid at the beginning is needed. Consider this example that logs an event with a time.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "name": "logged_user_event",
      "time": "{{timestamp}}"
    }
  ]
}
```

This next example links an event to a specific app using a custom event with optional properties and the `app_id`.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "app_id": "insert_app_id",
      "name": "rented_movie",
      "time": "{{timestamp}}",
      "properties": {
        "release": {
          "studio": "FilmStudio",
          "year": "2022"
        },
        "cast": [
          {
            "name": "Actor1"
          },
          {
            "name": "Actor2"
          }
        ]
      }
    }
  ]
}
```

### Edit subscription state

Within the JSON editor, you can also edit a user's subscription state. For example, the following shows a user's subscription state updated to `opted_in`. 

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### Update subscription groups 

You can also update subscription groups using this Canvas step. The following example shows how to update one or more subscription groups.

```
{
  "attributes": [
    {
      "subscription_groups": [
        {
          "subscription_group_id": "subscription_group_identifier_1",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_2",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}
```
{% endraw %}

