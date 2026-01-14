---
nav_title: "POST: Senden Sie Transaktions-E-Mails mit API-getriggerter Zustellung"
article_title: "POST: Senden Sie Transaktions-E-Mails mit API-getriggerter Zustellung"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Endpunkt Senden von Transaktions-E-Mails mit API-getriggerter Zustellung von Braze."

---

{% api %}
# Senden Sie Transaktions-E-Mails mit API-getriggerter Zustellung
{% apimethod post %}
/transactional/v1/campaigns/{campaign_id}/send
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um sofortige, einmalige transaktionsbezogene Nachrichten an einen bestimmten Nutzer:innen zu senden.

Dieser Endpunkt wird bei der Erstellung einer Braze [Transaktions-E-Mail-Kampagne]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) und der entsprechenden Kampagnen ID verwendet.

{% alert important %}
Transaktions-E-Mails sind derzeit als Teil ausgewählter Braze-Pakete verfügbar. Wenden Sie sich an Ihren Customer-Success-Manager:in von Braze, um weitere Einzelheiten zu erfahren.
{% endalert %}

Ähnlich wie beim [Endpunkt für getriggerte Kampagnen]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) können Sie mit diesem Kampagnentyp den Inhalt von Nachrichten innerhalb des Braze-Dashboards unterbringen und gleichzeitig festlegen, wann und an wen eine Nachricht über Ihre API gesendet wird. Im Gegensatz zum Endpunkt Getriggerte Kampagne senden, der eine Zielgruppe oder ein Segment akzeptiert, an das Nachrichten gesendet werden sollen, muss eine Anfrage an diesen Endpunkt einen einzelnen Nutzer:innen entweder durch `external_user_id` oder `user_alias` spezifizieren, da dieser Kampagnentyp für 1:1-Nachrichten wie Bestellbestätigungen oder die Rücksetzung von Passwörtern gedacht ist.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `transactional.send` erstellen.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

## Pfad-Parameter

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `campaign_id` | Erforderlich | String | ID der Kampagne |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Anfragetext

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

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`external_send_id`| Optional | String |  Ein Base64-kompatibler String. Überprüft anhand der folgenden Regex:<br><br> `/^[a-zA-Z0-9-_+\/=]+$/` <br><br>In diesem optionalen Feld können Sie einen internen Bezeichner für diese bestimmte Sendung angeben, der in den Ereignissen enthalten ist, die vom Transactional HTTP Event Postback gesendet werden. Wenn Sie diesen Bezeichner weitergeben, wird er auch als Deduplizierungsschlüssel verwendet, den Braze für 24 Stunden speichert. <br><br>Die Übergabe desselben Bezeichners in einer anderen Anfrage führt 24 Stunden lang nicht zu einer neuen Instanz einer Sendung von Braze.|
|`trigger_properties`|Optional|Objekt|Siehe [Eigenschaften des Auslösers]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Schlüssel-Wert-Paare für die Personalisierung, die für den Nutzer:innen in dieser Anfrage gelten sollen. |
|`recipient`|Erforderlich|Objekt| Der Nutzer:in, dem Sie diese Nachricht zukommen lassen möchten. Kann `attributes` und ein einzelnes `external_user_id` oder `user_alias` enthalten.<br><br>Beachten Sie, dass, wenn Sie eine externe ID angeben, die noch nicht in Braze existiert, durch die Übergabe von Feldern an das `attributes` Objekt dieses Nutzerprofil in Braze erstellt wird und diese Nachricht an den neu erstellten Nutzer gesendet wird. <br><br>Wenn Sie mehrere Anfragen an denselben Nutzer mit unterschiedlichen Daten im Objekt `attributes` senden, werden die Attribute `first_name`, `last_name` und `email` synchron aktualisiert und als Template in Ihre Nachricht eingefügt. Angepasste Attribute verfügen nicht über diesen Schutz. Seien Sie also vorsichtig, wenn Sie einen Nutzer:innen über diese API aktualisieren und verschiedene Werte für angepasste Attribute in schneller Folge übergeben.|
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

Der Endpunkt Transaktions-E-Mails senden antwortet mit der `dispatch_id` der Nachricht, die die Instanz dieser Nachricht darstellt. Dieser Bezeichner kann zusammen mit den Ereignissen aus der Transaktion HTTP Event Postback verwendet werden, um den Status einer einzelnen E-Mail zu verfolgen, die an einen einzelnen Nutzer:innen gesendet wurde.

### Beispielhafte Antworten

```json
{
    "dispatch_id": A randomly-generated unique ID of the instance of this send
    "status": Current status of the message
    "metadata" : Object containing additional information about the send instance
}
```

## Fehlersuche

Der Endpunkt kann in einigen Fällen auch einen Fehlercode und eine von Menschen lesbare Nachricht zurückgeben, wobei es sich meist um Validierungsfehler handelt. Hier finden Sie einige häufige Fehler, die bei ungültigen Anfragen auftreten können.

| Fehler | Fehlersuche |
| ----- | --------------- |
| `The campaign is not a transactional campaign. Only transactional campaigns may use this endpoint` | Die angegebene Kampagnen ID ist nicht für eine transaktionale Kampagne. |
| `The external reference has been queued.  Please retry to obtain send_id.` | Die external_send_id wurde erst kürzlich erstellt. Versuchen Sie eine neue external_send_id, wenn Sie eine neue Nachricht senden möchten. |
| `Campaign does not exist` | Die angegebene ID der Kampagne stimmt nicht mit einer bestehenden Kampagne überein. |
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | Die angegebene ID der Kampagne entspricht einer archivierten Kampagne. |
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | Die angegebene ID der Kampagne entspricht einer pausierten Kampagne. |
| `campaign_id must be a string of the campaign api identifier` | Die angegebene ID für die Kampagne ist kein gültiges Format. |
| `Error authenticating credentials` | Der angegebene API-Schlüssel ist ungültig |
| `Invalid whitelisted IPs `| Die IP-Adresse, von der die Anfrage ausgeht, steht nicht auf der IP-Whitelist (falls diese verwendet wird) |
| `You do not have permission to access this resource` | Der verwendete API-Schlüssel hat keine Berechtigung, diese Aktion durchzuführen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Die meisten Endpunkte bei Braze verfügen über eine Rate-Limits-Implementierung, die einen 429er Code als Antwort zurückgibt, wenn Sie zu viele Anfragen gestellt haben. Der Endpunkt für den Transaktionsversand funktioniert anders: Wenn Sie das Ihnen zugewiesene Rate-Limit überschreiten, nimmt unser System die API-Aufrufe weiterhin auf, gibt Erfolgscodes zurück und versendet die Nachrichten. Diese Nachrichten unterliegen jedoch möglicherweise nicht den vertraglichen SLAs für das Feature. Bitte kontaktieren Sie uns, wenn Sie weitere Informationen über diese Funktion benötigen.

## Transaktionelles HTTP-Ereignis Postback

{% multi_lang_include http_event_postback.md %}

{% endapi %}
