---
nav_title: "GET: Abfrage hart gebouncter E-Mails"
article_title: "GET: Abfrage hart gebouncter E-Mails"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze Endpunkts Query or list hard bounced email addresses."

---
{% api %}
# Abfrage hart gebouncter E-Mails
{% apimethod get %}
/email/hard_bounces
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste der E-Mail-Adressen abzurufen, die Ihre E-Mail-Nachrichten innerhalb eines bestimmten Zeitraums "hart gebounced" haben.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `email.hard_bounces`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| ----------|-----------| ----------|----- |
| `start_date` | Optional<br>(siehe Anmerkung) | Zeichenfolge im Format JJJJ-MM-TT| Startdatum des Bereichs zum Abrufen von Hard Bounces, muss vor `end_date` liegen. Dies wird von der API als Mitternacht in UTC-Zeit behandelt. |
| `end_date` | Optional<br>(siehe Anmerkung) | Zeichenfolge im Format JJJJ-MM-TT | Enddatum des Bereichs zum Abrufen von Hard Bounces. Dies wird von der API als Mitternacht in UTC-Zeit behandelt. |
| `limit` | Optional | Integer | Optionales Feld zur Begrenzung der Anzahl der zurückgegebenen Ergebnisse. Der Standardwert ist 100, das Maximum ist 500. |
| `offset` | Optional | Integer | Optionaler Anfangspunkt in der Liste, von dem aus abgerufen werden soll. |
| `email` | Optional<br>(siehe Anmerkung) | String | Falls angegeben, geben wir zurück, ob der Benutzer einen Hard Bounce durchgeführt hat oder nicht. Prüfen Sie, ob die E-Mail-Zeichenfolgen richtig formatiert sind. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Sie müssen entweder eine `start_date` und `end_date`, ODER eine `email` angeben. Wenn Sie alle drei, `start_date`, `end_date` und `email`, angeben, werden die angegebenen E-Mails vorrangig behandelt und der Datumsbereich wird nicht berücksichtigt.
{% endalert %}

Wenn Ihr Datumsbereich mehr als die `limit` Anzahl von Hard Bounces aufweist, müssen Sie mehrere API-Aufrufe tätigen und jedes Mal die `offset` erhöhen, bis ein Aufruf entweder weniger als `limit` oder null Ergebnisse liefert. Die Einbeziehung der Parameter `offset` und `limit` mit `email` kann zu einer leeren Antwort führen.

## Beispiel Anfrage
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Antwort
Die Einträge sind in absteigender Reihenfolge aufgeführt.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "emails": [
    {
      "email": (string) an email that has hard bounced,
      "unsubscribed_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "unsubscribed_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "unsubscribed_at": (string) the time the email hard bounced in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}
