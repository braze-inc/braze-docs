---
nav_title: "Trigger properties object"
article_title: API Trigger Properties Object
page_order: 11
page_type: reference
description: "This reference article explains the different components of the trigger properties object."
tool: Campaigns

---

# Trigger properties object

> When using one of the endpoints for sending a campaign with API-triggered delivery, you may provide a map of keys and values to customize your message.

If you make an API request that contains an object in `trigger_properties`, the values in that object can then be referenced in your message template under the `api_trigger_properties` namespace. For example, a request with the following could add the word `"shoes"` to a message by adding {% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %}.

Note that while trigger properties can be templated into messages, they aren't automatically stored in the user profile by default.

{% alert note %}
The `trigger_properties` object and {% raw %}`api_trigger_properties.${product_name}`{% endraw %} syntax is only supported in campaigns. To customize messages with keys and values from an API trigger request for Canvas, use the [Canvas entry properties object]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). The `trigger_properties` object has a maximum size limit of 50 KB.
{% endalert %}

## Object body

```json
{
  "trigger_properties" : {
    "product_name" : "shoes",
    "product_price" : 79.99,
    "details" : {
      "color" : "red",
      "size" : {
        "numerical" : 10,
        "country" : "US"
      }
    },
    "related_skus": ["123", "456", "789"]
  }
}
```


