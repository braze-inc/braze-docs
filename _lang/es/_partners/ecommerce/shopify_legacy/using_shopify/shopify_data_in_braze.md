---
nav_title: Datos de Shopify en Braze
article_title: "Uso de los datos de Shopify en Braze"
description: "Este artículo de referencia describe cómo utilizar los datos de Shopify en Braze para la personalización y la segmentación."
page_type: partner
search_tag: Partner
alias: "/shopify_data_legacy/"
page_order: 1
---

# Datos de Shopify en Braze

> Mediante el soporte de objetos anidados para eventos personalizados, los clientes de Shopify de Braze pueden utilizar las variables de plantilla Liquid de las propiedades de eventos anidados.

Una vez finalizada la instalación de la aplicación, Braze crea automáticamente tu webhook e integración ScriptTag con Shopify. Consulta la tabla siguiente para obtener más detalles sobre cómo se mapean los eventos de Shopify compatibles con los eventos y atributos personalizados de Braze.

{% multi_lang_include alerts.md alert='Shopify obsoleto' %}

## Eventos Shopify compatibles

{% tabs %}
{% tab Eventos Shopify %}
{% subtabs global %}
{% subtab Product Viewed %}
**Evento**: `shopify_product_viewed`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Plantilla Liquid |
| --- | --- |
| ID del artículo | `{{event_properties.${id}}}` |
| Título del artículo | `{{event_properties.${title}}}` |
| Precio del artículo | `{{event_properties.${price}}}` |
| Vendedor del artículo | `{{event_properties.${vendor}}}` |
| Imágenes de artículos | `{{event_properties.${images}}}` |


{% endraw %}
{% endsubtab %}


{% subtab Product Clicked %}
**Evento**: `shopify_product_clicked`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Plantilla Liquid |
| --- | --- |
| ID del artículo | `{{event_properties.${id}}}` |
| Título del artículo | `{{event_properties.${title}}}` |
| Precio del artículo | `{{event_properties.${price}}}` |
| Vendedor del artículo | `{{event_properties.${vendor}}}` |
| Imágenes de artículos | `{{event_properties.${images}}}` |
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Cart %}
**Evento**: `shopify_abandoned_cart`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Plantilla Liquid |
| --- | --- |
| ID del carrito | `{{event_properties.${cart_id}}}` |
| ID del artículo | `{{event_properties.${line_items}[0].product_id}}` |
| Cantidad de artículos | `{{event_properties.${line_items}[0].quantity}}` |
| SKU del artículo | `{{event_properties.${line_items}[0].sku}}` |
| Título del artículo | `{{event_properties.${line_items}[0].title}}` |
| Vendedor del artículo | `{{event_properties.${line_items}[0].vendor}}` |
| Propiedades del artículo | `{{event_properties.${line_items}[0].properties}}` |
| Precio del artículo | `{{event_properties.${line_items}[0].price}}` |
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Checkout %}
**Evento**: `shopify_abandoned_checkout`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Plantilla Liquid |
| --- | --- |
| ID de pago | `{{event_properties.${checkout_id}}}` |
| URL del carrito abandonado | `{{event_properties.${abandoned_checkout_url}}}` |
| Código de descuento | `{{event_properties.${discount_code}}}` |
| Precio total | `{{event_properties.${total_price}}}` |
| Importe del descuento | `{{event_properties.${applied_discount}[0].amount}}` |
| Título del descuento | `{{event_properties.${applied_discount}[0].title}}` |
| Descripción del descuento | `{{event_properties.${applied_discount}[0].description}}` |
| ID del artículo | `{{event_properties.${line_items}[0].product_id}}` |
| Cantidad de artículos | `{{event_properties.${line_items}[0].quantity}}` |
| SKU del artículo | `{{event_properties.${line_items}[0].sku}}` |
| Título del artículo | `{{event_properties.${line_items}[0].title}}` |
| Vendedor del artículo | `{{event_properties.${line_items}[0].vendor}}` |
| Propiedades del artículo | `{{event_properties.${line_items}[0].properties}}` |
| Precio del artículo | `{{event_properties.${line_items}[0].price}}` |
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Created Order %}


