---
nav_title: "POST: Katalogartikel erstellen"
article_title: "POST: Katalogartikel erstellen"
search_tag: Endpoint
page_order: 5

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Katalogartikel erstellen Braze."

---
{% api %}
# Katalogartikel erstellen
{% apimethod post %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen Artikel in Ihrem Katalog zu erstellen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#820c305b-ea6a-4b71-811a-55003a212a40 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `catalogs.create_item`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Pfad-Parameter

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `catalog_name` | Erforderlich | String | Name des Katalogs. |
| `item_id` | Erforderlich | String | Die ID des Katalogartikels. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `items` | Erforderlich | Array | Ein Array, das Artikel-Objekte enthält. Die Artikelobjekte sollten alle Felder des Katalogs mit Ausnahme des Feldes `id` enthalten. Pro Anfrage ist nur ein Artikel-Objekt zulässig. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
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
    }
  ]
}'
```

## Antwort

Es gibt drei Status Code Antworten für diesen Endpunkt: `201`, `400`, und `404`.

### Beispiel für eine erfolgreiche Antwort

Der Status Code `201` könnte den folgenden Antwortkörper zurückgeben.

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
| `arbitrary-error` | Es ist ein willkürlicher Fehler aufgetreten. Bitte versuchen Sie es erneut oder kontaktieren Sie den [Support]({{site.baseurl}}/support_contact/). |
| `catalog-not-found` | Prüfen Sie, ob der Katalogname gültig ist. |
| `filtered-set-field-too-long` | Der Feldwert wird in einer gefilterten Menge verwendet, die die Zeichengrenze für einen Artikel überschreitet. |
| `id-in-body` | Entfernen Sie alle IDs von Artikeln im Körper der Anfrage. |
| `ids-too-large` | Die Zeichenbegrenzung für jede Artikel ID beträgt 250 Zeichen. |
| `invalid-ids` | Unterstützte Zeichen für Artikel ID Namen sind Buchstaben, Zahlen, Bindestriche und Unterstriche. |
| `invalid-fields` | Stellen Sie sicher, dass alle Felder, die Sie in der API-Anfrage senden, bereits im Katalog vorhanden sind. Dies hat nichts mit dem in der Fehlermeldung erwähnten ID-Feld zu tun. |
| `invalid-keys-in-value-object` | Artikel-Objektschlüssel können nicht `.` oder `$` enthalten. |
| `item-already-exists` | Der Artikel ist bereits im Katalog vorhanden. |
| `item-array-invalid` | `items` muss ein Array von Objekten sein. |
| `items-too-large` | Das Zeichenlimit für jeden Artikel beträgt 5.000 Zeichen. |
| `request-includes-too-many-items` | Sie können pro Anfrage nur einen Artikel im Katalog erstellen. |
| `too-deep-nesting-in-value-object` | Artikel-Objekte können nicht mehr als 50 Verschachtelungsebenen haben. |
| `unable-to-coerce-value` | Artikel-Typen können nicht umgewandelt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
