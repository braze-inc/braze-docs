---
nav_title: "GET: Liste des fiches d'actualités"
article_title: "GET: Liste des fiches d'actualités"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails de la liste de terminaison de la liste des fiches de nouvelles."
---

{% api %}
# Point de terminaison de la liste des fiches d'actualités
{% apimethod get %}
/fr/feed/list
{% endapimethod %}

Ce point de terminaison vous permet d'exporter une liste de cartes de flux d'actualités, chacune incluant son nom et l'identifiant API de la carte. Les cartes sont retournées en groupes de 100 triés par date de création (du plus ancien au plus récent par défaut).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9fa7a3bc-4a02-4de2-bc4c-8f111750665e {% endapiref %}

## Paramètres de la requête

| Paramètre         | Requis    | Type de données      | Libellé                                                                                                                                                                                                                                                                                                                  |
| ----------------- | --------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `page`            | Optionnel | Nombre entier        | La page des cartes à retourner, la valeur par défaut est 0 (retourne le premier ensemble jusqu'à 100).                                                                                                                                                                                                                   |
| `include_archivé` | Optionnel | Boolean              | Si oui ou non inclure les cartes archivées, la valeur par défaut est false.                                                                                                                                                                                                                                              |
| `direction_tri`   | Optionnel | Chaîne de caractères | - Trier le temps de création du plus récent au plus ancien : passer dans la valeur `desc`.<br> - Trier le temps de création de la plus ancienne à la plus récente : passer dans la valeur `asc`. <br><br>Si `sort_direction` n'est pas incluse, l'ordre par défaut est plus ancien que le plus récent. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/feed/list?page=1&include_archived=true&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (requis, chaîne) le statut de l'exportation, retourne « success» quand terminé sans erreurs,
    "cartes" : [
        {
            "id" : (chaîne) Identifiant API de la carte,
            "type" : (chaîne) type de la carte - NewsItem (cartes classiques), CaptionedImage, Bannière
            "title" : (chaîne) titre de la carte,
            "tags" : (tableau) noms de balises associés à la carte
        },
...
    ]
}
```
{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
