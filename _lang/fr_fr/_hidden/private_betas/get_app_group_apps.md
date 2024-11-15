---
nav_title: "GET : Liste des applications de l'espace de travail"
layout: api_page
page_type: reference
hidden: true
permalink: /get_app_group_apps/

platform: API
description: "Cet article détaille l'endpoint Liste des applications de l’espace de travail de Braze."
---
{% api %}
# Liste des applications de l'espace de travail
{% apimethod get %}
/app_group/apps
{% endapimethod %}

> Utilisez cet endpoint pour répertorier le nom et l'identifiant unique (`api_key`) des applications d’un espace de travail. 

Cet endpoint renvoie un tableau d’objets appelé `apps`. Chaque objet dans `apps` contient le nom et l’identifiant unique pour l’application. 

{% apiref postman %}  {% endapiref %}

## Limite de débit

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

### Résolution des problèmes

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `401: Unauthorized` | La clé API ne dispose pas des autorisations requises. Assurez-vous que votre clé API dispose des autorisations `apps.get`. |
| `403: Forbidden` | La bascule de fonctionnalité n’est pas disponible pour cette entreprise. Contactez votre CSM pour obtenir de l’aide. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
