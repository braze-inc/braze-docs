---
nav_title: Ignorar o push interno
article_title: Ignorando as notificações por push internas do Braze para iOS
platform: iOS
page_order: 4
description: "Este artigo de referência aborda como ignorar as notificações por push internas do Braze."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Ignorando as notificações por push internas do Braze

A Braze usa notificações por push silenciosas para a implementação interna de determinados recursos avançados. Para a maioria das integrações, isso não requer alterações em nome do seu app. No entanto, se você integrar um recurso do Braze que dependa de notificações por push internas (por exemplo, rastreamento de desinstalação ou geofences), convém atualizar seu app para ignorar nossos pushes internos.

Se o seu app executa ações automáticas em inicializações de aplicativos ou push em segundo plano, considere a possibilidade de bloquear essa atividade para que ela não seja disparada por notificações por push internas. Por exemplo, se você tem uma lógica que chama seus servidores para obter novo conteúdo a cada push em segundo plano ou lançamento de aplicativo, provavelmente não gostaria que nossos pushes internos disparassem isso, pois haveria tráfego de rede desnecessário. Além disso, como o Braze envia certos tipos de pushes internos para todos os usuários aproximadamente ao mesmo tempo, não bloquear as chamadas de rede no lançamento de pushes internos poderia introduzir uma carga significativa no servidor.

## Verificação de ações automáticas em seu app

Você deve verificar se há ações automáticas em seu aplicativo nos seguintes locais e atualizar seu código para ignorar nossos pushes internos:

1. **Receptores push.** As notificações por push em segundo plano chamarão `application:didReceiveRemoteNotification:fetchCompletionHandler:` em`UIApplicationDelegate`.
2. **Delegado do app.** Os push em segundo plano podem iniciar apps [suspensos](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/TheAppLifeCycle/TheAppLifeCycle.html#//apple_ref/doc/uid/TP40007072-CH2-SW3) em segundo plano, disparando os métodos `application:willFinishLaunchingWithOptions:` e `application:didFinishLaunchingWithOptions:` em seu `UIApplicationDelegate`. Você pode verificar o site `launchOptions` desses métodos para determinar se o aplicativo foi iniciado a partir de um push em segundo plano.

## Uso de métodos utilitários push internos do Braze

Você pode usar os métodos utilitários em `ABKPushUtils` para verificar se o seu app recebeu ou foi iniciado por uma notificação por push interna do Braze. `isAppboyInternalRemoteNotification:` retornará `YES` em todas as notificações por push internas do Braze, enquanto `isUninstallTrackingRemoteNotification:` e `isGeofencesSyncRemoteNotification:` retornarão `YES` para rastreamento de desinstalação e notificações de sincronização de geofences, respectivamente. Consulte [`ABKPushUtils.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKPushUtils.h) para declarações de métodos.

## Exemplo de implementação {#internal-push-implementation-example}

{% tabs %}
{% tab OBJECTIVE C %}

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

