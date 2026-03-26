---
nav_title: Canvas entry properties
article_title: Canvas entry properties
page_order: 4
description: "Learn how to use Canvas entry properties as a personalization source in your messages."
---

# Canvas entry properties

> When a Canvas is triggered by a custom event, purchase, or API call, you can use metadata from that trigger to personalize messages throughout the Canvas workflow. These values are known as entry properties, and they persist across all steps in a Canvas.

## How it works

{% raw %}
Entry properties are available through the `{{context.${property_name}}}` Liquid tag. When a user enters a Canvas, Braze captures the properties from the triggering event or API call, and you can reference them in any subsequent Canvas step.

For example, if a Canvas is triggered by a `completed_order` event with a `product_name` property:

```liquid
Thanks for ordering {{context.${product_name}}}! We'll send you a tracking number soon.
```
{% endraw %}

Entry properties are available in action-based and API-triggered Canvases.

## Persistent entry properties

Persistent entry properties let you reference the original entry data in every step of your Canvas, including steps that occur after a delay. Without persistence, entry properties are only available in the first step.

{% alert important %}
Persistent entry properties are part of the original Canvas entry properties workflow. For the current updated Canvas editor, refer to [Context and event properties]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/).
{% endalert %}

For the full reference on persistent entry properties, see [Persistent entry properties]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties/).
