## Limites de taxa

As notificações por push são limitadas por taxa, então não tenha medo de enviar quantas sua aplicação precisar. O iOS e o serviço de Notificações por Push da Apple (APNs) controlarão a frequência com que são entregues, e você não terá problemas por enviar muitas. Se suas notificações por push forem limitadas, elas podem ser atrasadas até a próxima vez que o dispositivo enviar um pacote keep-alive ou receber outra notificação.

## Configurando notificações por push

### Etapa 1: Faça upload do seu token APNs

{% multi_lang_include developer_guide/swift/apns_token.md %}

### Etapa 2: Ativar push capabilities

No Xcode, acesse a seção **Assinatura & Capacidades** do alvo principal do app e adicione a capacidade de notificações por push.

![A seção 'Assinatura & Capacidades' em um projeto Xcode.]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

### Etapa 3: Configure o manuseio de push

Você pode usar o SDK Swift para automatizar o processamento de notificações remotas recebidas do Braze. Esta é a maneira mais simples de lidar com notificações por push e é o método de manuseio recomendado.

{% tabs local %}
{% tab Automatic %}
#### Etapa 3.1: Ative a automação na propriedade de push

Para ativar a integração automática de push, defina a propriedade `automation` da configuração `push` para `true`:

{% subtabs %}
{% subtab Swift %}
```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-API-ENDPOINT}")
configuration.push.automation = true
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{YOUR-BRAZE-API-KEY}" endpoint:@"{YOUR-BRAZE-API-ENDPOINT}"];
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
```

{% endsubtab %}
{% endsubtabs %}

Isso instrui o SDK a:
- Registre seu aplicativo para notificação por push no sistema.
- Solicite a autorização/permissão de notificação por push na inicialização.
- Forneça dinamicamente implementações para os métodos delegados relacionados ao sistema de notificação por push.

{% alert note %}
Os passos de automação realizados pelo SDK são compatíveis com as integrações de manuseio de notificação por push pré-existentes em sua base de código. O SDK apenas automatiza o processamento da notificação remota recebida da Braze. Qualquer handler de sistema implementado para processar suas próprias notificações remotas ou de outro SDK de terceiros continuará a funcionar quando `automation` estiver ativado.
{% endalert %}

{% alert warning %}
O SDK deve ser inicializado na thread principal para ativar a automação de notificação por push. A inicialização do SDK deve ocorrer antes que o aplicativo tenha terminado de iniciar ou na sua implementação do AppDelegate [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application).
Se o seu aplicativo exigir uma configuração adicional antes de inicializar o SDK, consulte a página da documentação sobre [inicialização por postergação]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=swift).
{% endalert %}

#### Etapa 3.2: Substitua configurações individuais (opcional)

Para um controle mais granular, cada etapa de automação pode ser ativada ou desativada individualmente:

{% subtabs %}
{% subtab Swift %}

```swift
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = true
configuration.push.automation.requestAuthorizationAtLaunch = false
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
configuration.push.automation.requestAuthorizationAtLaunch = NO;
```

{% endsubtab %}
{% endsubtabs %}

Consulte [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) para todas as opções disponíveis e [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property) para saber mais sobre o comportamento da automação.
{% endtab %}

{% tab Manual %}
{% alert note %}
Se você depende de notificações por push para comportamento adicional específico do seu app, ainda poderá usar a integração automática de push em vez da integração manual de notificação por push. O método [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)) oferece uma forma de receber notificação sobre notificações remotas processadas pela Braze.
{% endalert %}

#### Etapa 3.1: Registre-se para notificações por push com APNs

Inclua o exemplo de código apropriado no método de delegado [`application:didFinishLaunchingWithOptions:` do seu app](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) para que os dispositivos dos seus usuários possam se registrar no APNs. Certifique-se de chamar todo o código de integração push na thread principal do seu aplicativo.

Braze também fornece categorias de push padrão para suporte ao botão de ação por push, que devem ser adicionadas manualmente ao seu código de registro de push. Consulte os [botões de ação por push]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories) para obter etapas adicionais de integração.

Adicione o seguinte código ao método `application:didFinishLaunchingWithOptions:` do seu delegado do app. 

