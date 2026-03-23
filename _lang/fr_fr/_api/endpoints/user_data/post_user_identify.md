---
nav_title: "POST : Identifier les utilisateurs"
article_title: "POST : Identifier les utilisateurs"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
alias: /users_identify_merge/
description: "Cet article présente en détail l'endpoint Braze Identifier les utilisateurs."

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

L'identification d'un utilisateur nécessite qu'un `external_id` soit inclus dans les objets suivants :

- `aliases_to_identify`
- `emails_to_identify`
- `phone_numbers_to_identify`

S'il n'existe aucun utilisateur avec cet `external_id`, celui-ci est ajouté à l'enregistrement de l'utilisateur aliasé, et l'utilisateur est considéré comme identifié. Les utilisateurs ne peuvent disposer que d'un seul alias pour une étiquette spécifique. Si un utilisateur existe déjà avec l'`external_id` et dispose d'un alias existant avec la même étiquette que le profil alias uniquement, les profils utilisateur ne sont pas fusionnés.

{% alert tip %}
Pour éviter toute perte inattendue de données lors de l'identification des utilisateurs, nous vous recommandons vivement de consulter d'abord les [bonnes pratiques de collecte de données]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) pour savoir comment capturer les données des utilisateurs lorsque des informations d'alias uniquement sont déjà présentes.
{% endalert %}

### Comportement de fusion

Par défaut, cet endpoint fusionne la liste suivante de champs trouvés **exclusivement** sur l'utilisateur anonyme avec l'utilisateur identifié.

{% details Liste des champs fusionnés %}
- Prénom
- Nom de famille
- E-mail
- Genre
- Date de naissance
- Numéro de téléphone
- Fuseau horaire
- Ville d'origine
- Pays
- Langue
- Nombre de sessions (la somme des sessions des deux profils)
- Date de la première session (Braze sélectionne la date la plus ancienne des deux)
- Date de la dernière session (Braze sélectionne la date la plus récente des deux)
- Attributs personnalisés
- Données d'événements personnalisés et d'événements d'achat
- Propriétés d'événement personnalisé et d'événement d'achat pour la segmentation « X fois en Y jours » (où X<=50 et Y<=30)
- Résumé des événements personnalisés segmentables
  - Nombre d'événements (la somme des deux profils)
  - Date de première occurrence de l'événement (Braze sélectionne la date la plus ancienne des deux)
  - Date de dernière occurrence de l'événement (Braze sélectionne la date la plus récente des deux)
- Total des achats in-app en centimes (la somme des deux profils)
- Nombre total d'achats (la somme des deux profils)
- Date du premier achat (Braze sélectionne la date la plus ancienne des deux)
- Date du dernier achat (Braze sélectionne la date la plus récente des deux)
- Résumés des applications
- Champs Last_X_at (Braze met à jour les champs si ceux du profil orphelin sont plus récents)
- Résumés de campagne (Braze sélectionne les champs de date les plus récents)
- Résumés du flux de travail (Braze sélectionne les champs de date les plus récents)
- Message et historique d'engagement des messages
- Nombre d'événements personnalisés et d'événements d'achat, ainsi que les horodatages de première et dernière date
  - Ces champs fusionnés mettent à jour les filtres « pour X événements en Y jours ». Pour les événements d'achat, ces filtres incluent « nombre d'achats en Y jours » et « argent dépensé au cours des Y derniers jours ».
- Données de session si l'application existe sur les deux profils utilisateur
  - Par exemple, si l'utilisateur cible ne dispose pas d'un résumé d'application pour « ABCApp », mais que l'utilisateur d'origine en possède un, l'utilisateur cible aura le résumé d'application « ABCApp » sur son profil après la fusion.
{% enddetails %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l'autorisation `users.identify`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='users identify' %}

## Corps de la requête

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

### Paramètres de requête

Vous pouvez ajouter jusqu'à 50 alias utilisateur par requête. Vous pouvez associer plusieurs alias utilisateur supplémentaires à un seul `external_id`.

{% alert important %}
L'un des éléments suivants est requis par requête : `aliases_to_identify`, `emails_to_identify` ou `phone_numbers_to_identify`. Par exemple, vous pouvez utiliser cet endpoint pour identifier les utilisateurs par e-mail en utilisant `emails_to_identify` dans votre requête.
{% endalert %}

| Paramètre                   | Requis | Type de données                           | Description                                                                                                                                                                 |
|-----------------------------|----------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `aliases_to_identify`       | Requis | Tableau d'objets alias à identifier | Voir [objet alias à identifier]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) et [objet alias d'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `emails_to_identify`        | Requis | Tableau d'objets alias à identifier | Requis si `email` est spécifié comme identifiant. Adresses e-mail pour identifier les utilisateurs. Voir [Identification des utilisateurs par e-mail](#identifying-users-by-email).                                                                                                              |
| `phone_numbers_to_identify` | Requis | Tableau d'objets alias à identifier | Numéros de téléphone pour identifier les utilisateurs.                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Identification des utilisateurs par adresses e-mail et numéros de téléphone

Si une adresse e-mail ou un numéro de téléphone est spécifié comme identifiant, vous devez également inclure `prioritization` dans l'identifiant.

Le champ `prioritization` doit être un tableau spécifiant quel utilisateur fusionner si plusieurs utilisateurs sont trouvés. `prioritization` est un tableau ordonné, ce qui signifie que si plusieurs utilisateurs correspondent à partir d'une priorité donnée, la fusion n'a pas lieu.

Les valeurs autorisées pour le tableau sont les suivantes :

- `identified`
- `unidentified`
- `most_recently_updated` (priorité à l'utilisateur le plus récemment mis à jour)
- `least_recently_updated` (priorité à l'utilisateur le moins récemment mis à jour)

Une seule des options suivantes peut figurer à la fois dans le tableau de priorisation :

- `identified` donne la priorité à un utilisateur possédant un `external_id`
- `unidentified` donne la priorité à un utilisateur ne possédant pas d'`external_id`

{% alert note %}
La fusion n'a pas lieu si l'adresse e-mail ou le numéro de téléphone correspond à plusieurs utilisateurs. Cela inclut les cas où l'un de ces utilisateurs possède le même `external_id` que celui spécifié dans la requête. Dans ces cas, l'endpoint renvoie `"message": "success"`, mais les profils utilisateur ne sont pas combinés. Pour éviter cela, vérifiez que l'adresse e-mail ou le numéro de téléphone est associé uniquement à des utilisateurs non identifiés avant d'appeler cet endpoint.
{% endalert %}

## Exemple de requête

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

### Sensibilité à la casse

Le champ `alias_name` est sensible à la casse. Une requête qui renvoie un code d'état `201` confirme uniquement que la syntaxe de la requête est valide — elle ne confirme pas que l'alias a été trouvé. Si la casse de `alias_name` dans votre requête ne correspond pas exactement à l'alias stocké sur le profil utilisateur, l'opération échouera silencieusement et l'`external_id` ne sera pas attribué. Par exemple, si l'alias stocké est `JimJones@example.com`, une requête avec `jimjones@example.com` renverra un succès mais ne produira aucun résultat.

{% alert tip %}
Pour plus d'informations sur `alias_name` et `alias_label`, consultez notre documentation sur les [alias utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).
{% endalert %}

## Réponse

```json
{
    "aliases_processed": 1,
    "message": "success"
}
```

{% endapi %}