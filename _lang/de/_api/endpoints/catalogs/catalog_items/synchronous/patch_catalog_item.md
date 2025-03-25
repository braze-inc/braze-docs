---
nav_title: "PATCH: Katalogartikel bearbeiten"
article_title: "PATCH: Katalogartikel bearbeiten"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt Katalogartikel bearbeiten von Braze."

---
{% api %}
# Katalogartikel bearbeiten
{% apimethod patch %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen bestehenden Artikel in Ihrem Katalog zu bearbeiten.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e35976ae-ff77-42b7-b691-a883c980d8c0 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `catalogs.update_item`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Pfad-Parameter

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| `catalog_name` | Erforderlich | String | Name des Katalogs. |
| `item_id` | Erforderlich | String | Die ID des Katalogartikels. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| `items` | Erforderlich | Array | Ein Array, das Artikelobjekte enthält. Die Artikelobjekte sollten Felder enthalten, die im Katalog vorhanden sind, außer dem Feld `id`. Pro Anfrage ist nur ein Artikelobjekt zulässig. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl --location --request PATCH 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
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
    }
  ]
}'
```

{% alert note %}
Die Operatoren `$add` und `$remove` sind nur auf Felder vom Typ Array anwendbar und werden nur von PATCH-Endpunkten unterstützt.
{% endalert %}

## Antwort

Es gibt drei Statuscode-Antworten für diesen Endpunkt: `200`, `400`, und `404`.

### Beispiel für eine erfolgreiche Antwort

Der Statuscode `200` könnte den folgenden Antwortkörper zurückgeben.

```json
{
  "message": "success"
}
```

### Beispiel einer Fehlerantwort

Der Statuscode `400` könnte den folgenden Antwortkörper zurückgeben. Weitere Informationen zu Fehlern, die auftreten können, finden Sie unter [Fehlersuche](#troubleshooting).

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
| `filtered-set-field-too-long` | Der Feldwert wird in einem gefilterten Satz verwendet, der die Zeichengrenze für ein Element überschreitet. |
| `id-in-body` | Eine Artikel-ID existiert bereits im Katalog. |
| `ids-too-large` | Die Zeichenbegrenzung für jede Artikel-ID beträgt 250 Zeichen. |
| `invalid-ids` | Unterstützte Zeichen für Artikel-ID-Namen sind Buchstaben, Zahlen, Bindestriche und Unterstriche. |
| `invalid-fields` | Bestätigen Sie, dass die Felder in der Anfrage im Katalog vorhanden sind. |
| `invalid-keys-in-value-object` | Die Objektschlüssel können nicht `.` oder `$` enthalten. |
| `item-not-found` | Überprüfen Sie, ob der Artikel im Katalog enthalten ist. |
| `item-array-invalid` | `items` muss ein Array von Objekten sein. |
| `items-too-large` | Das Zeichenlimit für jeden Artikel beträgt 5.000 Zeichen. |
| `request-includes-too-many-items` | Sie können nur einen Katalogartikel pro Anfrage bearbeiten. |
| `too-deep-nesting-in-value-object` | Objektobjekte können nicht mehr als 50 Verschachtelungsebenen haben. |
| `unable-to-coerce-value` | Gegenstandstypen können nicht umgewandelt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
