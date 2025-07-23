{% multi_lang_include developer_guide/prerequisites/swift.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Limitações do iOS

O sistema operacional iOS pode bloquear notificações para alguns recursos. Se você estiver enfrentando dificuldades com esses recursos, o gate de notificações silenciosas do iOS pode ser a causa. Para obter mais detalhes, consulte a documentação sobre [o método de instância](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) e [as notificações não recebidas](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23) da Apple.

## Configurando notificações por push silenciosas

Para usar notificações por push silenciosas para disparar trabalho em segundo plano, você deve configurar seu app para receber notificações mesmo quando estiver em segundo plano. Para fazer isso, adicione a capacidade de Modos de Fundo usando o painel **Assinatura e Capacidades** ao alvo principal do app no Xcode. Selecione a caixa de seleção **Notificações remotas**.

![O Xcode mostra a caixa de seleção do modo "notificações remotas" em "capacitações".]({% image_buster /assets/img_archive/background_mode.png %} "background mode enabled")

Mesmo com o modo de fundo de notificações remotas ativado, o sistema não iniciará seu app em segundo plano se o usuário tiver forçado o encerramento do aplicativo. O usuário deve iniciar explicitamente o aplicativo ou reiniciar o dispositivo antes que o app possa ser lançado automaticamente em segundo plano pelo sistema.

Para saber mais, consulte as [atualizações de fundo do push](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) e a [documentação](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:) do site `application:didReceiveRemoteNotification:fetchCompletionHandler:`.

## Enviando notificações por push silenciosas

Para enviar uma notificação por push silenciosa, defina a `content-available` bandeira para `1` em uma carga útil de notificação por push. 

{% alert note %}
O que a Apple chama de notificação remota é apenas uma notificação por push normal com a sinalização `content-available` definida.
{% endalert %}

A `content-available` flag pode ser definida no dashboard da Braze, assim como dentro do nosso [objeto de push da Apple]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) na [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/).

{% alert warning %}
Anexar tanto um título quanto um corpo de texto com `content-available=1` não é recomendado porque pode levar a um comportamento indefinido. Para garantir que uma notificação seja realmente silenciosa, exclua tanto o título quanto o corpo de texto ao definir a sinalização`content-available` para `1.` Para mais detalhes, consulte a [documentação oficial da Apple sobre atualizações em segundo plano](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app).
{% endalert %}

![O painel do Braze mostra a caixa de seleção "content-available" (conteúdo disponível) encontrada na guia "settings" (configurações) do criador do push.]({% image_buster /assets/img_archive/remote_notification.png %} "content available" (conteúdo disponível))

Ao enviar uma notificação por push silenciosa, você também pode querer incluir alguns dados na carga útil da notificação, para que seu aplicativo possa referenciar o evento. Isso pode economizar algumas solicitações de rede e aumentar a capacidade de resposta do seu app.

## Ignorar notificações por push internas

O Braze usa notificações por push silenciosas para lidar internamente com determinados recursos avançados, como rastreamento de desinstalação ou geofences. Se o seu app executa ações automáticas em inicializações de aplicativos ou push em segundo plano, considere a possibilidade de bloquear essa atividade para que ela não seja disparada por nenhuma notificação por push interna.

Por exemplo, se você tem uma lógica que chama seus servidores para obter novo conteúdo a cada push em segundo plano ou lançamento de aplicativo, talvez queira impedir o disparo dos pushes internos do Braze para evitar tráfego de rede desnecessário. Como o Braze envia certos tipos de push internos para todos os usuários aproximadamente ao mesmo tempo, poderá ocorrer uma carga significativa no servidor se as chamadas de rede no lançamento de pushes internos não forem bloqueadas.

### Etapa 1: Verifique se há ações automáticas em seu app

Verifique se há ações automáticas em seu aplicativo nos seguintes locais e atualize seu código para ignorar os pushes internos do Braze:

1. **Receptores push.** As notificações por push em segundo plano chamarão `application:didReceiveRemoteNotification:fetchCompletionHandler:` no site `UIApplicationDelegate`.
2. **Delegado do app.** Os push em segundo plano podem iniciar apps [suspensos](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle) em segundo plano, disparando os métodos `application:willFinishLaunchingWithOptions:` e `application:didFinishLaunchingWithOptions:` em seu `UIApplicationDelegate`. Verifique os `launchOptions` desses métodos para determinar se o aplicativo foi iniciado a partir de um push em segundo plano.

### Etapa 2: Use o método do utilitário push interno

Você pode usar o método do utilitário estático em `Braze.Notifications` para verificar se seu app recebeu ou foi iniciado por um push interno da Braze. [`Braze.Notifications.isInternalNotification(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:)) retornará `true` em todas as notificações por push internas da Braze, que incluem rastreamento de desinstalação, sincronização de sinalizadores de recursos e notificações de sincronização de geofences.

Por exemplo:

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
