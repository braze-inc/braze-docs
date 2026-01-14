---
nav_title: ActionIQ
article_title: ActionIQ
description: "Dieser referenzierte Artikel behandelt die Integration von Braze und ActionIQ. ActionIQ ist eine unternehmensweite Customer Data Platform (CDP) für Marketer, Analysten und Technologen. Diese Integration erlaubt es Marken, ihre ActionIQ Daten direkt mit Braze zu synchronisieren und abzubilden."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

> [ActionIQ](https://www.actioniq.com/) ist eine Customer Data Platform für Unternehmensmarken, die Marketern einfache und sichere Möglichkeiten bietet, Daten überall im Kundenerlebnis zu aktivieren. Dank der eindeutigen, zusammensetzbaren Architektur von ActionIQ können die Daten sicher dort bleiben, wo sie sind, und die Marketing Teams verwenden nur die Tools, die sie benötigen.

_Diese Integration wird von ActionIQ gepflegt._

## Über die Integration

Die Integration von Braze und ActionIQ ermöglicht es Marken, ihre ActionIQ-Daten direkt mit Braze zu synchronisieren und abzubilden und so die Zustellung von außergewöhnlichen Kundenerlebnissen auf der Grundlage der gesamten Bandbreite ihrer Kundendaten zu ermöglichen. Die verfügbaren Integrationen ermöglichen es Nutzer:innen:

- Aktualisieren Sie Nutzerprofile in Braze mit Informationen zur Mitgliedschaft in der Zielgruppe und allen Attributen direkt aus ActionIQ
- Leiten Sie die von ActionIQ getrackten Ereignisse in Realtime an Braze weiter, um personalisierte und gezielte Kampagnen zu triggern.
- Stellen Sie API-getriggerte Kampagnen in Braze direkt von Touchpoints in einer ActionIQ-Journey zu.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| ActionIQ-Konto | Um die Vorteile dieser Integration zu nutzen, benötigen Sie ein ActionIQ-Konto. |
| Braze REST API-Schlüssel | Ein REST API-Schlüssel von Braze mit den erforderlichen Berechtigungen für die jeweilige Integration. Weitere Einzelheiten finden Sie im Abschnitt "Anforderungen". <br><br>Dieser Schlüssel kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integrationen

### Mitgliedschaft der Zielgruppe

Diese Integration dient dazu, die Mitgliedschaft in einer Zielgruppe von ActionIQ mit Braze zu synchronisieren, indem angepasste Attribute erstellt werden, die angeben, ob ein Profil von Braze Teil eines Segments ist. Jede ActionIQ-Zielgruppe entspricht einem eindeutigen booleschen angepassten Attribut.

Die Standard-Namenskonvention für das angepasste Attribut lautet: `AIQ_<Audience ID>_<Split ID>`.

Um ein Segment für diese Nutzer:innen zu erstellen, gehen Sie wie folgt vor:
1. Navigieren Sie in Braze zu **Segmente**.
2. Erstellen Sie ein neues Segment.
3. Wählen Sie **Angepasste Attribute** als Filter aus.
4. Wählen Sie hier das angepasste Attribut von ActionIQ aus. 
5. Nachdem das Segment erstellt wurde, können Sie es als Zielgruppen-Filter auswählen, wenn Sie eine Kampagne oder ein Canvas erstellen.

Darüber hinaus aktualisiert diese Integration jedes angepasste oder Standard Attribut in einem Braze Nutzerprofil mit den ActionIQ Attributwerten.

#### Anforderungen

Sie benötigen einen Braze REST API-Schlüssel mit den Berechtigungen `users.track` und `user.export.ids`. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. 

Richten Sie in ActionIQ eine Braze-Verbindung ein, indem Sie Ihren REST API-Schlüssel und den Braze REST-Endpunkt angeben. 

Um Verbraucher:in auf der Braze-Plattform zu finden, müssen die folgenden Bezeichner in Ihrer Aktivierungseinstellung enthalten sein:
- `braze_id`
- `external_id`

### Events

Sie können die ActionIQ-Plattform so konfigurieren, dass sie Ereignisinformationen über ihren Streaming-Ingest-Dienst empfängt. Diese Integrationsoption leitet diese Ereignisse an Braze weiter, damit Marketer sie zur Orchestrierung oder zum Triggern von Kampagnen nutzen können. Die Event Integration kann zusätzliche ActionIQ Attribute als Teil der Eigenschaften in der Event-Nutzlast senden.

#### Anforderungen

Sie benötigen einen Braze REST API-Schlüssel mit den Berechtigungen `users.track` und `user.export.ids`. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. 

Die Integration der Ereignisse sendet die folgenden Informationen an Braze:
- Event-Name
- Bezeichner des Verbrauchers:in (entweder `braze_id` oder `external_id`)
- Zeitstempel
- Event-Eigenschaften, die durch zusätzliche Attribute in der Exporteinstellung aufgefüllt werden

### Ausgelöste Kampagnen

Diese Integration triggert eine Kampagne in Braze für alle Nutzer:innen in einem Segment von ActionIQ. Nachdem Sie den Text Ihrer Kampagne, die multivariaten Tests und die Regeln für die Wiederzulassung konfiguriert haben, können Sie sie von jedem ActionIQ Journey Touchpoint aus triggern, indem Sie die ID der Kampagne von Braze zu Ihrer Exporteinstellung hinzufügen.

Optional können Sie auch andere ActionIQ Attribute in Ihren Export einbeziehen, um Ihre Kampagne zu füllen. Diese werden mit dem Objekt `trigger_properties` gesendet.

#### Anforderungen

Sie benötigen einen Braze REST API-Schlüssel mit den Berechtigungen `campaigns.trigger.send` und `campaigns.list`. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.

Die folgenden Werte müssen in Ihrem ActionIQ-Export an Braze gesendet werden:
- Bezeichner des Verbrauchers:in (entweder `braze_id` oder `external_id`)
- Kampagnen-ID


