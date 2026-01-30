---
nav_title: Einkäufe protokollieren
article_title: Käufe protokollieren für Windows Universal
platform: Windows Universal
page_order: 4
description: "Dieser referenzierte Artikel beschreibt, wie Sie Einkäufe auf der Windows Universal Plattform protokollieren können."
hidden: true
---
 
# Einkäufe protokollieren
{% multi_lang_include archive/windows_deprecation.md %}

Erfassen Sie In-App-Käufe, damit Sie Ihre Einnahmen im Laufe der Zeit und über verschiedene Einnahmequellen hinweg verfolgen und Ihre Nutzer nach ihrem Lifetime-Value segmentieren können.

Braze unterstützt Einkäufe in mehreren Währungen. Einkäufe, die Sie in einer anderen Währung als dem USD melden, werden im Dashboard in USD auf der Grundlage des Wechselkurses an dem Tag, an dem sie gemeldet wurden, angezeigt.

Lesen Sie vor der Implementierung unbedingt die Beispiele für die Segmentierungsoptionen, die angepasste Events, angepasste Attribute und Kauf-Events bieten, in unserem Artikel über [bewährte Verfahren]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection). Wir empfehlen Ihnen auch, sich mit unseren [Namenskonventionen für Events]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/) vertraut zu machen.

Um diese Funktion zu nutzen, fügen Sie diesen Methodenaufruf nach einem erfolgreichen Kauf in Ihrer App hinzu:

Käufe werden mit Hilfe der Eigenschaft `EventLogger` protokolliert, die in IAppboy enthalten ist. Um einen Verweis auf `EventLogger` zu erhalten, rufen Sie `Appboy.SharedInstance.EventLogger` auf.

```csharp
bool LogPurchase(string productId, string currencyCode, decimal price)
```

## Käufe auf der Ebene der Bestellung protokollieren
Wenn Sie Einkäufe auf der Bestellebene statt auf der Produktebene protokollieren möchten, können Sie den Bestellnamen oder die Bestellkategorie als `product_id` verwenden. Weitere Informationen finden Sie in unserer [Spezifikation für Kaufobjekte]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

## REST API

Sie können auch unsere REST API verwenden, um Einkäufe zu erfassen. Einzelheiten finden Sie in der [API-Dokumentation für Benutzer]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

