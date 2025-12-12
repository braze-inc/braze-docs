---
nav_title: "GET : Rechercher un compte utilisateur de tableau de bord existant"
article_title: "GET : Rechercher un compte utilisateur de tableau de bord existant"
alias: /get_see_user_account_information/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente les détails de la fonction Rechercher un compte d'utilisateur de tableau de bord existant ID ressource Braze endpoint."
---

{% api %}
# Recherche d'un compte d'utilisateur du tableau de bord existant par ID de ressource
{% apimethod get %}
/scim/v2/Users/{id}
{% endapimethod %}

> Utilisez cet endpoint pour rechercher un compte utilisateur du tableau de bord existant en spécifiant la ressource `id` retournée par la méthode [`POST`]({{site.baseurl}}/api/endpoints/scim/post_create_user_account/) SCIM. 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#3df40764-8f74-4532-aed3-ab8a6cb92122 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d’un jeton SCIM. Vous utiliserez l'origine de votre service comme en-tête de `X-Request-Origin`. Pour plus d’informations, consultez la section [Provisionnement automatisé des utilisateurs]({{site.baseurl}}/scim/automated_user_provisioning/).

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='look up dashboard user' %}

## Paramètres de chemin

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `id` | Requis | Chaîne de caractères | L’ID de ressource de l’utilisateur. Ce paramètre est renvoyé par les méthodes `POST` `/scim/v2/Users/` ou `GET`  `/scim/v2/Users?filter=userName eq "user@test.com"`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Corps de la demande
```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```

## Exemple de demande
```json
curl --location --request GET 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
```

## Réponse
```json
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "id": "dfa245b7-24195aec-887bb3ad-602b3340",
    "userName": "user@test.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "lastSignInAt": "Thursday, January 1, 1970 12:00:00 AM",
    "createdAt": "Thursday, January 1, 1970 12:00:00 AM",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Another Test Role",
                "roleId": "23125dad23dfaae7,
                "appGroup": [
                    {
                        "appGroupId": "241adcd25adfabcded",
                        "appGroupName": "Production Workspace",
                        "appGroupPermissionSets": [
                            {
                                "appGroupPermissionSetName": "A Permission Set",
                                "appGroupPermissionSetId": "dfa385109bc38",
                                "permissions": ["basic_access","publish_cards"]
                            }
                        ]
                    } 
                ]
            }
        ],
        "appGroup": [
            {
                "appGroupId": "241adcd25789fabcded",
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamId": "241adcd25789fabcded",
                         "teamName": "Test Team",                  
                         "teamPermissions": ["admin"]
                    }
                ]
            } 
        ]
    }
}
```

{% endapi %}