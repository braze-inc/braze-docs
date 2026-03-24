---
nav_title: Benachrichtigungen über Preissenkungen
article_title: Benachrichtigungen über Preissenkungen
page_order: 3
alias: "/price_drop_notifications/"
description: "In diesem Referenzartikel wird beschrieben, wie Sie Benachrichtigungen über Preissenkungen in Braze-Katalogen erstellen."
---

# Benachrichtigungen über Preissenkungen

> Auf dieser Seite erfahren Sie, wie Benachrichtigungen über Preissenkungen funktionieren und wie Sie sie einrichten und verwenden können. Mit einer Kombination aus Preissenkungsbenachrichtigungen über Braze-Kataloge und einem Canvas können Sie Kund:innen benachrichtigen, wenn der Preis eines Artikels gesunken ist.

## Funktionsweise

Wenn eine Nutzer:in ein angepasstes Event für einen Artikel auslöst, wird sie automatisch für den Erhalt von Benachrichtigungen über Preissenkungen für diesen Artikel abonniert. Wenn der Preis des Artikels Ihre Bestandsregel erfüllt (z. B. ein Preisrückgang von mehr als 50 %), sind alle Abonnent:innen für Benachrichtigungen über eine Kampagne oder ein Canvas berechtigt. Allerdings erhalten nur Nutzer:innen, die sich für Benachrichtigungen entschieden haben, tatsächlich eine Benachrichtigung. 

## Einrichten eines angepassten Events für Preissenkungsbenachrichtigungen

Sie richten ein angepasstes Event ein, das Sie als Abo-Event verwenden können, z. B. ein `product_clicked`-Event. Dieses Event muss eine Eigenschaft der Artikel-ID enthalten (Katalogartikel-IDs). Wir empfehlen die Angabe eines Katalognamens, dies ist jedoch nicht erforderlich. Sie geben auch den Namen eines Preisfeldes an, das den Datentyp Zahl haben muss. 

Sie können ein Preissenkungsabo für eine Nutzer:in und einen Katalogartikel erstellen, wenn Folgendes eintritt:

- Ein ausgewähltes angepasstes Event wird von einer Nutzer:in ausgeführt
- Das angepasste Event hat die Eigenschaft `type`, die `price_drop` enthält (`type` muss ein Array sein)

Um sowohl Preissenkungsbenachrichtigungen als auch Wieder-auf-Lager-Benachrichtigungen im selben Event festzulegen, können Sie die Eigenschaft `type` verwenden, die ein Array sein muss. Wenn ein Artikel eine Preisänderung erfährt, die Ihrer Preisregel entspricht, suchen wir alle Nutzer:innen, die diesen Artikel abonniert haben (Nutzer:innen, die das Abo-Event ausgeführt haben), und senden ein angepasstes Braze-Event, das Sie zum Triggern einer Kampagne oder eines Canvas verwenden können. 

Die Event-Eigenschaften werden zusammen mit der Nutzer:in gesendet, sodass Sie die Artikeldetails als Template in die Kampagne oder das Canvas einfügen können.

## Benachrichtigungen über Preissenkungen einrichten

Führen Sie diese Schritte aus, um Benachrichtigungen über Preissenkungen in einem bestimmten Katalog einzurichten.

1. Gehen Sie zu Ihrem Katalog und wählen Sie den Tab **Einstellungen**.
2. Wählen Sie den Schalter **Preissenkung**.
3. Wenn die globalen Katalogeinstellungen nicht konfiguriert wurden, werden Sie aufgefordert, die angepassten Events und Eigenschaften einzurichten, die zum Triggern von Benachrichtigungen verwendet werden. <br><br> ![Katalogeinstellungen.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}

| Feld | Beschreibung |
| --- | --- |
| **Fallback-Katalog** | Der Katalog, der für das Abo verwendet wird, wenn es keine `catalog_name`-Eigenschaft im angepassten Event gibt. |
| **Angepasstes Event für Abos** | Das angepasste Event, um eine Nutzer:in für Katalogbenachrichtigungen zu abonnieren. Wenn dieses Event eintritt, wird die Nutzer:in, die das Event ausgeführt hat, abonniert. |
| **Angepasstes Event für Abmeldung** | Das angepasste Event, mit dem eine Nutzer:in von den Benachrichtigungen abgemeldet werden kann. Dieses Event ist optional. Wenn die Nutzer:in dieses Event nicht ausführt, wird sie nach 90 Tagen abgemeldet oder wenn das Preissenkungsevent getriggert wird – je nachdem, was zuerst eintritt. |
| **Event-Eigenschaft für Artikel-ID** | Die Eigenschaft des obigen angepassten Events, die verwendet wird, um den Artikel für ein Abo oder eine Abmeldung zu bestimmen. Diese Eigenschaft des angepassten Events sollte eine Artikel-ID enthalten, die in einem Katalog vorkommt. Das angepasste Event muss eine `catalog_name`-Eigenschaft enthalten, die angibt, in welchem Katalog sich der Artikel befindet. |
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
4. Wählen Sie **Speichern** und fahren Sie mit dem nächsten Abschnitt fort, um Benachrichtigungsregeln einzurichten.

