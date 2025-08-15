---
nav_title: Shopify data in Braze
article_title: "Using Shopify Data in Braze"
description: "This reference article outlines how to use Shopify data in Braze for personalization and segmentation."
page_type: partner
search_tag: Partner
alias: "/shopify_data_legacy/"
page_order: 1
---

# Shopify data in Braze

> Using nested object support for custom events, Braze Shopify customers can use Liquid template variables of the nested event properties.

After the app installation is complete, Braze automatically creates your webhook and ScriptTag integration with Shopify. See the following table for more details on how the supported Shopify events map to Braze custom events and custom attributes.

{% multi_lang_include alerts/important_alerts.md alert='Shopify deprecation' %}

## Supported Shopify events

{% tabs %}
{% tab Shopify Events %}
{% subtabs global %}
{% subtab Product Viewed %}
**Event**: `shopify_product_viewed`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Item ID | `{{event_properties.${id}}}` |
| Item Title  | `{{event_properties.${title}}}` |
| Item Price | `{{event_properties.${price}}}` |
| Item Vendor | `{{event_properties.${vendor}}}` |
| Item Images | `{{event_properties.${images}}}` |


{% endraw %}
{% endsubtab %}


{% subtab Product Clicked %}
**Event**: `shopify_product_clicked`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Item ID | `{{event_properties.${id}}}` |
| Item Title  | `{{event_properties.${title}}}` |
| Item Price | `{{event_properties.${price}}}` |
| Item Vendor | `{{event_properties.${vendor}}}` |
| Item Images | `{{event_properties.${images}}}` |
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Cart %}
**Event**: `shopify_abandoned_cart`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Cart ID | `{{event_properties.${cart_id}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Checkout %}
**Event**: `shopify_abandoned_checkout`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Checkout ID | `{{event_properties.${checkout_id}}}` |
| Abandoned Cart URL | `{{event_properties.${abandoned_checkout_url}}}` |
| Discount Code | `{{event_properties.${discount_code}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Discount Amount | `{{event_properties.${applied_discount}[0].amount}}` |
| Discount Title | `{{event_properties.${applied_discount}[0].title}}` |
| Discount Description | `{{event_properties.${applied_discount}[0].description}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Created Order %}


**Event**: `shopify_created_order`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Discount Codes | `{{event_properties.${discount_codes}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
|Shopify store | `{{event_properties.${shopify_storefront}}}` |
| Fulfillment status | `{{event_properties.${fulfillment_status}}}` |
| Referring Site | `{{event_properties.${referring_site}}}` | 
| Payment Gateway Names | `{{event_properties.${payment_gateway_names}}}` |
| Shipping Address Line 1 | `{{event_properties.${shipping_address[0].address1}}}` |
| Shipping Address Line 2 | `{{event_properties.${shipping_address[0].address2}}}` |
| Shipping Address City | `{{event_properties.${shipping_address[0].city}}}` |
| Shipping Address Country | `{{event_properties.${shipping_address[0].country}}}` |
| Shipping Address First Name | `{{event_properties.${shipping_address[0].first_name}}}` |
| Shipping Address Last Name | `{{event_properties.${shipping_address[0].last_name}}}` | 
| Shipping Address Province | `{{event_properties.${shipping_address[0].province}}}` |
| Shipping Address Zip | `{{event_properties.${shipping_address[0].zip}}}` |
| Billing Address Line 1 | `{{event_properties.${billing_address[0].address1}}}` |
| Billing Address Line 2 | `{{event_properties.${billing_address[0].address2}}}` |
| Billing Address City | `{{event_properties.${billing_address[0].city}}}` |
| Billing Address Country | `{{event_properties.${billing_address[0].country}}}` |
| Billing Address First Name | `{{event_properties.${billing_address[0].first_name}}}` |
| Billing Address Last Name | `{{event_properties.${shipping_address[0].last_name}}}` |
| Billing Address Province | `{{event_properties.${billing_address[0].province}}}` |
| Billing Address Zip | `{{event_properties.${billing_address[0].zip}}}` |
{% endraw %}


{% endsubtab %}
{% subtab Purchase %}


**Event**: Purchase<br>
**Type**: [Braze Purchase Event]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title  | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}


{% endsubtab %}
{% subtab Paid Order %}
**Event**: `shopify_paid_order`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Discount Codes | `{{event_properties.${discount_codes}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Partially Fulfilled Order %}
**Event**: `shopify_partially_fulfilled_order`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Closed Timestamp | `{{event_properties.${closed_at}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillment Shipment Status | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].status}}` |
| Fulfillment Tracking Company | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| Fulfillment Tracking Number | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| Fulfillment Tracking Numbers | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| Fulfillment Tracking URL | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| Fulfillment Tracking URLs | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Fulfillment Name | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Fulfillment Price | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Fulfillment Product ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Fulfillment Quantity | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Fulfillment Shipping | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Fulfillment SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Fulfillment Title | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fulfillment Vendor | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Fulfilled Order %}
**Event**: `shopify_fulfilled_order`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Closed Timestamp | `{{event_properties.${closed_at}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillment Shipment Status | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Status | `{{event_properties.${fulfillments}[0].status}}` |
| Fulfillment Tracking Company | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| Fulfillment Tracking Number | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| Fulfillment Tracking Numbers | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| Fulfillment Tracking URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| Fulfillment Tracking URLs | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Fulfillment Name | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Fulfillment Price | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Fulfillment Product ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Fulfillment Quantity | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Fulfillment Shipping | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Fulfillment SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Fulfillment Title | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fulfillment Vendor | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Cancelled Order %}
**Event**: `shopify_cancelled_order`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Discount Codes | `{{event_properties.${discount_codes}}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillments | `{{event_properties.${fulfillments}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Fulfillment Status | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}

{% subtab Created Refund %}
**Event**: `shopify_created_refund`<br>
**Type**: [Custom Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Order Note | `{event_properties.${note}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Example Payload %}
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

## Supported Shopify custom attributes
{% tabs local %}
{% tab Shopify Custom Attributes %}
| Attribute Name | Description |
| --- | --- |
| `shopify_tags`  | Tags that the shop owner has attached to the customer, formatted as a string of comma-separated values. A customer can have up to 250 tags. Each tag can have up to 255 characters. |
| `shopify_total_spent` | The total amount of money that the customer has spent across their order history. |
| `shopify_order_count` | The number of orders associated with this customer. Test and archived orders aren't counted. |
| `shopify_last_order_id` | The ID of the customer's last order. |
| `shopify_last_order_name` | The name of the customer's last order. This is directly related to the `name` field on the order resource. |
| `shopify_zipcode` | The customer's zipcode from their default address. |
| `shopify_province` | The customer's province from their default address. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Liquid personalization

To add Liquid personalization for your Shopify custom attributes, select **+ Personalization**. Then select **Custom Attributes** as your personalization type.

![The "Add Personalization" section with the "Attribute" dropdown extended.]({% image_buster /assets/img/Shopify/add_personalization_2.png %}){: style="max-width:40%;"}

After selecting your custom attribute, input a default value and copy the Liquid snippet into your message.

![Pasting a Liquid snippet into a message.]({% image_buster /assets/img/Shopify/copy_liquid_snippet.png %})

#### Example payload

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
{% tab Example Payload %}
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

## Supported Shopify standard attributes

- Email
- First Name
- Last Name
- Phone
- City
- Country

{% alert note %}
Braze will only update supported Shopify custom attributes and Braze standard attributes if there is a difference in data from the existing user profile. For example, if the inbound Shopify data contains a first name of Bob and Bob already exists as a first name on the Braze user profile, Braze will not trigger an update, and you will not be charged a data point.
{% endalert %}

## Segmentation

You can filter Shopify's events with all of the [existing custom filters]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) in Segmentation. 

![Segment Details page for a Shopify_Test segment with the filter for the custom event "shopify_checkouts_abandon" highlighted.]({% image_buster /assets/img/Shopify/shopify_segmentation2.png %}){: style="max-width:80%;"}

In addition, you can use the breadth of purchase filter in Braze to create segments of users based on:
- First/last purchase
- First/last purchase for a specific app
- Products they have previously purchased within the last 30 days
- The number of purchases they made

![Segmentation filter for users that first made a purchase after October 17, 2020.]({% image_buster /assets/img/Shopify/shopify_segmentation3.png %})

![Searching for a specific product ID as a segmentation filter.]({% image_buster /assets/img/Shopify/shopify_segmentation4.png %})

{% alert note %}
If you are looking to segment by custom event properties, make sure that you work with your customer success manager or Braze [support]({{site.baseurl}}/braze_support/) to enable filtering for all relevant event properties that you'd like to use within segmentation and Liquid.
{% endalert %} 

## Campaign and Canvas triggering 

With Shopify custom events in Braze, you can trigger Canvases or campaigns like you normally would with any other [custom event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage). For example, you may create an Action-Based Canvas that triggers off of the Shopify `shopify_checkouts_abandon` event within the Canvas entry criteria. 

![Action-based Canvas that enters users who perform the custom event "shopify_checkouts_abandon".]({% image_buster /assets/img/Shopify/shopify_integration11.png %})

With nested object support for custom event properties, customers can trigger campaigns and Canvases using a nested event property. The following is an example of triggering a campaign using a specific product from the `shopify_created_order` custom event. Make sure to use `list_items[0].product_id` to index your item list and access the product ID.

![Action-based campaign that sends to users who perform the custom event "shopify_created_order" where the nested property "product_id" equals a specific number.]({% image_buster /assets/img/Shopify/shopify_integration17.png %})

