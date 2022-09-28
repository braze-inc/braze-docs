---
nav_title: "POST : Identifier les utilisateurs"
permalink: /users_identify_merge/
hidden: true
layout: api_page

---
{% api %}
# Identifier les utilisateurs
{% apimethod post %}
/users/identify
{% endapimethod %}

Utilisez cet endpoint pour identifier un utilisateur non identifié (alias uniquement).

{% alert important %}
La prise en charge du champ `merge_behavior` est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

Identifier un utilisateur nécessite un `external_id` à inclure dans l’objet `aliases_to_identify`. S’il n’y a pas d’utilisateur avec cet `external_id`, `external_id` sera simplement ajouté au dossier de l’utilisateur alias, et l’utilisateur sera considéré comme identifié. Vous pouvez ajouter jusqu’à 50 alias d’utilisateurs par demande. 

Ensuite, vous pouvez associer plusieurs alias d’utilisateur supplémentaires à un seul `external_id`. 
- Lorsque ces associations ultérieures sont effectuées avec le champ `merge_behavior` défini sur `none`, seuls les jetons de notification push et l'historique des messages associés à l'alias d’utilisateur sont conservés. Tous les attributs, événements ou achats deviendront « orphelins » et non disponibles pour l'utilisateur identifié. Il existe une solution qui consiste à exporter les données de l’utilisateur alias avant l’identification en utilisant le [`/users/export/ids`endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_user_identify/), puis à associer de nouveau les attributs, événements et achats à l’utilisateur identifié.
- Lorsque des associations sont faites avec le champ `merge_behavior` défini sur `merge`, cet endpoint fusionnera les [champs spécifiques](#merge) de l’utilisateur anonyme avec ceux de l’utilisateur identifié.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

{% alert note %}
Une limite de débit est appliquée aux demandes faites au niveau de cet endpoint pour les clients qui ont rejoint Braze le 16 septembre 2021 ou plus tard. Pour plus d’informations, consultez les [limites API]({{site.baseurl}}/api/basics/#api-limits).
{% endalert %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects), 
   "merge_behavior": (optional, string) one of 'none' or 'merge' is expected
}
```

### Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| -----------|----------| --------|------- |
| `aliases_to_identify` | Requis | Tableau d’alias pour identifier les objets | Voir [alias pour identifier l’objet]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) et [l’objet alias d’utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `merge_behavior` | Facultatif | Chaîne de caractères | Un des deux éléments, `none` ou `merge`, est attendu.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

#### Fusionner_champ de comportement {#merge}

Configurer le champ `merge_behavior` sur `merge` permet de définir l’endpoint à fusionner :

L’un des champs suivants a été trouvé **exclusivement** sur l’utilisateur anonyme ou l’utilisateur identifié :
- Prénom
- Nom
- E-mail
- Sexe
- Date de naissance
- Numéro de téléphone
- Fuseau horaire
- Ville d’origine
- Pays
- Langue
- Attributs personnalisés
- Données sur les événements d’achats et personnalisés (sauf propriétés d’événements, compte, horodatages correspondant à la première et dernière dates)
- Propriétés d’événements d’achats et personnalisées pour la segmentation « X fois en Y jours » (où X <= 50 et Y <= 30)

L’un des champs suivants a été trouvé sur l’utilisateur anonyme ou l’utilisateur identifié :
- Nombre d’événements d’achats et personnalisés, ainsi que les horodatages correspondant à la première et dernière dates 
  - Ces champs fusionnés mettront à jour les filtres « pour X événements en Y jours ». Pour les événements d’achat, ces filtres incluent « nombre d’achats en Y jours » et « argent dépensé au cours des Y derniers jours ».

{% alert warning %}
Les attributs suivants ne sont pas encore pris en charge :
- Données de session 
{% endalert %}

Configurer le champ sur `none` ne fusionnera aucune donnée utilisateur avec le profil utilisateur identifié.

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/identify' \
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
  "merge_behavior": "merge"
}'
```

Pour plus d’informations sur `alias_name` et `alias_label`, consultez notre [documentation sur les alias utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).

{% endapi %}