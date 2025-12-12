---
nav_title: "Trigger-Eigenschaften Objekt"
article_title: API Triggereigenschaften Objekt
page_order: 11
page_type: reference
description: "Dieser referenzierte Artikel erklärt die verschiedenen Komponenten des Objekts Eigenschaften des Triggers."
tool: Campaigns

---

# Objekt triggernde Eigenschaften

> Wenn Sie einen der Endpunkte für den Versand einer Kampagne mit API-getriggerter Zustellung verwenden, können Sie eine Abbildung der Schlüssel und Werte bereitstellen, um Ihre Nachricht anzupassen.

Wenn Sie eine API-Anfrage stellen, die ein Objekt in `trigger_properties` enthält, können die Werte in diesem Objekt dann in Ihrer Template für Nachrichten unter dem `api_trigger_properties` Namensraum referenziert werden. Eine Anfrage mit folgendem Inhalt könnte zum Beispiel das Wort `"shoes"` zu einer Nachricht hinzufügen, indem Sie {% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %} hinzufügen. 

Beachten Sie, dass Eigenschaften von Triggern zwar als Template in Nachrichten eingefügt werden können, aber standardmäßig nicht automatisch im Nutzerprofil gespeichert werden.

{% alert note %}
Das Objekt `trigger_properties` und die Syntax {% raw %}`api_trigger_properties.${product_name}`{% endraw %} werden nur in Kampagnen unterstützt. Um Nachrichten mit Schlüsseln und Werten aus einer API-Trigger-Anfrage für Canvas anzupassen, verwenden Sie das [Objekt Canvas-Eingangseigenschaften]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). Das Objekt `trigger_properties` hat eine maximale Größe von 50 KB.
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


