---
nav_title: Octolis
article_title: Octolis
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Octolis, einer Datenaktivierungsplattform, die es Ihnen erlaubt, Ihre Daten in Braze zu integrieren."
alias: /partners/octolis/
page_type: partner
search_tag: Octolis

---

# Octolis

> [Octolis](http://octolis.com) ist eine leistungsstarke Plattform zur Aktivierung von Daten (oder headless CDP). Octolis basiert auf einer Datenbank, die Sie besitzen, und ist eine einfache Möglichkeit, Daten in Ihren Geschäftsanwendungen zu vereinheitlichen, aufzubereiten, zu bewerten und zu synchronisieren.

_Diese Integration wird von Octolis gepflegt._

## Über die Integration

Die Integration von Braze und Octolis fungiert als Middleware zwischen Ihren Rohdatenquellen und Braze und ermöglicht es Ihnen, Daten aus verschiedenen Quellen, online und offline, abzurufen und zu vereinheitlichen:
1. Vereinheitlichen und kombinieren Sie Daten aus Quellen wie Eshop, CRM, POS-System, etc.
2. Normalisieren und bewerten
3. Realtime-Synchronisation von berechneten Feldern und Ereignissen mit Braze

![]({% image_buster /assets/img/Octolis/Braze_scheme.png %})

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Octolis-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Octolis-Konto. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit [**users.track**]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Braze App Schlüssel | Ihr Bezeichner für die App. Diese finden Sie im **Braze Dashboard > Einstellungen verwalten > API-Schlüssel**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Bevor Sie mit der Integration beginnen, lesen Sie die folgenden Abschnitte über Verbindungen, Quellen, Zielgruppen und Synchronisationen.

Weitere Informationen finden Sie im Abschnitt Octolis [Erste Schritte](https://help.octolis.com/).

### Schritt 1: Verbinden Sie Octolis mit Ihren Datenquellen

Um Daten an Braze zu senden, müssen Sie sicherstellen, dass Sie mindestens eine [Zielgruppe](https://help.octolis.com/audiences/create-a-no-code-audience) erstellt haben. Eine Zielgruppe kombiniert mehrere Datenquellen, wendet sie auf Vorbereitungsschritte an und fügt berechnete Felder hinzu.

Diese Zielgruppen müssen auf der Grundlage mehrerer Datenquellen erstellt werden. Eine Quelle kann einer der folgenden Punkte sein:
- Ein Salesforce-Objekt (Kontakte, Konten usw.)
- Ein Zendesk Objekt (Tickets)
- Eine Datei innerhalb eines SFTP (CSV-Datei mit einigen Kontakten, JSON-Datei mit Ereignissen...)
- Eine Tabelle/Ansicht in einer Datenbank.
- Eines Ihrer Systeme sendet uns Datensätze über Webhooks oder API-Aufrufe.

### Schritt 2: Braze als Reiseziel hinzufügen

Um Braze als neues Ziel festzulegen, wählen Sie im Hauptbildschirm oben auf Ihrem aktuellen Ziel **\+ Weitere hinzufügen** und wählen **Braze** aus den verfügbaren Business-Tools aus.

![]({% image_buster /assets/img/Octolis/Braze_screen2.png %})

Sobald Sie ausgewählt sind, geben Sie Folgendes an:

- Ihr Braze API-Schlüssel: Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.
- Zeitfenster: Octolis wendet das Rate-Limiting für den angegebenen Zeitraum an.
- Volumen der Anfrage: Anzahl der Anfragen, die Sie innerhalb dieses Zeitrahmens stellen können.
- Angepasste Attribute: Geben Sie hier die neuen Felder an, die Sie an Braze senden möchten, ihr Format (String, Ganzzahl, Gleitkommazahl), und markieren Sie das Feld **Erforderlich für Synchronisationen**, wenn Sie möchten, dass eines der Felder für eine Synchronisation Pflichtfeld ist.

![]({% image_buster /assets/img/Octolis/Braze_screen3.png %})

Einmal konfiguriert, erscheint Braze als neues Ziel auf dem Startbildschirm.

### Schritt 3: Eine neue Synchronisierung erstellen

Klicken Sie im Menü auf **Synchronisierungen** und wählen Sie oben rechts **Synchronisierung hinzufügen**. Wählen Sie die Zielgruppe, die Sie auswählen möchten, aus der zuvor erstellten Zielgruppe aus.
Als nächstes wählen Sie **Braze** als Ziel und die Einrichtung aus, an die Sie die Daten senden möchten.

![]({% image_buster /assets/img/Octolis/Braze_screen4.png %})

### Schritt 4: Ausgabeeinstellungen festlegen

Standardmäßig erstellt Braze alle Attribute, die Sie senden würden, aber Sie müssen die Liste der zu synchronisierenden Felder dokumentieren.

![]({% image_buster /assets/img/Octolis/Braze_screen5.png %}){: style="max-width:75%;"}

Hier finden Sie eine spezifische Definition von Einstellungsfeldern.

| Feld | Beschreibung |
| --- | --- |
| Wohin wollen Sie die Zielgruppe synchronisieren? | Die Braze-Einheit, in der Sie Datensätze erstellen oder aktualisieren werden. |
| Welches Feld wird zur Identifizierung eines Datensatzes verwendet? | Das Feld verwendet Octolis, um einen Datensatz zu identifizieren, wenn er bereits in Braze existiert. |
| Wie oft möchten Sie jeden Datensatz senden? | Standardmäßig erfolgt die Synchronisierung für alle Integrationen (API, Datenbank, FTP) inkrementell. Das bedeutet, dass nur neue Werte seit dem letzten Update aktualisiert werden. Bei Bedarf können Sie auch ganze Tabellen in regelmäßigen Abständen versenden. Bei der Initiierung sendet Octolis die vollständige Tabelle. |
| Welche Felder sollen synchronisiert werden? | Abbildung von Octolis auf Braze-Felder. Die Liste aller verfügbaren Felder wird im Dropdown-Menü angezeigt. Um ein berechnetes Feld an Braze zu senden, müssen Sie zunächst sicherstellen, dass Sie die entsprechende Spalte in Ihrer Braze-Entität erstellt haben. |
| Wann wollen Sie die Zielgruppe synchronisieren? | Wie die Daten an Braze gesendet werden sollen: manuell, in Realtime oder programmiert.  |
| Synchronisieren, wenn die Aufnahme... | Erstellen: Für Opt-ins ist es wichtig, dass die Tabelle Braze Master bleibt. Sie möchten nicht, dass Octolis eine Synchronisierung triggert, wenn das Feld aktualisiert wird.<br><br>Update: Andererseits möchten Sie z.B. bei einem Feld für den Vornamen in der Lage sein, das Feld in Ihrer Tabelle Braze jedes Mal zu aktualisieren, wenn ein Kunde Ihnen einen neuen Eingang gibt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Deduplizierung mit mehreren Schlüsseln

Die Deduplizierung ist eine große Herausforderung beim Abgleich von Daten aus verschiedenen Quellen, insbesondere online und offline. Durch das vorgebrachte No-Code-Modul von Octolis können Sie mehrere Schlüssel für die [Deduplizierung](https://help.octolis.com/resources/faq/what-is-deduplication-and-how-does-it-work) verwenden. Dieses Modul ist für jede Stammtabelle verfügbar, d.h. Sie können die Logik an jede Entität anpassen.


