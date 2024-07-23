---
nav_title: "PUT : Mettre à jour un centre de préférences"
article_title: "PUT : Mettre à jour un centre de préférences"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Cet article précise des détails concernant l’endpoint de Braze Mettre à jour un centre de préférences."

---
{% api %}
# Mettre à jour un centre de préférences
{% apimethod put %}
/preference_center/v1/{preferenceCenterExternalID}
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour un centre de préférences.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#bf1b43db-3f1b-461f-ad9a-2fbe35b804d7 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `preference_center.update`.

## Limite de débit

Cet endpoint a une limitation du débit de 10 requêtes par minute, par espace de travail.

## Paramètres de chemin

| Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| Requis | Chaîne | L'identifiant de ton centre de préférences. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## Corps de la demande

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
    "meta-viewport-content": "string", (optional) Only the `content` value of the meta tag
  }
}
```

## Paramètres de demande

| Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description
| --------- | ---------| --------- | ----------- |
|`preference_center_page_html`| Requis | Chaîne | Le code HTML de la page du centre de préférences. |
|`preference_center_title`| Facultatif | Chaîne | Le titre du centre de préférences et des pages de confirmation. Si aucun titre n’est précisé, le titre des pages passera par défaut à « Centre de préférences ».
|`confirmation_page_html`| Requis | Chaîne | Le code HTML de la page de confirmation. |
|`state` | Facultatif | Chaîne | Choisis `active` ou `draft`.
|`options` | Facultatif | Objet | Attributs : `meta-viewport-content`. Lorsqu'elle est présente, une balise méta `viewport` sera ajoutée à la page avec `content= <value of attribute>`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande

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
