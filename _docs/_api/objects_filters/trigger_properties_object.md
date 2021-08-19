---
nav_title: "Trigger Properties Object"
article_title: Trigger Properties Object
page_order: 11
page_type: reference
description: "This article explains the different components of the Trigger Properties object."
tool: Campaigns

---

# Trigger Properties Object Specification

When using one of the endpoints for sending a campaign with API-Triggered Delivery, you may provide a map of keys and values to customize your message.

If you make an API request that contains an object in `"trigger_properties"`, the values in that object can then be referenced in your message template under the api_trigger_properties namespace.
{% raw %}
For example, a request with the following could add the word `"shoes"` to a message by adding `{{api_trigger_properties.${product_name}}}`.
{% endraw %}

```json
"trigger_properties" : {
  "product_name" : "shoes",
  "product_price" : 79.99
  }
```

{% raw %}
The "trigger_properties" object and `api_trigger_properties.${product_name}` syntax is only supported in Campaigns. To customize messages with keys and values from an API trigger request, use the [Canvas Entry Properties Object](https://www.braze.com/docs/api/objects_filters/canvas_entry_properties_object/).
{% endraw %}


