---
nav_title: Empfohlene E-Commerce-Events
article_title: Empfohlene E-Commerce-Events
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "Dieser Referenzartikel beschreibt empfohlene E-Commerce-Events und -Eigenschaften, deren Verwendung, Segmentierung, wo Sie die relevanten Analytics einsehen können und mehr."
---

# Empfohlene E-Commerce-Events

> Diese Seite behandelt empfohlene E-Commerce-Events und -Eigenschaften. Diese Events werden erstellt, um wichtige Einkaufsverhaltensweisen zu erfassen, die Marketer benötigen, um effektives Messaging zu triggern – beispielsweise das Targeting von Warenkorb-Abbrüchen.

{% alert important %}
Empfohlene E-Commerce-Events befinden sich derzeit im Early Access. Wenden Sie sich an Ihren Customer-Success-Manager bei Braze, wenn Sie an diesem Early Access teilnehmen möchten. <br><br>Wenn Sie den neuen [Shopify-Konnektor]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector) verwenden, stehen diese empfohlenen Events automatisch über die Integration zur Verfügung.
{% endalert %}

Braze weiß, dass die Planung von Daten Zeit braucht. Wir ermutigen unsere Kund:innen, ihre Entwickler:innen-Teams damit vertraut zu machen und jetzt mit dem Versand dieser Events zu beginnen. Auch wenn einige Features bei den empfohlenen E-Commerce-Events nicht sofort verfügbar sind, können Sie sich auf die Einführung neuer Produkte im Laufe des Jahres 2025 freuen, die Ihre E-Commerce-Funktionen erweitern werden.

## Arten empfohlener E-Commerce-Events

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

Alle gemeldeten Nicht-USD-Währungen werden in Braze auf Basis des Wechselkurses am Tag der Meldung in USD angezeigt. Um eine Währungskonversion zu vermeiden, legen Sie die Währung fest auf USD fest.

{% tabs %}
{% tab ecommerce.product_viewed %}

Sie können das Event „Produkt angesehen" verwenden, um zu triggern, wenn eine Kund:in eine Produktdetailseite aufruft.

#### Eigenschaften

| Eigenschaftsname | Erforderlich | Datentyp | Beschreibung | 
|---|---|---|---|
| `product_id` | Ja | String | Ein eindeutiger Bezeichner für das angesehene Produkt. <br> Für Kund:innen, die nicht Shopify nutzen, ist dies der Wert, den Sie für Katalogartikel-IDs wie SKUs festlegen. |
| `product_name` | Ja | String | Der Name des angesehenen Produkts. | 
| `variant_id` | Ja | String | Ein eindeutiger Bezeichner für die Produktvariante. Ein Beispiel ist `shirt_medium_blue`. |
| `image_url` | Nein | String | URL des Produktbilds. |
| `product_url` | Nein | String | URL zur Produktseite für weitere Details. |
| `price` | Ja | Gleitkommazahl | Der Stückpreis der Produktvariante zum Zeitpunkt der Betrachtung. |
| `currency` | Ja | String | Die Währung, in der der Produktpreis angegeben ist (z. B. „USD" oder „EUR"), im [ISO-4217-Format](https://www.iso.org/iso-4217-currency-codes.html). |
| `source` | Ja | String | Quelle, aus der das Event stammt. (Bei Shopify ist dies die Storefront). |
| `metadata` | Nein | Objekt | |
| `type` | Nein | Objekt | Funktioniert mit [Wieder-verfügbar-Benachrichtigungen]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) und [Preissenkungsbenachrichtigungen]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications). |
| `sku` | Nein | String | (Nur Shopify) Shopify SKU. Dies kann als Katalog-ID-Feld konfiguriert werden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Beispielobjekte

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
        },
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

Sie können den Trigger **Warenkorb-Aktualisierung durchführen** verwenden, um zu verfolgen, wann Produkte im Warenkorb hinzugefügt, entfernt oder aktualisiert werden. Dieses Event überprüft die folgenden Informationen, bevor es ausgelöst wird:

