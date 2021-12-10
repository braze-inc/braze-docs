---
nav_title: "POST: Identifier les utilisateurs"
permalink: /fr/users_identifiant_merge/
hidden: vrai
layout: api_page
---

{% api %}
# Identifier les utilisateurs
{% apimethod post %}
/fr/users/identify
{% endapimethod %}

Utilisez ce point de terminaison pour identifier un utilisateur non identifié (alias seulement).

{% alert important %}
La prise en charge du champ `merge_behavior` est actuellement en accès anticipé. Veuillez contacter votre responsable de compte Braze si vous êtes intéressé à participer à l'accès anticipé.
{% endalert %}

L'identification d'un utilisateur nécessite qu'un `external_id` soit inclus dans l'objet `aliases_to_identify`. S'il n'y a pas d'utilisateur avec ce `external_id`, le `external_id` sera simplement ajouté à l'enregistrement de l'utilisateur aliasé, et l'utilisateur sera considéré comme identifié. Vous pouvez ajouter jusqu'à 50 alias par requête.

Par la suite, vous pouvez associer plusieurs alias utilisateurs supplémentaires avec un seul `external_id`.
- Lorsque ces associations suivantes sont faites avec le champ `fuge_behavior` réglé à `none`, seuls les jetons push et l'historique des messages associés à l'alias de l'utilisateur sont conservés ; tous les attributs, événements ou achats seront "orphelins" et ne seront pas disponibles sur l'utilisateur identifié. One workaround is to export the aliased user's data before identification using the [`/users/export/ids` endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_user_identify/), then re-associate the attributes, events, and purchases with the identified user.
- Lorsque les associations sont faites avec le champ `merge_behavior` réglé à `fusionner`, ce point de terminaison fusionnera les [champs spécifiques](#merge) trouvés exclusivement sur l'utilisateur anonyme à l'utilisateur identifié.

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
   "aliases_to_identify" : (requis, table d'alias pour identifier les objets), 
   "merge_behavior": (optionnel, chaîne) on attend un de 'none' ou 'fusion'
}
```

### Paramètres de la requête

| Paramètre                   | Requis    | Type de données                         | Libellé                                                                                                                                                                                   |
| --------------------------- | --------- | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `alias pour identifier`     | Requis    | Tableau d'alias pour identifier l'objet | Voir [alias pour identifier l'objet]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) et l'objet alias utilisateur []({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `Fusionner le comportement` | Optionnel | Chaîne de caractères                    | Une des `aucune` ou `fusion` est attendue.                                                                                                                                                |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

#### Champ fusion_comportement {#merge}

Définir le champ `fuge_behavior` à `fusionner` définit le point de terminaison pour fusionner l'un des champs suivants trouvés exclusivement sur l'utilisateur anonyme à l'utilisateur identifié:
- Prénom
- Nom de famille
- Courriel
- Sexe
- Date de naissance
- Numéro de téléphone
- Fuseau horaire
- Ville natale
- Pays
- Langue
- Données personnalisées (excluant les propriétés de l'événement)
- Acheter les données de l'événement (hors propriétés d'achat)

{% alert warning %}
Les attributs suivants ne sont pas encore pris en charge :
- Données de session
- Événement personnalisé ou achat de propriétés pour la segmentation
{% endalert %}

Définir le champ à `aucun` maintiendra la fonctionnalité actuelle décrite ci-dessus.

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
  ],
  "fusion_comportement": "fusion"
}'
```

Pour plus d'informations sur `alias_name` et `alias_label`, consultez notre documentation [alias utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).

{% endapi %}