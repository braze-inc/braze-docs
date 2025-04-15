---
nav_title: "Objekt kaufen"
article_title: API Kaufobjekt
page_order: 8
page_type: reference
description: "Dieser Referenzartikel erklärt die verschiedenen Komponenten eines Kaufobjekts, die korrekte Verwendung und Beispiele, auf die Sie zurückgreifen können."

---

# Objekt kaufen

> Dieser Artikel erklärt die verschiedenen Komponenten eines Kaufobjekts, die korrekte Verwendung, bewährte Verfahren und Beispiele, auf die Sie zurückgreifen können.

## Was ist ein Kaufobjekt?

Ein Kaufobjekt ist ein Objekt, das über die API übergeben wird, wenn ein Kauf getätigt wurde. Jedes Kaufobjekt befindet sich in einem Kauf-Array, wobei jedes Objekt einen einzelnen Kauf durch einen bestimmten Benutzer zu einem bestimmten Zeitpunkt darstellt. Das Kaufobjekt hat viele verschiedene Felder, die es dem Backend von Braze ermöglichen, diese Informationen zu speichern und für die Anpassung, Datenerfassung und Personalisierung zu verwenden.

### Objektkörper

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required.
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  // See the following product_id naming conventions for clarification.
  "product_id" : (required, string) identifier for the purchase, for example, Product Name or Product Category,
  "currency" : (required, string) ISO 4217 Alphabetic Currency Code,
  //Revenue from a purchase object is calculated as the product of quantity and price.
  "price" : (required, float) value in the base currency unit (for example, Dollars for USD, Yen for JPY),
  "quantity" : (optional, integer) the quantity purchased (defaults to 1, must be <= 100 -- currently, Braze treats a quantity _X_ as _X_ separate purchases with quantity 1),
  "time" : (required, datetime as string in ISO 8601) Time of purchase,
  // See the following purchase object explanation for clarification.
  "properties" : (optional, Properties Object) properties of the event,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
}
```

- [Externe Benutzer-ID]({{site.baseurl}}/api/basics/#user-ids)
- [App Kennung]({{site.baseurl}}/api/identifier_types/)
- [ISO 4217 Währungscode Wiki][20]
- [ISO 8601 Zeitcode Wiki][22]

## Kaufen product_id

Innerhalb des Kaufobjekts ist `product_id` ein Identifikator für den Kauf (z.B. `Product Name` oder `Product Category`):

- Mit Braze können Sie bis zu 5.000 `product_id`auf dem Dashboard speichern.
- Die `product_id` kann bis zu 255 Zeichen lang sein.

### Namenskonventionen für Produkt-IDs

Bei Braze bieten wir einige allgemeine Namenskonventionen für das Kaufobjekt `product_id` an. Bei der Auswahl von `product_id` schlägt Braze vor, einfache Namen wie den Produktnamen oder die Produktkategorie (anstelle von SKUs) zu verwenden, mit der Absicht, alle protokollierten Artikel nach diesem `product_id` zu gruppieren.

Auf diese Weise lassen sich Produkte für die Segmentierung und Auslösung leicht identifizieren.

### Käufe auf der Ebene der Bestellung protokollieren

Wenn Sie Einkäufe auf der Bestellebene statt auf der Produktebene protokollieren möchten, können Sie den Bestellnamen oder die Bestellkategorie als `product_id` verwenden (z.B. `Online Order` oder `Completed Order`).

Zum Beispiel, um Einkäufe auf der Ebene der Bestellung im Web SDK zu protokollieren:

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99, },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99, }
        ]
      }
    }
  ]
}
```

## Objekt Eigenschaften kaufen

Benutzerdefinierte Ereignisse und Käufe können Ereigniseigenschaften haben. Die "Eigenschaften"-Werte sollten ein Objekt sein, bei dem die Schlüssel die Eigenschaftsnamen und die Werte die Eigenschaftswerte sind. Eigenschaftsnamen müssen nicht leere Zeichenketten sein, die maximal 255 Zeichen lang sind und keine Dollarzeichen enthalten. 

Eigenschaftswerte können alle der folgenden Datentypen sein:

