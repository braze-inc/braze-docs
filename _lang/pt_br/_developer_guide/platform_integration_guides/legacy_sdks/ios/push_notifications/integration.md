---
nav_title: Integração
article_title: Integração push para iOS
platform: iOS
page_order: 0
description: "Este artigo de referência aborda como integrar notificações por push em seu aplicativo iOS."
channel:
  - push
search_rank: 5

local_redirect:
  ios-10-rich-notifications: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/'
local_redirect:
  creating-a-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-service-extension'
local_redirect:
  setting-up-the-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#setting-up-the-service-extension'
local_redirect:
  creating-a-rich-notification-in-your-dashboard: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-rich-notification-in-your-dashboard'
local_redirect:
  push-action-buttons-integration: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/'
local_redirect:
  step-1-adding-braze-default-push-categories: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-1-adding-braze-default-push-categories'
local_redirect:
  step-2-enable-interactive-push-handling: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-2-enable-interactive-push-handling'
  
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integração push

## Etapa 1: Configurar notificações por push

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

## Etapa 2: Ativar os recursos de push

Nas configurações do projeto, certifique-se de que, na guia **Recursos**, o recurso de **notificações por push** esteja ativado.

![]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

Se tiver certificados push de desenvolvimento e produção separados, desmarque a caixa **Gerenciar automaticamente o login** na guia **Geral**. Isso permitirá que você escolha diferentes perfis de provisionamento para cada configuração de compilação, pois o recurso de assinatura automática de código do Xcode só faz a assinatura de desenvolvimento.

![Configurações do projeto do Xcode mostrando a guia "General" (Geral). Nessa guia, a opção "Gerenciar assinatura automaticamente" está desmarcada.]({% image_buster /assets/img_archive/xcode8_auto_signing.png %})

## Etapa 3: Registre-se para receber notificações por push

O exemplo de código apropriado deve ser incluído no método delegado `application:didFinishLaunchingWithOptions:` do seu app para que o dispositivo dos seus usuários se registre com APNs. Chame todo o código de integração push na thread principal do app.

Braze também fornece categorias de push padrão para suporte ao botão de ação por push, que devem ser adicionadas manualmente ao seu código de registro de push. Consulte os [botões de ação por push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/) para obter etapas adicionais de integração.

{% alert warning %}
Se você implementou um prompt de push personalizado, conforme descrito em nossas [práticas recomendadas de push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/troubleshooting/), certifique-se de chamar o seguinte código **toda vez que o aplicativo for executado** após a concessão de permissões de push ao seu aplicativo. **Os apps precisam se registrar novamente no APNs, pois [os tokens de dispositivos podem mudar arbitrariamente](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html).**
{% endalert %}

### Usando a estrutura UserNotification (iOS 10+)

Se estiver usando o framework `UserNotifications` (recomendado) lançado no iOS 10, adicione o seguinte código ao método `application:didFinishLaunchingWithOptions:` do delegado do seu app.

{% alert important %}
O seguinte exemplo de código inclui integração para autenticação push provisória (linhas 5 e 6). Se você não planeja usar autorização provisória no seu app, pode remover as linhas de código que adicionam `UNAuthorizationOptionProvisional` às opções de `requestAuthorization`.<br>Visite [opções de notificação do iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) para saber mais sobre a autenticação provisória push.
{% endalert %}

{% tabs %}
{% tab OBJECTIVE C %}

```objc
if (floor(NSFoundationVersionNumber) > NSFoundationVersionNumber_iOS_9_x_Max) {
  UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
  center.delegate = self;
  UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
  }
  [center requestAuthorizationWithOptions:options
                        completionHandler:^(BOOL granted, NSError * _Nullable error) {
                          [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
} else {
  UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
  [[UIApplication sharedApplication] registerUserNotificationSettings:settings];
}
```

{% endtab %}
{% tab swift %}

```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.delegate = self as? UNUserNotificationCenterDelegate
  var options: UNAuthorizationOptions = [.alert, .sound, .badge]
  if #available(iOS 12.0, *) {
    options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
  }
  center.requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()
} else {
  let types : UIUserNotificationType = [.alert, .badge, .sound]
  let setting : UIUserNotificationSettings = UIUserNotificationSettings(types:types, categories:nil)
  UIApplication.shared.registerUserNotificationSettings(setting)
  UIApplication.shared.registerForRemoteNotifications()
}
```

{% endtab %}
{% endtabs %}


{% alert warning %}
Você deve atribuir seu objeto delegado usando `center.delegate = self` de forma síncrona antes que seu app termine de iniciar, de preferência em `application:didFinishLaunchingWithOptions:`. Se não fizer isso, seu app pode perder notificações por push recebidas. Consulte a documentação da Apple [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) para saber mais.
{% endalert %}

### Sem a estrutura UserNotifications

