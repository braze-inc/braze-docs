---
nav_title: „Wieder verfügbar“-Benachrichtigungen
article_title: Einrichten von „Wieder verfügbar“-Benachrichtigungen
page_order: 2
description: "Lernen Sie, wie Sie mit Hilfe Ihres Katalogs und angepasster Events Benachrichtigungen einrichten, wenn ein Artikel wieder vorrätig ist. So können Sie Abonnent:in automatisch benachrichtigen lassen, wenn ein Artikel wieder vorrätig ist."
---

# „Wieder verfügbar“-Benachrichtigungen

> Lernen Sie, wie Sie mit Hilfe Ihres Katalogs und angepasster Events Benachrichtigungen einrichten, wenn ein Artikel wieder vorrätig ist. So können Sie Abonnent:in automatisch benachrichtigen lassen, wenn ein Artikel wieder vorrätig ist. Beachten Sie, dass dies nur für Nutzer:innen gilt, die sich bereits für Benachrichtigungen entschieden haben.

## Funktionsweise

Sie können ein angepasstes Event als Abo-Event einrichten, z.B. ein `product_clicked` Event. Dieses Event muss eine Eigenschaft der Artikel-ID enthalten (Katalogartikel-IDs). Wir schlagen vor, dass Sie einen Katalognamen angeben, aber das ist nicht erforderlich. Sie geben auch den Namen eines Feldes für die Bestandsmenge an, das ein Zahlendatentyp sein muss. 

Beachten Sie, dass der Bestand eines Katalogartikels auf Null stehen muss, damit ein Nutzer:in diesen Artikel erfolgreich abonnieren kann. Wenn ein Artikel eine Bestandsmenge von mehr als Null hat, sucht Braze alle Nutzer:innen, die diesen Artikel abonniert haben, und sendet ein angepasstes Event, das Sie zum Triggern einer Kampagne oder eines Canvas verwenden können.

Die Event-Eigenschaften werden zusammen mit Ihrem Nutzer:innen versendet, so dass Sie die Artikeldetails als Template in die Kampagne oder das Canvas einfügen können, die/das sendet.

## Einrichten von „Wieder verfügbar“-Benachrichtigungen

Führen Sie diese Schritte aus, um eine Benachrichtigung über einen nicht vorrätigen Katalog einzurichten.

1. Gehen Sie zu Ihrem Katalog und wählen Sie die Registerkarte **Einstellungen**.
2. Wählen Sie den Schalter **Wieder vorrätig** aus.
3. Wenn die globalen „Wieder verfügbar“-Einstellungen nicht konfiguriert wurden, werden Sie aufgefordert, die angepassten Events und Eigenschaften einzurichten, die zum Auslösen von „Wieder verfügbar“-Benachrichtigungen verwendet werden sollen:
    <br> ![Schublade für Katalogeinstellungen.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}
    - **Fallback-Katalog** Dies ist der Katalog, der für das „Wieder verfügbar“-Abo verwendet wird, wenn die Eigenschaft `catalog_name` für das angepasste Event nicht vorhanden ist.
    - **Angepasstes Event für Abonnements** ist das angepasste Event von Braze, mit dem ein Nutzer:in für „Wieder verfügbar“-Benachrichtigungen abonniert wird. Wenn dieses Event eintritt, erhält der oder die Nutzer:in, der oder die das Event ausgeführt hat, ein Abonnement.
    - **Angepasstes Event für die Abmeldung** ist das angepasste Event von Braze, mit dem ein Nutzer:in von den „Wieder verfügbar“-Benachrichtigungen abgemeldet wird. Dieses Ereignis ist optional. Führt der Nutzer:in dieses Ereignis nicht aus, wird er nach 90 Tagen abgemeldet oder wenn das Back-in-Stock-Ereignis triggert, je nachdem, was zuerst eintritt.
    - Die **Event-Eigenschaft für Artikel-ID** ist die Eigenschaft des oben genannten angepassten Events, das verwendet wird, um den Artikel für ein Abo oder eine Abmeldung zu bestimmen, wenn ein Artikel wieder auf Lager ist. Diese Eigenschaft des angepassten Events sollte eine Artikel ID (`id`) enthalten, die in einem Katalog vorhanden ist. Die ID des Artikels muss als String gesendet werden, damit sie mit dem im Zielkatalog gespeicherten Datentyp `id` übereinstimmt. Das angepasste Event sollte auch eine Eigenschaft `catalog_name` enthalten, um anzugeben, in welchem Katalog sich dieser Artikel befindet.
    
    - Ein Beispiel für ein benutzerdefiniertes Ereignis würde wie folgt aussehen
    ```json
    {
        "events": [
            {
                "external_id": "<external_id>",
                "name": "subscription",
                "time": "2024-04-15T19:22:28Z",
                "properties": {
                    "id": "shirt-xl",
                    "catalog_name": "on_sale_products",
                    "type": ["back_in_stock"]
                }
            }
        ]
    }
    ```
{% alert note %}
Back-in-Stock- und Price-Drop-Trigger verwenden dasselbe Ereignis, um den Nutzer:in für die Benachrichtigung zu abonnieren. Sie können also die Eigenschaft `type` verwenden, um sowohl Price-Drop- als auch Back-in-Stock-Benachrichtigungen im selben Ereignis einzustellen. Beachten Sie, dass die Eigenschaft `type` ein Array sein muss.
{% endalert %}

