You can use Canvas entry properties and event properties in your Canvas user journeys.

{% tabs local %}
{% tab Canvas Entry Properties %}

[Canvas entry properties]({{site.baseurl}}/api/objects_filters/context_object/) are the properties you map for Canvases that are action-based or API-triggered. Note that the `canvas_entry_properties` object has a maximum size limit of 50 KB.

{% alert note %}
For in-app message channels specifically, `context` can only be referenced in Canvas.
{% endalert %}

You can reference `context` in any Message step with this Liquid format: ``{% raw %} context.${property_name} {% endraw %}``. Note that the events must be custom events or purchase events to be used this way.

#### Use case

{% raw %}
Let's say a retail store, RetailApp, has the following request: `\"context\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. 

RetailApp can pull the product name (shoes) into a message with this Liquid: `{{context.${product_name}}}`.
{% endraw %}

RetailApp can also trigger specific messages to send for different `product_name` properties in a Canvas that targets users after they've triggered a purchase event. For example, they can send different messages to users who purchased shoes and users who purchased something else by adding the following Liquid into a Message step.

{% raw %}
```markdown
{% if  {{context.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Expand for original Canvas editor %}

You can no longer create or duplicate Canvases using the original editor. This section is available for reference only. For the Canvases built with the original editor, Canvas entry properties can be referenced in the first full step of a Canvas only.

{% enddetails %}
{% endtab %}

{% tab Event Properties %}

Event properties refer to the properties you set for custom events and purchases. These `event_properties` can be used in campaigns with action-based delivery and Canvases.

{% alert important %}
You can't use `event_properties` in the first Message step of your Canvas. Instead, you must use `context` or add an Action Paths step with the corresponding event **before** the Message step that includes `event_properties`.
{% endalert %}

In Canvas, custom event and purchase event properties can be used in Liquid in any Message step that follows an Action Paths step. Make sure to use {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} if you're referencing these event properties. These events must be custom events or purchase events to be used this way in the Message component.

In the first Message step following an Action Path, you can use event properties related to the event referenced in that Action Path. However, these event properties can only be used if the user actually performed the action (and didn't get sorted into the Everyone Else group). You can have other steps (that are not another Action Paths or Message step) in between this Action Paths and the Message step.

{% details Expand for original Canvas editor %}

You can no longer create or duplicate Canvases using the original editor. This section is available for reference only. For the original Canvas editor, event properties can't be used in scheduled full steps. However, you can use event properties in the first full step of an action-based Canvas, even if the full step is scheduled.

{% enddetails %}

{% endtab %}
{% endtabs %}

Refer to [Canvas entry properties and event properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) for more information and examples.