{% alert note %}
O seguinte exemplo de código inclui integração para autenticação push provisória (linhas 5 e 6). Se você não planeja usar autorização provisória no seu app, pode remover as linhas de código que adicionam `UNAuthorizationOptionProvisional` às opções de `requestAuthorization`.<br>Visite [opções de notificação do iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) para saber mais sobre a autenticação provisória push.
{% endalert %}

{% subtabs %}
{% subtab Swift %}

```swift
application.registerForRemoteNotifications()
let center = UNUserNotificationCenter.current()
center.setNotificationCategories(Braze.Notifications.categories)
center.delegate = self
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
center.requestAuthorization(options: options) { granted, error in
  print("Notification authorization, granted: \(granted), error: \(String(describing: error))")
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
[application registerForRemoteNotifications];
UNUserNotificationCenter *center = UNUserNotificationCenter.currentNotificationCenter;
[center setNotificationCategories:BRZNotifications.categories];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
}
[center requestAuthorizationWithOptions:options
                      completionHandler:^(BOOL granted, NSError *_Nullable error) {
                        NSLog(@"Notification authorization, granted: %d, "
                              @"error: %@)",
                              granted, error);
}];
```

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
Você deve atribuir seu objeto delegado usando `center.delegate = self` de forma síncrona antes que seu app termine de iniciar, de preferência em `application:didFinishLaunchingWithOptions:`. Se não fizer isso, seu app pode perder notificações por push recebidas. Consulte a documentação da Apple [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) para saber mais.
{% endalert %}

#### Etapa 3.2: Registre push tokens com a Braze

Depois que o registro do APNs estiver completo, passe o `deviceToken` resultante para a Braze para ativar as notificações por push para o usuário.  

{% subtabs %}
{% subtab Swift %}

Adicione o seguinte código ao método `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` do seu app:

```swift
AppDelegate.braze?.notifications.register(deviceToken: deviceToken)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Adicione o seguinte código ao método `application:didRegisterForRemoteNotificationsWithDeviceToken:` do seu app:

```objc
[AppDelegate.braze.notifications registerDeviceToken:deviceToken];
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
O método delegado `application:didRegisterForRemoteNotificationsWithDeviceToken:` é chamado toda vez depois que `application.registerForRemoteNotifications()` é chamado. <br><br>Se você estiver migrando para o Braze de outro serviço de push e o dispositivo do seu usuário já estiver registrado no APNs, este método coletará tokens de registros existentes na próxima vez que o método for chamado, e os usuários não precisarão aceitar novamente o push.
{% endalert %}

#### Etapa 3.3: Ativar push handling

Em seguida, passe as notificações por push recebidas para a Braze. Esta etapa é necessária para registrar a análise de dados de push e o manuseio de links. Certifique-se de chamar todo o código de integração push na thread principal do seu aplicativo.

##### Manipulação padrão de push

{% subtabs %}
{% subtab Swift %}
Para ativar o manuseio padrão de push do Braze, adicione o seguinte código ao método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` do seu app:

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

Em seguida, adicione o seguinte ao método `userNotificationCenter(_:didReceive:withCompletionHandler:)` do seu app:

```swift
if let braze = AppDelegate.braze, braze.notifications.handleUserNotification(
  response: response,
  withCompletionHandler: completionHandler
) {
  return
}
completionHandler()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
Para ativar o manuseio padrão de push do Braze, adicione o seguinte código ao método `application:didReceiveRemoteNotification:fetchCompletionHandler:` do seu aplicativo:

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleBackgroundNotificationWithUserInfo:userInfo
                                                                                                       fetchCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler(UIBackgroundFetchResultNoData);
```

Em seguida, adicione o seguinte código ao método `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` do seu app:

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                                                                                  withCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler();
```
{% endsubtab %}
{% endsubtabs %}

##### Manipulação de push em primeiro plano

