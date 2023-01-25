---
nav_title: "Objet de notification push Kindle et FireOS"
article_title: Objet de messagerie de notifications push Kindle et FireOS
page_order: 7
page_type: reference
channel: push
platform:
  - Android
  - FireOS
description: "Cet article explique les différents composants du Kindle et de l’objet Notification push FireOS de Braze."

---

# Spécifications des objets de notifications push Kindle et FireOS

L’objet `kindle_push` vous permet de modifier ou de créer des notifications push Kindle et FireOS via nos [endpoints d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging).

```json
{
   "alert": (required, string) le message de notification,
   "title": (required, string) le titre qui apparaît dans la barre de notifications,
   "extra": (optional, object) clés et valeurs supplémentaires à envoyer dans la notification push,
   "message_variation_id": (optional, string) utilisé lorsqu’un campaign_id est fourni pour spécifier avec quelle variation du message ce message doit être suivi (il doit s’agir d’un message de notification push Kindle/FireOS),
   "priority": (optional, integer) la valeur de priorité de la notification,
   "collapse_key": (optional, string) la touche de réduction pour ce message,
   // Spécifier « par défaut » dans le champ « son » jouera le son de notification par défaut
   "sound": (optional, string) l’emplacement du son de notification personnalisé dans l’appli,
   "custom_uri": (optional, string) une URL Web ou une URI de lien profond
}
```

Le paramètre `priority` accepte les valeurs entre `-2` et `2`, où `-2` représente la priorité la plus basse et `2` la priorité la plus élevée. `0` est la valeur par défaut. Toutes les valeurs envoyées en dehors de cette plage d’entiers seront par défaut à `0`.
