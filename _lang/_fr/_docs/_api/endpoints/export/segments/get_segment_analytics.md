---
nav_title: "GET: Analyses de segment"
article_title: "GET: Analyses de segment"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails et l'utilisation du point de terminaison Get Segment Analytics."
---

{% api %}
# Point de terminaison d'analyse du segment
{% apimethod get %}
/fr/segments/data_series
{% endapimethod %}

Ce point de terminaison vous permet de récupérer une série quotidienne de la taille estimée d'un segment au fil du temps pour un segment.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e {% endapiref %}

## Paramètres de la requête

| Paramètre             | Requis    | Type de données                                                                | Libellé                                                                                                                                                                                                                                                                                                                                         |
| --------------------- | --------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `identifiant_segment` | Requis    | Chaîne de caractères                                                           | Voir [l'identifiant API du segment]({{site.baseurl}}/api/identifier_types/).<br><br> Le `segment_id` pour un segment donné peut être trouvé dans votre **Console développeur** dans votre compte Braze ou vous pouvez utiliser le [point d'extrémité de la liste des segments]({{site.baseurl}}/api/endpoints/export/get_segment/). |
| `Longueur`            | Requis    | Nombre entier                                                                  | Nombre maximum de jours avant `ending_at` pour inclure dans la série retournée. Doit être compris entre 1 et 100 (inclus).                                                                                                                                                                                                                      |
| `finalisation_à`      | Optionnel | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) chaîne) | Date à laquelle la série de données doit se terminer. Par défaut, l'heure de la requête.                                                                                                                                                                                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/data_series?segment_id={{segment_identifier}}&length=14&ending_at=2018-06-27T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (requis, chaîne) le statut de l'exportation, retourne 'success' lorsqu'il est terminé sans erreurs,
    "données" : [
        {
            "temps" : (chaîne) date comme date ISO 8601,
            "taille" : (int) taille du segment à cette date
        },
...
    ]
}
```
{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
