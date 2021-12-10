---
nav_title: Notifications Push silencieuses
article_title: Notifications Push silencieuses pour iOS
platform: iOS
page_order: 4
description: "Cet article décrit comment implémenter les notifications push silencieuses dans votre application iOS."
channel:
  - Pousser
---

# Notifications push silencieuses

Les notifications à distance vous permettent de notifier votre application lorsque des événements importants se produisent. Il se peut que vous ayez de nouveaux messages instantanés à envoyer, des alertes d'actualités à envoyer, ou le dernier épisode de la série TV préférée de votre utilisateur prêt à être téléchargé pour une visualisation hors ligne. Les notifications distantes sont idéales pour les contenus sporadiques mais immédiatement importants, où le délai entre les récupérations en arrière-plan pourrait ne pas être acceptable. Les notifications à distance peuvent également être beaucoup plus efficaces que la récupération en arrière-plan, car votre application ne se lance que lorsque nécessaire. Cependant, les notifications à distance sont limitées par le système et ne peuvent pas lancer automatiquement votre application si l'utilisateur a force-quitté.

Une notification distante est vraiment juste une notification Push normale avec le marqueur `Content-available` défini. Vous pouvez envoyer un push avec un message d'alerte informant l'utilisateur que quelque chose s'est passé, pendant que vous mettez à jour l'interface en arrière-plan. Mais les notifications distantes peuvent également être silencieuses, sans aucun message d'alerte ni aucun son, utilisé uniquement pour mettre à jour l'interface de votre application ou déclencher un travail en arrière-plan. Vous pouvez alors poster une notification locale lorsque vous avez fini de télécharger ou de traiter le nouveau contenu.

Les notifications push silencieuses sont limitées au rythme, donc n'ayez pas peur d'en envoyer autant que vous en avez besoin. Les serveurs iOS et APN contrôleront la fréquence de livraison et vous n'aurez aucun mal à en envoyer trop. Si vos notifications push sont limitées, elles peuvent être retardées jusqu'à la prochaine fois que le périphérique envoie un paquet en veille ou reçoit une autre notification.

## Envoi de notifications à distance silencieuses

Pour envoyer une notification distante en mode silencieux, définissez le drapeau `contenu-disponible` à 1 dans un bloc de notification push. Lorsque vous envoyez une notification à distance silencieuse, vous pouvez également inclure certaines données dans la charge utile de notification, afin que votre application puisse référencer l'événement. Cela pourrait vous faire économiser quelques requêtes réseau et augmenter la réactivité de votre application.

Le drapeau `contenent-available` peut être défini dans le tableau de bord Braze (photo ci-dessous) ainsi que dans notre [Apple Push Object]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) dans la [Messaging API][1].

!\[content-available\]\[2\]

## Utiliser les notifications à distance silencieuses pour déclencher un travail en arrière-plan

Les notifications à distance silencieuses peuvent réveiller votre application depuis un état "Envoyé" ou "Ne pas exécuter" pour mettre à jour le contenu ou exécuter certaines tâches sans notifier vos utilisateurs.

Pour utiliser des notifications distantes silencieuses pour déclencher un travail en arrière-plan, configurez le drapeau `contenent-available` en suivant les instructions ci-dessus sans aucun message ni son. Veuillez configurer le mode d'arrière-plan de votre application pour activer `les notifications à distance` dans l'onglet "Capabilities" dans les paramètres de votre projet.

!\[background-mode-enabled\]\[3\]

L'activation du mode d'arrière-plan pour les notifications à distance est nécessaire pour la fonctionnalité [Désinstaller le Tracking][6] de Brase.

Même avec le mode en arrière-plan des notifications à distance activé, le système ne lancera pas votre application en arrière-plan si l'utilisateur a forcé la fermeture de l'application. L'utilisateur doit explicitement lancer l'application ou redémarrer l'appareil avant que l'application ne puisse être lancée automatiquement en arrière-plan par le système.

Pour plus d'informations, veuillez vous référer à la documentation d'Apple sur [Pushing Background Updates][4] et [`application:didReceiveRemoteNotification:fetchCompletionHandler:`][5].

## Limitation des notifications silencieuses iOS
Le système d'exploitation iOS peut bloquer les notifications pour certaines fonctionnalités. Veuillez noter que si vous rencontrez des difficultés avec ces fonctionnalités, la porte des notifications silencieuses d'iOS pourrait en être la cause.

Braze a plusieurs fonctionnalités qui s'appuient sur iOS Silent Push Notifications:

| Fonctionnalités       | Expérience utilisateur                                                                |
| --------------------- | ------------------------------------------------------------------------------------- |
| Désinstaller le suivi | L'utilisateur reçoit une poussée de suivi silencieuse et nocturne de désinstallation. |
| Géorepérages          | Synchronisation silencieuse des géorepérages du serveur vers l'appareil.              |
{: .reset-td-br-1 .reset-td-br-2}

Pour plus d'informations, consultez le site développeur d'Apple sur la [méthode d'instance][7] et les [notifications non reçues][8].
[2]: {% image_buster /assets/img_archive/remote_notification.png %} "contenu disponible" [3]: {% image_buster /assets/img_archive/background_mode.png %} "mode d'arrière-plan activé"

[1]: {{site.baseurl}}/api/endpoints/messaging/
[4]: https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app?language=objc
[5]: https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/uninstall_tracking/#uninstall-tracking
[7]: https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application
[8]: https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23