- Die Event-Zeit ist größer als die `updated_at`-Zeit für den spezifischen Warenkorb der Nutzer:in.
- Der Warenkorb ist noch nicht zum Checkout-Prozess übergegangen.
- Das `products`-Array ist nicht leer.

#### Warenkorb-Abbildungsobjekt

Das `ecommerce.cart_updated`-Event verfügt über ein Warenkorb-Abbildungsobjekt. Dieses Objekt wird für das Nutzerprofil erstellt und enthält eine Abbildung der Warenkörbe mit allen Produkten im Warenkorb der Käufer:in. Sie können über den Liquid-Tag auf die Produkte im Warenkorb zugreifen: 

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

Wenn ein Warenkorb innerhalb von 10 Tagen nicht aktualisiert wurde und nicht zu einem Bestellungs-Event übergegangen ist, löschen wir den Warenkorb und die zugehörigen Produkte.

{% alert note %}
Produkte pro Warenkorb sind bei Braze nicht begrenzt. Das Limit von Shopify liegt jedoch bei 500.
{% endalert %}

#### Warenkorb-Verhalten beim Zusammenführen von Nutzerprofilen

Wenn es zwei Warenkörbe gibt, werden beide der zusammengeführten Nutzer:in hinzugefügt. Stellen Sie den Canvas erneut in die Warteschlange – unabhängig davon, ob es sich um denselben oder einen anderen Warenkorb handelt –, um eine Nachricht mit den aktuellsten Warenkorb-Informationen zu senden. Das `ecommerce.cart_updated`-Event enthält die letzte Warenkorb-ID und die letzten Produkte im Warenkorb.

#### Eigenschaften

