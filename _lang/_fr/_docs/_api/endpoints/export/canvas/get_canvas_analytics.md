---
nav_title: "GET: Analyse de la série de données sur les canvas"
article_title: "GET: Analyse de la série de données sur les canvas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison Analytique de la série de données Canvas ."
---

{% api %}
# Point de terminaison d'analyse de la série de données de Canvas
{% apimethod get %}
/fr/canvas/data_series
{% endapimethod %}

Ce point de terminaison vous permet d'exporter des données de séries temporelles pour un Canvas.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0fd61e93-7edf-4d87-a8dc-052420aefb73 {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

## Paramètres de la requête

| Paramètre                                   | Requis     | Type de données                                                                | Libellé                                                                                                                                                                                             |
| ------------------------------------------- | ---------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id_toile`                                  | Requis     | Chaîne de caractères                                                           | Voir [l'identifiant API Canvas]({{site.baseurl}}/api/identifier_types/).                                                                                                                            |
| `finalisation_à`                            | Requis     | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) chaîne) | Date à laquelle l'export de données doit se terminer. Par défaut, l'heure de la requête.                                                                                                            |
| `Démarrer_à`                                | Optionnel* | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) chaîne) | Date à laquelle l'exportation des données doit commencer. <br><br>* Soit la `longueur` ou `le démarrage_at` est requis.                                                                 |
| `Longueur`                                  | Optionnel* | Chaîne de caractères                                                           | Nombre maximum de jours avant `ending_at` pour inclure dans la série retournée. Doit être compris entre 1 et 14 (inclus). <br><br>* Soit la `longueur` ou `le démarrage_at` est requis. |
| `Comprend la répartition des variantes`     | Optionnel  | Boolean                                                                        | Si oui ou non inclure les stats de variante (par défaut, false).                                                                                                                                    |
| `Comprend la répartition des étapes`        | Optionnel  | Boolean                                                                        | Indique s'il faut ou non inclure les stats d'étape (par défaut la valeur false).                                                                                                                    |
| `Inclure les données des étapes supprimées` | Optionnel  | Boolean                                                                        | Inclure ou non les stats d'étape pour les étapes supprimées (par défaut la valeur false).                                                                                                           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_series?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-5:00&starting_at=2018-05-28T23:59:59-5:00&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "data": {
    "name": (string) Nom de Canvas
    "stats": [
      {
        "time": (string) date en tant que date ISO 8601,
        "total_stats": {
          "revenus": (float),
          "conversions": (int),
          "conversions_by_entry_time": (int),
          "entrées": (int)
        },
        "variant_stats": (facultatif) {
          "00000000-0000-0000-0000-0000000000000": (Identifiant API pour variant) {
            "name": (chaîne) nom de variante,
            "revenus": (int),
            "conversions": (int),
            "conversions_by_entry_time": (int),
            "entrées": (int)
          },
          ... (plus de variantes)
        },
        "step_stats": (facultatif) {
          "00000000-0000-0000-0000-0000000000000": (identifiant de l'API pour l'étape) {
            "name": (string) nom d'étape,
            "revenus": (flotte),
            "conversions": (int),
            "conversions_by_entry_time": (int),
            "messages": {
              "email": [
                {
                  "envoyé": (int),
                  "opens": (int),
                  "unique_opens": (int),
                  "clics": (int),
                  . . (plus de statistiques)
                }
              ],
              . . (plus de canaux)
            }
          },
          ... (plus d'étapes)
        }
      },
      ... (plus de stats par fois)
    ]
  },
  "message": (requis, chaîne) le statut de l'exportation, retourne 'success' quand complété sans erreurs
}
```
{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
