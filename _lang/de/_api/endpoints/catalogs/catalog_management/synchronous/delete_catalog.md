---
nav_title: "LÖSCHEN: Katalog löschen"
article_title: "LÖSCHEN: Katalog löschen"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel enthält Details zum Endpunkt Katalog löschen von Braze."

---
{% api %}
# Katalog löschen
{% apimethod delete %}
/catalogs/{catalog_name}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen Katalog zu löschen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c0915a86-797a-4486-8217-24cd1c689d0f {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `catalogs.delete`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## Pfad-Parameter

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| `catalog_name` | Erforderlich | String | Name des Katalogs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## Antwort

Es gibt zwei Statuscode-Antworten für diesen Endpunkt: `200` und `404`.

### Beispiel für eine erfolgreiche Antwort

Der Statuscode `200` könnte den folgenden Antwortkörper zurückgeben:

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

| Fehler | Fehlersuche |
| --- | --- |
| `catalog-not-found` | Prüfen Sie, ob der Katalogname gültig ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
