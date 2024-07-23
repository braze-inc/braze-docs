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

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l'autorisation `users.merge`.

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
| `merge_updates` | Obligatoire | Tableau | Un tableau d'objets. Chaque objet doit contenir un objet  et un objet `identifier_to_merge`, qui doivent tous les deux référencer un utilisateur soit avec un `identifier_to_keep` soit un `external_id`.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### Comportement de fusion

Le comportement documenté ci-dessous est vrai pour toutes les fonctionnalités de Braze qui *ne sont pas* optimisées par Snowflake. Les fusions d'utilisateurs ne seront pas reflétées pour l'onglet **Historique de la messagerie**, les extensions de segment, le générateur de requêtes et les courants.

{% alert important %}
Cet endpoint ne garantit pas que la séquence des objets `merge_updates` soit mise à jour.
{% endalert %}

Ce point de terminaison fusionnera n'importe lequel des champs suivants s'ils ne sont pas trouvés sur l'utilisateur cible :

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
- Attributs personnalisés (les attributs personnalisés existants sur le profil cible sont conservés et incluront les attributs personnalisés qui n'existaient pas sur le profil cible).
- Données sur les événements personnalisés et les événements d'achat
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
- Champs Last\_X\_at (Braze mettra à jour les champs si les champs de profil orphelins sont plus récents).
- Données d'interaction de la campagne (Braze choisira les champs de date les plus récents).
- Résumés du flux de travail (Braze choisira les champs de date les plus récents)
- Message et historique d’engagement du message

Les données de session ne seront fusionnées que si l’application existe sur les deux profils utilisateurs.

#### Comportement de la date de l'événement personnalisé et de la date de l'événement d'achat
Note que ces champs fusionnés mettront à jour les filtres "pour X événements dans Y jours". Pour les événements d’achat, ces filtres incluent « nombre d’achats en Y jours » et « argent dépensé au cours des Y derniers jours ».

### Fusionner les utilisateurs par e-mail

Si un `email` est spécifié comme identifiant, une valeur `prioritization` supplémentaire est requise dans l'identifiant. `prioritization` doit être un tableau spécifiant l'utilisateur à fusionner s'il y a plusieurs utilisateurs trouvés. `prioritization` est un tableau ordonné, ce qui signifie que si plus d'un utilisateur correspond à un ordre de priorité, la fusion n'aura pas lieu.

Les valeurs autorisées pour le tableau sont : `identified`, `unidentified`, `most_recently_updated`. `most_recently_updated` signifie que la priorité est donnée à l'utilisateur qui a effectué la dernière mise à jour.

Une seule des options suivantes peut exister à la fois dans le tableau de priorisation :
- `identified` se réfère à la priorisation d'un utilisateur avec une `external_id`
- `unidentified` désigne le fait d'accorder la priorité à un utilisateur sans `external_id`

## Exemple de requêtes

### Demande de base
Il s'agit d'un corps de requête basique pour montrer le modèle de la requête.

```json
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

### Fusionner les utilisateurs non identifiés

La requête suivante fusionnerait l'utilisateur non identifié le plus récemment mis à jour et dont l'adresse e-mail est « john.smith@braze.com » avec l'utilisateur dont l’`external_id` est « john ». L'utilisation de `most_recently_updated` permet de filtrer la requête pour afficher un seul utilisateur non identifié. Ainsi, s'il y avait deux utilisateurs non identifiés avec cette adresse électronique, un seul serait fusionné avec l'utilisateur avec `external_id` "john".

```json
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

L'exemple suivant fusionne l'utilisateur non identifié le plus récemment mis à jour et dont l'adresse e-mail est « john.smith@braze.com » avec l'utilisateur identifié le plus récemment mis à jour et dont l'adresse e-mail est « john.smith@braze.com ». L'utilisation de `most_recently_updated` filtre les requêtes pour afficher un seul utilisateur (un utilisateur non identifié pour `identifier_to_merge` et un utilisateur identifié pour `identifier_to_keep`).

```json
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

### Fusionner un utilisateur non identifié sans inclure la priorisation most\_recently\_updated

S'il y a deux utilisateurs non identifiés avec l'adresse électronique "john.smith@braze.com", cet exemple de demande ne fusionne aucun utilisateur puisqu'il y a deux utilisateurs non identifiés avec cette adresse électronique. Cette requête fonctionne uniquement s'il n'y a qu'un seul utilisateur non identifié dont l'adresse e-mail est « john.smith@braze.com ».

```json
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

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Reporte-toi à la rubrique [Dépannage](#troubleshooting) pour plus d'informations sur les erreurs que tu peux rencontrer.

```json
{
  "message": "'merge_updates' must be an array of objects"
}
```

## Résolution des problèmes

Le tableau suivant répertorie les messages d’erreur possibles.

| Erreur | Résolution des problèmes |
| --- |
| `'merge_updates' must be an array of objects` | Vérifie que `merge_updates` est un tableau d'objets. |
| `a single request may not contain more than 50 merge updates` | Vous pouvez spécifier jusqu'à 50 mises à jour de fusion dans une seule requête. |
| `identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, or 'email' property that is a string` | Vérifie les identifiants dans ta demande. |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | Vérifie que `merge_updates` ne contient que les deux objets `identifier_to_merge` et `identifier_to_keep`. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
