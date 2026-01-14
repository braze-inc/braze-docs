---
nav_title: Persistente Eigenschaften des Entrys
article_title: Persistente Entry-Eigenschaften
alias: "/persistent_entry/"
page_type: reference
description: "In diesem Referenzartikel wird beschrieben, wie Sie die Eigenschaften von persistenten Einträgen in Ihrem Canvas verwenden können, um mehr kuratierte Nachrichten zu versenden und eine hochgradig verfeinerte Endbenutzererfahrung zu schaffen."
tool: Canvas
page_order: 5
---

# Persistente Eigenschaften des Entrys

> Wenn ein Canvas durch ein benutzerdefiniertes Ereignis, einen Kauf oder einen API-Aufruf ausgelöst wird, können Sie Metadaten aus dem API-Aufruf, dem benutzerdefinierten Ereignis oder dem Kaufereignis zur Personalisierung in jedem Schritt Ihres Canvas-Workflows verwenden. Sie können diese Eigenschaften verwenden, um mehr kuratierte Nachrichten zu versenden.

{% alert important %}
Persistente Eingangs-Eigenschaften sind ein Artefakt des ursprünglichen Canvas-Editors, daher gibt es veraltete Referenzen auf Begriffe, die als historische Referenz verbleiben. Den aktuellen, aktualisierten Canvas-Editor finden Sie unter [Canvas-Eingangs-Eigenschaften und Event-Eigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties).
{% endalert %}

## Eingabeeigenschaften verwenden

Eingabeeigenschaften können in aktionsbasierten und API-gesteuerten Canvases verwendet werden. Diese Entry-Eigenschaften werden definiert, wenn ein Canvas durch ein angepasstes Event, einen Kauf oder einen API-Aufruf getriggert wird. Weitere Informationen finden Sie in den folgenden Artikeln:

- [Canvas Entry Eigenschaften Objekt]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)
- [Event-Eigenschaften Objekt]({{site.baseurl}}/api/objects_filters/event_object/)
- [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-product_id)

Eigenschaften, die von diesen Objekten übergeben werden, können mit dem Tag `canvas_entry_properties` Liquid-Tag referenziert werden. Eine Anfrage mit `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}` könnte zum Beispiel das Wort "Schuhe" zu einer Nachricht hinzufügen, indem Sie das Liquid {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %} hinzufügen.

Wenn ein Canvas eine Nachricht mit dem Tag `canvas_entry_properties` Liquid enthält, werden die mit diesen Eigenschaften verbundenen Werte für die Dauer der Reise eines Benutzers im Canvas gespeichert und gelöscht, wenn der Benutzer das Canvas verlässt. Beachten Sie, dass die Eigenschaften von Canvas-Entrys nur in Liquid referenziert werden können. Um nach den Eigenschaften innerhalb des Canvas zu filtern, verwenden Sie stattdessen die [Segmentierung von Event-Eigenschaften]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

{% alert note %}
Das Objekt Canvas Entry-Eigenschaften hat eine maximale Größe von 50 KB.
{% endalert %}

## Update von Canvas zur Verwendung von Entry-Eigenschaften

Wenn ein aktives Canvas, das zuvor keine Nachrichten enthielt, die `canvas_entry_properties` verwenden, so bearbeitet wird, dass es `canvas_entry_properties` enthält, ist der Wert, der dieser Eigenschaft entspricht, für Nutzer:innen, die das Canvas betreten haben, bevor `canvas_entry_properties` dem Canvas hinzugefügt wurde, nicht verfügbar. Die Werte werden nur für Nutzer:innen gespeichert, die den Canvas nach der Änderung betreten.

Wenn Sie beispielsweise am 3\. November eine Leinwand gestartet haben, die keine Eingabeeigenschaften verwendet, und dann am 11\. November eine neue Eigenschaft `product_name` zur Leinwand hinzugefügt haben, werden die Werte für `product_name` nur für Benutzer gespeichert, die die Leinwand ab dem 11\. November betreten.

Für den Fall, dass eine Eigenschaft eines Canvas-Entrys null oder leer ist, können Sie Nachrichten mithilfe von Konditionalen abbrechen. Der folgende Code Snippet ist ein Beispiel dafür, wie Sie Liquid verwenden können, um eine Nachricht abzubrechen.
{%raw%}
```
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}
```
{%endraw%}

Wenn Sie mehr über das Abbrechen von Nachrichten mit Liquid erfahren möchten, lesen Sie unsere [Dokumentation zu Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages).

## Globale Canvas-Entry-Eigenschaften

Mit `canvas_entry_properties` können Sie globale Eigenschaften festlegen, die für alle Nutzer:innen gelten, oder benutzerspezifische Eigenschaften, die nur für den angegebenen Nutzer gelten. Die benutzerspezifische Eigenschaft tritt an die Stelle der globalen Eigenschaft für diesen Benutzer.

### Beispiel Anfrage

```
url -X POST \
-H 'Content-Type:application/json' \
-d '{
      "api_key": "a valid rest api key",
      "canvas_id": "the ID of your Canvas",
         "canvas_entry_properties": {
            "food_allergies": "none"
          },
      "recipients": [
        {
          "external_user_id": Customer_123,
          "canvas_entry_properties": {
            "food_allergies": ["dairy", "soy"],
            "nutrition": {
              "calories_per_serving": 200,
              "serving_size_in_ounces": 4
            }
          }
        }
      ]
    }' \
```
 
In dieser Anfrage ist der globale Wert für "Lebensmittelallergien" "keine". Für Customer_123, lautet der Wert "Molkerei". Nachrichten in diesem Canvas, die das Liquid Snippet {%raw%}`{{canvas_entry_properties.${food_allergies}}}`{%endraw%} enthalten, erhalten ein Template mit "dairy" für Customer_123 und "none" für alle anderen. 

## Anwendungsfall

Wenn Sie ein Canvas haben, das ausgelöst wird, wenn ein Nutzer:in einen Artikel auf Ihrer E-Commerce-Website stöbert, ihn aber nicht in den Warenkorb legt, könnte der erste Schritt des Canvas eine Push-Benachrichtigung sein, in der er gefragt wird, ob er den Artikel kaufen möchte. Sie können den Namen des Produkts referenzieren, indem Sie {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}

![]({% image_buster /assets/img/persistent_entry_properties/PEP1.png %}){: style="border:0;margin-left:15px;"}

Im zweiten Schritt kann eine weitere Push-Benachrichtigung gesendet werden, die den Benutzer zur Kasse bittet, wenn er den Artikel in den Warenkorb gelegt, aber noch nicht gekauft hat. Sie können weiterhin die Eigenschaft des Entrys `product_name` referenzieren, indem Sie {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %} verwenden.

![]({% image_buster /assets/img/persistent_entry_properties/PEP12.png %}){: style="border:0;margin-left:15px;"}

