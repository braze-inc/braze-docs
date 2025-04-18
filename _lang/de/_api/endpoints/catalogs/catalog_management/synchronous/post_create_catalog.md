---
nav_title: "POST: Katalog erstellen"
article_title: "POST: Katalog erstellen"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten zum Endpunkt Katalog erstellen Braze."

---
{% api %}
# Katalog erstellen
{% apimethod post %}
/Kataloge
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen Katalog zu erstellen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#af9f3e2d-b7e7-49e7-aa64-f4652892be6e {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `catalogs.create`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `catalogs` | Erforderlich | Array | Ein Array, das Katalogobjekte enthält. Für diese Anfrage ist nur ein Katalogobjekt zulässig. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Katalogobjekt-Parameter

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `name` | Erforderlich | String | Der Name des Katalogs, den Sie erstellen möchten. |
| `description` | Erforderlich | String | Die Beschreibung des Katalogs, den Sie erstellen möchten. |
| `fields` | Erforderlich | Array | Ein Array von Objekten, wobei das Objekt die Schlüssel `name` und `type` enthält. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "catalogs": [
    {
      "name": "restaurants",
      "description": "My Restaurants",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "Name",
          "type": "string"
        },
        {
          "name": "City",
          "type": "string"
        },
        {
          "name": "Cuisine",
          "type": "string"
        },
        {
          "name": "Rating",
          "type": "number"
        },
        {
          "name": "Loyalty_Program",
          "type": "boolean"
        },
        {
          "name": "Location",
          "type": "object"
        },
        {
          "name": "Top_Dishes",
          "type": "array"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ]
    }
  ]
}'
```

## Antwort

Für diesen Endpunkt gibt es zwei Status Code Antworten: `201` und `400`.

### Beispiel für eine erfolgreiche Antwort

Der Status Code `201` könnte den folgenden Antwortkörper zurückgeben.

```json
{
  "catalogs": [
    {
      "description": "My Restaurants",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "Name",
          "type": "string"
        },
        {
          "name": "City",
          "type": "string"
        },
        {
          "name": "Cuisine",
          "type": "string"
        },
        {
          "name": "Rating",
          "type": "number"
        },
        {
          "name": "Loyalty_Program",
          "type": "boolean"
        },
        {
          "name": "Location",
          "type": "object"
        },
        {
          "name": "Top_Dishes",
          "type": "array"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ],
      "name": "restaurants",
      "num_items": 0,
      "updated_at": "2022-11-02T20:04:06.879+00:00"
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
      "id": "catalog-name-already-exists",
      "message": "A catalog with that name already exists",
      "parameters": [
        "name"
      ],
      "parameter_values": [
        "restaurants"
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
| `catalog-array-invalid` | `catalogs` muss ein Array von Objekten sein. |
| `catalog-name-already-exists` | Katalog mit diesem Namen existiert bereits. |
| `catalog-name-too-large`  | Das Zeichenlimit für einen Katalognamen beträgt 250. |
| `description-too-long` | Das Zeichenlimit für die Beschreibung beträgt 250. |
| `field-names-not-unique` | Derselbe Feldname wird zweimal referenziert. |
| `field-names-too-large` | Das Zeichenlimit für einen Feldnamen beträgt 250. |
| `id-not-first-column` | Die `id` muss das erste Feld im Array sein. Prüfen Sie, ob der Typ ein String ist. |
| `invalid-catalog-name` | Der Katalogname darf nur Buchstaben, Zahlen, Bindestriche und Unterstriche enthalten. |
| `invalid-field-names` | Felder können nur Buchstaben, Zahlen, Bindestriche und Unterstriche enthalten. |
| `invalid-field-types` | Stellen Sie sicher, dass die Feldtypen gültig sind. |
| `invalid-fields` | `fields` ist nicht korrekt formatiert. |
| `too-many-catalog-atoms` | Sie können nur einen Katalog pro Anfrage erstellen. |
| `too-many-fields` | Die Anzahl der Felder ist auf 500 begrenzt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
