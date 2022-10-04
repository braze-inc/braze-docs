---
nav_title: "Paramètres avancés de campagne de notification push"
article_title: Paramètres avancés de campagne de notification push
page_order: 5
page_layout: reference
description: "Le présent article de référence couvre certains paramètres avancés de campagne de notification push comme la priorité, les URL personnalisées, les options de livraison, etc."
platform: Android
channel:
  - notification push
tool:
  - Campagnes

---

# Paramètres avancés de campagne de notification push

> Il existe de nombreux paramètres avancés disponibles pour les notifications push Android et FireOS envoyées via le tableau de bord de Braze. Le présent article décrit ces fonctionnalités et la manière de les utiliser avec succès.

## ID de notification {#notification-id}

Un **« ID de notification » est un identifiant"** unique pour une catégorie de message de votre choix qui indique au service de messagerie de respecter uniquement le message le plus récent provenant de cet ID. Définir un ID de notification vous permet d’envoyer uniquement le message le plus récent et le plus pertinent, plutôt qu’une pile de données obsolètes et non pertinentes.

## TTL (Durée de vie) {#ttl}

Le champ **Time to Live"** (TTL, Durée de vie) vous permet de définir une durée personnalisée pour stocker les messages avec le service de messagerie de notification push. Les valeurs par défaut de Braze pour la durée de vie sont de quatre semaines pour FCM et de 31 jours pour ADM. 

Par exemple, supposons que votre application soit un jeu et que vous offrez à vos utilisateurs un bonus de monnaie du jeu s’ils maintiennent une habitude de jouer au jeu quotidiennement. Vous pourriez envoyer une notification push pour signaler à un utilisateur que cette série de connexions risque d’être brisée s’il a dépassé un certain nombre de jours. Cependant, si un utilisateur devait reconnecter son appareil à l’application de jeu 4 semaines plus tard avec la durée de vie réglée sur la valeur par défaut, alors ces messages auraient déjà expiré dans le service de messagerie et ne seraient pas livrés.

## Priorité de livraison de messagerie Firebase {#fcm-priority}

Le champ **Firebase Messaging Delivery Priority (Priorité de livraison de messagerie Firebase)** vous permet de contrôler si une notification push est envoyée avec une priorité « normale » ou « élevée » à Firebase Cloud Messaging. Consultez la [documentation FCM](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) pour en savoir plus.

## Texte récapitulatif

Le texte récapitulatif vous permet de définir un texte supplémentaire dans la vue de **notification étendue**. Le texte récapitulatif s’affiche sous le corps du message dans la vue étendue. Il sert également de légende pour les notifications avec des images.

![][9]

Pour les notifications push qui incluent des images, le texte du message s’affiche dans la vue réduite tandis que le texte récapitulatif s’affiche comme légende d’image lorsque la notification est étendue. Consultez l’animation suivante pour voir un exemple de ce comportement.

![Comportement du texte récapitulatif][15]

## URI personnalisés

La fonctionnalité d’**URI personnalisé** vous permet de spécifier une URL Web ou une ressource Android vers laquelle naviguer quand la notification est cliquée. Si aucun URI personnalisé n’est spécifié, cliquer sur la notification amène les utilisateurs dans votre application. Vous pouvez utiliser l’URI personnalisé pour créer un lien profond à l’intérieur de votre application ainsi que diriger les utilisateurs vers des ressources qui existent également en dehors de votre application. Cela peut être spécifié par le biais de notre [API de messagerie][13] ou dans les **Settings (Paramètres)** dans l’assistant de composeur de notification push.

> Pour activer l’URI personnalisé, le `BroadcastReceiver` de votre application doit être configuré pour gérer correctement l’ouverture de l’URI.  Cela implique d’analyser le contenu du message entrant pour obtenir l’URI personnalisé et de s’y rendre.  Notre [exemple de récepteur][14] fournit un exemple d’implémentation.

![URI personnalisé][12]

## Priorité d’affichage de la notification

