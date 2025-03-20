---
nav_title: "POST: Senden Sie Transaktions-E-Mails mit API-gesteuerter Zustellung"
article_title: "POST: Senden Sie Transaktions-E-Mails mit API-gesteuerter Zustellung"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts Transaktions-E-Mails mit API-gesteuerter Zustellung senden."

---

{% api %}
# Senden Sie Transaktions-E-Mails mit API-gesteuerter Zustellung
{% apimethod post %}
/transactional/v1/campaigns/{campaign_id}/send
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um sofortige, einmalige Transaktionsnachrichten an einen bestimmten Benutzer zu senden.

Dieser Endpunkt wird bei der Erstellung einer [Transaktions-E-Mail-Kampagne]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) von Braze und der entsprechenden Kampagnen-ID verwendet.

{% alert important %}
Transaktions-E-Mail ist derzeit als Teil ausgewählter Braze-Pakete verfügbar. Wenden Sie sich an Ihren Braze Customer Success Manager, um weitere Einzelheiten zu erfahren.
{% endalert %}

Ähnlich wie der [Endpunkt für ausgelöste Kampagnen]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) können Sie mit diesem Kampagnentyp den Inhalt von Nachrichten im Braze-Dashboard unterbringen und gleichzeitig festlegen, wann und an wen eine Nachricht über Ihre API gesendet wird. Im Gegensatz zum Endpunkt Ausgelöste Kampagne senden, der eine Zielgruppe oder ein Segment akzeptiert, an das Nachrichten gesendet werden sollen, muss eine Anfrage an diesen Endpunkt einen einzelnen Benutzer entweder über `external_user_id` oder `user_alias` angeben, da dieser Kampagnentyp speziell für 1:1-Benachrichtigungen wie Bestellbestätigungen oder Passwortrücksetzungen entwickelt wurde.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `transactional.send` erstellen.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

## Pfad-Parameter

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| `campaign_id` | Erforderlich | String | ID der Kampagne |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Körper der Anfrage

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_send_id": (optional, string) see the following request parameters,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to the user in this request,
  "recipient": (required, object)
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User alias object) User alias of the user to receive message,
      "external_user_id": (optional, string) External identifier of user to receive message,
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }
}
```

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`external_send_id`| Optional | String |  Eine Base64-kompatible Zeichenkette. Überprüft anhand der folgenden Regex:<br><br> `/^[a-zA-Z0-9-_+\/=]+$/` <br><br>In diesem optionalen Feld können Sie einen internen Bezeichner für diese bestimmte Sendung angeben, der in den Ereignissen enthalten ist, die vom Transactional HTTP Event Postback gesendet werden. Bei der Übergabe wird diese Kennung auch als Deduplizierungsschlüssel verwendet, den Braze 24 Stunden lang speichert. <br><br>Die Übergabe desselben Identifikators in einer anderen Anfrage führt 24 Stunden lang nicht zu einer neuen Instanz einer Sendung durch Braze.|
|`trigger_properties`|Optional|Objekt|Siehe [Auslösereigenschaften]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Schlüssel-Wert-Paare für die Personalisierung, die für den Benutzer in dieser Anfrage gelten sollen. |
|`recipient`|Erforderlich|Objekt| Der Benutzer, an den Sie diese Nachricht richten. Kann `attributes` und ein einzelnes `external_user_id` oder `user_alias` enthalten.<br><br>Beachten Sie, dass, wenn Sie eine externe Benutzer-ID angeben, die noch nicht in Braze existiert, die Übergabe von Feldern an das `attributes` Objekt dieses Benutzerprofil in Braze erstellt und diese Nachricht an den neu erstellten Benutzer sendet. <br><br>Wenn Sie mehrere Anfragen an denselben Benutzer mit unterschiedlichen Daten im Objekt `attributes` senden, werden die Attribute `first_name`, `last_name` und `email` synchron aktualisiert und als Schablone in Ihre Nachricht eingefügt. Benutzerdefinierte Attribute haben nicht den gleichen Schutz. Seien Sie also vorsichtig, wenn Sie einen Benutzer über diese API aktualisieren und verschiedene Werte für benutzerdefinierte Attribute in schneller Folge übergeben.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer YOUR-REST-API-KEY' \
  -d '{
        "external_send_id" : YOUR_BASE64_COMPATIBLE_ID
        "trigger_properties": {
          "example_string_property": YOUR_EXAMPLE_STRING,
          "example_integer_property": YOUR_EXAMPLE_INTEGER
        },
        "recipient": {
          "external_user_id": TARGETED_USER_ID_STRING
        }
      }' \
  https://rest.iad-01.braze.com/transactional/v1/campaigns/{campaign_id}/send
```

