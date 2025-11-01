---
nav_title: "POST: Löschen Sie geplante, durch APIs getriggerte Canvase"
article_title: "POST: Geplante, API-getriggerte Canvase löschen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des durch APIs getriggerten Endpunkts Canvase Braze mit Zeitplan löschen."

---
{% api %}
# Löschen Sie geplante, durch APIs getriggerte Canvase
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/triggern/zeitplan/loeschen
{% endapimethod %}

> Mit dem Endpunkt Zeitplan löschen können Sie eine Nachricht stornieren, die Sie zuvor mit API-getriggerten Canvase geplant haben, bevor sie versendet wurde.

Geplante Nachrichten oder Trigger, die kurz vor oder während der Zeit, zu der sie gesendet werden sollten, gelöscht werden, werden nach bestem Wissen und Gewissen aktualisiert, so dass Löschungen in letzter Sekunde für alle, einige oder keinen Ihrer Targeting Nutzer:innen vorgenommen werden können.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `canvas.trigger.schedule.delete`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) the Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `canvas_id`| Erforderlich | String | Siehe [Canvas Bezeichner]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Erforderlich | String | Die `schedule_id` zum Löschen (erhalten aus der Antwort auf den Zeitplan erstellen). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}
