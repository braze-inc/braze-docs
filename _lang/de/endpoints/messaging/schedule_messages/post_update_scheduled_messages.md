---
nav_title: "POST: Update der geplanten Nachrichten"
article_title: "POST: Geplante Nachrichten aktualisieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Update geplanter Nachrichten Braze."

---
{% api %}
# Update der geplanten Nachrichten
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/nachrichten/zeitplan/update
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um geplante Nachrichten zu aktualisieren.

Dieser Endpunkt akzeptiert Updates entweder für den Parameter `schedule` oder `messages` oder für beide. Ihre Anfrage muss mindestens einen dieser beiden Schlüssel enthalten.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f61edf74-4467-4551-b9c4-a4b8d188cd7a {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `messages.schedule.update`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // optional, see create schedule documentation
  },
  "messages": {
    // optional, see available messaging objects documentation
  }
}
```
## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `schedule_id` | Erforderlich | String | Die zu aktualisierende `schedule_id` (erhalten aus der Antwort auf Zeitplan erstellen). |
|`schedule` | Optional | Objekt | Siehe [Zeitplan-Objekt]({{site.baseurl}}/api/objects_filters/schedule_object/). |
|`messages` | Optional | Objekt | Siehe [verfügbare Messaging-Objekte]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T20:30:36Z"
   },
  "messages": {
    "apple_push": {
      "alert": "Updated Message!",
      "badge": 1
    },
    "android_push": {
      "title": "Updated title!",
      "alert": "Updated message!"
    },
    "sms": {  
      "subscription_group_id": "subscription_group_identifier",
      "message_variation_id": "message_variation_identifier",
      "body": "This is my SMS body.",
      "app_id": "app_identifier"
    }
  }
}'
```

{% endapi %}
