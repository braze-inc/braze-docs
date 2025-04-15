---
nav_title: "GET: Siehe Informationen zu Inhaltsblöcken"
article_title: "GET: Siehe Informationen zu Inhaltsblöcken"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze Endpunkts \"See Content Blocks information\"."
---

{% api %}
# Siehe Informationen zum Inhaltsblock
{% apimethod get %}
/content_blocks/info
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Informationen zu Ihren vorhandenen [Inhaltsblöcken]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) abzurufen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee {% endapiref %}

## Voraussetzungen
Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `content_blocks.info`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| `content_block_id`  | Erforderlich | String | Die Kennung des Inhaltsblocks. <br><br>Diese finden Sie, indem Sie entweder Content Block Informationen über einen API-Aufruf auflisten oder indem Sie auf die Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) gehen, dann nach unten scrollen und nach Ihrer Content Block API-Kennung suchen.|
| `include_inclusion_data`  | Optional | Boolesche | Wenn diese Option auf `true` gesetzt ist, gibt die API die API-Kennung der Nachrichtenvariationen von Kampagnen und Canvases zurück, in denen dieser Inhaltsblock enthalten ist, damit sie in nachfolgenden Aufrufen verwendet werden kann.  Die Ergebnisse schließen archivierte oder gelöschte Kampagnen oder Canvases aus. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id={{content_block_id}}&include_inclusion_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "content_block_id": (string) the Content Block identifier,
  "name": (string) the name of the Content Block,
  "content": (string) the content in the Content Block,
  "description": (string) the Content Block description,
  "content_type": (string) the content type, html or text,
  "tags": (array) An array of tags formatted as strings,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "last_edited": (string) The time the Content Block was last edited in ISO 8601,
  "inclusion_count" : (integer) the inclusion count,
  "inclusion_data": (array) the inclusion data,
  "message": "success",
}
```

## Fehlersuche

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehler | Fehlersuche |
| --- | --- |
| `Content Block ID cannot be blank` | Vergewissern Sie sich, dass ein Inhaltsblock in Ihrer Anfrage aufgeführt und in Anführungszeichen (`""`) gekapselt ist. |
| `Content Block ID is invalid for this workspace` | Dieser Inhaltsblock existiert nicht oder befindet sich in einem anderen Firmenkonto oder Arbeitsbereich. |
| `Content Block has been deleted—content not available` | Dieser Inhaltsblock wurde gelöscht, auch wenn er früher existiert haben mag. |
| `Include Inclusion Data—error` | Dieser Parameter akzeptiert nur boolesche Werte (true oder false). Vergewissern Sie sich, dass der Wert für `include_inclusion_data` nicht in Anführungszeichen (`""`) eingeschlossen ist, wodurch der Wert stattdessen als String gesendet wird. Siehe [Anfrageparameter](#request-parameters) für weitere Details. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
