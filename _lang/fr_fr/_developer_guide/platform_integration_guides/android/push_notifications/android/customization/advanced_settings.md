---
nav_title: Paramètres avancés
article_title: Paramètres avancés de notification push pour Android
platform: Android
page_order: 40
description: "Cet article de référence couvre les paramètres avancés de notification push pour Android tels que TTL (Durée de vie), les ID de notification, la priorité de notification, etc."
channel:
  - push

---

# Paramètres avancés

> Il existe de nombreux paramètres avancés disponibles pour les notifications push Android et FireOS envoyées via le tableau de bord de Braze. Le présent article décrit ces fonctionnalités et la manière de les utiliser avec succès.

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

## ID de notification {#notification-id}

Un **ID de notification** est un identifiant unique pour une catégorie de message de votre choix qui informe le service de messagerie de ne respecter que le message le plus récent de cet ID. Définir un ID de notification vous permet d’envoyer uniquement le message le plus récent et le plus pertinent, plutôt qu’une pile de données obsolètes et non pertinentes.

## Priorité de livraison d’envoi de message Firebase {#fcm-priority}

Le champ [Priorité d'envoi/distribution de la messagerie Firebase](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) vous permet de contrôler si un push est envoyé avec une priorité "normale" ou "élevée" à la messagerie Firebase Cloud.

## TTL (Durée de vie) {#ttl}

Le champ **Durée en vie** (TTL) vous permet de définir une durée personnalisée de stockage des messages avec le service de messagerie push. Les valeurs par défaut pour la durée de vie sont de quatre semaines pour FCM et de 31 jours pour ADM.

## Texte récapitulatif {#summary-text}

Le texte récapitulatif vous permet de définir un texte supplémentaire dans la vue de notification étendue. Il sert également de légende pour les notifications avec des images.

![Un message Android avec le titre « Salutations d’Appboy ! », le message « C’est le corps du message ! Vous pouvez même ajouter des emojis." et texte du résumé "Voici le texte du résumé."]({% image_buster /assets/img_archive/summary_text.png %})

Le texte récapitulatif s’affiche sous le corps du message dans la vue étendue.

Pour les notifications push qui incluent des images, le texte du message s’affiche dans la vue réduite tandis que le texte récapitulatif s’affiche comme légende d’image lorsque la notification est étendue. 

![Un envoi de messages Android avec le titre "Appboy !", le message "Ceci est le corps du message.." et le texte du résumé "et ceci est le texte du résumé."]({% image_buster /assets/img_archive/messagesummary.gif %})

## URI personnalisés {#custom-uri}

La fonctionnalité **URI personnalisé** vous permet de spécifier une URL Web ou une ressource Android vers laquelle naviguer lorsque l'on clique sur la notification. Si aucun URI personnalisé n’est spécifié, cliquer sur la notification amène les utilisateurs dans votre application. Vous pouvez utiliser l’URI personnalisé pour créer un lien profond à l’intérieur de votre application et diriger les utilisateurs vers des ressources qui existent en dehors de votre application. Ceci peut être spécifié via l'[API Messages]({{site.baseurl}}/api/endpoints/messaging/) ou notre tableau de bord sous **Paramètres avancés** dans le compositeur de push comme illustré :

![La création de liens profonds avancement dans le compositeur poussoir Braze.]({% image_buster /assets/img_archive/deep_link.png %})

## Priorité d’affichage de la notification {#notification-priority}

{% alert important %}
Le paramètre de priorité d’affichage de notification n’est plus utilisé sur les appareils exécutant Android O ou plus récents. Pour les appareils plus récents, définissez la priorité par le biais de la [configuration du canal de notification.](https://developer.android.com/training/notify-user/channels#importance)
{% endalert %}

Le niveau de priorité d’une notification push affecte la manière dont votre notification est affichée dans la barre de notification par rapport à d’autres notifications. Il peut également affecter la vitesse et la manière de livrer, car les messages normaux et moins prioritaires peuvent être envoyés avec une latence légèrement plus élevée ou groupés pour préserver la durée de vie de la batterie, alors que les messages haute priorité sont toujours envoyés immédiatement.

Dans Android O, la priorité de notification est devenue une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir la priorité d’un canal pendant sa configuration, puis utiliser le tableau de bord pour sélectionner le canal approprié lors de l’envoi de vos sons de notification. Pour les appareils exécutant des versions d’Android antérieures à O, il est possible de spécifier un niveau de priorité pour les notifications Android et FireOS via le tableau de bord de Braze et l’API de messagerie. 

Pour envoyer un message à l'ensemble de vos utilisateurs avec une priorité spécifique, nous vous recommandons de spécifier indirectement la priorité via la [configuration du canal de communication](https://developer.android.com/training/notify-user/channels#importance) (pour cibler les appareils O+) *et d'* envoyer la priorité individuelle depuis le tableau de bord (pour cibler les appareils <O).

Les niveaux de priorité que vous pouvez définir sur les notifications push Android ou Fire OS sont les suivants :

| Priorité | Description ou utilisation prévue | Valeur de `priority` (pour les messages API) |
|----------|--------------------------|-------------------------------------|
| Max      | Messages urgents ou à délai de réponse critique | `2` |
| Élevée     | Communication importante, telle que le nouveau message d’un ami | `1` |
| Par défaut  | La plupart des notifications : utilisez « par défaut » si votre message ne tombe pas explicitement dans les autres types de priorité | `0` |
| Faible      | Informations que vous voulez que les utilisateurs connaissent, mais ne nécessitant pas d’action immédiate | `-1` |
| Min      | Informations contextuelles ou d’arrière-plan. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Pour plus d'informations, reportez-vous à la documentation de Google sur [les notifications Android](http://developer.android.com/design/patterns/notifications.html).

## Sons {#sounds}

Dans Android O, les sons de notification sont devenus une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir le son d’un canal pendant sa configuration, puis utiliser le tableau de bord pour sélectionner le canal approprié lors de l’envoi de vos notifications.

Pour les appareils fonctionnant dans des versions d’Android antérieures à O, Braze vous permet de définir le son d’un message de notification push individuel via le composeur du tableau de bord. Vous pouvez le faire en spécifiant une ressource sonore locale sur l'appareil (par exemple, `android.resource://com.mycompany.myapp/raw/mysound`). Spécifier « par défaut » dans ce champ jouera le son de notification par défaut sur l’appareil. Cela peut être spécifié via l'[API Messages]({{site.baseurl}}/api/endpoints/messaging/) ou le tableau de bord sous **Paramètres avancés** dans le compositeur de push.

![Le réglage avancé du son dans le compositeur poussoir de Braze.]({% image_buster /assets/img_archive/sound_android.png %})

Saisissez l'URI complet de la ressource sonore (par exemple, `android.resource://com.mycompany.myapp/raw/mysound`) dans l'invite du tableau de bord.

Pour envoyer un message à l'ensemble de vos utilisateurs avec un son spécifique, nous vous recommandons de spécifier indirectement le son via la [configuration du canal de communication](https://developer.android.com/training/notify-user/channels) (pour cibler les appareils O+) *et d'* envoyer le son individuel depuis le tableau de bord (pour cibler les appareils <O).

