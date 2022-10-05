---
nav_title: "PUT : Mettre à jour le compte développeur de tableau de bord"
article_title: "PUT : Mettre à jour le compte développeur de tableau de bord"
permalink: /post_update_existing_developer_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente des informations concernant l’endpoint Mettre à jour le compte développeur du tableau de bord existant."
hidden: true
---

{% api %}
# Mettre à jour un compte développeur de tableau de bord
{% apimethod put %}
/scim/v2/Users/YOUR_ID_HERE
{% endapimethod %}

Cet endpoint vous permet de mettre à jour compte développeur de tableau de bord existant en spécifiant les adresses e-mail, données et noms de famille, droits (pour définir les autorisations au niveau de la société, du groupe d’applications et de l’équipe). Pour plus d’informations sur la manière d’obtenir un jeton SCIM, consultez [Automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning/) (Approvisionnement automatisé des utilisateurs).

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='update dashboard developer' %}

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
  "departments": (required, string),
  "entitlements": (required, JSON object)
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| Schémas | Requis | Tableau de chaînes de caractères | Nom du schéma SCIM 2.0 attendu pour l’objet utilisateur. |
| `id` | Requis | Chaîne de caractères | Adresse e-mail du développeur |
| `username` | Requis | Chaîne de caractères | Le nom d'utilisateur dont le développeur aura besoin pour se connecter à Braze (généralement le même que l'adresse e-mail) |
| `name` | Requis | Object JSON | Cet objet contient le prénom et le nom du développeur |
| `departments` | Requis | Chaîne de caractères | Cette chaîne indique le service auquel l’utilisateur appartient. Les options disponibles comprennent :<br>- « Agence / Tiers »<br>- « BI / Analyses »<br>- « C-suite »<br>- « Ingénierie »<br>- « Finance »<br>- « Marketing / Éditorial »<br>- « Gestion produits »" |
| `entitlements` | Requis | Object JSON | Cet objet permet de définir les autorisations du développeur dans une entreprise, un groupe d’apps et un niveau d’équipe. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```json
curl --location --request PUT 'https://rest.iad-01.braze.com/scim/v2/Users/user@test.com' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data raw '{
  "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
  "id": "user@test.com",
  "userName": "user@test.com",
  "name": {
    "givenName": "Test",
    "familyName": "User"
  },
  "department": "finance",
  "entitlements": {
    "company": {
      "admin": false,
      "can manage company settings": false,
      "can add/remove app groups": false
    },
    "app_group": [
      {
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

## Réponse
```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
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

### États relatifs aux d’erreur
Si un développeur avec cette adresse e-mail n’existe pas dans Braze, le endpoint répondra avec :
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

