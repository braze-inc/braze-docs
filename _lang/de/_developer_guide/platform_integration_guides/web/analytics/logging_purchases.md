---
nav_title: Käufe protokollieren
article_title: Einkäufe für das Internet protokollieren
platform: Web
page_order: 4
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie Einkäufe protokollieren und Eigenschaften zu diesen Käufen für Web hinzufügen."

---
 
# Einkäufe protokollieren

> Erfassen Sie In-App-Käufe, damit Sie Ihre Einnahmen im Laufe der Zeit und über verschiedene Einnahmequellen hinweg verfolgen und Ihre Nutzer nach ihrem Lifetime-Value segmentieren können. 

Braze unterstützt Einkäufe in mehreren Währungen. Einkäufe, die Sie in einer anderen Währung als dem USD melden, werden im Dashboard in USD auf der Grundlage des Wechselkurses an dem Tag, an dem sie gemeldet wurden, angezeigt.

Sehen Sie sich vor der Implementierung unbedingt in unseren [Best Practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection) die Beispiele für die Segmentierungsoptionen von angepassten Events, angepassten Attributen und Kauf-Events an.

Um dieses Feature zu nutzen, fügen Sie den [`logPurchase()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) Aufruf nach einem erfolgreichen Kauf in Ihrer App ein. Beachten Sie, dass die `quantity` kleiner oder gleich 100 sein muss.

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

## Hinzufügen von Eigenschaften

Sie können [Metadaten](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) über Käufe hinzufügen, indem Sie entweder ein [Event-Eigenschaften-Array]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects) oder ein Objekt mit Schlüssel-Wert-Paaren mit Ihren Kaufinformationen übergeben. 

#### Objekt Formatierung

Schlüssel sind `string`-Objekte und die Werte können `string`-, `numeric`-, `boolean`\- oder `Date`-Objekte sein.

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

#### Käufe auf der Ebene der Bestellung protokollieren
Wenn Sie Einkäufe auf der Bestellebene statt auf der Produktebene protokollieren möchten, können Sie den Bestellnamen oder die Bestellkategorie als `product_id` verwenden. Weitere Informationen finden Sie in unserer [Spezifikation für Kaufobjekte]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

## REST API

Sie können auch unsere REST API verwenden, um Einkäufe zu erfassen. Einzelheiten finden Sie in der [API-Dokumentation für Benutzer]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

