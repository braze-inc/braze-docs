---
nav_title: "POST: Canvase duplizieren"
article_title: "POST: Canvase duplizieren"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten zum Endpunkt Duplicate Canvase."
---

{% api %}
# Canvase über die API duplizieren
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/duplicate
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Canvase zu duplizieren. Dieser API Endpunkt ist vergleichbar mit der [Duplizierung von Canvase im Braze-Dashboard][1].

{% alert important %}
Dieser Endpunkt befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `canvas.duplicate` erstellen.

## Rate-Limit

Dieser Endpunkt ist auf 100 API-Aufrufe pro Minute beschränkt.

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) The Canvas identifier,
  "name": (required, string) The name of the resulting Canvas,
  "description": (optional, string) The description of the resulting Canvas,
  "tag_names": (optional, string) The tags of the resulting Canvas,
}
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| Erforderlich | String | Siehe [Canvas Bezeichner](https://www.braze.com/docs/api/identifier_types/). |
|`name`| Erforderlich | String | Der Name des entstehenden Canvas. |
|`description`| Optional | String | Das Beschreibungsfeld für das entstehende Canvas. |
|`tag_names` | Optional | String | Die Tags für das resultierende Canvas. Es muss sich um bestehende Tags handeln. Wenn Sie in der Anfrage neue Tags hinzufügen, überschreiben diese alle Tags, die sich auf dem ursprünglichen Canvas befanden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Antwort

Dieser Endpunkt gibt einen `202` Status Code zurück, und die Erstellung des Canvas erfolgt asynchron. Sie können den [Download der Sicherheitsereignisse][2] verwenden, um Aufzeichnungen darüber zu sehen, wann Canvase dupliziert wurden und mit welchem API-Schlüssel.

[1]: {{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings

{% endapi %}
