---
nav_title: Ignorer les notifications push internes
article_title: Ignorer les notifications push internes de Braze pour iOS
platform: Swift
page_order: 6
description: "Cet article explique comment ignorer les notifications push internes de Braze pour le SDK Swift."
channel:
  - push

---

# Ignorer les notifications push internes

> Braze utilise des [notifications push silencieuses]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/) pour la mise en œuvre interne de certaines fonctionnalités avancées. Pour la plupart des intégrations, cela ne nécessite aucune modification du côté de votre application. Cependant, si vous intégrez une fonction Braze qui repose sur des notifications push internes (par exemple, suivi de désinstallation ou géorepérages), nous vous conseillons de mettre à jour votre application pour ignorer les notifications push internes de Braze.

Si votre application prend des actions automatiques lors du lancement d'une application ou d'un push en arrière-plan, envisagez d'encadrer cette activité afin qu'elle ne soit pas déclenchée par nos notifications push internes. Par exemple, si vous avez une logique qui fait appel à vos serveurs pour de nouveaux contenus à chaque notification push en arrière-plan ou lancement d’application, vous ne voudriez probablement pas que le déclenchement de notifications push internes de Braze, car cela impliquerait un trafic réseau inutile. De plus, étant donné que Braze envoie certains types de notifications push internes à tous les utilisateurs à peu près au même moment, le fait de ne pas bloquer les appels réseau au lancement de notifications push internes pourrait entraîner une charge importante du serveur.

## Vérifier votre application pour les actions automatiques

Vérifiez que votre application ne contient pas d'actions automatiques aux endroits suivants et mettez à jour votre code pour ignorer les poussées internes de Braze :

1. **Récepteurs de notifications push.** Les notifications push en arrière-plan vont appeler `application:didReceiveRemoteNotification:fetchCompletionHandler:` sur le `UIApplicationDelegate`.
2. **Délégué d'application.** Les notifications push en arrière-plan peuvent lancer les applications [suspendues](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle) en arrière-plan, déclenchant les méthodes `application:willFinishLaunchingWithOptions:` et `application:didFinishLaunchingWithOptions:` sur votre `UIApplicationDelegate`. Vous pouvez vérifier les `launchOptions` de ces méthodes pour déterminer si l’application a été lancée à partir d’une notification push en arrière-plan.

## Utilisation de la méthode de l'utilitaire de poussée interne

Vous pouvez utiliser la méthode utilitaire statique dans `Braze.Notifications` pour vérifier si votre application a reçu ou a été lancée par un push interne de Braze. [`Braze.Notifications.isInternalNotification(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:)) retournera `true` pour toutes les notifications push internes de Braze, ce qui inclut le suivi des désinstallations, la synchronisation des drapeaux de fonctionnalité et les notifications de synchronisation des géorepérages.

## Exemple d’implémentation {#internal-push-implementation-example}

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

