---
nav_title: "GET: Abfrage der Liste der abgemeldeten E-Mail-Adressen"
article_title: "GET: Abfrage der Liste der abgemeldeten E-Mail-Adressen"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Retrieve list of or query email unsubscribes von Braze."

---
{% api %}
# Abfrage der Liste der abgemeldeten E-Mail-Adressen
{% apimethod get %}
/email/abgemeldet
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die letzten E-Mails zurückzugeben, die im Zeitraum von `start_date` bis `end_date` abgemeldet wurden. Um einen vollständigen Verlauf des Abo-Status zu erhalten, verwenden Sie [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), um diese Daten zu verfolgen.

Sie können diesen Endpunkt verwenden, um eine bidirektionale Synchronisierung zwischen Braze und anderen E-Mail-Systemen oder Ihrer eigenen Datenbank einzurichten.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d2966b81-188a-407b-ba7e-e6c252c44b4a {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `email.unsubscribe`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| ----------|-----------| ---------|------ |
| `start_date` | Optional <br>(siehe Anmerkung) | String im Format JJJJ-MM-TT| Startdatum des Bereichs zum Abmelden von Abonnements, muss vor end_date. liegen. Dies wird von der API als Mitternacht in UTC-Zeit behandelt. |
| `end_date` | Optional <br>(siehe Anmerkung) | String im Format JJJJ-MM-TT | Enddatum des Bereichs zum Abrufen der Abmeldungen. Dies wird von der API als Mitternacht in UTC-Zeit behandelt. |
| `limit` | Optional | Integer | Optionales Feld zur Begrenzung der Anzahl der zurückgegebenen Ergebnisse. Standardmäßig sind es 100, maximal 500. |
| `offset` | Optional | Integer | Optionaler Anfangspunkt in der Liste, ab dem abgerufen werden soll. |
| `sort_direction` | Optional | String | Geben Sie den Wert `asc` ein, um die Abmeldungen von den ältesten bis zu den neuesten zu sortieren. Geben Sie `desc` ein, um vom neuesten zum ältesten zu sortieren. Wenn `sort_direction` nicht enthalten ist, ist die Standardreihenfolge die neueste nach der ältesten. |
| `email` | Optional <br>(siehe Anmerkung) | String | Falls angegeben, geben wir zurück, ob sich der Nutzer:in abgemeldet hat oder nicht. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Sie müssen eine `end_date` sowie entweder eine `email` oder eine `start_date` bereitstellen.
{% endalert %}

Wenn Ihr Datumsbereich mehr als `limit` Abmeldungen aufweist, müssen Sie mehrere API-Aufrufe tätigen und dabei jedes Mal die `offset` erhöhen, bis ein Aufruf entweder weniger als `limit` oder null Ergebnisse liefert.

## Beispiel Anfrage
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/unsubscribes?start_date=2020-01-01&end_date=2020-02-01&limit=1&offset=1&sort_direction=desc&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Antwort

Die Eingänge sind in absteigender Reihenfolge aufgeführt.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "emails": [
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}
