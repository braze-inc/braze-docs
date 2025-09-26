---
nav_title: Características de los datos de Shopify
article_title: "Características de los datos de Shopify"
description: "Este artículo de referencia cubre las características de los datos de Shopify."
page_type: partner
search_tag: Partner
alias: /shopify_data_features/
page_order: 3
---

# Características de los datos de Shopify

> Este artículo proporciona una visión general de nuestras características de Shopify, incluyendo qué datos de Shopify son objeto de seguimiento y ejemplos de cargas útiles, backfill histórico y sincronización de productos.

## Seguimiento de eventos de Shopify

{% tabs %}
{% tab Ejemplo de carga útil %}
{% subtabs global %}
{% subtab Product viewed %}
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
        },
        "type": [
          "price_drop",
          "back_in_stock"
        ]
    }
}
```
{% endsubtab %}
{% subtab Cart updated %}
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
{% endsubtab %}
{% subtab Checkout started %}
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
{% endsubtab %}
{% subtab Order placed %}
{% raw %}
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
{% endraw %}
{% endsubtab %}
{% subtab Fulfilled order %}
```json
{
 "name": "shopify_fulfilled_order",
 "time": "2022-05-23T14:44:34-04:00",
 "properties": {
   "order_id": 4444668657855,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143032066239,
       "sku": null,
       "title": "Dark Denim Top",
  "variant_id": 40094740549876,
       "variant_title": "Small Dark Denim Top",


       "vendor": "partners-demo",
       "name": "Dark Denim Top",
       "properties": [],
       "price": "60.00",
       "fulfillment_status": "fulfilled"
     }
   ],
   "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   ],
   "total_price": "130.66",
   "confirmed": true,
   "total_discounts": "0.00",
   "discount_codes": [],
   "order_number": 1093,
   "order_status_url": "https://test-store.myshopify.com/",
   "cancelled_at": null,
   "tags": "",
   "closed_at": "2022-05-23T14:44:34-04:00",
   "fulfillment_status": "fulfilled",
   "fulfillments": [
     {
       "shipment_status": null,
       "status": "success",
       "tracking_company": "Other",
       "tracking_number": "456",
       "tracking_numbers": [
         "456"
       ],
       "tracking_url": "https://braze.com",
       "tracking_urls": [
         "https://braze.com"
       ],
       "line_items": [
         {
           "fulfillment_status": "fulfilled",
           "name": "Dark Denim Top",
           "price": "60.00",
           "product_id": 6143032066239,
           "quantity": 1,
           "requires_shipping": true,
           "sku": null,
           "title": "Dark Denim Top",
           "variant_id": 40094740549876,
           "variant_title": "Small Dark Denim Top",
           "vendor": "partners-demo"
         }
       ]
     }
   ]
 },
 "braze_id": "123abc123abc"
}
```
{% endsubtab %}
{% subtab Partially fulfilled order %}
```json
{
 "name": "shopify_partially_fulfilled_order",
 "time": "2022-05-23T14:43:34-04:00",
 "properties": {
   "order_id": 4444668657855,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143032066239,
       "sku": null,
       "title": "Dark Denim Top",
       "variant_id": 40094740549876,
       "variant_title": "",
       "vendor": "partners-demo",
       "name": "Dark Denim Top",
       "properties": [],
       "price": "60.00",
       "fulfillment_status": "fulfilled"
     }
   ],
   "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   ],
   "total_price": "130.66",
   "confirmed": true,
   "total_discounts": "0.00",
   "discount_codes": [],
   "order_number": 1093,
   "order_status_url": "https://test-store.myshopify.com/",
   "cancelled_at": null,
   "tags": "",
   "closed_at": null,
   "fulfillment_status": "partial",
   "fulfillments": [
     {
       "shipment_status": null,
       "status": "success",
       "tracking_company": "Other",
       "tracking_number": "123",
       "tracking_numbers": [
         "123"
       ],
       "tracking_url": "https://braze.com",
       "tracking_urls": [
         "https://braze.com"
       ],
       "line_items": [
         {
           "fulfillment_status": "fulfilled",
           "name": "Dark Denim Top",
           "price": "60.00",
           "product_id": 6143032066239,
           "properties": [],
           "quantity": 1,
           "requires_shipping": true,
           "sku": null,
           "title": "Dark Denim Top",
           "variant_id": 40094740549876,
           "variant_title": "",
           "vendor": "partners-demo"
         }
       ]
     }
   ]
 },
 "braze_id": "abc123abc123"
}
```
{% endsubtab %}
{% subtab Paid order %}
```json
{
 "name": "shopify_paid_order",
 "time": "2022-05-23T13:52:38-04:00",
 "properties": {
   "order_id": 4444596371647,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143033344191,
       "sku": null,
       "title": "LED High Tops",
       "variant_id": 40094740549876,
       "variant_title": null,
       "vendor": "partners-demo",
       "name": "LED High Tops",
       "properties": [],
       "price": "80.00",
       "fulfillment_status": null
     }
   ],
 }
}
```
{% endsubtab %}
{% subtab Order cancelled %}
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
{% endsubtab %}
{% subtab Order refunded %}
```json
{
    "name": "ecommerce.order_refunded",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
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
        "metadata": {
		"order_note": "item was broken"
        }
    }
} 
```
{% endsubtab %}
{% subtab Account login %}
```json
{
	name: "shopify_account_login",
	properties: {
	source: "braze-mock-storefront.myshopify.com"
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Eventos Shopify %}
{% subtabs global %}
{% subtab Product viewed %}
**Evento**: `ecommerce.product_viewed`<br>
**Tipo**: Evento recomendado<br>
**Desencadenado**: Cuando un cliente ve una página de producto<br>
**Casos de uso**: Abandono de la navegación

{% raw %}
| Variable | Liquid plantilla |
| --- | --- |
\|------------------|-----------------------------------------------------|
| `product_id` | `{{event_properties.${product_id}}}` |
| `product_name ` | `{{event_properties.${product_name}}}` |
| `variant_id` | `{{event_properties.${variant_id}}}` |
| `image_url ` | `{{event_properties.${image_url}}}` |
| `product_url` | `<your-store.myshopify.com>{{event_properties.${product_url}}}` <br><br>Añade el dominio de tu sitio Shopify antes de la URL. |
| `price` | `{{event_properties.${price}}}` |
| `currency` | `{{event_properties.${currency}}}` |
| `source` | `{{event_properties.${source}}}` |
| `sku` | `{{event_properties.${metadata}[0].sku}}` |
| `type` | `event_properties.${type}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Cart updated %}
**Evento**: `ecommerce.cart_updated`<br>
**Tipo**: Evento recomendado<br>
**Desencadenado**: Cuando un cliente añade, elimina o actualiza su cesta de la compra<br>
**Casos de uso**: Abandono del carro

Para los lienzos de Carrito Abandonado, primero tienes que añadir la etiqueta de Liquid inicial del carrito de la compra para obtener el contexto del carrito en tu mensaje. 

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} %}
```
{% endraw %}

A continuación, puedes añadir las siguientes etiquetas de Liquid en tu mensaje.

{% raw %}
| Variable | Liquid plantilla |
\|------------------|-----------------------------------------------------|
| `cart_id` | `{{ shopping_cart.cart_id }}` |
| `currency` | `{{ shopping_cart.currency }}` |
| `total_value` | `{{ shopping_cart.total_value }}` |
| `product_id` | `{{ shopping_cart.products[0].product_id }}` |
| `product_name` | `{{ shopping_cart.products[0].product_name }}` |
| `variant_id` | `{{ shopping_cart.products[0].variant_id }}` |
| `image_url` | `{{ shopping_cart.products[0].image_url }}` |
| `product_url` | `{{ shopping_cart.products[0].product_url }}` |
| `quantity` | `{{ shopping_cart.products[0].quantity }}` |
| `price` | `{{ shopping_cart.products[0].price }}` |
| `sku` | `{{ shopping_cart.products[0].metadata[0].sku }}` |
| `source` | `{{ shopping_cart.source }}` |
| `metadata (value)` | `{{ shopping_cart.metadata[0].<add_value_here> }}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert tip %}
Para más información sobre cómo crear un bucle Liquid `for` para añadir dinámicamente todos los productos a tu correo electrónico, consulta [Personalización de productos de carritos abandonados para correos electrónicos]({{site.baseurl}}/ecommerce_use_cases/#abandoned-cart).
{% endalert %}

{% endsubtab %}
{% subtab Checkout started %}
**Evento**: `ecommerce.checkout_started`<br>
**Tipo**: Evento recomendado<br>
**Desencadenado**: Cuando un cliente añade, elimina o actualiza su cesta de la compra<br>
**Casos de uso**: Abandono de la compra

Para los Lienzos de Pago Abandonado, primero tienes que utilizar la siguiente etiqueta de Liquid:

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
{{context.${cart_id}}}
```
{% endraw %}

A continuación, puedes añadir las siguientes etiquetas de Liquid en tu mensaje para hacer referencia a los productos de tu cesta en el momento de pagar.

{% raw %}
| Variable | Liquid plantilla |
\|------------------|-----------------------------------------------------|
| `cart_id` | `{{ shopping_cart.cart_id }}` |
| `currency` | `{{ shopping_cart.currency }}` |
| `total_value` | `{{ shopping_cart.total_value }}` |
| `product_id` | `{{ shopping_cart.products[0].product_id }}` |
| `product_name` | `{{ shopping_cart.products[0].product_name }}` |
| `variant_id` | `{{ shopping_cart.products[0].variant_id }}` |
| `image_url` | `{{ shopping_cart.products[0].image_url }}` |
| `product_url` | `{{ shopping_cart.products[0].product_url }}` |
| `quantity` | `{{ shopping_cart.products[0].quantity }}` |
| `price` | `{{ shopping_cart.products[0].price }}` |
| `sku` | `{{ shopping_cart.products[0].metadata.sku }}` |
| `source` | `{{ shopping_cart.source }}` |
| `checkout_url` | `{{ shopping_cart.metadata[0].checkout_url }}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Order placed %}
**Evento**: `ecommerce.order_placed`<br>
**Tipo**: Evento recomendado<br>
**Desencadenado**: Cuando un usuario completa con éxito el proceso de pago y realiza un pedido<br>
**Casos de uso**: Confirmación de pedidos, reorientación posterior a la compra, upsells o ventas cruzadas 

{% raw %}
| Variable | Liquid plantilla |
\|-------------------------|-----------------------------------------------------|
| cart_id | `{{event_properties.${cart_id}}}` |
| moneda | `{{event_properties.${currency}}}` |
| descuentos | `{{event_properties.${discounts}}}` |
| order_id | `{{event_properties.${order_id}}}` |
| product_id | `{{event_properties.${products}[0].product_id}}` |
| nombre_producto | `{{event_properties.${products}[0].product_name}}` |
| variant_id | `{{event_properties.${products}[0].variant_id}}` |
| cantidad | `{{event_properties.${products}[0].quantity}}` |
| sku | `{{event_properties.${products}[0].metadata.sku}}` |
| total_descuentos | `{{event_properties.${total_discounts}}}` |
| order_status_url | `{{event_properties.${metadata}.order_status_url}}` |
| número_de_pedido | `{{event_properties.${metadata}.order_number}}` |
| etiquetas | `{{event_properties.${metadata}.tags}}` |
| sitio_referente | `{{event_properties.${metadata}.referring_site}}` |
| payment_gateway_names | `{{event_properties.${metadata}.payment_gateway_names}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert tip %}
El webhook de pago completado de Shopify no contiene URL de productos ni URL de imágenes. Como resultado, tienes que utilizar la personalización de Catálogos Liquid, como se menciona en [Personalización de productos de carritos abandonados para correos electrónicos]({{site.baseurl}}/ecommerce_use_cases/#order-confirmation-and-feedback-survey).
{% endalert %}

{% endsubtab %}
{% subtab Fulfilled order %}
**Evento**: `shopify_fulfilled_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**Desencadenado**: Cuando el pedido de un usuario se ha completado y está listo para su envío<br>
**Casos de uso**: (Transaccional) Actualización de cumplimiento 

{% raw %}
| Variable | Liquid plantilla |
| --- | --- |
| ID de pedido | `{{event_properties.${order_id}}}` |
| Precio total | `{{event_properties.${total_price}}}` |
| Descuentos totales | `{{event_properties.${total_discounts}}}` |
| Estado confirmado | `{{event_properties.${confirmed}}}` |
| URL del estado del pedido | `{{event_properties.${order_status_url}}}` |
| Número de pedido | `{{event_properties.${order_number}}}` |
| Marca de tiempo Cancelado | `{{event_properties.${cancelled_at}}}` |
| Hora de cierre | `{{event_properties.${closed_at}}}` |
| ID del artículo | `{{event_properties.${line_items}[0].product_id}}` |
| Cantidad de artículos | `{{event_properties.${line_items}[0].quantity}}` |
| SKU del artículo | `{{event_properties.${line_items}[0].sku}}` |
| Título del artículo | `{{event_properties.${line_items}[0].title}}` |
| Vendedor del artículo | `{{event_properties.${line_items}[0].vendor}}` |
| Nombre del artículo | `{{event_properties.${line_items}[0].name}}` |
| Propiedades del artículo | `{{event_properties.${line_items}[0].properties}}` |
| Precio del artículo | `{{event_properties.${line_items}[0].price}}` |
| Título del envío | `{{event_properties.${shipping}[0].title}}` |
| Precio de envío | `{{event_properties.${shipping}[0].price}}` |
| Estado de cumplimiento | `{{event_properties.${fulfillment_status}}}` |
| Estado del envío | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Estado | `{{event_properties.${fulfillments}[0].status}}` |
| Empresa de Seguimiento de Envíos | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| Número de seguimiento de cumplimiento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| Números de seguimiento de cumplimiento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| URL de seguimiento de cumplimiento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| URL de seguimiento de cumplimiento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| Estado de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Nombre de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Precio de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Cumplimiento ID del producto | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Cantidad de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Envíos de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Cumplimiento SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Título de Cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Proveedor de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Partially fulfilled order %}
**Evento**: `shopify_partially_fulfilled_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**Desencadenado**: Cuando parte del pedido de un usuario se ha completado y está listo para su envío<br> 
**Casos de uso**: (Transaccional) Actualización de cumplimiento 

{% raw %}
| Variable | Liquid plantilla |
| --- | --- |
| ID de pedido | `{{event_properties.${order_id}}}` |
| Precio total | `{{event_properties.${total_price}}}` |
| Descuentos totales | `{{event_properties.${total_discounts}}}` |
| Estado confirmado | `{{event_properties.${confirmed}}}` |
| URL del estado del pedido | `{{event_properties.${order_status_url}}}` |
| Número de pedido | `{{event_properties.${order_number}}}` |
| Marca de tiempo Cancelado | `{{event_properties.${cancelled_at}}}` |
| Hora de cierre | `{{event_properties.${closed_at}}}` |
| ID del artículo | `{{event_properties.${line_items}[0].product_id}}` |
| Cantidad de artículos | `{{event_properties.${line_items}[0].quantity}}` |
| SKU del artículo | `{{event_properties.${line_items}[0].sku}}` |
| Título del artículo | `{{event_properties.${line_items}[0].title}}` |
| Vendedor del artículo | `{{event_properties.${line_items}[0].vendor}}` |
| Nombre del artículo | `{{event_properties.${line_items}[0].name}}` |
| Propiedades del artículo | `{{event_properties.${line_items}[0].properties}}` |
| Precio del artículo | `{{event_properties.${line_items}[0].price}}` |
| Título del envío | `{{event_properties.${shipping}[0].title}}` |
| Precio de envío | `{{event_properties.${shipping}[0].price}}` |
| Estado de cumplimiento | `{{event_properties.${fulfillment_status}}}` |
| Estado del envío | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Estado de cumplimiento | `{{event_properties.${fulfillments}[0].status}}` |
| Empresa de Seguimiento de Envíos | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| Número de seguimiento de cumplimiento | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| Números de seguimiento de cumplimiento | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| URL de seguimiento de cumplimiento | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| URL de seguimiento de cumplimiento | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| Estado de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Nombre de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Precio de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Cumplimiento ID del producto | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Cantidad de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Envíos de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Cumplimiento SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Título de Cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Proveedor de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Paid order %}
**Evento**: `shopify_paid_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**Desencadenado**: Cuando el pedido de un usuario se marca como pagado dentro de Shopify<br>  
**Casos de uso**: (Transaccional) Confirmación de pago

{% raw %}
| Variable | Liquid plantilla |
| --- | --- |
| ID de pedido | `{{event_properties.${order_id}}}` |
| Estado confirmado | `{{event_properties.${confirmed}}}` |
| URL del estado del pedido | `{{event_properties.${order_status_url}}}` |
| Número de pedido | `{{event_properties.${order_number}}}` |
| Marca de tiempo Cancelado | `{{event_properties.${cancelled_at}}}` |
| Descuentos totales | `{{event_properties.${total_discounts}}}` |
| Precio total | `{{event_properties.${total_price}}}` |
| Etiquetas | `{{event_properties.${tags}}}` |
| Códigos de descuento | `{{event_properties.${discount_codes}}}` |
| ID del artículo | `{{event_properties.${line_items}[0].product_id}}` |
| Cantidad de artículos | `{{event_properties.${line_items}[0].quantity}}` |
| SKU del artículo | `{{event_properties.${line_items}[0].sku}}` |
| Título del artículo | `{{event_properties.${line_items}[0].title}}` |
| Vendedor del artículo | `{{event_properties.${line_items}[0].vendor}}` |
| Propiedades del artículo | `{{event_properties.${line_items}[0].properties}}` |
| Precio del artículo | `{{event_properties.${line_items}[0].price}}` |
| Título del envío | `{{event_properties.${shipping}[0].title}}` |
| Precio de envío | `{{event_properties.${shipping}[0].price}}` |
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Order cancelled %}
**Evento**: `shopify_cancelled_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**Desencadenado**: Cuando se cancela el pedido de un usuario<br> 
**Casos de uso**: (Transaccional) Confirmación de cancelación de pedido

{% raw %}
| Variable | Liquid plantilla |
| --- | --- |
| ID de pedido | `{{event_properties.${order_id}}}` |
| Precio total | `{{event_properties.${total_price}}}` |
| Descuentos totales | `{{event_properties.${total_discounts}}}` |
| Confirmado | `{{event_properties.${confirmed}}}` |
| URL del estado del pedido | `{{event_properties.${order_status_url}}}` |
| Número de pedido | `{{event_properties.${order_number}}}` |
| Marca de tiempo Cancelado | `{{event_properties.${cancelled_at}}}` |
| Etiquetas | `{{event_properties.${tags}}}` |
| Códigos de descuento | `{{event_properties.${discount_codes}}}` |
| Estado de cumplimiento | `{{event_properties.${fulfillment_status}}}` |
| Cumplimientos | `{{event_properties.${fulfillments}}}` |
| ID del artículo | `{{event_properties.${line_items}[0].product_id}}` |
| Cantidad de artículos | `{{event_properties.${line_items}[0].quantity}}` |
| SKU del artículo | `{{event_properties.${line_items}[0].sku}}` |
| Título del artículo | `{{event_properties.${line_items}[0].title}}` |
| Vendedor del artículo | `{{event_properties.${line_items}[0].vendor}}` |
| Nombre del artículo | `{{event_properties.${line_items}[0].name}}` |
| Propiedades del artículo | `{{event_properties.${line_items}[0].properties}}` |
| Estado de cumplimiento | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| Título del envío | `{{event_properties.${shipping}[0].title}}` |
| Precio de envío | `{{event_properties.${shipping}[0].price}}` |
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}
{% endsubtab %}
{% subtab Order refunded %}
**Evento**: `shopify_order_refunded`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**Desencadenado**: Cuando se reembolsa el pedido de un usuario<br>
**Casos de uso**: (Transacción) Confirmación de reembolso

