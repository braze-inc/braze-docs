---
nav_title: "GET : Rechercher un compte utilisateur de tableau de bord existant"
article_title: "GET : Rechercher un compte utilisateur de tableau de bord existant"
alias: /get_see_user_account_information/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente des informations concernant l’endpoint Rechercher un compte utilisateur de tableau de bord existant."
---

{% api %}
# Rechercher un compte utilisateur de tableau de bord existant
{% apimethod get %}
/scim/v2/Users/YOUR_ID_HERE
{% endapimethod %}

Cet endpoint vous permet de rechercher un compte utilisateur de tableau de bord existant en spécifiant leur ID de ressource. Pour plus d’informations sur la manière d’obtenir un jeton SCIM, consultez [Automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning/) (Approvisionnement automatisé des utilisateurs).

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='look up dashboard user' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `id` | Requis | Chaîne de caractères | L’ID de ressource de l’utilisateur |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```json
curl --location --request GET 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## Réponse
```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "id": "9d5a095c-a350-4c88-bfc2-7e11782c1862",
    "userName": "user@test.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "lastSignInAt": "Thursday, January 1, 1970 12:00:00 AM",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "appGroup": [
            {
                "appGroupId": "241adcd25789fabcded",
                "appGroupName": "Test App Group",
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

