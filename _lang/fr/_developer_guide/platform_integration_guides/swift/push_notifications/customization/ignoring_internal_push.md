---
hidden: true
nav_title: Ignorer les notifications push internes
article_title: Ignorer les notifications push internes de Braze pour iOS
platform: iOS
page_order: 4
description: "Cet article traite de la façon d’ignorer les notifications push internes de Braze."
channel:
  - Notification push

---

# Ignorer les notifications push internes de Braze

Braze utilise des notifications push silencieuses pour l’implémentation interne de certaines fonctions avancées. Pour la plupart des intégrations, cela ne nécessite aucune modification du côté de votre application. Cependant, si vous intégrez une fonction Braze qui repose sur des notifications push internes (c.-à-d., suivi de désinstallation ou geofence), vous pouvez mettre à jour votre application pour ignorer les notifications push internes de Braze.

Si votre application prend des actions automatiques sur les lancements d’applications ou notifications push en arrière-plan, vous devez envisager de synchroniser cette activité afin qu’elle ne soit pas déclenchée par les notifications push internes de Braze. Par exemple, si vous avez une logique qui fait appel à vos serveurs pour de nouveaux contenus à chaque notification push en arrière-plan ou lancement d’application, vous ne voudriez probablement pas que le déclenchement de notifications push internes de Braze, car cela impliquerait un trafic réseau inutile. De plus, étant donné que Braze envoie certains types de notifications push internes à tous les utilisateurs à peu près au même moment, le fait de ne pas bloquer les appels réseau au lancement de notifications push internes pourrait entraîner une charge importante du serveur.

## Vérifier votre application pour les actions automatiques

Vous devez vérifier votre demande d’actions automatiques dans les endroits suivants et mettre à jour votre code pour ignorer les notifications push internes de Braze :

1. **Récepteurs de notification push.** Les notifications push en arrière-plan vont appeler `application:didReceiveRemoteNotification:fetchCompletionHandler:` sur le `UIApplicationDelegate`.
2. **Délégué d’application.** Les notifications push en arrière-plan peuvent lancer les applications [suspendues][4] en arrière-plan, déclenchant les méthodes `application:willFinishLaunchingWithOptions:` et `application:didFinishLaunchingWithOptions:` sur votre `UIApplicationDelegate`. Vous pouvez vérifier le `launchOptions` de ces méthodes pour déterminer si l’application a été lancée à partir d’une notification push en arrière-plan.

## Utiliser les méthodes utilitaires de notifications push interne de Braze

Vous pouvez utiliser les méthodes de l’utilitaire dans `ABKPushUtils` pour vérifier si votre application a été reçue ou a été lancée par une notification push interne de Braze. `isAppboyInternalRemoteNotification:` reviendra `YES` sur toutes les notifications push internes de Braze, alors que `isUninstallTrackingRemoteNotification:` et `isGeofencesSyncRemoteNotification:` reviendra `YES` pour le suivi de désinstallation et les notifications de synchronisation de geofence, respectivement. Consultez [`ABKPushUtils.h`][1] pour les déclarations de méthode.

## Exemple d’implémentation {#internal-push-implementation-example}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  NSDictionary *pushDictionary = launchOptions[UIApplicationLaunchOptionsRemoteNotificationKey];
  BOOL launchedFromAppboyInternalPush = pushDictionary && [ABKPushUtils isAppboyInternalRemoteNotification:pushDictionary];
  if (!launchedFromAppboyInternalPush) {
    // ... Gated logic here (e.g., pinging your server to download content) ...
  }
}
```

```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![ABKPushUtils isAppboyInternalRemoteNotification:userInfo]) {
    // ... Gated logic here (e.g., pinging server for content) ...
  }
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = nil) -> Bool {
  let pushDictionary = launchOptions?[UIApplicationLaunchOptionsKey.remoteNotification] as? NSDictionary as? [AnyHashable : Any] ?? [:]
  let launchedFromAppboyInternalPush = ABKPushUtils.isAppboyInternalRemoteNotification(pushDictionary)
  if (!launchedFromAppboyInternalPush) {
    // ... Gated logic here (e.g., pinging your server to download content) ...
  }
}
```

```swift
func application(_ application: UIApplication,
                 didReceiveRemoteNotification userInfo: [AnyHashable : Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  if (!ABKPushUtils.isAppboyInternalRemoteNotification(userInfo)) {
    // ... Gated logic here (e.g., pinging server for content) ...
  }
}
```

{% endtab %}
{% endtabs %}

[1]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKPushUtils.h
[4]: https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/TheAppLifeCycle/TheAppLifeCycle.html#//apple_ref/doc/uid/TP40007072-CH2-SW3