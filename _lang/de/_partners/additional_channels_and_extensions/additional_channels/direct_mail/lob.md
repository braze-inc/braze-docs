---
nav_title: Lob
article_title: Lob 
alias: /partners/lob/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Lob.com, die es Ihnen erlaubt, Direkt-Mailing wie Briefe, Postkarten und Schecks per Post zu versenden."
page_type: partner
search_tag: Partner

---

# Lob

> [Lob.com](https://lob.com) ist ein Online-Dienst, der es Ihnen erlaubt, Direkt-Mailing an Ihre Nutzer:innen zu senden.

_Diese Integration wird von Lob gepflegt._

## Über die Integration

Mit dieser Integration können Sie:

- Versenden Sie mit Braze-Webhooks und der Lob API briefähnliche Briefe, Postkarten und Schecks über die Post.
- Teilen Sie Lob-Events mit Braze als angepasste Attribute und Events mit Hilfe von Braze Data Transformation und Lob-Webhooks.

## Voraussetzungen

|Anforderung| Beschreibung|
| ---| ---|
|Lob Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Lob-Konto. |
| Lob API-Schlüssel | Ihren Lob API-Schlüssel finden Sie im Abschnitt Einstellungen unter Ihrem Namen im Lob Dashboard. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Versenden von E-Mails mit Braze-Webhooks

### Schritt 1: Wählen Sie einen Lob-Endpunkt

Je nachdem, was Sie in Lob tun möchten, müssen Sie den entsprechenden Endpunkt in der HTTP-Anfrage Ihres Webhooks verwenden. Ausführliche Informationen zu den einzelnen Endpunkten finden Sie in der [referenzierten Dokumentation der API von Lob](https://lob.com/docs#intro).

| Basis-URL | Verfügbare Endpunkte |
| ------------ | ------------------- |
| `https://api.lob.com/` | `/v1/addresses<br>/v1/addresses/{id}`<br>`/v1/verify`<br>`/v1/postcards`<br>`/v1/postcards/{id}`<br>`/v1/letter`<br>`/v1/letter/{id}`<br>`/v1/checks<br>/v1/checks/{id}`<br>`/v1/bank_accounts`<br>`/v1/bank_accounts/{id}`<br>`/v1/bank_accounts/{id}/verify`<br>`/v1/areas<br>/v1/areas/{id}`<br>`/v1/routes/{zip_code}`<br>`/v1/routes`<br>`/v1/countries<br>/v1/states`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Schritt 2: Erstellen Sie Ihr Braze-to-Braze-Webhook Template

Um eine Lob Webhook-Vorlage zu erstellen, die Sie in zukünftigen Kampagnen oder Canvase verwenden können, gehen Sie im Braze-Dashboard zu **Templates** > **Webhook Templates**. 

Wenn Sie eine einmalige Lob-Webhook-Kampagne erstellen oder eine bestehende Vorlage verwenden möchten, wählen Sie bei der Erstellung einer neuen Kampagne **Webhook** in Braze aus.

Füllen Sie in Ihrem neuen Webhook Template die folgenden Felder aus:

- **Webhook URL**: `<LOB_API_ENDPOINT>`
- **Anfrage Körper**: Rohtext

#### Kopfzeilen der Anfrage und Methode

Lob benötigt einen HTTP-Header für die Autorisierung und eine HTTP-Methode. Das Folgende ist bereits als Schlüssel-Wert-Paar in der Vorlage enthalten, aber auf dem Tab **Einstellungen** müssen Sie `<LOB_API_KEY>` durch Ihren Lob API-Schlüssel ersetzen. Dieser Schlüssel muss ein ":" direkt nach dem Schlüssel enthalten und in Base 64 kodiert sein. 

- **HTTP-Methode**: POST
- **Anfrage-Header**:
  - **Autorisierung**: Basic `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Typ**: application/json

![Der Code des Anfragekörpers und die Webhook-URL werden im Tab "Braze webhook builder compose" angezeigt.]({% image_buster /assets/img_archive/lob_full_request.png %})

#### Anfragetext

Im Folgenden sehen Sie einen Beispiel-Anfragetext für den Endpunkt Lob postcards. Dieser Body der Anfrage wird zwar im Basis-Template von Lob in Braze bereitgestellt, aber wenn Sie andere Endpunkte verwenden möchten, müssen Sie Ihre Liquid-Felder entsprechend anpassen.

{% raw %}
```json
"description": "Demo Postcard",
"to": {
    "name": "{{${first_name}}} {{${last_name}}}",
    "address_line1": "{{custom_attribute.${address_line1}}}",
    "address_city": "{{custom_attribute.${address_city}}}"
    "address_zip": "{{custom_attribute.${address_zip}}}",
    "address_country": "{{custom_attribute.${address_country}}}"
},
"front": "https://lob.com/postcardfront.pdf",
"back": "https://lob.com/postcardback.pdf"
```
{% endraw %}

### Schritt 3: Vorschau auf Ihre Anfrage

An diesem Punkt sollte Ihre Kampagne bereit sein, um getestet und versendet zu werden. Überprüfen Sie das Dashboard von Lob und die Nachrichtenprotokolle der Entwickler:in der Braze-Entwicklerkonsole, wenn Sie auf Fehler stoßen. Der folgende Fehler wurde zum Beispiel durch einen falsch formatierten Authentifizierungs-Header verursacht. 

{% alert important %}
Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Templates finden Sie in der Liste **Gespeicherte Webhook-Templates**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}

![Ein Nachrichten-Fehlerprotokoll, das die Zeit, den Namen der App, den Kanal und die Fehlermeldung anzeigt. Die Fehlermeldung enthält die Benachrichtigung und den Fehlercode.]({% image_buster /assets/img_archive/error_log.png %})

## Gemeinsame Nutzung von Ereignissen mit Lob Webhooks 

Mit [Braze Data Transformation]({{site.baseurl}}/user_guide/data/data_transformation/overview) können Sie Webhooks zur Automatisierung des Datenflusses von externen Plattformen in Braze erstellen und verwalten. Jede Transformation erhält einen eindeutigen Endpunkt, den andere Plattformen als Ziel für ihren Webhook verwenden können.

{% alert important %}
Das Template für Datentransformation von Lob sendet Ereignisse über Ihren [`/users/track` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track), der Datenpunkte in Braze konsumiert. Wir empfehlen Ihnen, in Ihren Lob Webhook-Einstellungen ein Rate-Limits festzulegen, damit Sie nicht zu viele Daten verbrauchen.
{% endalert %}

### Schritt 1: Erstellen Sie eine Transformation in Braze

1. Gehen Sie im Braze Dashboard zu **Dateneinstellungen** > **Datentransformationen** und wählen Sie dann **Transformation erstellen**.
2. Geben Sie einen kurzen, beschreibenden Namen für Ihre Transformation ein.
3. Wählen Sie unter **Bearbeitungserfahrung** die Option **Template verwenden** aus, suchen Sie dann nach Lob und aktivieren Sie das Kontrollkästchen.
4. Wenn Sie fertig sind, wählen Sie **Transformation erstellen**. Sie werden zum Transformations-Editor weitergeleitet, den Sie im nächsten Schritt verwenden werden.

### Schritt 2: Füllen Sie das Template Lob aus

Mit diesem Template können Sie eines Ihrer Lob Events in ein angepasstes Event oder Attribut transformieren, das in Braze verwendet werden kann. Folgen Sie den Inline-Kommentaren, um das Template fertig zu stellen.

{% alert tip %}
Ausführliche Informationen über die Struktur der Webhook-Nutzlast von Lob finden Sie unter [Lob: Webhooks verwenden](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks).
{% endalert %}

```json
// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JavaScript dot notation, such as payload.x.y.z

// In this example, this function removes the periods and underscores of the event_type.id sent in the Lob payload so that an event id that is formatted like: `letter.processed_for_delivery` will log an event to Braze with the name `letter processed for delivery`.

function formatString(input) {
    return input.replace(/[._]/g, ' ');
}

let braze_event = formatString(payload.event_type.id);

// In this example, a metadata value passed in the Lob Webhook called 'external_ID' is being used to match the Event to the corresponding Braze user.

let brazecall = {
  "attributes": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "Most Recent Mailer": payload.body.description
    }
  ],
  "events": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "name": braze_event,
      "time": new Date().toISOString(),
// Customize the properties to the Lob event you are syncing. Our example below pulls in the Tracking Events array of objects associated with certain Lob events.
      "properties": {
        "tracking_events": payload.body.tracking_events
      }
    }
  ]
};
// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

### Schritt 3: Erstellen Sie einen Webhook in Lob

1. Wenn Sie mit der Erstellung Ihres Templates fertig sind, wählen Sie **Aktivieren** und kopieren Sie die **Webhook-URL** in Ihre Zwischenablage.
2. [Erstellen Sie in Lob einen neuen Webhook](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks#receiving-a-webhook-1) und verwenden Sie dann Ihre Webhook-URL von Braze, um den Webhook zu empfangen.
