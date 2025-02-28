---
nav_title: Volkszählung
article_title: Volkszählung
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Census, einer Datenintegrationsplattform, die es Ihnen ermöglicht, mit Daten aus Ihrem Cloud Warehouse dynamisch gezielte Benutzersegmente zu erstellen."
alias: /partners/census/
page_type: partner
search_tag: Partner

---

# Volkszählung

> [Census][1] ist eine Datenaktivierungsplattform, die Cloud Data Warehouses wie Snowflake und BigQuery mit Braze verbindet. Marketingteams können die Leistungsfähigkeit ihrer Erstanbieterdaten nutzen, um dynamische Zielgruppensegmente zu erstellen, Kundenattribute zu synchronisieren, um Kampagnen zu personalisieren und alle Daten in Braze auf dem neuesten Stand zu halten. Es ist einfacher als je zuvor, mit verlässlichen, umsetzbaren Daten Maßnahmen zu ergreifen - ohne CSV-Uploads oder technische Hilfsmittel.

Die Integration von Braze und Census ermöglicht es Ihnen, Zielgruppen oder Produktdaten dynamisch in Braze zu importieren, um personalisierte Kampagnen zu versenden. Sie können in Braze zum Beispiel eine Kohorte für "Newsletter-Abonnenten mit einem CLV > 1000" erstellen, um hochwertige Kunden anzusprechen, oder "Benutzer, die in den letzten 30 Tagen aktiv waren", um bestimmte Benutzer für den Test einer bevorstehenden Beta-Funktion anzusprechen.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| Volkszählung Konto | Ein [Census-Konto][1] ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit allen Benutzerdaten-Berechtigungen (außer `users.delete`) und `segments.list` Berechtigungen. Die Berechtigungen können sich ändern, wenn Census die Unterstützung für weitere Braze-Objekte hinzufügt. Daher sollten Sie entweder jetzt mehr Berechtigungen erteilen oder planen, diese Berechtigungen in Zukunft zu aktualisieren. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz][2] ab. |
| Data Warehouse und Datenmodell | Bevor Sie mit der Integration beginnen, müssen Sie ein Data Warehouse in Census einrichten und ein Modell für die Teilmenge der Daten definieren, die Sie mit Braze synchronisieren möchten. In der [Census-Dokumentation](https://docs.getcensus.com/destinations/braze) finden Sie eine Liste der verfügbaren Datenquellen und eine Anleitung zur Modellerstellung. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integration

### Schritt 1: Braze Serviceverbindung erstellen

Um Census in die Census-Plattform zu integrieren, navigieren Sie zur Registerkarte **Verbindungen** und wählen Sie **Neues Ziel**, um eine neue Braze-Serviceverbindung zu erstellen.

In der daraufhin angezeigten Eingabeaufforderung geben Sie dieser Verbindung einen Namen und Ihre Braze-Endpunkt-URL und Ihren Braze-REST-API-Schlüssel an (und optional Ihren Datenimportschlüssel zur Synchronisierung von Kohorten).

![][8]{: style="max-width:60%;"}

### Schritt 2: Eine Census-Synchronisation erstellen

Um Kunden mit Braze zu synchronisieren, müssen Sie eine Synchronisierung erstellen. Hier legen Sie fest, wohin die Daten synchronisiert werden sollen und wie die Felder zwischen den beiden Plattformen zugeordnet werden sollen.

1. Navigieren Sie zur Registerkarte **Syncs** und wählen Sie **Neue Sync**.<br><br> 
2. Wählen Sie im Composer das Quelldatenmodell aus Ihrem Data Warehouse.<br><br>
3. Legen Sie fest, wohin das Modell synchronisiert werden soll. Wählen Sie **Braze** als Ziel und den zu synchronisierenden [Objekttyp](#supported-objects).<br>![In der Eingabeaufforderung "Wählen Sie ein Ziel" wird "Braze" als Verbindung ausgewählt, und es werden verschiedene Objekte aufgelistet.][10]{: style="max-width:80%;"}<br><br>
4. Wählen Sie aus, welche Synchronisierungsregel Sie anwenden möchten**(Aktualisieren oder Erstellen** ist die häufigste Wahl, aber Sie können auch fortgeschrittenere Regeln wählen, um z.B. das Löschen von Daten zu behandeln).<br><br>
5. Als nächstes wählen Sie für den Datensatzabgleich einen Synchronisationsschlüssel, um Ihr Braze-Objekt einem Modellfeld [zuzuordnen](#supported-objects).<br>![In der Aufforderung "Wählen Sie einen Sync-Schlüssel" wird "External User ID" aus Braze mit "user_id" in der Quelle abgeglichen.][9]{: style="max-width:80%;"}<br><br>
6. Zum Schluss ordnen Sie die Census-Datenfelder den entsprechenden Braze-Feldern zu.<br>![Kartierung der Volkszählung][11]{: style="max-width:80%;"}<br><br>
7. Bestätigen Sie die Details und erstellen Sie die Synchronisierung. 

Nachdem die Synchronisierung ausgeführt wurde, finden Sie die Benutzerdaten in Braze. Sie können jetzt ein Braze-Segment erstellen und zu zukünftigen Braze-Kampagnen und Canvases hinzufügen, um diese Benutzer anzusprechen. 

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
| Abonnement Gruppenmitgliedschaft | Spiegel |
| Event | Anhängen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Außerdem unterstützt Census das Senden [strukturierter Daten](https://docs.getcensus.com/destinations/braze#supported-objects) an Braze: 
- Benutzer-Push-Tokens: Um Push-Token zu senden, sollten Ihre Daten als Array von Objekten mit 2-3 Werten strukturiert sein: `app_id`, `token`, und einem optionalen `device_id`.
- Verschachtelte benutzerdefinierte Attribute: Es werden sowohl Objekte als auch Arrays unterstützt. Ab April 2022 befindet sich diese Funktion noch im Early Access. Möglicherweise müssen Sie Ihren Braze-Kundenbetreuer kontaktieren, um Zugang zu erhalten.

[1]: https://www.getcensus.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[8]: {% image_buster /assets/img/census/add_service.png %}
[9]: {% image_buster /assets/img/census/census_1.png %}
[10]: {% image_buster /assets/img/census/census_2.png %}
[11]: {% image_buster /assets/img/census/census_3.png %}