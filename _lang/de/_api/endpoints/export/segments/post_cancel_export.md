---
nav_title: "POST: Exporte nach Segmenten abbrechen"
article_title: "POST: Exporte nach Segmenten abbrechen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zu Cancel Exporte nach Segmenten Braze Endpunkt."

---
{% api %}
# Exporte nach Segmenten abbrechen
{% apimethod post %}
/export/segment/cancel
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um alle laufenden Exporte mit einer bestimmten Segment ID abzubrechen.

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `segments.list`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id": (required, string) the `segment_id` to locate and cancel its ongoing exports
}
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `segment_id` | Erforderlich | String | Die `segment_id`, ihre laufenden Exporte zu stornieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/export/segment/cancel' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id": "segment_identifier"
}'
```

{% endapi %}

