---
nav_title: Schatzdaten
article_title: Schatzdaten
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Treasure Data, einer Plattform für Unternehmenskundendaten, die es Ihnen ermöglicht, Auftragsergebnisse direkt in Braze zu schreiben."
alias: /partners/treasure_data/
page_type: partner
search_tag: Partner

---

# Schatzdaten

> [Treasure Data][4] ist eine Kundendatenplattform (CDP), die Informationen aus verschiedenen Quellen sammelt und an eine Vielzahl von anderen Stellen in Ihrem Marketing-Stack weiterleitet.

Die Braze- und Treasure Data-Integration ermöglicht es Ihnen, Auftragsergebnisse aus Treasure Data direkt in Braze zu schreiben, so dass Sie:
* **Externe IDs zuordnen**: Ordnen Sie IDs dem Braze-Benutzerkonto aus Ihrem CRM-System zu. 
* **Verwalten Sie die Abmeldung**: Wenn ein Endbenutzer seine Zustimmung aktualisiert und sich entscheidet, nicht teilzunehmen.
* **Laden Sie Ihr Tracking von Ereignissen, Käufen oder benutzerdefinierten Profilattributen hoch**. Diese Informationen können Ihnen helfen, präzise Kundensegmente zu erstellen, die das Benutzererlebnis für Ihre Kampagnen verbessern.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| Treasure Data Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Treasure Data-Konto](https://www.treasuredata.com/custom-demo/). |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track`, `users.delete`, `users.alias.new`, `users.identify`.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze URL für Ihre Instanz][1] ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Anwendungsfälle

Sie können Ihre konsolidierten Kundenprofile aus Treasure Data mit Braze synchronisieren, um Zielsegmente zu erstellen. Treasure Data unterstützt First-Party-Cookie-Daten, Mobile IDs, Systeme von Drittanbietern wie Ihr CRM und vieles mehr.

## Integration

### Schritt 1: Erstellen Sie eine neue Verbindung

Navigieren Sie in Treasure Data zum **Katalog** unter dem **Integrations-Hub**, suchen Sie nach **Braze** und wählen Sie es aus. 

In der daraufhin angezeigten Eingabeaufforderung **Neue Authentifizierung** geben Sie Ihrer Verbindung einen Namen und Ihren Braze REST API-Schlüssel sowie den REST-Endpunkt an. Wählen Sie **Fertig**, wenn Sie fertig sind.

![][2]{: style="max-width:80%;"}

### Schritt 2: Definieren Sie Ihre Anfrage

Navigieren Sie in Treasure Data zu **Abfragen** unter Ihrer **Daten-Workbench** und wählen Sie eine Abfrage aus, für die Sie Daten exportieren möchten. Führen Sie diese Abfrage aus, um die Ergebnismenge zu überprüfen.

{% alert note %}
Für Benutzer, die HIVE zum Erstellen von Abfragen verwenden, verlangt HIVE, dass alle Spalten oder Tabellen, die mit einem Unterstrich beginnen, in Anführungszeichen gesetzt werden. Zum Beispiel: `_merge_objects`.
{% endalert %}

Wählen Sie anschließend **Ergebnisse exportieren** und wählen Sie eine vorhandene Integrationsauthentifizierung.

![][11]{: style="max-width:80%;"}

Definieren Sie zusätzliche Parameter für die Exportergebnisse, wie im folgenden [Abschnitt über die Anpassung](#customization) beschrieben. Überprüfen Sie in Ihrem Export-Integrationsinhalt die Integrationsparameter.

![Die Seite "Ergebnisse exportieren". Auf dieser Seite befinden sich Felder für "Modus", "Datensatztyp" und "Vorformatierte Felder". In diesem Beispiel sind die Felder "Benutzerspur" und "Benutzerdefinierte Ereignisse" auf diese Felder eingestellt.][3]{: style="max-width:80%;"}

Wählen Sie schließlich **Fertig**, führen Sie Ihre Abfrage aus und überprüfen Sie, ob Ihre Daten nach Braze übertragen wurden.

### Anpassung

Die Parameter der Exportergebnisse sind in der folgenden Tabelle aufgeführt:

| Parameter                 | Werte | Beschreibung |
|---------------------------|---|---|
| `mode`                    | Benutzer - Neuer Alias<br>Benutzer - Identifizieren<br>Benutzer - Spur<br>Benutzer - Löschen | Stecker-Modus |
| `pre_formatted_fields`    | String | Verwenden Sie diese Option für Array- oder JSON-Spalten, um das Format beizubehalten. |
| `track_record_type`       | Angepasste Events<br>Käufe<br>Benutzerprofil-Attribute| Aufzeichnungstyp für **Benutzer - Track-Modus**  |
| `skip_on_invalid_records` | Boolesch | Falls aktiviert, fahren Sie fort und ignorieren alle ungültigen Datensätze für die JSON-Spalte. <br> Andernfalls wird der Auftrag abgebrochen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Besuchen Sie [Treasure Data](https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration) für weitere Informationen über vorformatierte Felder, Beispielabfragen, Parameterdetails und die Planung von Abfrageexportaufträgen.
{% endalert %}

## Webhooks

Treasure Data-Benutzer können Daten über die öffentliche REST-API einlesen. Sie können Treasure Data verwenden, um benutzerdefinierte Webhooks für Ihre Daten zu erstellen. Um mehr zu erfahren, besuchen Sie [Treasure Data][6]

[6]: https://docs.treasuredata.com/display/public/PD/Postback+API
[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]: {% image_buster /assets/img/treasure_data/braze_authentication.png %}
[3]: {% image_buster /assets/img/treasure_data/braze_export_configuration.png %}
[4]: https://www.treasuredata.com/
[5]: https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration
[10]: {% image_buster /assets/img/treasure_data/query_1.png %}
[11]: {% image_buster /assets/img/treasure_data/query_2.png %}