Se não estiver usando o framework `UserNotifications`, adicione o seguinte código ao método `application:didFinishLaunchingWithOptions:` do delegado do seu app:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
[[UIApplication sharedApplication] registerForRemoteNotifications];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
let types : UIUserNotificationType = UIUserNotificationType.Badge | UIUserNotificationType.Sound | UIUserNotificationType.Alert
var setting : UIUserNotificationSettings = UIUserNotificationSettings(forTypes: types, categories: nil)
UIApplication.shared.registerUserNotificationSettings(setting)
UIApplication.shared.registerForRemoteNotifications()
```

{% endtab %}
{% endtabs %}


## Etapa 4: Registrar tokens por push na Braze

Quando o registro de APNs estiver concluído, o método a seguir deverá ser alterado para passar o `deviceToken` resultante para o Braze, de modo que o usuário fique capacitado para notificações por push:

{% tabs %}
{% tab OBJECTIVE C %}

Adicione o seguinte código ao seu método `application:didRegisterForRemoteNotificationsWithDeviceToken:`:

```objc
[[Appboy sharedInstance] registerDeviceToken:deviceToken];
```

{% endtab %}
{% tab swift %}

Adicione o seguinte código ao método `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` do seu app:

```swift
Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
```

{% endtab %}
{% endtabs %}

{% alert important %}
O método delegado `application:didRegisterForRemoteNotificationsWithDeviceToken:` é chamado toda vez depois que `[[UIApplication sharedApplication] registerForRemoteNotifications]` é chamado. Se você estiver migrando para o Braze de outro serviço de push e o dispositivo do seu usuário já estiver registrado no APNs, este método coletará tokens de registros existentes na próxima vez que o método for chamado, e os usuários não precisarão aceitar novamente o push.
{% endalert %}

## Etapa 5: Ativar push handling

O código a seguir passa as notificações por push recebidas para o Braze e é necessário para o registro da análise por push e o tratamento de links. Certifique-se de chamar todo o código de integração push na thread principal do seu aplicativo.

### iOS 10+

Ao desenvolver para iOS 10 ou posteriores, recomendamos integrar o framework `UserNotifications` e fazer o seguinte:

{% tabs %}
{% tab OBJECTIVE C %}

Adicione o seguinte código ao método `application:didReceiveRemoteNotification:fetchCompletionHandler:` do seu aplicativo:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

Em seguida, adicione o seguinte código ao método `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` do seu app:

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                 didReceiveNotificationResponse:response
                          withCompletionHandler:completionHandler];
```

**Push handling em primeiro plano**

Para exibir uma notificação por push enquanto o app estiver em primeiro plano, implemente `userNotificationCenter:willPresentNotification:withCompletionHandler:`:

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```

Se a notificação em primeiro plano for clicada, o delegado de push do iOS 10 `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` será chamado, e a Braze registrará um evento de clique de push.

{% endtab %}
{% tab swift %}

Adicione o seguinte código ao método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` do seu app:

```swift
Appboy.sharedInstance()?.register(application,
                                            didReceiveRemoteNotification: userInfo,
                                            fetchCompletionHandler: completionHandler)
```

Em seguida, adicione o seguinte código ao método `userNotificationCenter(_:didReceive:withCompletionHandler:)` do seu app:

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                               didReceive: response,
                                               withCompletionHandler: completionHandler)
```

**Push handling em primeiro plano**

Para exibir uma notificação por push enquanto o app estiver em primeiro plano, implemente `userNotificationCenter(_:willPresent:withCompletionHandler:)`:

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter,
                              willPresent notification: UNNotification,
                              withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner]);
  } else {
    completionHandler([.alert]);
  }
}
```

Se a notificação em primeiro plano for clicada, o delegado de push do iOS 10 `userNotificationCenter(_:didReceive:withCompletionHandler:)` será chamado, e a Braze registrará um evento de clique de push.

{% endtab %}
{% endtabs %}

### Pré-iOS 10

O iOS 10 atualizou o comportamento de modo que não chama mais `application:didReceiveRemoteNotification:fetchCompletionHandler:` quando um push é clicado. Por isso, se você não atualizar o desenvolvimento para o iOS 10 e posteriores e usar o framework `UserNotifications`, terá que chamar a Braze a partir de ambos os delegados de estilo antigo, que é uma ruptura com a nossa integração anterior.

Para apps desenvolvidos com SDKs anteriores ao iOS 10, use as seguintes instruções:

{% tabs %}
{% tab OBJECTIVE C %}

Para ativar o rastreamento de abertura nas notificações por push, adicione o seguinte código ao método `application:didReceiveRemoteNotification:fetchCompletionHandler:` do seu app:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

Para atender à análise de dados por push no iOS 10, você também deve adicionar o seguinte código ao método delegado `application:didReceiveRemoteNotification:` do seu app:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo];
```

{% endtab %}
{% tab swift %}

Para ativar o rastreamento de abertura nas notificações por push, adicione o seguinte código ao método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` do seu app:

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo,
  fetchCompletionHandler: completionHandler)
```

Para atender à análise de dados por push no iOS 10, você também deve adicionar o seguinte código ao método delegado `application(_:didReceiveRemoteNotification:)` do seu app:

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo)
```

{% endtab %}
{% endtabs %}

## Etapa 6: Deep linking

Deep linking de um push para o app é automaticamente tratado por meio da nossa documentação padrão de integração de push. Se quiser saber mais sobre como adicionar deep links a locais específicos em seu app, consulte nossos [casos de uso avançados]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-implementation).

## Etapa 7: Testes de unidade (opcional)

Para adicionar cobertura de teste para as etapas de integração que você acabou de seguir, implemente [testes unitários push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/unit_tests/).

