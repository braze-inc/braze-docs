---
nav_title: "POST: Geplante API-getriggerte Kampagnen löschen"
article_title: "POST: Geplante API-getriggerte Kampagnen löschen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Details zum Braze-Endpunkt Geplante Kampagnen löschen, die über die API ausgelöst werden."

---
{% api %}
# Geplante API-ausgelöste Kampagnen löschen
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/schedule/delete
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Canvas-Nachricht abzubrechen, die Sie zuvor per API-Auslöser geplant haben, bevor sie gesendet wurde.

Geplante Nachrichten oder Auslöser, die kurz vor oder während des Zeitraums, in dem sie gesendet werden sollten, gelöscht werden, werden nach bestem Wissen und Gewissen aktualisiert, so dass Löschungen in letzter Sekunde alle, einige oder keinen Ihrer Zielbenutzer betreffen können.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `campaigns.trigger.schedule.delete`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Körper der Anfrage

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) the campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `campaign_id`| Erforderlich | String | Siehe [Kennung der Kampagne]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Erforderlich | String | Die zu löschende `schedule_id` (erhalten aus der Antwort auf Zeitplan erstellen). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}
