{% multi_lang_include developer_guide/prerequisites/swift.md %} Vous devrez également [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Limites de l'iOS

Le système d’exploitation iOS peut envoyer des notifications pour certaines fonctionnalités. Notez que si vous rencontrez des difficultés avec ces fonctionnalités, le blocage des notifications silencieuses d’iOS peut en être la cause. Pour plus de détails, consultez la documentation d'Apple sur les [méthodes d'instance](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) et les [notifications non reçues](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23).

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

## Ignorer les notifications push internes

Braze utilise des notifications push silencieuses pour gérer en interne certaines fonctionnalités avancées, telles que le suivi des désinstallations ou les géorepérages. Si votre application prend des actions automatiques au lancement d'une application ou lors d'un push en arrière-plan, envisagez d'encadrer cette activité afin qu'elle ne soit pas déclenchée par des notifications push internes.

Par exemple, si votre logique appelle vos serveurs pour obtenir du nouveau contenu à chaque poussée en arrière-plan ou lancement d'application, vous voudrez peut-être empêcher le déclenchement des poussées internes de Braze afin d'éviter un trafic réseau inutile. Étant donné que Braze envoie certains types d'appels internes à tous les utilisateurs à peu près en même temps, une charge importante du serveur peut se produire si les appels réseau au lancement provenant d'appels internes ne sont pas gérés.

### Étape 1 : Vérifiez que votre application ne contient pas d'actions automatiques

Vérifiez que votre application ne contient pas d'actions automatiques aux endroits suivants et mettez à jour votre code pour ignorer les poussées internes de Braze :

1. **Récepteurs de notifications push.** Les notifications push en arrière-plan vont appeler `application:didReceiveRemoteNotification:fetchCompletionHandler:` sur le `UIApplicationDelegate`.
2. **Délégué d'application.** Les notifications push en arrière-plan peuvent lancer les applications [suspendues](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle) en arrière-plan, déclenchant les méthodes `application:willFinishLaunchingWithOptions:` et `application:didFinishLaunchingWithOptions:` sur votre `UIApplicationDelegate`. Vous pouvez vérifier les `launchOptions` de ces méthodes pour déterminer si l’application a été lancée à partir d’une notification push en arrière-plan.

### Étape 2 : Utilisez la méthode de l'utilitaire de poussée interne

Vous pouvez utiliser la méthode utilitaire statique dans `Braze.Notifications` pour vérifier si votre application a reçu ou a été lancée par un push interne de Braze. [`Braze.Notifications.isInternalNotification(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:)) retournera `true` pour toutes les notifications push internes de Braze, ce qui inclut le suivi des désinstallations, la synchronisation des drapeaux de fonctionnalité et les notifications de synchronisation des géorepérages.

Par exemple :

{% tabs %}
{% tab swift %}


```swift
func application(_ application: UIApplication,
                 didReceiveRemoteNotification userInfo: [AnyHashable : Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  if (!Braze.Notifications.isInternalNotification(userInfo)) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% tab OBJECTIF-C %}


```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![BRZNotifications isInternalNotification:userInfo]) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% endtabs %}