{% subtabs %}
{% subtab Swift %}
Para ativar notificações por push em primeiro plano e permitir que a Braze as reconheça quando forem recebidas, implemente `UNUserNotificationCenter.userNotificationCenter(_:willPresent:withCompletionHandler:)`. Se um usuário tocar na sua notificação em primeiro plano, o `userNotificationCenter(_:didReceive:withCompletionHandler:)` push delegate será chamado e a Braze registrará o evento de clique no push.

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter,
  willPresent notification: UNNotification,
  withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions
) -> Void) {
  if let braze = AppDelegate.braze {
    // Forward notification payload to Braze for processing.
    braze.notifications.handleForegroundNotification(notification: notification)
  }

  // Configure application's foreground notification display options.
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner])
  } else {
    completionHandler([.alert])
  }
}
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
Para ativar notificações por push em primeiro plano e permitir que a Braze as reconheça quando forem recebidas, implemente `userNotificationCenter:willPresentNotification:withCompletionHandler:`. Se um usuário tocar na sua notificação em primeiro plano, o `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` push delegate será chamado e a Braze registrará o evento de clique no push.

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (AppDelegate.braze != nil) {
    // Forward notification payload to Braze for processing.
    [AppDelegate.braze.notifications handleForegroundNotificationWithNotification:notification];
  }

  // Configure application's foreground notification display options.
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Testando notificações {#push-testing}

Se você quiser testar notificações no app e notificações por push via a linha de comando, você pode enviar uma única notificação através do terminal via CURL e a [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Você precisará substituir os seguintes campos pelos valores corretos para o seu caso de teste:

- `YOUR_API_KEY` - disponível em **Configurações** > **Chaves de API**.
- `YOUR_EXTERNAL_USER_ID` - disponível na página **Pesquisar Usuários**. Para saber mais, consulte [atribuir IDs de usuário]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id).
- `YOUR_KEY1` (opcional)
- `YOUR_VALUE1` (opcional)

No exemplo a seguir, a instância`US-01` está sendo usada. Se você não estiver nessa instância, consulte nossa [documentação da API]({{site.baseurl}}/api/basics/) para ver em qual endpoint fazer solicitações.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

## Assinando atualizações de notificações por push

Para acessar as cargas úteis de notificação por push processadas pela Braze, use o método [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)/).

Você pode usar o parâmetro `payloadTypes` para especificar se deseja se inscrever em notificações envolvendo eventos de push abertos, eventos de push recebidos ou ambos.

{% tabs %}
{% tab Swift %}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.notifications.subscribeToUpdates(payloadTypes: [.open, .received]) { payload in
  print("Braze processed notification with title '\(payload.title)' and body '\(payload.body)'")
}
```

{% alert important %}
Lembre-se de que os eventos recebidos de push só dispararão para notificações em primeiro plano e notificações `content-available` em segundo plano. Não disparará para notificações recebidas enquanto encerrado ou para notificações em segundo plano sem o campo `content-available`.
{% endalert %}

{% endtab %}

{% tab OBJECTIVE-C %}

```objc
NSInteger filtersValue = BRZNotificationsPayloadTypeFilter.opened.rawValue | BRZNotificationsPayloadTypeFilter.received.rawValue;
BRZNotificationsPayloadTypeFilter *filters = [[BRZNotificationsPayloadTypeFilter alloc] initWithRawValue: filtersValue];
BRZCancellable *cancellable = [notifications subscribeToUpdatesWithPayloadTypes:filters update:^(BRZNotificationsPayload * _Nonnull payload) {
  NSLog(@"Braze processed notification with title '%@' and body '%@'", payload.title, payload.body);
}];
```

{% alert important %}
Lembre-se de que os eventos recebidos de push só dispararão para notificações em primeiro plano e notificações `content-available` em segundo plano. Não disparará para notificações recebidas enquanto encerrado ou para notificações em segundo plano sem o campo `content-available`.
{% endalert %}

{% endtab %}

{% endtabs %}
{% alert note %}
Ao usar a integração automática de push, `subscribeToUpdates(_:)` é a única maneira de ser notificado sobre notificações remotas processadas pelo Braze. Os métodos de sistema `UIAppDelegate` e `UNUserNotificationCenterDelegate` não são chamados quando a notificação é processada automaticamente pela Braze.
{% endalert %}

{% alert tip %}
Crie sua inscrição de notificação por push em `application(_:didFinishLaunchingWithOptions:)` para garantir que sua inscrição seja disparada depois que um usuário final tocar em uma notificação enquanto seu app estiver em um estado finalizado.
{% endalert %}

## Manuseio de notificações em primeiro plano

Por padrão, quando uma notificação por push chega enquanto seu app está em primeiro plano, o iOS não a exibe automaticamente. Para exibir notificações por push em primeiro plano e rastreá-las com a análise do Braze, chame o método `handleForegroundNotification(notification:)` dentro da sua implementação `UNUserNotificationCenterDelegate.userNotificationCenter(_:willPresent:withCompletionHandler:)`.

### Como funciona?

Quando você chama `handleForegroundNotification(notification:)`, o Braze processa a carga útil da notificação para registrar análises e lidar com quaisquer links profundos ou ações de botão. O comportamento real de exibição é controlado pelo `UNNotificationPresentationOptions` que você passa para o manipulador de conclusão.

```swift
import BrazeKit
import UserNotifications

