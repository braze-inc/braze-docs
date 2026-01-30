---
nav_title: Gesehen
article_title: Gesehen
description: "Seen ermöglicht personalisierte Video-Erlebnisse in großem Umfang und hilft Marken, das Engagement entlang der Customer Journey zu steigern."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# Gesehen

> [Seen](https://seen.io) ermöglicht es Marken, personalisierte Video-Erlebnisse in großem Umfang zu erstellen und zuzustellen. Mit Seen können Sie ein Video rund um Ihre Daten entwerfen, es in großem Umfang in der Cloud personalisieren und dann dort verteilen, wo es am besten funktioniert.
>
> Die Integration von Braze und Seen ermöglicht es Ihnen, Nutzerdaten von Braze an Seen zu senden, dynamisch personalisierte Videos zu generieren und Video-Assets, wie z.B. eine eindeutige Player-URL und eine Miniaturansicht, zur Verwendung in Kampagnen und Canvase an Braze zurückzugeben.


## Anwendungsfälle

Seen unterstützt die automatisierte, personalisierte Zustellung von Videos über den gesamten Kundenlebenszyklus, einschließlich:

- **Onboarding**: Begrüßen Sie neue Nutzer:innen mit Videos, die auf ihr Profil oder ihren Anmeldekontext personalisiert sind.
- **Konversion und Aktivierung**: Verstärken Sie wichtige Aktionen mit kontextuellem Video Messaging
- **Loyalität und Upselling**: Personalisierte Angebote oder Meilensteine der Nutzung hervorheben
- **Rückgewinnung und Abwandern verhindern**: Erneute Interaktion inaktiver Nutzer:innen mit maßgeschneiderten Video-Inhalten


## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
|--------------|-------------|
| Gesehen Plattform Zugang | Sie benötigen ein Abo der Seen Plattform oder eine aktive Seen Kampagne. Sie benötigen Zugriff auf Ihre Workspace-Einstellungen, um Ihre Workspace ID abzurufen und ein API-Token zu generieren. |
| Braze-Daten-Transformation Webhook URL | Braze Data Transformation formatiert die von Seen eingehenden Daten so um, dass sie vom /users/track Endpunkt von Braze akzeptiert werden können. |
| Braze Nutzer:innen-Daten | Für die Personalisierung von Videos sind Daten auf Nutzer:innen-Ebene erforderlich. Stellen Sie sicher, dass die relevanten Attribute in Braze verfügbar sind und dass Sie **braze_id** als eindeutigen Bezeichner angeben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}




## Wie Seen Journeys funktionieren

Seen verwendet [Journeys](https://docs.seen.io/journey), um zu steuern, wie eingehende Daten verarbeitet werden und wie Videoausgaben erzeugt werden.

Eine Journey ist ein konfigurierbarer Arbeitsablauf, der:
- Empfängt Daten von externen Systemen (z.B. Braze)
- Wendet Logik und Personalisierungsregeln an
- Erzeugt ein Video und zugehörige Assets
- Gibt eine konfigurierbare Antwort-Nutzlast zurück

Fahrten bestehen aus **Knotenpunkten**, die jeweils eine bestimmte Funktion haben:

- **Triggern Sie den Knoten**: Legt fest, wie und wann eine Journey startet (für Braze-Integrationen verwenden Sie einen `On Create` Trigger)
- **Bedingter Knoten**: Leitet Nutzer:innen auf der Grundlage von Datenwerten durch verschiedene logische Pfade
- **Projekt-Knotenpunkt**: Dynamische Personalisierung von Videos anhand der eingehenden Daten
- **Spieler-Knoten**: Erzeugt eine eindeutige Video-Player-URL
- **Webhook-Knoten**: Definiert die an Braze zurückgesendete Antwort-Nutzlast

Da Journey-Antworten konfigurierbar sind, stellen Sie sicher, dass die von Seen zurückgegebenen Ausgabefelder den von Ihrer Braze Data Transformation erwarteten Attributen entsprechen.


## Rate-Limit
Die Seen API akzeptiert bis zu 100 Anrufe alle 10 Sekunden.


## Integration

In diesem Beispiel sendet Braze Nutzerdaten an Seen, um ein personalisiertes Video zu erstellen. Seen liefert dann eine eindeutige Video-Player-URL und eine Miniatur-URL, die als angepasste Attribute in Braze zur Verwendung im Messaging gespeichert werden.

Wenn Sie mehrere Videokampagnen mit Seen haben, wiederholen Sie den Vorgang, um Braze mit allen Videokampagnen zu verbinden.

### Schritt 1: Erstellen Sie eine Webhook-Kampagne, um Daten an Seen zu senden

Erstellen Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks) in Braze.

Konfigurieren Sie den Webhook wie folgt:

- **Webhook URL**:  
  `https://next.seen.io/v1/workspaces/{WORKSPACE_ID}/data`  
  Suchen Sie Ihre Workspace ID in den Einstellungen der Seen Plattform.

