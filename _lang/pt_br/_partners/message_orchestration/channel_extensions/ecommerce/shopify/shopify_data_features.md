---
nav_title: ""
article_title: ""
description: ""
page_type: partner
search_tag: Partner
alias: /shopify_data_features/
page_order: 3
---

# 

> 

## 

{% tabs %}
{% tab Exemplo de carga útil %}
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
 "name": "shopify_cancelled_order",
 "time": "2022-05-23T14:40:52-04:00",
 "properties": {
   "order_id": 4444596371647,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143033344191,
       "sku": null,
       "title": "LED High Tops",
       "variant_id": 40094740549876,
       "variant_title": "",
       "vendor": "partners-demo",
       "name": "LED High Tops",
       "properties": [],
       "price": "80.00",
       "fulfillment_status": null
     }
   ],
   "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   ],
   "total_price": "141.54",
   "confirmed": true,
   "total_discounts": "0.00",
   "discount_codes": [],
   "order_number": 1092,
   "order_status_url": "https://test-store.myshopify.com/",
   "cancelled_at": "2022-05-23T14:40:52-04:00",
   "tags": "",
   "closed_at": "2022-05-23T14:40:51-04:00",
   "fulfillment_status": null,
   "fulfillments": []
 },
 "braze_id": "123abc123abc"
}
```
{% endsubtab %}
{% subtab Order refunded %}
```json
{
 "name": "shopify_created_refund",
 "time": "2022-05-23T14:40:50-04:00",
 "properties": {
   "order_id": 4444596371647,
   "note": null,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143033344191,
       "sku": null,
       "title": "LED High Tops",
       "variant_id": 40094740549876,
       "variant_title": "",
       "vendor": "partners-demo",
       "properties": [],
       "price": "80.00"
     },
     {
       "quantity": 1,
       "product_id": 6143032852671,
       "sku": null,
       "title": "Chequered Red Shirt",
       "variant_id": 40094796619876,
       "variant_title": "",
       "vendor": "partners-demo",
       "properties": [],
       "price": "50.00"
     }
   ]
 },
 "braze_id": "abc123abc123"
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

{% subtabs global %}
{% subtab Product viewed %}
**Evento**: `ecommerce.v1.product_viewed`<br>
**Tipo**: <br>
 <br>
 Abandono de navegação

{% raw %}







 <br><br>





{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Cart updated %}
**Evento**: `ecommerce.v1.cart_updated`<br>
**Tipo**: <br>
 <br>
 Abandono de carrinho

 

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} %}
```
{% endraw %}



{% raw %}















{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert tip %}

{% endalert %}

{% endsubtab %}
{% subtab Checkout started %}
**Evento**: `ecommerce.v1.checkout_started`<br>
**Tipo**: <br>
 <br>
 



{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
{{context.${cart_id}}}
```
{% endraw %}



{% raw %}















{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Order placed %}
**Evento**: `ecommerce.v1.order_placed`<br>
**Tipo**: <br>
 <br>
  

{% raw %}

















{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert tip %}
 
{% endalert %}

{% endsubtab %}
{% subtab Fulfilled order %}
**Evento**: `shopify_fulfilled_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events)<br>
 <br>
  

{% raw %}


| ID do pedido | `{{event_properties.${order_id}}}` |
| Preço total | `{{event_properties.${total_price}}}` |
| Descontos totais | `{{event_properties.${total_discounts}}}` |
| Status confirmado | `{{event_properties.${confirmed}}}` |
| URL de status do pedido | `{{event_properties.${order_status_url}}}` |
| Número do pedido | `{{event_properties.${order_number}}}` |
| Cancelamento de registro de data e hora | `{{event_properties.${cancelled_at}}}` |
Fechado | Carimbo de data/hora | `{{event_properties.${closed_at}}}` |
| ID do item | `{{event_properties.${line_items}[0].product_id}}` |
| Quantidade do item | `{{event_properties.${line_items}[0].quantity}}` |
| SKU do item | `{{event_properties.${line_items}[0].sku}}` |
| Título do item | `{{event_properties.${line_items}[0].title}}` |
| Fornecedor do item | `{{event_properties.${line_items}[0].vendor}}` |
| Nome do item | `{{event_properties.${line_items}[0].name}}` |
| Propriedades do item | `{{event_properties.${line_items}[0].properties}}` |
| Preço do item | `{{event_properties.${line_items}[0].price}}` |
| Título da remessa | `{{event_properties.${shipping}[0].title}}` |
| Preço de remessa | `{{event_properties.${shipping}[0].price}}` |
| Status de cumprimento | `{{event_properties.${fulfillment_status}}}` |
| Status do envio do processamento | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Status | `{{event_properties.${fulfillments}[0].status}}` |
| Empresa de rastreamento de cumprimento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| Número de rastreamento do cumprimento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| Números de rastreamento de cumprimento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| URL de rastreamento do processamento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| URLs de rastreamento do processamento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| Status de cumprimento | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Nome do processamento | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Preço do processamento | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| ID do produto de atendimento | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Quantidade do processamento | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Envio do processamento | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| SKU do processamento | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Título do processamento | `{{event_properties.${fulfillments}[0].line_items[0].title}}`
| Fornecedor do processamento | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
| ID da variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Partially fulfilled order %}
**Evento**: `shopify_partially_fulfilled_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events)<br>
 <br> 
  

