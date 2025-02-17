---
nav_title: "LÖSCHEN: Katalogartikel löschen"
article_title: "LÖSCHEN: Katalogartikel löschen"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Katalogartikel löschen von Braze."

---
{% api %}
# Einen Katalogartikel löschen
{% apimethod delete %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen Artikel in Ihrem Katalog zu löschen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0dcce797-1346-472f-9384-082f14541689 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `catalogs.delete_item`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Pfad-Parameter

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| `catalog_name` | Erforderlich | String | Name des Katalogs. |
| `item_id` | Erforderlich | String | Die ID des Katalogartikels. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parameter anfordern

Für diesen Endpunkt gibt es keinen Anfragetext.

## Beispiel Anfrage

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
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
      "id": "item-not-found",
      "message": "Could not find item",
      "parameters": [
        "item_id"
      ],
      "parameter_values": [
        "restaurant34"
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
| `item-not-found` | Überprüfen Sie, ob der zu löschende Artikel in Ihrem Katalog vorhanden ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
