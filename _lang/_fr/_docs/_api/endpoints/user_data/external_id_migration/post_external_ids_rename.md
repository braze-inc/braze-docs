---
nav_title: "POST: Renommage de l'ID externe"
article_title: "POST: Renommage de l'ID externe"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison de renommage des IDs externes."
---

{% api %}
# Renommer l'ID externe
{% apimethod post %}
/fr/users/external_ids/rename
{% endapimethod %}

{% alert note %}
Pour des raisons de sécurité, cette fonctionnalité est désactivée par défaut. Pour activer cette fonctionnalité, veuillez contacter votre gestionnaire de succès.
{% endalert %}

Utilisez ce point de terminaison pour "renommer" les identifiants externes de vos utilisateurs. Ce point de terminaison définit un nouveau (principal) `external_id` pour l'utilisateur et déprécie leur `external_id` existant. Cela signifie que l'utilisateur peut être identifié par `external_id` jusqu'à ce que la dépréciation soit supprimée. L'ID obsolète peut être supprimé en utilisant le point de terminaison [supprimer]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove). Avoir plusieurs identifiants externes permet une période de migration où les anciennes versions de vos applications sont encore dans le sauvage qui utilisent le schéma de nommage externe précédent ne se casse pas. Nous vous recommandons fortement de supprimer les identifiants externes obsolètes une fois que votre ancien schéma de nommage n'est plus utilisé.

Vous pouvez envoyer jusqu'à 50 objets de renommage par requête.

Vous devrez créer une nouvelle [clé API]({{site.baseurl}}/api/api_key/) avec les permissions pour ce point de terminaison.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "external_id_renames" : (requis, table d'objets de renommage d'ID externe)
}
```

## Paramètres de la requête

| Paramètre               | Requis | Type de données                                           | Libellé                                                                                                                 |
| ----------------------- | ------ | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `Renommer l'id externe` | Requis | Tableau des objets de renommage des identifiants externes | Voir l'exemple de requête et les limitations suivantes pour la structure de l'objet de renommage d'identifiant externe. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

- Le `current_external_id` doit être l'ID principal de l'utilisateur, et ne peut pas être un ID obsolète
- `Le new_external_id` ne doit pas déjà être utilisé comme un ID primaire ou un ID obsolète
- `Le <code> current_external_id` et `new_external_id` ne peuvent pas ętre le męme

## Exemple de requête
```
curl --location --request POST 'https://rest.iad-01.braze. om/users/external_ids/rename' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_id_renames" : 
  [
    {
      "current_external_id": "existing_external_id",
      "new_external_id" : "new_external_id"
    }
  ]
}'
```

## Réponse
La réponse confirmera tous les renommages réussis, ainsi que les renommages échoués avec toutes les erreurs associées. Les messages d'erreur dans le champ `rename_errors` référenceront l'index de l'objet dans la table de la requête originale.

```
{

  "message" : (string) status message,
  "external_ids" : (table d'opérations de renommage réussies),
  "rename_errors": (table de toutes les <minor error message>)

}
```

Le champ `message` retournera `succès` pour toute requête valide. Des erreurs plus spécifiques sont capturées dans le tableau `rename_errors`. Le champ `message` renvoie une erreur dans le cas de:
- Clé API invalide
- Vider la table `external_id_renames`
- `external_id_renames` table avec plus de 50 objets
- Limite de taux atteinte (>1 000 requêtes/minute)

## Foire aux questions

__Cela a-t-il un impact sur MAU?__
- Non, puisque le nombre d'utilisateurs restera le même, ils auront juste un nouveau `external_id`.

__Le comportement de l'utilisateur change-t-il historiquement ?__
- Non, puisque l'utilisateur est toujours le même, et tout son comportement historique est toujours lié à eux.

__Peut-on l'exécuter sur des groupes d'applications de dev/staging ?__
- « Oui. » En fait, nous vous recommandons fortement de faire une migration de test dans un groupe d'applications de pré-production ou de développement, et s'assurer que tout s'est bien passé avant de s'exécuter sur les données de production.

__Cela consomme-t-il des points de données ?__
- Cette fonctionnalité ne coûte pas de points de données.

__Quelle est la période de dépréciation recommandée ?__
- Nous n'avons pas de limite dure sur combien de temps vous pouvez conserver les identifiants externes obsolètes, mais nous vous recommandons fortement de les supprimer une fois qu'il n'y a plus besoin de référencer les utilisateurs par l'ID déprécié.

{% endapi %}