| Eigenschaftsname | Erforderlich | Datentyp | Beschreibung | 
|---|---|---|---|
| `cart_id` | Ja | String | Falls Sie keine Drittanbieterplattform verwenden, die eine `cart_id` bereitstellt, können Sie die [Braze-Session-ID]({{site.baseurl}}/developer_guide/analytics/tracking_sessions) verwenden. |
| `total_value` | Ja | Gleitkommazahl | Gesamter Geldwert des Warenkorbs. | 
| `currency` | Ja | String | Die Währung, in der der Produktpreis angegeben ist (z. B. „USD" oder „EUR"), im [ISO-4217-Format](https://www.iso.org/iso-4217-currency-codes.html). |
| `products` | Ja | Array |  |
| `product_id` | Ja | String | Ein eindeutiger Bezeichner für das angesehene Produkt. <br> Dieser Wert kann die Produkt-ID oder SKU sein. |
| `product_name` | Ja | String | Der Name des angesehenen Produkts. |
| `variant_id` | Ja | String | Ein eindeutiger Bezeichner für die Produktvariante. Ein Beispiel ist `shirt_medium_blue`. |
| `image_url` | Nein | String | URL des Produktbilds. |
| `product_url` | Nein | String | URL zur Produktseite für weitere Details. |
| `quantity` | Ja | Integer | Anzahl der Einheiten des Produkts im Warenkorb. |
| `price` | Ja | Gleitkommazahl | Der Stückpreis der Produktvariante zum Zeitpunkt der Betrachtung. |
| `metadata` | Nein | Objekt | Zusätzliches Metadatenfeld über das Produkt, das die Kund:in für ihre Anwendungsfälle hinzufügen möchte. Für Shopify wird SKU hinzugefügt. <br> Das Limit basiert auf unserem allgemeinen Limit für Event-Eigenschaften von 50 KB. |
| `sku` | Nein | String | (Nur Shopify) Shopify SKU. Dies kann als Katalog-ID-Feld konfiguriert werden. |
| `source` | Ja | String | Quelle, aus der das Event stammt. (Bei Shopify ist dies die Storefront). |
| `metadata` | Nein | Objekt | Zusätzliches Metadatenfeld über das Produkt, das die Kund:in für ihre Anwendungsfälle hinzufügen möchte. Für Shopify wird SKU hinzugefügt. <br> Das Limit basiert auf unserem allgemeinen Limit für Event-Eigenschaften von 50 KB. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Beispielobjekte

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

Sie können das Event „Checkout gestartet" verwenden, um Kund:innen zu retargeten, die den Checkout-Prozess begonnen, aber noch keine Bestellung aufgegeben haben.

Ähnlich wie das `ecommerce.cart_updated`-Event ermöglicht Ihnen dieses Event, den Warenkorb-Liquid-Tag zu nutzen, um auf alle Produkte im Warenkorb für Nachrichten bei abgebrochenem Checkout zuzugreifen:

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
| `cart_id` | Nein | String | Falls Sie keine Drittanbieterplattform verwenden, die eine `cart_id` bereitstellt, können Sie die [Braze-Session-ID]({{site.baseurl}}/developer_guide/analytics/tracking_sessions) verwenden. | 
| `total_value` | Ja | Gleitkommazahl | Gesamter Geldwert des Warenkorbs. |
| `currency` | Ja | String | Währung, in der der Warenkorb bewertet wird. |
| `products` | Ja | Array von Objekten |  |
| `product_id` | Ja | String | Ein eindeutiger Bezeichner für das angesehene Produkt. Dieser Wert könnte z. B. die Produkt-ID oder SKU sein. |
| `product_name` | Ja | String | Der Name des angesehenen Produkts.  |
| `variant_id` | Ja | String | Ein eindeutiger Bezeichner für die Produktvariante. Ein Beispiel ist `shirt_medium_blue`. |
| `image_url` | Nein | String | URL des Produktbilds. |
| `product_url` | Nein | String | URL zur Produktseite für weitere Details. |
| `quantity` | Ja | Integer | Anzahl der Einheiten des Produkts im Warenkorb. |
| `price` | Ja | Gleitkommazahl | Der Stückpreis der Produktvariante zum Zeitpunkt der Betrachtung. |
| `metadata` | Nein | Objekt | Zusätzliches Metadatenfeld über das Produkt, das die Kund:in für ihre Anwendungsfälle hinzufügen möchte. Für Shopify wird SKU hinzugefügt. <br> Das Limit basiert auf unserem allgemeinen Limit für Event-Eigenschaften von 50 KB. |
| `sku` | Nein | String | (Nur Shopify) Shopify SKU. Dies kann als Katalog-ID-Feld konfiguriert werden. |
| `source` | Ja | String | Quelle, aus der das Event stammt. (Bei Shopify ist dies die Storefront). |
| `metadata` | Nein | Objekt |  |
| `checkout_url` | Nein | String | URL für die Checkout-Seite. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Beispielobjekte

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

Sie können das Event „Bestellung aufgegeben" verwenden, um zu triggern, wenn eine Kund:in den Checkout-Prozess erfolgreich abschließt und eine Bestellung aufgibt.

#### Eigenschaften

| Eigenschaftsname | Erforderlich | Datentyp | Beschreibung | 
|---|---|---|---|
| `order_id` | Ja | String | Eindeutiger Bezeichner für die aufgegebene Bestellung. |
| `cart_id` | Nein | String | Falls Sie keine Drittanbieterplattform verwenden, die eine `cart_id` bereitstellt, können Sie die [Braze-Session-ID]({{site.baseurl}}/developer_guide/analytics/tracking_sessions) verwenden. |
| `total_value` | Ja | Gleitkommazahl | Gesamter Geldwert des Warenkorbs. | 
| `currency` | Ja | String | Währung, in der der Warenkorb bewertet wird. |
| `total_discounts` | Nein | Gleitkommazahl | Gesamtbetrag der auf die Bestellung angewandten Rabatte. | 
| `discounts`| Nein | Array von Objekten | Detaillierte Liste der auf die Bestellung angewandten Rabatte. |
| `products` | Ja | Array von Objekten |  |
| `product_id` | Ja | String | Ein eindeutiger Bezeichner für das angesehene Produkt. Dieser Wert kann die Produkt-ID oder SKU sein. |
| `product_name` | Ja | String | Der Name des angesehenen Produkts. |
| `variant_id` | Ja | String | Ein eindeutiger Bezeichner für die Produktvariante. Ein Beispiel ist `shirt_medium_blue`. |
| `image_url` | Nein | String | URL des Produktbilds. |
| `product_url` | Nein | String | URL zur Produktseite für weitere Details. |
| `quantity` | Ja | Integer | Anzahl der Einheiten des Produkts im Warenkorb. |
| `price` | Ja | Gleitkommazahl | Der Stückpreis der Produktvariante zum Zeitpunkt der Betrachtung. |
| `metadata` | Nein | Objekt | Zusätzliches Metadatenfeld über das Produkt, das die Kund:in für ihre Anwendungsfälle hinzufügen möchte. Für Shopify wird SKU hinzugefügt. <br> Das Limit basiert auf unserem allgemeinen Limit für Event-Eigenschaften von 50 KB. |
| `sku` | Nein | String | (Nur Shopify) Shopify SKU. Dies kann als Katalog-ID-Feld konfiguriert werden. |
| `source` | Ja | String | Quelle, aus der das Event stammt. (Bei Shopify ist dies die Storefront). |
| `order_status_url` | Nein | String | URL, um den Status der Bestellung einzusehen. |
| `order_number` | Nein | String | (Nur Shopify) Eindeutige Bestellnummer für die aufgegebene Bestellung. |
| `tags` | Nein | Array | (Nur Shopify) Bestell-Tags.
| `referring_site` | Nein | String | (Nur Shopify) Die Website, von der die Bestellung stammt (z. B. Meta). |
| `payment_gateway_names` | Nein | Array | (Nur Shopify) Quelle des Zahlungssystems (z. B. Point of Sale oder Mobilgerät). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Beispielobjekte

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

Sie können das Event „Bestellung erstattet" verwenden, um zu triggern, wenn eine Bestellung ganz oder teilweise erstattet wird.

#### Eigenschaften

| Eigenschaftsname       | Erforderlich | Datentyp | Beschreibung   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | Ja      | String    | Eindeutiger Bezeichner für die aufgegebene Bestellung.        |
| `total_value`         | Ja      | Gleitkommazahl     | Gesamter Geldwert des Warenkorbs.    |
| `currency`            | Ja      | String    | Währung, in der der Warenkorb bewertet wird.    |
| `total_discounts`     | Nein       | Gleitkommazahl     | Gesamtbetrag der auf die Bestellung angewandten Rabatte.   |
| `discounts`           | Nein       | Array von Objekten     | Detaillierte Liste der auf die Bestellung angewandten Rabatte. |
| `products`            | Ja      | Array von Objekten     |  |
| `product_id`       | Ja      | String    | Ein eindeutiger Bezeichner für das angesehene Produkt. Dieser Wert kann die Produkt-ID, SKU oder Ähnliches sein. <br>Wenn eine Teilerstattung ausgestellt wird und der Erstattung keine `product_id` zugeordnet ist (z. B. eine Erstattung auf Bestellebene), geben Sie eine allgemeine `product_id` an.             |
| `product_name`     | Ja      | String    | Der Name des angesehenen Produkts.                                                                      |
| `variant_id`       | Ja      | String    | Ein eindeutiger Bezeichner für die Produktvariante (z. B. `shirt_medium_blue`).                                         |
| `image_url`        | Nein       | String    | URL des Produktbilds.     |
| `product_url`      | Nein       | String    | URL zur Produktseite für weitere Details.  |
| `quantity`         | Ja      | Integer   | Anzahl der Einheiten des Produkts im Warenkorb.   |
| `price`            | Ja      | Gleitkommazahl     | Der Stückpreis der Produktvariante zum Zeitpunkt der Betrachtung.  |
| `metadata`         | Nein       | Objekt    | Zusätzliches Metadatenfeld über das Produkt, das die Kund:in für ihre Anwendungsfälle hinzufügen möchte. Für Shopify wird SKU hinzugefügt. Das Limit basiert auf unserem allgemeinen Limit für Event-Eigenschaften von 50 KB. |
| `sku`            | Nein       | String    | (Nur Shopify) Shopify SKU. Dies kann als Katalog-ID-Feld konfiguriert werden.  |
| `source`              | Ja      | String    | Quelle, aus der das Event stammt. (Bei Shopify ist dies die Storefront).    |
| `metadata`            | Nein       | Objekt    |                |
| `order_status_url`  | Nein       | String    | URL, um den Status der Bestellung einzusehen.     |
| `order_note`       | Nein       | String    | (Nur Shopify) Notiz, die der Händler der Bestellung beigefügt hat.    |
| `order_number`     | Nein       | String    | (Nur Shopify) Eindeutige Bestellnummer für die aufgegebene Bestellung.   |
| `tags`             | Nein       | Array     | (Nur Shopify) Bestell-Tags.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Beispielobjekte

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

Sie können das Event „Bestellung storniert" verwenden, um zu triggern, wenn eine Kund:in eine Bestellung storniert.

#### Eigenschaften

| Eigenschaftsname      | Erforderlich | Datentyp | Beschreibung       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | Ja      | String    | Eindeutiger Bezeichner für die aufgegebene Bestellung.              |
| `cancel_reason`       | Ja      | String    | Grund, warum die Bestellung storniert wurde.           |
| `total_value`         | Ja      | Gleitkommazahl     | Gesamter Geldwert des Warenkorbs.         |
| `currency`            | Ja      | String    | Währung, in der der Warenkorb bewertet wird.           |
| `total_discounts`     | Nein       | Gleitkommazahl     | Gesamtbetrag der auf die Bestellung angewandten Rabatte.     |
| `discounts`           | Nein       | Array von Objekten     | Detaillierte Liste der auf die Bestellung angewandten Rabatte.             |
| `products`            | Ja      | Array von Objekten     |         |
| `product_id`          | Ja      | String    | Ein eindeutiger Bezeichner für das angesehene Produkt. Dieser Wert kann die Produkt-ID, SKU oder Ähnliches sein.             |
| `product_name`        | Ja      | String    | Der Name des angesehenen Produkts.          |
| `variant_id`          | Ja      | String    | Ein eindeutiger Bezeichner für die Produktvariante (z. B. `shirt_medium_blue`).        |
| `image_url`           | Nein       | String    | URL des Produktbilds.           |
| `product_url`         | Nein       | String    | URL zur Produktseite für weitere Details.                                                                     |
| `quantity`            | Ja      | Integer   | Anzahl der Einheiten des Produkts im Warenkorb.        |
| `price`               | Ja      | Gleitkommazahl     | Der Stückpreis der Produktvariante zum Zeitpunkt der Betrachtung.     |
| `metadata`            | Nein       | Objekt    | Zusätzliches Metadatenfeld über das Produkt, das die Kund:in für ihre Anwendungsfälle hinzufügen möchte. Für Shopify wird SKU hinzugefügt. Das Limit basiert auf unserem allgemeinen Limit für Event-Eigenschaften von 50 KB. |
| `sku`                 | Nein       | String    | (Nur Shopify) Shopify SKU. Dies kann als Katalog-ID-Feld konfiguriert werden.        |
| `source`              | Ja      | String    | Quelle, aus der das Event stammt. (Bei Shopify ist dies die Storefront).    |
| `metadata`            | Nein       | Objekt    |       |
| `order_status_url`    | Nein       | String    | URL, um den Status der Bestellung einzusehen.                                                                          |
| `order_number`        | Nein       | String    | (Nur Shopify) Eindeutige Bestellnummer für die aufgegebene Bestellung.  |
| `tags`                | Nein       | Array     | (Nur Shopify) Bestell-Tags.            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Beispielobjekte

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

## E-Commerce Canvas-Templates

Braze hat vorgefertigte Canvas-Templates erstellt, die auf empfohlenen E-Commerce-Events basieren – z. B. das Targeting von Kund:innen, die den Checkout-Prozess begonnen, aber vor der Bestellung abgebrochen haben. Sie können diese Events nutzen, um fundierte Entscheidungen zu treffen und die User Journey durch personalisiertes Messaging und gezieltes Targeting bestimmter Zielgruppen zu verbessern.

In unseren speziellen [E-Commerce-Anwendungsfällen]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases) finden Sie weitere Möglichkeiten, wie Sie diese Events mit Canvas-Templates nutzen können.

