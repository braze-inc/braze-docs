---
nav_title: Wachsen Sie über sich hinaus
article_title: Wachsen Sie über sich hinaus
alias: /partners/outgrow/
description: "Dieser Artikel enthält eine umfassende Anleitung zur Konfiguration einer nativen Integration zwischen Outgrow und Braze für eine verbesserte Synchronisierung von Benutzerdaten und personalisierte Kampagnen."
page_type: partner
search_tag: Partner
---

# Wachsen Sie über sich hinaus

> [Outgrow](https://outgrow.co/) ist eine Plattform für interaktive Inhalte, mit der Sie Quiz, Rechner, Umfragen und andere Arten von ansprechenden Inhalten erstellen können, um Nutzerdaten und Erkenntnisse zu sammeln. Mit der Integration von Braze und Outgrow können Sie automatisch Benutzerdaten aus Outgrow in Braze übertragen, was hochgradig personalisierte und zielgerichtete Kampagnen ermöglicht.

Wenn Sie die Braze- und Outgrow-Integration für interaktive Inhalte nutzen, haben Sie unter anderem folgende Vorteile:

- **Bessere Personalisierung**: Sammeln Sie Daten aus Outgrow-Quizzes, Umfragen und Rechnern, die in Braze benutzerdefinierten Attributen zugeordnet werden können. Diese Daten ermöglichen eine präzise Segmentierung und personalisierte Kampagnen.
- **Datenabgleich in Echtzeit**: Empfangen Sie Outgrow-Daten in Braze in Echtzeit, so dass Sie sofort auf die Erkenntnisse der Benutzer reagieren können. Dies ermöglicht rechtzeitige Nachfassaktionen oder personalisierte Nachrichten, die auf den letzten Interaktionen der Nutzer basieren.
- **Rationalisierte Datenverwaltung**: Automatisieren Sie den Datentransfer zwischen Outgrow und Braze, um manuelle Datenexporte und -importe zu vermeiden, Datenabweichungen zu reduzieren und Zeit zu sparen.
- **Verbesserte Benutzerfreundlichkeit**: Nutzen Sie die Erkenntnisse der Benutzer, um relevantere Erlebnisse zu schaffen, die zu höherer Zufriedenheit, Bindung und Lebenszeitwert führen.
- **Flexible Zielgruppenansprache und Segmentierung**: Verfeinern Sie die Segmentierung in Braze mit Hilfe von Outgrow-Daten. So können Sie Benutzer auf der Grundlage bestimmter Interaktionen (z. B. Quizergebnisse oder Umfrageantworten) gezielt ansprechen, um Kampagnen zu erstellen, die bei Ihren Benutzern Anklang finden.

## Voraussetzungen

Bevor Sie die Outgrow- und Braze-Integration einrichten, sollten Sie sich vergewissern, dass Sie die folgenden Voraussetzungen erfüllen:

| Anforderung | Beschreibung |
|-------------|-------------|
| **Konto auswachsen lassen** | Ein registriertes Outgrow-Konto zur Konfiguration und Verwaltung von interaktiven Inhalten und Datenübertragungseinstellungen |
| **Braze Konto** | Ein Braze-Konto mit Zugriff auf REST-API-Zugangsdaten |
| **API-Schlüssel** | Ein API-Schlüssel von Braze mit der Berechtigung `users.track`, um die Übertragung von Benutzerdaten zu ermöglichen |
| **Benutzerdefinierte Attribute in Braze** | Benutzerdefinierte Attribute, die in Braze eingerichtet wurden, um Outgrow-Antworten zu erfassen (z. B. Quiz-Ergebnisse, Segmente und andere) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Folgen Sie diesen Schritten, um die Integration von Braze und Outgrow zu konfigurieren:

### Schritt 1: Braze API-Schlüssel generieren

1. Gehen Sie in Ihrem Braze-Konto zu **Entwicklerkonsole** > **API-Einstellungen**.
2. Wählen Sie **Neuen API-Schlüssel erstellen**.
3. Benennen Sie Ihren API-Schlüssel, aktivieren Sie die Berechtigung `users.track` und speichern Sie den API-Schlüssel.

### Schritt 2: Konfigurieren Sie die Braze-Integration in Outgrow

1. Melden Sie sich bei Ihrem Outgrow-Konto an.
2. Gehen Sie im Dashboard auf **Integrationen**.
3. Wählen Sie aus der Liste der verfügbaren Integrationen **Braze** aus.
4. Geben Sie Ihren **Braze-API-Schlüssel** und die **URL des REST-API-Endpunkts** ein:
   - **API-Schlüssel**: Geben Sie den API-Schlüssel ein, der in Braze generiert wurde.
   - **REST Endpunkt URL**: Geben Sie den Endpunkt für Ihre Braze-Instanz ein (zum Beispiel `https://rest.iad-01.braze.com`)
5. Wählen Sie **Speichern**, um die Integration zu aktivieren.

### Schritt 3: Zuordnung von Outgrow-Daten zu Braze-Attributen

In Outgrow können Sie Antworten aus interaktiven Inhalten (z.B. Quiz-Ergebnisse, benutzerdefinierte Segmente oder Engagement-Scores) den benutzerdefinierten Attributen von Braze zuordnen.

1. In den **Outgrow-Integrationseinstellungen** für Braze legen Sie fest, welche Outgrow-Antworten den Braze-Attributen zugeordnet werden sollen.
2. Stellen Sie sicher, dass jede ausgewählte Antwort mit einem benutzerdefinierten Attribut in Braze übereinstimmt. Zum Beispiel:
   - Die Quiz-Punktzahl wird auf `outgrow_quiz_score` abgebildet.
   - Benutzerdefinierte Segmentkarten auf `outgrow_custom_segment`.
3. Speichern Sie Ihre Mapping-Einstellungen.

### Schritt 4: Testen Sie die Integration

Nachdem Sie die Integration konfiguriert haben, führen Sie einen Test durch, um zu überprüfen, ob die Daten ordnungsgemäß von Outgrow zu Braze übertragen werden.

1. Veröffentlichen Sie ein Outgrow-Erlebnis (z. B. ein Quiz oder einen Taschenrechner) und schließen Sie es als Testbenutzer ab.
2. Gehen Sie in Ihrem Braze-Konto zum Abschnitt **Benutzerprofil** und prüfen Sie, ob die Attribute aktualisiert wurden (z. B. `outgrow_quiz_score` oder `outgrow_custom_segment`).
3. Überprüfen Sie, ob die Daten unter den entsprechenden benutzerdefinierten Attributen korrekt ausgefüllt sind.

## Verwendung von Outgrow-Daten in Braze für Segmentierung und Targeting

### Erstellen von Segmenten in Braze mit Outgrow-Daten

Mit der Integration können Sie Braze-Segmente erstellen, die auf benutzerdefinierten Attributen basieren, die aus Outgrow-Antworten ausgefüllt werden.

1. Gehen Sie in Braze zu **Engagement** > **Segmente** und wählen Sie **Neues Segment erstellen**.
2. Benennen Sie Ihr Segment und setzen Sie Filter auf Basis der Outgrow-Daten. Zum Beispiel:
   - Filtern Sie nach `outgrow_quiz_score`, um Nutzer anzusprechen, die einen bestimmten Schwellenwert überschritten haben.
   - Filtern Sie nach `outgrow_custom_segment`, um Benutzer anzusprechen, die zu einem bestimmten von Outgrow definierten Segment gehören.
3. Speichern Sie Ihr Segment zur Verwendung in Kampagnen und Canvases.

### Starten von Kampagnen mit von Outgrow definierten Segmenten

Sie können die aus Outgrow-Daten erstellten benutzerdefinierten Segmente verwenden, um Ihre Braze-Kampagnen zu personalisieren und Benutzer auf der Grundlage ihrer Reaktionen auf interaktive Inhalte anzusprechen. Führen Sie dazu die folgenden Schritte aus, um ein personalisiertes Benutzererlebnis zu schaffen:

1. Gehen Sie in Braze zu **Engagement** > **Kampagnen**.
2. Wählen Sie **Kampagne erstellen** und wählen Sie Ihren Kampagnentyp (E-Mail, Push, In-App-Nachricht oder andere).
3. Wählen Sie im Schritt Zielgruppenansprache das Segment aus, das mit den Outgrow-Attributen erstellt wurde (z. B. Nutzer mit bestimmten Quiz-Ergebnissen oder Segmenten).
4. Passen Sie den Inhalt und die Einstellungen Ihrer Kampagne an, und starten Sie sie dann.

## Fehlersuche bei allgemeinen Problemen

| Ausgabe | Lösung |
|-------|----------|
| **Die Daten werden nicht auf Braze übertragen** | Überprüfen Sie, ob der API-Schlüssel und die Endpunkt-URL in Ihren Outgrow-Integrationseinstellungen korrekt sind. Vergewissern Sie sich, dass für den API-Schlüssel die Berechtigung `users.track` aktiviert ist. |
| **Falsche Datenzuordnung** | Stellen Sie sicher, dass jede zugeordnete Outgrow-Antwort einem gültigen benutzerdefinierten Braze-Attribut entspricht und dass die Attributnamen genau übereinstimmen. |
| **Segment wird nicht korrekt gefiltert** | Stellen Sie sicher, dass die benutzerdefinierten Attribute in Braze richtig eingerichtet sind und Daten empfangen. Überprüfen Sie noch einmal Ihre Segmentfilterlogik. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Zusätzliche Überlegungen

- **Datenschutz**: Halten Sie die Datenschutzbestimmungen (wie GDPR und CCPA) ein, wenn Sie Benutzerdaten zwischen Plattformen übertragen.
- **Preisgrenzen**: Outgrow-Daten werden in Echtzeit an Braze gesendet. Bei großen Datenmengen können jedoch Ratenbeschränkungen für die Braze API gelten. Planen Sie entsprechend für stark frequentierte Erlebnisse.
- **Benutzerdefinierte Attributkonfiguration**: Stellen Sie sicher, dass die benutzerdefinierten Braze-Attribute, die in dieser Integration verwendet werden, korrekt konfiguriert sind, um die von Outgrow gesendeten Daten zu erfassen.

Weitere Hilfe erhalten Sie in der [Outgrow-Dokumentation](https://support.outgrow.co/docs/configuring-native-integration-between-outgrow-braze) oder vom Outgrow-Support.