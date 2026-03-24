---
nav_title: "POST : Fusionner les utilisateurs"
article_title: "POST : Fusionner les utilisateurs"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Fusion d’utilisateurs."

---
{% api %}
# Fusionner les utilisateurs
{% apimethod post %}
/users/merge
{% endapimethod %}

> Utilisez cet endpoint pour fusionner un utilisateur avec un autre utilisateur.

Vous pouvez spécifier jusqu’à 50 fusions par requête. Cet endpoint est asynchrone.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d262b86d-cf84-46e2-b9d0-f882bb7078de {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l’autorisation `users.merge`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='users merge' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "merge_updates" : (required, array of objects)
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `merge_updates` | Requis | Tableau | Un tableau d’objets. Chaque objet doit contenir un objet `identifier_to_merge` et un objet `identifier_to_keep`, qui doivent chacun référencer un utilisateur par `external_id`, `user_alias`, `phone` ou `email`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Comportement de fusion

Le comportement documenté ci-dessous est vrai pour toutes les fonctionnalités de Braze qui **ne sont pas** optimisées par Snowflake. Les fusions d'utilisateurs ne seront pas prises en compte pour l'onglet **Historique des messages**, les extensions de segments, le générateur de requêtes et les actualités.

{% alert important %}
Cet endpoint ne garantit pas que la séquence des objets `merge_updates` soit mise à jour.
{% endalert %}

Ce endpoint fusionne les champs suivants s'ils ne sont pas trouvés chez l'utilisateur cible.

- Prénom
- Nom
- Adresses de e-mail (à moins qu'elles ne soient [cryptées]({{site.baseurl}}/user_guide/data/field_level_encryption/))
- Genre
- Date de naissance
- Numéro de téléphone
- Fuseau horaire
- Ville d'origine
- Pays
- Langue
- Informations sur l’appareil
- Décompte des sessions (la somme des sessions des deux profils)
- Date de la première session (Braze sélectionne la date la plus proche des deux dates)
- Date de la dernière session (Braze sélectionne la date la plus récente parmi les deux dates)
- Attributs personnalisés (Braze conserve les attributs personnalisés existants dans le profil cible et inclut les attributs personnalisés qui n'existaient pas dans le profil cible)
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
- Données d'interaction de la campagne (Braze sélectionne les champs de date les plus récents)
- Résumés du flux de travail (Braze sélectionne les champs de date les plus récents)
- Message et historique d’engagement du message
- Braze fusionne les données de session uniquement si l'application est présente sur les deux profils utilisateurs.

{% alert note %}
Lors de la fusion d'utilisateurs, l'utilisation de l'endpoint `/users/merge` fonctionne de la même manière que la [méthode`changeUser()` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser).
{% endalert %}

#### Comportement personnalisé de la date de l'événement et de la date de l'événement d'achat

Ces champs fusionnés mettent à jour les filtres « pour X événements en Y jours ». Pour les événements d’achat, ces filtres incluent « nombre d’achats en Y jours » et « argent dépensé au cours des Y derniers jours ».

### Fusionner les utilisateurs par e-mail ou par numéro de téléphone

Si un`email`  ou`phone`  est spécifié comme identifiant, il est nécessaire d'inclure une valeur  `prioritization`supplémentaire dans l'identifiant. Il`prioritization`est nécessaire de fournir un tableau ordonné indiquant quel utilisateur fusionner si plusieurs utilisateurs sont détectés. Cela signifie que si plusieurs utilisateurs correspondent à une priorité, la fusion n'aura pas lieu.

Les valeurs autorisées pour le tableau sont les suivantes :

- `identified`
- `unidentified`
- `most_recently_updated` (Priorité à l'utilisateur le plus récemment mis à jour)
- `least_recently_updated` (Priorité à l'utilisateur le moins récemment mis à jour)

Une seule des options suivantes peut exister à la fois dans le tableau de priorisation :

- `identified` Il s'agit de donner la priorité à un utilisateur ayant une `external_id`
- `unidentified` Il s'agit de donner la priorité à un utilisateur qui n'a pas de `external_id`

## Exemple de requêtes

### Demande de base

Il s'agit d'un corps de requête basique pour montrer le modèle de la requête.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "external_id": "old-user1"
      },
      "identifier_to_keep": {
        "external_id": "current-user1"
      }
    },
    {
      "identifier_to_merge": {
        "email": "user1@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep":  {
        "email": "user2@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    },
    {
      "identifier_to_merge": {
        "user_alias": {
          "alias_name": "old-user2@example.com",
          "alias_label": "email"
        }
      },
      "identifier_to_keep": {
        "user_alias": {
          "alias_name": "current-user2@example.com",
          "alias_label": "email"
        }
      }
    }
  ]
}'
```

### Fusionner des utilisateurs non identifiés

La demande suivante fusionnerait l'utilisateur non identifié le plus récemment mis à jour avec l'adresse e-mail`john.smith@braze.com`  avec l'utilisateur ayant l'ID externe`john` . Dans cet exemple, l'utilisation`most_recently_updated`de filtre la requête à un utilisateur non identifié. Ainsi, s'il y avait deux utilisateurs non identifiés avec cette adresse e-mail, un seul serait fusionné avec l'utilisateur disposant d'un ID externe`john`.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

### Fusionner un utilisateur non identifié avec un utilisateur identifié

L'exemple suivant fusionne l'utilisateur non identifié le plus récemment mis à jour avec l'adresse e-mail`john.smith@braze.com`  et l'utilisateur identifié le plus récemment mis à jour avec l'adresse e-mail`john.smith@braze.com` .

Utilisation`most_recently_updated`de filtres pour limiter les requêtes à un utilisateur (un utilisateur non identifié pour `identifier_to_merge`et un utilisateur identifié pour le `identifier_to_keep`).

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "email": "john.smith@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    }
  ]
}'
```

### Fusionner un utilisateur non identifié sans inclure lamost_recently_updatedpriorisation

S'il existe deux utilisateurs non identifiés avec l'adresse e-mail`john.smith@braze.com` , cette requête exemple ne fusionne aucun utilisateur, car il y a deux utilisateurs non identifiés avec cette adresse e-mail. Cette requête ne fonctionne que s'il n'y a qu'un seul utilisateur non identifié avec l'adresse e-mail`john.smith@braze.com`.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

## Réponse

Deux réponses de code de statut existent pour cet endpoint : `202` et `400`.

### Exemple de réponse réussie

Le code de statut `202` pourrait renvoyer le corps de réponse suivant.

```json
{
  "message": "success"
}
```

### Exemple de réponse échouée

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la [résolution des problèmes](#troubleshooting) pour plus d’informations concernant les erreurs que vous pourriez rencontrer.

```json
{
  "message": "'merge_updates' must be an array of objects"
}
```

## Résolution des problèmes

Le tableau suivant répertorie les messages d’erreur possibles.

| Erreur | Résolution des problèmes |
| --- |
| `'merge_updates' must be an array of objects` | Vérifiez que `merge_updates` est un tableau d'objets. |
| `a single request may not contain more than 50 merge updates` | Vous pouvez spécifier jusqu’à 50 fusions dans une seule requête. |
| `identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, 'email' property that is a string, or 'phone' property that is a string` | Vérifiez les identifiants dans votre requête. |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | Vérifiez que `merge_updates` ne contient que les deux objets `identifier_to_merge` et `identifier_to_keep`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
