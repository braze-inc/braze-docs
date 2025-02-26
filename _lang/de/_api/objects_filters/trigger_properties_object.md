---
nav_title: "Trigger-Eigenschaften Objekt"
article_title: API Trigger-Eigenschaften Objekt
page_order: 11
page_type: reference
description: "Dieser Referenzartikel erläutert die verschiedenen Komponenten des Objekts Triggereigenschaften."
tool: Campaigns

---

# Trigger-Eigenschaften Objekt

> Wenn Sie einen der Endpunkte für den Versand einer Kampagne mit API-gesteuerter Zustellung verwenden, können Sie eine Zuordnung von Schlüsseln und Werten angeben, um Ihre Nachricht anzupassen.

Wenn Sie eine API-Anfrage stellen, die ein Objekt in `trigger_properties` enthält, können die Werte in diesem Objekt dann in Ihrer Nachrichtenvorlage unter dem Namensraum `api_trigger_properties` referenziert werden. Zum Beispiel könnte eine Anfrage mit folgendem Inhalt das Wort `"shoes"` zu einer Nachricht hinzufügen, indem Sie {% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %} hinzufügen.

{% alert note %}
Das Objekt `trigger_properties` und die Syntax {% raw %}`api_trigger_properties.${product_name}`{% endraw %} werden nur in Kampagnen unterstützt. Um Nachrichten mit Schlüsseln und Werten aus einer API-Trigger-Anfrage für Canvas anzupassen, verwenden Sie das [Objekt Canvas entry properties]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). Das Objekt `trigger_properties` hat eine maximale Größe von 50 KB.
{% endalert %}

## Objektkörper

```json
{
  "trigger_properties" : {
    "product_name" : "shoes",
    "product_price" : 79.99,
    "details" : {
      "color" : "red",
      "size" : {
        "numerical" : 10,
        "country" : "US"
      }
    },
    "related_skus": ["123", "456", "789"]
  }
}
```


