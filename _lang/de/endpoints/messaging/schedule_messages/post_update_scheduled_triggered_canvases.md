---
nav_title: "POST: Aktualisieren Sie geplante, durch APIs getriggerte Canvase"
article_title: "POST: Geplante API-getriggerte Canvase aktualisieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des durch die API getriggerten Endpunkts Update scheduled Canvase Braze."

---
{% api %}
# Aktualisieren Sie geplante, durch APIs getriggerte Canvase
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/triggern/zeitplan/update
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um geplante, durch APIs getriggerte Canvase zu aktualisieren, die im Dashboard erstellt wurden.

So können Sie entscheiden, welche Aktion die zu versendende Nachricht triggern soll. Sie können `trigger_properties` übergeben, das als Template in die Nachricht selbst eingefügt wird.

Beachten Sie, dass Sie zum Versenden von Nachrichten über diesen Endpunkt eine Canvas ID benötigen, die Sie beim Erstellen eines [Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier) erstellt haben.

Jeder Zeitplan überschreibt den Zeitplan, den Sie in der Anfrage zum Erstellen von Zeitplänen oder in früheren Anfragen zum Update von Zeitplänen angegeben haben, vollständig.
  - Wenn Sie z.B. ursprünglich `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` angegeben haben und dann in Ihrem Update `"schedule" : {"time" : "2015-02-20T14:14:47"}` angeben, wird Ihre Nachricht jetzt zur angegebenen Zeit in UTC und nicht in der Ortszeit des Nutzers:in gesendet.
  - Geplante Trigger, die kurz vor oder während der Zeit, zu der sie gesendet werden sollten, aktualisiert werden, werden nach bestem Wissen und Gewissen aktualisiert, so dass Änderungen in letzter Sekunde auf alle, einige oder keinen Ihrer Nutzer:innen angewendet werden können.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8fdf158b-ce20-41d8-80e4-a9300a6706d4 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `canvas.trigger.schedule.update`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`canvas_id`|Erforderlich|String| Siehe [Canvas Bezeichner]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Optional | String | Die zu aktualisierende `schedule_id` (erhalten aus der Antwort auf Zeitplan erstellen). |
|`schedule` | Erforderlich | Objekt | Siehe [Zeitplan-Objekt]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}
