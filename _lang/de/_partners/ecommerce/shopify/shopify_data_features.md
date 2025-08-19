---
nav_title: Shopify Daten Features
article_title: "Shopify Daten Features"
description: "Dieser referenzierte Artikel behandelt die Shopify Daten Features."
page_type: partner
search_tag: Partner
alias: /shopify_data_features/
page_order: 3
---

# Shopify Daten Features

> Dieser Artikel bietet eine Übersicht über unsere Shopify Features, einschließlich der Daten, die in Shopify getrackt werden, sowie Beispiele für Payloads, historische Backfills und Produktsynchronisationen.

## Tracking von Shopify-Ereignissen

{% tabs %}
{% tab Beispiel Payload %}
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
{% tab Shopify Ereignisse %}
{% subtabs global %}
{% subtab Product viewed %}
**Veranstaltung**: `ecommerce.product_viewed`<br>
**Typ**: Empfohlene Veranstaltung<br>
**Ausgelöst**: Wenn eine Kund:in eine Produktseite blickt<br>
**Anwendungsfälle**: Browse abandonment

{% raw %}
| Variable | Liquid Template |
| --- | --- |
\|------------------|-----------------------------------------------------|
| `product_id`       | `{{event_properties.${product_id}}}`                |
| `product_name `    | `{{event_properties.${product_name}}}`              |
| `variant_id`       | `{{event_properties.${variant_id}}}`                |
| `image_url `       | `{{event_properties.${image_url}}}`                 |
| `product_url`      | `<your-store.myshopify.com>{{event_properties.${product_url}}}` <br><br>Fügen Sie die Domain Ihrer Shopify Website vor der URL ein. |
| `price`            | `{{event_properties.${price}}}`                     |
| `currency`         | `{{event_properties.${currency}}}`                  |
| `source`           | `{{event_properties.${source}}}`                    |
| `sku`              | `{{event_properties.${metadata}[0].sku}}`          |
| `type`             | `event_properties.${type}`          |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Cart updated %}
**Veranstaltung**: `ecommerce.cart_updated`<br>
**Typ**: Empfohlene Veranstaltung<br>
**Ausgelöst**: Wenn eine Kund:in ihren Warenkorb hinzufügt, entfernt oder aktualisiert<br>
**Anwendungsfälle**: Warenkorb-Abbruch

