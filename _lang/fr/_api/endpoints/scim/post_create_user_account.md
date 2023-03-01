---
nav_title: "POST : Créer un nouveau compte utilisateur de tableau de bord"
article_title: "POST : Créer un nouveau compte utilisateur de tableau de bord"
alias: /post_create_user_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente les détails concernant l’endpoint Créer un nouveau compteur utilisateur de tableau de bord."

---

{% api %}
# Créer un nouveau compte utilisateur de tableau de bord
{% apimethod post %}
/scim/v2/Users
{% endapimethod %}

Cet endpoint vous permet de créer un nouveau compte utilisateur du tableau de bord en spécifiant les adresses e-mail, données et noms de famille, permissions (pour définir les autorisations au niveau de la société, du groupe d’apps et de l’équipe). Pour plus d’informations sur la manière d’obtenir un jeton SCIM, consultez [Automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning/) (Approvisionnement automatisé des utilisateurs). 

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='create dashboard user' %}

## Corps de la demande
```
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```
```
{
  "schemas": (required, array of strings),
  "id": (required, string),
  "userName": (required, string),
  "name": (required, JSON object),
  "department": (required, string),
  "permissions": (required, JSON object)
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| Schémas | Requis | Tableau de chaînes de caractères | Nom du schéma SCIM 2.0 attendu pour l’objet utilisateur. |
| `id` | Requis | Chaîne de caractères | L’ID de ressource de l’utilisateur. |
| `userName` | Requis | Chaîne de caractères | L’adresse e-mail de l’utilisateur. |
| `name` | Requis | Object JSON | Cet objet contient le prénom et le nom de famille de l’utilisateur. |
| `department` | Requis | Chaîne de caractères | Une chaîne de caractères de département valide à partir de la [table de chaînes de caractères de département]({{site.baseurl}}/scim_api_appendix/#department-strings). |
| `permissions` | Requis | Object JSON | Un objet de permissions tel que décrit dans la section d’[objet de permissions]({{site.baseurl}}/scim_api_appendix/#permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```json
curl --location --request POST 'https://rest.iad-01.braze.com/scim/v2/Users' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
--data raw '{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "id": "9d5a095c-a350-4c88-bfc2-7e11782c1862",
    "userName": "user@test.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "appGroup": [
            {
                "appGroupName": "Test App Group",
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
CContent-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "id": "user@test.com",
    "userName": "user@test.com",
    "name": {
        "givenName": "Test",
        "familyName": "Utilisateur"
    },
    "department": "finance",
    "lastSignInAt": "Mardi 1er janvier, 1970 12:00:00 AM",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "appGroup": [
            {
                "appGroupId": "241adcd25789fabcded",
                "appGroupName": "Test App Group",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamId": "2519dafcdba238ae7",
                         "teamName": "Test Team",                  
                         "teamPermissions": ["basic_access","export_user_data"]
                    }
                ]
            } 
        ]
    }
}
```

### États relatifs aux erreurs

Si un utilisateur avec cette adresse e-mail existe déjà dans Braze, l’endpoint répondra avec :

```json
HTTP/1.1 409 Conflict
Date: Tue, 10 Sep 2 019 02:22:30 GMT
Content-Type: text/json;charset=UTF-8

{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
  "detail": "User already exists in the database.",
  "status": 409
}
```

{% endapi %}




