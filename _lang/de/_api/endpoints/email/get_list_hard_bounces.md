---
nav_title: "GET: Abfrage hart gebouncter E-Mails"
article_title: "GET: Abfrage hart gebouncter E-Mails"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Abfrage oder Liste hart gebouncter E-Mail-Adressen von Braze."

---
{% api %}
# Abfrage hart gebouncter E-Mails
{% apimethod get %}
/email/hard_bounces
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste der E-Mail-Adressen abzurufen, die Ihre Nachrichten innerhalb eines bestimmten Zeitraums "hart gebounct" haben.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `email.hard_bounces`.

## Rate-Limits

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| ----------|-----------| ----------|----- |
| `start_date` | Fakultativ* | String im Format JJJJ-MM-TT| \*Eine der Optionen `start_date` oder `email` ist erforderlich. Dies ist das Startdatum des Bereichs zum Abrufen von Hard Bounces und muss vor `end_date` liegen. Dies wird von der API als Mitternacht in UTC-Zeit behandelt. |
| `end_date` | Erforderlich | String im Format JJJJ-MM-TT | Enddatum des Bereichs zum Abrufen von Hard Bounces. Dies wird von der API als Mitternacht in UTC-Zeit behandelt. |
| `limit` | Optional | Integer | Optionales Feld zur Begrenzung der Anzahl der zurückgegebenen Ergebnisse. Standardmäßig sind es 100, maximal 500. |
| `offset` | Optional | Integer | Optionaler Anfangspunkt in der Liste, ab dem abgerufen werden soll. |
| `email` | Fakultativ* | String | \*Eine der Optionen `start_date` oder `email` ist erforderlich. Falls angegeben, geben wir zurück, ob der Nutzer:in hart gebounced hat oder nicht. Überprüfen Sie, ob die Strings der E-Mails richtig formatiert sind. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Sie müssen eine `end_date` und entweder eine `email` oder eine `start_date` angeben. Wenn Sie alle drei Angaben machen, `start_date`, `end_date` und `email`, priorisieren wir die angegebenen E-Mails und lassen den Datumsbereich unberücksichtigt.
{% endalert %}

Wenn Ihr Datumsbereich mehr als die `limit` Anzahl von Hard Bounces aufweist, müssen Sie mehrere API-Aufrufe tätigen und dabei jedes Mal die `offset` erhöhen, bis ein Aufruf entweder weniger als `limit` oder null Ergebnisse liefert. Die Einbeziehung der Parameter `offset` und `limit` mit `email` kann zu einer leeren Antwort führen.

## Beispiel Anfrage
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1' \
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
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}
