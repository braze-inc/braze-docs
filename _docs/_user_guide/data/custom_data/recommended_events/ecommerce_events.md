---
nav_title: eCommerce Recommended Events
article_title: eCommerce Recommended Events
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "This reference article describes eCommerce recommended events and properties, their usage, segmentation, where to view relevant analytics, and more."
---

# eCommerce recommended events

> This page covers eCommerce recommended events and properties. These events are created to capture key shopping behaviors that marketers need to trigger effective messaging, such as targeting abandoned carts.

Braze recognizes that data planning takes time. We encourage our customers to familiarize their development teams and begin sending these events now. While some features may not be available immediately with the eCommerce recommended events, you can look forward to the introduction of new products throughout 2025 that will enhance your eCommerce capabilities.

{% alert important %}
eCommerce recommended events are currently in early access. Contact your Braze customer success manager if you’re interested in participating in this early access. <br><br>If you're leveraging the new [Shopify connector]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), these recommended events will be automatically available through the integration.
{% endalert %}


## Types of eCommerce recommended events

{% tabs %}
{% tab ecommerce.product_viewed %}

You can use the product viewed event to trigger when a customer views a product detail page.

#### Properties

| Property name | Required | Data type | Description | 
|---|---|---|---|
| `product_id` | Yes | String | A unique identifier for the product that was viewed. <br> For non-Shopify customers, this will be the value you set for catalog item IDs like SKUs. |
| `product_name` | Yes | String | The name of the product that was viewed. | 
| `variant_id` | Yes | String | A unique identifier for the product variant. An example is `shirt_medium_blue` |
| `image_url` | No | String | URL of the product image. |
| `product_url` | No | String | URL to the product page for more details. |
| `price` | Yes | Float | The variant unit price of the product at the time of viewing. |
| `currency` | Yes | String | The currency in which the product price is listed (such as "USD" or "EUR") in [ISO 4217 format](https://www.iso.org/iso-4217-currency-codes.html). |
| `source` | Yes | String | Source the event is derived from. (For Shopify, this is storefront). |
| `metadata` | No | Object | |
| `sku` | No | String | (Shopify only) Shopify SKU. This can be configured as the catalog ID field. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Example object

```json
{
    "name": "ecommerce.product_viewed",
    "properties": {
        "product_id": "12345",
        "product_name": "product",
        "variant_id": "123",
        "image_url": "www.image-url.com",
        "product_url": "mystorefront.myshopify.com/product",
        "price": 10,
        "currency": "USD",
        "source": "mystorefront.myshopify.com",
        "metadata": {
            "sku": "sku"
        }
    }
}
```
{% endtab %}
{% tab ecommerce.cart_updated %}

You can use the cart updated event to track when products are added, removed, or updated in the cart. The `ecommerce.cart_updated` event verifies the following information before triggering:

- The event time is greater than the `updated_at` time for the user's specific cart.
- The cart hasn't proceeded to the checkout process.
- The `products` array isn't empty.

#### Carts mapping object

The `ecommerce.cart_updated` event has a carts mapping object. This object is created for the user profile that contains a mapping of carts, which contain all products in the shopper's cart. You can access the products in their shopping cart through the Liquid tag: 

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

If a cart hasn’t been updated and progressed to an order placed event in 10 days, we'll delete the cart and associated products.

{% alert note %}
Products per cart aren't limited on Braze. However, Shopify’s limit is 500.
{% endalert %}

#### Cart behavior when merging user profiles

If there are two carts, add both to the merged user. Re-enqueue the Canvas if it's the same or different cart to send a message with the most recent cart information. The `ecommerce.cart_updated` event will contain the lasted cart ID and the lasted products in the cart.

#### Properties

| Property name | Required | Data type | Description | 
|---|---|---|---|
| `cart_id` | Yes | String | Unique identifier for the cart. If no value is passed, we'll determine a default value (shared across cart, checkout, and order events) for the user cart mapping. |
| `total_value` | Yes | Float | Total monetary value of the cart. | 
| `currency` | Yes | String | The currency in which the product price is listed (such as "USD" or "EUR") in [ISO 4217 format](https://www.iso.org/iso-4217-currency-codes.html). |
| `products` | Yes | Array |  |
| `product_id` | Yes | String | A unique identifier for the product that was viewed. <br> This value be can be the product ID or SKU. |
| `product_name` | Yes | String | The name of the product that was viewed. |
| `variant_id` | Yes | String | A unique identifier for the product variant. An example is `shirt_medium_blue` |
| `image_url` | No | String | URL of the product image. |
| `product_url` | No | String | URL to the product page for more details. |
| `quantity` | Yes | Integer | Number of units of the product in the cart. |
| `price` | Yes | Float | The variant unit price of the product at the time of viewing. |
| `metadata` | No | Object | Additional metadata field about the product that the customer wants to add for their use cases. For Shopify, we will add SKU. <br> This will have a limit based on our general event properties limit of 50kb. |
| `sku` | No | String | (Shopify only) Shopify SKU. This can be configured as the catalog ID field. |
| `source` | Yes | String | Source the event is derived from. (For Shopify, this is storefront). |
| `metadata` | No | Object | Additional metadata field about the product that the customer wants to add for their use cases. For Shopify, we will add SKU. <br> This will have a limit based on our general event properties limit of 50kb. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Example object

```json
{
    "name": "ecommerce.cart_updated",
    "properties": {
        "cart_id": "Z2NwLXVzLWVhc3QxOjAxSjk3UFg4RlFZMjVTVkRHRlc1RlI3SlRY",
        "currency": "USD",
        "total_value": 2000000,
        "products": [
            {
                "product_id": "8266836345064",
                "product_name": "PANTS!!!",
                "variant_id": "44610569208040",
                "image_url": "https://cdn.shopify.com/s/files/1/0604/4211/6328/files/1200px-Trousers-colourisolated.jpg?v=1689256168",
                "product_url": "https://test-store.myshopify.com/products/pants?variant=44610569208040",
                "quantity": 2,
                "price": 1000000,
                "metadata": {
                    "sku": "007"
                }
            }
        ],
        "source": "https://test-store.myshopify.com",
        "metadata": {}
    }
}
```
{% endtab %}
{% tab ecommerce.checkout_started %}

You can use the checkout started event to retarget customers who have started the checkout process but haven't placed an order.

Similar to the `ecommerce.cart_updated` event, this event allows you to leverage the shopping cart Liquid tag to access all products within their cart for abandoned checkout messages:

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} :abort_if_not_abandoned false %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

#### Properties

| Property name | Required | Data type | Description | 
|---|---|---|---|
| `checkout_id` | Yes | String | Unique identifier for the checkout. |
| `cart_id` | No | String | Unique identifier for the cart. If no value is passed, we'll determine a default value (shared across cart, checkout, and order events) for the user cart mapping.. | 
| `total_value` | Yes | Float | Total monetary value of the cart. |
| `currency` | Yes | String | Currency in which the cart is valued. |
| `products` | Yes | Array of objects |  |
| `product_id` | Yes | String | A unique identifier for the product that was viewed. For example, this value could be the product ID or SKU. |
| `product_name` | Yes | String | The name of the product that was viewed.  |
| `variant_id` | Yes | String | A unique identifier for the product variant. An example is `shirt_medium_blue` |
| `image_url` | No | String | URL of the product image. |
| `product_url` | No | String | URL to the product page for more details. |
| `quantity` | Yes | Integer | Number of units of the product in the cart. |
| `price` | Yes | Float | The variant unit price of the product at the time of viewing. |
| `metadata` | No | Object | Additional metadata field about the product that the customer wants to add for their use cases. For Shopify, we will add SKU. <br> This will have a limit based on our general event properties limit of 50kb. |
| `sku` | No | String | (Shopify only) Shopify SKU. This can be configured as the catalog ID field. |
| `source` | Yes | String | Source the event is derived from. (For Shopify, this is storefront). |
| `metadata` | No | Object |  |
| `checkout_url` | No | String | URL for the checkout page. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Example object

```json
{
    "name": "ecommerce.checkout_started",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "cart_id": "eeafa272cebfd4b22385bc4b645e762c",
        "total_value": 421.88,
        "currency": "USD",
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "checkout_id": "123123123",
        "metadata": {
            "checkout_url": "https://checkout.local/548380009/checkouts/123123123/recover?key=example-secret-token"
        }
    }
}
```
{% endtab %}
{% tab ecommerce.order_placed %}

You can use the order placed event to trigger when a customer successfully completes the checkout process and places an order.

#### Properties

| Property name | Required | Data type | Description | 
|---|---|---|---|
| `order_id` | Yes | String | Unique identifier for the order placed. |
| `cart_id` | No | String | Unique identifier for the cart. If no value is passed, we'll determine a default value (shared across cart, checkout, and order events) for the user cart mapping. |
| `total_value` | Yes | Float | Total monetary value of the cart. | 
| `currency` | Yes | String | Currency in which the cart is valued. |
| `total_discounts` | No | Float | Total amount of discounts applied to the order. | 
| `discounts`| No | Array of objects | Detailed list of discounts applied to the order. |
| `products` | Yes | Array of objects |  |
| `product_id` | Yes | String | A unique identifier for the product that was viewed. This value be can be the product ID or SKU. |
| `product_name` | Yes | String | The name of the product that was viewed. |
| `variant_id` | Yes | String | A unique identifier for the product variant. An example is `shirt_medium_blue` |
| `image_url` | No | String | URL of the product image. |
| `product_url` | No | String | URL to the product page for more details. |
| `quantity` | Yes | Integer | Number of units of the product in the cart. |
| `price` | Yes | Float | The variant unit price of the product at the time of viewing. |
| `metadata` | No | Object | Additional metadata field about the product that the customer wants to add for their use cases. For Shopify, we will add SKU. <br> This will have a limit based on our general event properties limit of 50kb. |
| `sku` | No | String | (Shopify only) Shopify SKU. This can be configured as the catalog ID field. |
| `source` | Yes | String | Source the event is derived from. (For Shopify, this is storefront). |
| `metadata` | No | Object |  |
| `order_status_url` | No | String | URL to view the status of the order. |
| `order_number` | No | String | (Shopify only) Unique order number for the order placed. |
| `tags` | No | Array | (Shopify only) Order tags
| `referring_site` | No | String | (Shopify only) The site the order originated from (such as Meta). |
| `payment_gateway_names` | No | Array | (Shopify only) Payement system source (such as point of sale or mobile). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Example object

```json
{
    "name": "ecommerce.order_placed",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "cart_id": "eeafa272cebfd4b22385bc4b645e762c",
        "total_value": 421.88,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
            "order_number": 1234,
            "tags": [
                "heavy",
                "heavy2"
            ],
            "referring_site": "https://www.google.com",
            "payment_gateway_names": [
                "visa",
                "bogus"
            ]
        }
    }
}
```
{% endtab %}
{% tab ecommerce.order_refunded %}

You can use the order refunded event to trigger when an order is partially or entirely refunded.

#### Properties

| Property Name       | Required | Data Type | Description   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | Yes      | String    | Unique identifier for the order placed.        |
| `total_value`         | Yes      | Float     | Total monetary value of the cart.    |
| `currency`            | Yes      | String    | Currency in which the cart is valued.    |
| `total_discounts`     | No       | Float     | Total amount of discounts applied to the order.   |
| `discounts`           | No       | Array of objects     | Detailed list of discounts applied to the order. |
| `products`            | Yes      | Array of objects     |  |
| `product_id`       | Yes      | String    | A unique identifier for the product that was viewed. This value can be the product ID, SKU, or similar. <br>If a partial refund is issued and there is no `product_id` assigned to the refund (for example, an order-level refund), provide a generalized `product_id`.             |
| `product_name`     | Yes      | String    | The name of the product that was viewed.                                                                      |
| `variant_id`       | Yes      | String    | A unique identifier for the product variant (such as `shirt_medium_blue`).                                         |
| `image_url`        | No       | String    | URL of the product image.     |
| `product_url`      | No       | String    | URL to the product page for more details.  |
| `quantity`         | Yes      | Integer   | Number of units of the product in the cart.   |
| `price`            | Yes      | Float     | The variant unit price of the product at the time of viewing.  |
| `metadata`         | No       | Object    | Additional metadata field about the product that the customer wants to add for their use cases. For Shopify, we will add SKU. This will have a limit based on our general event properties limit of 50kb. |
| `sku`            | No       | String    | (Shopify only) Shopify SKU. This can be configured as the catalog ID field.  |
| `source`              | Yes      | String    | Source the event is derived from. (For Shopify, this is storefront).    |
| `metadata`            | No       | Object    |                |
| `order_status_url`  | No       | String    | URL to view the status of the order.     |
| `order_note`       | No       | String    | (Shopify only) Note appended to the order by the merchant.    |
| `order_number`     | No       | String    | (Shopify only) Unique order number for the order placed.   |
| `tags`             | No       | Array     | (Shopify only) Order tags.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Example object

```json
{
    "name": "ecommerce.order_refunded",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "total_value": 421.88,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
			"order_note": "item was broken",
            "order_number": 1234,
            "tags": [
                "heavy",
                "heavy2"
            ]
        }
    }
}
```
{% endtab %}
{% tab ecommerce.order_cancelled %}

You can use the order cancelled event to trigger when a customer cancels an order.

#### Properties

| Property Name      | Required | Data Type | Description       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | Yes      | String    | Unique identifier for the order placed.              |
| `cancel_reason`       | Yes      | String    | Reason why the order was cancelled.           |
| `total_value`         | Yes      | Float     | Total monetary value of the cart.         |
| `currency`            | Yes      | String    | Currency in which the cart is valued.           |
| `total_discounts`     | No       | Float     | Total amount of discounts applied to the order.     |
| `discounts`           | No       | Array of objects     | Detailed list of discounts applied to the order.             |
| `products`            | Yes      | Array of objects     |         |
| `product_id`          | Yes      | String    | A unique identifier for the product that was viewed. This value can be the product ID, SKU, or similar.             |
| `product_name`        | Yes      | String    | The name of the product that was viewed.          |
| `variant_id`          | Yes      | String    | A unique identifier for the product variant (such as `shirt_medium_blue`).        |
| `image_url`           | No       | String    | URL of the product image.           |
| `product_url`         | No       | String    | URL to the product page for more details.                                                                     |
| `quantity`            | Yes      | Integer   | Number of units of the product in the cart.        |
| `price`               | Yes      | Float     | The variant unit price of the product at the time of viewing.     |
| `metadata`            | No       | Object    | Additional metadata field about the product that the customer wants to add for their use cases. For Shopify, we will add SKU. This will have a limit based on our general event properties limit of 50kb. |
| `sku`                 | No       | String    | (Shopify only) Shopify SKU. This can be configured as the catalog ID field.        |
| `source`              | Yes      | String    | Source the event is derived from. (For Shopify, this is storefront).    |
| `metadata`            | No       | Object    |       |
| `order_status_url`    | No       | String    | URL to view the status of the order.                                                                          |
| `order_number`        | No       | String    | (Shopify only) Unique order number for the order placed.  |
| `tags`                | No       | Array     | (Shopify only) Order tags.            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Example object

```json
{
    "name": "ecommerce.order_cancelled",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "cancel_reason": "no longer necessary",
        "total_value": 421.88,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
            "order_number": 1234,
            "tags": [
                "heavy",
                "heavy2"
            ]
        }
    }
}
```

{% endtab %}
{% endtabs %}

## eCommerce Canvas templates

Braze has created pre-built Canvas templates that are powered by eCommerce recommended events, such as targeting customers who started the checkout process but left before placing their order. You can use these events to make informed decisions to enhance your user journey by personalizing messaging and targeting specific audiences.

Check out our dedicated [eCommerce use cases]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases) for more ways on how you can use these events with Canvas templates.

## User calculated fields

We use standardized user field calculations for the following fields: 

- **Total Revenue** = sum of total order placed value - sum of total order refunded value
- **Total Orders count** = count of distinct order placed events - count of distinct order cancellations
- **Total Refund Value** = sum of total order refunded value 

These user field calculations are also included on the **Transactions** tab of user profiles.

![The "Transactions" tab with user calcuated fields.]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:60%;"}

{% alert important %}
The plans to phase out the purchase event will be announced in late 2025. In the long run, the purchase event will be replaced by new [eCommerce recommended events]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/), which will come with enhanced features for segmentation, reporting, analytics, and more. However, the new eCommerce events will not support existing features related to the purchase event, such as Lifetime Value (LTV) or revenue reporting in Canvases or campaigns. For a complete list of features related to purchase events, please refer to the section on [Logging purchase events]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}
