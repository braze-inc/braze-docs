---
nav_title: "GET: [Name des Endpunkts]"
article_title: "Beispiel-Layout: GET: [Name des Endpunkts]"
search_tag: Endpoint
page_order: 1
excerpt_separator: ""
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Verwendung und die Parameter für die Nutzung des Endpunkts Get [Endpunktname] Braze."

noindex: true
#ATTENTION: remove noindex and this alert from template
---
{% api %}
# Abfrage oder Liste [Artikel Endpunkt "Gets"]

{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

<!--
This is the description of the endpoint. API descriptions usually start with "Use this endpoint to..."-->
Verwenden Sie diesen Endpunkt, um eine Liste von Telefonnummern abzurufen, die innerhalb eines bestimmten Zeitraums als "ungültig" eingestuft wurden.

<!-- Your postman link. After you have published the endpoint to postman, you will be able get a direct link to the information in the postman docs to share here-->
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Rate-Limit

<!-- The rate limit of the endpoint. This pulls from /includes/rate_limits/ and displays specific endpoint limits based on the endpoint provided -->
{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

<!--This is where you can give more information about your endpoint parameters. -->

| Parameter | Erforderlich | Datentyp | Beschreibung |
| ----------|-----------| ----------|----- |
| `start_date` | Optional <br>(siehe Anmerkung) | String im Format JJJJ-MM-TT| Startdatum des Bereichs zum Abrufen ungültiger Telefonnummern, muss vor `end_date` liegen. Dies wird von der API als Mitternacht in UTC-Zeit behandelt. |
| `end_date` | Optional <br>(siehe Anmerkung) | String im Format JJJJ-MM-TT | Enddatum des Bereichs zum Abrufen ungültiger Telefonnummern. Dies wird von der API als Mitternacht in UTC-Zeit behandelt. |
| `limit` | Optional | Integer | Optionales Feld zur Begrenzung der Anzahl der zurückgegebenen Ergebnisse. Standardmäßig sind es 100, maximal 500. |
| `offset` | Optional | Integer | Optionaler Anfangspunkt in der Liste, ab dem abgerufen werden soll. |
| `phone_numbers` | Optional <br>(siehe Anmerkung) | Array von Strings im Format e.164  | Wenn Sie eine Telefonnummer angeben, werden wir diese zurückschicken, wenn sie sich als ungültig erweist. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Sie müssen entweder eine `start_date` und eine `end_date` ODER eine `phone_numbers` bereitstellen. Wenn Sie alle drei, `start_date`, `end_date` und `phone_numbers`, angeben, priorisieren wir die angegebenen Telefonnummern und lassen den Datumsbereich außer Acht.
{% endalert %}

## Beispiel Anfrage

<!--The following example demonstrates a request that will pull a list of phone numbers that have been deemed invalid via the API:-->
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Antwort

<!-- An example response that defines the different variables returned-->
```json
{
  "sms": [
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    }
  ],
  "message": "success"
}
```

{% endapi %}
