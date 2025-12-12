---
nav_title: "Objet Planification"
article_title: Objet Planification API
page_order: 12
page_type: reference
description: "Cet article de référence répertorie et explique l’objet Planification différent utilisé chez Braze."

---

# Objet Planification

> Les paramètres des points de terminaison de la campagne et de la création de la planification Canvas reflètent ceux du point de terminaison d'envoi et ajoutent le paramètre `schedule`, qui vous permet de spécifier le moment où vous souhaitez que les utilisateurs ciblés reçoivent votre message. Si vous incluez uniquement le paramètre `time` dans l’objet `schedule`, tous vos utilisateurs recevront des messages à ce moment-là.

Si vous définissez `in_local_time` sur `true`, vous obtiendrez une réponse d’erreur si le paramètre Time est passé dans tous les fuseaux horaires. Si vous attribuez la valeur "true" à `at_optimal_time`, vos utilisateurs recevront le message à la date désignée et à l'heure optimale (quelle que soit l'heure que vous avez indiquée). Lorsque vous utilisez l'envoi de l'heure locale ou optimale, n'indiquez pas les désignateurs de fuseaux horaires dans la valeur du paramètre de temps (par exemple, utilisez `"2015-02-20T13:14:47"` au lieu de `"2015-02-20T13:14:47-05:00"`).

La réponse vous fournira un `schedule_id` que vous devez enregistrer au cas où vous auriez ultérieurement besoin d’annuler ou de mettre à jour le message que vous planifiez :

## Corps de l’objet

Insérez cet objet si nécessaire pour planifier vos messages.

```json
"schedule": {
  "time": (required, datetime as ISO 8601 string) time to send the message in UTC,
  "in_local_time": (optional, bool),
  "at_optimal_time": (optional, bool),
}
```

## Réponse de l’ID de planification

Vous recevrez un `schedule_id` pour le message planifié que vous avez créé.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "schedule_id" : (required, string) identifier for the scheduled message that was created
}
```

Si vous utilisez l'API pour des appels de serveur à serveur, il se peut que vous deviez ajouter à votre liste blanche l’URL d’API appropriée si vous travaillez derrière un pare-feu.

Les réponses des endpoints de planification des messages incluront le `dispatch_id` du message pour y faire référence lors de l’envoi. Le `dispatch_id` est l’identifiant de la transmission du message (ID unique pour chaque « dispatch » envoyé par Braze).

