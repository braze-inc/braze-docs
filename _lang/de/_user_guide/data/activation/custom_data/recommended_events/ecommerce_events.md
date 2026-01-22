---
nav_title: E-Commerce empfohlene Veranstaltungen
article_title: E-Commerce Empfohlene Veranstaltungen
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "Dieser referenzierte Artikel beschreibt die im E-Commerce empfohlenen Ereignisse und Eigenschaften, ihre Verwendung, Segmentierung, wo Sie die relevanten Analytics einsehen können und vieles mehr."
---

# E-Commerce empfohlene Veranstaltungen

> Diese Seite behandelt die im E-Commerce empfohlenen Ereignisse und Eigenschaften. Diese Ereignisse werden erstellt, um wichtige Einkaufsverhaltensweisen zu erfassen, die Marketer benötigen, um effektives Messaging zu triggern, wie z.B. das Targeting von abgebrochenen Warenkörben.

{% alert important %}
E-Commerce empfohlene Veranstaltungen sind derzeit im frühen Zugriff. Wenden Sie sich an Ihren Customer-Success-Manager:in von Braze, wenn Sie an diesem frühzeitigen Zugang teilnehmen möchten. <br><br>Wenn Sie den neuen [Shopify Konnektor]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector) verwenden, werden diese empfohlenen Ereignisse automatisch über die Integration verfügbar sein.
{% endalert %}

Braze weiß, dass die Planung von Daten Zeit braucht. Wir ermutigen unsere Kund:in, ihre Entwickler:in-Teams damit vertraut zu machen und jetzt mit dem Versand dieser Events zu beginnen. Auch wenn einige Features bei den empfohlenen E-Commerce-Ereignissen nicht sofort verfügbar sind, können Sie sich auf die Einführung neuer Produkte im Laufe des Jahres 2025 freuen, die Ihre E-Commerce-Funktionen verbessern werden.

## Empfohlene Arten von E-Commerce-Veranstaltungen

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

Jede gemeldete Nicht-USD-Währung wird in Braze in USD angezeigt, basierend auf dem Wechselkurs an dem Tag, an dem sie gemeldet wurde. Um eine Konversion zu verhindern, codieren Sie die Währung fest in USD.

{% tabs %}
{% tab ecommerce.product_viewed %}

Sie können das Ereignis "Produkt angesehen" verwenden, um zu triggern, wenn ein Kund:in eine Produktdetailseite blickt.

#### Eigenschaften

