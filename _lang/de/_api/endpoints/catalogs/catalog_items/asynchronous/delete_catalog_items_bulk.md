---
nav_title: "LÖSCHEN: Mehrere Katalogobjekte löschen"
article_title: "LÖSCHEN: Mehrere Katalogobjekte löschen"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze Endpunkts Mehrere Katalogobjekte löschen."

---
{% api %}
# Mehrere Katalogobjekte löschen
{% apimethod delete %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um mehrere Artikel in Ihrem Katalog zu löschen.

Jeder Antrag kann bis zu 50 Artikel enthalten. Dieser Endpunkt ist asynchron.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#647c82e8-8b38-4df2-bde2-b1d8e19fd332 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `catalogs.delete_items`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## Pfad-Parameter

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| `catalog_name` | Erforderlich | String | Name des Katalogs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| `items` | Erforderlich | Array | Ein Array, das Artikelobjekte enthält. Die Artikelobjekte sollten eine `id` enthalten, die auf die Artikel verweist, die Braze löschen soll. Pro Anfrage sind bis zu 50 Artikelobjekte zulässig. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "restaurant1"},
    {"id": "restaurant2"},
    {"id": "restaurant3"}
  ]
}'
```

## Antwort

Es gibt drei Statuscode-Antworten für diesen Endpunkt: `202`, `400`, und `404`.

### Beispiel für eine erfolgreiche Antwort

Der Statuscode `202` könnte den folgenden Antwortkörper zurückgeben.

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
      "id": "items-missing-ids",
      "message": "There are 1 item(s) that do not have ids",
      "parameters": [],
      "parameter_values": []
    }
  ],
  "message": "Invalid Request",
}
```

## Fehlersuche

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehler | Fehlersuche |
| --- | --- |
| `catalog-not-found` | Prüfen Sie, ob der Katalogname gültig ist. |
| `ids-too-large` | Die Artikel-IDs dürfen nicht mehr als 250 Zeichen lang sein. |
| `ids-not-unique` | Prüfen Sie, ob die Artikel-IDs in der Anfrage eindeutig sind. |
| `ids-not-strings` | Artikel-IDs müssen vom Typ String sein. |
| `items-missing-ids` | Einige Artikel haben keine Artikel-IDs. Prüfen Sie, ob jeder Artikel eine Artikel-ID hat. |
| `invalid-ids` | Artikel-IDs dürfen nur Buchstaben, Zahlen, Bindestriche und Unterstriche enthalten. |
| `request-includes-too-many-items` | Ihre Anfrage enthält zu viele Artikel. Das Artikellimit pro Anfrage beträgt 50. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
