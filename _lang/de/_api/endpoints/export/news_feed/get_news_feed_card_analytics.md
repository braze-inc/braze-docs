---
nav_title: "GET: Exportieren von Newsfeed-Kartenanalysen"
article_title: "GET: Exportieren von Newsfeed-Kartenanalysen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Export Newsfeed card analytics Braze."

---
{% api %}
# Exportieren Sie Newsfeed-Kartenanalysen
{% apimethod get %}
/feed/data_series
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine tägliche Reihe von Statistiken über das Engagement einer Karte im Laufe der Zeit abzurufen.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `feed.data_series`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter   | Erforderlich | Datentyp | Beschreibung |
| ----------- | -------- | --------- | ----------- |
| `card_id` | Erforderlich | String | Siehe [Bezeichner der Karten-API]({{site.baseurl}}/api/identifier_types/). <br><br> Die `card_id` für eine bestimmte Karte finden Sie auf der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) und auf der Seite mit den Kartendetails in Ihrem Dashboard, oder Sie können den [Endpunkt Liste der Newsfeed-Karten exportieren]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/) verwenden.|
| `length` | Erforderlich | Integer | Maximale Anzahl der Einheiten (Tage oder Stunden) vor `ending_at`, die in die zurückgegebene Serie aufgenommen werden sollen. Muss zwischen 1 und 100 (einschließlich) liegen. |
| `unit` | Optional | String | Zeiteinheit zwischen Datenpunkten. Kann `day` oder `hour` sein, der Standard ist `day`.  |
| `ending_at` | Optional | Datetime <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) String) | Datum, an dem die Datenreihe enden soll. Standardmäßig wird die Zeit der Anfrage verwendet. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/feed/data_series?card_id={{card_identifier}}&length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00' \
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
            "clicks" : (int) the number of clicks,
            "impressions" : (int) the number of impressions,
            "unique_clicks" : (int) the number of unique clicks,
            "unique_impressions" : (int) the number of unique impressions
        },
        ...
    ]
}
```

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
