{% tabs %}
{% tab Abandoned browse %}

### Abandoned browse

Use the **Abandoned browse** template to engage users who have browsed products but did not add them to their cart or place an order.

![An applied "Abandoned Browse" Canvas template with expanded "Entry Rules".]({% image_buster /assets/img_archive/abandoned_browse.png %})

#### Setup

On the Canvas page, select **Use a Canvas Template** > **Braze templates** and then apply the **Abandoned browse** template. 

##### Default settings

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

#### Abandoned browse product personalization for emails 

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

##### Product URL

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}    

{% endtab %}
{% tab Abandoned cart %}

### Abandoned cart

Use the **Abandoned cart** template to cover potential lost sales from customers who added products to their cart but did not continue to checkout or place an order. 

![An applied "Abandoned Cart" Canvas template with expanded "Entry Rules".]({% image_buster /assets/img_archive/abandoned_cart.png %})

#### Setup

On the Canvas page, select **Use a Canvas Template** > **Braze templates** and then apply the **Abandoned cart** template. 

##### Default settings

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

#### How abandoned cart re-entry logic works

When a user starts the checkout process, their cart is marked as `checkout_started`. From that point onward, any further cart updates with the same cart ID will not qualify the user to re-enter the abandoned cart user journey.

1. When a user adds an item to their cart, they enter the Canvas.
2. Each time they add or update items, they re-enter the Canvas—this keeps their cart data and messaging up to date.
3. When the user starts the checkout process, their cart is tagged as `checkout_started`, and they exit the Canvas.
4. Any future cart updates using the same cart ID will not trigger re-entry because this cart has already moved into the checkout stage.

When users move to the checkout user journey, they're targeted by the [abandoned checkout Canvas](#abandoned-checkout) instead, which is designed for users further along in the purchase journey.

#### Abandoned cart product personalization for emails {#abandoned-cart-checkout}

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

##### HTML cart URL

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

{% endtab %}
{% tab Abandoned checkout %}

### Abandoned checkout

Use the **Abandoned checkout** template to target customers who started the checkout process but left before placing their order. 

![An applied "Abandoned Checkout" Canvas template with expanded "Entry Rules".]({% image_buster /assets/img_archive/abandoned_checkout.png %})

#### Setup

On the Canvas page, select **Use a Canvas Template** > **Braze templates** and then apply the **Abandoned checkout** template. 

##### Default settings

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

#### Abandoned checkout personalization for emails

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

##### Checkout URL

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

{% endtab %}
{% tab Order confirmation and feedback survey %}

### Order confirmation and feedback survey

Use the **Order confirmation & feedback survey** template to confirm successful orders and enhance customer satisfaction.

![An applied "Order confirmation" Canvas template with expanded "Entry Rules".]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

#### Setup

On the Canvas page, select **Use a Canvas Template** > **Braze templates** and then apply the **Order confirmation & feedback survey** template. 

##### Default settings

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

#### Order confirmation personalization for emails

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

##### Order status URL

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

{% endtab %}
{% endtabs %}