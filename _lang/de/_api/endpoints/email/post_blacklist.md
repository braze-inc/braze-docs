---
nav_title: "POST: Schwarze Liste E-Mails"
article_title: "POST: Schwarze Liste E-Mails"
search_tag: Endpoint
page_order: 10
layout: api_page
page_type: reference
alias: /blacklist/
description: "Dieser Artikel beschreibt die Details des Blacklist Emails Braze Endpunkts."

---
{% api %}
# Schwarze Liste für E-Mails
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/blacklist
{% endapimethod %}

{% alert important %}
Braze hat den [`/email/blocklist` Endpunkt]({{site.baseurl}}/api/endpoints/email/post_blocklist/) mit denselben Funktionen wie den `/email/blacklist` Endpunkt veröffentlicht. Wir empfehlen Ihnen, stattdessen den Endpunkt `/email/blocklist` zu verwenden.
{% endalert %}

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
  "email": ["blacklist_email1","blacklist_email2"]
}
```

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| -----------|----------| --------|------- |
| `email` | Erforderlich | String oder Array | String-E-Mail-Adresse, die auf die schwarze Liste gesetzt werden soll, oder ein Array mit bis zu 50 E-Mail-Adressen, die auf die schwarze Liste gesetzt werden sollen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blacklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blacklist_email1","blacklist_email2"]
}'
```

{% endapi %}
