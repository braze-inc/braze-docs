---
nav_title: "POST: Aktualisieren Sie geplante, durch APIs getriggerte Kampagnen"
article_title: "POST: Geplante API-getriggerte Kampagnen aktualisieren"
search_tag: Endpoint
page_order: 4
layout: api_page
description: "Dieser Artikel beschreibt die Details des Endpunkts Update geplanter Kampagnen, die durch APIs getriggert werden, von Braze."

---
{% api %}
# Aktualisieren Sie geplante, durch APIs getriggerte Kampagnen
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/kampagnen/ausloesen/zeitplan/update
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um geplante Kampagnen mit API-Auslösung zu aktualisieren, die im Dashboard erstellt wurden. So können Sie entscheiden, welche Aktion den Versand der Nachricht triggern soll.

Sie können `trigger_properties` übergeben, das als Template in die Nachricht selbst eingefügt wird.

Beachten Sie, dass Sie zum Versenden von Nachrichten mit diesem Endpunkt eine ID für die Kampagne benötigen, die Sie beim Erstellen einer [API-getriggerten Kampagne]({{site.baseurl}}/api/api_campaigns/) erstellt haben.

Jeder Zeitplan überschreibt den Zeitplan, den Sie in der Anfrage zum Erstellen des Zeitplans oder in früheren Anfragen zum Update des Zeitplans angegeben haben, vollständig. Wenn Sie den Zeitplan beispielsweise ursprünglich auf `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` eingestellt haben und ihn später auf `"schedule" : {"time" : "2015-02-20T14:14:47"}` aktualisieren, wird die Nachricht nun zur angegebenen Zeit in UTC und nicht in der Ortszeit des Nutzers:in gesendet.

Geplante Trigger, die kurz vor oder während der Zeit, zu der sie gesendet werden sollten, aktualisiert werden, werden nach bestem Wissen und Gewissen aktualisiert, so dass Änderungen in letzter Sekunde auf alle, einige oder keinen Ihrer Nutzer:innen angewendet werden können. Updates werden nicht übernommen, wenn der ursprüngliche Zeitplan die Ortszeit verwendete und die ursprüngliche Zeit in einer beliebigen Zeitzone bereits vergangen ist.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d2a6e66-9d6f-4ae1-965a-79fa52b86b1d {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `campaigns.trigger.schedule.update`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Erforderlich|String| Siehe [Bezeichner der Kampagne]({{site.baseurl}}/api/identifier_types/)|
| `schedule_id` | Erforderlich | String | Die zu aktualisierende `schedule_id` (erhalten aus der Antwort zum Erstellen eines Zeitplans). |
|`schedule` | Erforderlich | Objekt | Siehe [Zeitplan-Objekt]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}
