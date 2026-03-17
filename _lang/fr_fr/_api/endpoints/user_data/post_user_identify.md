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

> Utilisez cet endpoint pour identifier un utilisateur non identifié (alias uniquement, e-mail uniquement ou numéro de téléphone uniquement) à l'aide de l'ID externe fourni.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## Fonctionnement

L'appel à `/users/identify` combine un profil utilisateur identifié par un alias (profil alias seul), une adresse e-mail (profil e-mail seul) ou un numéro de téléphone (profil numéro de téléphone seul) avec un profil utilisateur possédant un `external_id` (profil identifié), puis supprime le profil alias seul.

L'identification d'un utilisateur nécessite qu'une adresse `external_id` soit incluse dans les objets suivants :

- `aliases_to_identify`
- `emails_to_identify`
- `phone_numbers_to_identify`

S'il n'existe aucun utilisateur avec cet identifiant`external_id`, celui-ci`external_id`est ajouté à l'enregistrement de l'utilisateur aliasé, et l'utilisateur est considéré comme identifié. Les utilisateurs ne peuvent disposer que d'un seul alias pour une étiquette spécifique. Si un utilisateur existe déjà avec le`external_id`  et dispose d'un alias existant avec le même libellé d'alias que le profil alias uniquement, les profils utilisateur ne sont pas fusionnés.

{% alert tip %}
Pour éviter toute perte inattendue de données lors de l'identification des utilisateurs, nous vous recommandons vivement de vous reporter d'abord aux [meilleures pratiques en]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) matière de [collecte de données]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) pour savoir comment capturer les données des utilisateurs lorsque des informations sur les utilisateurs sous forme d'alias seulement sont déjà présentes.
{% endalert %}

### Comportement de fusion

Par défaut, cet endpoint fusionne la liste suivante de champs trouvés **exclusivement** sur l'utilisateur anonyme avec l'utilisateur identifié.

{% details List of fields that are merged %}
- Prénom
- Nom de famille
- e-mail
- Genre
- Date de naissance
- Numéro de téléphone
- Fuseau horaire
- Ville d'origine
- Pays
- Langue
- Décompte des sessions (la somme des sessions des deux profils)
- Date de la première session (Braze sélectionne la date la plus proche des deux dates)
- Date de la dernière session (Braze sélectionne la date la plus récente parmi les deux dates)
- Attributs personnalisés
- Données d'événements personnalisés et d'événements d'achat
- Propriétés d'événement personnalisé et d'événement d'achat pour la segmentation « X fois en Y jours » (oùX<=50et Y<=30)
- Résumé des événements personnalisés pouvant être segmentés
  - Nombre d’événements (la somme des deux profils)
  - Date à laquelle l'événement s'est produit pour la première fois (Braze sélectionne la date la plus ancienne parmi les deux dates)
  - Dernière occurrence de l'événement (Braze sélectionne la date la plus récente parmi les deux dates)
- Total des achats intégrés à l’application en centimes (la somme des deux profils)
- Nombre total d’achats (la somme des deux profils)
- Date du premier achat (Braze sélectionne la date la plus ancienne parmi les deux dates)
- Date du dernier achat (Braze sélectionne la date la plus récente parmi les deux dates)
- Résumés des applications
- Last_X_at champs (Braze met à jour les champs si les champs du profil orphelin sont plus récents)
- Résumés de campagne (Braze sélectionne les champs de date les plus récents)
- Résumés du flux de travail (Braze sélectionne les champs de date les plus récents)
- Message et historique d’engagement du message
- Nombre d’événements d’achats et personnalisés, ainsi que les horodatages correspondant à la première et dernière dates
  - Ces champs fusionnés mettent à jour les filtres « pour X événements en Y jours ». Pour les événements d’achat, ces filtres incluent « nombre d’achats en Y jours » et « argent dépensé au cours des Y derniers jours ».
- Données de session si l'application existe sur les deux profils utilisateurs.
  - Par exemple, si notre utilisateur cible ne dispose pas d'un résumé d'application pour « ABCApp », mais que notre utilisateur d'origine en possède un, l'utilisateur cible aura le résumé d'application « ABCApp » sur son profil utilisateur après la fusion.
{% enddetails %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l’autorisation `users.identify`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='users identify' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects),
   "emails_to_identify": (optional, array of alias to identify objects) User emails to identify,
   "phone_numbers_to_identify": (optional, array of alias to identify objects) User phone numbers to identify,
},
```

### Paramètres de demande

Vous pouvez ajouter jusqu’à 50 alias utilisateur par demande. Vous pouvez associer plusieurs alias utilisateur supplémentaires à un seul `external_id`.

{% alert important %}
L'un des éléments suivants est requis : `aliases_to_identify`, `emails_to_identify`, ou `phone_numbers_to_identify` par demande. Par exemple, vous pouvez utiliser cet endpoint pour identifier les utilisateurs par e-mail en utilisant `emails_to_identify` dans votre requête.
{% endalert %}

| Paramètre                   | Requis | Type de données                           | Description                                                                                                                                                                 |
|-----------------------------|----------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `aliases_to_identify`       | Requis | Tableau d’alias pour identifier l’objet | Voir [alias pour identifier l'objet]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) et [alias d'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `emails_to_identify`        | Requis | Tableau d’alias pour identifier l’objet | Requis si `email` est spécifié comme identifiant. Adresses e-mail pour identifier les utilisateurs. Voir [Identification des utilisateurs par e-mail](#identifying-users-by-email).                                                                                                              |
| `phone_numbers_to_identify` | Requis | Tableau d’alias pour identifier l’objet | Numéros de téléphone pour identifier les utilisateurs.                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Identification des utilisateurs par leurs adresses e-mail et leurs numéros de téléphone

Si une adresse e-mail ou un numéro de téléphone est spécifié comme identifiant, vous devez également inclure `prioritization` dans l'identifiant.

Il`prioritization`doit s'agir d'un tableau spécifiant quel utilisateur fusionner si plusieurs utilisateurs sont trouvés.`prioritization`Il s'agit d'un tableau ordonné, ce qui signifie que si plusieurs utilisateurs correspondent à une priorité, la fusion n'a pas lieu.

Les valeurs autorisées pour le tableau sont les suivantes :

- `identified`
- `unidentified`
- `most_recently_updated` (Priorité à l'utilisateur le plus récemment mis à jour)
- `least_recently_updated` (Priorité à l'utilisateur le moins récemment mis à jour)

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
}'
```

{% alert tip %}
Pour plus d'informations sur `alias_name` et `alias_label`, consultez notre documentation sur les [alias utilisateurs.]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
{% endalert %}

## Réponse

```json
{
    "aliases_processed": 1,
    "message": "success"
}
```

{% endapi %}
