---
nav_title: "POST: Katalogauswahl erstellen"
article_title: "POST: Katalogauswahl erstellen"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Katalogauswahl erstellen Braze."

---
{% api %}
# Katalogauswahl erstellen
{% apimethod post %}
/catalogs/{catalog_name}/selections
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Auswahl in Ihrem Katalog zu treffen.

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `catalogs.create_selection`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## Pfad-Parameter

| Parameter      | Erforderlich | Datentyp | Beschreibung          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | Erforderlich | String    | Name des Katalogs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parameter der Anfrage

| Parameter   | Erforderlich | Datentyp | Beschreibung                                                                                                                                                        |
| ----------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `selection` | Erforderlich | Objekt    | Ein Objekt, das Auswahlkriterien enthält. Die Auswahlobjekte könnten `name`, `description`, `filters`, `results_limit`, `sort_field` und `sort_order` enthalten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/selections' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "selection": {
    "name": "favorite-restaurants",
    "description": "Favorite restaurants in NYC",
    "filters": [
      {
        "field": "City",
        "operator": "equals",
        "value": "NYC"
      },
      {
        "field": "Rating",
        "operator": "greater than",
        "value": 7
      }
    ]
  }
}'
```

### Filteroperatoren

| Feldtyp | Unterstützte Operatoren                                     |
| ---------- | ------------------------------------------------------- |
| `string`   | `equals`, `does not equal`                              |
| `number`   | `equals`, `does not equal`, `greater than`, `less than` |
| `boolean`  | `is`                                                    |
| `time`     | `before`, `after`                                       |
| `array`    | `includes value`, `does not include value`              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

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
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
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

| Fehler                                | Fehlersuche                                                                               |
|--------------------------------------|-----------------------------------------------------------------------------------------------|
| `catalog-not-found`                  | Prüfen Sie, ob der Katalogname gültig ist.                                                         |
| `company-size-limit-already-reached` | Das Limit für die Katalogspeichergröße ist erreicht.                                                    |
| `selection-limit-reached`            | Das Limit für die Katalogauswahl ist erreicht.                                                      |
| `invalid-selection`                  | Prüfen Sie, ob die Auswahl gültig ist.                                                            |
| `too-many-filters`                   | Prüfen Sie, ob die Auswahl zu viele Filter enthält.                                                  |
| `selection-name-already-exists`      | Prüfen Sie, ob der Name der Auswahl bereits im Katalog vorhanden ist.                                    |
| `selection-has-invalid-filter`       | Prüfen Sie, ob der Auswahlfilter gültig ist.                                                       |
| `selection-invalid-results-limit`    | Prüfen Sie, ob die Ergebnisgrenze der Auswahl gültig ist.                                                |
| `invalid-sorting`                    | Prüfen Sie, ob die Auswahlsortierung gültig ist.                                                      |
| `invalid-sort-field`                 | Prüfen Sie, ob das Feld für die Auswahlsortierung gültig ist.                                                   |
| `invalid-sort-order`                 | Prüfen Sie, ob die Sortierreihenfolge der Auswahl gültig ist.                                                   |
| `selection-contains-too-many-arrays` | Prüfen Sie, ob die Auswahl mehr als ein Feld mit dem Typ `array` enthält. Es wird nur eines unterstützt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