{% raw %}


| ID do pedido | `{{event_properties.${order_id}}}` |
| Preço total | `{{event_properties.${total_price}}}` |
| Descontos totais | `{{event_properties.${total_discounts}}}` |
| Status confirmado | `{{event_properties.${confirmed}}}` |
| URL de status do pedido | `{{event_properties.${order_status_url}}}` |
| Número do pedido | `{{event_properties.${order_number}}}` |
| Cancelamento de registro de data e hora | `{{event_properties.${cancelled_at}}}` |
Fechado | Carimbo de data/hora | `{{event_properties.${closed_at}}}` |
| ID do item | `{{event_properties.${line_items}[0].product_id}}` |
| Quantidade do item | `{{event_properties.${line_items}[0].quantity}}` |
| SKU do item | `{{event_properties.${line_items}[0].sku}}` |
| Título do item | `{{event_properties.${line_items}[0].title}}` |
| Fornecedor do item | `{{event_properties.${line_items}[0].vendor}}` |
| Nome do item | `{{event_properties.${line_items}[0].name}}` |
| Propriedades do item | `{{event_properties.${line_items}[0].properties}}` |
| Preço do item | `{{event_properties.${line_items}[0].price}}` |
| Título da remessa | `{{event_properties.${shipping}[0].title}}` |
| Preço de remessa | `{{event_properties.${shipping}[0].price}}` |
| Status de cumprimento | `{{event_properties.${fulfillment_status}}}` |
| Status do envio do processamento | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Status de cumprimento | `{{event_properties.${fulfillments}[0].status}}` |
| Empresa de rastreamento de cumprimento | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| Número de rastreamento do cumprimento | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| Números de rastreamento de cumprimento | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| URL de rastreamento do processamento | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| URLs de rastreamento do processamento | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| Status de cumprimento | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Nome do processamento | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Preço do processamento | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| ID do produto de atendimento | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Quantidade do processamento | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Envio do processamento | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| SKU do processamento | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Título do processamento | `{{event_properties.${fulfillments}[0].line_items[0].title}}`
| Fornecedor do processamento | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
| ID da variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Paid order %}
**Evento**: `shopify_paid_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events)<br>
 <br>  
 

{% raw %}


| ID do pedido | `{{event_properties.${order_id}}}` |
| Status confirmado | `{{event_properties.${confirmed}}}` |
| URL de status do pedido | `{{event_properties.${order_status_url}}}` |
| Número do pedido | `{{event_properties.${order_number}}}` |
| Cancelamento de registro de data e hora | `{{event_properties.${cancelled_at}}}` |
| Descontos totais | `{{event_properties.${total_discounts}}}` |
| Preço total | `{{event_properties.${total_price}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Códigos de desconto | `{{event_properties.${discount_codes}}}` |
| ID do item | `{{event_properties.${line_items}[0].product_id}}` |
| Quantidade do item | `{{event_properties.${line_items}[0].quantity}}` |
| SKU do item | `{{event_properties.${line_items}[0].sku}}` |
| Título do item | `{{event_properties.${line_items}[0].title}}` |
| Fornecedor do item | `{{event_properties.${line_items}[0].vendor}}` |
| Propriedades do item | `{{event_properties.${line_items}[0].properties}}` |
| Preço do item | `{{event_properties.${line_items}[0].price}}` |
| Título da remessa | `{{event_properties.${shipping}[0].title}}` |
| Preço de remessa | `{{event_properties.${shipping}[0].price}}` |
| ID da variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Order cancelled %}
**Evento**: `shopify_cancelled_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events)<br>
 <br> 
 

{% raw %}


| ID do pedido | `{{event_properties.${order_id}}}` |
| Preço total | `{{event_properties.${total_price}}}` |
| Descontos totais | `{{event_properties.${total_discounts}}}` |
| Confirmado | `{{event_properties.${confirmed}}}` |
| URL de status do pedido | `{{event_properties.${order_status_url}}}` |
| Número do pedido | `{{event_properties.${order_number}}}` |
| Cancelamento de registro de data e hora | `{{event_properties.${cancelled_at}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Códigos de desconto | `{{event_properties.${discount_codes}}}` |
| Status de cumprimento | `{{event_properties.${fulfillment_status}}}` |
| Cumprimentos | `{{event_properties.${fulfillments}}}` |
| ID do item | `{{event_properties.${line_items}[0].product_id}}` |
| Quantidade do item | `{{event_properties.${line_items}[0].quantity}}` |
| SKU do item | `{{event_properties.${line_items}[0].sku}}` |
| Título do item | `{{event_properties.${line_items}[0].title}}` |
| Fornecedor do item | `{{event_properties.${line_items}[0].vendor}}` |
| Nome do item | `{{event_properties.${line_items}[0].name}}` |
| Propriedades do item | `{{event_properties.${line_items}[0].properties}}` |
| Status de cumprimento | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| Título da remessa | `{{event_properties.${shipping}[0].title}}` |
| Preço de remessa | `{{event_properties.${shipping}[0].price}}` |
| ID da variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}
{% endsubtab %}
{% subtab Order refunded %}
**Evento**: `shopify_order_refunded`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events)<br>
 <br>
 

{% raw %}


| ID do pedido | `{{event_properties.${order_id}}}` |
| Nota de pedido | `{event_properties.${note}}}` |
| ID do item | `{{event_properties.${line_items}[0].product_id}}` |
| Quantidade do item | `{{event_properties.${line_items}[0].quantity}}` |
| SKU do item | `{{event_properties.${line_items}[0].sku}}` |
| Título do item | `{{event_properties.${line_items}[0].title}}` |
| Fornecedor do item | `{{event_properties.${line_items}[0].vendor}}` |
| Nome do item | `{{event_properties.${line_items}[0].name}}` |
| Propriedades do item | `{{event_properties.${line_items}[0].properties}}` |
| Preço do item | `{{event_properties.${line_items}[0].price}}` |
| ID da variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Account login %}

