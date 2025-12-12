---
nav_title: "PUT: Update des Einstellungszentrums"
article_title: "PUT: Update Preference Center"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Update a preference center Braze."

---
{% api %}
# Update des Einstellungszentrums
{% apimethod put %}
/preference_center/v1/{preferenceCenterExternalID}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein Einstellungszentrum zu aktualisieren.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#bf1b43db-3f1b-461f-ad9a-2fbe35b804d7 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `preference_center.update`.

## Rate-Limit

Für diesen Endpunkt gilt ein Rate-Limits von 10 Anfragen pro Minute und Workspace.

## Pfad-Parameter

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| Erforderlich | String | Die ID für Ihr Präferenzzentrum. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```
{
  "name": "preference_center_name",
  "preference_center_title": "string",
  "preference_center_page_html": "string",
  "confirmation_page_html": "string",
  "options": {
    "unknown macro": {links-tags}
  "options": {
    "meta-viewport-content": "string", (optional) Only the `content` value of the meta tag,
    "links-tags": [
      {
        "rel": "string", (required) One of: "icon", "shortcut icon", or "apple-touch-icon",
        "type": "string", (optional) Valid values: "image/png", "image/svg", "image/gif", "image/x-icon", "image/svg+xml", "mask-icon",
        "sizes": "string", (optional),
        "color": "string", (optional) Use when type="mask-icon",
        "href": "string", (required)
      }
    ]
  }
} 
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`preference_center_page_html`| Erforderlich | String | Der HTML-Code für die Seite des Einstellungszentrums. |
|`preference_center_title`| Optional | String | Der Titel für das Einstellungscenter und die Bestätigungsseiten. Wenn kein Titel angegeben wird, lautet der Titel der Seiten standardmäßig "Einstellungscenter". |
|`confirmation_page_html`| Erforderlich | String | Der HTML-Code für die Bestätigungsseite. |
|`state` | Optional | String | Wählen Sie `active` oder `draft`.|
|`options` | Optional | Objekt | Attribute: <br>`meta-viewport-content`: Wenn vorhanden, wird der Seite ein `viewport` Meta-Tag mit `content= <value of attribute>` hinzugefügt.<br><br> `link-tags`: Legen Sie ein Favicon für die Seite fest. Wenn diese Option aktiviert ist, wird der Seite ein `<link>` Tag mit einem rel-Attribut hinzugefügt.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

{% raw %}
```
curl --location --request POST 'https://rest.iad-01.braze.com/preference_center/v1/{preferenceCenterExternalId}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "name": "Example",
  "preference_center_title": "Example Preference Center Title",
  "preference_center_page_html": "HTML for preference center here",
  "confirmation_page_html": "HTML here with a message to users here",
  "state": "active"
}
'
```
{% endraw %}

## Beispielhafte Antwort
{% raw %}
```
{
  "preference_center_api_id": "8efc52aa-935e-42b7-bd6b-98f43bb9b0f1",
  "created_at": "2022-09-22T18:28:07Z",
  "updated_at": "2022-09-22T18:32:07Z",
  "message": "success"
}
```
{% endraw %}

{% endapi %}
