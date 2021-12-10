---
nav_title: "GET: Liste des toiles"
article_title: "GET: Liste des toiles"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails du point de terminaison de la liste des canevas."
---

{% api %}
# Point de terminaison de la liste de toiles
{% apimethod get %}
/fr/canvas/list
{% endapimethod %}

Ce point de terminaison vous permet d'exporter une liste de Canvases, y compris le nom, l'identifiant de l'API Canvas et les balises associées. Les Canevas sont retournés en groupes de 100 triés par date de création (du plus ancien au plus récent par défaut).

Les Canevas archivés ne seront pas inclus dans la réponse de l'API, sauf si le champ `include_archived` est spécifié. Les toiles qui sont arrêtées mais non archivées seront retournées par défaut.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1 {% endapiref %}

## Paramètres de la requête

| Paramètre                         | Requis    | Type de données      | Libellé                                                                                                                                                                                                                                                                                                                  |
| --------------------------------- | --------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `page`                            | Optionnel | Nombre entier        | La page de Canvases à retourner, par défaut à `0` (retourne le premier ensemble jusqu'à 100)                                                                                                                                                                                                                             |
| `include_archivé`                 | Optionnel | Boolean              | Si oui ou non inclure des Canvases archivés, la valeur par défaut est `false`.                                                                                                                                                                                                                                           |
| `direction_tri`                   | Optionnel | Chaîne de caractères | - Trier le temps de création du plus récent au plus ancien : passer dans la valeur `desc`.<br> - Trier le temps de création de la plus ancienne à la plus récente : passer dans la valeur `asc`. <br><br>Si `sort_direction` n'est pas incluse, l'ordre par défaut est plus ancien que le plus récent. |
| `Dernière_modification.heure[gt]` | Optionnel | Date et heure        | Filtre les résultats et ne renvoie que les Canvases qui ont été édités plus grand que le temps fourni jusqu'à présent. Le format est `yyyy-MM-DDTHH:mm:ss`.                                                                                                                                                              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/list?page=1&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvases" : [
    {
        "id" : (string) Identificateur API Canvas
        "last_editeded": (chaîne ISO 8601) la dernière fois modifiée pour le message,
        "nom" : (chaîne) Nom de la toile,
        "tags" : (tableau) noms de balises associés aux Canvas,
    },
    . . (plus de Canvases)
  ],
  "message": (requis, chaîne) le statut de l'exportation, retourne 'success' quand complété sans erreurs
}
```
{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
