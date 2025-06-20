---
nav_title: Product Messages
article_title: Product Messages
page_order: 1
description: "This page covers how to use WhatsApp product messages to send interactive WhatsApp messages that showcase products from your Meta catalog."
page_type: reference
alias: "/whatsapp_product_messages/"
tool:
 - Campaigns
channel:
 - WhatsApp
---

# Product messages

> Product messages empower you to send interactive WhatsApp messages that showcase products directly from your Meta catalog.

{% alert important %}
WhatsApp product messages are currently in early access and are planned to have rolling updates through the early access duration. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

When you send a WhatsApp product message to a user, the user goes on the following customer journey:

1. The user receives your product or catalog message in WhatsApp.
2. The user adds products to their cart directly from WhatsApp.
3. The user taps **Place order** in WhatsApp.
4. Your website or app recieves the cart data from Braze and generates a checkout link.
5. The user is directed to your website or app to complete their checkout.

When users add items to their cart through catalog messages, Braze receives webhook data for follow-up actions.

## Requirements

| Requirement | Description |
| --- | --- |
| WhatsApp Business Account | To use WhatsApp product messages, you must have a WhatsApp Business Account connected with Braze. |
| Meta catalog | You need to set up a Meta catalog in your Commerce Manager. |
| Term compliance | Comply with the [Meta Commerce Terms and Policies](https://www.facebook.com/policies_center/commerce). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Product message templates

{% tabs %}
{% tab Catalog messages %}

Display your entire product catalog in an interactive format.

{% alert note %}
You don't need to make additional product selections in Braze, as the catalog connection is managed by Meta and thus is inherited into your product catalog.
{% endalert %}

{% endtab %}
{% tab Multi-product messages %}

Highlight specific products from your catalog, with up to 30 highlighted items per message Currently, there isn't an integrated product selector, so you must manually reference your Meta catalog to obtain product SKUs.

{% alert important %}
Multi-product message templates currently have a header display bug. Meta is working on a fix.
{% endalert %}

{% endtab %}
{% endtabs %}

## Setting up product messages

1. In the [Meta Commerce Manager](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fbusiness.facebook.com%2Fcommerce_manager%2F#), follow [Meta's instructions](https://www.facebook.com/business/help/1275400645914358?id=725943027795860&ref=search_new_1) to create your Meta catalog. Make sure you’re in the same Meta Business Portfolio where your Braze-connected WhatsApp Business Accont resides.
2. Follow Meta's instructions to [connect your Meta catalog](https://www.facebook.com/business/help/1953352334878186?id=2042840805783715) to your Braze-connected WhatsApp Business Account by assigning the "Manage Catalog" permission in Meta Business Manager. 

![Meta "Catalogs" page with an arrow pointing at the "Assign partner" button for the catalog called "sweeney_catalog".]({% image_buster /assets/img/whatsapp/meta_catalog.png %}){: style="max-width:80%;"}

Make sure to use the Braze Business Manager ID, `332231937299182`, as the partner business ID.

![Window to share a catalog with a partner that contains fields to enter a partner business ID and assign the permission "Manage catalog".]({% image_buster /assets/img/whatsapp/share_meta_catalog.png %}){: style="max-width:60%;"}

{: start="3"}
3. Select your Meta catalog settings. You must select “Show catalog icon in chat header” to send catalog messages.

![WhatsApp Manager settings page for the "Catalog_products" catalog.]({% image_buster /assets/img/whatsapp/meta_catalog_settings.png %}){: style="max-width:80%;"}

{: start="4"}
4. In Braze, go through the [embedded signup]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) process to provide permissions. This will unlock the Braze integrated product selector.

{% alert tip %}
For best practices to follow when creating Meta catalogs, refer to [Tips for building a high-quality catalog in Commerce Manager](https://www.facebook.com/business/help/2086567618225367?id=725943027795860).
{% endalert %}

## Building a product message

1. In your Meta Business manager, go to **Message Templates**.
2. Select **Catalog** as a format, and then choose between **Catalog message** (displays full catalog) and **Multi-product catalog message** (highlights specific items).
3. In Braze, create a WhatsApp campaign or Canvas Message step.
4. Select the subscription group that matches where you submitted the template.
5. Select **WhatsApp Template Message**. (Product and catalog messages aren't available yet in response messages.)
6. Select the template you’d like to use.
    - If you select a multi-product template, provide the section title and content IDs for the products to highlight.
7. Continue building your message.

## Managing products

### Accessing Commerce Manager

In your Meta Business Manager, go to **Commerce Manager** and select your organization. Here, you can manage your catalog assets, such as:
- Create new catalogs
- Add products to existing catalogs
- Update product information
- Remove discontinued items

{% alert important %}
If you remove referenced products from your catalog, the associated messages will fail to send.
{% endalert %}

## Checkout: Cart processing and webhooks

When users interact with your WhatsApp product messages, they can browse products and add items to their cart. However, currently there is no built-in checkout functionality for shipping information or payment processing. Instead, we encourage you to create a cart within your own app or website and direct users to that cart using a custom link.

### Considerations

- **No in-app checkout:** Users can't complete purchases directly within WhatsApp. All transactions must be redirected to your website or app.
- **Custom link required:** You need to create a custom link that directs users to their cart on your platform.
- **Manual setup:** The setup process requires manual configuration of your cart and messaging workflows.

{% alert note %}
We currently don't support payments directly occurring in WhatsApp, and future support will be country-specific (currently, Meta offers it only for companies based in and working directly with users in India, Brazil, and Singapore).
{% endalert %}

### Setting up cart event triggers

When a customer places an order in WhatsApp, Braze automatically:
1. Receives the cart contents from WhatsApp (product IDs, quantities, and other order data).
2. Creates an `ecommerce.cart_update` eCommerce event with all relevant data, including `source = whats_app`.
3. Triggers a response, allowing you to set up automated campaigns to respond to the order.

The `ecommerce.cart_update` eCommerce event only appears listed in Braze after an event has been sent, which can be done by generating a test product message from Braze and submitting a cart event.
The cart event includes:

- **Cart ID:** Unique identifier for the cart
- **Products:** List of items with product IDs, quantities, and prices
- **Total Value:** Sum of all items
- **Currency:** The cart's currency
- **Source:** Marked as "whats_app"
- **Metadata:** Additional data like catalog ID and message text

You can find additional Braze cart event information in [Types of eCommerce recommended events]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events).

### Setting up a triggered response

1. Create a custom event trigger for `ecommerce.cart_updated`.
2. Add a property filter for `source = "whats_app"`.
3. Configure follow-up actions based on cart data.

### Recommended checkout implementations 

{% tabs %}
{% tab Simple Liquid-based cart links %}

Use Liquid to build cart URLs directly in your response message. This is best if you have consistent product IDs between WhatsApp and your eCommerce platform.

#### Example Liquid

{% raw %}
```liquid
{% assign cart_link = "http://alejandro-test-new.myshopify.com/cart/" %}
{% for product in event_properties.products %}
 {% assign variant_id = product.product_id %}
 {% assign quantity = product.quantity %}
 {% if forloop.first %}
   {% assign cart_link = cart_link | append: variant_id | append: ":" | append: quantity %}
 {% else %}
   {% assign cart_link = cart_link | append: "," | append: variant_id | append: ":" | append: quantity %}
 {% endif %}
{% endfor %}
{{ cart_link }}
```
{% endraw %}

#### Setup

1. Create a WhatsApp response message campaign with the trigger of an `ecommerce.cart_update` eCommerce event.
2. Create a subsequent message with the cart URL.
3. Build your cart URL with Liquid. If you use Shopify, you can [create a cart permalink](https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks) with the prior example Liquid.

{% endtab %}
{% tab Connected Content %}

Make an API call to your eCommerce system to generate a personalized checkout URL. This is best if you needi dynamic cart URL generation or complex product mapping.

#### Setup

1. Create a webhook campaign or Canvas step triggered by the [`ecommerce.cart_update`]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/?tab=ecommerce.cart_updated) eCommerce event, which will send the cart data to your eCommerce system.
2. Create a WhatsApp campaign or Canvas Message step triggered by the same eCommerce event to send a WhatsApp response message with the cart URL to the user. Follow the direction in the subsequent response message to use [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content).

{% endtab %}
{% tab Webhook and custom events %}

Use webhooks to send cart data to your system, then trigger follow-up messages through custom events. This is best for complex integrations requiring extensive cart processing or multi-step workflows.

#### Setup

Create a webhook campaign or Canvas step triggered by the `ecommerce.cart_update` eCommerce event, which will send the cart data to your eCommerce system. Your API will then:
1. Receive cart data
2. Create a cart in your system
3. Generate the checkout URL
4. Send a `checkout_started` event to Braze, triggering your WhatsApp message to send with the checkout link

{% endtab %}
{% endtabs %}

## Testing and validation

### Test message requirements

Cart functionality carries over between test messages, but processing of the inbound result doesn't carry over.

### Message preview

- Product images and details are pulled from your Meta catalog.
- Interactive preview shows placeholders until integration is complete.

### Error codes 

- If a product ID doesn't exist in the catalog, you’ll receive the error `product not found for product_retailer_id, fake-product-id, in catalog_id, 1903196950214359`.
- If a catalog is disconnected from the WABA, you'll receive the error `Check if catalog is linked to the WhatsApp Business Account and the catalog is enabled in the WhatsApp Commerce Settings`.