{% raw %}
| Variable | Liquid plantilla |
| --- | --- |
| ID de pedido | `{{event_properties.${order_id}}}` |
| Nota de pedido | `{event_properties.${note}}}` |
| ID del artículo | `{{event_properties.${line_items}[0].product_id}}` |
| Cantidad de artículos | `{{event_properties.${line_items}[0].quantity}}` |
| SKU del artículo | `{{event_properties.${line_items}[0].sku}}` |
| Título del artículo | `{{event_properties.${line_items}[0].title}}` |
| Vendedor del artículo | `{{event_properties.${line_items}[0].vendor}}` |
| Nombre del artículo | `{{event_properties.${line_items}[0].name}}` |
| Propiedades del artículo | `{{event_properties.${line_items}[0].properties}}` |
| Precio del artículo | `{{event_properties.${line_items}[0].price}}` |
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Account login %}

**Evento**: `shopify_account_login`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**Desencadenado**: Cuando un usuario se conecta a su cuenta<br>
**Casos de uso**: Series de bienvenida

{% raw %}
| Variable | Liquid plantilla |
| --- | --- |
| `source` | {{event_properties.${source}}} |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert note %}
Actualmente, la integración de Shopify no permite rellenar el [evento de compra]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-events) Braze. Como resultado, los filtros de compra, las etiquetas de Liquid, los desencadenantes basados en acciones y los análisis deben utilizar el evento ecommerce.order_placed.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Atributos personalizados de Shopify compatibles
{% tabs local %}
{% tab Ejemplo de carga útil %}
{% subtabs %}
{% subtab Shopify Tags %}
```json
{
  "attributes": [
    {
      "shopify_tags": "VIP_customer",
      "shopify_total_spent": "60.00",
      "shopify_order_count": "3",
      "shopify_last_order_id": "1234567",
      "shopify_last_order_name": "test_order",
      "shopify_zipcode": "10001",
      "shopify_province": "null"
    }
  ]
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Atributos personalizados de Shopify %}
| Nombre del atributo Descripción
| --- | --- |
| `shopify_total_spent` | La cantidad total de dinero que el cliente ha gastado en su historial de pedidos. |
| `shopify_order_count` | El número de pedidos asociados a este cliente. No se cuentan los pedidos de prueba ni los archivados. |
| `shopify_last_order_id` | El ID del último pedido del cliente. |
| `shopify_last_order_name` | El nombre del último pedido del cliente. Esto está directamente relacionado con el campo `name` del recurso pedido. |
| `shopify_zipcode` | El código postal del cliente a partir de su dirección predeterminada. |
| `shopify_province` | La provincia del cliente a partir de su dirección predeterminada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Personalización de Liquid

Para añadir personalización Liquid a tus atributos personalizados de Shopify, selecciona **\+ Personalización**. A continuación, selecciona **Atributos personalizados** como tipo de personalización.

![La sección "Añadir personalización" con el desplegable "Atributo" ampliado.]({% image_buster /assets/img/Shopify/add_personalization_2.png %}){: style="max-width:40%;"}

Tras seleccionar tu atributo personalizado, introduce un valor predeterminado y copia el fragmento de código Liquid en tu mensaje.

![Pegar un fragmento de código Liquid en un mensaje.]({% image_buster /assets/img/Shopify/copy_liquid_snippet.png %})
{% endtab %}
{% endtabs %}

## Atributos estándar de Shopify compatibles

- Correo electrónico
- Nombre
- Apellido
- Teléfono
- Localidad
- País

{% alert note %}
Braze sólo actualizará los atributos personalizados de Shopify y los atributos estándar de Braze admitidos si hay una diferencia en los datos del perfil de usuario existente. Por ejemplo, si los datos entrantes de Shopify contienen un nombre de pila de Bob y Bob ya existe como nombre de pila en el perfil de usuario de Braze, Braze no desencadenará una actualización y no se te cobrará un punto de datos.
{% endalert %}

## Recopilación de datos del SDK 

Para más información sobre qué datos recopilan los SDK de Braze, consulta [Recopilación de datos de SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/). 

## Relleno histórico

Durante la incorporación a tu tienda Shopify, puedes iniciar una sincronización inicial de datos a través del backfill histórico para interactuar inmediatamente con tus clientes. Como parte de este backfill, Braze ejecutará una sincronización inicial de datos de todos los clientes y pedidos realizados en los últimos 90 días antes de tu conexión de integración con Shopify. Cuando Braze importe tus clientes de Shopify, les asignaremos el tipo `external_id` que hayas elegido en tus ajustes de configuración.

{% alert note %}
Si planeas realizar la integración con un ID externo personalizado (ya sea para la [integración estándar]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-4-configure-how-you-manage-users) o para la [integración personalizada]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/#step-6-configure-how-you-manage-users-optional)), deberás añadir tu ID externo personalizado como metacampo de cliente de Shopify a todos los perfiles de cliente de Shopify existentes y, a continuación, realizar el relleno histórico.
{% endalert %}

### Configuración del relleno histórico de Shopify

1. Activa el relleno histórico en el paso **Seguimiento de datos de Shopify**.

![El paso "Seguimiento de los datos de Shopify" de la integración de Shopify muestra el relleno histórico seleccionado.]({% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %})

{: start="2"}

2. Después de completar la configuración de tu integración, Braze comenzará la sincronización inicial de datos. Puedes controlar el progreso en la pestaña **Datos de Shopify** de tu configuración de integración. 

![La página de configuración de la integración de Shopify con una rueda giratoria que muestra que los eventos se están sincronizando activamente.]({% image_buster /assets/img/Shopify/historical_data_backfill_syncing.png %})

### Datos sincronizados 

Para la sincronización inicial de datos, Braze importará los clientes y pedidos realizados de los últimos 90 días anteriores a tu conexión de integración con Shopify. Cuando Braze importe tus clientes de Shopify, les asignará el tipo `external_id` que hayas elegido en tus ajustes de configuración.