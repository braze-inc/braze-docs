---
nav_title: "POST: Créer un nouvel alias d'utilisateur"
article_title: "POST: Créer un nouvel alias d'utilisateur"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur la création de nouveaux alias utilisateur Braze terminpoint de terminaison de Braze."
---

{% api %}
# Créer un nouvel alias utilisateur
{% apimethod post %}
/fr/users/alias/new
{% endapimethod %}

Utilisez ce point de terminaison pour ajouter de nouveaux alias pour les utilisateurs identifiés existants, ou pour créer de nouveaux utilisateurs non identifiés.

{% alert note %}
Vous pouvez ajouter jusqu'à 50 alias par requête.
{% endalert %}

__L'ajout d'un alias utilisateur pour un utilisateur existant__ nécessite l'inclusion d'un `external_id` dans l'objet alias nouvel utilisateur. Si le `external_id` est présent dans l'objet mais qu'il n'y a aucun utilisateur avec ce `external_id`, l'alias ne sera ajouté à aucun utilisateur. Si un `external_id` n'est pas présent, un utilisateur sera toujours créé mais devra être identifié plus tard. Vous pouvez le faire en utilisant "Identifier les utilisateurs" et le point de terminaison `utilisateurs/identifier`.

__La création d'un nouvel utilisateur uniquement alias__ nécessite que le `external_id` soit omis du nouvel objet alias utilisateur. Une fois que l'utilisateur est créé, utilisez le point de terminaison `/users/track` pour associer l'utilisateur uniquement avec des attributs, des événements, et achats, et le point de terminaison `/users/identify` pour identifier l'utilisateur avec un `external_id`.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

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
   "user_aliases" : (requis, tableau de nouvel objet alias utilisateur)
}
```

### Paramètres de la requête

| Paramètre           | Requis | Type de données                                    | Libellé                                                                                                                                                                                                                                                                                                                                   |
| ------------------- | ------ | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Alias utilisateur` | Requis | Tableau des nouveaux objets alias de l'utilisateur | Voir [l'objet alias utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/).<br><br> Pour plus d'informations sur `alias_name` et `alias_label`, Consultez notre documentation [Alias d'utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Corps de la requête de point de terminaison avec la nouvelle spécification de l'objet alias utilisateur

```json
{
  "external_id" : (optionnel, string) voir l'identifiant utilisateur externe ci-dessous,
  "alias_name" : (requis, chaîne),
  "alias_label" : (requis, chaîne)
}
```

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze. om/users/alias/new' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "user_aliases" : 
  [
    {
      "external_id": "external_identifier",
      "alias_name" : "example_name",
      "alias_label" : "example_label"
    }
  ]
}'
```

{% endapi %}

