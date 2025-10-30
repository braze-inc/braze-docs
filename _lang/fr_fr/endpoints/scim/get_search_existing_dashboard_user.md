---
nav_title: "GET : Effectuer une recherche par e-mail d’un compte utilisateur de tableau de bord existant"
article_title: "GET : Effectuer une recherche par e-mail d’un compte utilisateur de tableau de bord existant"
alias: /get_search_existing_dashboard_user_email/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Effectuer une recherche par e-mail d’un compte utilisateur du tableau de bord existant."
---

{% api %}
# Effectuer une recherche par e-mail d’un compte utilisateur de tableau de bord existant
{% apimethod get %}
scim/v2/Users?filter=userName%20eq%20 "user%40test.com"
{% endapimethod %}

> Utilisez cet endpoint pour rechercher un compte utilisateur de tableau de bord existant en spécifiant son e-mail dans le paramètre de requête du filtre. 

Veuillez prendre en compte que, lorsque le paramètre de recherche est encodé par URL, il s’affichera ainsi :

`/scim/v2/Users?filter=userName%20eq%20%22user@test.com%22`

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5037d810-b822-4c54-bb51-f30470a42a95 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d’un jeton SCIM. Vous utiliserez l'origine de votre service comme en-tête de `X-Request-Origin`. Pour plus d’informations, consultez la section [Provisionnement automatisé des utilisateurs]({{site.baseurl}}/scim/automated_user_provisioning/).

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='look up dashboard user email' %}

## Paramètres de chemin

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `userName@example.com` | Requis | Chaîne de caractères | L’adresse e-mail de l’utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Paramètres de demande

```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```

## Exemple de demande
```json
curl --location --request GET \ 'https://rest.iad-01.braze.com/scim/v2/Users?filter=userName%20eq%20%22user@test.com%22' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
```

## Réponse
```json
{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
    "totalResults": 1,
    "Resources": [
        {
            "userName": "user@test.com",
            "id": "dfa245b7-24195aec-887bb3ad-602b3340",
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
    ]
}
```

{% endapi %}