extension AppDelegate: UNUserNotificationCenterDelegate {
  func userNotificationCenter(
    _ center: UNUserNotificationCenter,
    willPresent notification: UNNotification,
    withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void
  ) {
    // Let Braze process the notification payload
    if let braze = AppDelegate.braze {
      braze.notifications.handleForegroundNotification(notification: notification)
    }
    
    // Control how the notification appears in the foreground
    if #available(iOS 14.0, *) {
      completionHandler([.banner, .list, .sound])
    } else {
      completionHandler([.alert, .sound])
    }
  }
}
```

Para um exemplo completo, veja o [exemplo de integração manual de notificações por push](https://github.com/braze-inc/braze-swift-sdk/blob/e31907eaa0dbd151dc2e6826de66cc494242ba60/Examples/Swift/Sources/PushNotifications-Manual/AppDelegate.swift#L1-L120) no repositório do SDK Swift do Braze.

## Push primers {#push-primers}

Campanhas de push primer incentivam seus usuários a ativar notificações por push em seu dispositivo para seu app. Isso pode ser feito sem personalização de SDK usando nosso [Push Primer sem código]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Gerenciamento dinâmico de gateway APNs

O gerenciamento dinâmico do Serviço de Notificações por Push da Apple (APNs) melhora a confiabilidade e eficiência das notificações por push do iOS, detectando automaticamente o ambiente APNs correto. Anteriormente, você selecionava manualmente os ambientes APNs (desenvolvimento ou produção) para suas notificações por push, o que às vezes levava a configurações de gateway incorretas, falhas na entrega e erros de `BadDeviceToken`.

Com a gestão dinâmica de gateway APNs, você terá:

- **Confiabilidade aprimorada:** As notificações são sempre entregues ao ambiente APNs correto, reduzindo as entregas falhadas.
- **Configuração simplificada:** Você não precisa mais gerenciar manualmente as configurações do gateway APNs.
- **Resiliência a erros:** Valores de gateway inválidos ou ausentes são tratados de forma elegante, proporcionando um serviço ininterrupto.

### Pré-requisitos

A Braze suporta a gestão dinâmica de gateway APNs para notificações por push no iOS com o seguinte requisito de versão do SDK:

{% sdk_min_versions swift:10.0.0 %}

### Como funciona?

Quando um app iOS se integra ao SDK Swift da Braze, ele envia dados relacionados ao dispositivo, incluindo [`aps-environment`](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment) para a API do SDK da Braze, se disponível. O valor `apns_gateway` indica se o app está usando o ambiente APNs de desenvolvimento (`dev`) ou produção (`prod`).

A Braze também armazena o valor de gateway reportado para cada dispositivo. Se um novo valor de gateway válido for recebido, a Braze atualiza automaticamente o valor armazenado.

Quando a Braze envia uma notificação por push:

- Se um valor de gateway válido (dev ou prod) estiver armazenado para o dispositivo, a Braze o utiliza para determinar o ambiente APNs correto.
- Se nenhum valor de gateway estiver armazenado, a Braze usa como padrão o ambiente APNs configurado na página **Configurações do App**.

### Perguntas frequentes

#### Por que esse recurso foi introduzido?

Com a gestão dinâmica de gateway APNs, o ambiente correto é selecionado automaticamente. Anteriormente, você tinha que configurar manualmente o gateway APNs, o que poderia levar a erros de `BadDeviceToken`, invalidação de token e potenciais problemas de limitação de taxa do APNs.

#### Como isso impacta o desempenho da entrega de push?

Este recurso melhora as taxas de entrega, sempre roteando os tokens de push para o ambiente APNs correto, evitando falhas causadas por gateways mal configurados.

#### Posso desativar este recurso?

A Gestão Dinâmica de Gateway APNs está ativada por padrão e oferece melhorias de confiabilidade. Se você tiver casos de uso específicos que exigem seleção manual de gateway, entre em contato com [suporte da Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support/).
