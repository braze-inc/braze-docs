---
nav_title: "GET : Applications du groupe d’apps"
layout: api_page
page_type: reference
hidden: true
permalink: /get_app_group_apps/

platform: API
description: "Cet article présente des informations concernant l’endpoint des applications du groupe d’apps GET, qui vous permet de récupérer un`apps` tableau d’objets."
---
{% api %}
# Endpoint des applications du groupe d’apps
{% apimethod get %}
/app_group/apps
{% endapimethod %}

Utilisez cet endpoint pour lister le nom et l’identifiant unique (`api_key`) pour les applications d’un groupe d’apps. Cet endpoint renvoie un tableau d’objets appelé `apps`. Chaque objet dans `apps` contient le nom et l’identifiant unique pour l’application. 

{% apiref postman %}  {% endapiref %}

## Limites de débit

Cet endpoint a une limitation du débit de 100 demandes par jour (24 heures).

## Paramètres de demande

Cette demande ne prend pas de paramètres.

## Exemple de demande

```
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/apps' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "apps": [
        {
          "name": "App Name",
          "api_key": 00000000-0000-0000-0000-000000000000
        }
    ],
    "message": "success"
}
```

### Erreurs possibles

- `401: Non autorisé` — API key does not have the required permissions. Make sure your API key has `autorisations apps.get.
- `403: Interdit — La bascule n’est pas disponible pour cette entreprise. Contactez votre CSM pour obtenir de l’aide.


{% endapi %}
