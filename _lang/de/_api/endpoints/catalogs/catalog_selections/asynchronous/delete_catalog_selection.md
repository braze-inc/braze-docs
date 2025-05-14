---
nav_title: "LÖSCHEN: Katalogauswahl löschen"
article_title: "LÖSCHEN: Katalogauswahl löschen"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Katalogauswahl löschen in Braze."

---
{% api %}
# Katalogauswahl löschen
{% apimethod delete %}
/catalogs/{catalog_name}/selections/{selection_name}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Katalogauswahl zu löschen.

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `catalogs.delete_selection`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## Pfad-Parameter

| Parameter        | Erforderlich | Datentyp | Beschreibung                    |
| ---------------- | -------- | --------- | ------------------------------ |
| `catalog_name`   | Erforderlich | String    | Name des Katalogs.           |
| `selection_name` | Erforderlich | String    | Name der Katalogauswahl. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/selections/favorite_list' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## Antwort

Für diesen Endpunkt gibt es zwei Status Code Antworten: `202` und `404`.

### Beispiel für eine erfolgreiche Antwort

Der Status Code `202` könnte den folgenden Antwortkörper zurückgeben:

```json
{
  "message": "success"
}
```

### Beispiel einer Fehlerantwort

Der Status Code `404` könnte den folgenden Antwortkörper zurückgeben. Unter [Fehlerbehebung](#troubleshooting) finden Sie weitere Informationen zu Fehlern, die bei Ihnen auftreten können.

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

| Fehler                | Fehlersuche                                          |
| -------------------- | -------------------------------------------------------- |
| `catalog-not-found`  | Prüfen Sie, ob der Katalogname gültig ist.                    |
| `invalid-selection`  | Prüfen Sie, ob der Auswahlname gültig ist.                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
