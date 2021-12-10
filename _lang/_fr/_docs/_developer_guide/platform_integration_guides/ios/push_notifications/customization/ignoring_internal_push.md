---
nav_title: Ignorer la poussée interne
article_title: Ignorer les notifications Push internes de Braze pour iOS
platform: iOS
page_order: 0.2
description: "Cet article explique comment ignorer les notifications push internes de Braze."
channel:
  - Pousser
---

# Ignorer les notifications push internes de Braze

Braze utilise des notifications push silencieuses pour l'implémentation interne de certaines fonctionnalités avancées. Pour la plupart des intégrations, cela ne nécessite aucun changement au nom de votre application. Cependant, si vous intégrez une fonctionnalité Braze qui s'appuie sur les notifications push internes (i.e. désinstaller le suivi ou les géofences), vous pouvez mettre à jour votre application pour ignorer les poussées internes de Brase.

Si votre application prend des actions automatiques lors du lancement de l'application ou des poussées en arrière-plan, vous devriez envisager de mettre en garde cette activité afin qu'elle ne soit pas déclenchée par les notifications push internes de Braze. Par exemple, si vous avez une logique qui appelle vos serveurs pour de nouveaux contenus à chaque lancement de push ou d'application en arrière-plan, vous ne voudrez probablement pas que les poussées internes de Braze déclenchent cela parce que vous devrez subir un trafic réseau inutile. De plus, parce que Braze envoie certains types de poussées internes à tous les utilisateurs à peu près en même temps, ne pas gater les appels réseau au lancement à partir de pushes internes pourrait introduire une charge de serveur significative.

## Vérification de votre application pour les actions automatiques

Vous devriez vérifier votre application pour trouver des actions automatiques dans les endroits suivants et mettre à jour votre code pour ignorer les poussées internes de Braze :

1. **Récepteurs Push.** Les notifications push en arrière-plan appelleront `application:didReceiveRemoteNotification:fetchCompletionHandler:` sur le `UIApplicationDelegate`.
2. **Délégué de la candidature.** Les pousses en arrière-plan peuvent lancer [des applications suspendues][4] en arrière-plan, déclenchement de l'application `: willFinishLaunchingWithOptions :` et `application:didFinishLaunchingWithOptions:` méthodes sur votre `UIApplicationDelegate`. Vous pouvez vérifier les `options de lancement` de ces méthodes pour déterminer si l'application a été lancée à partir d'une poussée en arrière-plan.

## Utilisation des méthodes internes de l'utilitaire push de Braze

Vous pouvez utiliser les méthodes utilitaires dans `ABKPushUtils` pour vérifier si votre application a été reçue ou a été lancée par une poussée interne de Braze. `isAppboyInternalRemoteNotification:` retournera `OUI` sur toutes les notifications push internes de Braze, tandis que `isUninstallTrackingRemoteNotification:` et `isGeofencesSyncRemoteNotification:` retournera `OUI` pour les notifications de désinstallation du suivi et de synchronisation des géorepérages, respectivement. Voir [`ABKPushUtils.h`][1] pour les déclarations de méthode.

## Exemple d'implémentation {#internal-push-implementation-example}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  NSDictionary *pushDictionary = launchOptions[UIApplicationLaunchOptionsRemoteNotificationKey];
  BOOL launchedFromAppboyInternalPush = pushDictionary && [ABKPushUtils isAppboyInternalRemoteNotification:pushDictionary];
  if (! aunchedFromAppboyInternalPush) {
    // ... Logique portée ici (par exemple, pinging votre serveur pour télécharger le contenu) ...
  }
}
```

```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![ABKPushUtils isAppboyInternalRemoteNotification:userInfo]) {
    // ... Logique portée ici (par exemple, ping du serveur pour le contenu) ...
  }
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = nil) -> Bool {
  let pushDictionary = launchOptions?[UIApplicationLaunchOptionsKey.remoteNotification] comme? NSDictionary comme? [AnyHashable : Any] ?? [:]
  let launchedFromAppboyInternalPush = ABKPushUtils.isAppboyInternalRemoteNotification(pushDictionary)
  if (!launchedFromAppboyInternalPush) {
    // ... Logique portée ici (par exemple, pinging votre serveur pour télécharger le contenu) ...
  }
}
```

```swift
application func(_ application: UIApplication,
                 didReceiveRemoteNotification userInfo: [AnyHashable : Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  if (! BKPushUtils. sAppboyInternalRemoteNotification(userInfo)) {
    // ... Logique portée ici (par exemple, ping du serveur pour le contenu) ...
  }
}
```

{% endtab %}
{% endtabs %}

[1]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKPushUtils.h
[4]: https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/TheAppLifeCycle/TheAppLifeCycle.html#//apple_ref/doc/uid/TP40007072-CH2-SW3