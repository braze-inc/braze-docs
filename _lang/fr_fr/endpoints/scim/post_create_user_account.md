---
nav_title: "POST : Créer un nouveau compte utilisateur de tableau de bord"
article_title: "POST : Créer un nouveau compte utilisateur de tableau de bord"
alias: /post_create_user_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Créer un nouveau compteur utilisateur de tableau de bord."

---

{% api %}
# Créer un nouveau compte utilisateur de tableau de bord
{% apimethod post %}
/scim/v2/Users
{% endapimethod %}

> Utilisez ce point de terminaison pour créer un nouveau compte utilisateur de tableau de bord en spécifiant l'e-mail, les prénoms et noms de famille, les autorisations (pour définir les autorisations au niveau de l'entreprise, de l'espace de travail et de l'équipe).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#768a3c9d-ce1d-44fc-a0e4-d556b09f7aa3 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d’un jeton SCIM. Vous utiliserez l'origine de votre service comme en-tête de `X-Request-Origin`. Pour plus d’informations, consultez la section [Provisionnement automatisé des utilisateurs]({{site.baseurl}}/scim/automated_user_provisioning/).

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='create dashboard user' %}

## Corps de la demande
```
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-KEY
```
```
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "userName": "user@test.com",
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
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",                  
                         "teamPermissions": ["basic_access","export_user_data"]
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
| `schemas` | Requis | Tableau de chaînes de caractères | Nom du schéma SCIM 2.0 attendu pour l'objet utilisateur. |
| `userName` | Requis | Chaîne de caractères | L’adresse e-mail de l’utilisateur. |
| `name` | Requis | Object JSON | Cet objet contient le prénom et le nom de famille de l’utilisateur. |
| `department` | Requis | Chaîne de caractères | Chaîne de [caractères]({{site.baseurl}}/scim_api_appendix/#department-strings) valide du département, tirée de la [documentation sur les chaînes de caractères du département]({{site.baseurl}}/scim_api_appendix/#department-strings). |
| `permissions` | Facultatif | Object JSON | Objet de permissions tel que décrit dans la [documentation de l'objet de permissions]({{site.baseurl}}/scim_api_appendix/#permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande
```json
curl --location --request POST 'https://rest.iad-01.braze.com/scim/v2/Users' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM–TOKEN-HERE' \
--data raw '{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "userName": "user@test.com",
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
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",                  
                         "teamPermissions": ["basic_access","export_user_data"]
                    }
                ]
            } 
        ]
    }
}'
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
                         "teamPermissions": ["basic_access","export_user_data"]
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

## Paramètres de réponse

| Paramètre | Type de données | Description |
| --------- | --------- | ----------- |
| `schemas` | Tableau de chaînes de caractères | Nom du schéma SCIM 2.0 attendu pour l'objet utilisateur. |
| `userName` | Chaîne de caractères | L’adresse e-mail de l’utilisateur. |
| `name` | Object JSON | Cet objet contient le prénom et le nom de famille de l'utilisateur. |
| `department` | Chaîne de caractères | Chaîne de [caractères]({{site.baseurl}}/scim_api_appendix/#department-strings) valide du département, tirée de la [documentation sur les chaînes de caractères du département]({{site.baseurl}}/scim_api_appendix/#department-strings). |
| `permissions` | Object JSON | Objet de permissions tel que décrit dans la [documentation de l'objet de permissions]({{site.baseurl}}/scim_api_appendix/#permissions-object). |
| `id` | Chaîne de caractères | ID généré par Braze qui est utilisé pour rechercher et gérer les comptes utilisateurs. |
| `lastSignInAt` | Chaîne de caractères | Date de la dernière connexion réussie en temps UTC. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### États relatifs aux d’erreur

Si un utilisateur ayant cette adresse `userName` ou e-mail existe déjà dans Braze, l'endpoint répondra par :

```json
HTTP/1.1 409 Conflict
Date: Tue, 10 Sep 2019 02:22:30 GMT
Content-Type: text/json;charset=UTF-8

{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
  "detail": "User already exists in the database.",
  "status": 409
}
```

{% endapi %}
