---
nav_title: "POST: Geplante API-getriggerte Canvases aktualisieren"
article_title: "POST: Geplante API-getriggerte Canvases aktualisieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten zum API-gesteuerten Canvases Braze-Endpunkt Update scheduled."

---
{% api %}
# Geplante API-ausgelöste Canvases aktualisieren
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/update
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um geplante API-ausgelöste Canvases zu aktualisieren, die im Dashboard erstellt wurden.

So können Sie entscheiden, welche Aktion das Versenden der Nachricht auslösen soll. Sie können `trigger_properties` übergeben, das als Vorlage in die Nachricht selbst eingefügt wird.

Beachten Sie, dass Sie zum Senden von Nachrichten mit diesem Endpunkt eine Canvas-ID benötigen, die Sie beim Erstellen eines [Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier) erstellt haben.

Jeder Zeitplan überschreibt den Zeitplan, den Sie in der Anfrage zum Erstellen eines Zeitplans oder in früheren Anfragen zum Aktualisieren eines Zeitplans angegeben haben, vollständig.
  - Wenn Sie z.B. ursprünglich `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` angegeben haben und dann in Ihrer Aktualisierung `"schedule" : {"time" : "2015-02-20T14:14:47"}` angeben, wird Ihre Nachricht jetzt zur angegebenen Zeit in UTC und nicht in der Ortszeit des Benutzers gesendet.
  - Geplante Auslöser, die kurz vor oder während der Zeit, zu der sie gesendet werden sollten, aktualisiert werden, werden so gut wie möglich aktualisiert, so dass Änderungen in letzter Sekunde auf alle, einige oder keinen Ihrer Zielbenutzer angewendet werden können.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8fdf158b-ce20-41d8-80e4-a9300a6706d4 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `canvas.trigger.schedule.update`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Körper der Anfrage

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

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`canvas_id`|Erforderlich|String| Siehe [Canvas-Kennung]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Optional | String | Die zu aktualisierende `schedule_id` (erhalten aus der Antwort auf Zeitplan erstellen). |
|`schedule` | Erforderlich | Objekt | Siehe [Schedule-Objekt]({{site.baseurl}}/api/objects_filters/schedule_object/). |
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
