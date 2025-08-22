---
nav_title: Dados do Shopify no Braze
article_title: "Usando dados do Shopify no Braze"
description: "Este artigo de referência descreve como usar os dados da Shopify na Braze para personalização e segmentação."
page_type: partner
search_tag: Partner
alias: "/shopify_data_legacy/"
page_order: 1
---

# Dados do Shopify no Braze

> Usando o suporte de objetos aninhados para eventos personalizados, os clientes do Braze Shopify podem usar variáveis de modelo Liquid das propriedades de eventos aninhados.

Depois que a instalação do app for concluída, o Braze criará automaticamente seu webhook e a integração do ScriptTag com o Shopify. Consulte a tabela a seguir para obter mais detalhes sobre como os eventos suportados do Shopify são mapeados para os eventos personalizados e atributos personalizados do Braze.

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

## Eventos compatíveis com a Shopify

{% tabs %}
{% tab Eventos da Shopify %}
{% subtabs global %}
{% subtab Product Viewed %}
**Evento**: `shopify_product_viewed`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variável | Modelagem Liquid | Variável
| --- | --- |
| ID do item | `{{event_properties.${id}}}` |
| Título do item | `{{event_properties.${title}}}` |
| Preço do item | `{{event_properties.${price}}}` |
| Fornecedor do item | `{{event_properties.${vendor}}}` |
| Imagens do item | `{{event_properties.${images}}}` |


{% endraw %}
{% endsubtab %}


{% subtab Product Clicked %}
**Evento**: `shopify_product_clicked`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variável | Modelagem Liquid | Variável
| --- | --- |
| ID do item | `{{event_properties.${id}}}` |
| Título do item | `{{event_properties.${title}}}` |
| Preço do item | `{{event_properties.${price}}}` |
| Fornecedor do item | `{{event_properties.${vendor}}}` |
| Imagens do item | `{{event_properties.${images}}}` |
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Cart %}
**Evento**: `shopify_abandoned_cart`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variável | Modelagem Liquid | Variável
| --- | --- |
| ID do Cartão | `{{event_properties.${cart_id}}}` |
| ID do item | `{{event_properties.${line_items}[0].product_id}}` |
| Quantidade do item | `{{event_properties.${line_items}[0].quantity}}` |
| SKU do item | `{{event_properties.${line_items}[0].sku}}` |
| Título do item | `{{event_properties.${line_items}[0].title}}` |
| Fornecedor do item | `{{event_properties.${line_items}[0].vendor}}` |
| Propriedades do item | `{{event_properties.${line_items}[0].properties}}` |
| Preço do item | `{{event_properties.${line_items}[0].price}}` |
| ID da variante | `{{event_properties.${line_items}[0].variant_id}}` |
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Checkout %}
**Evento**: `shopify_abandoned_checkout`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variável | Modelagem Liquid | Variável
| --- | --- |
| ID do checkout | `{{event_properties.${checkout_id}}}` |
| URL de carrinho abandonado `{{event_properties.${abandoned_checkout_url}}}`
| Código de desconto | `{{event_properties.${discount_code}}}` |
| Preço total | `{{event_properties.${total_price}}}` |
| Valor do desconto | `{{event_properties.${applied_discount}[0].amount}}` |
| Título do desconto | `{{event_properties.${applied_discount}[0].title}}` |
| Descrição do desconto | `{{event_properties.${applied_discount}[0].description}}` |
| ID do item | `{{event_properties.${line_items}[0].product_id}}` |
| Quantidade do item | `{{event_properties.${line_items}[0].quantity}}` |
| SKU do item | `{{event_properties.${line_items}[0].sku}}` |
| Título do item | `{{event_properties.${line_items}[0].title}}` |
| Fornecedor do item | `{{event_properties.${line_items}[0].vendor}}` |
| Propriedades do item | `{{event_properties.${line_items}[0].properties}}` |
| Preço do item | `{{event_properties.${line_items}[0].price}}` |
| ID da variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título variante | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Created Order %}


