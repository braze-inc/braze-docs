---
nav_title: Shopify Daten in Braze
article_title: "Shopify Daten in Braze verwenden"
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie Shopify-Daten in Braze für die Personalisierung und Segmentierung verwenden können."
page_type: partner
search_tag: Partner
alias: "/shopify_data_legacy/"
page_order: 1
---

# Shopify Daten in Braze

> Mit der Unterstützung von verschachtelten Objekten für angepasste Events können Braze Shopify Kund:in Liquid Template-Variablen der verschachtelten Event-Eigenschaften verwenden.

Nachdem die Installation der App abgeschlossen ist, erstellt Braze automatisch Ihren Webhook und die ScriptTag Integration mit Shopify. In der folgenden Tabelle finden Sie weitere Informationen dazu, wie die unterstützten Shopify Events an angepasste Events und angepasste Attribute von Braze angepasst werden.

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

## Unterstützte Shopify Ereignisse

{% tabs %}
{% tab Shopify Ereignisse %}
{% subtabs global %}
{% subtab Product Viewed %}
**Veranstaltung**: `shopify_product_viewed`<br>
**Typ**: [Angepasstes Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Artikel ID | `{{event_properties.${id}}}` |
| Artikel Titel | `{{event_properties.${title}}}` |
| Artikel Preis | `{{event_properties.${price}}}` |
| Artikel Verkäufer | `{{event_properties.${vendor}}}` |
| Artikel Bilder | `{{event_properties.${images}}}` |


{% endraw %}
{% endsubtab %}


{% subtab Product Clicked %}
**Veranstaltung**: `shopify_product_clicked`<br>
**Typ**: [Angepasstes Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Artikel ID | `{{event_properties.${id}}}` |
| Artikel Titel | `{{event_properties.${title}}}` |
| Artikel Preis | `{{event_properties.${price}}}` |
| Artikel Verkäufer | `{{event_properties.${vendor}}}` |
| Artikel Bilder | `{{event_properties.${images}}}` |
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Cart %}
**Veranstaltung**: `shopify_abandoned_cart`<br>
**Typ**: [Angepasstes Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Warenkorb ID | `{{event_properties.${cart_id}}}` |
| Artikel ID | `{{event_properties.${line_items}[0].product_id}}` |
| Artikel Menge | `{{event_properties.${line_items}[0].quantity}}` |
| Artikel SKU | `{{event_properties.${line_items}[0].sku}}` |
| Artikel Titel | `{{event_properties.${line_items}[0].title}}` |
| Artikel Verkäufer | `{{event_properties.${line_items}[0].vendor}}` |
| Artikel Eigenschaften | `{{event_properties.${line_items}[0].properties}}` |
| Artikel Preis | `{{event_properties.${line_items}[0].price}}` |
| Variante ID | `{{event_properties.${line_items}[0].variant_id}}` |
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Checkout %}
**Veranstaltung**: `shopify_abandoned_checkout`<br>
**Typ**: [Angepasstes Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Checkout ID | `{{event_properties.${checkout_id}}}` |
| Abgebrochener Warenkorb URL | `{{event_properties.${abandoned_checkout_url}}}` |
| Rabattcode | `{{event_properties.${discount_code}}}` |
| Gesamtpreis | `{{event_properties.${total_price}}}` |
| Rabatt-Betrag | `{{event_properties.${applied_discount}[0].amount}}` |
| Rabatt Titel | `{{event_properties.${applied_discount}[0].title}}` |
| Rabatt Beschreibung | `{{event_properties.${applied_discount}[0].description}}` |
| Artikel ID | `{{event_properties.${line_items}[0].product_id}}` |
| Artikel Menge | `{{event_properties.${line_items}[0].quantity}}` |
| Artikel SKU | `{{event_properties.${line_items}[0].sku}}` |
| Artikel Titel | `{{event_properties.${line_items}[0].title}}` |
| Artikel Verkäufer | `{{event_properties.${line_items}[0].vendor}}` |
| Artikel Eigenschaften | `{{event_properties.${line_items}[0].properties}}` |
| Artikel Preis | `{{event_properties.${line_items}[0].price}}` |
| Variante ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variante Titel | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Created Order %}


**Veranstaltung**: `shopify_created_order`<br>
**Typ**: [Angepasstes Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)

{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Bestell-ID | `{{event_properties.${order_id}}}` |
| Bestätigter Status | `{{event_properties.${confirmed}}}` |
| Auftragsstatus URL | `{{event_properties.${order_status_url}}}` |
| Bestellnummer | `{{event_properties.${order_number}}}` |
| Abgebrochener Zeitstempel | `{{event_properties.${cancelled_at}}}` |
| Total Rabatte | `{{event_properties.${total_discounts}}}` |
| Gesamtpreis | `{{event_properties.${total_price}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Rabattcodes | `{{event_properties.${discount_codes}}}` |
| Artikel ID | `{{event_properties.${line_items}[0].product_id}}` |
| Artikel Menge | `{{event_properties.${line_items}[0].quantity}}` |
| Artikel SKU | `{{event_properties.${line_items}[0].sku}}` |
| Artikel Titel | `{{event_properties.${line_items}[0].title}}` |
| Artikel Verkäufer | `{{event_properties.${line_items}[0].vendor}}` |
| Artikel Eigenschaften | `{{event_properties.${line_items}[0].properties}}` |
| Artikel Preis | `{{event_properties.${line_items}[0].price}}` |
| Variante ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variante Titel | `{{event_properties.${line_items}[0].variant_title}}` |
| Versandtitel | `{{event_properties.${shipping}[0].title}}` |
| Versandpreis | `{{event_properties.${shipping}[0].price}}` |
|Shopify Shop | `{{event_properties.${shopify_storefront}}}` |
| Erfüllungsstatus | `{{event_properties.${fulfillment_status}}}` |
| Verweisende Website | `{{event_properties.${referring_site}}}` |
| Payment Gateway Names | `{{event_properties.${payment_gateway_names}}}` |
| Lieferadresse Zeile 1 | `{{event_properties.${shipping_address[0].address1}}}` |
| Lieferadresse Zeile 2 | `{{event_properties.${shipping_address[0].address2}}}` |
| Lieferadresse Ort | `{{event_properties.${shipping_address[0].city}}}` |
| Lieferadresse Land | `{{event_properties.${shipping_address[0].country}}}` |
| Versandadresse Vorname | `{{event_properties.${shipping_address[0].first_name}}}` |
| Lieferadresse Nachname | `{{event_properties.${shipping_address[0].last_name}}}` |
| Lieferadresse Provinz | `{{event_properties.${shipping_address[0].province}}}` |
| Versandadresse Zip | `{{event_properties.${shipping_address[0].zip}}}` |
| Rechnungsadresse Zeile 1 | `{{event_properties.${billing_address[0].address1}}}` |
| Rechnungsadresse Zeile 2 | `{{event_properties.${billing_address[0].address2}}}` |
| Rechnungsadresse Ort | `{{event_properties.${billing_address[0].city}}}` |
| Rechnungsadresse Land | `{{event_properties.${billing_address[0].country}}}` |
| Rechnungsadresse Vorname | `{{event_properties.${billing_address[0].first_name}}}` |
| Rechnungsadresse Nachname | `{{event_properties.${shipping_address[0].last_name}}}` |
| Rechnungsadresse Bundesland | `{{event_properties.${billing_address[0].province}}}` |
| Rechnungsadresse Zip | `{{event_properties.${billing_address[0].zip}}}` |
{% endraw %}


{% endsubtab %}
{% subtab Purchase %}


**Veranstaltung**: Kauf<br>
**Typ**: [Braze-Kauf-Event]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Artikel SKU | `{{event_properties.${line_items}[0].sku}}` |
| Artikel Titel | `{{event_properties.${line_items}[0].title}}` |
| Artikel Verkäufer | `{{event_properties.${line_items}[0].vendor}}` |
| Artikel Eigenschaften | `{{event_properties.${line_items}[0].properties}}` |
| Variante ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variante Titel | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}


{% endsubtab %}
{% subtab Paid Order %}
**Veranstaltung**: `shopify_paid_order`<br>
**Typ**: [Angepasstes Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Bestell-ID | `{{event_properties.${order_id}}}` |
| Bestätigter Status | `{{event_properties.${confirmed}}}` |
| Auftragsstatus URL | `{{event_properties.${order_status_url}}}` |
| Bestellnummer | `{{event_properties.${order_number}}}` |
| Abgebrochener Zeitstempel | `{{event_properties.${cancelled_at}}}` |
| Total Rabatte | `{{event_properties.${total_discounts}}}` |
| Gesamtpreis | `{{event_properties.${total_price}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Rabattcodes | `{{event_properties.${discount_codes}}}` |
| Artikel ID | `{{event_properties.${line_items}[0].product_id}}` |
| Artikel Menge | `{{event_properties.${line_items}[0].quantity}}` |
| Artikel SKU | `{{event_properties.${line_items}[0].sku}}` |
| Artikel Titel | `{{event_properties.${line_items}[0].title}}` |
| Artikel Verkäufer | `{{event_properties.${line_items}[0].vendor}}` |
| Artikel Eigenschaften | `{{event_properties.${line_items}[0].properties}}` |
| Artikel Preis | `{{event_properties.${line_items}[0].price}}` |
| Versandtitel | `{{event_properties.${shipping}[0].title}}` |
| Versandpreis | `{{event_properties.${shipping}[0].price}}` |
| Variante ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variante Titel | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Partially Fulfilled Order %}
**Veranstaltung**: `shopify_partially_fulfilled_order`<br>
**Typ**: [Angepasstes Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Bestell-ID | `{{event_properties.${order_id}}}` |
| Gesamtpreis | `{{event_properties.${total_price}}}` |
| Total Rabatte | `{{event_properties.${total_discounts}}}` |
| Bestätigter Status | `{{event_properties.${confirmed}}}` |
| Auftragsstatus URL | `{{event_properties.${order_status_url}}}` |
| Bestellnummer | `{{event_properties.${order_number}}}` |
| Abgebrochener Zeitstempel | `{{event_properties.${cancelled_at}}}` |
| Closed Timestamp | `{{event_properties.${closed_at}}}` |
| Artikel ID | `{{event_properties.${line_items}[0].product_id}}` |
| Artikel Menge | `{{event_properties.${line_items}[0].quantity}}` |
| Artikel SKU | `{{event_properties.${line_items}[0].sku}}` |
| Artikel Titel | `{{event_properties.${line_items}[0].title}}` |
| Artikel Verkäufer | `{{event_properties.${line_items}[0].vendor}}` |
| Artikel Name | `{{event_properties.${line_items}[0].name}}` |
| Artikel Eigenschaften | `{{event_properties.${line_items}[0].properties}}` |
| Artikel Preis | `{{event_properties.${line_items}[0].price}}` |
| Versandtitel | `{{event_properties.${shipping}[0].title}}` |
| Versandpreis | `{{event_properties.${shipping}[0].price}}` |
| Erfüllungsstatus | `{{event_properties.${fulfillment_status}}}` |
| Fulfillment Sendungsstatus | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Erfüllungsstatus | `{{event_properties.${fulfillments}[0].status}}` |
| Fulfillment Tracking Unternehmen | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| Fulfillment Tracking Nummer | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| Fulfillment Tracking-Nummern | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| Fulfillment Tracking URL | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| Fulfillment Tracking URLs | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| Erfüllungsstatus | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Fulfillment Name | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Fulfillment Preis | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Fulfillment Produkt ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Erfüllungsmenge | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Fulfillment Versand | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Fulfillment SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Fulfillment Title | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fulfillment Vendor | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
| Variante ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variante Titel | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Fulfilled Order %}
**Veranstaltung**: `shopify_fulfilled_order`<br>
**Typ**: [Angepasstes Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Bestell-ID | `{{event_properties.${order_id}}}` |
| Gesamtpreis | `{{event_properties.${total_price}}}` |
| Total Rabatte | `{{event_properties.${total_discounts}}}` |
| Bestätigter Status | `{{event_properties.${confirmed}}}` |
| Auftragsstatus URL | `{{event_properties.${order_status_url}}}` |
| Bestellnummer | `{{event_properties.${order_number}}}` |
| Abgebrochener Zeitstempel | `{{event_properties.${cancelled_at}}}` |
| Closed Timestamp | `{{event_properties.${closed_at}}}` |
| Artikel ID | `{{event_properties.${line_items}[0].product_id}}` |
| Artikel Menge | `{{event_properties.${line_items}[0].quantity}}` |
| Artikel SKU | `{{event_properties.${line_items}[0].sku}}` |
| Artikel Titel | `{{event_properties.${line_items}[0].title}}` |
| Artikel Verkäufer | `{{event_properties.${line_items}[0].vendor}}` |
| Artikel Name | `{{event_properties.${line_items}[0].name}}` |
| Artikel Eigenschaften | `{{event_properties.${line_items}[0].properties}}` |
| Artikel Preis | `{{event_properties.${line_items}[0].price}}` |
| Versandtitel | `{{event_properties.${shipping}[0].title}}` |
| Versandpreis | `{{event_properties.${shipping}[0].price}}` |
| Erfüllungsstatus | `{{event_properties.${fulfillment_status}}}` |
| Fulfillment Sendungsstatus | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Status | `{{event_properties.${fulfillments}[0].status}}` |
| Fulfillment Tracking Unternehmen | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| Fulfillment Tracking Nummer | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| Fulfillment Tracking-Nummern | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| Fulfillment Tracking URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| Fulfillment Tracking URLs | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| Erfüllungsstatus | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Fulfillment Name | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Fulfillment Preis | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Fulfillment Produkt ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Erfüllungsmenge | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Fulfillment Versand | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Fulfillment SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Fulfillment Title | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fulfillment Vendor | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
| Variante ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variante Titel | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Cancelled Order %}
**Veranstaltung**: `shopify_cancelled_order`<br>
**Typ**: [Angepasstes Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Bestell-ID | `{{event_properties.${order_id}}}` |
| Gesamtpreis | `{{event_properties.${total_price}}}` |
| Total Rabatte | `{{event_properties.${total_discounts}}}` |
| Bestätigt | `{{event_properties.${confirmed}}}` |
| Auftragsstatus URL | `{{event_properties.${order_status_url}}}` |
| Bestellnummer | `{{event_properties.${order_number}}}` |
| Abgebrochener Zeitstempel | `{{event_properties.${cancelled_at}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Rabattcodes | `{{event_properties.${discount_codes}}}` |
| Erfüllungsstatus | `{{event_properties.${fulfillment_status}}}` |
| Erfüllungen | `{{event_properties.${fulfillments}}}` |
| Artikel ID | `{{event_properties.${line_items}[0].product_id}}` |
| Artikel Menge | `{{event_properties.${line_items}[0].quantity}}` |
| Artikel SKU | `{{event_properties.${line_items}[0].sku}}` |
| Artikel Titel | `{{event_properties.${line_items}[0].title}}` |
| Artikel Verkäufer | `{{event_properties.${line_items}[0].vendor}}` |
| Artikel Name | `{{event_properties.${line_items}[0].name}}` |
| Artikel Eigenschaften | `{{event_properties.${line_items}[0].properties}}` |
| Erfüllungsstatus | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| Versandtitel | `{{event_properties.${shipping}[0].title}}` |
| Versandpreis | `{{event_properties.${shipping}[0].price}}` |
| Variante ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variante Titel | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}

{% subtab Created Refund %}
**Veranstaltung**: `shopify_created_refund`<br>
**Typ**: [Angepasstes Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| Variable | Liquid Templating |
| --- | --- |
| Bestell-ID | `{{event_properties.${order_id}}}` |
| Bestellnotiz | `{event_properties.${note}}}` |
| Artikel ID | `{{event_properties.${line_items}[0].product_id}}` |
| Artikel Menge | `{{event_properties.${line_items}[0].quantity}}` |
| Artikel SKU | `{{event_properties.${line_items}[0].sku}}` |
| Artikel Titel | `{{event_properties.${line_items}[0].title}}` |
| Artikel Verkäufer | `{{event_properties.${line_items}[0].vendor}}` |
| Artikel Name | `{{event_properties.${line_items}[0].name}}` |
| Artikel Eigenschaften | `{{event_properties.${line_items}[0].properties}}` |
| Artikel Preis | `{{event_properties.${line_items}[0].price}}` |
| Variante ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variante Titel | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Beispiel Payload %}
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

## Unterstützte angepasste Attribute von Shopify
{% tabs local %}
{% tab Shopify Angepasste Attribute %}
| Attribut Name | Beschreibung |
| --- | --- |
| `shopify_tags` | Tags, die der Shop-Betreiber dem Kunden zugewiesen hat, formatiert als String mit durch Komma getrennten Werten. Eine Kund:in kann bis zu 250 Tags haben. Jeder Tag kann bis zu 255 Zeichen enthalten. |
| `shopify_total_spent` | Der Gesamtbetrag, den der Kunde im Verlauf seiner Bestellung ausgegeben hat. |
| `shopify_order_count` | Die Anzahl der Bestellungen, die mit diesem Kund:in verbunden sind. Test- und archivierte Bestellungen werden nicht gezählt. |
| `shopify_last_order_id` | Die ID der letzten Bestellung des Kunden. |
| `shopify_last_order_name` | Der Name der letzten Bestellung der Kund:in. Dies steht in direktem Zusammenhang mit dem Feld `name` in der Auftragsressource. |
| `shopify_zipcode` | Die Postleitzahl der Kund:in aus ihrer Standardadresse. |
| `shopify_province` | Die Provinz der Kund:in aus ihrer Standardadresse. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Liquid Personalisierung

Um eine Liquid-Personalisierung für Ihre angepassten Attribute in Shopify hinzuzufügen, wählen Sie **\+ Personalisierung**. Wählen Sie dann als Personalisierungstyp **angepasste Attribute** aus.

![Der Bereich "Personalisierung hinzufügen" mit dem erweiterten Dropdown-Menü "Attribute".]({% image_buster /assets/img/Shopify/add_personalization_2.png %}){: style="max-width:40%;"}

Nachdem Sie Ihr angepasstes Attribut ausgewählt haben, geben Sie einen Standardattribut ein und kopieren das Liquid Snippet in Ihre Nachricht.

![Einfügen eines Liquid-Snippets in eine Nachricht.]({% image_buster /assets/img/Shopify/copy_liquid_snippet.png %})

#### Beispiel-Nutzlast

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
{% tab Beispiel Payload %}
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

## Unterstützte Shopify Standard Attribute

- E-Mail
- Vorname
- Nachname
- Telefon
- Ort
- Land

{% alert note %}
Braze aktualisiert die unterstützten angepassten Attribute von Shopify und die Standardattribute von Braze nur dann, wenn sich die Daten vom bestehenden Nutzerprofil unterscheiden. Wenn die eingehenden Shopify-Daten beispielsweise den Vornamen Bob enthalten und Bob bereits als Vorname im Nutzerprofil von Braze existiert, wird Braze kein Update triggern und Ihnen wird kein Datenpunkt berechnet.
{% endalert %}

## Segmentierung

Sie können die Events von Shopify mit allen [vorhandenen angepassten Filtern]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) in der Segmentierung filtern. 

![Segmentdetailseite für ein Shopify_Test Segment mit dem Filter für das angepasste Event "shopify_checkouts_abandon" hervorgehoben.]({% image_buster /assets/img/Shopify/shopify_segmentation2.png %}){: style="max-width:80%;"}

Darüber hinaus können Sie den Filter "Kaufumfang" in Braze verwenden, um Segmente von Nutzer:innen auf der Grundlage von:
- Erster/letzter Kauf
- Erster/letzter Kauf für eine bestimmte App
- Produkte, die sie in den letzten 30 Tagen gekauft haben
- Die Anzahl der Einkäufe, die sie getätigt haben

![Segmentierungsfilter für Nutzer:innen, die nach dem 17\. Oktober 2020 zum ersten Mal einen Kauf getätigt haben.]({% image_buster /assets/img/Shopify/shopify_segmentation3.png %})

![Suche nach einer bestimmten Produkt ID als Filter für die Segmentierung.]({% image_buster /assets/img/Shopify/shopify_segmentation4.png %})

{% alert note %}
Wenn Sie nach angepassten Event-Eigenschaften segmentieren möchten, stellen Sie sicher, dass Sie mit Ihrem Customer-Success-Manager oder dem [Braze-Support]({{site.baseurl}}/braze_support/) zusammenarbeiten, um die Filterung für alle relevanten Event-Eigenschaften zu aktivieren, die Sie in der Segmentierung und in Liquid verwenden möchten.
{% endalert %} 

## Auslösen von Kampagnen und Canvas 

Mit den angepassten Events von Shopify in Braze können Sie Canvase oder Kampagnen triggern, wie Sie es von jedem anderen [angepassten Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage) gewohnt sind. Sie können zum Beispiel ein aktionsbasiertes Canvas erstellen, das durch das Shopify-Ereignis `shopify_checkouts_abandon` innerhalb der Eingangskriterien des Canvas ausgelöst wird. 

![Aktionsbasiertes Canvas, das Nutzer:innen erfasst, die das angepasste Event "shopify_checkouts_abandon" ausführen.]({% image_buster /assets/img/Shopify/shopify_integration11.png %})

Mit der verschachtelten Objektunterstützung für angepasste Event-Eigenschaften können Kund:in Kampagnen und Canvase mit einer verschachtelten Event-Eigenschaft triggern. Im Folgenden sehen Sie ein Beispiel für das Auslösen einer Kampagne mit einem bestimmten Produkt aus dem angepassten Event `shopify_created_order`. Stellen Sie sicher, dass Sie `list_items[0].product_id` verwenden, um Ihre Artikelliste zu indizieren und auf die ID des Produkts zuzugreifen.

![Aktionsbasierte Kampagne, die an Nutzer:innen gesendet wird, die das angepasste Event "shopify_created_order" ausführen, wobei die verschachtelte Eigenschaft "product_id" einer bestimmten Zahl entspricht.]({% image_buster /assets/img/Shopify/shopify_integration17.png %})

