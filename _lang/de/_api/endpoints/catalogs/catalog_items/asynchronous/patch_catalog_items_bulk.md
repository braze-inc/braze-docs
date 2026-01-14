---
nav_title: "PATCH: Mehrere Katalogartikel bearbeiten"
article_title: "PATCH: Mehrere Katalogartikel bearbeiten"
alias: /catalogs_items_patch/
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Mehrere Katalogartikel bearbeiten in Braze."

---
{% api %}
# Mehrere Katalogartikel bearbeiten
{% apimethod patch %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um mehrere vorhandene Artikel in Ihrem Katalog zu bearbeiten.

Jede Anfrage kann bis zu 50 Artikel enthalten. Dieser Endpunkt ist asynchron.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#03f3548e-4139-4f60-812d-7e1a695a738a {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `catalogs.update_items`.

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
| `items` | Erforderlich | Array | Ein Array, das Artikel-Objekte enthält. Die Artikelobjekte sollten Felder enthalten, die im Katalog vorhanden sind. Es sind bis zu 50 Artikel pro Anfrage zulässig. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl --location --request PATCH 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
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
      "Top_Dishes": {
        "$add": [
          "Biscuits",
          "Coleslaw"
        ],
        "$remove": [
          "French Fries"
        ]
      },
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2,
      "Top_Dishes": [
        "Buffalo Wings",
        "Philly Cheesesteak"
      ]
    }
  ]
}'
```

{% alert note %}
Die Operatoren `$add` und `$remove` sind nur auf Felder vom Typ Array anwendbar und werden nur von PATCH-Endpunkten unterstützt.
{% endalert %}

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
| `ids-too-large` | Artikel IDs dürfen nicht mehr als 250 Zeichen lang sein. |
| `ids-not-strings` | Artikel IDs müssen vom Typ String sein. |
| `ids-not-unique` | Die IDs der Artikel müssen in der Anfrage eindeutig sein. |
| `invalid-ids` | Artikel IDs dürfen nur Buchstaben, Zahlen, Bindestriche und Unterstriche enthalten. |
| `invalid-fields` | Stellen Sie sicher, dass alle Felder, die Sie in der API-Anfrage senden, bereits im Katalog vorhanden sind. Dies hat nichts mit dem in der Fehlermeldung erwähnten ID-Feld zu tun. |
| `invalid-keys-in-value-object` | Artikel-Objektschlüssel können nicht `.` oder `$` enthalten. |
| `items-missing-ids` | Einige Artikel haben keine IDs. Prüfen Sie, ob jeder Artikel eine ID hat. |
| `item-array-invalid` | `items` muss ein Array von Objekten sein. |
| `items-too-large` | Die Werte der Artikel dürfen nicht länger als 5.000 Zeichen sein. |
| `request-includes-too-many-items` | Ihre Anfrage enthält zu viele Artikel. Die Anzahl der Artikel pro Anfrage ist auf 50 begrenzt. |
| `too-deep-nesting-in-value-object` | Artikel-Objekte können nicht mehr als 50 Verschachtelungsebenen haben. |
| `unable-to-coerce-value` | Artikel-Typen können nicht umgewandelt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
