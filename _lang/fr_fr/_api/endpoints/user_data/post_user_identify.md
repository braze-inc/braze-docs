---
nav_title: "POST : Identifier les utilisateurs"
article_title: "POST : Identifier les utilisateurs"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
alias: /users_identify_merge/
description: "Cet article présente en détail l’endpoint Braze Identifier les utilisateurs."

---
{% api %}
# Identifier les utilisateurs
{% apimethod post %}
/users/identify
{% endapimethod %}

> Utilisez cet endpoint pour identifier un utilisateur non identifié (alias uniquement). 

{% alert important %}
À compter du 7 août 2023, cet endpoint fusionnera les données de tous les appels. Cela signifie que [`merge_behavior`](#merge) sera réglé sur `merge` pour tous les appels.
{% endalert %}

Appeler `/users/identify` combine le profil alias uniquement avec le profil identifié, et supprime le profil alias uniquement.

Identifier un utilisateur nécessite un `external_id` à inclure dans l’objet `aliases_to_identify`. Si aucun utilisateur ne porte cet `external_id`, l’`external_id` sera simplement ajouté au dossier de l’utilisateur alias, et l’utilisateur sera considéré comme identifié. Vous pouvez ajouter jusqu’à 50 alias utilisateur par demande.

Ensuite, vous pouvez associer plusieurs alias d’utilisateur supplémentaires à un seul `external_id`. 
- Lorsque ces associations ultérieures sont effectuées avec le champ `merge_behavior` défini sur `none`, seuls les jetons de notification push et l’historique des messages associés à l’alias d’utilisateur sont conservés. Tous les attributs, événements ou achats deviendront « orphelins » et non disponibles pour l’utilisateur identifié. Une solution consiste à exporter les données de l'utilisateur aliasé avant l'identification à l'aide de l' [endpoint`/users/export/ids` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/), puis à réassocier les attributs, les événements et les achats à l'utilisateur identifié.
- Lorsque des associations sont faites avec le champ `merge_behavior` défini sur `merge`, cet endpoint fusionnera les [champs spécifiques](#merge) trouvés sur l'utilisateur anonyme avec ceux de l'utilisateur identifié.

{% alert tip %}
Pour éviter toute perte inattendue de données lors de l'identification des utilisateurs, nous vous recommandons vivement de vous reporter d'abord aux [meilleures pratiques en]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) matière de [collecte de données]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) pour savoir comment capturer les données des utilisateurs lorsque des informations sur les utilisateurs sous forme d'alias seulement sont déjà présentes.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l’autorisation `users.identify`.

## Limite de débit 
Une limite de débit est appliquée aux demandes faites au niveau de cet endpoint pour les clients qui ont rejoint Braze le 16 septembre 2021 ou plus tard. Pour plus d'informations, consultez [Limites de l'API]({{site.baseurl}}/api/basics/#api-limits).

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects), 
   "merge_behavior": (optional, string) one of 'none' or 'merge' is expected
}
```

### Paramètres de demande

| Paramètre             | Requis | Type de données                           | Description                                                                                                                                                                 |
| --------------------- | -------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aliases_to_identify` | Requis | Tableau d’alias pour identifier l’objet | Voir [alias pour identifier l'objet]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) et [alias d'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `merge_behavior`      | Facultatif | Chaîne de caractères                              | `merge` ou  est attendu.                                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

#### Champ Merge_behavior {#merge}

Définir le champ `merge_behavior` sur `merge` paramètre l’endpoint pour fusionner tous les champs suivants trouvés **exclusivement** depuis l’utilisateur anonyme vers l’utilisateur identifié. 
- Prénom
- Nom
- E-mail
- Genre
- Date de naissance
- Numéro de téléphone
- Fuseau horaire
- Ville d’origine
- Pays
- Langue
- Décompte des sessions (la somme des sessions des deux profils)
- Date de la première session (Braze choisira la date la plus ancienne parmi les deux)
- Date de la dernière session (Braze choisira la date la plus récente parmi les deux)
- Attributs personnalisés
- Données d'événements personnalisés et d'événements d'achat
- Propriétés de l’événement d’achat et personnalisées pour la segmentation « X fois en Y jours » (où X <= 50 et Y <= 30)
- Résumé des événements personnalisés pouvant être segmentés
  - Nombre d’événements (la somme des deux profils)
  - Événement survenu pour la première fois (Braze choisira la date la plus ancienne parmi les deux)
  - Événement survenu pour la dernière fois (Braze choisira la date la plus récente parmi les deux)
- Total des achats intégrés à l’application en centimes (la somme des deux profils)
- Nombre total d’achats (la somme des deux profils)
- Date du premier achat (Braze choisira la date la plus ancienne parmi les deux)
- Date du dernier achat (Braze choisira la date la plus récente parmi les deux)
- Résumés des applications
- Champs Last_X_at (Braze mettra à jour les champs si les champs du profil orphelins sont plus récents).
- Résumés de campagne (Braze choisira les champs de date les plus récents)
- Résumés du flux de travail (Braze choisira les champs de date les plus récents)
- Message et historique d’engagement du message

L’un des champs suivants a été trouvé sur l’utilisateur anonyme ou l’utilisateur identifié :
- Nombre d’événements d’achats et personnalisés, ainsi que les horodatages correspondant à la première et dernière dates 
  - Ces champs fusionnés mettront à jour les filtres « pour X événements en Y jours ». Pour les événements d’achat, ces filtres incluent « nombre d’achats en Y jours » et « argent dépensé au cours des Y derniers jours ».

Les données de session ne seront fusionnées que si l’application existe sur les deux profils utilisateurs. Par exemple, si votre utilisateur cible ne dispose pas d’un résumé d’application pour « ABCApp », mais que votre utilisateur d’origine l’a, l’utilisateur cible disposera du résumé d’application pour « ABCApp » sur son profil après la fusion. 

Configurer le champ sur `none` ne fusionnera aucune donnée utilisateur avec le profil utilisateur identifié.

### Identifier les utilisateurs par e-mail
Si un `email` est spécifié comme identifiant, une valeur `prioritization` supplémentaire est requise dans l'identifiant. `prioritization` doit être un tableau spécifiant l'utilisateur à fusionner s'il y a plusieurs utilisateurs trouvés. `prioritization` est un tableau ordonné, ce qui signifie que si plus d'un utilisateur correspond à un ordre de priorité, la fusion n'aura pas lieu.

Les valeurs autorisées pour le tableau sont les suivantes : `identified`, `unidentified`, `most_recently_updated`. `most_recently_updated` signifie que la priorité est accordée à l'utilisateur ayant effectué la dernière mise à jour.

Une seule des options suivantes peut exister à la fois dans le tableau de priorisation :
- `identified` Il s'agit de donner la priorité à un utilisateur ayant une `external_id`
- `unidentified` Il s'agit de donner la priorité à un utilisateur qui n'a pas de `external_id`

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/identify' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "aliases_to_identify": [
    {
      "external_id": "external_identifier",
      "user_alias": {
          "alias_name": "example_alias",
          "alias_label": "example_label"
      }
    }
  ],
  "emails_to_identify": [
    {
      "external_id": "external_identifier_2",
      "email": "john.smith@braze.com",
      "prioritization": ["unidentified", "most_recently_updated"]
    }
  ]
  "merge_behavior": "merge"
}'
```

{% alert tip %}
Pour plus d'informations sur `alias_name` et `alias_label`, consultez notre documentation sur les [alias utilisateurs.]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) 
{% endalert %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
    "aliases_processed": 1,
    "message": "success"
}
```

{% endapi %}
