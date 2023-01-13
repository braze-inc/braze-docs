---
nav_title: "GET : Voir les informations du compte développeur du tableau de bord"
article_title: "GET : Voir les informations du compte développeur du tableau de bord"
permalink: /get_see_developer_account_information/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente les détails concernant l’endpoint Voir les informations relatives au compte développeur de tableau de bord."
hidden: true
---

{% api %}
# Voir les informations du compte développeur du tableau de bord
{% apimethod get %}
/scim/v2/Users/YOUR_ID_HERE
{% endapimethod %}

Cet endpoint vous permet de rechercher un compte développeur de tableau de bord existant en spécifiant leur e-mail. Pour plus d’informations sur la manière d’obtenir un jeton SCIM, consultez [Automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning/) (Approvisionnement automatisé des utilisateurs).

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='look up dashboard developer' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `id` | Requis | Chaîne de caractères | Adresse e-mail du développeur |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```json
curl --location --request GET 'https://rest.iad-01.braze.com/scim/v2/Users/user@test.com' \
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
  "id": "user@test.com",
  "userName": "user@test.com",
  "name": {
    "givenName": "Test",
    "familyName": "User"
  },
  "department": "finance",
  "last_sign_in_at": "Thursday, January 1, 1970 12:00:00 AM",
  "entitlements": {
    "company": {
      "admin": false,
      "can manage company settings": false,
      "can add/remove app groups": false
    },
    "app_group": [
      {
        "app_group_id": "241adcd25789fabcded",
        "app_group_name": "Test App Group",
        "admin": false,
        "access campaigns, canvases, cards, segments, media library": true,
        "export user data": false,
        "send campaigns, canvases": true,
        "publish cards": false,
        "edit segments": false,
        "access dev console": false,
        "manage teams": false,
        "view usage data": false,
        "view billing details": false,
        "manage tags": false,
        "view user profiles": false,
        "manage dashboard users": false,
        "manage events, attributes, purchases": false,
        "manage email settings": false,
        "manage media library": false,
        "manage apps": false,
        "import and update user data": false,
        "manage external integrations": false,
        "view pii": false,
        "manage subscription groups": false,
        "team": [
          {
            "team_id": "241adcd25789fabcded",
            "team_name": "Test Team",
            "admin": false,
            "access campaigns, canvases, cards, segments, media library": true,
            "export user data": false,
            "send campaigns, canvases": true,
            "publish cards": false,
            "edit segments": false,
            "view user profiles": false,
            "manage dashboard users": false   
          } 
        ]
      } 
    ],
  }
}
```

{% endapi %}

