---
nav_title: "GET: Liste der anstehenden geplanten Kampagnen und Canvase"
article_title: "GET: Liste geplanter Kampagnen und Canvase"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten über den Endpunkt Liste der geplanten Kampagnen und Canvase Braze."

---
{% api %}
# Liste der anstehenden geplanten Kampagnen und Canvase
{% apimethod get %}
/messages/scheduled_broadcasts
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine JSON-Liste mit Informationen über geplante Kampagnen und Eingänge Canvase zwischen jetzt und einem in der Anfrage angegebenen `end_time` zurückzugeben.

Tägliche, wiederkehrende Nachrichten erscheinen nur einmal bei ihrem nächsten Vorkommen. Die über diesen Endpunkt zurückgegebenen Ergebnisse umfassen Kampagnen und Canvase, die im Braze-Dashboard erstellt und geplant wurden.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6f623cc3-383b-4bf7-b14d-7c56fc5562f5 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `messages.schedule_broadcasts`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | -------- | --------- | ----------- |
| `end_time` | Erforderlich | String im [ISO-8601-Format](https://en.wikipedia.org/wiki/ISO_8601)  | Enddatum des Bereichs zum Abrufen der nächsten geplanten Kampagnen und Canvase. Dies wird von der API als Mitternacht in UTC-Zeit behandelt. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2018-09-01T00:00:00-04:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "scheduled_broadcasts": [
    {
      "name": (string) the name of the scheduled broadcast,
      "id": (stings) the Canvas or campaign identifier,
      "type": (string) the broadcast type either Canvas or Campaign,
      "tags": (array) an array of tag names formatted as strings,
      "next_send_time": (string) The next send time formatted in ISO 8601, may also include time zone if not local/intelligent delivery,
      "schedule_type": (string) The schedule type, either local_time_zones, intelligent_delivery or the name of your company's time zone,
    },
  ]
}
```

{% endapi %}