## Antwort

Der Endpunkt Transaktions-E-Mail senden antwortet mit der Nachricht `dispatch_id`, die die Instanz dieser gesendeten Nachricht darstellt. Diese Kennung kann zusammen mit Ereignissen aus dem HTTP-Ereignis Postback Transactional verwendet werden, um den Status einer einzelnen, an einen einzelnen Benutzer gesendeten E-Mail zu verfolgen.

### Beispielhafte Antworten

```json
{
    "dispatch_id": A randomly-generated unique ID of the instance of this send
    "status": Current status of the message
    "metadata" : Object containing additional information about the send instance
}
```

## Fehlersuche

Der Endpunkt kann in einigen Fällen auch einen Fehlercode und eine von Menschen lesbare Nachricht zurückgeben, wobei es sich meist um Validierungsfehler handelt. Hier sind einige häufige Fehler, die Sie bei ungültigen Anfragen erhalten können.

| Fehler | Fehlersuche |
| ----- | --------------- |
| `The campaign is not a transactional campaign. Only transactional campaigns may use this endpoint` | Die angegebene Kampagnen-ID ist nicht für eine Transaktionskampagne bestimmt. |
| `The external reference has been queued.  Please retry to obtain send_id.` | Die external_send_id wurde erst kürzlich erstellt. Versuchen Sie eine neue external_send_id, wenn Sie eine neue Nachricht senden möchten. |
| `Campaign does not exist` | Die angegebene Kampagnen-ID stimmt nicht mit einer bestehenden Kampagne überein. |
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | Die angegebene Kampagnen-ID entspricht einer archivierten Kampagne. |
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | Die angegebene Kampagnen-ID entspricht einer pausierten Kampagne. |
| `campaign_id must be a string of the campaign api identifier` | Die angegebene Kampagnen-ID ist kein gültiges Format. |
| `Error authenticating credentials` | Der angegebene API-Schlüssel ist ungültig |
| `Invalid whitelisted IPs `| Die IP-Adresse, die die Anfrage sendet, steht nicht auf der IP-Whitelist (falls diese verwendet wird) |
| `You do not have permission to access this resource` | Der verwendete API-Schlüssel hat nicht die Berechtigung, diese Aktion durchzuführen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Die meisten Endpunkte bei Braze haben eine Ratenbegrenzung implementiert, die einen Antwortcode 429 zurückgibt, wenn Sie zu viele Anfragen gestellt haben. Der Endpunkt für den Transaktionsversand funktioniert anders: Wenn Sie das Ihnen zugewiesene Ratenlimit überschreiten, nimmt unser System weiterhin die API-Aufrufe auf, gibt Erfolgscodes zurück und sendet die Nachrichten, allerdings unterliegen diese Nachrichten möglicherweise nicht dem vertraglichen SLA für die Funktion. Bitte kontaktieren Sie uns, wenn Sie weitere Informationen über diese Funktion benötigen.

## Transaktionelles HTTP-Ereignis Postback

Alle Transaktions-E-Mails werden durch Ereignisstatus-Postbacks ergänzt, die als HTTP-Anfrage an die von Ihnen angegebene URL zurückgeschickt werden. So können Sie den Status der Nachricht in Echtzeit auswerten und Maßnahmen ergreifen, um den Benutzer auf einem anderen Kanal zu erreichen, wenn die Nachricht nicht zugestellt wurde, oder auf ein internes System zurückgreifen, wenn Braze eine Latenz aufweist.

