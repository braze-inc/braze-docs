---
nav_title: ActionIQ
article_title: ActionIQ
description: "Dieser Referenzartikel behandelt die Integration von Braze und ActionIQ. ActionIQ ist eine unternehmensweite Kundendatenplattform für Vermarkter, Analysten und Technologen. Diese Integration ermöglicht es Marken, ihre ActionIQ-Daten direkt mit Braze zu synchronisieren und zuzuordnen."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

> [ActionIQ][2] bringt Ordnung in das Chaos der Kundenerfahrung. Der ActionIQ Customer Experience (CX) Hub bietet allen Teams direkten, aber kontrollierten Self-Service-Zugang zu Kundendaten, um Zielgruppen zu entdecken und Erlebnisse in großem Umfang zu orchestrieren.

Die Integration von Braze und ActionIQ ermöglicht es Marken, ihre ActionIQ-Daten direkt mit Braze zu synchronisieren und abzubilden. So können sie außergewöhnliche Kundenerlebnisse auf der Grundlage der gesamten Bandbreite ihrer Kundendaten bieten. Die Integration ermöglicht es den Benutzern,:
- Übertragen Sie Zielgruppensegmente oder benutzerdefinierte Attribute direkt von ActionIQ auf Braze
- Leiten Sie die von ActionIQ verfolgten Ereignisse in Echtzeit an Braze weiter, um personalisierte und gezielte Kampagnen auszulösen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| ActionIQ-Konto | Um die Vorteile dieser Integration zu nutzen, benötigen Sie ein ActionIQ-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track` und `user.export.ids`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Zugehörigkeit zum Publikum

Diese Integration wird verwendet, um die ActionIQ-Zielgruppenmitgliedschaft mit Braze zu synchronisieren, indem benutzerdefinierte Attribute erstellt werden, die angeben, ob ein Braze-Profil zu einem Segment gehört. Jede ActionIQ-Zielgruppe entspricht einem eindeutigen booleschen benutzerdefinierten Attribut.

Die Standardbenennungskonvention für das erstellte benutzerdefinierte Attribut lautet: `AIQ_<Audience ID>_<Split ID>`.

Um ein Segment dieser Benutzer zu erstellen, navigieren Sie in Braze zu **Segmente**, erstellen ein neues Segment und wählen **Benutzerdefinierte Attribute** als Filter. Von hier aus können Sie das benutzerdefinierte ActionIQ-Attribut auswählen. Nachdem das Segment erstellt wurde, können Sie es bei der Erstellung einer Kampagne oder eines Canvas als Zielgruppenfilter auswählen.

#### Anforderungen

Richten Sie in ActionIQ eine Braze-Verbindung ein, indem Sie Ihren REST-API-Schlüssel und den REST-Endpunkt von Braze angeben. 

Um mit den Verbrauchern auf der Braze-Plattform übereinzustimmen, müssen die folgenden Identifikatoren in Ihrer Aktivierungseinstellung enthalten sein:
- `braze_id`
- `external_id`

Sobald Ihre Integration verbunden ist, werden die Informationen an Braze gesendet.

### Events

Die ActionIQ-Plattform kann so konfiguriert werden, dass sie Ereignisinformationen über ihren Streaming-Ingest-Service empfängt. Diese andere Integrationsoption leitet diese Ereignisse an Braze weiter, damit Marketingspezialisten sie für die Orchestrierung oder das Auslösen von Marketingkampagnen nutzen können.

Die Ereignisintegration ist in der Lage, zusätzliche ActionIQ-Attribute als Teil der Eigenschaften innerhalb der Ereignis-Nutzdaten zu senden.

#### Anforderungen

Die Ereignisintegration sendet die folgenden Informationen an Braze:
- Event-Name
- Kennung des Verbrauchers (entweder `braze_id` oder `external_id`)
- Zeitstempel
- Ereigniseigenschaften, die durch zusätzliche Attribute in der Exporteinstellung aufgefüllt werden


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.actioniq.com/