**Evento**: `shopify_account_login`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events)<br>
 <br>
 

{% raw %}



{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert note %}
 
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Atributos personalizados compatíveis com a Shopify
{% tabs local %}
{% tab Exemplo de carga útil %}
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
{% tab Atributos personalizados da Shopify %}
Nome do atributo | Descrição | Nome do atributo | Descrição

| `shopify_total_spent` O valor total que o cliente gastou no histórico de pedidos. |
| `shopify_order_count` | O número de pedidos associados a esse cliente. Os pedidos de teste e arquivados não são considerados. |
| `shopify_last_order_id` | O ID do último pedido do cliente. |
| `shopify_last_order_name` | O nome do último pedido do cliente. Isso está diretamente relacionado ao campo `name` no recurso do pedido. |
| `shopify_zipcode` | O código postal do cliente do endereço padrão. |
| `shopify_province` A província do cliente a partir de seu endereço padrão. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Personalização Liquid

Para adicionar a personalização Liquid aos seus atributos personalizados da Shopify, selecione **\+ Personalização**. Em seguida, selecione **Atributos personalizados** como seu tipo de personalização.

![A seção "Add Personalization" (Adicionar personalização) com o menu suspenso "Attribute" (Atribuição) estendido.]({% image_buster /assets/img/Shopify/add_personalization_2.png %}){: style="max-width:40%;"}

Depois de selecionar seu atributo personalizado, insira um valor padrão e cole o snippet do Liquid na sua mensagem.

![Colar um trecho do Liquid em uma mensagem.]({% image_buster /assets/img/Shopify/copy_liquid_snippet.png %})
{% endtab %}
{% endtabs %}

## Atribuições padrão compatíveis com o Shopify

- E-mail
- Nome
- Sobrenome
- Telefone
- Cidade
- País

{% alert note %}
A Braze só atualizará os atributos personalizados compatíveis da Shopify e os atributos padrão da Braze se houver uma diferença nos dados do perfil do usuário existente. Por exemplo, se os dados de entrada do Shopify contiverem um primeiro nome de Bob e Bob já existir como um primeiro nome no perfil de usuário do Braze, o Braze não disparará uma atualização e não será cobrado um ponto de dados.
{% endalert %}

## coleta de dados do SDK 

 

## Provisionamento de dados históricos

  

### 

1. 



{: start="2"}

2.   



###  

 