---
nav_title: "POST: Hard Bounced Emails entfernen"
article_title: "POST: Hard Bounced Emails entfernen"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze Endpunkts Remove hard bounced email addresses."

---
{% api %}
# Entfernen Sie hartnäckig abgelehnte E-Mails
{% apimethod post %}
/email/bounce/remove
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um E-Mail-Adressen aus Ihrer Braze Bounce-Liste und der Bounce-Liste Ihres E-Mail-Anbieters zu entfernen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7b87a884-fa20-4085-b9f1-18363103575f {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `email.bounce.remove`.

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
| ----------|-----------| ---------|------ |
| `email` | Erforderlich | String oder Array | String-E-Mail-Adresse, die geändert werden soll, oder ein Array mit bis zu 50 zu ändernden E-Mail-Adressen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/bounce/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```

{% endapi %}