**Evento**: `shopify_created_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)

{% raw %}
| Variável | Modelagem Liquid | Variável
| --- | --- |
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
| ID da variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título variante | `{{event_properties.${line_items}[0].variant_title}}` |
| Título da remessa | `{{event_properties.${shipping}[0].title}}` |
| Preço de remessa | `{{event_properties.${shipping}[0].price}}` |
|Shopify Store | `{{event_properties.${shopify_storefront}}}` |
| Status do processamento | `{{event_properties.${fulfillment_status}}}` |
| Site de referência | `{{event_properties.${referring_site}}}` |
| Nomes de gateway de pagamento | `{{event_properties.${payment_gateway_names}}}` |
| Endereço de entrega Linha 1 | `{{event_properties.${shipping_address[0].address1}}}` |
| Endereço de entrega Linha 2 | `{{event_properties.${shipping_address[0].address2}}}` |
| Cidade do endereço de entrega | `{{event_properties.${shipping_address[0].city}}}` |
| Endereço de entrega País | `{{event_properties.${shipping_address[0].country}}}` |
| Endereço de entrega Nome | `{{event_properties.${shipping_address[0].first_name}}}` |
| Endereço de entrega Sobrenome | `{{event_properties.${shipping_address[0].last_name}}}` | Endereço de entrega
| Endereço de entrega Província | `{{event_properties.${shipping_address[0].province}}}` |
| Endereço de entrega CEP | `{{event_properties.${shipping_address[0].zip}}}` |
| Endereço de cobrança LINE 1 | `{{event_properties.${billing_address[0].address1}}}` |
| Endereço de cobrança LINE 2 | `{{event_properties.${billing_address[0].address2}}}` |
| Cidade do endereço de cobrança | `{{event_properties.${billing_address[0].city}}}` |
| País do endereço de cobrança | `{{event_properties.${billing_address[0].country}}}` |
| Endereço de cobrança Nome | `{{event_properties.${billing_address[0].first_name}}}` | Endereço de cobrança
| Endereço de cobrança Sobrenome | `{{event_properties.${shipping_address[0].last_name}}}` | Endereço de cobrança
| Endereço de cobrança Província | `{{event_properties.${billing_address[0].province}}}` |
| Endereço de cobrança CEP | `{{event_properties.${billing_address[0].zip}}}` |
{% endraw %}


{% endsubtab %}
{% subtab Purchase %}


**Evento**: Compra<br>
**Tipo**: [Evento de compra da Braze]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/)


{% raw %}
| Variável | Modelagem Liquid | Variável
| --- | --- |
| SKU do item | `{{event_properties.${line_items}[0].sku}}` |
| Título do item | `{{event_properties.${line_items}[0].title}}` |
| Fornecedor do item | `{{event_properties.${line_items}[0].vendor}}` |
| Propriedades do item | `{{event_properties.${line_items}[0].properties}}` |
| ID da variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título variante | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}


{% endsubtab %}
{% subtab Paid Order %}
**Evento**: `shopify_paid_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variável | Modelagem Liquid | Variável
| --- | --- |
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
{% endraw %}
{% endsubtab %}


{% subtab Partially Fulfilled Order %}
**Evento**: `shopify_partially_fulfilled_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variável | Modelagem Liquid | Variável
| --- | --- |
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
{% endraw %}
{% endsubtab %}


{% subtab Fulfilled Order %}
**Evento**: `shopify_fulfilled_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variável | Modelagem Liquid | Variável
| --- | --- |
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
{% endraw %}
{% endsubtab %}


