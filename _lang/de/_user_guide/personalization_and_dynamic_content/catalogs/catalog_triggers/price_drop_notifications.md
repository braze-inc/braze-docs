---
nav_title: Benachrichtigungen über Preissenkungen
article_title: Benachrichtigungen über Preissenkungen
page_order: 3
alias: "/price_drop_notifications/"
description: "In diesem Artikel werden Benachrichtigungen über Preissenkungen in Braze-Katalogen erläutert."
---

# Benachrichtigungen über Preissenkungen

> Mit einer Kombination aus Preissenkungsbenachrichtigungen über Braze-Kataloge und einem Canvas können Sie Kunden benachrichtigen, wenn der Preis eines Artikels gesunken ist. Jedes Mal, wenn ein Kunde ein bestimmtes angepasstes Event ausführt, kann er automatisch benachrichtigt werden, wenn der Artikelpreis reduziert wird.

Wenn ein Benutzer ein benutzerdefiniertes Ereignis für einen Artikel auslöst, abonnieren wir ihn automatisch für den Erhalt von Benachrichtigungen über Preissenkungen für diesen Artikel. Wenn der Preis des Artikels Ihre Bestandsregel erfüllt (z.B. ein Preisrückgang von mehr als 50%), werden alle Abonnenten über eine Kampagne oder Canvas benachrichtigt. Allerdings erhalten nur diejenigen Personen eine Benachrichtigung, die deren Erhalt zugestimmt haben. 

## Wie Benachrichtigungen über Preissenkungen funktionieren

Sie richten ein angepasstes Event ein, das als Abo-Event verwendet werden kann, z.B. ein `product_clicked`-Event. Dieses Event muss eine Eigenschaft der Artikel-ID enthalten (Katalogartikel-IDs). Wir empfehlen, einen Katalognamen anzugeben. Dies ist aber nicht zwingend erforderlich. Geben Sie außerdem den Namen eines Preisfeldes mit dem Datentyp "Zahl" an. 

Wenn ein ausgewähltes angepasstes Event ausgeführt wird, das eine `type`-Eigenschaft mit `price_drop` enthält, können Sie so entsprechende nutzer- und artikelspezifische Abos zu Preissenkungen erstellen. Sie können das `type`-Array auch verwenden, um Benachrichtigungen sowohl zu Preissenkungen als auch zu wieder lieferbaren Artikeln im selben Event einzurichten.

Wenn ein Artikel eine Preisänderung erfährt, die Ihrer Preisregel entspricht, suchen wir alle Benutzer, die diesen Artikel abonniert haben (Benutzer, die das Abonnement-Ereignis durchgeführt haben) und senden ein benutzerdefiniertes Braze-Ereignis, das Sie zum Auslösen einer Kampagne oder eines Canvas verwenden können.

Die Event-Eigenschaften werden zusammen mit den Nutzerdaten gesendet, sodass Sie die Artikeldetails als Template in die zu versendende Kampagne bzw. das Canvas einfügen können.

## Benachrichtigungen über Preissenkungen einrichten

Führen Sie diese Schritte aus, um Benachrichtigungen über Preissenkungen in einem bestimmten Katalog einzurichten.

