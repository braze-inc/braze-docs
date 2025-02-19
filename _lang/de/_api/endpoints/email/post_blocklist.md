---
nav_title: "POST: Blocklisten-E-Mails"
article_title: "POST: Blocklisten-E-Mails"
search_tag: Endpoint
page_order: 8
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Blocklist emails Braze."

---
{% api %}
# Blocklisten-E-Mails
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/blocklist
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen Benutzer von einer E-Mail abzumelden und ihn als "hard bounced" zu kennzeichnen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `email.blacklist`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Körper der Anfrage

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["blocklist_email1","blocklist_email2"]
}
```

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| -----------|----------| --------|------- |
| `email` | Erforderlich | String oder Array | String-E-Mail-Adresse für die Blockliste oder ein Array mit bis zu 50 E-Mail-Adressen für die Blockliste. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blocklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blocklist_email1","blocklist_email2"]
}'
```

{% endapi %}
