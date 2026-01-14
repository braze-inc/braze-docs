---
nav_title: Outgrow
article_title: Outgrow
alias: /partners/outgrow/
description: "Dieser Artikel enthält eine umfassende Anleitung zur Konfiguration einer nativen Integration zwischen Outgrow und Braze für eine verbesserte Synchronisierung von Nutzerdaten und personalisierte Kampagnen."
page_type: partner
search_tag: Partner
---

# Outgrow

> [Outgrow](https://outgrow.co/) ist eine Plattform für interaktive Inhalte, mit der Sie Quiz, Rechner, Umfragen und andere Arten von ansprechenden Inhalten erstellen können, um Nutzerdaten und Insights zu sammeln. Mit der Integration von Braze und Outgrow können Sie Nutzerdaten aus Outgrow automatisch in Braze übertragen und so hochgradig personalisierte und zielgerichtete Kampagnen ermöglichen.

Wenn Sie die Integration von Braze und Outgrow für interaktive Inhalte nutzen, profitieren Sie unter anderem von folgenden Vorteilen:

- **Verbesserte Personalisierung**: Erfassen Sie Daten aus Outgrow-Quizzes, Umfragen und Rechnern, die an angepasste Attribute in Braze angepasst werden können. Diese Daten sind für eine präzise Segmentierung und personalisierte Kampagnen zulässig.
- **Echtzeitdaten synchronisieren**: Sie erhalten Outgrow-Daten in Braze in Realtime, was es Ihnen erlaubt, sofort auf Nutzer:innen-Insights zu reagieren. Dies erlaubt zeitnahe Nachfassaktionen oder personalisierte Nachrichten, die auf den letzten Interaktionen der Nutzer:innen basieren.
- **Rationalisierte Datenverwaltung**: Automatisieren Sie den Datentransfer zwischen Outgrow und Braze. So vermeiden Sie manuelle Datenexporte und -importe, reduzieren Datenabweichungen und sparen Zeit.
- **Verbesserte Nutzererfahrung**: Nutzen Sie Insights der Nutzer:innen, um relevantere Erlebnisse zu schaffen, die zu höherer Zufriedenheit, Bindung und Lifetime-Value führen.
- **Flexibles Targeting und Segmentierung**: Verfeinern Sie die Segmentierung in Braze mit Hilfe von Outgrow-Daten, die es Ihnen erlauben, Nutzer:innen auf der Grundlage bestimmter Interaktionen (z.B. Quiz-Ergebnisse oder Antworten auf Umfragen) anzusprechen, um Kampagnen zu erstellen, die bei Ihren Nutzer:innen auf Resonanz stoßen.

## Voraussetzungen

Bevor Sie die Integration von Outgrow und Braze einrichten, vergewissern Sie sich, dass Sie über die folgenden Informationen verfügen:

| Anforderung | Beschreibung |
|-------------|-------------|
| **Konto auswachsen lassen** | Ein registriertes Outgrow-Konto zur Konfiguration und Verwaltung der Einstellungen für interaktive Inhalte und Datenübertragungen |
| **Braze-Konto** | Ein Braze-Konto mit Zugriff auf REST API-Zugangsdaten |
| **API-Schlüssel** | Ein API-Schlüssel von Braze mit der Berechtigung `users.track`, um die Übertragung von Nutzer:innen-Daten zu ermöglichen |
| **Angepasste Attribute in Braze** | Angepasste Attribute, die in Braze eingerichtet wurden, um Outgrow-Antworten zu erfassen (z.B. Quiz-Ergebnisse, Segmente und andere) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Folgen Sie diesen Schritten, um die Integration von Braze und Outgrow zu konfigurieren:

### Schritt 1: Generieren Sie Braze API-Schlüssel

1. Gehen Sie in Ihrem Braze-Konto zu **Entwickler-Konsole** > **API-Einstellungen**.
2. Wählen Sie **Neuen API-Schlüssel erstellen**.
3. Benennen Sie Ihren API-Schlüssel, schalten Sie die Berechtigung `users.track` ein und speichern Sie den API-Schlüssel.

### Schritt 2: Konfigurieren Sie die Integration von Braze in Outgrow

1. Melden Sie sich bei Ihrem Outgrow-Konto an.
2. Gehen Sie auf dem Dashboard zu **Integrationen**.
3. Wählen Sie aus der Liste der verfügbaren Integrationen **Braze** aus.
4. Geben Sie Ihren **Braze API-Schlüssel** und die **URL des REST-API-Endpunkts** ein:
   - **API-Schlüssel**: Geben Sie den API-Schlüssel ein, der in Braze generiert wurde
   - **REST Endpunkt URL**: Geben Sie den Endpunkt für Ihre Braze-Instanz ein (z.B. `https://rest.iad-01.braze.com`)
5. Wählen Sie **Speichern**, um die Integration zu aktivieren.

### Schritt 3: Abbildung von Outgrow-Daten auf Braze-Attribute

In Outgrow können Sie Antworten aus interaktiven Inhalten (wie Quiz-Ergebnisse, benutzerdefinierte Segmente oder Engagement-Scores) den angepassten Attributen von Braze zuordnen.

1. In den Outgrow **Integration Settings** für Braze legen Sie fest, welche Outgrow-Antworten den Attributen von Braze zugeordnet werden sollen.
2. Stellen Sie sicher, dass jede ausgewählte Antwort mit einem angepassten Attribut in Braze übereinstimmt. Zum Beispiel:
   - Die Abbildungen der Quiz-Punkte finden Sie unter `outgrow_quiz_score`.
   - Angepasste Segmente Abbildungen auf `outgrow_custom_segment`.
3. Speichern Sie Ihre Einstellungen für die Abbildung.

### Schritt 4: Testen Sie die Integration

Nachdem Sie die Integration konfiguriert haben, führen Sie einen Test durch, um zu überprüfen, ob die Daten ordnungsgemäß von Outgrow zu Braze übertragen werden.

1. Veröffentlichen Sie ein Outgrow-Erlebnis (z.B. ein Quiz oder einen Taschenrechner) und schließen Sie es als Testnutzer:in ab.
2. Gehen Sie in Ihrem Braze-Konto zum Abschnitt **Benutzerprofil** und prüfen Sie, ob die Attribute aktualisiert wurden (z. B. `outgrow_quiz_score` oder `outgrow_custom_segment`).
3. Überprüfen Sie, ob die Daten unter den entsprechenden angepassten Attributen korrekt ausgefüllt sind.

## Verwendung von Outgrow-Daten in Braze für Segmentierung und Targeting

### Erstellen von Segmenten in Braze mit Outgrow-Daten

Mit der Integration können Sie Braze Segmente erstellen, die auf angepassten Attributen basieren, die aus Outgrow-Antworten zusammengestellt werden.

1. Gehen Sie in Braze zu **Engagement** > **Segmente** und wählen Sie **Neues Segment erstellen**.
2. Benennen Sie Ihr Segment und setzen Sie Filter auf der Grundlage von Outgrow-Daten. Zum Beispiel:
   - Filtern Sie nach `outgrow_quiz_score`, um Nutzer:innen mit einer Punktzahl über einem bestimmten Schwellenwert zusammenzustellen.
   - Filtern Sie nach `outgrow_custom_segment`, um Nutzer:innen, die zu einem bestimmten von Outgrow definierten Segment gehören, zu targetieren.
3. Speichern Sie Ihre Segmente zur Verwendung in Kampagnen und Canvase.

### Kampagnen mit von Outgrow definierten Segmenten einführen

Mit den angepassten Segmenten, die aus Outgrow-Daten erstellt wurden, können Sie Ihre Kampagnen für Braze personalisieren und Nutzer:in auf der Grundlage ihrer Reaktionen auf interaktive Inhalte ansprechen. Um dies zu tun und ein personalisiertes Nutzer:innen-Erlebnis zu schaffen, folgen Sie diesen Schritten:

1. Gehen Sie in Braze zu **Engagement** > **Kampagnen**.
2. Wählen Sie **Kampagne erstellen** und wählen Sie die Art Ihrer Kampagne (E-Mail, Push, In-App-Nachricht oder andere).
3. Im Schritt Targeting wählen Sie das Segment aus, das aus den Attributen von Outgrow zusammengestellt wurde (z. B. Nutzer:innen mit bestimmten Quizwerten oder Segmenten).
4. Passen Sie den Inhalt und die Einstellungen Ihrer Kampagne an, und starten Sie sie dann.

## Fehlerbehebung bei allgemeinen Problemen

| Fehler | Lösung |
|-------|----------|
| **Die Daten werden nicht auf Braze übertragen** | Überprüfen Sie, ob der API-Schlüssel und die Endpunkt-URL in Ihren Outgrow-Integrationseinstellungen korrekt sind. Stellen Sie sicher, dass für den API-Schlüssel die Berechtigung `users.track` aktiviert ist. |
| **Falsche Abbildung der Daten** | Stellen Sie sicher, dass jede angepasste Outgrow-Antwort einem gültigen angepassten Attribut von Braze entspricht und dass die Attributnamen genau übereinstimmen. |
| **Segmente werden nicht richtig gefiltert** | Stellen Sie sicher, dass angepasste Attribute in Braze richtig eingerichtet sind und Daten empfangen. Überprüfen Sie noch einmal die Logik Ihrer Segmente-Filter. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Zusätzliche Überlegungen

- **Datenschutz**: Halten Sie sich bei der Übertragung von Nutzerdaten zwischen Plattformen an die Datenschutzbestimmungen (z.B. DSGVO und CCPA).
- **Rate-Limits**: Outgrow-Daten werden in Realtime an Braze gesendet, aber für große Datenmengen können Rate-Limits der Braze API gelten. Planen Sie entsprechend für hochfrequentierte Erlebnisse.
- **Angepasste Attribute konfigurieren**: Überprüfen Sie, ob die angepassten Attribute von Braze, die in dieser Integration verwendet werden, korrekt konfiguriert sind, um die von Outgrow gesendeten Daten zu erfassen.

Weitere Hilfe finden Sie in der [Dokumentation von Outgrow](https://support.outgrow.co/docs/configuring-native-integration-between-outgrow-braze) oder beim Outgrow-Support.