### Einrichten von Benachrichtigungsregeln

1. Rufen Sie die Seite **Einstellungen** Ihres Katalogs auf. 
2. Wählen Sie für **Benachrichtigungsregeln** eine der folgenden Optionen aus:<br>

    - **Alle Abonnent:innen benachrichtigen:** Benachrichtigen Sie alle Kund:innen, die warten, wenn der Preis des Artikels sinkt.
    - **Benachrichtigungsgrenzen festlegen:** Benachrichtigen Sie eine bestimmte Anzahl von Kund:innen in dem von Ihnen konfigurierten Benachrichtigungszeitraum. Braze benachrichtigt die angegebene Anzahl von Kund:innen schrittweise, bis es keine Kund:innen mehr zu benachrichtigen gibt oder bis der Preis des Artikels wieder steigt. Ihre Benachrichtigungsrate darf 10.000 Nutzer:innen pro Minute nicht überschreiten.<br>

2. Legen Sie das **Preisfeld im Katalog** fest. Dies ist das Katalogfeld zur Ermittlung des Artikelpreises. Es muss ein Zahlentyp sein.
3. Legen Sie die **Preissenkungsregel** fest. Diese Logik bestimmt, ob eine Benachrichtigung gesendet werden soll. Eine Preissenkung kann als prozentuale Preisänderung oder durch die Änderung des Wertes für das Preisfeld konfiguriert werden.
4. Wählen Sie **Einstellungen speichern**.

![Katalogeinstellungen, die die aktivierte Preissenkungsfunktion anzeigen. Die Preissenkungsregel ist eine Änderung von drei Prozent des ursprünglichen Preises.]({% image_buster /assets/img/price_drop_notifications.png %})

{% alert important %}
Die Benachrichtigungsregeln in diesen Einstellungen ersetzen nicht die Canvas-Benachrichtigungseinstellungen, wie z. B. Ruhezeiten.
{% endalert %}

## Benachrichtigungen über Preissenkungen in einem Canvas verwenden

Nachdem Sie die Benachrichtigungen über Preissenkungen in einem Katalog eingerichtet haben, folgen Sie diesen Schritten, um diese Benachrichtigungen in einem Canvas zu verwenden.

1. Richten Sie ein aktionsbasiertes Canvas ein.
2. Wählen Sie als Trigger **Preissenkungsevent durchführen**.
3. Wählen Sie den Namen des Katalogs mit den Preissenkungsbenachrichtigungen aus.
4. Fahren Sie mit der [Einrichtung]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) Ihres Canvas fort, wie Sie es gewohnt sind.

Jetzt werden Ihre Kund:innen benachrichtigt, wenn der Preis eines Artikels sinkt.

### Liquid verwenden

Um Details zum reduzierten Katalogartikel als Template einzufügen, können Sie den Liquid-Tag `context` verwenden, um auf die `item_id` zuzugreifen. 

Die Verwendung von {%raw%}``{{context.${catalog_update}.item_id}}``{%endraw%} gibt die ID des Artikels zurück, dessen Preis gesunken ist. {%raw%}``{{context.${catalog_update}.previous_value}}``{%endraw%} gibt den Preiswert des Artikels vor dem Update zurück, und {%raw%}``{{context.${catalog_update}.new_value}}``{%endraw%} gibt den neuen Preiswert nach dem Update zurück. 

Verwenden Sie den Liquid-Tag {%raw%}``{% catalog_items <name_of_your_catalog> {{context.${catalog_update}.item_id}} %}``{%endraw%} am Anfang Ihrer Nachricht und nutzen Sie anschließend {%raw%}`{{items[0].<field_name>}}`{%endraw%}, um auf Daten zu diesem Artikel in der gesamten Nachricht zuzugreifen.

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}

## Überlegungen

- Nutzer:innen sind für 90 Tage abonniert. Wenn der Preis eines Artikels innerhalb von 90 Tagen nicht sinkt, wird die Nutzer:in aus dem Abo entfernt.
- Wenn Sie die Benachrichtigungsregel **Alle Abonnent:innen benachrichtigen** verwenden, benachrichtigt Braze 100.000 Nutzer:innen innerhalb von 10 Minuten.
- Braze unterstützt bis zu 50.000 aktualisierte Artikel pro Tag, die für das Triggern von Preissenkungsbenachrichtigungen berechtigt sind. Sie können bis zu 100 Millionen aktive Abos gleichzeitig haben, wobei jedes Abo ein Nutzerprofil darstellt, das einen Katalogartikel beobachtet.