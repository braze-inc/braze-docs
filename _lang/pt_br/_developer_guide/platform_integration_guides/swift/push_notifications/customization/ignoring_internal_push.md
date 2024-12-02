---
nav_title: Ignorar o push interno
article_title: Ignorando as notificações por push internas do Braze para iOS
platform: Swift
page_order: 6
description: "Este artigo aborda como ignorar as notificações por push internas da Braze para o Swift SDK."
channel:
  - push

---

# Ignorar notificações por push internas

> A Braze usa [notificações por push silenciosas]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/) para a implementação interna de determinados recursos avançados. Para a maioria das integrações, isso não requer alterações em nome do seu app. No entanto, se você integrar um recurso da Braze que dependa de notificações por push internas (como rastreamento de desinstalação ou geofences), talvez queira atualizar seu app para ignorar os pushes internos da Braze.

Se o seu app executa ações automáticas em inicializações de aplicativos ou push em segundo plano, considere a possibilidade de bloquear essa atividade para que ela não seja disparada por nossas notificações por push internas. Por exemplo, se você tem uma lógica que chama seus servidores para obter novo conteúdo a cada push em segundo plano ou inicialização de aplicativo, provavelmente não gostaria que os pushes internos do Braze disparassem isso, pois haveria tráfego de rede desnecessário. Além disso, como o Braze envia certos tipos de pushes internos para todos os usuários aproximadamente ao mesmo tempo, não bloquear as chamadas de rede no lançamento de pushes internos poderia introduzir uma carga significativa no servidor.

## Verificação de ações automáticas em seu app

Verifique se há ações automáticas em seu aplicativo nos seguintes locais e atualize seu código para ignorar os pushes internos do Braze:

1. **Receptores push.** As notificações por push em segundo plano chamarão `application:didReceiveRemoteNotification:fetchCompletionHandler:` em`UIApplicationDelegate`.
2. **Delegado do app.** Os push em segundo plano podem iniciar apps [suspensos](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle) em segundo plano, disparando os métodos `application:willFinishLaunchingWithOptions:` e `application:didFinishLaunchingWithOptions:` em seu `UIApplicationDelegate`. Verifique os `launchOptions` desses métodos para determinar se o aplicativo foi iniciado a partir de um push em segundo plano.

## Usando o método do utilitário push interno

Você pode usar o método do utilitário estático em `Braze.Notifications` para verificar se seu app recebeu ou foi iniciado por um push interno da Braze. [`Braze.Notifications.isInternalNotification(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:)) retornará `true` em todas as notificações por push internas da Braze, que incluem rastreamento de desinstalação, sincronização de sinalizadores de recursos e notificações de sincronização de geofences.

## Exemplo de implementação {#internal-push-implementation-example}

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
{% tab OBJECTIVE C %}


```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![BRZNotifications isInternalNotification:userInfo]) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% endtabs %}