## Berechnete Nutzerfelder

Wir verwenden standardisierte Berechnungen für die folgenden Nutzerfelder: 

- **Gesamtumsatz** = Summe des Gesamtwerts aufgegebener Bestellungen - Summe des Gesamtwerts erstatteter Bestellungen
- **Gesamtanzahl Bestellungen** = Anzahl eindeutiger Bestellungs-Events - Anzahl eindeutiger Stornierungen
- **Gesamterstattungswert** = Summe des Gesamtwerts erstatteter Bestellungen 

Diese berechneten Nutzerfelder sind auch im Tab **Transaktionen** der Nutzerprofile enthalten.

![Der Tab „Transaktionen" mit berechneten Nutzerfeldern.]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:70%;"}

## Häufig gestellte Fragen

### Wo kann ich Kaufdaten auf Produktebene einsehen?

Der Tab **Transaktionen** des Nutzerprofils zeigt übergeordnete berechnete Felder (wie Gesamtumsatz und Gesamtanzahl der Bestellungen). Um Produktdetails für eine bestimmte Nutzer:in anzuzeigen, verwenden Sie den [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/), um E-Commerce-Event-Daten abzufragen, oder exportieren Sie Event-Daten über [Currents]({{site.baseurl}}/user_guide/data/braze_currents/).