- **HTTP-Methode**: POST
- **Körper der Anfrage**: Rohtext  
  Verwenden Sie das folgende Beispiel als Ausgangspunkt. Weitere Informationen finden Sie in [der Dokumentation von Seen zur Erstellung von Daten](https://docs.seen.io/create-data).

{% raw %}
```json
{
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "id": "{{${braze_id}}}"
}
```
{% endraw %}
- **Anfrage-Header**:
  - `Authorization`: Bearer `{Seen_API_TOKEN}`
  - `Content-Type`: `application/json`

  > Generieren Sie ein [API Token](https://docs.seen.io/authorization) in der Seen Plattform unter Workspace-Einstellungen. Sie können sich an Ihren Seen Customer Success Manager:in wenden, um Hilfe zu erhalten.

- Um den Webhook mit einem Nutzer:innen zu testen, wechseln Sie auf den Tab **Test**.
- Nachdem Sie bestätigt haben, dass der Test wie vorgesehen funktioniert, schließen Sie die Einrichtung des Webhooks ab.


### Schritt 2: Konfigurieren Sie eine Reise in der Seen Plattform

Seen verwendet [Journeys](https://docs.seen.io/journey), um festzulegen, wie die eingehenden Daten verarbeitet, personalisiert und an Braze zurückgegeben werden.  
Jede Journey ist ein konfigurierbarer Arbeitsablauf, der aus Knoten besteht, mit denen Sie sowohl die Logik der Videogenerierung als auch die Nutzlast der Antwort steuern können.

So konfigurieren Sie Ihre Journey:

1. Erstellen Sie eine neue Reise in der Seen Plattform
2. Fügen Sie einen **Trigger-Knoten** hinzu und wählen Sie den Trigger `On Create`   
   Dadurch wird sichergestellt, dass die Journey beginnt, wenn Braze Daten an Seen sendet. Erstellen Sie bei Bedarf eine [Segmentierungslogik](https://docs.seen.io/segments) in Ihrem Workspace und fügen Sie diese hinzu.
3. Bauen Sie Ihre Logik nach Bedarf mit den folgenden Knotenpunkten auf:
   - **Bedingter Knoten**: Nutzer:innen auf der Grundlage von Attributen leiten (z.B. Tarifart oder Region)
   - **Projekt-Knotenpunkt**: Wenden Sie die dynamische Personalisierung von Videos anhand der eingehenden Daten an
   - **Spieler-Knoten**: Generieren Sie eine eindeutige URL für den Video-Player
4. Fügen Sie einen **Webhook-Knoten** hinzu, um die Antwort zu definieren, die an Braze zurückgeschickt wird.

#### Webhook-Knoten Antwortanforderungen

Da die Nutzlast der Antwort konfigurierbar ist, stellen Sie sicher, dass die folgenden Felder zurückgegeben werden, um die im nächsten Schritt beschriebene Braze Data Transformation zu unterstützen:

| Feld | Beschreibung |
|------|-------------|
| `id` | Muss mit der von Braze gesendeten `braze_id` übereinstimmen. |
| `player_url` | Eindeutige URL für den personalisierten Video-Player |
| `email_thumbnail_url` | URL der generierten Video-Miniaturansicht |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Wenn Ihr Anwendungsfall zusätzliche Attribute erfordert, fügen Sie diese in die Antwort ein und bilden sie in Braze ab.


### Schritt 3: Erstellen Sie eine Datentransformation, um Daten von Seen zu erhalten.

Verwenden Sie Braze Data Transformations, um die Seen Journey-Antwort aufzunehmen und Video-Assets im Nutzerprofil zu speichern.

1. Erstellen Sie die folgenden [angepassten Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) in Braze:
   - `player_url`
   - `email_thumbnail_url`
2. Navigieren Sie zu **Dateneinstellungen** → **Datentransformation** und klicken Sie auf **Transformation erstellen**.
3. Konfigurieren Sie die Transformation:
   - **Von Grund auf neu erstellen**
   - **Ziel** → POST: Nutzer:innen tracken
4. Geben Sie die generierte Webhook-URL an Seen weiter oder fügen Sie sie direkt zum Journey **Webhook-Knoten** hinzu.
5. Verwenden Sie den folgenden Code für die Transformation:

```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.id,
      "_update_existing_only": true,
      "player_url": payload.player_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```

{: start="6"}
6\. Senden Sie eine Test-Nutzlast an den angegebenen Endpunkt. Senden Sie Daten an Seen Platform, um Ihre Journey auszuführen, oder senden Sie die Nutzlast mit [Postman](https://www.postman.com/) oder einem anderen ähnlichen Dienst direkt an Braze.
7\. Wählen Sie **Validieren**, um sicherzustellen, dass alles wie vorgesehen funktioniert.
8\. Wählen Sie **Speichern** und **Aktivieren**.