---
nav_title: "Canvas Entry Properties Object"
article_title: API Canvas Entry Properties Object
page_order: 2
page_type: reference
tool:
  - Canvas
description: "This article explains the Braze Canvas Entry Properties object."

---

# Canvas entry properties object specification

When using one of the endpoints for triggering or scheduling a Canvas via the API, you may provide a map of keys and values to customize messages sent by the first steps of your Canvas, in the `canvas_entry_properties` namespace.

{% alert note %}
The Canvas entry properties object has a maximum size limit of 50 KB. 
{% endalert %}

## Object body

This object body contains an example request.

```json
"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}
```
{% raw %}
For example, a request with `"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}` could add the word "shoes" to a message by adding ```{{canvas_entry_properties.${product_name}}}``` to the request.
{% endraw %}
