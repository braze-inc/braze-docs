---
nav_title: "PUT: Ersetzen Sie mehrere Artikel im Katalog"
article_title: "PUT: Mehrere Katalogartikel ersetzen"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Ersetzen mehrerer Artikel in Braze."

---
{% api %}
# Katalogartikel ersetzen
{% apimethod put %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um mehrere Artikel in Ihrem Katalog zu ersetzen.

Wenn ein Artikel im Katalog nicht vorhanden ist, wird dieser Endpunkt den Artikel in Ihrem Katalog erstellen. Jede Anfrage kann bis zu 50 Artikel aus dem Katalog unterstützen. Dieser Endpunkt ist asynchron.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#ab30a4fc-60bc-4460-885c-1b92af8bc061 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `catalogs.replace_items`.

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
| `items` | Erforderlich | Array | Ein Array, das Artikel-Objekte enthält. Jedes Objekt muss eine ID haben. Die Artikelobjekte sollten Felder enthalten, die im Katalog vorhanden sind. Es sind bis zu 50 Artikel pro Anfrage zulässig. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2,
      "Top_Dishes": [
        "Hot Dog",
        "French Fries"
      ]
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
| `ids-not-string` | Bestätigen Sie, dass jede Artikel ID ein String ist. |
| `ids-not-unique` | Prüfen Sie, ob jede Artikel ID eindeutig ist. |
| `ids-too-large` | Die Zeichenbegrenzung für jede Artikel ID beträgt 250 Zeichen. |
| `item-array-invalid` | `items` muss ein Array von Objekten sein. |
| `items-missing-ids` | Einige Artikel haben keine IDs. Bestätigen Sie, dass jeder Artikel eine ID hat. |
| `items-too-large` | Die Werte der Artikel dürfen nicht länger als 5.000 Zeichen sein. |
| `invalid-ids` | Unterstützte Zeichen für Artikel ID Namen sind Buchstaben, Zahlen, Bindestriche und Unterstriche. |
| `invalid-fields` | Stellen Sie sicher, dass alle Felder, die Sie in der API-Anfrage senden, bereits im Katalog vorhanden sind. Dies hat nichts mit dem in der Fehlermeldung erwähnten ID-Feld zu tun. |
| `invalid-keys-in-value-object` | Artikel-Objektschlüssel können nicht `.` oder `$` enthalten. |
| `too-deep-nesting-in-value-object` | Artikel-Objekte können nicht mehr als 50 Verschachtelungsebenen haben. |
| `request-includes-too-many-items` | Ihre Anfrage enthält zu viele Artikel. Die Anzahl der Artikel pro Anfrage ist auf 50 begrenzt. |
| `unable-to-coerce-value` | Artikel-Typen können nicht umgewandelt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
