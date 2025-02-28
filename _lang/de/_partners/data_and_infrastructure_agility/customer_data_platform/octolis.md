---
nav_title: Octolis
article_title: Octolis
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Octolis, einer Datenaktivierungsplattform, die es Ihnen ermöglicht, Ihre Daten in Braze zu integrieren."
alias: /partners/octolis/
page_type: partner
search_tag: Octolis

---

# Octolis

> [Octolis][0] ist eine leistungsstarke Datenaktivierungsplattform (oder Headless CDP). Octolis basiert auf einer Datenbank, die Sie besitzen, und bietet eine einfache Möglichkeit, Daten in Ihren Geschäftsanwendungen zu vereinheitlichen, aufzubereiten, zu bewerten und zu synchronisieren.

Die Integration von Braze und Octolis fungiert als Middleware zwischen Ihren Rohdatenquellen und Braze, so dass Sie Daten aus verschiedenen Quellen, online und offline, abrufen und vereinheitlichen können:
1. Vereinheitlichen und kombinieren Sie Daten aus Quellen wie Eshop, CRM, POS-System, usw.
2. Normalisieren und bewerten
3. Echtzeit-Synchronisation von berechneten Feldern und Ereignissen mit Braze

![][7]

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Octolis-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Octolis-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit [**users.track**][1] Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][2]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Braze App Schlüssel | Der Schlüssel zu Ihrer App-Kennung. Diesen finden Sie im **Braze Dashboard > Einstellungen verwalten > API-Schlüssel**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Bevor Sie mit der Integration beginnen, lesen Sie die folgenden Abschnitte über Verbindungen, Quellen, Zielgruppen und Synchronisationen.

Weitere Informationen finden Sie im Abschnitt Octolis [Erste Schritte][4].

### Schritt 1: Verbinden Sie Octolis mit Ihren Datenquellen

Um Daten an Braze zu senden, müssen Sie sicherstellen, dass Sie mindestens eine [Zielgruppe][5] erstellt haben. Eine Zielgruppe kombiniert mehrere Datenquellen, wendet sie auf Vorbereitungsschritte an und fügt berechnete Felder hinzu.

Diese Zielgruppen müssen auf der Grundlage verschiedener Datenquellen erstellt werden. Eine Quelle kann einer der folgenden Punkte sein:
- Ein Salesforce-Objekt (Kontakte, Konten usw.)
- Ein Zendesk-Objekt (Tickets)
- Eine Datei innerhalb eines SFTP (CSV-Datei mit einigen Kontakten, JSON-Datei mit Ereignissen...)
- Eine Tabelle/Ansicht in einer Datenbank.
- Eines Ihrer Systeme sendet uns Datensätze über Webhooks oder API-Aufrufe.

### Schritt 2: Braze als Ziel hinzufügen

Um Braze als neues Ziel einzurichten, klicken Sie auf **\+ Mehr hinzufügen** oben auf Ihrem aktuellen Ziel im Hauptbildschirm und wählen **Braze** aus den verfügbaren Business-Tools aus.

![][9]

Wenn Sie ausgewählt wurden, geben Sie Folgendes an:

- Ihr Braze API-Schlüssel: Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.
- Zeitfenster: Octolis wendet die Tarifbegrenzung in dem angegebenen Zeitraum an.
- Volumen anfordern: Anzahl der Anfragen, die Sie innerhalb dieses Zeitrahmens stellen können.
- Benutzerdefinierte Attribute: Geben Sie hier die neuen Felder an, die Sie an Braze senden möchten, ihr Format (String, Integer, Float) und markieren Sie das Feld **Erforderlich für Synchronisationen**, wenn Sie möchten, dass eines dieser Felder für eine Synchronisation obligatorisch ist.

![][10]

Sobald Sie Braze konfiguriert haben, erscheint es als neues Ziel auf dem Startbildschirm.

### Schritt 3: Eine neue Synchronisierung erstellen

