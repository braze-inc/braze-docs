---
nav_title: "PUT : Mettre à jour un compte utilisateur de tableau de bord"
article_title: "PUT : Mettre à jour le compte utilisateur de tableau de bord"
alias: /post_update_existing_user_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Mettre à jour un compte utilisateur de tableau de bord existant."
---

{% api %}
# Mettre à jour un compte utilisateur de tableau de bord
{% apimethod put %}
/scim/v2/Users/{id}
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour un compte utilisateur de tableau de bord existant en spécifiant la ressource `id` renvoyée par la méthode SCIM [`POST`]({{site.baseurl}}/api/endpoints/scim/post_create_user_account/) .

Il vous permet de mettre à jour les noms et prénoms, les autorisations (pour définir les autorisations au niveau de l'entreprise, de l'espace de travail et de l'équipe) et le département.

Pour des raisons de sécurité, `userName` (adresse e-mail) ne peut pas actuellement être mis à jour à l’aide de cet endpoint. Si vous souhaitez modifier le `userName` (adresse e-mail) d'un utilisateur, contactez l'[assistance]({{site.baseurl}}/support_contact/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f9a1642-988e-4011-8fb8-db4340ea1ac7 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d’un jeton SCIM. Vous utiliserez l'origine de votre service comme en-tête de `X-Request-Origin`. Pour plus d’informations, consultez la section [Provisionnement automatisé des utilisateurs]({{site.baseurl}}/scim/automated_user_provisioning/).

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='update dashboard user' %}

## Paramètres de chemin

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `id` | Requis | Chaîne de caractères | L’ID de ressource de l’utilisateur. Ce paramètre est renvoyé par les méthodes `POST` `/scim/v2/Users/` ou `GET` `/scim/v2/Users?filter=userName eq "user@test.com"`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Corps de la demande
```
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-KEY
```
```json
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "name": {"name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Test Role"
            },
            {
                "roleId": "2519dafcdba238ae7"
            }
        ],
        "appGroup": [
            {
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",
                         "teamPermissions": ["admin"]
                    } 
                ]
            },
            {
                "appGroupName": "Other Test Workspace",
                "appGroupPermissionSets": [
                    {
                        "appGroupPermissionSetName":  "Test Permission Set"
                    }
                ]
            } 
        ]
   }
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `schemas` | Requis | Tableau de chaînes de caractères | Nom du schéma SCIM 2.0 attendu pour l’objet Utilisateur. |
| `name` | Requis | Object JSON | Cet objet contient le prénom et le nom de famille de l’utilisateur. |
| `department` | Requis | Chaîne de caractères | Chaîne de [caractères]({{site.baseurl}}/scim_api_appendix/#department-strings) valide du département, tirée de la [documentation sur les chaînes de caractères du département]({{site.baseurl}}/scim_api_appendix/#department-strings). |
| `permissions` | Requis | Object JSON | Objet de permissions tel que décrit dans la [documentation de l'objet de permissions]({{site.baseurl}}/scim_api_appendix/#permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Exemple de demande
```json
curl --location --request PUT 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
--data raw '{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Test Role"
            },
            {
                "roleId": "2519dafcdba238ae7"
            }
        ],
        "appGroup": [
            {
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaign_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",                  
                         "teamPermissions": ["admin"]
                    }
                ]
            } 
        ]
    }
}
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
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Test Role",
                "roleId": "519dafcdba23dfaae7,
                "appGroup": [
                    {
                        "appGroupId": "241adcd25789fabcded",
                        "appGroupName": "Some Workspace",
                        "appGroupPermissions": ["basic_access", "publish_cards"],
                        "team": [
                            {
                                "teamId": "2519dafcdba238ae7",
                                "teamName": "Some Team",                  
                                "teamPermissions": ["export_user_data"]
                            }
                        ]
                    } 
                ]
            },
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
                         "teamId": "2519dafcdba238ae7",
                         "teamName": "Test Team",                  
                         "teamPermissions": ["admin"]
                    }
                ]
            } 
        ]
    }
}
```

### États relatifs aux d’erreur
Si un utilisateur avec cet ID n’existe pas dans Braze, l’endpoint répondra avec :

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