Im Gegensatz zu herkömmlichen Kauf-Events speichern empfohlene E-Commerce-Events Produktdetails als verschachtelte Event-Eigenschaften innerhalb des `products`-Arrays. Diese Eigenschaften sind im Messaging über Liquid und in der Segmentierung über [Segmenterweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) verfügbar.

### Wie kann ich Nutzer:innen nach einem bestimmten Produkt segmentieren?

Der Segmentierer ermöglicht es Ihnen, nach der Häufigkeit zu filtern, mit der eine Nutzer:in ein E-Commerce-Event durchgeführt hat. Um nach bestimmten Produkteigenschaften (wie `product_id` oder `product_name`) zu filtern, verwenden Sie [Segmenterweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), die die Filterung nach verschachtelten Event-Eigenschaften unterstützen. So können Sie beispielsweise alle Nutzer:innen finden, die in den letzten 90 Tagen das Produkt „SKU-123" gekauft haben.

### Was ist der Unterschied zwischen herkömmlichen Kauf-Events und empfohlenen E-Commerce-Events?

Herkömmliche Kauf-Events verwenden das Braze-[Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/) und erfassen einzelne Produktkäufe mit einer `product_id` und einem `price`. Empfohlene E-Commerce-Events (wie `ecommerce.order_placed`) verwenden angepasste Event-Eigenschaften und erfassen den gesamten Bestellkontext – einschließlich mehrerer Produkte, Rabatte und Metadaten – in einem einzigen Event.