Klicken Sie im Menü auf **Synchronisationen** und wählen Sie oben rechts **Synchronisation hinzufügen**. Wählen Sie die Zielgruppe, die Sie auswählen möchten, aus der zuvor erstellten Zielgruppe aus.
Als nächstes wählen Sie **Braze** als Ziel und die Entität, an die Sie Daten senden möchten.

![][11]

### Schritt 4: Ausgabeeinstellungen festlegen

Braze erstellt standardmäßig alle Attribute, die Sie senden würden, aber Sie müssen die Liste der zu synchronisierenden Felder dokumentieren.

![][12]{: style="max-width:75%;"}

Hier finden Sie eine spezifische Definition von Einstellungsfeldern.

| Feld | Beschreibung |
| --- | --- |
| Wohin wollen Sie das Publikum synchronisieren? | Die Entität von Braze, in der Sie Datensätze erstellen oder aktualisieren werden. |
| Welches Feld wird zur Identifizierung eines Datensatzes verwendet? | Das Feld verwendet Octolis, um einen Datensatz zu identifizieren, wenn er bereits in Braze existiert. |
| Wie oft möchten Sie jeden Datensatz senden? | Standardmäßig erfolgt die Synchronisierung für alle Integrationen (API, Datenbank, FTP) inkrementell. Das bedeutet, dass nur neue Werte seit der letzten Aktualisierung aktualisiert werden. Bei Bedarf können Sie auch ganze Tabellen in regelmäßigen Abständen versenden. Bei der Initiierung sendet Octolis die vollständige Tabelle. |
| Welche Felder sollen synchronisiert werden? | Zuordnung von Octolis zu Braze-Feldern. Die Liste aller verfügbaren Felder wird im Dropdown-Menü angezeigt. Um ein berechnetes Feld an Braze zu senden, müssen Sie zunächst sicherstellen, dass Sie die entsprechende Spalte in Ihrer Braze-Entität erstellt haben. |
| Wann wollen Sie das Publikum synchronisieren? | Wie die Daten an Braze gesendet werden sollen: manuell, in Echtzeit oder programmiert.  |
| Synchronisieren, wenn die Aufnahme... | Erstellen Sie: Für Opt-Ins ist es wichtig, dass die Braze-Tabelle Master bleibt. Sie möchten nicht, dass Octolis eine Synchronisierung auslöst, wenn das Feld aktualisiert wird.<br><br>Update: Andererseits möchten Sie z.B. bei einem Feld für den Vornamen das Feld in Ihrer Tabelle Braze jedes Mal aktualisieren können, wenn ein Kunde Ihnen einen neuen Eintrag gibt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Deduplizierung mit mehreren Schlüsseln

Die Deduplizierung ist eine große Herausforderung beim Abgleich von Daten aus verschiedenen Quellen, insbesondere online und offline. Mit dem fortschrittlichen no-code Modul von Octolis können Sie mehrere Schlüssel für die [Deduplizierung][3] verwenden. Dieses Modul ist für jede Stammtabelle verfügbar, d.h. Sie können die Logik an jede Entität anpassen.

[0]: http://octolis.com
[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://help.octolis.com/resources/faq/what-is-deduplication-and-how-does-it-work
[4]: https://help.octolis.com/
[5]: https://help.octolis.com/audiences/create-a-no-code-audience
[6]: {{site.baseurl}}/api/api_limits/
[7]: {% image_buster /assets/img/Octolis/Braze_scheme.png %}
[8]: {% image_buster /assets/img/Octolis/Braze_screen1.png %}
[9]: {% image_buster /assets/img/Octolis/Braze_screen2.png %}
[10]: {% image_buster /assets/img/Octolis/Braze_screen3.png %}
[11]: {% image_buster /assets/img/Octolis/Braze_screen4.png %}
[12]: {% image_buster /assets/img/Octolis/Braze_screen5.png %}
