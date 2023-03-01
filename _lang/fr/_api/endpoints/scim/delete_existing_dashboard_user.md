---
nav_title: "SUPPRIMER : Supprimer le compte utilisateur de tableau de bord"
article_title: "SUPPRIMER : Supprimer le compte utilisateur de tableau de bord"
alias: /delete_existing_dashboard_user/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente des informations concernant l’endpoint Supprimer un compte utilisateur existant."
---

{% api %}
# Supprimer un compte utilisateur de tableau de bord
{% apimethod delete %}
/scim/v2/Users/YOUR_ID_HERE
{% endapimethod %}

Cet endpoint vous permet de supprimer définitivement un utilisateur de tableau de bord existant, comme la suppression d’un utilisateur dans la section **Gérer les utilisateurs** du tableau de bord de Braze. Pour plus d’informations sur la manière d’obtenir un jeton SCIM, consultez [Automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning/) (Approvisionnement automatisé des utilisateurs).

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='delete dashboard user' %}

## Corps de la demande

```json
Content-Type: application/json
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `id` | Requis | Chaîne de caractères | L’ID de ressource de l’utilisateur |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```json
curl --location --request DELETE 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```
## Réponse
```json
HTTP/1.1 204 Not Found
Content-Type: text/html; charset=UTF-8
```
### États relatifs aux erreurs
Si cet ID ne correspond à aucun développeur dans Braze, l’endpoint répondra avec :
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
