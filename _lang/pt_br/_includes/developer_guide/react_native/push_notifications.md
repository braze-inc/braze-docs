{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Configuração de notificações por push {#setting-up-push-notifications}

### Etapa 1: Concluir a configuração inicial

{% tabs local %}
{% tab Expo %}
#### Pré-requisitos

Antes de poder usar a Expo para notificações por push, você precisará [configurar o plug-in Braze Expo]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/sdk_integration/?tab=expo).

#### Etapa 1.1: Atualize seu arquivo `app.json` 

Em seguida, atualize seu arquivo `app.json` para Android e iOS:

- **Android:** Adicione a opção `enableFirebaseCloudMessaging`.
- **iOS:** Adicione a opção `enableBrazeIosPush`.

#### Etapa 1.2: Adicione seu ID de remetente do Google

Primeiro, acesse o Firebase Console, abra seu projeto e selecione <i class="fa-solid fa-gear"></i> **Settings** > **Project settings**.

![O projeto Firebase com o menu "Settings" aberto.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Selecione **Envio de mensagens na nuvem** e, em seguida, em **Firebase Cloud Messaging API (V1)**, copie o **ID do remetente** para a área de transferência.

![A página "Cloud Messaging" do projeto Firebase com o "Sender ID" destacado.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

Em seguida, abra o arquivo `app.json` do seu projeto e defina a propriedade `firebaseCloudMessagingSenderId` como o ID do remetente na área de transferência. Por exemplo:

```
"firebaseCloudMessagingSenderId": "693679403398"
```

#### Etapa 1.3: Adicione a jornada ao seu JSON do Google Services

No arquivo `app.json` de seu projeto, adicione a jornada para seu arquivo `google-services.json`. Esse arquivo é necessário ao definir `enableFirebaseCloudMessaging: true` em sua configuração.

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
Se não estiver usando o plug-in Braze Expo ou se, em vez disso, quiser definir essas configurações nativamente, registre-se para receber push consultando o [guia de integração de push nativo do Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/).
{% endtab %}

{% tab iOS Native %}
Se não estiver usando o plug-in Braze Expo ou se, em vez disso, quiser definir essas configurações nativamente, registre-se para push consultando as etapas a seguir do [guia de integração de push nativo do iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift):

#### Etapa 1.1: Solicitação de permissões push

Se não planeja solicitar permissões push quando o app for iniciado, omita a chamada `requestAuthorizationWithOptions:completionHandler:` em seu AppDelegate. Em seguida, pule para a [etapa 2](#reactnative_step-2-request-push-notifications-permission). Caso contrário, siga o [guia de integração nativa do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

#### Etapa 1.2 (opcional): Migre sua chave push

Se estava usando anteriormente o site `expo-notifications` para gerenciar sua chave push, execute o site `expo fetch:ios:certs` na pasta raiz do seu aplicativo. Isso baixará sua chave push (um arquivo .p8), que poderá ser feito upload no dashboard da Braze.
{% endtab %}
{% endtabs %}

### Etapa 2: Solicitar permissão para notificações por push

Use o método `Braze.requestPushPermission()` (disponível na versão v1.38.0 e superior) para solicitar permissão para notificações por push do usuário no iOS e no Android 13+. Para o Android 12 e versões inferiores, esse método não funciona.

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

Além disso, você pode se inscrever em eventos em que o Braze detectou e tratou uma notificação por push recebida. Use a tecla do ouvinte `Braze.Events.PUSH_NOTIFICATION_EVENT`.

{% alert important %}
os eventos de push recebidos do iOS só dispararão para notificações em primeiro plano e `content-available` notificações em segundo plano. Não disparará para notificações recebidas enquanto encerrado ou para notificações em segundo plano sem o campo `content-available`.
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
| `payload_type`     | String    | Especifica o tipo de carga útil da notificação. Os dois valores enviados pelo SDK da Braze React Native são `push_opened` e `push_received`. |
| `url`              | String    | Especifica a URL que foi aberta pela notificação. |
| `use_webview`      | Booleano   | Se for `true`, o URL será aberto no app em uma visualização modal da Web. Se `false`, o URL será aberto no navegador do dispositivo. |
| `title`            | String    | Representa o título da notificação. |
| `body`             | String    | Representa o corpo ou o texto do conteúdo da notificação. |
| `summary_text`     | String    | Representa o texto resumido da notificação. Isso é mapeado em `subtitle` no iOS. |
| `badge_count`      | Número   | Representa a contagem de emblemas da notificação. |
| `timestamp`        | Número | Representa a hora em que a carga útil foi recebida pelo aplicativo. |
| `is_silent`        | Booleano   | Se `true`, a carga útil é recebida silenciosamente. Para obter detalhes sobre o envio de notificações por push silenciosas no Android, consulte [Notificações por push silenciosas no Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android). Para obter detalhes sobre o envio de notificações por push silenciosas no iOS, consulte [Notificações por push silenciosas no iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift). |
| `is_braze_internal`| Booleano   | Este será o endereço `true` se uma carga útil de notificação tiver sido enviada para um recurso interno do SDK, como sincronização de geofences, sincronização de Feature Flag ou rastreamento de desinstalação. A carga útil é recebida silenciosamente para o usuário. |
| `image_url`        | String    | Especifica o URL associado à imagem da notificação. |
| `braze_properties` | Objeto    | Representa as propriedades do Braze associadas à campanha (pares chave-valor). |
| `ios`              | Objeto    | Representa campos específicos do iOS. |
| `android`          | Objeto    | Representa campos específicos do Android. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapa 3: Ativar o deep linking (opcional)

Para ativar o Braze para lidar com deep links dentro de componentes React quando uma notificação por push for clicada, primeiro implemente as etapas descritas na biblioteca [React Native Linking](https://reactnative.dev/docs/linking) ou com a solução de sua escolha. Em seguida, siga as etapas adicionais abaixo.

Para saber mais sobre o que são deep linkings, consulte nosso [artigo de perguntas frequentes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

{% tabs local %}
{% tab Android Native %}
Se estiver usando [o plug-in Braze Expo]({{site.baseurl}}/developer_guide/platforms/react_native/sdk_integration/?tab=expo#step-2-choose-a-setup-option), poderá lidar com os deep links de notificações por push automaticamente, definindo `androidHandlePushDeepLinksAutomatically` como `true` em seu `app.json`.

Para lidar com deep links manualmente, consulte a documentação nativa do Android: [Adição de deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking).

{% endtab %}
{% tab iOS Native %}
#### Etapa 3.1: Armazene a carga útil da notificação por push na inicialização do aplicativo
{% alert note %}
Pule a etapa 3.1 se estiver usando o plug-in Braze Expo, pois essa funcionalidade é tratada automaticamente.
{% endalert %}

Para iOS, adicione `populateInitialPayloadFromLaunchOptions` ao método `didFinishLaunchingWithOptions` de seu AppDelegate. Por exemplo:

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  self.moduleName = @"BrazeProject";
  self.initialProps = @{};

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

#### Etapa 3.2: Lidar com deep linking a partir de um estado fechado

Além dos cenários básicos tratados pelo [React Native Linking](https://reactnative.dev/docs/linking), implemente o método `Braze.getInitialPushPayload` e recupere o valor `url` para levar em conta os deep links das notificações por push que abrem o app quando ele não está em execução. Por exemplo:

```javascript
// Handles deep links when an iOS app is launched from a hard close via push click.
// This edge case is not handled in the React Native Linking library and is provided as a workaround by Braze.
Braze.getInitialPushPayload(pushPayload => {
  if (pushPayload) {
    console.log('Braze.getInitialPushPayload is ' + pushPayload);
    showToast('Initial URL is ' + pushPayload.url);
    handleOpenUrl({ pushPayload.url });
  }
});
```
{% alert note %}
A Braze fornece essa solução alternativa, pois a API de vinculação do React Native não oferece suporte a esse cenário devido a uma condição de corrida na inicialização do app.
{% endalert %}

#### Etapa 3.3 Ativar links universais (opcional)

Para ativar o suporte à [vinculação universal]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#universal-links), crie um arquivo `BrazeReactDelegate.h` em seu diretório `iOS` e adicione o seguinte trecho de código.

```objc
#import <Foundation/Foundation.h>
#import <BrazeKit/BrazeKit-Swift.h>

@interface BrazeReactDelegate: NSObject<BrazeDelegate>

@end
```

Em seguida, crie um arquivo `BrazeReactDelegate.m` e adicione o seguinte trecho de código. Substitua `YOUR_DOMAIN_HOST` por seu domínio real.

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

Para obter um exemplo de integração, consulte nosso app de amostra [aqui](https://github.com/braze-inc/braze-react-native-sdk/blob/master/BrazeProject/ios/BrazeProject/AppDelegate.mm).
{% endtab %}
{% endtabs %}

### Etapa 4: Enviar uma notificação por push de teste

Nesse ponto, você deve poder enviar notificações aos dispositivos. Siga as etapas a seguir para testar sua integração push.

{% alert note %}
A partir do macOS 13, em determinados dispositivos, você pode testar as notificações por push do iOS em um simulador iOS 16+ executado no Xcode 14 ou superior. Para mais informações, consulte [as Notas de versão do Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

1. Defina um usuário ativo no aplicativo React Native chamando o método `Braze.changeUserId('your-user-id')`.
2. Vá para **Campaigns (Campanhas** ) e crie uma nova campanha de notificação por push. Escolha as plataformas que você gostaria de testar.
3. Crie sua notificação de teste e vá para a guia **Teste**. Adicione o mesmo `user-id` que o usuário teste e clique em **Send Test (Enviar teste**). Você deverá receber a notificação em seu dispositivo em breve.

![Uma campanha push do Braze mostrando que você pode adicionar seu próprio ID de usuário como um destinatário de teste para testar sua notificação por push.]({% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test")

## Usando o plug-in Expo

Depois de [configurar as notificações por push para a Expo](#reactnative_setting-up-push-notifications), você poderá usá-la para lidar com os seguintes comportamentos de notificações por push, sem precisar escrever nenhum código nas camadas nativas do Android ou do iOS.

### Encaminhamento de push do Android para FMS adicionais

Se quiser usar um Firebase Messaging Service (FMS) adicional, você pode especificar um FMS fallback para chamar se o aplicativo receber um push que não seja do Braze. Por exemplo:

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

Se estiver usando o Expo Application Services (EAS) e tiver ativado `enableBrazeIosRichPush` ou `enableBrazeIosPushStories`, será necessário declarar os identificadores de pacote correspondentes para cada extensão de app em seu projeto. Há várias maneiras de abordar essa etapa, dependendo de como seu projeto está configurado para gerenciar a assinatura de código com o EAS.

Uma abordagem é usar a configuração `appExtensions` em seu arquivo `app.json` seguindo [a documentação de extensões de app](https://docs.expo.dev/build-reference/app-extensions/) da Expo. Como alternativa, você pode definir a configuração `multitarget` em seu arquivo `credentials.json` seguindo a [documentação sobre credenciais de localização](https://docs.expo.dev/app-signing/local-credentials/#multi-target-project) da Expo.

### Solução de problemas

Estas são etapas comuns de solução de problemas para integrações de notificações por push com o SDK React Native do Braze e o plug-in Expo.

#### As notificações por push pararam de funcionar {#troubleshooting-stopped-working}

Se as notificações por push por meio do plug-in Expo pararem de funcionar:

1. Verifique se o SDK do Braze ainda está rastreando as sessões.
2. Verifique se o SDK não foi desativado por uma chamada explícita ou implícita para `wipeData`.
3. Revise todas as atualizações recentes da Expo ou de suas bibliotecas relacionadas, pois pode haver conflitos com sua configuração do Braze.
4. Revise as dependências de projeto adicionadas recentemente e verifique se elas estão substituindo manualmente os métodos delegados de notificação por push existentes.

{% alert tip %}
Para integrações com iOS, você também pode consultar nosso [tutorial de configuração de notificações por push](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications) para ajudá-lo a identificar possíveis conflitos com as dependências do seu projeto.
{% endalert %}

#### O token do dispositivo não é registrado no Braze {#troubleshooting-token-registration}

Se o token do seu dispositivo não se registrar no Braze, primeiro analise [As notificações por push pararam de funcionar](#troubleshooting-stopped-working).

Se o problema persistir, pode haver uma dependência separada interferindo em sua configuração de notificação por push do Braze. Você pode tentar removê-lo ou, em vez disso, chamar manualmente `Braze.registerPushToken`.
