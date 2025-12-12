{% multi_lang_include developer_guide/prerequisites/android.md %} Vous devrez également [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Paramètres

De nombreux paramètres avancés sont disponibles pour les notifications push de FireOS envoyées via le tableau de bord de Braze. Le présent article décrit ces fonctionnalités et la manière de les utiliser avec succès.

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

### TTL (Durée de vie) {#ttl}

Le champ **Durée en vie** (TTL) vous permet de définir une durée personnalisée de stockage des messages avec le service de messagerie push. Les valeurs par défaut pour la durée de vie sont de quatre semaines pour FCM et de 31 jours pour ADM.

### Texte récapitulatif {#summary-text}

Le texte récapitulatif vous permet de définir un texte supplémentaire dans la vue de notification étendue. Il sert également de légende pour les notifications avec des images.

![Un message Android avec le titre "Ceci est le titre de la notification" et le texte résumé "Ceci est le texte résumé de la notification".]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

Le texte récapitulatif s’affiche sous le corps du message dans la vue étendue. 

![Un message Android avec le titre "Ceci est le titre de la notification" et le texte résumé "Ceci est le texte résumé de la notification".]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Pour les notifications push qui incluent des images, le texte du message s’affiche dans la vue réduite tandis que le texte récapitulatif s’affiche comme légende d’image lorsque la notification est étendue. 

### URI personnalisés {#custom-uri}

La fonctionnalité **URI personnalisé** vous permet de spécifier une URL Web ou une ressource Android vers laquelle naviguer lorsque l'on clique sur la notification. Si aucun URI personnalisé n’est spécifié, cliquer sur la notification amène les utilisateurs dans votre application. Vous pouvez utiliser l’URI personnalisé pour créer un lien profond à l’intérieur de votre application et diriger les utilisateurs vers des ressources qui existent en dehors de votre application. Ceci peut être spécifié via l'[API Messages]({{site.baseurl}}/api/endpoints/messaging) ou notre tableau de bord sous **Paramètres avancés** dans le compositeur de push comme illustré :

![La création de liens profonds avancement dans le compositeur poussoir Braze.]({% image_buster /assets/img_archive/deep_link.png %})

### Priorité d’affichage de la notification

{% alert important %}
Le paramètre de priorité d’affichage de notification n’est plus utilisé sur les appareils exécutant Android O ou plus récents. Pour les appareils plus récents, définissez la priorité par le biais de la [configuration du canal de notification.](https://developer.android.com/training/notify-user/channels#importance)
{% endalert %}

Le niveau de priorité d’une notification push affecte la manière dont votre notification est affichée dans la barre de notification par rapport à d’autres notifications. Il peut également affecter la vitesse et la manière de livrer, car les messages normaux et moins prioritaires peuvent être envoyés avec une latence légèrement plus élevée ou groupés pour préserver la durée de vie de la batterie, alors que les messages haute priorité sont toujours envoyés immédiatement.

Dans Android O, la priorité de notification est devenue une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir la priorité d’un canal pendant sa configuration, puis utiliser le tableau de bord pour sélectionner le canal approprié lors de l’envoi de vos sons de notification. Pour les appareils fonctionnant avec des versions d'Android antérieures à O, la spécification d'un niveau de priorité pour les notifications FireOS est possible via le tableau de bord de Braze et l'API d'envoi de messages. 

Pour envoyer un message à l'ensemble de votre base d'utilisateurs avec une priorité spécifique, nous vous recommandons de spécifier indirectement la priorité via la [configuration du canal de communication](https://developer.android.com/training/notify-user/channels#importance) (pour cibler les appareils O+) *et d'* envoyer la priorité individuelle à partir du tableau de bord (pour cibler les appareils <O).

Les niveaux de priorité que vous pouvez définir sur les notifications push de Fire OS sont les suivants :

| Priorité | Description ou utilisation prévue | Valeur de `priority` (pour les messages API) |
|----------|--------------------------|-------------------------------------|
| Max      | Messages urgents ou à délai de réponse critique | `2` |
| Élevée     | Communication importante, telle que le nouveau message d’un ami | `1` |
| Par défaut  | La plupart des notifications : utilisez « par défaut » si votre message ne tombe pas explicitement dans les autres types de priorité | `0` |
| Faible      | Informations que vous voulez que les utilisateurs connaissent, mais ne nécessitant pas d’action immédiate | `-1` |
| Min      | Informations contextuelles ou d’arrière-plan. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Pour plus d'informations, consultez la documentation de Google sur [les notifications Android](http://developer.android.com/design/patterns/notifications.html).

### Sons {#sounds}

Dans Android O, les sons de notification sont devenus une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir le son d’un canal pendant sa configuration, puis utiliser le tableau de bord pour sélectionner le canal approprié lors de l’envoi de vos notifications.

Pour les appareils fonctionnant dans des versions d’Android antérieures à O, Braze vous permet de définir le son d’un message de notification push individuel via le composeur du tableau de bord. Vous pouvez le faire en spécifiant une ressource sonore locale sur l'appareil (par exemple, `android.resource://com.mycompany.myapp/raw/mysound`). Spécifier « par défaut » dans ce champ jouera le son de notification par défaut sur l’appareil. Cela peut être spécifié via l'[API Messages]({{site.baseurl}}/api/endpoints/messaging) ou le tableau de bord sous **Paramètres** dans le compositeur de push.

![Le réglage avancé du son dans le compositeur poussoir de Braze.]({% image_buster /assets/img_archive/sound_android.png %})

Saisissez l'URI complet de la ressource sonore (par exemple, `android.resource://com.mycompany.myapp/raw/mysound`) dans l'invite du tableau de bord.

Pour envoyer un message à l'ensemble de votre base d'utilisateurs avec un son spécifique, nous vous recommandons de spécifier indirectement le son via la [configuration du canal de communication](https://developer.android.com/training/notify-user/channels) (pour cibler les appareils O+) *et d'* envoyer le son individuel à partir du tableau de bord (pour cibler les appareils <O).
