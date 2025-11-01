---
nav_title: "Kauf-Objekt"
article_title: API Kauf-Objekt
page_order: 8
page_type: reference
description: "In diesem referenzierten Artikel werden die verschiedenen Komponenten eines Kauf-Objekts erläutert, wie Sie es richtig verwenden und welche Beispiele Sie verwenden können."

---

# Kauf-Objekt

> In diesem Artikel werden die verschiedenen Komponenten eines Kauf-Objekts, die richtige Verwendung, bewährte Verfahren und Beispiele erläutert.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

## Was ist ein Kauf-Objekt?

Ein Kauf-Objekt ist ein Objekt, das über die API übergeben wird, wenn ein Kauf getätigt wurde. Jedes Kauf-Objekt befindet sich in einem Kauf-Array, wobei jedes Objekt einen einzelnen Kauf durch einen bestimmten Nutzer:in zu einem bestimmten Zeitpunkt darstellt. Das Kauf-Objekt hat viele verschiedene Felder, die es dem Backend von Braze erlauben, diese Informationen zu speichern und für die Anpassung, Datenerfassung und Personalisierung zu verwenden.

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
- [Bezeichner der App]({{site.baseurl}}/api/identifier_types/)
- [ISO 4217 Währungscode Wiki](http://en.wikipedia.org/wiki/ISO_4217)
- [ISO 8601 Zeitcode Wiki](https://en.wikipedia.org/wiki/ISO_8601)

## ID des Produkts kaufen

Innerhalb des Kauf-Objekts ist `product_id` ein Bezeichner für den Kauf (z.B. `Product Name` oder `Product Category`):

- Braze erlaubt es Ihnen, bis zu 5.000 `product_id`s im Dashboard zu speichern.
- Die `product_id` kann bis zu 255 Zeichen lang sein.

### Konventionen zur Namensgebung

Bei Braze bieten wir einige allgemeine Namenskonventionen für das Kauf-Objekt `product_id` an. Bei der Auswahl von `product_id` schlägt Braze vor, einfache Namen wie den Produktnamen oder die Produktkategorie (anstelle von SKUs) zu verwenden, mit der Absicht, alle protokollierten Artikel nach diesem `product_id` zu gruppieren.

So lassen sich Produkte für die Segmentierung und das Triggern leicht identifizieren.

### Käufe auf der Ebene der Bestellung protokollieren

Wenn Sie Einkäufe auf Auftragsebene statt auf Produktebene protokollieren möchten, können Sie den Auftragsnamen oder die Auftragskategorie als `product_id` verwenden (z. B. `Online Order` oder `Completed Order`).

Zum Beispiel, um Einkäufe auf der Ebene der Bestellung im Internet SDK zu protokollieren:

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

## Kauf-Details-Objekt

Angepasste Events und Käufe können Event-Eigenschaften haben. Die "Eigenschaften"-Werte sollten ein Objekt sein, bei dem die Schlüssel die Eigenschaftsnamen und die Werte die Eigenschaftswerte sind. Eigenschaftsnamen müssen nicht-leere Strings mit maximal 255 Zeichen sein, ohne führende Dollarzeichen. 

Bei den Eigenschaften kann es sich um jeden der folgenden Datentypen handeln:

| Datentyp | Beschreibung |
| --- | --- |
| Zahlen | Entweder als [Ganzzahlen](https://en.wikipedia.org/wiki/Integer) oder [Gleitkommazahlen](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Boolesche Werte |  |
| Datumsangaben | Formatiert als Strings im [ISO-8601-](https://en.wikipedia.org/wiki/ISO_8601) oder `yyyy-MM-dd'T'HH:mm:ss:SSSZ` -Format. Innerhalb von Arrays nicht unterstützt. |
| Strings | 255 Zeichen oder weniger. |
| Arrays | Arrays können keine Datumsangaben enthalten. |
| Objekte | Die Objekte werden als Strings eingelesen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Objekte mit Event-Eigenschaften, die Array- oder Objektwerte enthalten, können eine Nutzlast für Event-Eigenschaften von bis zu 50 KB haben.

### Eigenschaften des Kaufs

[Kauf-Details]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties) können zum Triggern von Nachrichten und zur Personalisierung mit Liquid verwendet werden. Außerdem ist eine Segmentierung auf der Grundlage dieser Eigenschaften zulässig.

#### Konventionen zur Namensgebung

Bitte beachten Sie, dass dieses Feature **pro Produkt** und nicht pro Kauf aktiviert wird. Wenn Sie z.B. ein großes Volumen an unterschiedlichen Produkten haben, die aber alle die gleichen Eigenschaften haben, ist eine Segmentierung vielleicht eher unnötig.

In dieser Instanz empfehlen wir die Verwendung von Produktnamen auf "Gruppenebene" anstelle von etwas Granularem bei der Festlegung von Datenstrukturen. Zum Beispiel sollte ein Unternehmen, das Fahrkarten für Züge anbietet, Produkte für "Einzelfahrt", "Hin- und Rückfahrt", "Multi-City" und nicht für bestimmte Transaktionen wie "Transaktion 123" oder "Transaktion 046" haben. Ein weiteres Beispiel: Für das Kauf-Event "Essen" sollten Sie die Eigenschaften "Kuchen" und "Sandwich" festlegen.

{% alert important %}
Beachten Sie, dass Produkte über die Braze REST API hinzugefügt werden können. Wenn Sie beispielsweise einen Anruf an den Endpunkt `/users/track` senden und eine neue Kauf-ID angeben, wird im Abschnitt **Dateneinstellungen** > **Produkte** des Dashboards automatisch ein Produkt erstellt.
{% endalert %}

### Beispiel Kauf-Objekt

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

### Kauf-Objekte, Event-Objekte und Webhooks

Anhand des angegebenen Beispiels können wir sehen, dass jemand einen Rucksack mit den Eigenschaften Farbe, Monogramm, Kassendauer, Größe und Marke gekauft hat. Wir können dann Segmente mit diesen Eigenschaften erstellen, indem wir [Kauf-Event-Eigenschaften]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties) verwenden oder angepasste Nachrichten über einen Kanal mit Liquid senden. Zum Beispiel: "Hallo **Ann F.**, vielen Dank für den Kauf dieses **roten, mittelgroßen Rucksacks** für ** 40,00 $**! Danke für Ihren Einkauf bei **Backpack Locker**!"

Wenn Sie Eigenschaften zur Segmentierung speichern, speichern und tracken möchten, müssen Sie diese als angepasste Attribute einrichten. Dies kann mit Hilfe von [Segment-Erweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) geschehen, die es Ihnen ermöglichen, Targeting auf der Grundlage von angepassten Events oder Kauf-Events durchzuführen, die für die Lifetime des jeweiligen Benutzerprofils gespeichert wurden.