| Eigenschaftsname | Erforderlich | Datentyp | Beschreibung | 
|---|---|---|---|
| `product_id` | Ja | String | Ein eindeutiger Bezeichner für das Produkt, das angesehen wurde. <br> Für Kunden:in, die nicht Shopify sind, ist dies der Wert, den Sie für Katalogartikel-IDs wie SKUs festlegen. |
| `product_name` | Ja | String | Der Name des Produkts, das angesehen wurde. | 
| `variant_id` | Ja | String | Ein eindeutiger Bezeichner für die Variante des Produkts. Ein Beispiel ist `shirt_medium_blue` |
| `image_url` | Kein:e | String | URL des Bildes des Produkts. |
| `product_url` | Kein:e | String | URL zur Produktseite für weitere Details. |
| `price` | Ja | Gleitkommazahl | Der Stückpreis der Variante des Produkts zum Zeitpunkt der Betrachtung. |
| `currency` | Ja | String | Die Währung, in der der Preis des Produkts angegeben ist (z.B. "USD" oder "EUR"), im [Format ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `source` | Ja | String | Quelle, aus der das Ereignis stammt. (Bei Shopify ist dies die Storefront). |
| `metadata` | Kein:e | Objekt | |
| `type` | Kein:e | Objekt | Funktioniert mit [Back-in-Stock-Benachrichtigungen]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) und [Benachrichtigungen über Preissenkungen]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications). |
| `sku` | Kein:e | String | (nur Shopify) Shopify SKU. Dies kann als Feld für die Katalog ID konfiguriert werden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Beispielhafte Objekte

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.product_viewed", {
    "product_id": "4111176",
    "product_name": "Torchie runners",
    "variant_id": "4111176700",
    "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    "price": 85,
    "currency": "GBP",
    "source": "https://braze-apparel.com/",
    "metadata": {
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
BrazeProperties properties = new BrazeProperties()
    .addProperty("product_id", "4111176")
    .addProperty("product_name", "Torchie runners")
    .addProperty("variant_id", "4111176700")
    .addProperty("image_url", "https://braze-apparel.com/images/products/large/torchie-runners.jpg")
    .addProperty("product_url", "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/")
    .addProperty("price", 85)
    .addProperty("currency", "GBP")
    .addProperty("source", "https://braze-apparel.com/")
    .addProperty("metadata", new JSONObject()
        .put("sku", "")
        .put("color", "ORANGE")
        .put("size", "6")
        .put("brand", "Braze"));

Braze.getInstance(context).logCustomEvent("ecommerce.product_viewed", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let properties: [String: Any] = [
    "product_id": "4111176",
    "product_name": "Torchie runners",
    "variant_id": "4111176700",
    "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    "price": 85,
    "currency": "GBP",
    "source": "https://braze-apparel.com/",
    "metadata": [
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.product_viewed", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.product_viewed",
      "time": "2024-01-15T09:03:45Z",
      "properties": {
        "product_id": "4111176",
        "product_name": "Torchie runners",
        "variant_id": "4111176700",
        "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
        "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
        "price": 85,
        "currency": "GBP",
        "source": "https://braze-apparel.com/",
        "metadata": {
          "sku": "",
          "color": "ORANGE",
          "size": "6",
          "brand": "Braze"
        }
        "type": [
          "price_drop",
          "back_in_stock"
        ]
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.cart_updated %}

Sie können das Ereignis "Warenkorb aktualisiert" verwenden, um zu verfolgen, wann Produkte im Warenkorb hinzugefügt, entfernt oder aktualisiert werden. Das Ereignis `ecommerce.cart_updated` überprüft die folgenden Informationen, bevor es ausgelöst wird:

- Die Ereigniszeit ist größer als die `updated_at` Zeit für den spezifischen Warenkorb des Nutzers:in.
- Der Warenkorb ist noch nicht zur Kasse gegangen.
- Das Array `products` ist nicht leer.

#### Warenkorb Abbildung Objekt

Das Ereignis `ecommerce.cart_updated` verfügt über ein Objekt zur Abbildung von Warenkörben. Dieses Objekt wird für das Nutzerprofil erstellt, das eine Abbildung der Warenkörbe enthält, die alle Produkte im Warenkorb des Käufers enthalten. Sie können über den Liquid-Tag auf die Produkte in ihrem Warenkorb zugreifen: 

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

Wenn ein Warenkorb innerhalb von 10 Tagen nicht aktualisiert und zu einem Bestellvorgang weitergeleitet wurde, löschen wir den Warenkorb und die zugehörigen Produkte.

{% alert note %}
Produkte pro Warenkorb sind auf Braze nicht begrenzt. Das Limit von Shopify liegt jedoch bei 500.
{% endalert %}

#### Verhalten des Warenkorbs beim Zusammenführen von Nutzerprofilen

Wenn es zwei Warenkörbe gibt, fügen Sie beide dem zusammengeführten Nutzer:in hinzu. Stellen Sie das Canvas erneut in die Warteschlange, wenn es sich um denselben oder einen anderen Warenkorb handelt, um eine Nachricht mit den neuesten Warenkorb-Informationen zu senden. Das Ereignis `ecommerce.cart_updated` enthält die ID des letzten Warenkorbs und die Produkte, die sich im Warenkorb befinden.

#### Eigenschaften

| Eigenschaftsname | Erforderlich | Datentyp | Beschreibung | 
|---|---|---|---|
| `cart_id` | Ja | String | Eindeutiger Bezeichner für den Warenkorb. Wenn kein Wert übergeben wird, legen wir einen Standardwert für die Abbildung des Nutzer:innen-Warenkorbs fest (der für alle Warenkorb-, Checkout- und Bestell-Ereignisse gilt). |
| `total_value` | Ja | Gleitkommazahl | Gesamtwert des Warenkorbs. | 
| `currency` | Ja | String | Die Währung, in der der Preis des Produkts angegeben ist (z.B. "USD" oder "EUR"), im [Format ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `products` | Ja | Array |  |
| `product_id` | Ja | String | Ein eindeutiger Bezeichner für das Produkt, das angesehen wurde. <br> Dieser Wert kann die ID oder SKU des Produkts sein. |
| `product_name` | Ja | String | Der Name des Produkts, das angesehen wurde. |
| `variant_id` | Ja | String | Ein eindeutiger Bezeichner für die Variante des Produkts. Ein Beispiel ist `shirt_medium_blue` |
| `image_url` | Kein:e | String | URL des Bildes des Produkts. |
| `product_url` | Kein:e | String | URL zur Produktseite für weitere Details. |
| `quantity` | Ja | Integer | Anzahl der Einheiten des Produkts im Warenkorb. |
| `price` | Ja | Gleitkommazahl | Der Stückpreis der Variante des Produkts zum Zeitpunkt der Betrachtung. |
| `metadata` | Kein:e | Objekt | Zusätzliches Metadatenfeld über das Produkt, das der Kund:in für seine Anwendungsfälle hinzufügen möchte. Für Shopify werden wir SKU hinzufügen. <br> Das Limit basiert auf unserem allgemeinen Limit für Event-Eigenschaften von 50kb. |
| `sku` | Kein:e | String | (nur Shopify) Shopify SKU. Dies kann als Feld für die Katalog ID konfiguriert werden. |
| `source` | Ja | String | Quelle, aus der das Ereignis stammt. (Bei Shopify ist dies die Storefront). |
| `metadata` | Kein:e | Objekt | Zusätzliches Metadatenfeld über das Produkt, das der Kund:in für seine Anwendungsfälle hinzufügen möchte. Für Shopify werden wir SKU hinzufügen. <br> Das Limit basiert auf unserem allgemeinen Limit für Event-Eigenschaften von 50kb. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Beispielhafte Objekte

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
    "cart_id": "cart_12345",
    "currency": "USD",
    "total_value": 199.98,
    "products": [
        {
            "product_id": "8266836345064",
            "product_name": "Classic T-Shirt",
            "variant_id": "44610569208040",
            "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
            "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
            "quantity": 2,
            "price": 99.99,
            "metadata": {
                "sku": "TSH-BLU-M",
                "color": "BLUE",
                "size": "Medium",
                "brand": "Braze"
            }
        }
    ],
    "source": "https://braze-apparel.com",
    "metadata": {}
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "8266836345064")
    .put("product_name", "Classic T-Shirt")
    .put("variant_id", "44610569208040")
    .put("image_url", "https://braze-apparel.com/images/tshirt-blue-medium.jpg")
    .put("product_url", "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040")
    .put("quantity", 2)
    .put("price", 99.99)
    .put("metadata", new JSONObject()
        .put("sku", "TSH-BLU-M")
        .put("color", "BLUE")
        .put("size", "Medium")
        .put("brand", "Braze"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("cart_id", "cart_12345")
    .addProperty("currency", "USD")
    .addProperty("total_value", 199.98)
    .addProperty("products", products)
    .addProperty("source", "https://braze-apparel.com")
    .addProperty("metadata", new JSONObject());

Braze.getInstance(context).logCustomEvent("ecommerce.cart_updated", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let products: [[String: Any]] = [
    [
        "product_id": "8266836345064",
        "product_name": "Classic T-Shirt",
        "variant_id": "44610569208040",
        "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
        "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
        "quantity": 2,
        "price": 99.99,
        "metadata": [
            "sku": "TSH-BLU-M",
            "color": "BLUE",
            "size": "Medium",
            "brand": "Braze"
        ]
    ]
]

let properties: [String: Any] = [
    "cart_id": "cart_12345",
    "currency": "USD",
    "total_value": 199.98,
    "products": products,
    "source": "https://braze-apparel.com",
    "metadata": [:]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.cart_updated", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.cart_updated",
      "time": "2024-01-15T09:15:30Z",
      "properties": {
        "cart_id": "cart_12345",
        "currency": "USD",
        "total_value": 199.98,
        "products": [
          {
            "product_id": "8266836345064",
            "product_name": "Classic T-Shirt",
            "variant_id": "44610569208040",
            "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
            "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
            "quantity": 2,
            "price": 99.99,
            "metadata": {
              "sku": "TSH-BLU-M",
              "color": "BLUE",
              "size": "Medium",
              "brand": "Braze"
            }
          }
        ],
        "source": "https://braze-apparel.com",
        "metadata": {}
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.checkout_started %}

Sie können das Ereignis "Checkout started" verwenden, um Kunden:in zu retargeten, die den Checkout-Prozess begonnen, aber noch keine Bestellung aufgegeben haben.

Ähnlich wie das Ereignis `ecommerce.cart_updated` erlaubt Ihnen dieses Ereignis, den Liquid-Tag des Warenkorbs zu nutzen, um auf alle Produkte in ihrem Warenkorb zuzugreifen, um Nachrichten über abgebrochene Einkäufe zu erhalten:

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} :abort_if_not_abandoned false %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

#### Eigenschaften

| Eigenschaftsname | Erforderlich | Datentyp | Beschreibung | 
|---|---|---|---|
| `checkout_id` | Ja | String | Eindeutiger Bezeichner für den Checkout. |
| `cart_id` | Kein:e | String | Eindeutiger Bezeichner für den Warenkorb. Wenn kein Wert übergeben wird, legen wir einen Standardwert für die Abbildung des Nutzer:in-Warenkorbs fest (der für alle Warenkorb-, Checkout- und Bestell-Ereignisse gilt). | 
| `total_value` | Ja | Gleitkommazahl | Gesamtwert des Warenkorbs. |
| `currency` | Ja | String | Währung, in der der Warenkorb bewertet wird. |
| `products` | Ja | Array von Objekten |  |
| `product_id` | Ja | String | Ein eindeutiger Bezeichner für das Produkt, das angesehen wurde. Dieser Wert könnte zum Beispiel die ID oder SKU des Produkts sein. |
| `product_name` | Ja | String | Der Name des Produkts, das angesehen wurde.  |
| `variant_id` | Ja | String | Ein eindeutiger Bezeichner für die Variante des Produkts. Ein Beispiel ist `shirt_medium_blue` |
| `image_url` | Kein:e | String | URL des Bildes des Produkts. |
| `product_url` | Kein:e | String | URL zur Produktseite für weitere Details. |
| `quantity` | Ja | Integer | Anzahl der Einheiten des Produkts im Warenkorb. |
| `price` | Ja | Gleitkommazahl | Der Stückpreis der Variante des Produkts zum Zeitpunkt der Betrachtung. |
| `metadata` | Kein:e | Objekt | Zusätzliches Metadatenfeld über das Produkt, das der Kund:in für seine Anwendungsfälle hinzufügen möchte. Für Shopify werden wir SKU hinzufügen. <br> Das Limit basiert auf unserem allgemeinen Limit für Event-Eigenschaften von 50kb. |
| `sku` | Kein:e | String | (nur Shopify) Shopify SKU. Dies kann als Feld für die Katalog ID konfiguriert werden. |
| `source` | Ja | String | Quelle, aus der das Ereignis stammt. (Bei Shopify ist dies die Storefront). |
| `metadata` | Kein:e | Objekt |  |
| `checkout_url` | Kein:e | String | URL für die Kassenseite. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Beispielhafte Objekte

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.checkout_started", {
    "checkout_id": "checkout_abc123",
    "cart_id": "cart_12345",
    "total_value": 199.98,
    "currency": "USD",
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("checkout_id", "checkout_abc123")
    .addProperty("cart_id", "cart_12345")
    .addProperty("total_value", 199.98)
    .addProperty("currency", "USD")
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("checkout_url", "https://checkout.braze-audio.com/abc123"));

Braze.getInstance(context).logCustomEvent("ecommerce.checkout_started", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "checkout_id": "checkout_abc123",
    "cart_id": "cart_12345",
    "total_value": 199.98,
    "currency": "USD",
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.checkout_started", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.checkout_started",
      "time": "2024-01-15T09:25:45Z",
      "properties": {
        "checkout_id": "checkout_abc123",
        "cart_id": "cart_12345",
        "total_value": 199.98,
        "currency": "USD",
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "checkout_url": "https://checkout.braze-audio.com/abc123"
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_placed %}

Sie können das Ereignis "Bestellung aufgegeben" verwenden, um zu triggern, wenn ein Kund:in den Checkout-Prozess erfolgreich einsteigt und eine Bestellung aufgibt.

#### Eigenschaften

| Eigenschaftsname | Erforderlich | Datentyp | Beschreibung | 
|---|---|---|---|
| `order_id` | Ja | String | Eindeutiger Bezeichner für die aufgegebene Bestellung. |
| `cart_id` | Kein:e | String | Eindeutiger Bezeichner für den Warenkorb. Wenn kein Wert übergeben wird, legen wir einen Standardwert für die Abbildung des Nutzer:innen-Warenkorbs fest (der für alle Warenkorb-, Checkout- und Bestell-Ereignisse gilt). |
| `total_value` | Ja | Gleitkommazahl | Gesamtwert des Warenkorbs. | 
| `currency` | Ja | String | Währung, in der der Warenkorb bewertet wird. |
| `total_discounts` | Kein:e | Gleitkommazahl | Gesamtbetrag der auf die Bestellung angewandten Rabatte. | 
| `discounts`| Kein:e | Array von Objekten | Detaillierte Liste der auf die Bestellung angewandten Rabatte. |
| `products` | Ja | Array von Objekten |  |
| `product_id` | Ja | String | Ein eindeutiger Bezeichner für das Produkt, das angesehen wurde. Dieser Wert kann die ID oder SKU des Produkts sein. |
| `product_name` | Ja | String | Der Name des Produkts, das angesehen wurde. |
| `variant_id` | Ja | String | Ein eindeutiger Bezeichner für die Variante des Produkts. Ein Beispiel ist `shirt_medium_blue` |
| `image_url` | Kein:e | String | URL des Bildes des Produkts. |
| `product_url` | Kein:e | String | URL zur Produktseite für weitere Details. |
| `quantity` | Ja | Integer | Anzahl der Einheiten des Produkts im Warenkorb. |
| `price` | Ja | Gleitkommazahl | Der Stückpreis der Variante des Produkts zum Zeitpunkt der Betrachtung. |
| `metadata` | Kein:e | Objekt | Zusätzliches Metadatenfeld über das Produkt, das der Kund:in für seine Anwendungsfälle hinzufügen möchte. Für Shopify werden wir SKU hinzufügen. <br> Das Limit basiert auf unserem allgemeinen Limit für Event-Eigenschaften von 50kb. |
| `sku` | Kein:e | String | (nur Shopify) Shopify SKU. Dies kann als Feld für die Katalog ID konfiguriert werden. |
| `source` | Ja | String | Quelle, aus der das Ereignis stammt. (Bei Shopify ist dies die Storefront). |
| `metadata` | Kein:e | Objekt |  |
| `order_status_url` | Kein:e | String | URL, um den Status der Bestellung einzusehen. |
| `order_number` | Kein:e | String | (nur Shopify) Eindeutige Bestellnummer für die aufgegebene Bestellung. |
| `tags` | Kein:e | Array | (nur Shopify) Tags für Bestellungen
| `referring_site` | Kein:e | String | (nur Shopify) Die Website, von der die Bestellung stammt (z.B. Meta). |
| `payment_gateway_names` | Kein:e | Array | (nur Shopify) Quelle des Bezahlsystems (z.B. Point of Sale oder Mobile). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Beispielhafte Objekte

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_placed", {
    "order_id": "order_67890",
    "cart_id": "cart_12345",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": [
        {
            "code": "SAVE10",
            "amount": 10.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE10")
    .put("amount", 10.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("cart_id", "cart_12345")
    .addProperty("total_value", 189.98)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 10.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("electronics").put("audio"))
        .put("referring_site", "https://www.e-referrals.com")
        .put("payment_gateway_names", new JSONArray().put("tap2pay").put("dotcash")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_placed", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE10",
        "amount": 10.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "cart_id": "cart_12345",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_placed", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_placed",
      "time": "2024-01-15T09:35:20Z",
      "properties": {
        "order_id": "order_67890",
        "cart_id": "cart_12345",
        "total_value": 189.98,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
          {
            "code": "SAVE10",
            "amount": 10.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_number": "ORD-2024-001234",
          "tags": ["electronics", "audio"],
          "referring_site": "https://www.e-referrals.com",
          "payment_gateway_names": ["tap2pay", "dotcash"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_refunded %}

Sie können das Ereignis Bestellung erstattet verwenden, um zu triggern, wenn eine Bestellung ganz oder teilweise erstattet wird.

#### Eigenschaften

| Eigenschaftsname       | Erforderlich | Datentyp | Beschreibung   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | Ja      | String    | Eindeutiger Bezeichner für die aufgegebene Bestellung.        |
| `total_value`         | Ja      | Gleitkommazahl     | Gesamtwert des Warenkorbs.    |
| `currency`            | Ja      | String    | Währung, in der der Warenkorb bewertet wird.    |
| `total_discounts`     | Kein:e       | Gleitkommazahl     | Gesamtbetrag der auf die Bestellung angewandten Rabatte.   |
| `discounts`           | Kein:e       | Array von Objekten     | Detaillierte Liste der auf die Bestellung angewandten Rabatte. |
| `products`            | Ja      | Array von Objekten     |  |
| `product_id`       | Ja      | String    | Ein eindeutiger Bezeichner für das Produkt, das angesehen wurde. Dieser Wert kann die ID des Produkts, die SKU oder etwas Ähnliches sein. <br>Wenn eine Teilerstattung ausgestellt wird und der Erstattung keine `product_id` zugeordnet ist (z.B. eine Erstattung auf Auftragsebene), geben Sie eine allgemeine `product_id` an.             |
| `product_name`     | Ja      | String    | Der Name des Produkts, das angesehen wurde.                                                                      |
| `variant_id`       | Ja      | String    | Ein eindeutiger Bezeichner für die Variante des Produkts (z.B. `shirt_medium_blue`).                                         |
| `image_url`        | Kein:e       | String    | URL des Bildes des Produkts.     |
| `product_url`      | Kein:e       | String    | URL zur Produktseite für weitere Details.  |
| `quantity`         | Ja      | Integer   | Anzahl der Einheiten des Produkts im Warenkorb.   |
| `price`            | Ja      | Gleitkommazahl     | Der Stückpreis der Variante des Produkts zum Zeitpunkt der Betrachtung.  |
| `metadata`         | Kein:e       | Objekt    | Zusätzliches Metadatenfeld über das Produkt, das der Kund:in für seine Anwendungsfälle hinzufügen möchte. Für Shopify werden wir SKU hinzufügen. Das Limit basiert auf unserem allgemeinen Limit für Event-Eigenschaften von 50kb. |
| `sku`            | Kein:e       | String    | (nur Shopify) Shopify SKU. Dies kann als Feld für die Katalog ID konfiguriert werden.  |
| `source`              | Ja      | String    | Quelle, aus der das Ereignis stammt. (Bei Shopify ist dies die Storefront).    |
| `metadata`            | Kein:e       | Objekt    |                |
| `order_status_url`  | Kein:e       | String    | URL, um den Status der Bestellung einzusehen.     |
| `order_note`       | Kein:e       | String    | (nur Shopify) Notiz, die der Händler der Bestellung beifügt.    |
| `order_number`     | Kein:e       | String    | (nur Shopify) Eindeutige Bestellnummer für die aufgegebene Bestellung.   |
| `tags`             | Kein:e       | Array     | (nur Shopify) Tags bestellen.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Beispielhafte Objekte

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_refunded", {
    "order_id": "order_67890",
    "total_value": 99.99,
    "currency": "USD",
    "total_discounts": 5.00,
    "discounts": [
        {
            "code": "SAVE5",
            "amount": 5.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 99.99,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_note": "Customer requested refund due to defective item",
        "order_number": "ORD-2024-001234",
        "tags": ["refund", "defective"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE5")
    .put("amount", 5.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 99.99)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("total_value", 99.99)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 5.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_note", "Customer requested refund due to defective item")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("refund").put("defective")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_refunded", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE5",
        "amount": 5.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 99.99,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "total_value": 99.99,
    "currency": "USD",
    "total_discounts": 5.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_note": "Customer requested refund due to defective item",
        "order_number": "ORD-2024-001234",
        "tags": ["refund", "defective"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_refunded", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_refunded",
      "time": "2024-01-15T10:15:30Z",
      "properties": {
        "order_id": "order_67890",
        "total_value": 99.99,
        "currency": "USD",
        "total_discounts": 5.00,
        "discounts": [
          {
            "code": "SAVE5",
            "amount": 5.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 99.99,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_note": "Customer requested refund due to defective item",
          "order_number": "ORD-2024-001234",
          "tags": ["refund", "defective"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_cancelled %}

Sie können das Ereignis Bestellung storniert verwenden, um zu triggern, wenn eine Kund:in eine Bestellung storniert.

#### Eigenschaften

| Eigenschaftsname      | Erforderlich | Datentyp | Beschreibung       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | Ja      | String    | Eindeutiger Bezeichner für die aufgegebene Bestellung.              |
| `cancel_reason`       | Ja      | String    | Grund, warum die Bestellung storniert wurde.           |
| `total_value`         | Ja      | Gleitkommazahl     | Gesamtwert des Warenkorbs.         |
| `currency`            | Ja      | String    | Währung, in der der Warenkorb bewertet wird.           |
| `total_discounts`     | Kein:e       | Gleitkommazahl     | Gesamtbetrag der auf die Bestellung angewandten Rabatte.     |
| `discounts`           | Kein:e       | Array von Objekten     | Detaillierte Liste der auf die Bestellung angewandten Rabatte.             |
| `products`            | Ja      | Array von Objekten     |         |
| `product_id`          | Ja      | String    | Ein eindeutiger Bezeichner für das Produkt, das angesehen wurde. Dieser Wert kann die ID des Produkts, die SKU oder etwas Ähnliches sein.             |
| `product_name`        | Ja      | String    | Der Name des Produkts, das angesehen wurde.          |
| `variant_id`          | Ja      | String    | Ein eindeutiger Bezeichner für die Variante des Produkts (z.B. `shirt_medium_blue`).        |
| `image_url`           | Kein:e       | String    | URL des Bildes des Produkts.           |
| `product_url`         | Kein:e       | String    | URL zur Produktseite für weitere Details.                                                                     |
| `quantity`            | Ja      | Integer   | Anzahl der Einheiten des Produkts im Warenkorb.        |
| `price`               | Ja      | Gleitkommazahl     | Der Stückpreis der Variante des Produkts zum Zeitpunkt der Betrachtung.     |
| `metadata`            | Kein:e       | Objekt    | Zusätzliches Metadatenfeld über das Produkt, das der Kund:in für seine Anwendungsfälle hinzufügen möchte. Für Shopify werden wir SKU hinzufügen. Das Limit basiert auf unserem allgemeinen Limit für Event-Eigenschaften von 50kb. |
| `sku`                 | Kein:e       | String    | (nur Shopify) Shopify SKU. Dies kann als Feld für die Katalog ID konfiguriert werden.        |
| `source`              | Ja      | String    | Quelle, aus der das Ereignis stammt. (Bei Shopify ist dies die Storefront).    |
| `metadata`            | Kein:e       | Objekt    |       |
| `order_status_url`    | Kein:e       | String    | URL, um den Status der Bestellung einzusehen.                                                                          |
| `order_number`        | Kein:e       | String    | (nur Shopify) Eindeutige Bestellnummer für die aufgegebene Bestellung.  |
| `tags`                | Kein:e       | Array     | (nur Shopify) Tags bestellen.            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Beispielhafte Objekte

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_cancelled", {
    "order_id": "order_67890",
    "cancel_reason": "customer changed mind",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": [
        {
            "code": "SAVE10",
            "amount": 10.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["cancelled", "customer_request"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE10")
    .put("amount", 10.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("cancel_reason", "customer changed mind")
    .addProperty("total_value", 189.98)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 10.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("cancelled").put("customer_request")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_cancelled", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE10",
        "amount": 10.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "cancel_reason": "customer changed mind",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["cancelled", "customer_request"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_cancelled", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_cancelled",
      "time": "2024-01-15T10:45:15Z",
      "properties": {
        "order_id": "order_67890",
        "cancel_reason": "customer changed mind",
        "total_value": 189.98,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
          {
            "code": "SAVE10",
            "amount": 10.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_number": "ORD-2024-001234",
          "tags": ["cancelled", "customer_request"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

## E-Commerce Canvas Templates

Braze hat speziell entwickelte Canvas-Templates entwickelt, die sich auf die im E-Commerce empfohlenen Events stützen, z. B. das Targeting von Kund:inen, die den Checkout-Prozess begonnen, aber vor der Bestellung verlassen haben. Sie können diese Ereignisse nutzen, um fundierte Entscheidungen zu treffen und Ihre Nutzer:innen durch Personalisierung von Nachrichten und Targeting mit bestimmten Zielgruppen zu erreichen.

In unseren speziellen [Anwendungsfällen für E-Commerce]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases) finden Sie weitere Möglichkeiten, wie Sie diese Ereignisse mit Canvas Templates nutzen können.

## Nutzer:innen berechnete Felder

Wir verwenden standardisierte Nutzer:innen Feldberechnungen für die folgenden Felder: 

- **Gesamteinnahmen** = Summe des Gesamtwerts der erteilten Aufträge - Summe des Gesamtwerts der erstatteten Aufträge
- **Gesamtzahl der Bestellungen** = Anzahl der eindeutigen Bestellungsereignisse - Anzahl der eindeutigen Stornierungen von Bestellungen
- **Gesamterstattungswert** = Summe des gesamten erstatteten Auftragswerts 

Diese Benutzerfeldberechnungen sind auch auf dem Tab **Transaktionen** der Nutzerprofile enthalten.

![Der Tab "Transaktionen" mit von Nutzer:innen berechneten Feldern.]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:60%;"}
