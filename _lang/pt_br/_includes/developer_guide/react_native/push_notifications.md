{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Configurando notificações por push {#setting-up-push-notifications}

### Etapa 1: Concluir a configuração inicial

{% tabs local %}
{% tab Expo %}
#### Pré-requisitos

Antes de usar o Expo para notificações por push, você precisará [configurar o plugin Braze Expo]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/sdk_integration/?tab=expo).

#### Etapa 1.1: Atualize seu arquivo `app.json`

Em seguida, atualize seu arquivo `app.json` para Android e iOS:

- **Android:** Adicione a opção `enableFirebaseCloudMessaging`.
- **iOS:** Adicione a opção `enableBrazeIosPush`.

#### Etapa 1.2: Adicione seu ID de remetente do Google

Primeiro, acesse o Firebase Console, abra seu projeto e selecione <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **Project settings**.

![O projeto Firebase com o menu "Settings" aberto.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Selecione **Cloud Messaging** e, em seguida, em **Firebase Cloud Messaging API (V1)**, copie o **Sender ID** para a área de transferência.

![A página "Cloud Messaging" do projeto Firebase com o "Sender ID" destacado.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

Em seguida, abra o arquivo `app.json` do seu projeto e defina a propriedade `firebaseCloudMessagingSenderId` como o ID do remetente na área de transferência. Por exemplo:

```
"firebaseCloudMessagingSenderId": "693679403398"
```

#### Etapa 1.3: Adicione o caminho para o JSON do Google Services

No arquivo `app.json` do seu projeto, adicione o caminho para o arquivo `google-services.json`. Esse arquivo é necessário ao definir `enableFirebaseCloudMessaging: true` na sua configuração.

```json
{
  "expo": {
    "android": {
      "googleServicesFile": "PATH_TO_GOOGLE_SERVICES"
    },
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "enableBrazeIosPush": true,
          "enableFirebaseCloudMessaging": true,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true
        }
      ],
    ]
  }
}
```

Note que será necessário usar essas configurações em vez das instruções de configuração nativas se estiver dependendo de bibliotecas adicionais de notificação por push, como a [Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/).
{% endtab %}

{% tab Android Native %}
Se você não estiver usando o plugin Braze Expo, ou se preferir definir essas configurações nativamente, registre-se para push consultando o [guia de integração nativa para push no Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/).
{% endtab %}

{% tab iOS Native %}
Se você não estiver usando o plugin Braze Expo, ou se preferir definir essas configurações nativamente, registre-se para push consultando as etapas a seguir do [guia de integração nativa para push no iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift):

#### Etapa 1.1: Solicitação de permissões para push

Se você não planeja solicitar permissões para push quando o app for iniciado, omita a chamada `requestAuthorizationWithOptions:completionHandler:` no seu AppDelegate. Então, pule para a [Etapa 2](#reactnative_step-2-request-push-notifications-permission). Caso contrário, siga o [guia de integração nativa do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

#### Etapa 1.2 (Opcional): Migre sua chave push

Se estava usando anteriormente o `expo-notifications` para gerenciar sua chave push, execute `expo fetch:ios:certs` na pasta raiz do seu aplicativo. Isso vai baixar sua chave push (um arquivo .p8), que poderá então ser enviada para o dashboard da Braze.
{% endtab %}
{% endtabs %}

### Etapa 2: Solicitar permissão para notificações por push

Use o método `Braze.requestPushPermission()` (disponível na versão v1.38.0 e superior) para solicitar permissão para notificações por push do usuário no iOS e no Android 13+. Para o Android 12 e versões anteriores, esse método não tem efeito.

Esse método recebe um parâmetro obrigatório que especifica quais permissões o SDK deve solicitar do usuário no iOS. Essas opções não têm efeito no Android.

```javascript
const permissionOptions = {
  alert: true,
  sound: true,
  badge: true,
  provisional: false
};

Braze.requestPushPermission(permissionOptions);
```

#### Etapa 2.1: Ouça as notificações por push (opcional)

Além disso, você pode se inscrever em eventos em que a Braze detectou e tratou uma notificação por push recebida. Use a chave do listener `Braze.Events.PUSH_NOTIFICATION_EVENT`.

{% alert important %}
Os eventos de push recebidos no iOS só serão disparados para notificações em primeiro plano e notificações em segundo plano com `content-available`. Não serão disparados para notificações recebidas enquanto o app estiver encerrado ou para notificações em segundo plano sem o campo `content-available`.
{% endalert %}

```javascript
Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, data => {
  console.log(`Push Notification event of type ${data.payload_type} seen. Title ${data.title}\n and deeplink ${data.url}`);
  console.log(JSON.stringify(data, undefined, 2));
});
```

##### Campos de eventos de notificação por push

Para obter uma lista completa dos campos de notificação por push, consulte a tabela abaixo:

| Nome do campo         | Tipo      | Descrição |
| ------------------ | --------- | ----------- |
| `payload_type`     | String    | Especifica o tipo de carga útil da notificação. Os dois valores enviados pelo SDK da Braze para React Native são `push_opened` e `push_received`. |
| `url`              | String    | Especifica a URL que foi aberta pela notificação. |
| `use_webview`      | booleano   | Se for `true`, a URL será aberta no app em uma webview modal. Se `false`, a URL será aberta no navegador do dispositivo. |
| `title`            | String    | Representa o título da notificação. |
| `body`             | String    | Representa o corpo ou o texto do conteúdo da notificação. |
| `summary_text`     | String    | Representa o texto resumido da notificação. Isso é mapeado a partir de `subtitle` no iOS. |
| `badge_count`      | Número   | Representa a contagem de emblemas da notificação. |
| `timestamp`        | Número | Representa a hora em que a carga útil foi recebida pelo aplicativo. |
| `is_silent`        | booleano   | Se `true`, a carga útil é recebida silenciosamente. Para detalhes sobre o envio de notificações por push silenciosas no Android, consulte [Notificações por push silenciosas no Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android). Para detalhes sobre o envio de notificações por push silenciosas no iOS, consulte [Notificações por push silenciosas no iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift). |
| `is_braze_internal`| booleano   | Será `true` se uma carga útil de notificação tiver sido enviada para um recurso interno do SDK, como sincronização de geofences, sincronização de Feature Flag ou rastreamento de desinstalação. A carga útil é recebida silenciosamente para o usuário. |
| `image_url`        | String    | Especifica a URL associada à imagem da notificação. |
| `braze_properties` | Objeto    | Representa as propriedades da Braze associadas à campanha (pares chave-valor). |
| `ios`              | Objeto    | Representa campos específicos do iOS. |
| `android`          | Objeto    | Representa campos específicos do Android. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapa 3: Ativar deep linking (opcional)

Para permitir que a Braze gerencie deep links dentro de componentes React quando uma notificação por push é clicada, primeiro implemente as etapas descritas na biblioteca [React Native Linking](https://reactnative.dev/docs/linking), ou com a solução de sua escolha. Em seguida, siga as etapas adicionais abaixo.

Para saber mais sobre o que são deep links, consulte nosso [artigo de perguntas frequentes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

{% tabs local %}
{% tab Android Native %}
Se você estiver usando o [plugin Braze Expo]({{site.baseurl}}/developer_guide/platforms/react_native/sdk_integration/?tab=expo#step-2-choose-a-setup-option), pode gerenciar deep links de notificações por push automaticamente definindo `androidHandlePushDeepLinksAutomatically` como `true` no seu `app.json`.

Para gerenciar deep links manualmente, consulte a documentação nativa do Android: [Adicionando deep links]({{site.baseurl}}/developer_guide/push_notifications/deep_linking).

#### Etapa 3.1: Armazene a carga útil da notificação por push ao iniciar o app

{% alert note %}
Isso é suportado a partir do SDK React Native 19.1.0.
{% endalert %}

Adicione `populateInitialPushPayloadFromIntent` ao método `onCreate()` da sua atividade principal. Isso deve ser chamado antes que o React Native inicialize para capturar os dados do Intent inicial. Por exemplo:

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
  BrazeReactUtils.populateInitialPushPayloadFromIntent(intent)
  super.onCreate(savedInstanceState)
}
```

#### Etapa 3.2: Gerencie deep links a partir de um estado fechado

Além dos cenários básicos tratados pelo [React Native Linking](https://reactnative.dev/docs/linking), implemente o método `Braze.getInitialPushPayload` e recupere o valor `url` para considerar deep links de notificações por push que abrem seu app quando ele não está em execução. Por exemplo:

```javascript
// Handles deep links when an app is launched from a hard close via push click.
Braze.getInitialPushPayload(pushPayload => {
  if (pushPayload) {
    console.log('Braze.getInitialPushPayload is ' + pushPayload);
    showToast('Initial URL is ' + pushPayload.url);
    handleOpenUrl({ pushPayload.url });
  }
});
```
{% alert note %}
Este método requer a configuração nativa da Etapa 3.1 para sua plataforma. Se você estiver usando o plugin Braze Expo, isso pode ser tratado automaticamente.
{% endalert %}

{% endtab %}
{% tab iOS Native %}

{% alert important %}
Para gerenciar deep links de notificações por push no iOS, você também deve configurar o tratamento de links na sua camada nativa do iOS.
{% endalert %}

Isso inclui registrar um esquema de URL personalizado e implementar um manipulador de URL no seu `AppDelegate`. Para instruções completas de configuração, consulte [Gerenciando deep links]({{site.baseurl}}/developer_guide/platforms/swift/in_app_messages/deep_linking/?tab=objective-c) na documentação nativa do iOS.
#### Etapa 3.1: Armazene a carga útil da notificação por push ao iniciar o app
{% alert note %}
Pule a etapa 3.1 se você estiver usando o plugin Braze Expo, pois essa funcionalidade é tratada automaticamente.
{% endalert %}

Para iOS, adicione `populateInitialPayloadFromLaunchOptions` ao método `didFinishLaunchingWithOptions` do seu AppDelegate. Por exemplo:

{% subtabs local %}
{% subtab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  // ... Perform regular React Native setup

  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  configuration.triggerMinimumTimeInterval = 1;
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  [self registerForPushNotifications];
  [[BrazeReactUtils sharedInstance] populateInitialPayloadFromLaunchOptions:launchOptions];

  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}
```
{% endsubtab %}
{% subtab Swift %}
```swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
) -> Bool {
  // ... Perform regular React Native setup

  let configuration = Braze.Configuration(apiKey: apiKey, endpoint: endpoint)
  configuration.triggerMinimumTimeInterval = 1
  configuration.logger.level = .info
  let braze = BrazeReactBridge.initBraze(configuration)
  AppDelegate.braze = braze
  registerForPushNotifications()
  BrazeReactUtils.shared().populateInitialPayload(fromLaunchOptions: launchOptions)

  return super.application(application, didFinishLaunchingWithOptions: launchOptions)
}
```
{% endsubtab %}
{% endsubtabs %}

#### Etapa 3.2: Gerencie deep links a partir de um estado fechado

Além dos cenários básicos tratados pelo [React Native Linking](https://reactnative.dev/docs/linking), implemente o método `Braze.getInitialPushPayload` e recupere o valor `url` para considerar deep links de notificações por push que abrem seu app quando ele não está em execução. Por exemplo:

```javascript
// Handles deep links when an app is launched from a hard close via push click.
Braze.getInitialPushPayload(pushPayload => {
  if (pushPayload) {
    console.log('Braze.getInitialPushPayload is ' + pushPayload);
    showToast('Initial URL is ' + pushPayload.url);
    handleOpenUrl({ pushPayload.url });
  }
});
```
{% alert note %}
Este método requer a configuração nativa da Etapa 3.1 para sua plataforma. Se você estiver usando o plugin Braze Expo, isso pode ser tratado automaticamente.
{% endalert %}

#### Etapa 3.3: Ativar Universal Links (opcional)

Para ativar o suporte a [Universal Links]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#universal-links), implemente um delegado da Braze que determina se deve abrir uma URL específica e então registre-o com sua instância da Braze.

{% subtabs local %}
{% subtab Swift %}
Crie um arquivo `BrazeReactDelegate.swift` no seu diretório `iOS` e adicione o seguinte. Substitua `YOUR_DOMAIN_HOST` pelo seu domínio real.

```swift
import Foundation
import BrazeKit
import UIKit

class BrazeReactDelegate: NSObject, BrazeDelegate {

  /// This delegate method determines whether to open a given URL.
  /// Reference the context to get additional details about the URL payload.
  func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
    if let host = context.url.host,
       host.caseInsensitiveCompare("YOUR_DOMAIN_HOST") == .orderedSame {
      // Sample custom handling of universal links
      let application = UIApplication.shared
      let userActivity = NSUserActivity(activityType: NSUserActivityTypeBrowsingWeb)
      userActivity.webpageURL = context.url
      // Routes to the `continueUserActivity` method, which should be handled in your AppDelegate.
      application.delegate?.application?(
        application,
        continue: userActivity,
        restorationHandler: { _ in }
      )
      return false
    }
    // Let Braze handle links otherwise
    return true
  }
}
```

Em seguida, crie e registre seu `BrazeReactDelegate` em `didFinishLaunchingWithOptions` do arquivo `AppDelegate.swift` do seu projeto.

```swift
import BrazeKit

class AppDelegate: UIResponder, UIApplicationDelegate {
  
  static var braze: Braze?
  
  // Keep a strong reference to the BrazeDelegate so it is not deallocated.
  private var brazeDelegate: BrazeReactDelegate?
  
  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    // Other setup code (e.g., Braze initialization)
    
    brazeDelegate = BrazeReactDelegate()
    AppDelegate.braze?.delegate = brazeDelegate
    return true
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
Crie um arquivo `BrazeReactDelegate.h` no seu diretório `iOS` e adicione o seguinte trecho de código.

```objc
#import <Foundation/Foundation.h>
#import <BrazeKit/BrazeKit-Swift.h>

@interface BrazeReactDelegate: NSObject<BrazeDelegate>

@end
```

Em seguida, crie um arquivo `BrazeReactDelegate.m` e adicione o seguinte trecho de código. Substitua `YOUR_DOMAIN_HOST` pelo seu domínio real.

```objc
#import "BrazeReactDelegate.h"
#import <UIKit/UIKit.h>

@implementation BrazeReactDelegate

/// This delegate method determines whether to open a given URL.
///
/// Reference the `BRZURLContext` object to get additional details about the URL payload.
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  if ([[context.url.host lowercaseString] isEqualToString:@"YOUR_DOMAIN_HOST"]) {
    // Sample custom handling of universal links
    UIApplication *application = UIApplication.sharedApplication;
    NSUserActivity* userActivity = [[NSUserActivity alloc] initWithActivityType:NSUserActivityTypeBrowsingWeb];
    userActivity.webpageURL = context.url;
    // Routes to the `continueUserActivity` method, which should be handled in your `AppDelegate`.
    [application.delegate application:application
                 continueUserActivity:userActivity restorationHandler:^(NSArray<id<UIUserActivityRestoring>> * _Nullable restorableObjects) {}];
    return NO;
  }
  // Let Braze handle links otherwise
  return YES;
}

@end
```

Em seguida, crie e registre seu `BrazeReactDelegate` em `didFinishLaunchingWithOptions` do arquivo `AppDelegate.m` do seu projeto.

```objc
#import "BrazeReactUtils.h"
#import "BrazeReactDelegate.h"

@interface AppDelegate ()

// Keep a strong reference to the BrazeDelegate to ensure it is not deallocated.
@property (nonatomic, strong) BrazeReactDelegate *brazeDelegate;

@end

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  // Other setup code

  self.brazeDelegate = [[BrazeReactDelegate alloc] init];
  braze.delegate = self.brazeDelegate;
}
```
{% endsubtab %}
{% endsubtabs %}

Para um exemplo de integração, consulte nosso app de amostra [aqui](https://github.com/braze-inc/braze-react-native-sdk/blob/master/BrazeProject/ios/BrazeProject/AppDelegate.mm).
{% endtab %}
{% endtabs %}

### Etapa 4: Gerencie notificações em primeiro plano

O gerenciamento de notificações em primeiro plano funciona de maneira diferente dependendo da sua plataforma e configuração. Escolha a abordagem que corresponde à sua integração:

{% tabs local %}
{% tab iOS %}
Para iOS, o gerenciamento de notificações em primeiro plano é o mesmo da integração nativa em Swift. Chame `handleForegroundNotification(notification:)` dentro da sua implementação de `UNUserNotificationCenterDelegate.userNotificationCenter(_:willPresent:withCompletionHandler:)`.

Para detalhes completos e exemplos de código, consulte [Gerenciando notificações em primeiro plano]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#handling-foreground-notifications) na documentação de notificações por push do Swift.
{% endtab %}

{% tab Android %}
Para Android, o gerenciamento de notificações em primeiro plano é o mesmo da integração nativa do Android. Chame `BrazeFirebaseMessagingService.handleBrazeRemoteMessage` dentro do seu método `FirebaseMessagingService.onMessageReceived`.

Para detalhes completos e exemplos de código, consulte [Gerenciando notificações em primeiro plano]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android#handling-foreground-notifications) na documentação de notificações por push do Android.
{% endtab %}

{% tab Expo %}
No fluxo de trabalho gerenciado pelo Expo, você não chama manipuladores de notificações nativos diretamente. Em vez disso, use a API de Notificações do Expo para controlar a apresentação em primeiro plano, enquanto o Plugin Braze para Expo lida automaticamente com o processamento nativo.

```javascript
import * as Notifications from 'expo-notifications';
import Braze from '@braze/react-native-sdk';

// Control foreground presentation in Expo
Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true,    // Show alert while in foreground
    shouldPlaySound: false,
    shouldSetBadge: false,
  }),
});

// React to Braze push events
const subscription = Braze.addListener('pushNotificationEvent', (event) => {
  console.log('Braze push event', {
    type: event.payload_type,   // "push_received" | "push_opened"
    title: event.title,
    url: event.url,
    is_silent: event.is_silent,
  });
  // Handle deep links, custom behavior, etc.
});

// Handle initial payload when app launches via push
Braze.getInitialPushPayload((payload) => {
  if (payload) {
    console.log('Initial push payload', payload);
  }
});
```

{% alert note %}
No fluxo de trabalho gerenciado pelo Expo, o Plugin Braze para Expo lida automaticamente com o processamento de push nativo. Você controla a interface em primeiro plano por meio das opções de apresentação de Notificações do Expo mostradas acima.
{% endalert %}

Para integrações de fluxo de trabalho bare, siga as abordagens nativas do iOS e Android.
{% endtab %}
{% endtabs %}

### Etapa 5: Envie uma notificação por push de teste

Nesse ponto, você deve conseguir enviar notificações para os dispositivos. Siga as etapas a seguir para testar sua integração push.

{% alert note %}
A partir do macOS 13, em determinados dispositivos, você pode testar as notificações por push do iOS em um simulador iOS 16+ executado no Xcode 14 ou superior. Para mais informações, consulte as [Notas de versão do Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

1. Defina um usuário ativo no aplicativo React Native chamando o método `Braze.changeUserId('your-user-id')`.
2. Acesse **Campanhas** e crie uma nova campanha de notificação por push. Escolha as plataformas que você gostaria de testar.
3. Crie sua notificação de teste e vá para a guia **Teste**. Adicione o mesmo `user-id` como usuário teste e clique em **Enviar teste**. Você deverá receber a notificação no seu dispositivo em breve.

![Uma campanha push da Braze mostrando que você pode adicionar seu próprio ID de usuário como um destinatário de teste para testar sua notificação por push.]({% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test")

## Usando o plugin do Expo

Depois de [configurar notificações por push para o Expo](#reactnative_setting-up-push-notifications), você pode usá-lo para lidar com os seguintes comportamentos de notificações por push&#8212;sem precisar escrever nenhum código nas camadas nativas do Android ou iOS.

### Encaminhamento de push do Android para FMS adicionais

Se quiser usar um Firebase Messaging Service (FMS) adicional, você pode especificar um FMS de fallback para chamar se o aplicativo receber um push que não seja da Braze. Por exemplo:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "androidFirebaseMessagingFallbackServiceEnabled": true,
          "androidFirebaseMessagingFallbackServiceClasspath": "com.company.OurFirebaseMessagingService"
        }
      ]
    ]
  }
}
```

### Uso de extensões de app com o Expo Application Services {#app-extensions}

Se estiver usando o Expo Application Services (EAS) e tiver ativado `enableBrazeIosRichPush` ou `enableBrazeIosPushStories`, será necessário declarar os identificadores de pacote correspondentes para cada extensão de app no seu projeto. Há várias maneiras de abordar essa etapa, dependendo de como seu projeto está configurado para gerenciar a assinatura de código com o EAS.

Uma abordagem é usar a configuração `appExtensions` no seu arquivo `app.json` seguindo a [documentação de extensões de app](https://docs.expo.dev/build-reference/app-extensions/) da Expo. Como alternativa, você pode definir a configuração `multitarget` no seu arquivo `credentials.json` seguindo a [documentação sobre credenciais locais](https://docs.expo.dev/app-signing/local-credentials/#multi-target-project) da Expo.

### Solução de problemas

Estas são etapas comuns de solução de problemas para integrações de notificações por push com o SDK Braze React Native e o plugin do Expo.

#### As notificações por push pararam de funcionar {#troubleshooting-stopped-working}

Se as notificações por push pelo plugin do Expo pararam de funcionar:

1. Verifique se o SDK da Braze ainda está rastreando sessões.
2. Verifique se o SDK não foi desativado por uma chamada explícita ou implícita para `wipeData`.
3. Revise quaisquer atualizações recentes do Expo ou de suas bibliotecas relacionadas, pois pode haver conflitos com sua configuração da Braze.
4. Revise as dependências do projeto adicionadas recentemente e verifique se elas estão substituindo manualmente seus métodos de delegado de notificação por push existentes.

{% alert tip %}
Para integrações iOS, você também pode consultar nosso [tutorial de configuração de notificação por push](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications) para ajudar a identificar possíveis conflitos com as dependências do seu projeto.
{% endalert %}

#### O token do dispositivo não registra na Braze {#troubleshooting-token-registration}

Se o token do seu dispositivo não estiver sendo registrado na Braze, primeiro revise [As notificações por push pararam de funcionar](#troubleshooting-stopped-working).

Se o problema persistir, pode haver uma dependência separada interferindo na configuração de notificação por push da Braze. Você pode tentar removê-la ou chamar `Braze.registerPushToken` manualmente.