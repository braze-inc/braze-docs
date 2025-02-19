---
nav_title: "PUT: Katalogartikel aktualisieren"
article_title: "PUT: Katalogartikel aktualisieren"
search_tag: Endpoint
page_order: 6

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt Update catalog item Braze."

---
{% api %}
# Katalogartikel aktualisieren
{% apimethod put %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen Artikel in Ihrem Katalog zu aktualisieren.

Wenn der `item_id` nicht gefunden wird, erstellt dieser Endpunkt den Artikel in Ihrem Katalog. Dieser Endpunkt ist synchron.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b2871ed7-734e-4a37-b8f1-e11584e569f5 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `catalogs.replace_item`.

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
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
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
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    }
  ]
}'
```

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
| `id-in-body` | Entfernen Sie alle Artikel-IDs im Text der Anfrage. |
| `ids-too-large` | Die Zeichenbegrenzung für jede Artikel-ID beträgt 250 Zeichen. |
| `invalid-ids` | Unterstützte Zeichen für Artikel-ID-Namen sind Buchstaben, Zahlen, Bindestriche und Unterstriche. |
| `invalid-fields` | Stellen Sie sicher, dass alle Felder, die Sie in der API-Anfrage senden, bereits im Katalog vorhanden sind. Dies hat nichts mit dem in der Fehlermeldung erwähnten ID-Feld zu tun. |
| `invalid-keys-in-value-object` | Die Objektschlüssel können nicht `.` oder `$` enthalten. |
| `item-already-exists` | Der Artikel ist bereits im Katalog vorhanden. |
| `item-array-invalid` | `items` muss ein Array von Objekten sein. |
| `items-too-large` | Das Zeichenlimit für jeden Artikel beträgt 5.000 Zeichen. |
| `request-includes-too-many-items` | Sie können nur einen Katalogartikel pro Anfrage erstellen. |
| `too-deep-nesting-in-value-object` | Objektobjekte können nicht mehr als 50 Verschachtelungsebenen haben. |
| `unable-to-coerce-value` | Gegenstandstypen können nicht umgewandelt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