**Evento**: `shopify_created_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)

{% raw %}
| Variable | Plantilla Liquid |
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
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
| Título del envío | `{{event_properties.${shipping}[0].title}}` |
| Precio de envío | `{{event_properties.${shipping}[0].price}}` |
|Tienda Shopify | `{{event_properties.${shopify_storefront}}}` |
| Estado de cumplimiento | `{{event_properties.${fulfillment_status}}}` |
| Sitio de referencia | `{{event_properties.${referring_site}}}` |
| Nombres de pasarelas de pago | `{{event_properties.${payment_gateway_names}}}` |
| Dirección de envío Línea 1 | `{{event_properties.${shipping_address[0].address1}}}` |
| Dirección de envío Línea 2 | `{{event_properties.${shipping_address[0].address2}}}` |
| Dirección de envío Ciudad | `{{event_properties.${shipping_address[0].city}}}` |
| Dirección de envío País | `{{event_properties.${shipping_address[0].country}}}` |
| Dirección de envío Nombre | `{{event_properties.${shipping_address[0].first_name}}}` |
| Dirección de envío Apellidos | `{{event_properties.${shipping_address[0].last_name}}}` |
| Dirección de envío Provincia | `{{event_properties.${shipping_address[0].province}}}` |
| Dirección de envío Código postal | `{{event_properties.${shipping_address[0].zip}}}` |
| Dirección de facturación Línea 1 | `{{event_properties.${billing_address[0].address1}}}` |
| Dirección de facturación Línea 2 | `{{event_properties.${billing_address[0].address2}}}` |
| Dirección de facturación Ciudad | `{{event_properties.${billing_address[0].city}}}` |
| Dirección de facturación País | `{{event_properties.${billing_address[0].country}}}` |
| Dirección de facturación Nombre | `{{event_properties.${billing_address[0].first_name}}}` |
| Dirección de facturación Apellidos | `{{event_properties.${shipping_address[0].last_name}}}` |
| Dirección de facturación Provincia | `{{event_properties.${billing_address[0].province}}}` |
| Dirección de facturación Código postal | `{{event_properties.${billing_address[0].zip}}}` |
{% endraw %}


{% endsubtab %}
{% subtab Purchase %}


**Evento**: Compra<br>
**Tipo**: [Evento de compra de Braze]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/)


{% raw %}
| Variable | Plantilla Liquid |
| --- | --- |
| SKU del artículo | `{{event_properties.${line_items}[0].sku}}` |
| Título del artículo | `{{event_properties.${line_items}[0].title}}` |
| Vendedor del artículo | `{{event_properties.${line_items}[0].vendor}}` |
| Propiedades del artículo | `{{event_properties.${line_items}[0].properties}}` |
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título de la variante | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}


{% endsubtab %}
{% subtab Paid Order %}
**Evento**: `shopify_paid_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Plantilla Liquid |
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
{% endraw %}
{% endsubtab %}


{% subtab Partially Fulfilled Order %}
**Evento**: `shopify_partially_fulfilled_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Plantilla Liquid |
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
{% endraw %}
{% endsubtab %}


{% subtab Fulfilled Order %}
**Evento**: `shopify_fulfilled_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Plantilla Liquid |
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
{% endraw %}
{% endsubtab %}


