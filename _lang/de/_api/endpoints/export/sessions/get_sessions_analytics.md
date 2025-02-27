---
nav_title: "GET: App-Sitzungen nach Zeit exportieren"
article_title: "Holen Sie sich: App-Sitzungen nach Zeit exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten über die Analyse von App-Sitzungen nach Zeit Braze Endpunkt exportieren."

---
{% api %}
# App-Sitzung nach Zeit exportieren
{% apimethod get %}
/sessions/data_series
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Reihe von Sitzungen für Ihre App über einen bestimmten Zeitraum abzurufen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#79efb6a9-62ec-4b8a-bf4a-e96313aa4be1 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `sessions.data_series`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter anfordern

| Parameter| Erforderlich | Daten Typ | Beschreibung |
| -------- | -------- | --------- | ----------- |
| `length` | Erforderlich | Integer | Maximale Anzahl der Einheiten (Tage oder Stunden) vor `ending_at`, die in die zurückgegebene Serie aufgenommen werden sollen. Muss zwischen 1 und 100 (einschließlich) liegen. |
| `unit` | Optional | String | Zeiteinheit zwischen Datenpunkten. Kann `day` oder `hour` sein, die Standardeinstellung ist `day`.  |
| `ending_at` | Optional | Datetime <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) Zeichenfolge) | Datum, an dem die Datenreihe enden soll. Standardmäßig wird die Zeit der Anfrage verwendet. |
| `app_id` | Optional | String | App-API-Kennung, die von der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) abgerufen wird, um Analysen auf eine bestimmte App zu beschränken. |
| `segment_id` | Optional | String | Siehe [Segment-API-Bezeichner]({{site.baseurl}}/api/identifier_types/). Segment-ID, die das analytikfähige Segment angibt, für das Sitzungen zurückgegeben werden sollen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/sessions/data_series?length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
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
            "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "sessions" : (int)
        },
        ...
    ]
}
```

{% alert tip %}
Hilfe zum CSV- und API-Export finden Sie unter [Fehlerbehebung beim Exportieren]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
