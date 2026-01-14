---
nav_title: "GET: Exportieren Sie angepasste Events Analytics"
article_title: "GET: Exportieren Sie angepasste Event Analytics"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt Export angepasster Events Analytics Braze."

---
{% api %}
# Exportieren Sie angepasste Events Analytics
{% apimethod get %}
/ereignisse/daten_serien
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Reihe von Vorkommen eines angepassten Events in Ihrer App über einen bestimmten Zeitraum abzurufen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `events.data_series`.

## Rate-Limits

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter| Erforderlich | Datentyp | Beschreibung |
| -------- | -------- | --------- | ----------- |
| `event` | Erforderlich | String | Der Name des angepassten Events, für das Analytics zurückgegeben werden soll. |
| `length` | Erforderlich | Integer | Maximale Anzahl der Einheiten (Tage oder Stunden) vor `ending_at`, die in die zurückgegebene Serie aufgenommen werden sollen. Muss zwischen 1 und 100 (einschließlich) liegen. |
| `unit` | Optional | String | Zeiteinheit zwischen Datenpunkten. Kann `day` oder `hour` sein, der Standard ist `day`.  |
| `ending_at` | Optional | Datetime <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) String) | Datum, an dem die Datenreihe enden soll. Standardmäßig wird die Zeit der Anfrage verwendet. |
| `app_id` | Optional | String | Bezeichner der App-API, der von der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) abgerufen wird, um Analytics auf eine bestimmte App zu beschränken. |
| `segment_id` | Optional | String | Siehe [Segment API Bezeichner]({{site.baseurl}}/api/identifier_types/). Segment ID, die das analytics-aktivierte Segment angibt, für das Event Analytics zurückgegeben werden soll. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Beispiel Anfrage
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/events/data_series?event=event_name&length=24&unit=hour&ending_at=2014-12-10T23:59:59-05:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) the point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "count" : (int) the number of occurrences of provided custom event
        },
        ...
    ]
}
```

### Schwerwiegende Fehler Antwortcodes {#fatal-export}

Für Statuscodes und zugehörige Nachrichten, die zurückgegeben werden, wenn Ihre Anfrage auf einen schwerwiegenden Fehler stößt, referenzieren Sie [Schwerwiegende Fehler & Antworten.]({{site.baseurl}}/api/errors/#fatal-errors)

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