Für Abandoned Cart Canvase müssen Sie zunächst den Liquid-Tag für den Warenkorb-Abbruch hinzufügen, um den Kontext des Warenkorbs in Ihrer Nachricht zu erhalten. 

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} %}
```
{% endraw %}

Dann können Sie die folgenden Liquid-Tags für den Warenkorb in Ihre Nachricht einfügen.

{% raw %}
| Variable | Liquid Template |
\|------------------|-----------------------------------------------------|
| `cart_id`          | `{{ shopping_cart.cart_id }}`                       |
| `currency`         | `{{ shopping_cart.currency }}`                      |
| `total_value`      | `{{ shopping_cart.total_value }}`                   |
| `product_id`       | `{{ shopping_cart.products[0].product_id }}`       |
| `product_name`     | `{{ shopping_cart.products[0].product_name }}`     |
| `variant_id`       | `{{ shopping_cart.products[0].variant_id }}`       |
| `image_url`        | `{{ shopping_cart.products[0].image_url }}`        |
| `product_url`      | `{{ shopping_cart.products[0].product_url }}`      |
| `quantity`         | `{{ shopping_cart.products[0].quantity }}`         |
| `price`            | `{{ shopping_cart.products[0].price }}`            |
| `sku`              | `{{ shopping_cart.products[0].metadata[0].sku }}`  |
| `source`           | `{{ shopping_cart.source }}`                        |
| `metadata (value)` | `{{ shopping_cart.metadata[0].<add_value_here> }}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert tip %}
Weitere Informationen darüber, wie Sie eine Liquid `for` -Schleife einrichten, um alle Produkte dynamisch in Ihre E-Mail einzufügen, finden Sie unter [Personalisierung von Produkten aus abgebrochenen Einkäufen für E-Mails]({{site.baseurl}}/ecommerce_use_cases/#abandoned-cart).
{% endalert %}

{% endsubtab %}
{% subtab Checkout started %}
**Veranstaltung**: `ecommerce.checkout_started`<br>
**Typ**: Empfohlene Veranstaltung<br>
**Ausgelöst**: Wenn eine Kund:in ihren Warenkorb hinzufügt, entfernt oder aktualisiert<br>
**Anwendungsfälle**: Abbruch der Kaufabwicklung

Für Abandoned Checkout Canvase müssen Sie zunächst den folgenden Liquid-Tag verwenden:

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
{{context.${cart_id}}}
```
{% endraw %}

Dann können Sie die folgenden Liquid-Tags in Ihre Nachricht einfügen, um die Produkte in Ihrem Warenkorb zu referenzieren, wenn Sie zur Kasse gehen.

{% raw %}
| Variable | Liquid Template |
\|------------------|-----------------------------------------------------|
| `cart_id`          | `{{ shopping_cart.cart_id }}`                       |
| `currency`         | `{{ shopping_cart.currency }}`                      |
| `total_value`      | `{{ shopping_cart.total_value }}`                   |
| `product_id`       | `{{ shopping_cart.products[0].product_id }}`       |
| `product_name`     | `{{ shopping_cart.products[0].product_name }}`     |
| `variant_id`       | `{{ shopping_cart.products[0].variant_id }}`       |
| `image_url`        | `{{ shopping_cart.products[0].image_url }}`        |
| `product_url`      | `{{ shopping_cart.products[0].product_url }}`      |
| `quantity`         | `{{ shopping_cart.products[0].quantity }}`         |
| `price`            | `{{ shopping_cart.products[0].price }}`            |
| `sku`              | `{{ shopping_cart.products[0].metadata.sku }}`     |
| `source`           | `{{ shopping_cart.source }}`                        |
| `checkout_url`     | `{{ shopping_cart.metadata[0].checkout_url }}`     |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Order placed %}
**Veranstaltung**: `ecommerce.order_placed`<br>
**Typ**: Empfohlene Veranstaltung<br>
**Ausgelöst**: Wenn ein Nutzer:innen den Bezahlvorgang erfolgreich abschließt und eine Bestellung aufgibt<br>
**Anwendungsfälle**: Auftragsbestätigung, Retargeting nach dem Kauf, Upsells oder Cross-Sells 

{% raw %}
| Variable | Liquid Template |
\|-------------------------|-----------------------------------------------------|
| cart_id                 | `{{event_properties.${cart_id}}}`                   |
| currency                | `{{event_properties.${currency}}}`                  |
| discounts               | `{{event_properties.${discounts}}}`                 |
| order_id                | `{{event_properties.${order_id}}}`                  |
| product_id              | `{{event_properties.${products}[0].product_id}}`   |
| product_name            | `{{event_properties.${products}[0].product_name}}` |
| variant_id              | `{{event_properties.${products}[0].variant_id}}`   |
| quantity                | `{{event_properties.${products}[0].quantity}}`     |
| sku                     | `{{event_properties.${products}[0].metadata.sku}}` |
| total_discounts         | `{{event_properties.${total_discounts}}}`           |
| order_status_url        | `{{event_properties.${metadata}.order_status_url}}` |
| order_number            | `{{event_properties.${metadata}.order_number}}`     |
| tags                    | `{{event_properties.${metadata}.tags}}`             |
| referring_site          | `{{event_properties.${metadata}.referring_site}}`   |
| payment_gateway_names    | `{{event_properties.${metadata}.payment_gateway_names}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert tip %}
Der Webhook "Kasse abgeschlossen" von Shopify enthält keine Produkt-URLs oder Bild-URLs. Infolgedessen müssen Sie die Personalisierung von Katalogen Liquid verwenden, wie unter [Personalisierung von Produkten aus abgebrochenen Einkäufen für E-Mails]({{site.baseurl}}/ecommerce_use_cases/#order-confirmation-and-feedback-survey) erwähnt.
{% endalert %}

{% endsubtab %}
{% subtab Fulfilled order %}
**Veranstaltung**: `shopify_fulfilled_order`<br>
**Typ**: [Angepasstes Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**Ausgelöst**: Wenn die Bestellung eines Nutzers:innen erfüllt und versandfertig ist<br>
**Anwendungsfälle**: (Transactional) Fulfillment Update 

{% raw %}
| Variable | Liquid Template |
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
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Partially fulfilled order %}
**Veranstaltung**: `shopify_partially_fulfilled_order`<br>
**Typ**: [Angepasstes Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**Ausgelöst**: Wenn ein Teil der Bestellung eines Nutzers:innen erfüllt und versandfertig ist<br> 
**Anwendungsfälle**: (Transactional) Fulfillment Update 

{% raw %}
| Variable | Liquid Template |
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
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Paid order %}
**Veranstaltung**: `shopify_paid_order`<br>
**Typ**: [Angepasstes Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**Ausgelöst**: Wenn die Bestellung eines Nutzers:innen in Shopify als bezahlt markiert wird<br>  
**Anwendungsfälle**: (Transaktion) Zahlungsbestätigung

{% raw %}
| Variable | Liquid Template |
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
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Order cancelled %}
**Veranstaltung**: `shopify_cancelled_order`<br>
**Typ**: [Angepasstes Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**Ausgelöst**: Wenn die Bestellung eines Nutzers:innen storniert wird<br> 
**Anwendungsfälle**: (Transaktion) Bestätigung der Auftragsstornierung

{% raw %}
| Variable | Liquid Template |
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
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}
{% endsubtab %}
{% subtab Order refunded %}
**Veranstaltung**: `shopify_order_refunded`<br>
**Typ**: [Angepasstes Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**Ausgelöst**: Wenn die Bestellung eines Nutzers:innen erstattet wird<br>
**Anwendungsfälle**: (Transaktion) Erstattungsbestätigung

{% raw %}
| Variable | Liquid Template |
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
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Account login %}

**Veranstaltung**: `shopify_account_login`<br>
**Typ**: [Angepasstes Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**Ausgelöst**: Wenn sich ein Nutzer:in bei seinem Konto anmeldet<br>
**Anwendungsfälle**: Serie Willkommen

{% raw %}
| Variable | Liquid Template |
| --- | --- |
| `source` | {{event_properties.${source}}} |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert note %}
Die Shopify-Integration unterstützt derzeit nicht das Auffüllen des [Kauf-Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-events) von Braze. Folglich sollten Kauf-Filter, Liquid-Tags, aktionsbasierte Trigger und Analytics das Ereignis ecommerce.order_placed verwenden.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Unterstützte angepasste Attribute von Shopify
{% tabs local %}
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
{% tab Shopify Angepasste Attribute %}
| Attribut Name | Beschreibung |
| --- | --- |
| `shopify_total_spent` | Der Gesamtbetrag, den der Kunde im Verlauf seiner Bestellung ausgegeben hat. |
| `shopify_order_count` | Die Anzahl der Bestellungen, die mit diesem Kund:in verbunden sind. Test- und archivierte Bestellungen werden nicht gezählt. |
| `shopify_last_order_id` | Die ID der letzten Bestellung des Kunden. |
| `shopify_last_order_name` | Der Name der letzten Bestellung der Kund:in. Dies steht in direktem Zusammenhang mit dem Feld `name` in der Auftragsressource. |
| `shopify_zipcode` | Die Postleitzahl der Kund:in aus ihrer Standardadresse. |
| `shopify_province` | Die Provinz der Kund:in aus ihrer Standardadresse. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Liquid Personalisierung

Um eine Liquid-Personalisierung für Ihre angepassten Attribute in Shopify hinzuzufügen, wählen Sie **\+ Personalisierung**. Wählen Sie dann als Personalisierungstyp **angepasste Attribute** aus.

![Der Bereich "Personalisierung hinzufügen" mit dem erweiterten Dropdown-Menü "Attribute".]({% image_buster /assets/img/Shopify/add_personalization_2.png %}){: style="max-width:40%;"}

Nachdem Sie Ihr angepasstes Attribut ausgewählt haben, geben Sie einen Standardattribut ein und kopieren das Liquid Snippet in Ihre Nachricht.

![Einfügen eines Liquid-Snippets in eine Nachricht.]({% image_buster /assets/img/Shopify/copy_liquid_snippet.png %})
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

## SDK Datenerfassung 

Weitere Informationen darüber, welche Daten von den Braze SDKs erfasst werden, finden Sie unter [SDK Datenerfassung]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/). 

## Historische Verfüllung

Während des Onboarding Ihres Shopify Shops können Sie eine erste Synchronisierung der Daten durch historische Backfills initiieren, um sich sofort mit Ihren Kunden zu engagieren. Im Rahmen dieses Backfill führt Braze eine erste Datensynchronisation aller Kunden und Bestellungen der letzten 90 Tage vor der Anbindung an Ihre Shopify Integration durch. Wenn Braze Ihre Shopify Kund:in importiert, weisen wir den `external_id` Typ zu, den Sie in Ihren Konfigurationseinstellungen gewählt haben.

{% alert note %}
Wenn Sie die Integration mit einer angepassten externen ID planen (entweder für die [Standardintegration]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-4-configure-how-you-manage-users) oder die [benutzerdefinierte Integration]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/#step-6-configure-how-you-manage-users-optional)), müssen Sie Ihre angepasste externe ID als Shopify-Kunden-Metafeld zu allen bestehenden Shopify-Kundenprofilen hinzufügen und dann den historischen Backfill durchführen.
{% endalert %}

### Einrichten der Shopify-Historienauffüllung

1. Aktivieren Sie das historische Backfill im Schritt **Tracking der Shopify Daten**.

![Der Schritt "Tracking von Shopify Daten" der Shopify Integration zeigt die ausgewählte historische Auffüllung an.]({% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %})

{: start="2"}

2. Nachdem Sie Ihre Integration eingerichtet haben, beginnt Braze mit der ersten Synchronisierung der Daten. Sie können den Fortschritt auf dem Tab **Shopify Daten** Ihrer Integrationseinstellungen überwachen. 

![Die Seite mit den Einstellungen für die Shopify Integration mit einer Anzeige, die anzeigt, dass die Ereignisse aktiv synchronisiert werden.]({% image_buster /assets/img/Shopify/historical_data_backfill_syncing.png %})

### Synchronisierte Daten 

Für die anfängliche Datensynchronisation importiert Braze Kunden und Bestellungen aus den letzten 90 Tagen vor der Verbindung mit Ihrer Shopify Integration. Wenn Braze Ihre Shopify Kund:in importiert, wird es den `external_id` Typ zuweisen, den Sie in Ihren Konfigurationseinstellungen gewählt haben.