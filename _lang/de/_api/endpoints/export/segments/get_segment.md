---
nav_title: "GET: Segmentliste exportieren"
article_title: "GET: Segmentliste exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Export der Segmentliste Braze Endpunkt."

---
{% api %}
# Segmentliste exportieren
{% apimethod get %}
/segments/list
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste von Segmenten zu exportieren, die jeweils den Namen, die Segment-API-Kennung und die Angabe enthalten, ob das analytische Tracking aktiviert ist.

Die Segmente werden in Gruppen von 100 zurückgegeben, sortiert nach dem Zeitpunkt der Erstellung (standardmäßig vom ältesten zum neuesten). Archivierte Segmente sind nicht enthalten.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `segments.list`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter anfordern

| Parameter| Erforderlich | Daten Typ | Beschreibung |
| -------- | -------- | --------- | ----------- |
| `page` | Optional | Integer | Die Seite der zurückzugebenden Segmente, Standardwert ist 0 (gibt den ersten Satz von bis zu 100 zurück). |
| `sort_direction` | Optional | String | \- Sortieren Sie die Erstellungszeit von der neuesten zur ältesten: Geben Sie den Wert `desc` ein.<br> \- Sortieren Sie die Erstellungszeit von der ältesten zur neuesten: Geben Sie den Wert `asc` ein. <br><br>Wenn `sort_direction` nicht enthalten ist, ist die Standardreihenfolge die älteste nach der neuesten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request GET 'https://rest.iad-01.braze.com/segments/list?page=1&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "segments" : [
        {
            "id" : (string) the Segment API identifier,
            "name" : (string) segment name,
            "analytics_tracking_enabled" : (boolean) whether the segment has analytics tracking enabled,
            "tags" : (array) the tag names associated with the segment formatted as strings
        },
        ...
    ]
}
```

{% alert tip %}
Hilfe zum CSV- und API-Export finden Sie unter [Fehlerbehebung beim Exportieren]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
