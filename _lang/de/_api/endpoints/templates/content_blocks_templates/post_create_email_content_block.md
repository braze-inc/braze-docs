---
nav_title: "POST: Inhaltsblock erstellen"
article_title: "POST: Inhaltsblock erstellen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten zum Endpunkt Inhaltsblöcke erstellen von Braze."

---
{% api %}
# Inhaltsblock erstellen
{% apimethod post %}
/content_blocks/create
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen [Inhaltsblock]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) zu erstellen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f1cefa8b-7a28-4e64-b579-198a4610d0a5 {% endapiref %}

## Voraussetzungen
Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `content_blocks.create`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Körper der Anfrage

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "name": (required, string) Must be less than 100 characters,
  "description": (optional, string) The description of the Content Block. Must be less than 250 character,
  "content": (required, string) HTML or text content within Content Block,
  "state": (optional, string) Choose `active` or `draft`. Defaults to `active` if not specified,
  "tags": (optional, array of strings) Tags must already exist
}
```

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| `name` | Erforderlich | String | Name des Inhaltsblocks. Muss weniger als 100 Zeichen umfassen. |
| `description` | Optional | String | Beschreibung des Inhaltsblocks. Muss weniger als 250 Zeichen umfassen. |
| `content` | Erforderlich | String | HTML- oder Textinhalt innerhalb des Inhaltsblocks. |
| `state` | Optional | String | Wählen Sie `active` oder `draft`. Der Standardwert ist `active`, wenn nicht angegeben. |
| `tags` | Optional | Array von Zeichenketten | Die [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) müssen bereits vorhanden sein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```json
curl --location --request POST 'https://rest.iad-01.braze.com/content_blocks/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "name": "content_block",
  "description": "This is my Content Block",
  "content": "HTML content within block",
  "state": "draft",
  "tags": ["marketing"]
}'
```

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "content_block_id": (string) Your newly generated block id,
  "liquid_tag": (string) The generated block tag from the Content Block name,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "message": "success"
}
```

## Fehlersuche

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehler | Fehlersuche |
| --- | --- |
| `Content cannot be blank` | |
| `Content must be a string` | Achten Sie darauf, dass Ihr Inhalt in Anführungszeichen eingeschlossen ist (`""`). |
| `Content must be smaller than 50kb` | Der Inhalt Ihres Inhaltsblocks muss insgesamt weniger als 50kb groß sein. |
| `Content contains malformed liquid` | Die angegebene Flüssigkeit ist nicht gültig oder nicht parsbar. Versuchen Sie es erneut mit einer gültigen Flüssigkeit oder wenden Sie sich an den Support. |
| `Content Block cannot be referenced within itself` | |
| `Content Block description cannot be blank` | |
| `Content Block description must be a string` | Achten Sie darauf, dass die Beschreibung Ihres Inhaltsblocks in Anführungszeichen (`""`) eingeschlossen ist. |
| `Content Block description must be shorter than 250 characters` | |
| `Content Block name cannot be blank` | |
| `Content Block name must be shorter than 100 characters` | |
| `Content Block name can only contain alphanumeric characters` | Die Namen der Inhaltsblöcke können jedes der folgenden Zeichen enthalten: die Buchstaben (groß- oder kleingeschrieben) `A` bis `Z`, die Zahlen `0` bis `9`, Bindestriche `-` und Unterstriche `_`. Er darf keine nicht-alphanumerischen Zeichen wie Emojis, `!`, `@`, `~`, `&` und andere "Sonderzeichen" enthalten. |
| `Content Block with this name already exists` | Versuchen Sie einen anderen Namen. |
| `Content Block state must be either active or draft` | |
| `Tags must be an array` | Tags müssen als Array von Strings formatiert werden, zum Beispiel `["marketing", "promotional", "transactional"]`. | |
| `All tags must be strings` | Stellen Sie sicher, dass Ihre Tags in Anführungszeichen (`""`) eingeschlossen sind. |
| `Some tags could not be found` | Um bei der Erstellung eines Inhaltsblocks ein Tag hinzuzufügen, muss das Tag bereits in Braze vorhanden sein. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
