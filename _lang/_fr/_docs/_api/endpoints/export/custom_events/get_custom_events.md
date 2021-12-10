---
nav_title: "GET: Liste des événements personnalisés"
article_title: "GET: Liste des événements personnalisés"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails du point de terminaison de la liste des événements personnalisés."
---

{% api %}
# Obtenir la liste des événements personnalisés
{% apimethod get %}
/fr/events/list
{% endapimethod %}

Ce point de terminaison vous permet d'exporter une liste d'événements personnalisés qui ont été enregistrés pour votre application. Les noms des événements sont retournés en groupes de 250, triés par ordre alphabétique.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1 {% endapiref %}

{% alert note %}
Une limite de taux est appliquée aux demandes faites à ce point de terminaison pour les clients embarqués avec Braze le ou après le 16 septembre 2021. Pour plus d'informations, voir [les limites de l'API]({{site.baseurl}}/api/basics/#api-limits).
{% endalert %}

## Paramètres de la requête

| Paramètre | Requis    | Type de données | Libellé                                                                                               |
| --------- | --------- | --------------- | ----------------------------------------------------------------------------------------------------- |
| `page`    | Optionnel | Nombre entier   | La page des noms d'événements à retourner, par défaut à 0 (retourne le premier ensemble jusqu'à 250). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

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
    "message": (requis, chaîne) le statut de l'exportation, renvoie 'success' quand complété sans erreurs,
    "events" : [
        "Event A",
        "Evénement B",
        "Événement C",
...
    ]
}
```

### Code de réponse d'erreur fatal {#fatal-export}

Les codes de statut suivants et les messages d'erreur associés seront retournés si votre requête rencontre une erreur fatale. Ces codes d’erreur indiquent qu’aucune donnée ne sera traitée.

| Code d'erreur        | Raison / Cause                                                                |
| -------------------- | ----------------------------------------------------------------------------- |
| 400 Mauvaise requête | Syntaxe incorrecte                                                            |
| 401 Non autorisé     | Clé d'API REST inconnue ou manquante                                          |
| Tarif Limité 429     | Limite de débordement                                                         |
| 5XX                  | Erreur interne du serveur, vous devriez réessayer avec le backoff exponentiel |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}


{% endapi %}
