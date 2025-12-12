---
nav_title: "DELETE : Supprimer un compte utilisateur de tableau de bord"
article_title: "DELETE : Supprimer le compte utilisateur de tableau de bord"
alias: /delete_existing_dashboard_user/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Supprimer un compte utilisateur de tableau de bord."
---

{% api %}
# Supprimer un compte utilisateur de tableau de bord
{% apimethod delete %}
/scim/v2/Users/{id}
{% endapimethod %}

> Utilisez cet endpoint pour supprimer définitivement un utilisateur de tableau de bord existant en spécifiant la ressource `id` renvoyée par la méthode SCIM [`POST`]({{site.baseurl}}/api/endpoints/scim/post_create_user_account/) . 

Cette opération est similaire à la suppression d'un utilisateur dans la section **Utilisateurs de l'entreprise** du tableau de bord Braze.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9c7c71ea-afd6-414a-99d1-4eb1fe274f16 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d’un jeton SCIM. Vous utiliserez l'origine de votre service comme en-tête de `X-Request-Origin`. Pour plus d’informations, consultez la section [Provisionnement automatisé des utilisateurs]({{site.baseurl}}/scim/automated_user_provisioning/).

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='delete dashboard user' %}

## Paramètres de chemin

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `id` | Requis | Chaîne de caractères | L’ID de ressource de l’utilisateur. Ce paramètre est renvoyé par les méthodes `POST` `/scim/v2/Users/` ou `GET` `/scim/v2/Users?filter=userName eq "user@test.com"`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Corps de la demande

```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```

## Exemple de demande
```json
curl --location --request DELETE 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## Réponse

### Exemple de réponse échouée

```json
HTTP/1.1 204 Not Found
Content-Type: text/html; charset=UTF-8
```

Si cet ID ne correspond à aucun développeur dans Braze, l’endpoint répondra avec :
```json
HTTP/1.1 404 Not Found
Content-Type: text/html; charset=UTF-8

{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
    "detail": "User not found",
    "status": 404
}
```
{% endapi %}
