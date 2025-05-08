---
nav_title: Ignorer les notifications push internes
article_title: Ignorer les notifications push internes de Braze pour iOS
platform: iOS
page_order: 4
description: "Cet article de référence explique comment ignorer les notifications push internes de Braze."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Ignorer les notifications push internes de Braze

Braze utilise des notifications push silencieuses pour l’implémentation interne de certaines fonctions avancées. Pour la plupart des intégrations, cela ne nécessite aucune modification du côté de votre application. Toutefois, si vous intégrez une fonctionnalité de Braze qui repose sur des notifications push internes (par exemple, le suivi de désinstallation ou les géorepérages), vous pouvez mettre à jour votre application pour ignorer nos push internes.

Si votre application effectue des actions automatiques lors du lancement d'une application ou d'un push en arrière-plan, vous devriez envisager de filtrer cette activité afin qu'elle ne soit pas déclenchée par des notifications push internes. Par exemple, si vous avez une logique qui appelle vos serveurs pour un nouveau contenu à chaque poussée en arrière-plan ou au lancement d'une application, vous ne voudrez probablement pas que nos poussées internes déclenchent cela, car cela entraînerait un trafic réseau inutile. De plus, étant donné que Braze envoie certains types de notifications push internes à tous les utilisateurs à peu près au même moment, le fait de ne pas bloquer les appels réseau au lancement de notifications push internes pourrait entraîner une charge importante du serveur.

## Vérifier votre application pour les actions automatiques

Vous devez vérifier votre demande d’actions automatiques dans les endroits suivants et mettre à jour votre code pour ignorer nos notifications push internes :

1. **Récepteurs de notifications push.** Les notifications push en arrière-plan vont appeler `application:didReceiveRemoteNotification:fetchCompletionHandler:` sur le `UIApplicationDelegate`.
2. **Délégué d'application.** Les notifications push en arrière-plan peuvent lancer les applications [suspendues](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/TheAppLifeCycle/TheAppLifeCycle.html#//apple_ref/doc/uid/TP40007072-CH2-SW3) en arrière-plan, déclenchant les méthodes `application:willFinishLaunchingWithOptions:` et `application:didFinishLaunchingWithOptions:` sur votre `UIApplicationDelegate`. Vous pouvez vérifier le `launchOptions` de ces méthodes pour déterminer si l’application a été lancée à partir d’une notification push en arrière-plan.

## Utilisation des méthodes utilitaires de poussée interne de Braze

Vous pouvez utiliser les méthodes de l’utilitaire dans `ABKPushUtils` pour vérifier si votre application a été reçue ou a été lancée par une notification push interne de Braze. `isAppboyInternalRemoteNotification:` reviendra `YES` sur toutes les notifications push internes de Braze, alors que `isUninstallTrackingRemoteNotification:` et `isGeofencesSyncRemoteNotification:` reviendra `YES` pour le suivi de désinstallation et les notifications de synchronisation de géorepérage, respectivement. Pour connaître les déclarations de méthodes, reportez-vous à [`ABKPushUtils.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKPushUtils.h).

## Exemple d’implémentation {#internal-push-implementation-example}

{% tabs %}
{% tab OBJECTIF-C %}

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  NSDictionary *pushDictionary = launchOptions[UIApplicationLaunchOptionsRemoteNotificationKey];
  BOOL launchedFromAppboyInternalPush = pushDictionary && [ABKPushUtils isAppboyInternalRemoteNotification:pushDictionary];
  if (!launchedFromAppboyInternalPush) {
    // ... Gated logic here (such as pinging your server to download content) ...
  }
}
```

```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![ABKPushUtils isAppboyInternalRemoteNotification:userInfo]) {
    // ... Gated logic here (such as pinging server for content) ...
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
    // ... Gated logic here (such as pinging your server to download content) ...
  }
}
```

```swift
func application(_ application: UIApplication,
                 didReceiveRemoteNotification userInfo: [AnyHashable : Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  if (!ABKPushUtils.isAppboyInternalRemoteNotification(userInfo)) {
    // ... Gated logic here (such as pinging server for content) ...
  }
}
```

{% endtab %}
{% endtabs %}

