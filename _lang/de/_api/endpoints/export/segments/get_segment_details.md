---
nav_title: "GET: Details zum Segment Export"
article_title: "GET: Details zum Segment Export"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Export Segmente Braze."

---
{% api %}
# Details zum Segment Export
{% apimethod get %}
/segmente/details
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um relevante Informationen über ein Segment abzurufen, das durch den Bezeichner `segment_id` identifiziert werden kann.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aab56ed9-0a28-476a-8b57-b79786dbb9c1 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `segments.details`.

## Rate-Limits

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter    | Erforderlich | Datentyp | Beschreibung            |
| ------------ | -------- | --------- | ---------------------- |
| `segment_id` | Erforderlich | String | Siehe [Segment API Bezeichner]({{site.baseurl}}/api/identifier_types/).<br><br> Die `segment_id` für ein bestimmtes Segment finden Sie auf der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) in Ihrem Braze-Konto oder Sie können den [Endpunkt Segmentliste exportieren]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) verwenden.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/details?segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
      "message": (required, string) the status of the export, returns 'success' when completed without errors,
      "created_at" : (string) the date created as ISO 8601 date,
      "updated_at" : (string) the date last updated as ISO 8601 date,
      "name" : (string) the segment name,
      "description" : (string) a human-readable description of filters,
      "text_description" : (string) the segment description,
      "tags" : (array) the tag names associated with the segment formatted as strings,
      "teams" : (array) the names of the Teams associated with the campaign
}
```

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
