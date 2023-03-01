---
nav_title: "PUT : Mettre à jour le compte utilisateur de tableau de bord"
article_title: "PUT : Mettre à jour le compte utilisateur de tableau de bord"
alias: /post_update_existing_user_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente des informations concernant l’endpoint Mettre à jour un compte utilisateur de tableau de bord existant."
---

{% api %}
# Mettre à jour un compte utilisateur de tableau de bord existant
{% apimethod put %}
/scim/v2/Users/YOUR_ID_HERE
{% endapimethod %}

Cet endpoint vous permet de mettre à jour un compte utilisateur de tableau de bord existant en spécifiant l’ID de ressource. Permet de mettre à jour les prénoms, noms de famille, permissions (pour définir des permissions au niveau de la société, du groupe d’apps et de l’équipe) et département. Pour plus d’informations sur la manière d’obtenir un jeton SCIM, consultez [Automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning/) (Approvisionnement automatisé des utilisateurs).

Pour des raisons de sécurité, `userName` (adresse e-mail) ne peut pas actuellement être mis à jour à l’aide de cet endpoint. Si vous désirez modifier le `userName` (adresse e-mail) d’un utilisateur, contactez l’[assistance]({{site.baseurl}}/support_contact/).

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='update dashboard user' %}

## Corps de la demande
```
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```
```
{
  "schemas": (required, array of strings),
  "name": (required, JSON object),
  "department": (required, string),
  "permissions": (required, JSON object)
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| Schémas | Requis | Tableau de chaînes de caractères | Nom du schéma SCIM 2.0 attendu pour l’objet Utilisateur. |
| `name` | Requis | Object JSON | Cet objet contient le prénom et le nom de famille de l’utilisateur. |
| `department` | Requis | Chaîne de caractères | Une chaîne de caractères de département à partir de la [table de chaînes de caractères de département]({{site.baseurl}}/scim_api_appendix/#department-strings). |
| `permissions` | Requis | Object JSON | Un objet Permissions tel que décrit dans la section d’[objet Permissions]({{site.baseurl}}/scim_api_appendix/#permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```json
curl --location --request PUT 'https://rest.iad-01.braze.com/scim/v2/Users/user@test.com' \
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
        "appGroup": [
            {
                "appGroupName": "Test App Group",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
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
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE

{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "id": "user@test.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "lastSignInAt": "Thursday, January 1, 1 970 12:00:00 AM",
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


