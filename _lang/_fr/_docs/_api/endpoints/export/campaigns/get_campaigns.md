---
nav_title: "GET: Liste des campagnes"
article_title: "GET: Listes de Campagnes"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison Get Campaigns Liste."
---

{% api %}
# Fin de la liste des campagnes
{% apimethod get %}
/fr/campaigns/list
{% endapimethod %}

Ce point de terminaison vous permet d'exporter une liste de campagnes, dont chacune inclura son nom, identifiant API de la campagne, qu'il s'agisse d'une campagne de l'API, et des tags associés à la campagne. Les campagnes sont retournées en groupes de 100 triés par date de création (du plus ancien au plus récent par défaut).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18 {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

## Paramètres de la requête

| Paramètre                         | Requis    | Type de données      | Libellé                                                                                                                                                                                                                                                                                                                  |
| --------------------------------- | --------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `page`                            | Optionnel | Nombre entier        | La page des campagnes à retourner, par défaut à 0 (retourne le premier ensemble jusqu'à 100).                                                                                                                                                                                                                            |
| `include_archivé`                 | Optionnel | Boolean              | Si oui ou non inclure des campagnes archivées, la valeur par défaut est false.                                                                                                                                                                                                                                           |
| `direction_tri`                   | Optionnel | Chaîne de caractères | - Trier le temps de création du plus récent au plus ancien : passer dans la valeur `desc`.<br> - Trier le temps de création de la plus ancienne à la plus récente : passer dans la valeur `asc`. <br><br>Si `sort_direction` n'est pas incluse, l'ordre par défaut est plus ancien que le plus récent. |
| `Dernière_modification.heure[gt]` | Optionnel | Date et heure        | Filtre les résultats et ne renvoie que les campagnes qui ont été éditées plus grand que le temps fourni jusqu'à présent. Le format est `yyyy-MM-DDTHH:mm:ss`.                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/list?page=0&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse de l'API de la liste des campagnes

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (requis, chaîne) le statut de l'exportation, retourne « success» quand terminé sans erreurs,
    "campagnes" : [
        {
            "id" : (string) Identifiant API de la campagne,
            "last_editeded": (chaîne ISO 8601) la dernière fois pour le message 
            "name" : (string) nom de la campagne,
            "is_api_campaign" : (boolean) si la campagne est une campagne API,
            "tags" : (tableau) noms de balises associés à la campagne
        },
...
    ]
}
```

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
