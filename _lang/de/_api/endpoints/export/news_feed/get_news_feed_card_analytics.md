---
nav_title: "GET: Exportieren Sie News Feed Card Analytics"
article_title: "GET: Exportieren Sie News Feed Card Analytics"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Export News Feed card analytics Braze Endpunkts."

---
{% api %}
# Exportieren Sie die Analyse der News Feed Karte
{% apimethod get %}
/feed/data_series
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine tägliche Reihe von Engagement-Statistiken für eine Karte im Laufe der Zeit abzurufen.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `feed.data_series`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter anfordern

| Parameter   | Erforderlich | Daten Typ | Beschreibung |
| ----------- | -------- | --------- | ----------- |
| `card_id` | Erforderlich | String | Siehe [Karten-API-Kennung]({{site.baseurl}}/api/identifier_types/). <br><br> Die `card_id` für eine bestimmte Karte finden Sie auf der Seite mit [den API-Schlüsseln]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) und auf der Seite mit den Kartendetails in Ihrem Dashboard, oder Sie können den [Endpunkt Exportieren der News Feed-Kartenliste]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/) verwenden.|
| `length` | Erforderlich | Integer | Maximale Anzahl der Einheiten (Tage oder Stunden) vor `ending_at`, die in die zurückgegebene Serie aufgenommen werden sollen. Muss zwischen 1 und 100 (einschließlich) liegen. |
| `unit` | Optional | String | Zeiteinheit zwischen Datenpunkten. Kann `day` oder `hour` sein, die Standardeinstellung ist `day`.  |
| `ending_at` | Optional | Datetime <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) Zeichenfolge) | Datum, an dem die Datenreihe enden soll. Standardmäßig wird die Zeit der Anfrage verwendet. |
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
Hilfe zum CSV- und API-Export finden Sie unter [Fehlerbehebung beim Exportieren]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
