---
nav_title: Notifications push silencieuses
article_title: Notifications push silencieuses pour iOS
platform: iOS
page_order: 4
description: "Cet article couvre l’implémentation des notifications push silencieuses dans votre application iOS."
channel:
  - Notification push

---

# Notifications push silencieuses

Les notifications distantes vous permettent d’informer votre application lorsque des événements importants se produisent. Vous pouvez avoir de nouveaux messages instantanés à livrer, des alertes d’actualité à envoyer ou le dernier épisode de l’émission télévisée préférée de votre utilisateur prêt à être téléchargé pour un visionnage hors ligne. Les notifications à distance sont idéales pour le contenu sporadique, mais immédiatement important, alors que le délai entre les récupérations en arrière-plan peut ne pas être acceptable. Les notifications à distance peuvent également être beaucoup plus efficaces que la récupération en arrière-plan, car votre application ne démarre que si nécessaire. Toutefois, les notifications à distance sont limitées par le système et ne peuvent pas lancer automatiquement votre application si l’utilisateur l’a forcée à quitter.

Une notification à distance est simplement une notification push normale pourvue de l’ensemble d’indicateurs `content-available`. Vous pouvez envoyer une notification push avec un message d’alerte informant l’utilisateur que quelque chose s’est passé, pendant que vous mettez à jour l’interface utilisateur en arrière-plan, mais les notifications à distance peuvent également être silencieuses, ne contenant aucun message d’alerte ou son, utilisé uniquement pour mettre à jour l’interface de votre application ou déclencher un travail en arrière-plan. Vous pouvez ensuite publier une notification locale lorsque vous avez terminé de télécharger ou de traiter le nouveau contenu.

Les notifications push silencieuses sont limitées en débit, alors n’ayez pas peur d’en envoyer autant que votre application en a besoin. iOS et les serveurs APNs contrôleront la fréquence de livraison, et vous n’aurez pas de problèmes si vous en envoyez trop. Si vos notifications push sont limitées, elles peuvent être retardées jusqu’à la prochaine fois que le périphérique envoie un paquet persistant ou reçoit une autre notification.

## Envoi de notifications silencieuses à distance

Pour envoyer une notification silencieuse à distance, définissez l’indicateur `content-available` sur `1` dans une charge utile de notification push. Lors de l’envoi d’une notification à distance silencieuse, vous pouvez également inclure certaines données dans la charge utile de la notification, afin que votre application puisse référencer l’événement. Cela pourrait vous éviter quelques requêtes réseau et augmenter la réactivité de votre application.

L’indicateur `content-available` peut être défini sur le tableau de bord de Braze et dans notre [Apple push object]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) dans le [API de messagerie][1].

![Le tableau de bord de Braze affichant la case « content-available » (contenu disponible) dans l’onglet « settings » (paramètres) du compositeur.][2]

## Utiliser des notifications distantes silencieuses pour déclencher le travail en arrière-plan

Les notifications silencieuses à distance peuvent faire sortir votre application d’un état « Suspendu » ou « Pas en cours d’exécution » pour mettre le contenu à jour ou exécuter certaines tâches sans en avertir vos utilisateurs. 

Pour utiliser des notifications distantes silencieuses pour déclencher un travail en arrière-plan, configurez l’indicateur `content-available` suivant les instructions précédentes sans message ni son. Configurez le mode arrière-plan de votre application pour activer `remote notifications` sous l’onglet **Capabilities** (Fonctionnalités) dans les paramètres de votre projet.

![Xcode affichant la case à cocher du mode « Notifications à distance » dans « Capacités ».][3]

L’activation du mode d’arrière-plan pour les notifications à distance est requise pour la fonction de [suivi de désinstallation][6] de Braze.

Même avec le mode arrière-plan des notifications à distance activé, le système ne lance pas votre application en arrière-plan si l’utilisateur a quitté l’application de manière forcée. L’utilisateur doit explicitement lancer l’application ou redémarrer le périphérique avant que l’application ne puisse être automatiquement lancée dans l’arrière-plan par le système.

Pour plus d’informations, référez-vous aux [mises à jour des notifications push en arrière-plan][4] et [`application:didReceiveRemoteNotification:fetchCompletionHandler:`][5].

## Limitations des notifications silencieuses iOS

Le système d’exploitation iOS peut envoyer des notifications pour certaines fonctionnalités. Notez que si vous rencontrez des difficultés avec ces fonctions, la porte de notifications silencieuse d’iOS peut être la cause.

Braze possède plusieurs fonctions qui reposent sur des notifications push iOS silencieuses :

|Caractéristique|Expérience utilisateur|
|---|---|
|Désinstaller le suivi | L’utilisateur reçoit une notification push silencieuse et nocturne de suivi de désinstallation.|
|Geofences | Synchronisation silencieuse des geofences du serveur vers le périphérique.|
{: .reset-td-br-1 .reset-td-br-2}

Se référer à la documentation d’Apple sur la [méthode d’instance][7] et les [notifications non reçues][8] pour plus d’informations.

[1]: {{site.baseurl}}/api/endpoints/messaging/
[2]: {% image_buster /assets/img_archive/remote_notification.png %} "content available"
[3]: {% image_buster /assets/img_archive/background_mode.png %} "background mode enabled"
[4]: https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app?language=objc
[5]: https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/uninstall_tracking/
[7]: https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application
[8]:https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23