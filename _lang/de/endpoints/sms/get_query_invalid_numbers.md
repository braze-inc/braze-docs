---
nav_title: "GET: Abfrage ungültiger Telefonnummern"
article_title: "GET: Ungültige Telefonnummern abfragen"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Query invalid phone numbers Braze."
---
{% api %}
# Abfrage ungültiger Telefonnummern
{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste der Telefonnummern abzurufen, die innerhalb eines bestimmten Zeitraums als "ungültig" markiert wurden. Weitere Informationen finden Sie in der Dokumentation [Behandlung ungültiger Telefonnummern]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#handling-invalid-phone-numbers).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81ceae19-15d1-4ac1-ad22-a6b86a92456d {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `sms.invalid_phone_numbers`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| ----------|-----------| ----------|----- |
| `start_date` | Optional <br>(siehe Anmerkung) | String im Format JJJJ-MM-TT| Startdatum des Bereichs zum Abrufen ungültiger Telefonnummern, muss vor `end_date` liegen. Dies wird von der API als Mitternacht in UTC-Zeit behandelt. |
| `end_date` | Optional <br>(siehe Anmerkung) | String im Format JJJJ-MM-TT | Enddatum des Bereichs zum Abrufen ungültiger Telefonnummern. Dies wird von der API als Mitternacht in UTC-Zeit behandelt. |
| `limit` | Optional | Integer | Optionales Feld zur Begrenzung der Anzahl der zurückgegebenen Ergebnisse. Standardmäßig sind es 100, maximal 500. |
| `offset` | Optional | Integer | Optionaler Anfangspunkt in der Liste, ab dem abgerufen werden soll. |
| `phone_numbers` | Optional <br>(siehe Anmerkung) | Array von Strings im Format e.164  | Wenn Sie eine Telefonnummer angeben, werden wir diese zurückschicken, wenn sie sich als ungültig erweist. |
| `reason` | Optional <br>(siehe Anmerkung) | String | Verfügbare Werte sind "provider_error" (Providerfehler zeigt an, dass das Telefon keine SMS empfangen kann) oder "deaktiviert" (die Telefonnummer wurde deaktiviert). Wenn Sie diese Option auslassen, werden alle Gründe zurückgegeben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Sie müssen entweder eine `start_date` und eine `end_date` ODER eine `phone_numbers` bereitstellen. Wenn Sie alle drei, `start_date`, `end_date` und `phone_numbers`, angeben, priorisieren wir die angegebenen Telefonnummern und lassen den Datumsbereich außer Acht.
{% endalert %}

Wenn Ihr Datumsbereich mehr als die `limit` Anzahl ungültiger Telefonnummern enthält, müssen Sie mehrere API-Aufrufe tätigen und dabei jedes Mal die `offset` erhöhen, bis ein Aufruf entweder weniger als `limit` oder null Ergebnisse liefert.

## Beispiel Anfrage
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Antwort
Die Eingänge sind in absteigender Reihenfolge aufgeführt.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "sms": [
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "provider_error"
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "deactivated"
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "provider_error"
    }
  ],
  "message": "success"
}
```
{% endapi %}
