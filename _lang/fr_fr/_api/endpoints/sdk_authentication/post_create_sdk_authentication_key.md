---
nav_title: "POST : Créer une clé d'authentification SDK"
article_title: "POST : Créer une clé d'authentification SDK"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "Cet article présente les détails du point de terminaison Créer une clé d'authentification SDK Braze."
---

{% api %}
# Créer une clé d'authentification SDK
{% apimethod post %}
/app_group/sdk_authentication/create
{% endapimethod %}

> Utilisez cet endpoint pour créer une nouvelle clé d'authentification SDK pour votre application.

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `sdk_authentication.create`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```
```json
{
  "app_id": "App API identifier",
  "rsa_public_key_str": "RSA public key string", 
  "description": "description", 
  "make_primary": false
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `app_id` | Requis | Chaîne de caractères | L'identifiant de l'API de l'application. |
| `rsa_public_key_str` | Requis | Chaîne de caractères | Chaîne de caractères de la clé publique RSA. Il doit s'agir d'une clé publique RSA valide, sinon une erreur sera renvoyée. |
| `description` | Requis | Chaîne de caractères | Description de la clé d'authentification du SDK. |
| `make_primary` | Facultatif | Valeur booléenne | Si la valeur est `true`, cette clé devient la clé d'authentification principale du SDK lors de sa création. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande

```json
curl --location --request POST 'https://rest.iad-01.braze.com/app_group/sdk_authentication/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "rsa_public_key_str": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----", 
  "description": "SDK Authentication Key for iOS App", 
  "make_primary": false
}'
```

## Réponse
```json
{
  "id": "key id"
}
```

## Paramètres de réponse

| Paramètre | Type de données | Description |
| --------- | --------- | ----------- |
| `id` | Chaîne de caractères | L'ID de la clé d'authentification SDK nouvellement créée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Règles de validation

Les règles de validation suivantes s'appliquent à cet endpoint :

- Vous pouvez avoir jusqu'à 3 clés d'authentification SDK par application.
- La chaîne de caractères de la clé publique RSA doit être une clé publique RSA valide dans le format approprié.
- L'adresse `app_id` doit être un identifiant d'API d'application valide.
- La description ne peut pas être vide.

{% endapi %}
