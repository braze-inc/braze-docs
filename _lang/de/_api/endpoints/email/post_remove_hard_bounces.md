---
nav_title: "POST: Hartnäckig gebouncte E-Mails entfernen"
article_title: "POST: Hard Bounced E-Mails entfernen"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Remove hard bounced email addresses Braze."

---
{% api %}
# Hartnäckig gebouncte E-Mails entfernen
{% apimethod post %}
/email/bounce/remove
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um E-Mail-Adressen aus Ihrer Braze Bounce-Liste und der von Ihrem E-Mail-Anbieter geführten Bounce-Liste zu entfernen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7b87a884-fa20-4085-b9f1-18363103575f {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `email.bounce.remove`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com"
}
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| ----------|-----------| ---------|------ |
| `email` | Erforderlich | String oder Array | Zu ändernde String-E-Mail-Adresse oder ein Array mit bis zu 50 zu ändernden E-Mail-Adressen. |
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