{: start="4"}
4\. Wählen Sie **Speichern** und fahren Sie mit der Seite **Einstellungen** des Katalogs fort.
5\. Legen Sie Ihre Benachrichtigungsregel fest. Es gibt zwei Optionen:
    - **Alle abonnierten Benutzer benachrichtigen** benachrichtigt alle Kunden, die warten, wenn der Artikel wieder auf Lager ist.
    - **Benachrichtigungslimits festlegen** benachrichtigt eine bestimmte Anzahl von Kunden pro von Ihnen konfiguriertem Benachrichtigungszeitraum. Braze benachrichtigt die angegebene Anzahl von Kunden schrittweise, bis es keine Kunden mehr zu benachrichtigen gibt oder der Artikel nicht mehr vorrätig ist. Ihre Benachrichtigungsrate darf 10.000 Nutzer:innen pro Minute nicht überschreiten.
6\. Legen Sie das **Feld Inventar im Katalog** fest. Dieses Katalogfeld wird verwendet, um festzustellen, ob der Artikel nicht mehr vorrätig ist. Das Feld muss vom Typ Zahl sein.
7\. Wählen Sie **Einstellungen speichern**.

![Katalogeinstellungen, in denen das Feature "Auf Lager" aktiviert ist. Die Benachrichtigungsregeln sehen vor, dass alle zehn Minuten tausend Nutzer:innen benachrichtigt werden.]({% image_buster /assets/img/back_in_stock_settings.png %})

{% alert important %}
Die Benachrichtigungsregeln in diesen Einstellungen ersetzen nicht die Canvas-Benachrichtigungseinstellungen, wie z.B. Stille Stunden.
{% endalert %}

## Back-in-Stock-Benachrichtigungen in einem Canvas verwenden

Nachdem Sie das „Wieder verfügbar“-Feature in einem Katalog eingerichtet haben, folgen Sie diesen Schritten zur Verwendung mit Canvas.

1. Richten Sie einen aktionsbasierten Canvas ein.
2. Wählen Sie **Zurück auf Lager** als Auslöser.
3. Wählen Sie den Namen des Katalogs mit den „Wieder verfügbar“-Benachrichtigungen aus.
4. Fahren Sie mit der [Einrichtung]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) Ihres Canvas fort, wie Sie es gewohnt sind.

Jetzt können Ihre Kunden benachrichtigt werden, wenn ein Artikel wieder auf Lager ist.

### Liquid verwenden

Um ein Template mit Details zu dem Artikel zu erstellen, der wieder verfügbar ist, können Sie den `canvas_entry_properties`-Liquid-Tag verwenden, um auf die `item_id` zuzugreifen. 

Die Verwendung von {%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%} gibt die ID des Artikels zurück, der wieder auf Lager ist. {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%} gibt den Bestandswert des Artikels vor der Aktualisierung zurück, und {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%} gibt den neuen Bestandswert nach der Aktualisierung zurück.

Verwenden Sie diesen Liquid-Tag {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}``{%endraw%} am Anfang Ihrer Nachricht und verwenden Sie dann {%raw%}``{{ items[0].<field_name> }}``{%endraw%}, um in der gesamten Nachricht auf Daten zu diesem Artikel zuzugreifen.

## Überlegungen

- Das Abonnement gilt nur für 90 Tage. Wenn der Artikel nicht innerhalb von 90 Tagen wieder auf Lager ist, wird der oder die Nutzer:in abgemeldet.
- Wenn Sie die Benachrichtigungsregel **Alle abonnierten Benutzer benachrichtigen** verwenden, benachrichtigt Braze 100.000 Benutzer innerhalb von 10 Minuten.
- Braze verarbeitet maximal 10 Artikelaktualisierungen innerhalb einer Minute. Wenn Sie 11 Artikel in einer Minute aktualisieren, können nur die ersten 10 eine „Wieder verfügbar“-Benachrichtigungen auslösen.

