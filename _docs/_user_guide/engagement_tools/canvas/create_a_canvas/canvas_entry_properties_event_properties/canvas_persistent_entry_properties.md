---
nav_title: Persistent entry properties
article_title: Persistent Entry Properties
alias: "/persistent_entry/"
page_type: reference
description: "This reference article describes how to use persistent entry properties in your Canvas to send more curated messages, and create a highly refined end-user experience."
tool: Canvas
page_order: 5
---

# Persistent entry properties

> When a Canvas is triggered by a custom event, purchase, or an API call, you can use metadata from the API call, custom event, or purchase event for personalization in each step in your Canvas workflow. 

Prior to this feature, the entry properties could only be used in the first step of Canvas. The ability to use entry properties throughout a Canvas journey allows customers to send more curated messages and create a highly refined end-user experience.

## Using entry properties

Entry properties can be used in action-based and API-triggered Canvases. These entry properties are defined when a Canvas is triggered by a custom event, purchase, or API call. Refer to the following articles for more information:

- [Canvas entry properties object]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)
- [Event properties object]({{site.baseurl}}/api/objects_filters/event_object/)
- [Purchase object]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-product_id)

Properties passed in from these objects can be referenced by using the `canvas_entry_properties` Liquid tag. For example, a request with `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}` could add the word "shoes" to a message by adding the Liquid {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}.

When a Canvas includes a message with the `canvas_entry_properties` Liquid tag, the values associated with those properties will be saved for the duration of a user's journey in the Canvas and deleted when the user exits the Canvas. Note that Canvas entry properties are only available for reference in Liquid. To filter on the properties within the Canvas, use [event property segmentation]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/) instead.

{% alert note %}
The Canvas entry properties object has a maximum size limit of 50 KB.
{% endalert %}

## Updating Canvas to use entry properties

If an active Canvas that previously did not include any messages that use `canvas_entry_properties` is edited to include `canvas_entry_properties`, the value corresponding to that property will not be available for users who entered the Canvas before `canvas_entry_properties` was added to the Canvas. The values will only be saved for users that enter the Canvas after the change is made.

For example, if you initially launched a Canvas that did not use any entry properties on November 3, then added a new property `product_name` to the Canvas on November 11, values for `product_name` would only be saved for users that entered the Canvas on November 11 onward.

In the case that a Canvas entry property is null or blank, you can abort messages using conditionals. The following code snippet is an example of how you could use Liquid to abort a message.
{%raw%}
```
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}
```
{%endraw%}

To read more about aborting messages with Liquid, check out our [Liquid documentation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages).

## Global Canvas entry properties

With `canvas_entry_properties`, you can set global properties that apply to all users or user-specific properties that only apply to the specified user. The user-specific property will supersede the global property for that user.

### Example request

```
url -X POST \
-H 'Content-Type:application/json' \
-d '{
      "api_key": "a valid rest api key",
      "canvas_id": "the ID of your Canvas",
         "canvas_entry_properties": {
            "food_allergies": "none"
          },
      "recipients": [
        {
          "external_user_id": Customer_123,
          "canvas_entry_properties": {
            "food_allergies": ["dairy", "soy"],
            "nutrition": {
              "calories_per_serving": 200,
              "serving_size_in_ounces": 4
            }
          }
        }
      ]
    }' \
```
 
In this request, the global value for "food allergies" is "none". For Customer_123, the value is "dairy". Messages in this Canvas containing the Liquid snippet {%raw%}`{{canvas_entry_properties.${food_allergies}}}`{%endraw%} will template with "dairy" for Customer_123 and "none" for everyone else. 

## Use case

If you have a Canvas that is triggered when a user browses an item in your eCommerce site but does not add it to their cart, the first step of the Canvas might be a push notification asking if they are interested in purchasing the item. You could reference the product name by using {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}

![]({% image_buster /assets/img/persistent_entry_properties/PEP1.png %}){: style="border:0;margin-left:15px;"}

The second step may send another push notification prompting the user to checkout if they added the item to their cart but have not purchased it yet. You can continue to reference the `product_name` entry property by using {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}.

![]({% image_buster /assets/img/persistent_entry_properties/PEP12.png %}){: style="border:0;margin-left:15px;"}

