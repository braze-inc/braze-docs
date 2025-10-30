---
nav_title: "GET: Siehe Content-Blöcke Informationen"
article_title: "GET: Siehe Content-Blöcke Informationen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts See Content Blocks information Braze."
---

{% api %}
# Siehe Content-Block Informationen
{% apimethod get %}
/content_blocks/info
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Informationen zu Ihren bestehenden [Content-Blöcken]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) abzurufen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee {% endapiref %}

## Voraussetzungen
Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `content_blocks.info`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `content_block_id`  | Erforderlich | String | Der Bezeichner für den Content-Block. <br><br>Sie finden dies, indem Sie entweder die Content-Block-Informationen über einen API-Aufruf auflisten oder die Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) aufrufen, dann nach unten scrollen und nach Ihrem Content-Block-API-Bezeichner suchen.|
| `include_inclusion_data`  | Optional | Boolesche | Bei der Einstellung `true` gibt die API den Bezeichner der Nachrichtenvariationen-API von Kampagnen und Canvase zurück, in denen dieser Content-Block enthalten ist, um ihn in nachfolgenden Aufrufen zu verwenden.  Die Ergebnisse schließen archivierte oder gelöschte Kampagnen oder Canvase aus. |
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
| `Content Block ID cannot be blank` | Stellen Sie sicher, dass ein Content-Block in Ihrer Anfrage aufgeführt und in Anführungszeichen (`""`) gekapselt ist. |
| `Content Block ID is invalid for this workspace` | Dieser Content-Block existiert nicht oder befindet sich in einem anderen Firmenkonto oder Workspace. |
| `Content Block has been deleted—content not available` | Dieser Content-Block wurde gelöscht, auch wenn er schon früher existiert hat. |
| `Include Inclusion Data—error` | Dieser Parameter akzeptiert nur boolesche Werte (true oder false). Vergewissern Sie sich, dass der Wert für `include_inclusion_data` nicht in Anführungszeichen (`""`) eingeschlossen ist, wodurch der Wert stattdessen als String gesendet wird. Siehe [Anfrage-Parameter](#request-parameters) für Details. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
