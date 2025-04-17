---
nav_title: "GET: Newsfeed-Kartenliste exportieren"
article_title: "GET: Newsfeed-Kartenliste exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details der Export Newsfeed-Kartenliste Braze Endpunkt."

---
{% api %}
# Newsfeed-Kartenliste exportieren
{% apimethod get %}
/feed/list
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste von Newsfeed-Karten zu exportieren, die jeweils ihren Namen und den API-Bezeichner der Karte enthalten.

Die Karten werden in Gruppen von 100 Karten zurückgegeben, sortiert nach dem Zeitpunkt der Erstellung (standardmäßig vom ältesten zum neuesten).

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9fa7a3bc-4a02-4de2-bc4c-8f111750665e {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `feed.list`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | -------- | --------- | ----------- |
| `page` | Optional | Integer   | Die Seite der zurückzugebenden Karten, Standardwert ist 0 (gibt den ersten Satz von bis zu 100 zurück). |
| `include_archived` | Optional | Boolesch   | Ob archivierte Karten einbezogen werden sollen oder nicht, Standardwert ist false. |
| `sort_direction` | Optional | String | \- Sortieren Sie die Erstellungszeit von der neuesten zur ältesten: Geben Sie den Wert `desc` ein.<br> \- Sortieren Sie die Erstellungszeit von der ältesten zur neuesten: Geben Sie den Wert `asc` ein. <br><br>Wenn `sort_direction` nicht enthalten ist, ist die Standardreihenfolge die älteste nach der neuesten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request GET 'https://rest.iad-01.braze.com/feed/list?page=1&include_archived=true&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "cards" : [
        {
            "id" : (string) the card API identifier,
            "type" : (string) type of the card - NewsItem (classic cards), CaptionedImage, Banner
            "title" : (string) the title of the card,
            "tags" : (array) the tag names associated with the card
        },
        ...
    ]
}
```

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
