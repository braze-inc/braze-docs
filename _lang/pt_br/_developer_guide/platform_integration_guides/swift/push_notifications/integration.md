---
nav_title: Integração
article_title: push Integração para iOS
platform: Swift
page_order: 0
description: "Este artigo de referência explica como configurar notificações por push no SDK da Braze para Swift para iOS."
channel:
  - push
  
---

# integração de notificações por push

> Este artigo de referência explica como configurar notificações por push no Swift SDK da Braze para iOS.

[Notificações por push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/) permitem que você envie notificações do seu app quando eventos importantes ocorrerem. Você pode enviar uma notificação por push quando tiver novas mensagens instantâneas para entregar, alertas de notícias de última hora para enviar ou o episódio mais recente do programa de TV favorito do seu usuário pronto para ele baixar para visualização offline. Notificações por push também podem ser [silenciosas]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/), sendo usadas apenas para atualizar a interface do seu app ou disparar trabalho em segundo plano. 

As notificações por push também podem ser muito mais eficientes do que a busca em segundo plano, pois seu aplicativo só é iniciado quando necessário. As notificações por push também podem ser muito mais eficientes do que a busca em segundo plano, pois seu aplicativo só é iniciado quando necessário. 

As notificações por push são limitadas por taxa, então não tenha medo de enviar quantas sua aplicação precisar. O iOS e o serviço de Notificações por Push da Apple (APNs) controlarão a frequência com que são entregues, e você não terá problemas por enviar muitas. Se suas notificações por push forem limitadas, elas podem ser atrasadas até a próxima vez que o dispositivo enviar um pacote keep-alive ou receber outra notificação.

## Configuração inicial

### Etapa 1: Faça upload do seu certificado APNs