Mit der Einführung der empfohlenen E-Commerce-Events wird Braze das herkömmliche Kauf-Event in Zukunft auslaufen lassen. Wenn Sie derzeit Kauf-Events nutzen, werden Sie vorab darüber informiert. In der Zwischenzeit können Sie Kauf-Events bis zum offiziellen Auslaufdatum weiterhin verwenden. Weitere Informationen finden Sie in der [Übersicht der empfohlenen Events]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/).

### Kann ich angepasste Eigenschaften zu empfohlenen E-Commerce-Events hinzufügen?

Empfohlene E-Commerce-Events verfügen über ein definiertes Schema mit erforderlichen und optionalen Feldern. Sie können für jedes Event zusätzliche angepasste Daten im `metadata`-Objekt hinzufügen. Angepasste Tags auf Bestellebene oder proprietäre Felder (wie Kaufkanal oder Shop-Informationen) werden jedoch nicht als Eigenschaften der obersten Ebene unterstützt. Wenn Sie diese Felder für die Segmentierung benötigen, senden Sie sie weiterhin als separate angepasste Events zusammen mit Ihren E-Commerce-Events.

### Muss ich `external_id` beim Senden von E-Commerce-Events angeben?

Das hängt davon ab, wie Sie die Events senden:

- **Über das SDK**: Nein. Bei der Verwendung eines Braze SDK werden Events automatisch mit dem aktuellen Nutzerkontext des SDK (anonym oder identifiziert) verknüpft. Sie müssen bei jedem Event-Aufruf keinen Nutzerbezeichner übergeben; stattdessen können Sie die Nutzer:in für diesen Kontext mit Methoden wie `changeUser` identifizieren.
- **Über die REST API** (`/users/track`): Ja. Jede API-Anfrage muss einen Nutzerbezeichner enthalten, wie z. B. `external_id`, `braze_id`, `user_alias`, `email` oder `phone`, da die API keinen Kontext für die „aktuelle Nutzer:in" hat.

