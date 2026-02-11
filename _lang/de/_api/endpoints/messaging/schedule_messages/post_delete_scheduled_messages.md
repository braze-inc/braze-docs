---
nav_title: "POST: Geplante Nachrichten löschen"
article_title: "POST: Geplante Nachrichten löschen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt Löschen geplanter Nachrichten in Braze."

---
{% api %}
# Geplante Nachrichten löschen
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/nachrichten/zeitplan/loeschen
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Nachricht abzubrechen, die Sie zuvor im Zeitplan vorgesehen haben, bevor sie gesendet wurde.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5e89355c-0a5d-4d8b-8d89-2fd99bac36b0 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `messages.schedule.delete`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `schedule_id` | Erforderlich | String | Die `schedule_id` zum Löschen (erhalten aus der Antwort auf den Zeitplan erstellen). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}
