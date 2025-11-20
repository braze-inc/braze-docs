---
nav_title: "DELETE : Supprimer la clé d'authentification du SDK"
article_title: "DELETE : Supprimer la clé d'authentification du SDK"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Cet article présente des détails sur le point de terminaison de la clé d'authentification du SDK Delete Braze."
---

{% api %}
# Supprimer la clé d'authentification SDK
{% apimethod delete %}
/app_group/sdk_authentication/delete
{% endapimethod %}

> Utilisez cet endpoint pour supprimer une clé d'authentification SDK pour votre application.

{% alert important %}
La clé primaire ne peut pas être supprimée. Si vous tentez de supprimer la clé primaire, cet endpoint renverra une erreur.
{% endalert %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `sdk_authentication.delete`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```
```json
{
  "app_id": "App API Identifier",
  "key_id": "key id"
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `app_id` | Requis | Chaîne de caractères | L'identifiant de l'API de l'application. |
| `key_id` | Requis | Chaîne de caractères | L'ID de la clé d'authentification SDK à supprimer. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande

```json
curl --location --request DELETE 'https://rest.iad-01.braze.com/app_group/sdk_authentication/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "key_id": "fedcba98-7654-3210-fedc-ba9876543210"
}'
```

## Réponse

```json
{
  "keys": [
    {
      "id": "abcdef12-3456-7890-abcd-ef1234567890",
      "rsa_public_key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----",
      "description": "SDK Authentication Key for iOS App",
      "is_primary": true
    }
  ]
}
```

## Paramètres de réponse

| Paramètre | Type de données | Description |
| --------- | --------- | ----------- |
| `keys` | Tableau | Tableau d'objets de clés d'authentification SDK restants. |
| `keys[].id` | Chaîne de caractères | L'ID de la clé d'authentification du SDK. |
| `keys[].rsa_public_key` | Chaîne de caractères | Chaîne de caractères de la clé publique RSA. |
| `keys[].description` | Chaîne de caractères | Description de la clé d'authentification du SDK. |
| `keys[].is_primary` | Valeur booléenne | Indique si cette clé est la clé d'authentification principale du SDK. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Règles de validation

Les règles de validation suivantes s'appliquent à cet endpoint :

- L'adresse `key_id` doit être un ID de clé d'authentification SDK valide.
- L'adresse `app_id` doit être un identifiant d'API d'application valide.
- La clé d'authentification SDK doit exister pour l'application spécifiée.
- La clé d'authentification SDK primaire ne peut pas être supprimée.

{% endapi %}
