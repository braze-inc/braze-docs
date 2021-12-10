---
nav_title: "POST: ID externe supprimé"
article_title: "POST: ID externe supprimé"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur les IDs externes Supprimer le point de terminaison."
---

{% api %}
# Supprimer un ID externe
{% apimethod post %}
/fr/users/external_ids/remove
{% endapimethod %}

{% alert note %}
Pour des raisons de sécurité, cette fonctionnalité est désactivée par défaut. Pour activer cette fonctionnalité, veuillez contacter votre gestionnaire de succès.
{% endalert %}

Utilisez ce point de terminaison pour supprimer les anciens identifiants externes obsolètes de vos utilisateurs. Ce point de terminaison supprime complètement l'identifiant obsolète et ne peut pas être annulé.

Vous pouvez envoyer jusqu'à 50 identifiants externes par demande.

Vous devrez créer une nouvelle [clé API]({{site.baseurl}}/api/api_key/) avec les permissions pour ce point de terminaison.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e16b5340-5f44-42b6-9033-2398faf8908e {% endapiref %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids" : (requis, table d'identifiants externes à supprimer)
}
```

### Paramètres de la requête

| Paramètre    | Requis | Type de données    | Libellé                                                  |
| ------------ | ------ | ------------------ | -------------------------------------------------------- |
| `ID_externe` | Requis | Tableau de chaînes | Identifiants externes à supprimer pour les utilisateurs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de requête
```
curl --location --request POST 'https://rest.iad-01.braze. om/users/external_ids/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids" : 
    [
      "existing_deprecated_external_id_string",
...
    ]
}'
```
{% alert important %}
Seuls les identifiants obsolètes peuvent être supprimés ; tenter de supprimer un ID externe primaire entraînera une erreur.
{% endalert %}

## Réponse
La réponse confirmera toutes les suppressions réussies, ainsi que les suppressions infructueuses avec les erreurs associées. Les messages d'erreur dans le champ `removal_errors` référenceront l'index dans la table de la requête originale.

```
{

  "message" : (string) status message,
  "removed_ids" : (table d'opérations de suppression réussies),
  "removal_errors": (table de toutes les <minor error message>)

}
```

Le champ `message` retournera `succès` pour toute requête valide. Des erreurs plus spécifiques sont capturées dans le tableau `removal_errors`. Le champ `message` renvoie une erreur dans le cas de:
- Clé API invalide
- Tableau `external_ids` vide
- `table external_ids` avec plus de 50 éléments
- Limite de taux atteinte (>1 000 requêtes/minute)

{% endapi %}
