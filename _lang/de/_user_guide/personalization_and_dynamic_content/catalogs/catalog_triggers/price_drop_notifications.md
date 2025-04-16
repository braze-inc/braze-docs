---
nav_title: Benachrichtigungen über Preissenkungen
article_title: Benachrichtigungen über Preissenkungen
page_order: 3
alias: "/price_drop_notifications/"
description: "In diesem Artikel werden Benachrichtigungen über Preissenkungen in Braze-Katalogen erläutert."
---

# Benachrichtigungen über Preissenkungen

> Auf dieser Seite erfahren Sie, wie Benachrichtigungen über Preisrückgänge funktionieren und wie Sie sie einrichten und verwenden können. 

## 

Wenn ein Benutzer ein benutzerdefiniertes Ereignis für einen Artikel auslöst, abonnieren wir ihn automatisch für den Erhalt von Benachrichtigungen über Preissenkungen für diesen Artikel. Wenn der Preis des Artikels Ihre Bestandsregel erfüllt (z.B. ein Preisrückgang von mehr als 50%), werden alle Abonnenten über eine Kampagne oder Canvas benachrichtigt. Allerdings erhalten nur diejenigen Personen eine Benachrichtigung, die deren Erhalt zugestimmt haben. 

## 

Sie richten ein angepasstes Event ein, das als Abo-Event verwendet werden kann, z.B. ein `product_clicked`-Event. Dieses Event muss eine Eigenschaft der Artikel-ID enthalten (Katalogartikel-IDs).   



- 
- 

 Wenn ein Artikel eine Preisänderung erfährt, die Ihrer Preisregel entspricht, suchen wir alle Benutzer, die diesen Artikel abonniert haben (Benutzer, die das Abonnement-Ereignis durchgeführt haben) und senden ein benutzerdefiniertes Braze-Ereignis, das Sie zum Auslösen einer Kampagne oder eines Canvas verwenden können. 



## Benachrichtigungen über Preissenkungen einrichten

Führen Sie diese Schritte aus, um Benachrichtigungen über Preissenkungen in einem bestimmten Katalog einzurichten.

1. Gehen Sie zu Ihrem Katalog und wählen Sie die Registerkarte **Einstellungen**.
2. Wählen Sie den Schalter **Preissenkung**.
3.  <br><br> ![Katalogeinstellungen][2]{: style="max-width:70%;"}

|  |  |
| --- | --- |
|  |  |
|  |  Wenn das Ereignis eintritt, erhält dieser ein Abonnement. |
|  |  Dieses Ereignis ist optional. Wenn der Nutzer:innen dieses Ereignis nicht ausführt, wird er nach 90 Tagen abgemeldet oder wenn das Preissenkungsereignis triggert, je nachdem, was zuerst eintritt. |
|  | Die Eigenschaft des obigen benutzerdefinierten Ereignisses, die verwendet wird, um das Element für ein Abonnement oder eine Abbestellung zu bestimmen. Diese Eigenschaft des angepassten Events sollte eine Artikelnummer enthalten, die in einem Katalog vorkommt.  |




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
4\. 

### 

1.  
2. <br>

    -  
    -   Braze benachrichtigt die angegebene Anzahl von Kunden schrittweise, bis es keine Kunden mehr zu benachrichtigen gibt oder bis der Preis des Artikels wieder steigt. Sie dürfen maximal 10.000 Nutzer:innen pro Minute benachrichtigen.<br>

2.  Dies ist das Katalogfeld zur Ermittlung des Artikelpreises. Es muss ein Zahlentyp sein.
3. Legen Sie die **Preissenkungsregel** fest. Diese Logik bestimmt, ob eine Benachrichtigung gesendet werden soll. Eine Preissenkung kann als prozentuale Preisänderung oder als Wert, um den sich das Preisfeld geändert hat, konfiguriert werden.
4. Wählen Sie **Einstellungen speichern**.

![Katalogeinstellungen, die die aktivierte Preissenkungsfunktion anzeigen. 

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
