---
nav_title: "GET : Exporter la liste des événements personnalisés"
article_title: "GET : Exporter la liste des événements personnalisés"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Exporter la liste des événements personnalisés."

---
{% api %}
# Exporter la liste des événements personnalisés
{% apimethod get %}
/events/list
{% endapimethod %}

> Utilisez cet endpoint pour exporter une liste d’événements personnalisés qui ont été enregistrés pour votre application. Les noms des événements sont renvoyés par groupes de 250, triés par ordre alphabétique.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `events.list`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='events list' %}

## Paramètres de demande

| Paramètre| Requis | Type de données | Description |
| -------- | -------- | --------- | ----------- |
| `page` | Facultatif | Entier | La page des noms d’événement à renvoyer, par défaut sur 0 (renvoie le premier ensemble jusqu’à 250 éléments). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/events/list?page=3' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        "Event A", (string) the event name,
        "Event B", (string) the event name,
        "Event C", (string) the event name,
        ...
    ]
}
```

### Codes de réponse des erreurs fatales {#fatal-export}

Pour connaître les codes d'état et les messages d'erreur associés qui seront renvoyés si votre demande rencontre une erreur fatale, reportez-vous à la rubrique [Erreurs fatales & responses.]({{site.baseurl}}/api/errors/#fatal-errors)

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
