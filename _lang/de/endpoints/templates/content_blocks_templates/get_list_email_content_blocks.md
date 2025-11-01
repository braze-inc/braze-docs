---
nav_title: "GET: Liste der verfügbaren Content-Blöcke"
article_title: "GET: Verfügbare Content-Blöcke auflisten"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Liste verfügbarer Content-Blöcke Braze."

---
{% api %}
# Liste der verfügbaren Content-Blöcke
{% apimethod get %}
/content_blocks/list
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Ihre vorhandenen [Content-Blöcke]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) aufzulisten.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d87048f-68fd-46c9-aa15-3a970e99540e {% endapiref %}

## Voraussetzungen
Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `content_blocks.list`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `modified_after`  | Optional | String im [ISO-8601-Format](https://en.wikipedia.org/wiki/ISO_8601)  | Ruft nur Content-Blöcke ab, die zum oder nach dem angegebenen Zeitpunkt aktualisiert wurden. |
| `modified_before`  |  Optional | String im [ISO-8601-Format](https://en.wikipedia.org/wiki/ISO_8601)  | Ruft nur Content-Blöcke ab, die zum oder vor dem angegebenen Zeitpunkt aktualisiert wurden. |
| `limit` | Optional | Positive Zahl | Maximale Anzahl der abzurufenden Content-Blöcke. Standardmäßig 100, wenn nicht angegeben, mit einem maximal zulässigen Wert von 1000. |
| `offset`  |  Optional | Positive Zahl | Anzahl der Content-Blöcke, die übersprungen werden sollen, bevor der Rest der Templates zurückgegeben wird, die den Suchkriterien entsprechen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request GET 'https://rest.iad-01.braze.com/content_blocks/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "count": "integer",
  "content_blocks": [
    {
      "content_block_id": (string) the Content Block identifier,
      "name": (string) the name of the Content Block,
      "content_type": (string) the content type, html or text,
      "liquid_tag": (string) the Liquid tags,
      "inclusion_count" : (integer) the inclusion count,
      "created_at": (string) The time the Content Block was created in ISO 8601,
      "last_edited": (string) The time the Content Block was last edited in ISO 8601,
      "tags": (array) An array of tags formatted as strings,
    }
  ]
}
```

## Fehlersuche

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehler | Fehlersuche |
| --- | --- |
| `Modified after time is invalid` | Das angegebene Datum ist kein gültiges oder analysierbares Datum. Formatieren Sie diesen Wert als String im ISO 8601-Format (`yyyy-mm-ddThh:mm:ss.ffffff`). |
| `Modified before time is invalid` | Das angegebene Datum ist kein gültiges oder analysierbares Datum. Formatieren Sie diesen Wert als String im ISO 8601-Format (`yyyy-mm-ddThh:mm:ss.ffffff`). |
| `Modified after time must be earlier than or the same as modified before time.` | Ändern Sie den Wert `modified_after` auf eine Zeit, die vor der Zeit von `modified_before` liegt. |
| `Content Block number limit is invalid` | Der Parameter `limit` muss eine Ganzzahl (positive Zahl) größer als 0 sein. |
| `Content Block number limit must be greater than 0` | Ändern Sie den Parameter `limit` in eine ganze Zahl größer als 0. |
| `Content Block number limit exceeds maximum of 1000` | Ändern Sie den Parameter `limit` in eine ganze Zahl kleiner als 1000. |
| `Offset is invalid` | Der Parameter `offset` muss eine ganze Zahl größer als 0 sein. |
| Offset muss größer als 0 sein | Ändern Sie den Parameter `offset` in eine ganze Zahl größer als 0. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
