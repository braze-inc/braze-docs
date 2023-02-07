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
