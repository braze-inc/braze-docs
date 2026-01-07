---
nav_title: eCommerce use cases
article_title: eCommerce Use Cases
alias: /ecommerce_use_cases/
page_order: 4
description: "This reference article covers several pre-built Braze templates tailored specifically for eCommerce marketers, making it easier to implement essential strategies."
toc_headers: h2
---

# eCommerce use cases

> Braze Canvas offers several pre-built templates tailored specifically for eCommerce marketers, making it easier to implement essential strategies. This page offers some key templates you can use to enhance your customer journeys.

{% alert important %}
[eCommerce recommended events]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/) are currently in early access. Contact your Braze customer success manager if you’re interested in participating in this early access. <br><br>If you’re using the new Shopify connector, eCommerce recommended events will automatically be available through the integration.
{% endalert %}

## Using a Canvas template

To use a Canvas template:
1. Go to **Messaging** > **Canvas**.
2. Select **Create Canvas** > **Use a Canvas Template**.
3. Browse the **Braze templates** tab for the template you want to use. You can preview a template by selecting its name.
4. Select **Apply Template** for the template you want to use.<br><br>!["Canvas templates" page opened to the "Braze templates" tab and showing a list of recently used templates and selectable Braze templates.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## eCommerce templates

- [Abandoned browse](#abandoned-browse)
- [Abandoned cart](#abandoned-cart)
- [Abandoned checkout](#abandoned-checkout)
- [Order confirmation and feedback survey](#order-confirmation--feedback-survey)

## Abandoned browse

Use the **Abandoned browse** template to engage users who have browsed products but did not add them to their cart or place an order.

![An applied "Abandoned Browse" Canvas template with expanded "Entry Rules".]({% image_buster /assets/img_archive/abandoned_browse.png %})

### Setup

On the Canvas page, select **Use a Canvas Template** > **Braze templates** and then apply the **Abandoned browse** template. 

#### Default settings

The following settings are pre-configured in your Canvas:
- Basics 
    - Canvas name: **Abandoned browse**
    - Conversion event: `ecommerce.order placed`
        - Conversion deadline: 3 days 
- Entry schedule 
    - Action-based when a user performs the `ecommerce.product_viewed` event
    - Start time is when you create the Canvas template<br><br>!["Action Based Options" for the Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br> 
- Target audience 
    - Entry audience 
        - Email **is not blank**
        - You can also modify the entry audience criteria to meet your business needs
    - Entry controls
        - Users are eligible to re-enter this Canvas after the full duration of the Canvas is complete
    - Exit criteria 
        - Performs `ecommerce.cart_updated`, `ecommerce.checkout_started`, or `ecommerce.order_placed`<br><br>![Entry controls and exit criteria for the Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br> 
- Send settings 
    - Users who are subscribed or opted in 
- Delay step
    - 1 hour delay
- Message step 
    - Review the email template and HTML block with a Liquid templating example to add products to your message in the pre-built template. If you use your own email template, you can also reference [Liquid variables](#message-personalization), as demonstrated in the following section.

### Abandoned browse product personalization for emails 

Here is an example of how you would add an HTML product block for your Abandoned Browse email. 

{% raw %}
```java
<table style="width:100%">
  <tr>
    <th><img src="{{context.${image_url}}}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{context.${product_name}}}</li>
        <li>Price: ${{context.${price}}}</li>
      </ul>
    </th>
  </tr>
</table>
```
{% endraw %}

#### Product URL

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}    

## Abandoned cart

Use the **Abandoned cart** template to cover potential lost sales from customers who added products to their cart but did not continue to checkout or place an order. 

![An applied "Abandoned Cart" Canvas template with expanded "Entry Rules".]({% image_buster /assets/img_archive/abandoned_cart.png %})

### Setup

On the Canvas page, select **Use a Canvas Template** > **Braze templates** and then apply the **Abandoned cart** template. 

#### Default settings

The following settings are pre-configured in your Canvas:
- Basics 
    - Canvas name: **Abandoned cart**
    - Conversion event: `ecommerce.order_placed`
        - Conversion deadline: 3 days 
- Entry schedule 
    - Action-based trigger when a user triggers the **Perform Cart Updated Event** (located in the dropdown)
    - Start time is when you create the Canvas template<br><br>!["Action Based Options" for the Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br> 
- Target Audience 
    - Entry audience 
        - Has used these apps **more than 0** times 
        - Email **is not blank**
    - Entry controls
        - Users are immediately re-eligible for Canvas entry
    - Exit criteria 
        - Performs `ecommerce.cart_updated`, `ecommerce.checkout_started`, or `ecommerce.order_placed`<br><br>![Entry controls and exit criteria for the Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br> 
- Send settings 
    - Users who are subscribed or opted in 
- Delay step
     - 4 hour delay
- Message step 
    - Review the email template and HTML block with a Liquid templating example to add products to your message in the pre-built template. If you use your own email template, you can also reference [Liquid variables](#message-personalization), as demonstrated in the following section.


### How abandoned cart re-entry logic works

When a user starts the checkout process, their cart is marked as `checkout_started`. From that point onward, any further cart updates with the same cart ID will not qualify the user to re-enter the abandoned cart user journey.

1. When a user adds an item to their cart, they enter the Canvas.
2. Each time they add or update items, they re-enter the Canvas—this keeps their cart data and messaging up to date.
3. When the user starts the checkout process, their cart is tagged as `checkout_started`, and they exit the Canvas.
4. Any future cart updates using the same cart ID will not trigger re-entry because this cart has already moved into the checkout stage.

When users move to the checkout user journey, they're targeted by the [abandoned checkout Canvas](#abandoned-checkout) instead, which is designed for users further along in the purchase journey.

### Abandoned cart product personalization for emails {#abandoned-cart-checkout}

Abandoned cart user journeys require a special `shopping_cart` Liquid tag for product personalization. 

Here is an example of how you would add an HTML block with your `shopping_cart` Liquid tag to add products into your email. 

{% raw %}
```java
<table style="width:100%">
  {% shopping_cart {{context.${cart_id}}} %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

{% alert note %}
If you use Shopify, add your catalog name to get the variant image URL. 
{% endalert %}

#### HTML cart URL

If you want to direct users back to their cart, you can add a nested event property under the metadata object, such as:

{% raw %}
```liquid
{{context.${metadata}.cart_url}}
```
{% endraw %}

If you use Shopify, create your cart URL by using this Liquid template:

{% raw %}
```liquid
{{context.${source}}}/checkouts/cn/{{context.${cart_id}}} 
```
{% endraw %}

## Abandoned checkout

Use the **Abandoned checkout** template to target customers who started the checkout process but left before placing their order. 

![An applied "Abandoned Checkout" Canvas template with expanded "Entry Rules".]({% image_buster /assets/img_archive/abandoned_checkout.png %})

### Setup

On the Canvas page, select **Use a Canvas Template** > **Braze templates** and then apply the **Abandoned checkout** template. 

#### Default settings

The following settings are pre-configured in your Canvas:

- Basics 
    - Canvas name: **Abandoned checkout**
    - Conversion event: `ecommerce.order_placed`
        - Conversion deadline: 3 days 
- Entry schedule 
    - Action-based trigger when a user performs the `ecommerce.checkout_started` event
    - Start time is when you create the Canvas template<br><br>!["Action Based Options" for the Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- Target audience 
    - Entry audience 
        - Has used these apps **more than 0** times 
        - Email **is not blank**
    - Entry controls
        - Users are immediately re-eligible for Canvas entry
        - Exit criteria 
            - Performs the `ecommerce.order_placed` events<br><br>![Entry controls and exit criteria for the Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- Send settings 
    - Users who are subscribed or opted in 
- Delay step
    - 4 hour delay
- Message step 
    - Review the email template and HTML block with a Liquid templating example to add products to your message in the pre-built template. If you use your own email template, you can also reference [Liquid variables](#message-personalization), as demonstrated in the following section.

### Abandoned checkout personalization for emails

Abandoned checkout user journeys require a special `shopping_cart` Liquid tag for product personalization. 

Here is an example of how you would add an HTML block with your `shopping_cart` Liquid tag to add products into your email. 

{% raw %}
```java
<table style="width:100%">
  {% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
    {% endfor %}
</table>
```
{% endraw %}

#### Checkout URL

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

## Order confirmation and feedback survey

Use the **Order confirmation & feedback survey** template to confirm successful orders and enhance customer satisfaction.

![An applied "Order confirmation" Canvas template with expanded "Entry Rules".]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

### Setup

On the Canvas page, select **Use a Canvas Template** > **Braze templates** and then apply the **Order confirmation & feedback survey** template. 

#### Default settings

The following settings are pre-configured in your Canvas:

- Basics 
    - Canvas name: **Order confirmation with feedback survey**
    - Conversion event: `ecommerce.session_start`
        - Conversion deadline: 10 days 
- Entry schedule 
    - Action-based trigger when a user performs the `ecommerce.cart_updated` event
    - Start time is when you create the Canvas template<br><br>!["Action Based Options" for the Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- Target audience 
    - Entry audience 
        - Has used these apps **more than 0** times 
        - Email **is not blank**
    - Entry controls
        - Users are immediately re-eligible for Canvas entry
    - Exit criteria 
        - Not applicable<br><br>![Additional filters and entry controls for the Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- Send settings 
    - Users who are subscribed or opted in 
- Message step 
    - Review the email template and HTML block with a Liquid templating example to add products to your message in the pre-built template. If you use your own email template, you can also reference [Liquid variables](#message-personalization), as demonstrated in the following section.

### Order confirmation personalization for emails

Here is an example of how you would add an HTML product block to your order confirmation after an order is placed.

{% raw %}
```json
<table style="width:100%">
  {% for item in {{context.${products}}} %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200" /></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{item.product_name}}</li>
        <li>Price: {{item.price}}</li>
        <li>Quantity: {{item.quantity}}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

#### Order status URL

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

## Message personalization

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) is a powerful templating language used by Braze that allows you to create dynamic and personalized content for your customers. By using Liquid tags, you can customize messages based on customer data, product information, and other variables, enhancing the shopping experience and driving engagement.

### Key features of Liquid

- **Dynamic content:** Insert customer-specific information such as names, order details, and preferences into your messages.
- **Conditional logic:** Use if/else statements to display different content based on specific conditions (such as customer location and purchase history).
- **Loops:** Iterate over collections of products or customer data to display lists or grids of items.

### Getting started with Liquid

To begin personalizing your messages using Liquid tags, you can refer to the following resources:

- [Shopify data]({{site.baseurl}}/shopify_features/#shopify-data) reference with pre-defined liquid tags
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

## Segmentation

Use Braze segments to create targeted customer segments based on specific attributes and behaviors, and deliver personalized messaging and campaigns. With this powerful feature, you can effectively engage your customers by reaching the right audience with the right message at the right time.

For more information on getting started with segments, check out [About Braze segments]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments).

### Recommended events

eCommerce events are based on [recommended events]({{site.baseurl}}/recommended_events/).
Because recommended events are more opinionated custom events, you can search for the recommended eCommerce event names by selecting any [custom event filter]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#segmentation-filters).

### eCommerce filters

Segment your users with eCommerce filters, like **Ecommerce Source** and **Total Revenue**, by going to the **Ecommerce** section within the segmenter. 

For a list of eCommerce filters and their definitions, refer to [Segment filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) and select the "eCommerce" search category.

![Segment filters dropdown with "Ecommerce" filters.]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:50%"}

{% alert important %}
The purchase event will eventually be deprecated and replaced with [eCommerce recommended events]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/). When this happens, segment filters will no longer populate under purchase behavior. For a full list of purchase events, refer to [Logging purchase events]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events). 
{% endalert %}

## Nested event properties

To segment by nested event properties, you can leverage [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions). For example, you can use Segment Extensions to find who has bought the product “SKU-123” in the last 90 days.

## Analytics

{% alert note %}
At this time, the Shopify integration doesn’t support populating the Braze [purchase event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-events). As a result, purchase filters, Liquid tags, action-based triggered, and analytics should use the ecommerce.order_placed event. 
{% endalert %}

### Custom Events report

To create a [Custom Events report]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#analytics) based on who has performed an event supported through the integration, you can specify the specific [event name]({{site.baseurl}}/shopify_data_features/).

### Dashboards

#### Conversions dashboard

To gain insights into the trends related to orders placed from your launched Canvases, set up a [Conversions dashboard]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard#conversions-dashboard) and specify your Canvases.

#### eCommerce revenue dashboard

To gain insights into revenue attributed to the last campaign or Canvas a user interacted with before placing an order, use the [eCommerce revenue dashboard]({{site.baseurl}}/ecommerce_revenue_dashboard/) and select a conversion window.

### Query Builder

For more advanced reporting use cases, you can use the Braze [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) to generate custom reports. 