{% subtab Cancelled Order %}
**Evento**: `shopify_cancelled_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Plantilla Liquid |
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
{% endraw %}
{% endsubtab %}

{% subtab Created Refund %}
**Evento**: `shopify_created_refund`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Plantilla Liquid |
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
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Ejemplo de carga útil %}
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

## Atributos personalizados de Shopify compatibles
{% tabs local %}
{% tab Atributos personalizados de Shopify %}
| Nombre del atributo Descripción
| --- | --- |
| `shopify_tags` | Etiquetas que el propietario de la tienda ha asignado al cliente, formateadas como una cadena de valores separados por comas. Un cliente puede tener hasta 250 etiquetas. Cada etiqueta puede tener hasta 255 caracteres. |
| `shopify_total_spent` | La cantidad total de dinero que el cliente ha gastado en su historial de pedidos. |
| `shopify_order_count` | El número de pedidos asociados a este cliente. No se cuentan los pedidos de prueba ni los archivados. |
| `shopify_last_order_id` | El ID del último pedido del cliente. |
| `shopify_last_order_name` | El nombre del último pedido del cliente. Esto está directamente relacionado con el campo `name` del recurso pedido. |
| `shopify_zipcode` | El código postal del cliente a partir de su dirección predeterminada. |
| `shopify_province` | La provincia del cliente a partir de su dirección predeterminada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Personalización de Liquid

Para añadir personalización Liquid a tus atributos personalizados de Shopify, selecciona **\+ Personalización**. A continuación, selecciona **Atributos personalizados** como tipo de personalización.

![La sección "Añadir personalización" con el desplegable "Atributo" ampliado.]({% image_buster /assets/img/Shopify/add_personalization_2.png %}){: style="max-width:40%;"}

Tras seleccionar tu atributo personalizado, introduce un valor predeterminado y copia el fragmento de código Liquid en tu mensaje.

![Pegar un fragmento de código Liquid en un mensaje.]({% image_buster /assets/img/Shopify/copy_liquid_snippet.png %})

#### Ejemplo de carga útil

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

## Segmentación

Puedes filtrar los eventos de Shopify con todos los [filtros personalizados existentes]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) en Segmentación. 

![Página de detalles del segmento para un segmento de Shopify_Test con el filtro para el evento personalizado "shopify_checkouts_abandon" resaltado.]({% image_buster /assets/img/Shopify/shopify_segmentation2.png %}){: style="max-width:80%;"}

Además, puedes utilizar el filtro de amplitud de compra en Braze para crear segmentos de usuarios basados en:
- Primera/última compra
- Primera/última compra de una aplicación concreta
- Productos que han comprado anteriormente en los últimos 30 días
- El número de compras que hicieron

![Filtro de segmentación para usuarios que realizaron su primera compra después del 17 de octubre de 2020.]({% image_buster /assets/img/Shopify/shopify_segmentation3.png %})

![Buscar un ID de producto específico como filtro de segmentación.]({% image_buster /assets/img/Shopify/shopify_segmentation4.png %})

{% alert note %}
Si quieres segmentar por propiedades del evento personalizadas, asegúrate de trabajar con tu administrador del éxito del cliente o con [el soporte de]({{site.baseurl}}/braze_support/) Braze para habilitar el filtrado de todas las propiedades del evento relevantes que quieras utilizar en la segmentación y en Liquid.
{% endalert %} 

## Desencadenar campañas y Canvas 

Con los eventos personalizados de Shopify en Braze, puedes desencadenar Canvas o campañas como harías normalmente con cualquier otro [evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage). Por ejemplo, puedes crear un Canvas basado en acciones que se desencadene a partir del evento de Shopify `shopify_checkouts_abandon` dentro de los criterios de entrada del Canvas. 

![Canvas basado en acciones que introduce a los usuarios que realizan el evento personalizado "shopify_checkouts_abandon".]({% image_buster /assets/img/Shopify/shopify_integration11.png %})

Con la compatibilidad de objetos anidados para propiedades del evento personalizadas, los clientes pueden desencadenar campañas y Lienzos utilizando una propiedad del evento anidada. A continuación se muestra un ejemplo de desencadenar una campaña utilizando un producto específico del evento personalizado `shopify_created_order`. Asegúrate de utilizar `list_items[0].product_id` para indexar tu lista de artículos y acceder al ID del producto.

![Campaña basada en acciones que se envía a los usuarios que realizan el evento personalizado "shopify_created_order" en el que la propiedad anidada "product_id" es igual a un número específico.]({% image_buster /assets/img/Shopify/shopify_integration17.png %})

