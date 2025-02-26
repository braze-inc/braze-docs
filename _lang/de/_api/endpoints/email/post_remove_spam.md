---
nav_title: "POST: E-Mail-Adressen aus der Spam-Liste entfernen"
article_title: "POST: E-Mail-Adressen aus der Spam-Liste entfernen"
search_tag: Endpoint
page_order: 7
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze Endpunkts E-Mail-Adressen aus der Spamliste entfernen."

---
{% api %}
# E-Mail-Adressen aus der Spam-Liste entfernen
{% apimethod post %}
/email/spam/remove
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um E-Mail-Adressen aus Ihrer Braze-Spamliste und der von Ihrem E-Mail-Anbieter geführten Spamliste zu entfernen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `email.spam.remove`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Körper der Anfrage
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com"
}
```

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| ----------|-----------| --------|------- |
| `email` | Erforderlich | String oder Array | String-E-Mail-Adresse, die geändert werden soll, oder ein Array mit bis zu 50 zu ändernden E-Mail-Adressen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/spam/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```
{% endapi %}