Um die eingehenden Ereignisse einer bestimmten Sendeinstanz zuzuordnen, können Sie entweder die in der [API-Antwort](#example-response) zurückgegebene Braze `dispatch_id` erfassen und speichern oder Ihre eigene Kennung an das Feld `external_send_id` übergeben. Ein Beispiel für einen Wert, den Sie an dieses Feld übergeben können, ist eine Bestell-ID, bei der nach Abschluss der Bestellung 1234 eine Bestellbestätigungsnachricht über Braze an den Benutzer ausgelöst wird, und `external_send_id : 1234` ist in der Anfrage enthalten. Alle folgenden Ereignis-Postbacks wie `Sent` und `Delivered` enthalten `external_send_id : 1234` in der Nutzlast, so dass Sie bestätigen können, dass der Benutzer seine Bestellbestätigungs-E-Mail erfolgreich erhalten hat.

Um mit dem Transaktions-HTTP-Ereignis-Postback zu beginnen, navigieren Sie in Ihrem Braze-Dashboard zu **Einstellungen** > **E-Mail-Voreinstellungen** und suchen Sie den Abschnitt **Transaktions-Ereignis-Status-Postback**. Geben Sie die gewünschte URL ein, um Postbacks zu erhalten.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie diese Seite unter **Einstellungen verwalten** > **E-Mail-Einstellungen**.
{% endalert %}

![]({% image_buster /assets/img/transactional_webhook_url.png %})

### Körper der Rückmeldung

```json
{
  "dispatch_id": (string, a randomly-generated unique ID of the instance of this send),
  "status": (string, Current status of message from the following message status table,
  "metadata" : (object, additional information relating to the execution of an event)
   {
     "external_send_id" : (string, If provided at the time of the request, Braze will pass your internal identifier for this send for all postbacks),
     "campaign_api_id" : (string, API identifier of this transactional campaign),
     "received_at": (ISO 8601 DateTime string, Timestamp of when the request was received by Braze, only included for events with "sent" status),
     "enqueued_at": (ISO 8601 DateTime string, Timestamp of when the request was enqueued by Braze, only included for events with "sent" status),
     "executed_at": (ISO 8601 DateTime string, Timestamp of when the request was processed by Braze, only included for events with "sent" status),
     "sent_at": (ISO 8601 DateTime string, Timestamp of when the request was sent to the ESP by Braze, only included for events with "sent" status),
     "processed_at" : (ISO 8601 DateTime string, Timestamp the event was processed by the ESP, only included for events with "processed" status),
     "delivered_at" : (ISO 8601 DateTime string, Timestamp the event was delivered to the user's inbox provider, only included for events with "processed" status),
     "bounced_at" : (ISO 8601 DateTime string, Timestamp the event was bounced by the user's inbox provider, only included for events with "bounced" status),
     "aborted_at" : (ISO 8601 DateTime string, Timestamp the event was Aborted by Braze, only included for events with "aborted" status),
     "reason" : (string, The reason Braze or the Inbox provider was unable to process this message to the user, only included for events with "aborted" or "bounced" status),
   }
}
```

#### Status der Nachricht

|  Status | Beschreibung |
| ------------ | ----------- |
| `sent` | Nachricht wurde erfolgreich an einen Braze E-Mail-Versandpartner gesendet |
| `processed` | Der E-Mail-Versandpartner hat die Nachricht erfolgreich empfangen und für den Versand an den Posteingangsanbieter des Benutzers vorbereitet |
| `aborted` | Braze war nicht in der Lage, die Nachricht erfolgreich zu versenden, da der Benutzer keine E-Mail-Adresse hat oder die Logik für den Flüssigkeitsabbruch im Nachrichtentext aufgerufen wurde. Alle abgebrochenen Ereignisse enthalten ein `reason` Feld innerhalb des Metadatenobjekts, das angibt, warum die Nachricht abgebrochen wurde |
|`delivered`| Die Nachricht wurde vom Anbieter des E-Mail-Postfachs des Benutzers akzeptiert |
|`bounced`| Die Nachricht wurde vom Anbieter des E-Mail-Postfachs des Benutzers abgelehnt. Alle Bounce-Ereignisse enthalten ein `reason` Feld im Metadatenobjekt, das den Bounce-Fehlercode des Posteingangsanbieters wiedergibt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Beispiel Postback
```json

// Sent Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "sent",
    "metadata": {
      "received_at": "2020-08-31T18:58:41.000+00:00",
      "enqueued_at": "2020-08-31T18:58:41.000+00:00",
      "executed_at": "2020-08-31T18:58:41.000+00:00",
      "sent_at": "2020-08-31T18:58:42.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Processed Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "processed",
    "metadata": {
      "processed_at": "2020-08-31T18:58:42.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Aborted
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "aborted",
    "metadata": {
      "reason": "User not emailable",
      "aborted_at": "2020-08-31T19:04:51.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Delivered Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "delivered",
    "metadata": {
      "delivered_at": "2020-08-31T18:27:32.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Bounced Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "bounced",
    "metadata": {
      "bounced_at": "2020-08-31T18:58:43.000+00:00",
      "reason": "550 5.1.1 The email account that you tried to reach does not exist",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

```


{% endapi %}
