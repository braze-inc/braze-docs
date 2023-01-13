---
nav_title: "SUPPRIMER : Supprimer le compte développeur de tableau de bord"
article_title: "SUPPRIMER : Supprimer le compte développeur de tableau de bord"
permalink: /delete_existing_dashboard_developer/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente des informations concernant l’endpoint Supprimer le compte développeur existant."
hidden: true
---

{% api %}
# Supprimer un compte développeur de tableau de bord
{% apimethod delete %}
/scim/v2/Users/YOUR_ID_HERE
{% endapimethod %}

Cet endpoint vous permet de supprimer définitivement un développeur de tableau de bord existant, comme la suppression d’un utilisateur dans la section **Gérer les utilisateurs** du tableau de bord de Braze. Pour plus d’informations sur la manière d’obtenir un jeton SCIM, consultez [Automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning/) (Approvisionnement automatisé des utilisateurs).

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='delete dashboard developer' %}

## Corps de la demande

```json
Content-Type: application/json
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `id` | Requis | Chaîne de caractères | Adresse e-mail du développeur |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```json
curl --location --request DELETE 'https://rest.iad-01.braze.com/scim/v2/Users/user@test.com' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```
## Réponse
```json
HTTP/1.1 204 Not Found
Content-Type: text/html; charset=UTF-8
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
