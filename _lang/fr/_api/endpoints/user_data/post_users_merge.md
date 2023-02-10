---
nav_title: "POST : Fusion d’utilisateurs"
article_title: "POST : Fusion d’utilisateurs"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Users Merge (Fusion d’Utilisateurs)"

---
{% api %}
# Fusionner les utilisateurs
{% apimethod post %}
/users/merge
{% endapimethod %}

Utilisez cet endpoint pour fusionner un utilisateur avec un autre utilisateur. Vous pouvez spécifier jusqu’à 50 fusions par requête. Cet endpoint est asynchrone.

{% alert important %}
Cet endpoint est actuellement en accès anticipé. Contactez votre CSM Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='users merge' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "merge_updates" : (required, array of objects)
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `merge_updates` | Requis | Tableau | Un array d’objets. Chaque objet doit contenir un objet `identifier_to_merge` et un objet `identifier_to_keep`, qui doivent tous les deux référencer un utilisateur soit avec un `external_id` soit un `user_alias`. Les deux utilisateurs qui sont fusionnés doivent être identifiés avec la même méthode. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### Comportement Merge_updates

Définir le champ `merge_updates` sur `merge` paramètre l’endpoint pour fusionner tous les champs suivants trouvés **exclusivement** depuis l’utilisateur original vers l’utilisateur cible.

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
- Décompte des sessions (la somme des sessions depuis les deux profils)
- Date de la première session (Braze choisira la date la plus ancienne parmi les deux)
- Date de la dernière session (Braze choisira la date la plus récente parmi les deux)
- Attributs personnalisés
- Données sur les événements d’achats et personnalisés (sauf propriétés d’événements, compte, horodatages correspondant à la première et dernière dates)
- Propriétés d’événements d’achats et personnalisées pour la segmentation « X fois en Y jours » (où X <= 50 et Y <= 30)

L’un des champs suivants a été trouvé sur un utilisateur vers l’autre utilisateur :
- Nombre d’événements d’achats et personnalisés, ainsi que les horodatages correspondant à la première et dernière dates
  - Ces champs fusionnés mettront à jour les filtres « pour X événements en Y jours ». Pour les événements d’achat, ces filtres incluent « nombre d’achats en Y jours » et « argent dépensé au cours des Y derniers jours ».

Les données de session ne seront fusionnées que si l’application existe sur les deux profils utilisateurs. Par exemple, si votre utilisateur cible ne dispose pas d’un résumé d’application pour « ABCApp » mais que votre utilisateur d’origine l’a, l’utilisateur cible disposera du résumé d’application pour « ABCApp » sur son profil après la fusion. Configurer le champ sur `none` ne fusionnera aucune donnée utilisateur avec le profil utilisateur identifié.

## Exemple de demande

```
curl --location --request POST 'https://rest.iad-03.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
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
        "user_alias": {
          "alias_name": "old-user2@example.com",
          "alias_label": "e-mail"
        }
      },
      "identifier_to_keep": {
        "user_alias": {
          "alias_name": "current-user2@example.com",
          "alias_label": "e-mail"
        }
      }
    }
  ]
}'
```

## Réponse

Deux réponses de code de statut existent pour cet endpoint : `202` et `400`.

### Exemple de réponse réussie

Le code de statut `202` pourrait retourner le corps de réponse suivant.

```json
{
  "message": "success"
}
```

### Exemple de réponse échouée

Le code de statut `400` pourrait retourner le corps de réponse suivant. Consultez la [résolution des problèmes](#troubleshooting) pour plus d’informations concernant les erreurs que vous pourriez rencontrer.

```json
{
  "message": "’merge_updates’ doit être un array d’objets."
}
```

## Résolution des problèmes

Le tableau suivant répertorie les messages d’erreur possibles.

| Erreur | Résolution des problèmes |
| --- |
| `'merge_updates' must be an array of objects` | Vérifiez que `merge_updates` est un array d’objets. |
| `a single request may not contain more than 50 merge updates` | Vous pouvez spécifier jusqu’à 50 fusions dans une seule requête. |
| `identifiers must be objects with an 'external_id' property that is a string, or 'user_alias' property that is an object` | Vérifiez les identifiants dans votre requête. |
| `identifiers must be objects of the same type` | Assurez-vous que les types d’objets des identificateurs correspondent. |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | Assurez-vous que `merge_updates` contient uniquement les deux objets `identifier_to_merge` et `identifier_to_keep`. .|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
