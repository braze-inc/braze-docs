---
nav_title: "GET: Liste der Kampagnen exportieren"
article_title: "GET: Liste der Kampagnen exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt Kampagnen-Liste exportieren Braze."

---
{% api %}
# Liste der Kampagnen exportieren
{% apimethod get %}
/kampagnen/liste
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste von Kampagnen zu exportieren, die jeweils den Namen, den API-Bezeichner der Kampagne, die Angabe, ob es sich um eine API-Kampagne handelt, und die mit der Kampagne verbundenen Tags enthält.

Die Kampagnen werden in 100er-Gruppen zurückgegeben, sortiert nach Erstellungszeitpunkt (standardmäßig vom ältesten zum neuesten).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `campaigns.list`.

## Rate-Limits

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | -------- | --------- | ----------- |
| `page` | Optional | Integer | Die Seite der zurückzugebenden Kampagnen, Standard ist 0 (gibt den ersten Satz von bis zu 100 zurück). |
| `include_archived` | Optional | Boolesch | Ob archivierte Kampagnen einbezogen werden sollen oder nicht, Standardwert ist false. |
| `sort_direction` | Optional | String | \- Sortieren Sie die Erstellungszeit von der neuesten zur ältesten: Geben Sie den Wert `desc` ein.<br> \- Sortieren Sie die Erstellungszeit von der ältesten zur neuesten: Geben Sie den Wert `asc` ein. <br><br>Wenn `sort_direction` nicht enthalten ist, ist die Standardreihenfolge die älteste nach der neuesten. |
| `last_edit.time[gt]` | Optional | Uhrzeit | Filtert die Ergebnisse und gibt nur Kampagnen zurück, die länger als die angegebene Zeit bearbeitet wurden. Das Format ist `yyyy-MM-DDTHH:mm:ss`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/list?page=0&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "campaigns" : [
        {
            "id" : (string) the Campaign API identifier,
            "last_edited": (ISO 8601 string) the last edited time for the message
            "name" : (string) the campaign name,
            "is_api_campaign" : (boolean) whether the campaign is an API campaign,
            "tags" : (array) the tag names associated with the campaign formatted as strings
        },
        ...
    ]
}
```

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