### Warum werden verschachtelte Produkteigenschaften nicht im Dropdown-Menü der KI-Empfehlungen-Einrichtung angezeigt?

Bei der Konfiguration von [KI-Artikelempfehlungen]({{site.baseurl}}/user_guide/brazeai/recommendations/) werden im Dropdown-Menü **Eigenschaftsname** nur Event-Eigenschaften der obersten Ebene aufgeführt (wie `order_id`, `total_value` und `currency`). Verschachtelte Eigenschaften innerhalb des `products`-Arrays (z. B. `products.product_id` oder `products.variant_id`) werden möglicherweise nicht in dieser Liste angezeigt, können jedoch manuell mithilfe der Punktnotation in das Feld eingegeben werden. Für die meisten E-Commerce-Implementierungen empfiehlt Braze, `products.product_id` als Artikelbezeichner zu verwenden und diesen mit einem [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs/) zu verknüpfen, dessen Artikel-IDs mit Ihren `product_id`- oder `variant_id`-Werten übereinstimmen.

### Warum werden einige meiner E-Commerce-Events nicht in Braze angezeigt?

Wenn Events nicht in Nutzerprofilen oder Protokollen angezeigt werden, überprüfen Sie Folgendes:

- **Zeitpunkt der SDK-Datenübertragung**: Das Braze SDK speichert Daten lokal im Cache und lädt sie regelmäßig hoch (in der Regel innerhalb von 10–60 Sekunden). Rufen Sie `requestImmediateDataFlush()` nach `logCustomEvent()` auf, um einen sofortigen Upload zu erzwingen.
- **Erforderliche Eigenschaften**: E-Commerce-Events haben erforderliche Eigenschaften. Wenn eine erforderliche Eigenschaft fehlt oder einen ungültigen Datentyp aufweist, kann das Event abgelehnt werden. Überprüfen Sie, ob Ihre Event-Payload dem [erforderlichen Schema](#types-of-ecommerce-recommended-events) entspricht.
- **Genauigkeit der Event-Namen**: E-Commerce-Event-Namen unterscheiden zwischen Groß- und Kleinschreibung und müssen exakt übereinstimmen (z. B. `ecommerce.checkout_started`, nicht `ecommerce.checkoutStarted`).