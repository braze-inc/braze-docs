---
nav_title: "POST: Sende-IDs erstellen"
article_title: "POST: Sende-IDs erstellen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Braze-Endpunkt Sende-IDs erstellen."

---
{% api %}
# Sende-IDs erstellen
{% apimethod post %}
/sends/id/create
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Sende-IDs zu erstellen, die zum programmgesteuerten Versenden von Nachrichten und zur Verfolgung der Nachrichtenleistung verwendet werden können, ohne dass für jede Sendung eine Kampagne erstellt werden muss.

Die Verwendung der Sendekennung zum Verfolgen und Versenden von Nachrichten ist nützlich, wenn Sie planen, Inhalte programmgesteuert zu erstellen und zu versenden.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#74a04e53-659f-4473-abc5-0f6f735550ff {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `sends.id.create` erstellen.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='sends id create' %}

## Körper der Anfrage

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier
}
```

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Erforderlich | String | Siehe [Kennung der Kampagne]({{site.baseurl}}/api/identifier_types/). |
|`send_id`| Optional | String | Siehe [Kennung senden]({{site.baseurl}}/api/identifier_types/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/sends/id/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier"
}'
```

## Antwort

### Beispiel für eine erfolgreiche Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "message": "success",
  "send_id" : (string) the send identifier
}
```

{% endapi %}
