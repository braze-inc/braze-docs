---
nav_title: "GET : Générer l’URL du centre de préférences"
article_title: "GET : Générer l’URL du centre de préférences"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Cet article précise des détails concernant l’endpoint de Braze Générer l’URL du centre de préférences."

---
{% api %}
# Générer l’URL du centre de préférences
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}/url/{userID}
{% endapimethod %}

> Utilisez cet endpoint pour générer une URL pour un centre de préférences.

Chaque URL de centre de préférence est unique pour un utilisateur.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bc750ff-068e-4391-897e-6eddca2561cd {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `preference_center.user.get`.

## Limite de débit

Cet endpoint a une limitation du débit de 1 000 requêtes par minute, par espace de travail.

## Paramètres de chemin

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| Requis | Chaîne de caractères | L’ID de votre centre de préférences. |
|`userID`| Requis | Chaîne de caractères | L'ID utilisateur. |
{:  role="presentation" }

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`preference_center_api_id`| Requis | Chaîne de caractères | L’ID de votre centre de préférences. |
|`external_id`| Requis | Chaîne de caractères | L’ID externe pour un utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande

```
curl --location --request GET 'https://rest.iad-01.braze.com/preference_center/v1/$preference_center_external_id/url/$user_external_id' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Réponse

```json
{
  "preference_center_url": "https://www.example.com/preferences"
}
```

{% endapi %}

{% alert note %}
Cet endpoint génère uniquement des URL pour le nouveau centre de préférences (comme les centres de préférences créés à l'aide de notre API ou de l'éditeur par glisser-déposer).
{% endalert %}
