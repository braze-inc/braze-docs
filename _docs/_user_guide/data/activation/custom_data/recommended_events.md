---
nav_title: Recommended events
article_title: Recommended Events
alias: /recommended_events/
page_type: reference
description: "This reference article describes recommended events, which are recommendations provided by Braze for eCommerce events."
---

# Recommended events

> Recommended events map to the most common eCommerce use cases. By using recommended events, you can unlock pre-built Canvas templates, reporting dashboards that map to the customer lifecycle, and more.

For example, you may have a custom event named “cart_updated” or “update_to_cart” to capture when a user has added, removed, or updated the products in their cart. For recommended events, Braze will provide the event template, which includes a defined name and relevant properties for this event.

{% alert important %}
Recommended events are currently in early access. Contact your Braze customer success manager if you’re interested in participating in this early access. <br><br>If you're leveraging the new [Shopify connector]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), these recommended events will be automatically available through the integration.
{% endalert %}

## How it works

Braze applies special validation to all recommended events, and some recommended events have special post-processing actions. For certain industry recommended events, Braze may support special handling, such as new action-based triggers for campaigns and Canvases.

Recommended events function similarly to [custom events]({{site.baseurl}}/user_guide/data/custom_data/custom_events). You can export recommended events from Currents, blocklist them, and use them in reporting. You can also send data into Braze for tracking these events using the [Braze SDK]({{site.baseurl}}/developer_guide/getting_started/sdk_overview) or the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

### eCommerce recommended events

[eCommerce recommended events]({{site.baseurl}}/ecommerce_events/) are based on recommended events. These eCommerce recommended events track actions taken by your customers such as viewing a product, updating their cart, or starting the checkout process. 

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

#### eCommerce Canvas templates

Check out our dedicated [eCommerce use cases]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/) for more ideas on how to use Braze Canvas pre-built templates to implement essential strategies.

## Frequently asked questions

### Are recommended events the same as custom events?

No. Braze will define opinionated data schemas for recommended events. This will include required and optional event properties that will undergo a validation process in Braze. [Custom events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) are specific actions taken by, or updates about, your users in your app or website that you want to track. You can customize the event name and what it tracks.

### Can I customize the name of the recommended events?

No. Recommended events have standardized event names and properties. These standardizations help create consistency across your data.

### Can I still use purchase events to log purchases?

With the launch of eCommerce recommended events, Braze will phase out the legacy purchase event in the future. If you're currently using the purchase event, you will receive advance notice regarding the deprecation plans. In the meantime, you can continue to use the purchase events until the official deprecation date.