| Daten Typ | Beschreibung |
| --- | --- |
| Zahlen | Entweder als [Ganzzahl](https://en.wikipedia.org/wiki/Integer) oder als [Fließkommazahl](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Boolesche Wörter |  |
| Datumsangaben | Formatiert als Zeichenketten im [ISO-8601-](https://en.wikipedia.org/wiki/ISO_8601) oder `yyyy-MM-dd'T'HH:mm:ss:SSSZ` -Format. Innerhalb von Arrays nicht unterstützt. |
| Streicher | 255 Zeichen oder weniger. |
| Arrays | Arrays können keine Datumsangaben enthalten. |
| Objekte | Objekte werden als Strings eingelesen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Objekte mit Ereigniseigenschaften, die Array- oder Objektwerte enthalten, können eine Nutzlast für Ereigniseigenschaften von bis zu 50 KB haben.

### Immobilien kaufen

[Kaufeigenschaften]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties) können zum Auslösen von Nachrichten und für die Personalisierung mit Liquid verwendet werden und ermöglichen Ihnen auch die Segmentierung auf der Grundlage dieser Eigenschaften.

### Namenskonventionen für den Kauf von Immobilien

Bitte beachten Sie, dass diese Funktion **pro Produkt** und nicht pro Kauf aktiviert ist. Wenn ein Kunde zum Beispiel eine große Anzahl unterschiedlicher Produkte hat, die aber alle die gleichen Eigenschaften haben, wird die Segmentierung ziemlich sinnlos.

In diesem Fall empfehlen wir daher, bei der Festlegung der Datenstrukturen Produktnamen auf "Gruppenebene" zu verwenden, anstatt etwas Granulares. Ein Zugfahrkartenunternehmen sollte beispielsweise Produkte für "Einzelfahrt", "Hin- und Rückfahrt", "Multicity" und nicht für bestimmte Transaktionen wie "Transaktion 123" oder "Transaktion 046" haben. Bei dem Kaufereignis "Essen" wären zum Beispiel die Eigenschaften "Kuchen" und "Sandwich" am besten geeignet.

### Beispiel Kaufobjekt
```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "backpack",
      "currency" : "USD",
      "price" : 40.00,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "color" : "red",
        "monogram" : "ABC",
        "checkout_duration" : 180,
        "size" : "Large",
        "brand" : "Backpack Locker"
      }
    },
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pencil",
      "currency" : "USD",
      "price" : 2.00,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "number" : 2,
        "sharpened" : true
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pen",
      "currency" : "USD",
      "price" : 2.50,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "color" : "blue",
      }
    }
  ]
}
```

## Kaufobjekte, Ereignisobjekte und Webhooks

Anhand des angegebenen Beispiels können wir sehen, dass jemand einen Rucksack mit den Eigenschaften Farbe, Monogramm, Kassendauer, Größe und Marke gekauft hat. Mit diesen Eigenschaften können wir dann Segmente erstellen, indem wir [Eigenschaften von Kaufereignissen][2] verwenden oder mit Liquid benutzerdefinierte Nachrichten über einen Kanal senden. Zum Beispiel: "Hallo **Ann F.**, vielen Dank für den Kauf dieses **roten, mittelgroßen Rucksacks** für ** 40,00 $**! Danke für Ihren Einkauf bei **Backpack Locker**!"

Wenn Sie Eigenschaften für die Segmentierung speichern, aufbewahren und verfolgen möchten, müssen Sie sie als benutzerdefinierte Attribute einrichten. Dazu können Sie [Segmenterweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) verwenden, die es Ihnen ermöglichen, Benutzer auf der Grundlage von benutzerdefinierten Ereignissen oder Kaufverhalten anzusprechen, die für die gesamte Lebensdauer des Benutzerprofils gespeichert werden.

[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties
[20]: http://en.wikipedia.org/wiki/ISO_4217 "ISO 4217 Währungscode"
[21]: {{site.baseurl}}/api/api_key/#the-app-identifier-api-key
[22]: https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 Zeitcode"
[23]: {{site.baseurl}}/api/basics/#external-user-id-explanation
