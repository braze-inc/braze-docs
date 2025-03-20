---
nav_title: "POST: E-Mail-Abonnementstatus ändern"
article_title: "POST: E-Mail-Abonnementstatus ändern"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts Status des E-Mail-Abonnements des Benutzers ändern."

---
{% api %}
# Status des E-Mail-Abonnements ändern
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/status
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um den Status des E-Mail-Abonnements für Ihre Benutzer festzulegen.

Benutzer können `opted_in`, `unsubscribed` oder `subscribed` sein (nicht speziell ein- oder ausgeschaltet).

Sie können den E-Mail-Abonnementstatus für eine E-Mail-Adresse festlegen, die noch mit keinem Ihrer Benutzer in Braze verknüpft ist. Wenn diese E-Mail-Adresse anschließend mit einem Benutzer verknüpft wird, wird der von Ihnen hochgeladene E-Mail-Abonnementstatus automatisch eingestellt.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `email.status`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Körper der Anfrage

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

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `email` | Erforderlich | String oder Array | String-E-Mail-Adresse, die geändert werden soll, oder ein Array mit bis zu 50 zu ändernden E-Mail-Adressen. |
| `subscription_state` | Erforderlich | String | Entweder "abonniert", "abgemeldet" oder "opted_in". |
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
