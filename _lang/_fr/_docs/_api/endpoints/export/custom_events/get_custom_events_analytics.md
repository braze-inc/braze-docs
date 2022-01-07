---
nav_title: "GET: Analyse d'événements personnalisés"
article_title: "GET: Analyse d'événements personnalisés"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails du point de terminaison Analytique des événements personnalisés."
---

{% api %}
# Analyse des événements personnalisés
{% apimethod get %}
/fr/events/data_series
{% endapimethod %}

Ce point de terminaison vous permet de récupérer une série d'occurrences d'un événement personnalisé dans votre application sur une période déterminée.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

## Paramètres de la requête

| Paramètre             | Requis    | Type de données                                                                | Libellé                                                                                                                                                                     |
| --------------------- | --------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Evénement`           | Requis    | Chaîne de caractères                                                           | Le nom de l'événement personnalisé pour lequel retourner des analyses.                                                                                                      |
| `Longueur`            | Requis    | Nombre entier                                                                  | Nombre maximal d'unités (jours ou heures) avant `ending_at` pour inclure dans la série retournée. Doit être compris entre 1 et 100 (inclus).                                |
| `unité`               | Optionnel | Chaîne de caractères                                                           | Unité de temps entre les points de données. Peut être `jour` ou `heure`, par défaut à `jour`.                                                                               |
| `finalisation_à`      | Optionnel | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) chaîne) | Date à laquelle la série de données doit se terminer. Par défaut, l'heure de la requête.                                                                                    |
| `app_id`              | Optionnel | Chaîne de caractères                                                           | Identifiant API de l'application récupéré de la **console développeur** pour limiter les analyses à une application spécifique.                                             |
| `identifiant_segment` | Optionnel | Chaîne de caractères                                                           | See [Segment API identifier]({{site.baseurl}}/api/identifier_types/). ID de segment indiquant le segment analytique pour lequel l'analyse d'événements doit être retournée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/events/data_series?event=event_name&length=24&unit=hour&ending_at=2014-12-10T23:59:59-05:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (requis, chaîne) le statut de l'exportation, retourne 'success' lorsqu'il est terminé sans erreurs,
    "data" : [
        {
            "time" : (string) point dans le temps - comme ISO 8601 étendu lorsque l'unité est "hour" et comme la date ISO 8601 lorsque l'unité est "day",
            "count" : (int)
        },
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
