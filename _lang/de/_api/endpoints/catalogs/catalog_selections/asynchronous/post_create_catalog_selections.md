---
nav_title: "POST: Katalogauswahl erstellen"
article_title: "POST: Katalogauswahl erstellen"
search_tag: Endpunkt
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
| `selection` | Erforderlich | Objekt    | Ein Objekt, das Auswahlkriterien enthält. Eine vollständige Aufschlüsselung des Objekts und seiner Felder finden Sie im [Objekt, das die Kataloge auswählt]({{site.baseurl}}/api/objects_filters/catalog_selection_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Auswahlobjektparameter

| Parameter        | Erforderlich | Datentyp | Beschreibung                                                                                                                                                        |
| ---------------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`           | Erforderlich | String    | Der Name der Katalogauswahl, die ausgewählt wurde. |
| `description`    | Optional | String    | Eine Beschreibung der Auswahl der Kataloge. |
| `external_id`    | Erforderlich | String    | Ein eindeutiger Bezeichner für die Auswahl. |
| `source`         | Erforderlich | String    | Die Quelle der Katalogdaten. Für Shopify-Kataloge verwenden Sie bitte `"Shopify"`. Für angepasste Kataloge verwenden Sie bitte `"custom"`. |
| `filters`        | Optional | Array    | Ein Array von Filtern, die auf die Artikel angewendet werden sollen. Sie können bis zu vier Filter pro Anfrage festlegen. Wenn keine Filter angegeben werden, werden alle Artikel aus dem Katalog berücksichtigt. |
| `results_limit`  | Optional | Integer   | Die maximale Anzahl der zurückzugebenden Ergebnisse. Es muss sich um eine Zahl zwischen 1 und 50 handeln. |
| `sort_field`     | Optional | String    | Das Feld, nach dem die Ergebnisse sortiert werden sollen. Dies muss mit `sort_order`kombiniert werden. Wenn sowohl`sort_field`  als auch  `sort_order`nicht vorhanden sind, werden die Ergebnisse randomisiert. |
| `sort_order`     | Optional | String    | Die Reihenfolge, in der die Ergebnisse sortiert werden sollen. Zulässige Werte sind`"asc"`(aufsteigend) oder`"desc"`(absteigend). Dies muss mit `sort_field`kombiniert werden. Wenn sowohl`sort_field`  als auch  `sort_order`nicht vorhanden sind, werden die Ergebnisse randomisiert. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Die `sort_field`Parameter`sort_order` und müssen zusammen verwendet werden. Wenn Sie nur einen der beiden Parameter angeben oder beide Parameter weglassen, werden die Ergebnisse, die Sie ausgewählt haben, in zufälliger Reihenfolge angezeigt.
{% endalert %}

## Beispiel Anfrage

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/selections' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "selection": {
    "name": "favorite-restaurants",
    "description": "Favorite restaurants in NYC",
    "external_id": "favorite-nyc-restaurants",
    "source": "custom",
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
    ],
    "results_limit": 10,
    "sort_field": "Rating",
    "sort_order": "desc"
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

{% alert note %}
Die API unterstützt maximal vier Filter pro Auswahlanfrage. Im Braze-Dashboard können Sie bis zu 10 Filter pro Auswahl hinzufügen. Filter werden in der Reihenfolge angewendet, in der sie im Array erscheinen.
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
