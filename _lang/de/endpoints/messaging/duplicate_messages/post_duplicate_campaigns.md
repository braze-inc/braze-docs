---
nav_title: "POST: Duplizierte Kampagnen"
article_title: "POST: Duplizierte Kampagnen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten zum Endpunkt Doppelte Kampagnen."

---
{% api %}
# Duplizieren von Kampagnen über die API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/kampagnen/duplizieren
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Kampagnen zu duplizieren. Dieser API Endpunkt ist vergleichbar mit dem [Duplizieren von Kampagnen im Braze-Dashboard][1].

{% alert important %}
Die Duplizierung einer Kampagne mit Hilfe der API befindet sich derzeit in der Early-Access-Phase. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `campaigns.duplicate` erstellen.

## Rate-Limit

Dieser Endpunkt ist auf 100 API-Aufrufe pro Minute beschränkt.

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) The campaign identifier,
  "name": (required, string) The name of the resulting campaign,
  "description": (optional, string) The description of the resulting campaign,
}
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| Erforderlich | String | Siehe [Bezeichner der Kampagne]({{site.baseurl}}/api/identifier_types/). |
|`name`| Erforderlich | String | Der Name der daraus resultierenden Kampagne. |
|`description`| Optional | String | Das Beschreibungsfeld für die resultierende Kampagne. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Antwort

Dieser Endpunkt gibt einen `202` Status Code zurück, und die Erstellung der Kampagne erfolgt asynchron. Mit dem [Sicherheitsereignis-Download][2] können Sie Aufzeichnungen darüber einsehen, wann Kampagnen dupliziert wurden und mit welchem API-Schlüssel.


[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns#duplicating-segments-campaigns-and-canvases
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report

{% endapi %}