{% subtab Cancelled Order %}
**Evento**: `shopify_cancelled_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variável | Modelagem Liquid | Variável
| --- | --- |
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
{% endraw %}
{% endsubtab %}

{% subtab Created Refund %}
**Evento**: `shopify_created_refund`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variável | Modelagem Liquid | Variável
| --- | --- |
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
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Exemplo de carga útil %}
{% subtabs global %}
{% subtab Product Viewed %}
```json
{
 "name": "shopify_product_viewed",
 "properties": {
     "id": 5971657097407,
     "title": "Example T-Shirt",
     "price": 1999,
     "vendor": "Acme",
     "images": [
         "//cdn.shopify.com/s/files/1/0503/3849/6703/products/green-t-shirt.jpg?v=1603397913"
     ]
 }
}
```
{% endsubtab %}
{% subtab Product Clicked %}
```json
{
   "name": "shopify_product_clicked",
   "properties": {
       "id": 5971657097407,
       "title": "Example T-Shirt",
       "price": 1999,
       "vendor": "Acme",
       "images": [
           "//cdn.shopify.com/s/files/1/0503/3849/6703/products/green-t-shirt.jpg?v=1603397913"
       ]
   }
}
```
{% endsubtab %}
{% subtab Abandoned Cart %}
```json
{
   "name": "shopify_abandoned_cart",
   "time": "2022-10-14T15:08:31.571Z",
   "properties": {
     "cart_id": "163989958f6b0de13f3b4f702fa5ee0d",
     "line_items": [
       {
         "price": 60,
         "product_id": 7110622675033,
         "properties": null,
         "quantity": 1,
         "sku": null,
         "title": "Spinach Surprise Smoothie - 12 Pack",
         "variant_id": 40094740545625,
         "vendor": "Jennifer's Juice"
       }
     ]
   },
   "braze_id": "63497b3ca3eabd0053380451"
 }

