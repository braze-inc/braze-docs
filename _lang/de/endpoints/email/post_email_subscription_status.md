---
nav_title: "POST: Status des E-Mail Abos ändern"
article_title: "POST: Status des E-Mail-Abonnements ändern"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Benutzer:innen den Status ihres E-Mail-Abos ändern Braze."

---
{% api %}
# Status des E-Mail Abos ändern
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/status
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um den Status des E-Mail Abos für Ihre Nutzer:innen festzulegen.

Nutzer:in können `opted_in`, `unsubscribed` oder `subscribed` sein (ohne spezielles Opt-in oder Opt-out).

Sie können den Status des E-Mail Abos für eine E-Mail Adresse festlegen, die noch mit keiner Ihrer Nutzer:innen in Braze verbunden ist. Wenn diese E-Mail Adresse anschließend mit einem Nutzer:innen verknüpft wird, wird der von Ihnen hochgeladene Status des E-Mail Abos automatisch eingestellt.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `email.status`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `email` | Erforderlich | String oder Array | Zu ändernde String-E-Mail-Adresse oder ein Array mit bis zu 50 zu ändernden E-Mail-Adressen. |
| `subscription_state` | Erforderlich | String | Entweder "abonniert", "abgemeldet", oder "opted_in". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}'
```


{% endapi %}
