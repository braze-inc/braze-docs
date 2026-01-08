---
nav_title: "Canvas context object"
article_title: API Canvas Context Object
page_order: 2
page_type: reference
alias: /api/objects_filters/canvas_entry_properties_object/
tool:
  - Canvas
description: "This article explains the Braze Canvas context object."

---

# Canvas context object

> When using one of the endpoints for triggering or scheduling a Canvas through the API, you may provide a map of keys and values to customize messages sent by the first steps of your Canvas, in the `context` namespace.

{% alert note %}
The context object has a maximum size limit of 50 KB. 
{% endalert %}

## Object body

This object body contains an example request.

```json
"context": {"product_name" : "shoes", "product_price" : 79.99}
```

{% raw %}
For example, a request with `"context": {"product_name" : "shoes", "product_price" : 79.99}` could add the word "shoes" to a message by adding ```{{context.${product_name}}}``` to the request.
{% endraw %}
