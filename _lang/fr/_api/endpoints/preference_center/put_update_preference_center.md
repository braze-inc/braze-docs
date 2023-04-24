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
/preference_center/v1/{preferenceCenterExternalId}
{% endapimethod %}

Utilisez cet endpoint pour mettre à jour un centre de préférences.

{% alert important %}
La prise en charge de cet endpoint est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Limites de débit

Cet endpoint a une limitation du débit de 10 demandes par minute, par groupe d’apps.

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```
{
  "name": "preference_center_name",
  "preference_center_title": "chaîne de caractères",
  "preference_center_page_html": "chaîne de caractères",
  "confirmation_page_html": "chaîne de caractères"
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`preference_center_page_html`| Requis | String | L’HTML de la page du centre de préférences. |
|`preference_center_title`| Facultatif | String | Le titre des pages du centre de préférences et de confirmation. Si aucun titre n’est précisé le titre des pages passera par défaut à « Centre de préférences ». |
|`confirmation_page_html`| Requis | String | L’HTML de la page de confirmation. |
|`state` | Facultatif | String | Choisir `active` ou `draft`.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location --request POST 'https://rest.iad-01.braze.com/preference_center/v1/{preferenceCenterExternalId}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "name": "Example",
  "preference_center_title": "Exemple de titre du centre de préférences",
  "preference_center_page_html": "HTML du centre de préférences ici",
  "confirmation_page_html": "HTML ici avec un message pour les utilisateurs ici",
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
