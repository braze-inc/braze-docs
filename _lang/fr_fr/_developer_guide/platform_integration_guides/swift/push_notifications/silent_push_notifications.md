---
nav_title: Notifications push silencieuses
article_title: Notifications push silencieuses pour iOS
platform: Swift
page_order: 4
description: "Cet article explique comment implémenter des notifications push iOS silencieuses pour le SDK Swift."
channel:
  - push

---

# Notifications push silencieuses pour iOS

> Les notifications push vous permettent d'envoyer des notifications depuis votre appli lorsque des événements importants se produisent. 

Vous pourriez envoyer une notification push en cas d'alerte importante pour un utilisateur. Les notifications push peuvent également être silencieuses, ne contenir aucun message d’alerte ou son, et être utilisées uniquement pour mettre à jour l’interface de votre application ou déclencher une tâche en arrière-plan. Les notifications push silencieuses peuvent faire sortir votre application d’un état « Suspendu » ou « Pas en cours d’exécution » pour mettre le contenu à jour ou exécuter certaines tâches sans en avertir vos utilisateurs.

Braze dispose de plusieurs fonctionnalités qui s'appuient sur des notifications push silencieuses :

|Fonctionnalité|Expérience utilisateur|
|---|---|
|[Suivi des désinstallations]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/uninstall_tracking/) | L’utilisateur reçoit une notification push silencieuse et nocturne de suivi de désinstallation.|
|[Géorepérages]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences) | Synchronisation silencieuse des géorepérages du serveur vers l’appareil.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Mise en place de notifications push silencieuses

Pour utiliser les notifications push silencieuses afin de déclencher des travaux en arrière-plan, vous devez configurer votre app de manière à ce qu'elle reçoive des notifications même lorsqu'elle est en arrière-plan. Pour ce faire, ajoutez la capacité Modes d'arrière-plan à l'aide du volet **Signature et capacités** pour la cible d’appli principale dans Xcode. Cochez la case **Notifications à distance.**

![Xcode affiche la case à cocher du mode "notifications à distance" sous "capacités".]({% image_buster /assets/img_archive/background_mode.png %} "background mode enabled")

Même avec le mode arrière-plan des notifications à distance activé, le système ne lance pas votre application en arrière-plan si l’utilisateur a quitté l’application de manière forcée. L’utilisateur doit explicitement lancer l’application ou redémarrer l’appareil avant que l’application ne puisse être automatiquement lancée dans l’arrière-plan par le système.

Pour plus d'informations, reportez-vous aux [mises à jour du contexte de poussée](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) et à la [documentation](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:) `application:didReceiveRemoteNotification:fetchCompletionHandler:`.

## Envoi de notifications push silencieuses

Pour envoyer une notification push silencieuse, définissez l’indicateur `content-available` sur `1` dans une charge utile de notification push. 

{% alert note %}
Ce qu'Apple appelle une notification à distance est juste une notification push normale avec le drapeau `content-available` activé.
{% endalert %}

Le drapeau `content-available` peut être défini dans le tableau de bord de Braze ainsi que dans notre [objet Apple push]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) dans l'[API d'envoi messages.]({{site.baseurl}}/api/endpoints/messaging/)

{% alert warning %}
Il n'est pas recommandé d'attacher un titre et un corps `content-available=1`, car cela peut entraîner un comportement non défini. Pour qu'une notification soit vraiment silencieuse, excluez à la fois le titre et le corps lorsque vous définissez l'indicateur `content-available` sur `1.`. Pour plus de détails, reportez-vous à la [documentation Apple officielle sur les mises à jour en arrière-plan](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app).
{% endalert %}

![Le tableau de bord de Braze montre la case à cocher "content-available" qui se trouve dans l'onglet "settings" du compositeur de push.]({% image_buster /assets/img_archive/remote_notification.png %} "content available")

Lors de l’envoi d’une notification push silencieuse, vous pouvez également inclure certaines données dans la charge utile de la notification, afin que votre application puisse référencer l’événement. Cela pourrait vous éviter quelques requêtes réseau et augmenter la réactivité de votre application.

## Limitations des notifications silencieuses iOS

Le système d’exploitation iOS peut envoyer des notifications pour certaines fonctionnalités. Notez que si vous rencontrez des difficultés avec ces fonctionnalités, le blocage des notifications silencieuses d’iOS peut en être la cause.

Reportez-vous à la documentation d'Apple sur les [méthodes d'instance](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) et les [notifications non reçues](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23) pour plus de détails.

