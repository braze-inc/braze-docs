---
nav_title: "GET: Newsfeed-Kartendetails exportieren"
article_title: "GET: Newsfeed-Kartendetails exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Export Newsfeed-Karte Details Braze."

---
{% api %}
# Newsfeed-Kartendetails exportieren
{% apimethod get %}
/feed/details
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um relevante Informationen über eine Karte abzurufen, die durch den Bezeichner `card_id` identifiziert werden kann.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5b1401a6-f12c-4827-82c9-8dc604f1671e {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `feed.details`.

## Rate-Limits

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter | Erforderlich | Daten Typ | Beschreibung            |
| --------- | -------- | --------- | ---------------------- |
| `card_id` | Erforderlich | String | Siehe [Bezeichner der Karten-API]({{site.baseurl}}/api/identifier_types/). <br><br> Die `card_id` für eine bestimmte Karte finden Sie auf der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) und auf der Seite mit den Kartendetails in Ihrem Dashboard, oder Sie können den [Endpunkt Liste der Newsfeed-Karten exportieren]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/) verwenden.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/feed/details?card_id={{card_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) The status of the export, returns 'success' when completed without errors,
    "created_at" : (string) the ate created as ISO 8601 date,
    "updated_at" : (string) the ate last updated as ISO 8601 date,
    "name" : (string) the card name,
    "publish_at" : (string) the date the card was published as ISO 8601 date,
    "end_at" : (string) the date the card will stop displaying for users as ISO 8601 date,
    "tags" : (array) the tag names associated with the card,
    "title" : (string) the title of the card,
    "image_url" : (string) the image URL used by this card,
    "extras" : (dictionary) a dictionary containing key-value pair data attached to this card,
    "description" : (string) the description text used by this card,
    "archived": (boolean) whether this Card is archived,
    "draft": (boolean) whether this Card is a draft,
}
```

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
