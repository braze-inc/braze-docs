---
nav_title: "GET: Segment Details"
article_title: "GET: Segment Details"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails et l'utilisation du point de terminaison des détails des segments pour exporter une liste des segments disponibles."
---

{% api %}
# Point de terminaison des détails du segment
{% apimethod get %}
/fr/segments/details
{% endapimethod %}

Ce point de terminaison vous permet de récupérer des informations pertinentes sur le segment, qui peuvent être identifiées par le `segment_id`.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aab56ed9-0a28-476a-8b57-b79786dbb9c1 {% endapiref %}

## Paramètres de la requête

| Paramètre             | Requis | Type de données      | Libellé                                                                                                                                                                                                                                                                                                                                         |
| --------------------- | ------ | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `identifiant_segment` | Requis | Chaîne de caractères | Voir [l'identifiant API du segment]({{site.baseurl}}/api/identifier_types/).<br><br> Le `segment_id` pour un segment donné peut être trouvé dans votre **Console développeur** dans votre compte Braze ou vous pouvez utiliser le [point d'extrémité de la liste des segments]({{site.baseurl}}/api/endpoints/export/get_segment/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/details?segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
      "message": (requis, chaîne) le statut de l'exportation, retourne 'success' lorsqu'il est terminé sans erreurs,
      "created_at" : (chaîne) date créée en tant que date ISO 8601,
      "updated_at" : (chaîne) date dernière mise à jour en tant que date ISO 8601,
      "nome" : (chaîne) nom de segment,
      "description" : (chaîne) description lisible par l'homme des filtres,
      "text_description" : (string) description du segment, 
      "tags" : (tableau) noms de balises associés au segment
}
```
{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
