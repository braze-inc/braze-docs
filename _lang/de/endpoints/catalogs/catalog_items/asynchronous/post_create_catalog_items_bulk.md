---
nav_title: "POST: Mehrere Artikel im Katalog erstellen"
article_title: "POST: Mehrere Katalogartikel erstellen"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Mehrere Katalogartikel erstellen in Braze."

---
{% api %}
# Mehrere Artikel im Katalog erstellen
{% apimethod post %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um mehrere Artikel in Ihrem Katalog zu erstellen.

Jede Anfrage kann bis zu 50 Artikel enthalten. Dieser Endpunkt ist asynchron.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cea18bb3-b83a-4160-81fe-8cd42aa6e7cc {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `catalogs.add_items`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## Pfad-Parameter

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `catalog_name` | Erforderlich | String | Name des Katalogs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `items` | Erforderlich | Array | Ein Array, das Artikel-Objekte enthält. Die Artikelobjekte sollten alle Felder des Katalogs enthalten. Es sind bis zu 50 Artikel pro Anfrage zulässig. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Created_At": "2022-11-01T09:03:19.967+00:00"
    },
    {
      "id": "restaurant2",
      "Name": "Restaurant2",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 10,
      "Loyalty_Program": true,
      "Location": {
        "Latitude": 40.7413,
        "Longitude": -73.9764
      },
      "Top_Dishes": [
        "Hot Dog",
        "French Fries"
      ],
      "Created_At": "2022-11-02T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "Name": "Restaurant3",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 3,
      "Loyalty_Program": false,
      "Location": {
        "Latitude": 40.7489,
        "Longitude": -73.9972
      },
      "Top_Dishes": [
        "Buffalo Wings",
        "Philly Cheesesteak"
      ],
      "Created_At": "2022-11-03T09:03:19.967+00:00"
    }
  ]
}'
```

## Antwort

Es gibt drei Status Code Antworten für diesen Endpunkt: `202`, `400`, und `404`.

### Beispiel für eine erfolgreiche Antwort

Der Status Code `202` könnte den folgenden Antwortkörper zurückgeben.

```json
{
  "message": "success"
}
```

### Beispiel einer Fehlerantwort

Der Status Code `400` könnte den folgenden Antwortkörper zurückgeben. Unter [Fehlerbehebung](#troubleshooting) finden Sie weitere Informationen zu Fehlern, die bei Ihnen auftreten können.

```json
{
  "errors": [
    {
      "id": "invalid-fields",
      "message": "Some of the fields given do not exist in the catalog",
      "parameters": [
        "id"
      ],
      "parameter_values": [
        "restaurant1"
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
| `ids-not-strings` | Artikel IDs müssen vom Typ String sein. |
| `ids-not-unique` | Die IDs der Artikel müssen in der Anfrage eindeutig sein. |
| `ids-too-large` | Artikel IDs dürfen nicht mehr als 250 Zeichen lang sein. |
| `invalid-ids` | Artikel IDs dürfen nur Buchstaben, Zahlen, Bindestriche und Unterstriche enthalten. |
| `invalid-fields` | Stellen Sie sicher, dass alle Felder, die Sie in der API-Anfrage senden, bereits im Katalog vorhanden sind. Dies hat nichts mit dem in der Fehlermeldung erwähnten ID-Feld zu tun. |
| `invalid-keys-in-value-object` | Artikel-Objektschlüssel können nicht `.` oder `$` enthalten. |
| `item-array-invalid` | `items` muss ein Array von Objekten sein. |
| `items-missing-ids` | Einige Artikel haben keine IDs. Prüfen Sie, ob jeder Artikel eine ID hat. |
| `items-too-large` | Die Werte der Artikel dürfen nicht länger als 5.000 Zeichen sein. |
| `request-includes-too-many-items` | Ihre Anfrage enthält zu viele Artikel. Die Anzahl der Artikel pro Anfrage ist auf 50 begrenzt. |
| `too-deep-nesting-in-value-object` | Artikel-Objekte können nicht mehr als 50 Verschachtelungsebenen haben. |
| `unable-to-coerce-value` | Artikel-Typen können nicht umgewandelt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
