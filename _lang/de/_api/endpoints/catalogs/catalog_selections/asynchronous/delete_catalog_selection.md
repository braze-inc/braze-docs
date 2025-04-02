---
nav_title: "LÖSCHEN: Katalogauswahl löschen"
article_title: "LÖSCHEN: Katalogauswahl löschen"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze Endpunkts Katalogauswahl löschen."

---
{% api %}
# Katalogauswahl löschen
{% apimethod delete %}
/catalogs/{catalog_name}/selections/{selection_name}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Katalogauswahl zu löschen.
{% alert important %}
Dieser Endpunkt befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Customer Success Manager, wenn Sie an diesem frühen Zugang interessiert sind.
{% endalert %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `catalogs.delete_selection`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## Pfad-Parameter

| Parameter        | Erforderlich | Daten Typ | Beschreibung                    |
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

Es gibt zwei Statuscode-Antworten für diesen Endpunkt: `202` und `404`.

### Beispiel für eine erfolgreiche Antwort

Der Statuscode `202` könnte den folgenden Antwortkörper zurückgeben:

```json
{
  "message": "success"
}
```

### Beispiel einer Fehlerantwort

Der Statuscode `404` könnte den folgenden Antwortkörper zurückgeben. Weitere Informationen zu Fehlern, die auftreten können, finden Sie unter [Fehlersuche](#troubleshooting).

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
| `invalid-selection`  | Prüfen Sie, ob der Name der Auswahl gültig ist.                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
