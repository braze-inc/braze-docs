---
nav_title: Benachrichtigungen über Preissenkungen
article_title: Benachrichtigungen über Preissenkungen
page_order: 3
alias: "/price_drop_notifications/"
description: "In diesem Artikel werden Benachrichtigungen über Preissenkungen in Braze-Katalogen erläutert."
---

# Benachrichtigungen über Preissenkungen

> Auf dieser Seite erfahren Sie, wie Benachrichtigungen über Preisrückgänge funktionieren und wie Sie sie einrichten und verwenden können. Mit einer Kombination aus Preissenkungsbenachrichtigungen über Braze-Kataloge und einem Canvas können Sie Kund:in benachrichtigen, wenn der Preis eines Artikels gesunken ist.

## Funktionsweise

Wenn ein Benutzer ein benutzerdefiniertes Ereignis für einen Artikel auslöst, abonnieren wir ihn automatisch für den Erhalt von Benachrichtigungen über Preissenkungen für diesen Artikel. Wenn der Preis des Artikels Ihre Bestandsregel erfüllt (z.B. ein Preisrückgang von mehr als 50%), werden alle Abonnenten über eine Kampagne oder Canvas benachrichtigt. Allerdings erhalten nur diejenigen Personen eine Benachrichtigung, die deren Erhalt zugestimmt haben. 

## Anpassen eines angepassten Events für Preissenkungsbenachrichtigungen

Sie richten ein angepasstes Event ein, das als Abo-Event verwendet werden kann, z.B. ein `product_clicked`-Event. Dieses Event muss eine Eigenschaft der Artikel-ID enthalten (Katalogartikel-IDs). Wir empfehlen die Angabe eines Katalognamens, dies ist jedoch nicht erforderlich. Sie geben auch den Namen eines Preisfeldes an, das ein Zahlendatentyp sein muss. 

Sie können ein Abo für einen Nutzer:innen und einen Katalogartikel erstellen, wenn Folgendes eintritt:

- Ein ausgewähltes angepasstes Event wird von einem Nutzer:innen ausgeführt
- Das angepasste Event hat die Eigenschaft `type`, die `price_drop` enthält (`type` muss ein Array sein)

Um sowohl die Benachrichtigung über eine Preisreduzierung als auch über eine Wiederauffüllung des Lagerbestands in demselben Ereignis festzulegen, können Sie die Eigenschaft `type` verwenden, die ein Array sein muss. Wenn ein Artikel eine Preisänderung erfährt, die Ihrer Preisregel entspricht, suchen wir alle Benutzer, die diesen Artikel abonniert haben (Benutzer, die das Abonnement-Ereignis durchgeführt haben) und senden ein benutzerdefiniertes Braze-Ereignis, das Sie zum Auslösen einer Kampagne oder eines Canvas verwenden können. 

Die Event-Eigenschaften werden zusammen mit Ihrem Nutzer:innen versendet, so dass Sie die Artikeldetails als Template in die Kampagne oder das Canvas einfügen können, die/das sendet.

## Benachrichtigungen über Preissenkungen einrichten

Führen Sie diese Schritte aus, um Benachrichtigungen über Preissenkungen in einem bestimmten Katalog einzurichten.

1. Gehen Sie zu Ihrem Katalog und wählen Sie die Registerkarte **Einstellungen**.
2. Wählen Sie den Schalter **Preissenkung**.
3. Wenn die globalen Einstellungen des Katalogs nicht konfiguriert wurden, werden Sie aufgefordert, die angepassten Events und Eigenschaften einzurichten, die zum Auslösen von Benachrichtigungen verwendet werden. <br><br> ![Katalogeinstellungen][2]{: style="max-width:70%;"}

| Feld | Beschreibung |
| --- | --- |
| **Fallback-Katalog** | Der Katalog, der für das Abonnement verwendet wird, wenn es keine `catalog_name` Eigenschaft im benutzerdefinierten Ereignis gibt. |
| **Angepasstes Event für Abos** | Das angepasste Event, um einen Nutzer:in für Katalogbenachrichtigungen zu abonnieren. Wenn das Ereignis eintritt, erhält dieser ein Abonnement. |
| **Angepasstes Event für Abmeldung** | Das angepasste Event, mit dem ein Nutzer:in von den Benachrichtigungen abgemeldet werden kann. Dieses Ereignis ist optional. Wenn der Nutzer:innen dieses Ereignis nicht ausführt, wird er nach 90 Tagen abgemeldet oder wenn das Preissenkungsereignis triggert, je nachdem, was zuerst eintritt. |
| **Event-Eigenschaft für Artikel-ID** | Die Eigenschaft des obigen benutzerdefinierten Ereignisses, die verwendet wird, um das Element für ein Abonnement oder eine Abbestellung zu bestimmen. Diese Eigenschaft des angepassten Events sollte eine Artikelnummer enthalten, die in einem Katalog vorkommt. Das angepasste Event muss eine `catalog_name`-Eigenschaft enthalten, die angibt, in welchem Katalog sich der Artikel befindet. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Hier ist ein Beispiel für ein angepasstes Event:

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
4\. Wählen Sie **Speichern** aus, und fahren Sie mit dem nächsten Abschnitt fort, um Benachrichtigungsregeln einzurichten.

### Einrichten von Benachrichtigungsregeln

1. Rufen Sie die Seite **Einstellungen** Ihres Katalogs auf. 
2. Wählen Sie für **Benachrichtigungsregeln** eine der folgenden Optionen aus:<br>

    - **Alle Abonnent:innen benachrichtigen:** Benachrichtigen Sie alle Kund:innen, die warten, wenn der Preis des Artikels sinkt.
    - **Legen Sie Benachrichtigungsgrenzen fest:** Benachrichtigen Sie eine bestimmte Anzahl von Kund:innen in dem von Ihnen konfigurierten Benachrichtigungszeitraum. Braze benachrichtigt die angegebene Anzahl von Kunden schrittweise, bis es keine Kunden mehr zu benachrichtigen gibt oder bis der Preis des Artikels wieder steigt. Sie dürfen maximal 10.000 Nutzer:innen pro Minute benachrichtigen.<br>

2. Legen Sie das **Feld Preis im Katalog** fest. Dies ist das Katalogfeld zur Ermittlung des Artikelpreises. Es muss ein Zahlentyp sein.
3. Legen Sie die **Preissenkungsregel** fest. Diese Logik bestimmt, ob eine Benachrichtigung gesendet werden soll. Eine Preissenkung kann als prozentuale Preisänderung oder als Wert, um den sich das Preisfeld geändert hat, konfiguriert werden.
4. Wählen Sie **Einstellungen speichern**.

![Katalogeinstellungen, die die aktivierte Preissenkungsfunktion anzeigen. Die Preissenkungsregel ist eine Änderung von drei Prozent des ursprünglichen Preises.][1]

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
