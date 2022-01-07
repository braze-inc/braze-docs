---
nav_title: "GET: Informations sur la carte des actualités"
article_title: "GET: Informations sur la carte des actualités"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison de la fiche de nouvelles ."
---

{% api %}
# Point de terminaison des détails de la carte de flux d'actualités
{% apimethod get %}
/feed/details
{% endapimethod %}

Ce point de terminaison vous permet de récupérer des informations pertinentes sur la carte, qui peuvent être identifiées par la `card_id`.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5b1401a6-f12c-4827-82c9-8dc604f1671e {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

## Paramètres de la requête

| Paramètre        | Requis | Type de données      | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------- | ------ | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id de la carte` | Requis | Chaîne de caractères | Voir [Identifiant API de la carte]({{site.baseurl}}/api/identifier_types/). <br><br> La `card_id` pour une carte donnée peut être trouvée dans la page **Console développeur** et sur la page de détails de la carte dans votre tableau de bord, ou vous pouvez utiliser le [Point de terminaison de la liste des fils d'actualités]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/feed/details?card_id={{card_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (requis, string) Le statut de l'exportation, retourne 'success' lorsqu'il est terminé sans erreurs,
    "created_at" : (chaîne) Date créée en tant que date ISO 8601,
    "updated_at" : (chaîne) Date mise à jour en date ISO 8601,
    "name" : (string) Card name,
    "publish_at" : (chaîne) La carte a été publiée en date ISO 8601,
    "end_at" : (chaîne) La carte de date s'arrêtera de s'afficher pour les utilisateurs sous la date ISO 8601,
    "tags" : (tableau) Noms d'étiquettes associés à la carte,
    "title" : (chaîne) Titre de la carte,
    "image_url" : (string) URL de l'image utilisée par cette carte,
    "extras" : dictionnaire contenant les données de la paire de valeurs clés attachées à cette carte,
    "description" : (chaîne) Texte de description utilisé par cette carte,
    "archivé" : (booléen) si cette carte est archivée,
    "brouillon": (booléen) si cette carte est un brouillon,
}
```
{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
