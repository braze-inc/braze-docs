---
nav_title: "GET: Details zu mehreren Artikeln im Katalog auflisten"
article_title: "GET: Mehrere Katalogartikel auflisten Details"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts List multiple catalog item details Braze."

---
{% api %}
# Details zu mehreren Artikeln im Katalog auflisten
{% apimethod get %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um mehrere Katalogartikel und deren Inhalt zurückzugeben.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#63a19dd5-10e0-4649-bdf0-097216748bbb {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `catalogs.get_items`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Pfad-Parameter

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `catalog_name` | Erforderlich | String | Name des Katalogs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Abfrageparameter

Beachten Sie, dass jeder Aufruf dieses Endpunkts 50 Artikel zurückgibt. Bei einem Katalog mit mehr als 50 Artikeln verwenden Sie die Kopfzeile `Link`, um die Daten auf der nächsten Seite abzurufen, wie in der folgenden Beispielantwort gezeigt.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `cursor` | Optional | String | Bestimmt die Paginierung der Katalogartikel. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parameter der Anfrage

Für diesen Endpunkt gibt es keinen Anfragetext.

## Beispiel-Anfragen

### Ohne Cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Mit Cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

Es gibt drei Status Code Antworten für diesen Endpunkt: `200`, `400`, und `404`.

### Beispiel für eine erfolgreiche Antwort

Der Status Code `200` könnte den folgenden Response Header und Body zurückgeben.

{% alert note %}
Die Kopfzeile `Link` ist nicht vorhanden, wenn der Katalog weniger als oder gleich 50 Artikel enthält. Bei Anrufen ohne Cursor wird `prev` nicht angezeigt. Wenn Sie sich die letzte Seite der Artikel ansehen, wird `next` nicht angezeigt.
{% endalert %}

```
Link: </catalogs/all_restaurants/items?cursor=c2tpcDow>; rel="prev",</catalogs/all_restaurants/items?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    },
    {
      "id": "restaurant2",
      "Name": "Restaurant2",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 10,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    },
    {
      "id": "restaurant3",
      "Name": "Restaurant3",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": false,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    }
  ],
  "message": "success"
}
```

### Beispiel einer Fehlerantwort

Der Status Code `400` könnte den folgenden Antwortkörper zurückgeben. Unter [Fehlerbehebung](#troubleshooting) finden Sie weitere Informationen zu Fehlern, die bei Ihnen auftreten können.

```json
{
  "errors": [
    {
      "id": "invalid-cursor",
      "message": "'cursor' is not valid",
      "parameters": [
        "cursor"
      ],
      "parameter_values": [
        "bad-cursor"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Fehlersuche

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehler | Fehlersuche |
| --- | --- |
| `catalog-not-found` | Prüfen Sie, ob der Katalogname gültig ist. |
| `invalid-cursor` | Prüfen Sie, ob Ihre `cursor` gültig ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
