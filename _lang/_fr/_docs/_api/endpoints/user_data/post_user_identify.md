---
nav_title: "POST: Identifier les utilisateurs"
article_title: "POST: Identifier les utilisateurs"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison Identifier les utilisateurs Braze."
---

{% api %}
# Identifier les utilisateurs
{% apimethod post %}
/fr/users/identify
{% endapimethod %}

Utilisez ce point de terminaison pour identifier un utilisateur non identifié (alias seulement).

{% alert note %}
Vous pouvez ajouter jusqu'à 50 alias par requête.
{% endalert %}

L'identification d'un utilisateur nécessite qu'un `external_id` soit inclus dans l'objet `aliases_to_identify`. S'il n'y a pas d'utilisateur avec ce `external_id`, le `external_id` sera simplement ajouté à l'enregistrement de l'utilisateur aliasé, et l'utilisateur sera considéré comme identifié.

Par la suite, vous pouvez associer plusieurs alias utilisateurs supplémentaires avec un seul `external_id`. Lorsque ces associations suivantes sont faites, seuls les jetons push et l'historique des messages associés à l'alias de l'utilisateur sont conservés ; tous les attributs, événements ou achats seront "orphelins" et ne seront pas disponibles sur l'utilisateur identifié. One workaround is to export the aliased user's data before identification using the [`/users/export/ids` endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_user_identify/), then re-associate the attributes, events, and purchases with the identified user.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

{% alert note %}
Une limite de taux est appliquée aux demandes faites à ce point de terminaison pour les clients embarqués avec Braze le ou après le 16 septembre 2021. Pour plus d'informations, voir [les limites de l'API]({{site.baseurl}}/api/basics/#api-limits).
{% endalert %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
   "aliases_to_identify" : (requis, table d'alias pour identifier les objets)
}
```

### Paramètres de la requête

| Paramètre               | Requis | Type de données                         | Libellé                                                                                                                                                                                   |
| ----------------------- | ------ | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `alias pour identifier` | Requis | Tableau d'alias pour identifier l'objet | Voir [alias pour identifier l'objet]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) et l'objet alias utilisateur []({{site.baseurl}}/api/objects_filters/user_alias_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de requête
```
curl --location --request POST 'https://rest.iad-01.braze. om/users/identify' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "aliases_to_identify" : 
  [
    {
      "external_id": "external_identifier",
      "user_alias" : {
          "alias_name" : "example_alias",
          "alias_label" : "example_label"
      }
    }
  ]
}'
```

Pour plus d'informations sur `alias_name` et `alias_label`, consultez notre documentation [alias utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).

{% endapi %}

