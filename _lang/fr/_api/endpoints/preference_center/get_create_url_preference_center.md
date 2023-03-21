---
nav_title: "GET : Générer l’URL du centre de préférences"
article_title: "GET : Générer l’URL du centre de préférences"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Cet article précise des détails concernant l’endpoint Braze Générer l’URL du centre de préférences."

---
{% api %}
# Générer l’URL du centre de préférences
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalId}/url/{userId}
{% endapimethod %}

Utilisez cet endpoint pour générer une URL pour un centre de préférences. Chaque URL de centre de préférence est unique pour un utilisateur.

## Limite de débit

Cet endpoint a une limitation du débit de 1 000 demandes par minute, par groupe d’apps.

## Exemple de demande

```
curl --location --request GET 'https://rest.iad-01.braze.com/preference_center/v1/$preference_center_external_id/url/$user_external_id' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`preference_center_api_id`| Requis | String | L’ID de votre centre de préférences. |
|`external_id`| Requis | String | L’ID externe pour un utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Réponse 

```json
{
  "preference_center_url": "https://www.example.com/preferences"
}
```

{% endapi %}