```
{% endsubtab %}
{% subtab Abandoned Checkout %}
```json
{
 "name": "shopify_abandoned_checkout",
 "time": "2020-09-10T18:53:37-04:00",
 "properties": {
   "discount_code": "30_DOLLARS_OFF",
   "total_price": "398.00",
   "line_items": [
     {
   "price": "199.00",
   "properties": {},       
   "product_id": 632910392,
       "quantity": 1,
       "sku": "IPOD2008PINK",
       "title": "IPodNano-8GB",
       "variant_id": 40094740545625,
       "variant_title": "Pink iPod Nano 8 GB",
       "vendor": "Apple",
     }
   ],
   "abandoned_checkout_url": "https://checkout.local/690933842/checkouts/123123123/recover?key=example-secret-token",
   "checkout_id": "123123123"
 }
}
```
{% endsubtab %}
{% subtab Created Order %}
```json
{
 "name": "shopify_created_order",
 "time": "2020-09-10T18:53:45-04:00",
 "properties": {
   "total_discounts": "5.00",
   "total_price": "403.00",
   "discount_codes": [],
   "line_items": [
     {
       "product_id": 632910392,
       "quantity": 1,
       "sku": "IPOD2008PINK",
       "title": "IPodNano-8GB",
       "variant_id": 40094740545625,
       "variant_title": "Pink iPod Nano 8 GB",
       "vendor": null,
       "name": "IPodNano-8GB",
       "properties": [],
       "price": "199.00"
     },
     {
       "product_id": 632910393,
       "quantity": 1,
       "sku": "IPOD2008SILVER",
       "title": "IPodNano-8GB",
       "variant_id": 40094740545626,
       "variant_title": "Silver iPod Nano 8 GB",
       "vendor": null,
       "name": "IPodNano-8GB",
       "properties": [],
       "price": "199.00"
     }
   ],
   "order_id": 820982911946154500,
   "confirmed": false,
   "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
   "order_number": 1234,
   "cancelled_at": "2020-09-10T18:53:45-04:00",
   "shipping": [
     {
       "title": "Standard",
       "price": "10.00"
     },
     {
       "title": "Expedited",
       "price": "25.00"
     }
   ],
   "tags": "heavy"
 }
}
```
{% endsubtab %}
{% subtab Purchase %}
```json
{
 "product_id": 632910392,
 "currency": "USD",
 "price": "199.00",
 "time": "2020-09-10T18:53:45-04:00",
 "quantity": 1,
 "source": "shopify",
 "properties": {
   "name": "IPodNano-8GB",
   "sku": "IPOD2008PINK",
   "variant_id": 40094740545626,
   "variant_title": "Silver iPod Nano 8 GB",
   "vendor": null,
   "properties": []
 }
}
```
{% endsubtab %}
{% subtab Paid Order %}
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
{% subtab Partially Fulfilled Order %}
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
{% subtab Fulfilled Order %}
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
{% subtab Cancelled Order %}
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
{% subtab Created Refund %}
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
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Atributos personalizados compatíveis com a Shopify
{% tabs local %}
{% tab Atributos personalizados da Shopify %}
Nome do atributo | Descrição | Nome do atributo | Descrição
| --- | --- |
| `shopify_tags` | Tags que o proprietário da loja anexou ao cliente, formatadas como uma string de valores separados por vírgulas. Um cliente pode ter até 250 tags. Cada tag pode ter até 255 caracteres. |
| `shopify_total_spent` O valor total que o cliente gastou no histórico de pedidos. |
| `shopify_order_count` | O número de pedidos associados a esse cliente. Os pedidos de teste e arquivados não são considerados. |
| `shopify_last_order_id` | O ID do último pedido do cliente. |
| `shopify_last_order_name` | O nome do último pedido do cliente. Isso está diretamente relacionado ao campo `name` no recurso do pedido. |
| `shopify_zipcode` | O código postal do cliente do endereço padrão. |
| `shopify_province` A província do cliente a partir de seu endereço padrão. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Personalização Liquid

Para adicionar a personalização Liquid aos seus atributos personalizados da Shopify, selecione **\+ Personalização**. Em seguida, selecione **Atributos personalizados** como seu tipo de personalização.

![A seção "Add Personalization" (Adicionar personalização) com o menu suspenso "Attribute" (Atribuição) estendido.]({% image_buster /assets/img/Shopify/add_personalization_2.png %}){: style="max-width:40%;"}

Depois de selecionar seu atributo personalizado, insira um valor padrão e cole o snippet do Liquid na sua mensagem.

![Colar um trecho do Liquid em uma mensagem.]({% image_buster /assets/img/Shopify/copy_liquid_snippet.png %})

#### Exemplo de carga útil

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

{% endtab %}
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

## Segmentação

Você pode filtrar os eventos do Shopify com todos os [filtros personalizados existentes]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) na Segmentação. 

![Página de detalhes do segmento para um segmento Shopify_Test com o filtro para o evento personalizado "shopify_checkouts_abandon" destacado.]({% image_buster /assets/img/Shopify/shopify_segmentation2.png %}){: style="max-width:80%;"}

Além disso, você pode usar o filtro de amplitude de compra no Braze para criar segmentos de usuários com base em:
- Primeira/última compra
- Primeira/última compra de um app específico
- Produtos que eles compraram anteriormente nos últimos 30 dias
- O número de compras que fizeram

![Filtro de segmentação para usuários que fizeram uma compra pela primeira vez após 17 de outubro de 2020.]({% image_buster /assets/img/Shopify/shopify_segmentation3.png %})

![Pesquisa de um ID de produto específico como um filtro de segmentação.]({% image_buster /assets/img/Shopify/shopify_segmentation4.png %})

{% alert note %}
Se estiver procurando segmentar por propriedades de eventos personalizados, certifique-se de trabalhar com seu gerente de sucesso do cliente ou com o [suporte]({{site.baseurl}}/braze_support/) da Braze para ativar a filtragem de todas as propriedades de eventos relevantes que você gostaria de usar na segmentação e no Liquid.
{% endalert %} 

## Campanha e disparo do Canva 

Com os eventos personalizados do Shopify no Braze, você pode disparar canvas ou campanhas como faria normalmente com qualquer outro [evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage). Por exemplo, você pode criar um canva baseado em ação que dispara a partir do evento `shopify_checkouts_abandon` da Shopify nos critérios de entrada do canva. 

![Canva baseada em ação que entra nos usuários que executam o evento personalizado "shopify_checkouts_abandon".]({% image_buster /assets/img/Shopify/shopify_integration11.png %})

Com o suporte a objetos aninhados para propriedades de eventos personalizados, os clientes podem disparar campanhas e Canvas usando uma propriedade de evento aninhada. A seguir, um exemplo de como disparar uma campanha usando um produto específico do evento personalizado `shopify_created_order`. Use `list_items[0].product_id` para indexar sua lista de itens e acessar o ID do produto.

![Campanha baseada em ação que envia aos usuários que realizam o evento personalizado "shopify_created_order" em que a propriedade aninhada "product_id" é igual a um número específico.]({% image_buster /assets/img/Shopify/shopify_integration17.png %})

