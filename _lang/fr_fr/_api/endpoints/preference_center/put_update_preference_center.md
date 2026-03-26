---
nav_title: "PUT : Mettre à jour un centre de préférences"
article_title: "PUT : Mettre à jour un centre de préférences"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Cet article détaille l'endpoint Braze Mettre à jour un centre de préférences."

---
{% api %}
# Mettre à jour un centre de préférences
{% apimethod put %}
/preference_center/v1/{preferenceCenterExternalID}
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour un centre de préférences.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#bf1b43db-3f1b-461f-ad9a-2fbe35b804d7 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l'autorisation `preference_center.update`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='post or put preference center' %}

## Paramètres de chemin

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| Requis | Chaîne de caractères | L'ID de votre centre de préférences. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Corps de la requête

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

## Paramètres de requête

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`preference_center_page_html`| Requis | Chaîne de caractères | Le code HTML de la page du centre de préférences. |
|`preference_center_title`| Facultatif | Chaîne de caractères | Le titre des pages du centre de préférences et de confirmation. Si aucun titre n'est spécifié, le titre des pages sera par défaut « Preference Center ». |
|`confirmation_page_html`| Requis | Chaîne de caractères | Le code HTML de la page de confirmation. |
|`state` | Facultatif | Chaîne de caractères | Choisissez `active` ou `draft`.|
|`options` | Facultatif | Objet | Attributs : <br>`meta-viewport-content` : Lorsque ce paramètre est présent, une balise méta `viewport` est ajoutée à la page avec `content= <value of attribute>`.<br><br> `link-tags` : Permet de définir un favicon pour la page. Lorsque ce paramètre est défini, une balise `<link>` avec un attribut rel est ajoutée à la page.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de requête

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

## Exemple de réponse
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