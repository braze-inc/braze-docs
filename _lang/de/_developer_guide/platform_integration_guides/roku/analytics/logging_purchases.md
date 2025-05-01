---
nav_title: Käufe protokollieren
article_title: Käufe für Roku protokollieren
platform: Roku
page_order: 3
page_type: reference
description: "Auf dieser Seite werden Methoden zur Protokollierung von Kauf-Events für Roku über das Braze SDK beschrieben."

---
 
# Einkäufe protokollieren

> Erfassen Sie In-App-Käufe, um Ihren Umsatz im Zeitverlauf und über verschiedene Umsatzquellen hinweg zu verfolgen und Ihre Nutzer nach ihrem Lifetime-Value zu segmentieren.

Braze unterstützt Einkäufe in mehreren Währungen. Einkäufe, die Sie in einer anderen Währung als dem USD melden, werden im Dashboard in USD auf der Grundlage des Wechselkurses an dem Tag, an dem sie gemeldet wurden, angezeigt.

Lesen Sie vor der Implementierung unbedingt die Beispiele für die Segmentierungsoptionen, die sich durch benutzerdefinierte Ereignisse, benutzerdefinierte Attribute und Kaufereignisse ergeben, in unserem Artikel [Best Practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection). Wir empfehlen Ihnen auch, sich mit unseren [Namenskonventionen für Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/) vertraut zu machen.

## Tracken von Käufen und Umsätzen

Um dieses Feature zu nutzen, fügen Sie diesen Methodenaufruf nach einem erfolgreichen Kauf in Ihrer App hinzu:

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity)
```

### Hinzufügen von Eigenschaften

Sie können Metadaten über Käufe hinzufügen, indem Sie ein Eigenschaften-Wörterbuch mit Ihren Kaufinformationen übergeben.

Eigenschaften werden als Schlüssel-Werte-Paare definiert.  Die Schlüssel sind Objekte des Typs `String` und die Werte können ein `String` oder `Integer` sein.

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity, {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```

### Käufe auf Bestellebene protokollieren
Wenn Sie Einkäufe auf der Bestellebene statt auf der Produktebene protokollieren möchten, können Sie den Bestellnamen oder die Bestellkategorie als `product_id` verwenden. Weitere Informationen finden Sie in unserer [Spezifikation für Kaufobjekte]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

### REST API

Sie können auch unsere REST API verwenden, um Einkäufe zu erfassen. Einzelheiten finden Sie in der [API-Dokumentation für Benutzer]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

