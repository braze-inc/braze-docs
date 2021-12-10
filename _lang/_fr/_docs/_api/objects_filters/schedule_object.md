---
nav_title: "Planifier l'objet"
article_title: API Schedule Object
page_order: 12
page_type: Référence
description: "Cet article énumère et explique les différents objets de planification utilisés au Brésil."
---

# Spécification de l'objet de planification

Les paramètres de la campagne et des terminaux de création de Canvas reflètent ceux de l'extrémité d'envoi et ajoutent le paramètre `Schedule` , qui vous permet de spécifier quand vous voulez que vos utilisateurs ciblés reçoivent votre message (jusqu'à 90 jours dans le futur). Si vous n'incluez que le paramètre `time` dans l'objet `schedule` , tous vos utilisateurs seront envoyés à ce moment-là.

Si vous définissez `in_local_time` à être `true`, vos utilisateurs recevront le message à la date et à l'heure désignées dans leurs fuseaux horaires respectifs. Si `in_local_time` est vrai, vous obtiendrez une réponse d'erreur si le paramètre `temps` est passé dans le fuseau horaire de votre entreprise. Si vous définissez `at_optimal_time` pour être vrai, vos utilisateurs recevront le message à la date désignée à la [heure optimale][33] pour eux (quel que soit le moment que vous leur fournissez). Lorsque vous utilisez un envoi local ou optimal, ne fournissez pas de concepteurs de fuseaux horaires dans la valeur du paramètre de temps (par ex. donnez-nous simplement `"2015-02-20T13:14:47"` au lieu de `"2015-02-20T13:14:47-05:00"`).

La réponse vous fournira un `schedule_id` que vous devriez enregistrer au cas où vous auriez besoin d'annuler ou de mettre à jour le message que vous planifiez :

## Corps de l'objet

Insérez cet objet si nécessaire pour planifier vos messages.

```json
"schedule": {
  "time": (obligatoire, date et heure sous le format ISO 8601) heure pour envoyer le message (jusqu'à 90 jours dans le futur),
  "in_local_time": (optionnel, bool)
  "at_optimal_time": (optionnel, bool)
}
```

## Répondre à l'ID du planning

Vous recevrez un `schedule_id` pour le message planifié que vous avez créé.

```json
Content-Type: application/json
Autorisation : Bearer YOUR-REST-API-KEY
{
  "schedule_id" : (requis, chaîne) identifiant pour le message planifié qui a été créé
}
```

Les clients qui utilisent l'API pour les appels de serveur à serveur peuvent avoir besoin de mettre en liste blanche l'URL de l'API appropriée s'ils sont derrière un pare-feu.

Les réponses aux points de terminaison de planification des messages incluront le message `dispatch_id` pour être référencé à l'envoi du message. Le `dispatch_id` est l'id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze).

[33]: {{site.baseurl}}/user_guide/intelligence/intelligent_timing/
