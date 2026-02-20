---
nav_title: "GET: Details für Präferenzzentrum anzeigen"
article_title: "GET: Details für Präferenzzentrum anzeigen"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details der Ansicht Details für den Endpunkt des Einstellungszentrums Braze."

---
{% api %}
# Details für Präferenzzentrum anzeigen
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die Details zu Ihren Einstellungszentren einzusehen, einschließlich des Zeitpunkts, zu dem sie erstellt und aktualisiert wurden.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6a47fd7c-2997-4832-aedb-d101a2dd03a5 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `preference_center.get`.

## Rate-Limit

Für diesen Endpunkt gilt ein Rate-Limits von 1.000 Anfragen pro Minute und Workspace.

## Pfad-Parameter

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| Erforderlich | String | Die ID für Ihr Präferenzzentrum. |
{: role="presentation" }

## Parameter der Anfrage

Für diesen Endpunkt gibt es keine Anfrage-Parameter.

## Beispiel Anfrage

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/preference_center_external_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort
```json
{
  "name": "My Preference Center",
  "preference_center_api_id": "preference_center_api_id",
  "created_at": "example_time_created",
  "updated_at": "example_time_updated",
  "preference_center_title": "Example preference center title",
  "preference_center_page_html": "HTML for preference center here",
  "confirmation_page_html": "HTML for confirmation page here",
  "redirect_page_html": null,
  "preference_center_options": {
    "meta-viewport-content": "width=device-width, initial-scale=2"
  },
  "state": "active"
}
```

{% endapi %}