{% alert important %}
Le paramètre de priorité d’affichage de notification n’est plus utilisé sur les appareils exécutant Android O ou plus récents. Pour les nouveaux appareils, définissez la priorité dans la [configuration du canal de notification](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

Le niveau de priorité d’une notification push affecte la manière dont votre notification est affichée dans la barre de notification par rapport à d’autres notifications. Il peut également affecter la vitesse et la manière de livrer, car les messages normaux et moins prioritaires peuvent être envoyés avec une latence légèrement plus élevée ou groupés pour préserver la durée de vie de la batterie, alors que les messages haute priorité sont toujours envoyés immédiatement.

Cette fonction est utile pour différencier vos messages en fonction de leur importance ou de leur sensibilité au temps. Par exemple, une notification sur des conditions routières dangereuses serait un bon candidat pour recevoir une priorité élevée, tandis qu’une notification sur une vente en cours devrait recevoir une priorité inférieure. Vous devez réfléchir à la nécessité de l’utilisation ou non d’une priorité perturbatrice pour la notification que vous envoyez, étant donné que se positionner constamment au sommet de la boîte de réception de votre utilisateur ou interrompre ses autres activités, peut avoir un impact négatif.

Dans Android O, la priorité de notification est devenue une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir la priorité d’un canal pendant sa configuration, puis utiliser le tableau de bord pour sélectionner le canal approprié lors de l’envoi de vos sons de notification. Pour les appareils exécutant des versions d’Android antérieures à O, il est possible de spécifier un niveau de priorité pour les notifications Android et FireOS via le tableau de bord de Braze et l’API de messagerie.

Pour envoyer un message à la totalité de votre base d’utilisateurs avec une priorité spécifique, nous vous recommandons de spécifier indirectement la priorité par une [configuration de canal de notification][17] (pour cibler les appareils O et ultérieurs) et envoyer la priorité individuelle à partir du tableau de bord (pour cibler les appareils &#60; O).

Référez-vous au tableau suivant concernant les niveaux de priorité que vous pouvez définir sur les notifications push Android ou Fire OS :

| Priorité | Description| Valeur de `priority` (pour les messages API) |
|------|-----------|----------------------------|
| Max | Messages urgents ou à délai de réponse critique. | `2` |
| Élevé | Communication importante, telle que le nouveau message d’un ami. | `1` |
| Par défaut | La plupart des notifications. Utilisez « par défaut » si votre message ne tombe pas explicitement dans les autres types de priorité. | `0` |
| Bas | Informations que vous voulez que les utilisateurs connaissent, mais ne nécessitant pas d’action immédiate. | `-1`|
| Min | Informations contextuelles ou d’arrière-plan. | `-2`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Consultez la documentation Google sur les [notifications Android][2] pour plus d’informations.

## Sons de notification

Dans Android O, les sons de notification sont devenus une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir le son d’un canal pendant sa configuration, puis utiliser le tableau de bord pour sélectionner le canal approprié lors de l’envoi de vos notifications.

Pour les appareils fonctionnant dans des versions d’Android antérieures à Android O, Braze vous permet de définir le son d’un message de notification push individuel via le composeur du tableau de bord. Vous pouvez le faire en spécifiant une ressource sonore locale sur l’appareil (par ex., `android.resource://com.mycompany.myapp/raw/mysound`). 

Sélectionner **Default** (Par défaut) dans ce champ jouera le son de notification par défaut sur le périphérique. Cela peut être spécifié par le biais de notre [API de messagerie][13] ou dans les **Settings (Paramètres)** dans l’assistant de composeur de notification push.

![][11]

Saisissez ensuite l’URI complet de ressources sonores (par ex., `android.resource://com.mycompany.myapp/raw/mysound`) dans l’invite du tableau de bord.

Pour envoyer un message à la totalité de votre base d’utilisateurs avec un son spécifique, nous vous recommandons de spécifier indirectement le son par une [configuration de canal de notification][16] (pour cibler les appareils O et ultérieurs) et envoyer le son individuel à partir du tableau de bord (pour cibler les appareils &#60; O).

[2]: http://developer.android.com/design/patterns/notifications.html
[9]: {% image_buster /assets/img_archive/summary_text.png %}
[11]: {% image_buster /assets/img_archive/sound_android.png %}
[12]: {% image_buster /assets/img_archive/deep_link.png %}
[13]: {{site.baseurl}}/api/endpoints/messaging/
[14]: https://github.com/Appboy/appboy-android-sdk/blob/master/samples/custom-broadcast/src/main/java/com/braze/custombroadcast/CustomBroadcastReceiver.java
[15]: {% image_buster /assets/img_archive/messagesummary.gif %}
[17]: https://developer.android.com/training/notify-user/channels#importance
[16]: https://developer.android.com/training/notify-user/channels