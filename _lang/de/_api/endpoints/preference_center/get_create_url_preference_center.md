---
nav_title: "GET: URL für das Einstellungszentrum generieren"
article_title: "GET: URL des Präferenzzentrums generieren"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Generate preference center URL Braze."

---
{% api %}
# URL für das Einstellungszentrum generieren
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}/url/{userID}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine URL für ein Einstellungszentrum zu generieren.

Die URL der Einstellungszentrale ist für jeden Nutzer:innen eindeutig.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bc750ff-068e-4391-897e-6eddca2561cd {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `preference_center.user.get`.

## Rate-Limit

Für diesen Endpunkt gilt ein Rate-Limits von 1.000 Anfragen pro Minute und Workspace.

## Pfad-Parameter

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| Erforderlich | String | Die ID für Ihr Präferenzzentrum. |
|`userID`| Erforderlich | String | Die Nutzer:innen ID. |
{:  role="presentation" }

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`preference_center_api_id`| Erforderlich | String | Die ID für Ihr Präferenzzentrum. |
|`external_id`| Erforderlich | String | Die externe ID für einen Nutzer:in. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl --location --request GET 'https://rest.iad-01.braze.com/preference_center/v1/$preference_center_external_id/url/$user_external_id' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Antwort

```json
{
  "preference_center_url": "https://www.example.com/preferences"
}
```

{% endapi %}

{% alert note %}
Dieser Endpunkt generiert nur URLs für das neue Einstellungszentrum (wie Einstellungszentren, die mit unserer API oder dem Drag-and-Drop-Editor erstellt wurden).
{% endalert %}
