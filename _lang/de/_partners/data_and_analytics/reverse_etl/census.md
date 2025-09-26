---
nav_title: Census
article_title: Census
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und Census, einer Datenintegrationsplattform, die es Ihnen erlaubt, dynamisch Targeting Segmente mit Daten aus Ihrem Cloud Warehouse zusammenzustellen."
alias: /partners/census/
page_type: partner
search_tag: Partner

---

# Census

> [Census](https://www.getcensus.com/) ist eine Datenaktivierungsplattform, die Cloud Data Warehouses wie Snowflake und BigQuery mit Braze verbindet. Marketingteams können das Potenzial ihrer First-Party-Daten nutzen, um dynamische Zielgruppensegmente zu erstellen, Kundenattribute zu synchronisieren, Kampagnen zu personalisieren und ihre Daten in Braze auf dem neuesten Stand zu halten. Es ist einfacher als je zuvor, mit zuverlässigen, verwertbaren Daten zu handeln - ohne CSV-Uploads oder technische Hilfsmittel.

Die Integration von Braze und Census erlaubt es Ihnen, Zielgruppen oder Produktdaten dynamisch in Braze zu importieren, um personalisierte Kampagnen zu versenden. Sie können in Braze zum Beispiel eine Kohorte für "Newsletter-Abonnenten mit CLV > 1000" erstellen, um hochwertige Kunden anzusprechen, oder "Nutzer:innen, die in den letzten 30 Tagen aktiv waren", um bestimmte Nutzer:innen für den Test eines bevorstehenden Beta-Features anzusprechen.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| Census-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein [Census-Konto](https://www.getcensus.com/). |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit allen Nutzerdaten-Berechtigungen (außer für `users.delete`) und `segments.list`. Die Berechtigungen können sich ändern, wenn Census die Unterstützung für weitere Braze-Objekte hinzufügt. Daher sollten Sie entweder jetzt mehr Berechtigungen erteilen oder ein Update dieser Berechtigungen für die Zukunft planen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) ab. |
| Data Warehouse und Datenmodell | Bevor Sie mit der Integration beginnen, müssen Sie ein Data Warehouse in Census einrichten und ein Modell der Teilmenge von Daten definieren, die Sie mit Braze synchronisieren möchten. Besuchen Sie die [Census Dokumentation](https://docs.getcensus.com/destinations/braze), um eine Liste der verfügbaren Datenquellen und eine Anleitung zur Modellerstellung zu erhalten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integration

### Schritt 1: Braze Serviceverbindung erstellen

Um Census in die Census-Plattform zu integrieren, navigieren Sie zum Tab **Verbindungen** und wählen Sie **Neues Ziel**, um eine neue Braze Serviceverbindung zu erstellen.

In der daraufhin angezeigten Eingabeaufforderung benennen Sie diese Verbindung und geben die URL des Braze-Endpunkts und den REST-API-Schlüssel von Braze an (sowie optional Ihren Datenimport-Schlüssel für die Synchronisierung von Kohorten).

![]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### Schritt 2: Eine Census-Synchronisation erstellen

Um Kund:innen mit Braze zu synchronisieren, müssen Sie eine Synchronisierung erstellen. Hier legen Sie fest, wo die Daten synchronisiert werden sollen und wie die Felder auf den beiden Plattformen abgebildet werden sollen.

1. Navigieren Sie zum Tab **Synchronisierungen** und wählen Sie **Neue Synchronisierung**.<br><br> 
2. Wählen Sie im Composer das Quelldatenmodell aus Ihrem Data Warehouse aus.<br><br>
3. Legen Sie fest, wohin das Modell synchronisiert werden soll. Wählen Sie **Braze** als Ziel und den [unterstützten Objekttyp](#supported-objects) für die Synchronisierung aus.<br>![In der Eingabeaufforderung "Ziel auswählen" wird "Braze" als Verbindung ausgewählt, und es werden verschiedene Objekte aufgelistet.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. Wählen Sie aus, welche Synchronisierungsregel Sie anwenden möchten**(Update oder Erstellen** ist die häufigste Wahl, aber Sie können auch fortschrittlichere Regeln wählen, um z.B. das Löschen von Daten zu behandeln).<br><br>
5. Als nächstes wählen Sie für den Abgleich von Datensätzen einen Synchronisationsschlüssel, um Ihr Braze-Objekt einem Modellfeld [zuzuordnen](#supported-objects).<br>![In der Eingabeaufforderung "Wählen Sie einen Sync-Schlüssel" wird die "External User ID" von Braze mit der "user_id" in der Quelle abgeglichen.]({% image_buster /assets/img/census/census_1.png %}){: style="max-width:80%;"}<br><br>
6. Abschließend ordnen Sie die Census Datenfelder den entsprechenden Braze Feldern zu.<br>![Census-Abbildung]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
7. Bestätigen Sie die Details und erstellen Sie die Synchronisierung. 

Nachdem die Synchronisierung durchgeführt wurde, finden Sie die Nutzerdaten in Braze. Sie können jetzt ein Braze Segment erstellen und zu zukünftigen Kampagnen und Canvase hinzufügen, um diese Nutzer:innen zu targetieren. 

{% alert note %}
Wenn Sie die Integration von Census und Braze verwenden, sendet Census bei jeder Synchronisierung nur die Deltas (sich ändernde Daten) an Braze.
{% endalert %}

## Unterstützte Objekte

Census unterstützt derzeit die Synchronisierung der folgenden Braze-Objekte:

| Objektname | Sync-Verhaltensweisen |
| --- | --- |
| Nutzer:in | Aktualisieren, Erstellen, Spiegeln, Löschen |
| Kohorte | Aktualisieren, Erstellen, Spiegeln | 
| Katalog | Aktualisieren, Erstellen, Spiegeln |
| Abo-Gruppe Mitgliedschaft | Spiegel |
| Event | Anhängen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Außerdem unterstützt Census das Senden [strukturierter Daten](https://docs.getcensus.com/destinations/braze#supported-objects) an Braze: 
- Nutzer:innen Push-Token: Um Push-Token zu senden, sollten Ihre Daten als Array von Objekten mit 2-3 Werten strukturiert sein: `app_id`, `token`, und einem optionalen `device_id`.
- Verschachtelte angepasste Attribute: Es werden sowohl Objekte als auch Arrays unterstützt. Ab April 2022 befindet sich dieses Feature noch im Early Access. Möglicherweise müssen Sie Ihren Braze-Konto Manager:in kontaktieren, um Zugang zu erhalten.

