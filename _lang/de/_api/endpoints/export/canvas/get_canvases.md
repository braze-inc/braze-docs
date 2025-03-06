---
nav_title: "GET: Leinwandliste exportieren"
article_title: "GET: Leinwandliste exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Export Canvas list Braze Endpunkt."

---
{% api %}
# Leinwandliste exportieren
{% apimethod get %}
/canvas/list
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste von Leinwänden zu exportieren, einschließlich des Namens, der Canvas-API-Kennung und der zugehörigen Tags.

Die Leinwände werden in Gruppen von 100 Stück zurückgegeben, sortiert nach Erstellungszeitpunkt (standardmäßig vom ältesten zum neuesten).

Archivierte Leinwände werden nicht in die API-Antwort aufgenommen, es sei denn, das Feld `include_archived` ist angegeben. Leinwände, die angehalten, aber nicht archiviert wurden, werden jedoch standardmäßig zurückgegeben.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `canvas.list`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | -------- | --------- | ----------- |
| `page` | Optional | Integer | Die Seite der zurückzugebenden Leinwände, Standardwert ist `0` (gibt den ersten Satz von bis zu 100 zurück) |
| `include_archived` | Optional | Boolesche | Ob archivierte Leinwände einbezogen werden sollen oder nicht, die Standardeinstellung ist `false`. |
| `sort_direction` | Optional | String | \- Sortieren Sie die Erstellungszeit von der neuesten zur ältesten: Geben Sie den Wert `desc` ein.<br> \- Sortieren Sie die Erstellungszeit von der ältesten zur neuesten: Geben Sie den Wert `asc` ein. <br><br>Wenn `sort_direction` nicht enthalten ist, ist die Standardreihenfolge die älteste nach der neuesten. |
| `last_edit.time[gt]` | Optional | Zeit | Filtert die Ergebnisse und gibt nur Leinwände zurück, die länger als die angegebene Zeit bearbeitet wurden. Das Format ist `yyyy-MM-DDTHH:mm:ss`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/list?page=1&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvases" : [
  	{
  		"id" : (string) the Canvas API identifier,
  		"last_edited": (ISO 8601 string) the last edited time for the message,
  		"name" : (string) the Canvas name,
  		"tags" : (array) the tag names associated with the Canvas formatted as strings,
  	},
    ... (more Canvases)
  ],
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

{% alert tip %}
Hilfe zum CSV- und API-Export finden Sie unter [Fehlerbehebung beim Exportieren]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
