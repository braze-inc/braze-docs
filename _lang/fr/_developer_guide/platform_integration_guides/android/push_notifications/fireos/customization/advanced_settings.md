---
nav_title: Paramètres avancés
article_title: Paramètres avancés pour FireOS
platform: FireOS
page_order: 4
page_type: reference
description: "Cet article décrit les paramètres avancés disponibles pour les notifications push FireOS envoyées via le tableau de bord de Braze."
channel: push

---

# Paramètres avancés

Il existe de nombreux paramètres avancés disponibles pour les notifications push Android et FireOS envoyées via le tableau de bord de Braze. Le présent article décrit ces fonctionnalités et la manière de les utiliser avec succès.

![][1]

## TTL (Durée de vie) {#ttl}

Le champ **Time to Live** (TTL, Durée de vie) vous permet de définir une durée personnalisée pour stocker les messages avec le service de messagerie de notification push. Les valeurs par défaut de Braze pour la durée de vie sont de quatre semaines pour FCM et de 31 jours pour ADM.

## Texte récapitulatif {#summary-text}

Le texte récapitulatif vous permet de définir un texte supplémentaire dans la vue de notification étendue. Il sert également de légende pour les notifications avec des images.

![Un message Android avec le titre « Salutations d’Appboy ! », le message « C’est le corps du message ! Vous pouvez même ajouter des émojis. » et un résumé du texte « Il s’agit du texte récapitulatif. »][9]

Le texte récapitulatif s’affiche sous le corps du message dans la vue étendue.

Pour les notifications push qui incluent des images, le texte du message s’affiche dans la vue réduite tandis que le texte récapitulatif s’affiche comme légende d’image lorsque la notification est étendue. 

![Un message Android avec le titre « Appboy ! », le message « C’est le corps du message. » et résumé du texte « et ceci est le texte récapitulatif. »][15]

## URI personnalisés {#custom-uri}

La fonctionnalité d’**URI personnalisé** vous permet de spécifier une URL Web ou une ressource Android vers laquelle naviguer quand la notification est cliquée. Si aucun URI personnalisé n’est spécifié, cliquer sur la notification amène les utilisateurs dans votre application. Vous pouvez utiliser l’URI personnalisé pour créer un lien profond à l’intérieur de votre application et diriger les utilisateurs vers des ressources qui existent en dehors de votre application. Cela peut être spécifié par le biais de l’[API de messagerie][13] ou par notre tableau de bord sous **Advanced Settings (Paramètres avancés)** dans l’assistant de composeur de notification push comme illustré :

![Le paramétrage avancé de la création de liens profonds dans le composeur de notification push Braze.][12]

## Priorité d’affichage de la notification

{% alert important %}
Le paramètre de priorité d’affichage de notification n’est plus utilisé sur les appareils exécutant Android O ou plus récents. Pour les nouveaux appareils, définissez la priorité dans la [configuration du canal de notification](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

Le niveau de priorité d’une notification push affecte la manière dont votre notification est affichée dans la barre de notification par rapport à d’autres notifications. Il peut également affecter la vitesse et la manière de livrer, car les messages normaux et moins prioritaires peuvent être envoyés avec une latence légèrement plus élevée ou groupés pour préserver la durée de vie de la batterie, alors que les messages haute priorité sont toujours envoyés immédiatement.

Dans Android O, la priorité de notification est devenue une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir la priorité d’un canal pendant sa configuration, puis utiliser le tableau de bord pour sélectionner le canal approprié lors de l’envoi de vos sons de notification. Pour les appareils exécutant des versions d’Android antérieures à O, il est possible de spécifier un niveau de priorité pour les notifications Android et FireOS via le tableau de bord de Braze et l’API de messagerie. 

Pour envoyer un message à la totalité de votre base d’utilisateurs avec une priorité spécifique, nous vous recommandons de spécifier indirectement la priorité par une [configuration de canal de notification][17] (pour cibler les appareils O et ultérieurs) *et* envoyer la priorité individuelle à partir du tableau de bord (pour cibler les appareils &#60; O).

Les niveaux de priorité que vous pouvez définir sur les notifications push Android ou Fire OS sont les suivants :

| Priorité | Description ou utilisation prévue | Valeur de `priority` (pour les messages API) |
|----------|--------------------------|-------------------------------------|
| Max      | Messages urgents ou à délai de réponse critique | `2` |
| Élevé     | Communication importante, telle que le nouveau message d’un ami | `1` |
| Par défaut  | La plupart des notifications : utilisez « par défaut » si votre message ne tombe pas explicitement dans les autres types de priorité | `0` |
| Bas      | Informations que vous voulez que les utilisateurs connaissent, mais ne nécessitant pas d’action immédiate | `-1` |
| Min      | Informations contextuelles ou d’arrière-plan. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Consultez la [notification Android][2] de Google pour plus d’informations.

## Sons {#sounds}

Dans Android O, les sons de notification sont devenus une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir le son d’un canal pendant sa configuration, puis utiliser le tableau de bord pour sélectionner le canal approprié lors de l’envoi de vos notifications.

Pour les appareils fonctionnant dans des versions d’Android antérieures à O, Braze vous permet de définir le son d’un message de notification push individuel via le composeur du tableau de bord. Vous pouvez le faire en spécifiant une ressource sonore locale sur l’appareil (par ex., `android.resource://com.mycompany.myapp/raw/mysound`). Spécifier « par défaut » dans ce champ jouera le son de notification par défaut sur le périphérique. Cela peut être spécifié par le biais de l’[API de messagerie][13] ou par le tableau de bord sous **Advanced Settings (Paramètres avancés)** dans l’assistant de composeur de notification push.

![Le paramétrage avancé de son dans le composeur de notification push Braze.][11]

Saisissez l’URI complet de ressources sonores (par ex., `android.resource://com.mycompany.myapp/raw/mysound`) dans l’invite du tableau de bord.

Pour envoyer un message à la totalité de votre base d’utilisateurs avec un son spécifique, nous vous recommandons de spécifier indirectement le son par une [configuration de canal de notification][16] (pour cibler les appareils O et ultérieurs) *et* envoyer le son individuel à partir du tableau de bord (pour cibler &#60;les appareils antérieurs à O).

[1]: {% image_buster /assets/img_archive/android_advanced_settings.png %}
[2]: http://developer.android.com/design/patterns/notifications.html
[9]: {% image_buster /assets/img_archive/summary_text.png %}
[11]: {% image_buster /assets/img_archive/sound_android.png %}
[12]: {% image_buster /assets/img_archive/deep_link.png %}
[13]: {{site.baseurl}}/api/endpoints/messaging
[15]: {% image_buster /assets/img_archive/messagesummary.gif %}
[17]: https://developer.android.com/training/notify-user/channels#importance
[16]: https://developer.android.com/training/notify-user/channels