Antes de poder enviar uma notificação por push iOS usando a Braze, você precisa fornecer seu `.p8` arquivo de notificação por push fornecido pela Apple. Conforme descrito na documentação [do desenvolvedor](https://developer.apple.com/documentation/usernotifications) da Apple:

1. Em sua conta de desenvolvedor Apple, acessar [**Certificados, Identificadores e Perfis**](https://developer.apple.com/account/ios/certificate).
2. Em **Chaves**, selecione **Todos** e clique no botão adicionar (+) no canto superior direito.
3. Em **Descrição da Chave**, insira um nome único para a chave de assinatura.
4. Em **Serviços Principais**, selecione a caixa de seleção **serviço de Notificações por Push da Apple (APNs)**, depois clique em **Continuar**. Clique **Confirmar**.
5. Note o ID da chave. Clique em **baixar** para gerar e baixar a chave. Certifique-se de salvar o arquivo baixado em um local seguro, pois você não pode baixar isso mais de uma vez.
6. Na Braze, acesse **Configurações** > **Configurações do app** e faça upload do arquivo `.p8` em **Certificado de push da Apple**. Você pode fazer upload do seu certificado de push de desenvolvimento ou de produção. Para testar notificações por push depois que seu app estiver disponível na App Store, é recomendável configurar um espaço de trabalho separado para a versão de desenvolvimento do seu app.
7. Quando solicitado, informe o [ID do pacote](https://developer.apple.com/documentation/foundation/nsbundle/1418023-bundleidentifier), o [ID da chave](https://developer.apple.com/help/account/manage-keys/get-a-key-identifier/) e o [ID da equipe](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id) e clique em **Salvar**.

{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), você pode fazer upload do seu `.p8` arquivo de **Gerenciar Configurações** > **Configurações**.
{% endalert %}

### Etapa 2: Ativar push capabilities

No Xcode, acesse a seção **Signing & Capabilities** do direcionamento do app principal e adicione o recurso de notificações por push.

![A seção "Signing & Capabilities" (Assinatura e recursos) em um projeto Xcode.]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

## Integração automática de push

O SDK SWIFT fornece uma abordagem apenas de configuração para automatizar o processamento de notificações remotas recebidas da Braze. Esta abordagem é a maneira mais simples de integrar notificações por push e é recomendada para a maioria dos clientes.

Para ativar a integração automática de push, defina a propriedade `automation` da configuração `push` para `true`:

{% tabs %}
{% tab Swift %}
```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-API-ENDPOINT}")
configuration.push.automation = true
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{YOUR-BRAZE-API-KEY}" endpoint:@"{YOUR-BRAZE-API-ENDPOINT}"];
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
```

{% endtab %}
{% endtabs %}

Isso instrui o SDK a:
- Registre seu aplicativo para notificação por push no sistema.
- Solicite a autorização/permissão de notificação por push na inicialização.
- Forneça dinamicamente implementações para os métodos delegados relacionados ao sistema de notificação por push.

{% alert note %}
Os passos de automação realizados pelo SDK são compatíveis com as integrações de manuseio de notificação por push pré-existentes em sua base de código. O SDK apenas automatiza o processamento da notificação remota recebida da Braze. Qualquer handler de sistema implementado para processar suas próprias notificações remotas ou de outro SDK de terceiros continuará a funcionar quando `automation` estiver ativado.
{% endalert %}

{% alert warning %}
O SDK deve ser inicializado na thread principal para ativar a automação de notificação por push. A inicialização do SDK deve ocorrer antes que o aplicativo tenha terminado de iniciar ou na sua implementação do AppDelegate [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application).
Se o seu aplicativo exigir uma configuração adicional antes de inicializar o SDK, consulte a página da documentação sobre [inicialização por postergação]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/delayed_initialization/).
{% endalert %}

### Substituindo configurações individuais

Para um controle mais granular, cada etapa de automação pode ser ativada ou desativada individualmente:

{% tabs %}
{% tab Swift %}

```swift
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = true
configuration.push.automation.requestAuthorizationAtLaunch = false
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
configuration.push.automation.requestAuthorizationAtLaunch = NO;
```

{% endtab %}
{% endtabs %}

Consulte [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) para todas as opções disponíveis e [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property) para saber mais sobre o comportamento da automação.

Você pode pular a próxima seção e continuar para [deep linking](#deep-linking) se estiver usando a integração automática de push.

## Integração manual de push

As notificações por push também podem ser integradas manualmente. Esta seção descreve os passos necessários para esta integração. 

{% alert note %}
Se você depende de notificações por push para comportamento adicional específico do seu app, ainda poderá usar a integração automática de push em vez da integração manual de notificação por push. O método [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)) oferece uma forma de receber notificação sobre notificações remotas processadas pela Braze.
{% endalert %}

### Etapa 1: Registre-se para notificações por push com APNs

Inclua o exemplo de código apropriado no método de delegado [`application:didFinishLaunchingWithOptions:` do seu app](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) para que os dispositivos dos seus usuários possam se registrar no APNs. Certifique-se de chamar todo o código de integração push na thread principal do seu aplicativo.

Braze também fornece categorias de push padrão para suporte ao botão de ação por push, que devem ser adicionadas manualmente ao seu código de registro de push. Consulte os [botões de ação por push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/action_buttons/) para obter etapas adicionais de integração.

Adicione o seguinte código ao método `application:didFinishLaunchingWithOptions:` do seu delegado do app. 

{% alert note %}
O seguinte exemplo de código inclui integração para autenticação push provisória (linhas 5 e 6). Se você não planeja usar autorização provisória no seu app, pode remover as linhas de código que adicionam `UNAuthorizationOptionProvisional` às opções de `requestAuthorization`.<br>Visite [opções de notificação do iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) para saber mais sobre a autenticação provisória push.
{% endalert %}

{% tabs %}
{% tab Swift %}

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

{% endtab %}
{% tab OBJECTIVE C %}

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

{% endtab %}
{% endtabs %}

{% alert warning %}
Você deve atribuir seu objeto delegado usando `center.delegate = self` de forma síncrona antes que seu app termine de iniciar, de preferência em `application:didFinishLaunchingWithOptions:`. Se não fizer isso, seu app pode perder notificações por push recebidas. Consulte a documentação da Apple [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) para saber mais.
{% endalert %}

### Etapa 2: Registre push tokens com a Braze

Depois que o registro do APNs estiver completo, passe o `deviceToken` resultante para a Braze para ativar as notificações por push para o usuário.  

{% tabs %}
{% tab SWIFT %}

Adicione o seguinte código ao método `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` do seu app:

```swift
AppDelegate.braze?.notifications.register(deviceToken: deviceToken)
```

{% endtab %}
{% tab OBJECTIVE C %}

Adicione o seguinte código ao método `application:didRegisterForRemoteNotificationsWithDeviceToken:` do seu app:

```objc
[AppDelegate.braze.notifications registerDeviceToken:deviceToken];
```

{% endtab %}
{% endtabs %}

{% alert important %}
O método delegado `application:didRegisterForRemoteNotificationsWithDeviceToken:` é chamado toda vez depois que `application.registerForRemoteNotifications()` é chamado. <br><br>Se você estiver migrando para o Braze de outro serviço de push e o dispositivo do seu usuário já estiver registrado no APNs, este método coletará tokens de registros existentes na próxima vez que o método for chamado, e os usuários não precisarão aceitar novamente o push.
{% endalert %}

### Etapa 3: Ativar push handling

Em seguida, passe as notificações por push recebidas para a Braze. Esta etapa é necessária para registrar a análise de dados de push e o manuseio de links. Certifique-se de chamar todo o código de integração push na thread principal do seu aplicativo.

#### Manipulação padrão de push

{% tabs %}
{% tab SWIFT %}
Para ativar o tratamento de push padrão da Braze, adicione o seguinte código ao método do seu app `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`:

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
{% endtab %}

{% tab OBJECTIVE C %}
Para ativar o gerenciamento de push padrão da Braze, adicione o seguinte código ao método da sua aplicação `application:didReceiveRemoteNotification:fetchCompletionHandler:`:

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
{% endtab %}
{% endtabs %}

#### Manipulação de push em primeiro plano

{% tabs %}
{% tab SWIFT %}
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
{% endtab %}

{% tab OBJECTIVE C %}
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
{% endtab %}
{% endtabs %}

## Deep linking

Deep linking de um push para o app é automaticamente tratado por meio da nossa documentação padrão de integração de push. Se você quiser saber mais sobre como adicionar links profundos a locais específicos no seu app, veja nossos [casos de uso avançados]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-implementation).

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

{% tab OBJECTIVE C %}

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

## Testando {#push-testing}

Se você quiser testar notificações no app e notificações por push via a linha de comando, você pode enviar uma única notificação através do terminal via CURL e a [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Você precisará substituir os seguintes campos pelos valores corretos para o seu caso de teste:

- `YOUR_API_KEY` - disponível em **Configurações** > **Chaves de API**.
- `YOUR_EXTERNAL_USER_ID` - disponível na página **Pesquisar Usuários**. Para saber mais, consulte [atribuir IDs de usuário]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id).
- `YOUR_KEY1` (opcional)
- `YOUR_VALUE1` (opcional)

{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), essas páginas estão em um local diferente: <br>- **Chaves de API** está localizado em **Console de desenvolvedor** > **Configurações de API** <br>**Pesquisar Usuários** está localizado em **Usuários** > **Pesquisa de Usuários**
{% endalert %}

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

## Push primers {#push-primers}

Campanhas de push primer incentivam seus usuários a ativar notificações por push em seu dispositivo para seu app. Isso pode ser feito sem personalização de SDK usando nosso [Push Primer sem código]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/).

