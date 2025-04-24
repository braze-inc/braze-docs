---
nav_title: "POST: Ungültige Telefonnummern entfernen"
article_title: "POST: Ungültige Telefonnummern entfernen"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Ungültige Telefonnummern entfernen von Braze."

---
{% api %}
# Ungültige Telefonnummern entfernen
{% apimethod post %}
/sms/invalid_phone_numbers/remove
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um "ungültige" Telefonnummern aus unserer Ungültigkeitsliste zu entfernen.

Damit können Sie Telefonnummern erneut validieren, nachdem sie als ungültig markiert wurden.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76495aac-8c2d-4e1a-8cac-12e3856ab1d3 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `sms.invalid_phone_numbers.remove`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "phone_numbers": (required, array of string in e.164 format)
}
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| ----------|-----------| ---------|------ |
| `phone_number` | Erforderlich | String-Array im Format e.164  | Eine Reihe von bis zu 50 Telefonnummern zum Ändern. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl --location --request POST 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "phone_numbers" : ["12183095514","14255551212"]
}'
```

{% endapi %}
