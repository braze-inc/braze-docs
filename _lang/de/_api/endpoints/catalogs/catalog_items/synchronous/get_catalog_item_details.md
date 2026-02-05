---
nav_title: "GET: Details zum Katalogartikel auflisten"
article_title: "GET: Liste Katalog Artikel Details"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts List catalog item details Braze."

---
{% api %}
# Details zum Katalogartikel auflisten
{% apimethod get %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen Katalogartikel und seinen Inhalt zurückzugeben.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#52c6631c-7366-48e5-9e0e-16de7b6285cc {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `catalogs.get_item`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Pfad-Parameter

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `catalog_name` | Erforderlich | String | Name des Katalogs. |
| `item_id` | Erforderlich | String | Die ID des Katalogartikels. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parameter der Anfrage

Für diesen Endpunkt gibt es keinen Anfragetext.

## Beispiel Anfrage

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

Für diesen Endpunkt gibt es zwei Status Code Antworten: `200` und `404`.

### Beispiel für eine erfolgreiche Antwort

Der Status Code `200` könnte den folgenden Antwortkörper zurückgeben.

```json
{
  "items": [
    {
      "id": "restaurant3",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-01T09:03:19.967Z"
    }
  ],
  "message": "success"
}
```

### Beispiel einer Fehlerantwort

Der Status Code `404` könnte die folgende Antwort liefern. Unter [Fehlerbehebung](#troubleshooting) finden Sie weitere Informationen zu Fehlern, die bei Ihnen auftreten können.

```json
{
  "errors": [
    {
      "id": "item-not-found",
      "message": "Could not find item",
      "parameters": [
        "item_id"
      ],
      "parameter_values": [
        "restaurant34"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Fehlersuche

In der folgenden Tabelle sind die möglichen zurückgegebenen Fehler und die dazugehörigen Schritte zur Fehlerbehebung aufgelistet, falls zutreffend.

| Fehler | Fehlersuche |
| --- | --- |
| `catalog-not-found` | Prüfen Sie, ob der Katalogname gültig ist. |
| `item-not-found` | Prüfen Sie, ob der Artikel im Katalog enthalten ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