1. Gehen Sie zu Ihrem Katalog und wählen Sie die Registerkarte **Einstellungen**.<br>
2. Wählen Sie den Schalter **Preissenkung**.<br>
3. Wenn die allgemeinen Einstellungen des Katalogs noch nicht konfiguriert worden sind, werden Sie dazu aufgefordert, angepasste Events und Eigenschaften einzurichten, mit denen Benachrichtigungen getriggert werden sollen:
    <br> ![Katalogeinstellungen][2]{: style="max-width:70%;"}
    - **Ersatzkatalog:** Der Katalog, der für das Abonnement verwendet wird, wenn es keine `catalog_name` Eigenschaft im benutzerdefinierten Ereignis gibt.
    - **Angepasstes Event für Abonnements:** Das benutzerdefinierte Ereignis von Braze, das verwendet wird, um einen Benutzer für Katalogbenachrichtigungen zu abonnieren. Wenn das Ereignis eintritt, erhält dieser ein Abonnement.
    - **Angepasstes Event zur Abmeldung:** Das benutzerdefinierte Ereignis von Braze, mit dem ein Benutzer von den Benachrichtigungen abgemeldet wird.
    - **Ereigniseigenschaft Artikelnummer:** Die Eigenschaft des obigen benutzerdefinierten Ereignisses, die verwendet wird, um das Element für ein Abonnement oder eine Abbestellung zu bestimmen. Diese Eigenschaft des angepassten Events sollte eine Artikelnummer enthalten, die in einem Katalog vorkommt. Das angepasste Event muss eine `catalog_name`-Eigenschaft enthalten, die angibt, in welchem Katalog sich der Artikel befindet.
   
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
                    "type": ["price_drop", "back_in_stock"]
                }
            }
        ]
    }
    ```

{: start="4"}
4\. Wählen Sie **Speichern** und fahren Sie mit der Seite **Einstellungen** des Katalogs fort.
5\. Legen Sie Ihre Benachrichtigungsregel fest. Es gibt zwei Optionen:
    - **Alle abonnierten Benutzer benachrichtigen** benachrichtigt alle Kunden, die warten, wenn der Preis des Artikels fällt.
    - **Benachrichtigungslimits festlegen** benachrichtigt eine bestimmte Anzahl von Kunden pro von Ihnen konfiguriertem Benachrichtigungszeitraum. Braze benachrichtigt die angegebene Anzahl von Kunden schrittweise, bis es keine Kunden mehr zu benachrichtigen gibt oder bis der Preis des Artikels wieder steigt. Sie dürfen maximal 10.000 Nutzer:innen pro Minute benachrichtigen.
6\. Legen Sie das **Feld Preis im Katalog** fest. Dies ist das Katalogfeld zur Ermittlung des Artikelpreises. Es muss ein Zahlentyp sein.<br>
7\. Legen Sie die **Preissenkungsregel** fest. Diese Logik bestimmt, ob eine Benachrichtigung gesendet werden soll. Eine Preissenkung kann als prozentuale Preisänderung oder als Wert, um den sich das Preisfeld geändert hat, konfiguriert werden.<br>
8\. Wählen Sie **Einstellungen speichern**.

![Katalogeinstellungen, die die aktivierte Preissenkungsfunktion anzeigen. Die Preissenkungsregel ist eine Änderung von drei Prozent des ursprünglichen Preises.][1]{:style="max-width:60%;"}

{% alert important %}
Die Benachrichtigungsregeln in diesen Einstellungen ersetzen nicht die Canvas-Benachrichtigungseinstellungen, wie z.B. Stille Stunden.
{% endalert %}

## Benachrichtigungen über Preisrückgänge in Canvas verwenden

Nachdem Sie die Benachrichtigungen über Preissenkungen in einem Katalog eingerichtet haben, folgen Sie diesen Schritten, um diese Benachrichtigungen in einem Canvas zu verwenden.

1. Richten Sie einen aktionsbasierten Canvas ein.
2. Wählen Sie als Auslöser **Preissturzereignis durchführen**.
3. Wählen Sie den Namen des Katalogs mit den Preissenkungsbenachrichtigungen.
4. Fahren Sie mit der [Einrichtung]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) Ihres Canvas fort, wie Sie es gewohnt sind.

Jetzt werden Ihre Kunden benachrichtigt, wenn der Preis eines Artikels sinkt.

### Liquid verwenden

Um ein Template mit Details zu dem reduzierten Katalogartikel zu erstellen, können Sie das Liquid-Tag `canvas_entry_properties` verwenden, um auf die Seite `item_id` zuzugreifen. 

Die Verwendung von {%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%} gibt die ID des Artikels zurück, dessen Preis gesunken ist. {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%} gibt den Preiswert des Artikels vor der Aktualisierung zurück und {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%} gibt den neuen Preiswert nach der Aktualisierung zurück. 

Verwenden Sie das {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}}``{%endraw%} Liquid-Tag am Anfang Ihrer Nachricht und dann {%raw%}`{{items[0].<field_name>}}`{%endraw%}, um in der gesamten Nachricht auf Daten zu diesem Artikel zuzugreifen.

## Überlegungen

- Benutzer sind für 90 Tage abonniert. Wenn der Preis eines Artikels innerhalb von 90 Tagen nicht sinkt, wird der Benutzer aus dem Abonnement entfernt.
- Wenn Sie die Benachrichtigungsregel **Alle abonnierten Benutzer benachrichtigen** verwenden, wird Braze 100.000 Benutzer innerhalb von 10 Minuten benachrichtigen.
- Braze kann bis zu 10 Artikelaktualisierungen pro Minute verarbeiten. Wenn Sie also 11 Artikel pro Minute aktualisieren, können nur die ersten 10 davon eine Benachrichtigung über eine Preissenkung auslösen.

[1]: {% image_buster /assets/img/price_drop_notifications.png %}
[2]: {% image_buster /assets/img/catalog_settings_drawer.png %}
