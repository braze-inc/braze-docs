---
nav_title: Käufe protokollieren
article_title: Käufe protokollieren für iOS
platform: Swift
page_order: 4
description: "Dieser Referenzartikel beschreibt, wie Sie In-App-Käufe und Umsätze tracken und Kauf-Eigenschaften für das Swift SDK zuweisen können."

---

# Einkäufe protokollieren

Erfassen Sie In-App-Käufe, um Ihre Umsätze im Zeitverlauf über verschiedene Umsatzquellen hinweg zu tracken und Ihre Nutzer nach ihrem Lifetime-Value zu segmentieren.

Braze unterstützt Einkäufe in mehreren Währungen. Einkäufe, die Sie in einer anderen Währung als dem USD melden, werden im Dashboard in USD auf der Grundlage des Wechselkurses an dem Tag, an dem sie gemeldet wurden, angezeigt.

Lesen Sie vor der Implementierung unbedingt die Beispiele für die Segmentierungsoptionen, die benutzerdefinierte Ereignisse, benutzerdefinierte Attribute und Kaufereignisse bieten, in unseren [Best Practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection) sowie unsere Hinweise zu den [Namenskonventionen für Ereignisse]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Verfolgung von Käufen und Einnahmen

Um diese Funktion zu nutzen, fügen Sie diesen Methodenaufruf nach einem erfolgreichen Kauf in Ihrer App hinzu:

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze logPurchase:"product_id"
                      currency:@"USD"
                         price:price];
```

{% endtab %}
{% endtabs %}

- Folgende Währungssymbole werden unterstützt: USD, CAD, EUR, GBP, JPY, AUD, CHF, NOK, MXN, NZD, CNY, RUB, TRY, INR, IDR, ILS, SAR, ZAR, AED, SEK, HKD, SPD, DKK, und mehr.
  - Jedes andere angegebene Währungssymbol führt zu einer protokollierten Warnung und zu keiner weiteren Aktion durch das SDK.
- Die Produkt-ID darf maximal 255 Zeichen lang sein.
- Beachten Sie, dass der Kauf nicht in Braze protokolliert wird, wenn die Produktkennung leer ist.

### Hinzufügen von Eigenschaften {#properties-purchases}
Sie können Metadaten über Käufe hinzufügen, indem Sie ein Wörterbuch mit den Werten `Int`, `Double`, `String`, `Bool` oder `Date` übergeben.

Weitere Einzelheiten finden Sie in der [iOS-Klassendokumentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/logpurchase(productid:currency:price:quantity:properties:fileid:line:) "Logpurchase-Dokumentation").

### Menge hinzufügen
Sie können eine Menge zu Ihren Einkäufen hinzufügen, wenn Kunden denselben Einkauf mehrmals in einer einzigen Kasse tätigen. Sie können dies erreichen, indem Sie `Int` für die Menge eingeben.

* Die eingegebene Menge muss im Bereich von [0, 100] liegen, damit das SDK einen Kauf protokollieren kann.
* Methoden ohne Mengeneingabe haben standardmäßig den Mengenwert 1.

Weitere Einzelheiten finden Sie in der [iOS-Klassendokumentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/logpurchase(productid:currency:price:quantity:properties:fileid:line:) "Logpurchase-Dokumentation").

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.logPurchase(productId: "product_id", currency: "USD", price: price, quantity: quantity, properties: ["key1":"value1"])
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze logPurchase:productId
                      currency:@"USD"
                         price:price
                      quantity:quantity
                    properties:@{@"checkout_id" : self.checkoutId}];
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Wenn Sie einen Wert von 10 USD und eine Menge von 3 eingeben, wird dies im Profil des Benutzers als drei Käufe von 10 Dollar für insgesamt 30 Dollar protokolliert.
{% endalert %}

### Käufe auf der Ebene der Bestellung protokollieren
Wenn Sie Einkäufe auf der Bestellebene statt auf der Produktebene protokollieren möchten, können Sie den Bestellnamen oder die Bestellkategorie als `product_id` verwenden. Weitere Informationen finden Sie in unserer [Spezifikation für Kaufobjekte]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

### Reservierte Tasten

Die folgenden Schlüssel sind reserviert und können nicht als Kaufeigenschaften verwendet werden:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

### REST API

Sie können auch unsere REST API verwenden, um Einkäufe zu erfassen. Einzelheiten finden Sie in der [Benutzer-API-Dokumentation]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

