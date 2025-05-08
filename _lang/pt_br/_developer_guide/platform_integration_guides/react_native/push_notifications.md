---
nav_title: Notificações por push
article_title: Notificações por push para React Native
platform: React Native
page_order: 2
toc_headers: h2
description: "Este artigo aborda a implementação de notificações por push no React Native."
channel: push

---

# Integração de notificações por push

> Este artigo de referência aborda como definir notificações por push para o React Native. A integração de notificações por push requer a configuração de cada plataforma nativa separadamente. Siga os respectivos guias listados para concluir a instalação.

## Etapa 1: Concluir a configuração inicial

{% tabs %}
{% tab Expo %}
Defina as opções `enableBrazeIosPush` e `enableFirebaseCloudMessaging` em seu arquivo `app.json` para ativar o push para iOS e Android, respectivamente. Consulte as instruções de configuração [aqui]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/#step-2-complete-native-setup) para obter mais detalhes.

Note que será necessário usar essas configurações em vez das instruções de configuração nativas se estiver dependendo de bibliotecas adicionais de notificação por push, como a [Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/).
{% endtab %}

{% tab Android %}
### Etapa 1.1: Registro para push

Registre-se para push usando a API Firebase Cloud Messaging (FCM) do Google. Para obter um passo a passo completo, consulte as etapas a seguir do [guia de integração de push do Android nativo]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/):

1. [Adicione o Firebase ao seu projeto]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-add-firebase-to-your-project).
2. [Adicione o Cloud Messaging às suas dependências]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-2-add-cloud-messaging-to-your-dependencies).
3. [Crie uma conta de serviço]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-3-create-a-service-account).
4. [Gerar credenciais JSON]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-generate-json-credentials).
5. [Faça upload de suas credenciais JSON na Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-upload-your-json-credentials-to-braze).

### Etapa 1.2: Adicione seu ID de remetente do Google

Primeiro, acesse o Firebase Console, abra seu projeto e selecione <i class="fa-solid fa-gear"></i> **Settings** > **Project settings**.

![O projeto Firebase com o menu "Settings" (Configurações) aberto.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Selecione **Envio de mensagens na nuvem** e, em seguida, em **Firebase Cloud Messaging API (V1)**, copie o **ID do remetente** para a área de transferência.

![A página "Cloud Messaging" do projeto Firebase com o "Sender ID" destacado.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

Em seguida, abra o arquivo `app.json` do seu projeto e defina a propriedade `firebaseCloudMessagingSenderId` como o ID do remetente na área de transferência. Por exemplo:

```
"firebaseCloudMessagingSenderId": "693679403398"
```

### Etapa 1.3: Adicione a jornada ao seu JSON do Google Services

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
{% endtab %}

{% tab iOS %}
### Etapa 1.1: Faça upload de certificados APNs

Gere um certificado do serviço de Notificações por Push da Apple (APNs) e faça upload dele no dashboard do Braze. Veja um passo a passo completo em [Como fazer upload de seu certificado de APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-upload-your-apns-certificate).

### Etapa 1.2: Escolha um método de integração

Se não planeja solicitar permissões push quando o aplicativo for iniciado, omita a chamada `requestAuthorizationWithOptions:completionHandler:` em seu AppDelegate e pule para a [etapa 2](#step-2-request-push-notifications-permission). Caso contrário, siga o [guia de integração nativa do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

Quando terminar, continue na [etapa 1.3](#step-13-migrate-your-push-key).

### Etapa 1.3: Migre sua chave push

Se estava usando anteriormente o site `expo-notifications` para gerenciar sua chave push, execute o site `expo fetch:ios:certs` na pasta raiz do seu aplicativo. Isso baixará sua chave push (um arquivo .p8), que poderá ser feito upload no dashboard da Braze.
{% endtab %}
{% endtabs %}

## Etapa 2: Solicitar permissão para notificações por push

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

### Etapa 2.1: Ouça as notificações por push (opcional)

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

#### Campos de eventos de notificação por push

Para obter uma lista completa dos campos de notificação por push, consulte a tabela abaixo:

| Nome do campo         | Tipo      | Descrição |
| ------------------ | --------- | ----------- |
| `payload_type`     | String    | Especifica o tipo de carga útil da notificação. Os dois valores enviados pelo SDK da Braze React Native são `push_opened` e `push_received`. |
| `url`              | String    | Especifica a URL que foi aberta pela notificação. |
| `use_webview`      | Booleano   | Se for `true`, a URL será aberta no app em uma visualização modal da Web. Se for `false`, a URL será aberta no navegador do dispositivo. |
| `title`            | String    | Representa o título da notificação. |
| `body`             | String    | Representa o corpo ou o texto do conteúdo da notificação. |
| `summary_text`     | String    | Representa o texto resumido da notificação. Isso é mapeado em `subtitle` no iOS. |
| `badge_count`      | Número   | Representa a contagem de emblemas da notificação. |
| `timestamp`        | Número | Representa a hora em que a carga útil foi recebida pelo app. |
| `is_silent`        | Booleano   | Se for `true`, a carga útil é recebida silenciosamente. Para obter detalhes sobre o envio de notificações por push silenciosas no Android, consulte [Notificações por push silenciosas no Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications). Para obter detalhes sobre o envio de notificações por push silenciosas no iOS, consulte [Notificações por push silenciosas no iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/). |
| `is_braze_internal`| Booleano   | Este será o endereço `true` se uma carga útil de notificação tiver sido enviada para um recurso interno do SDK, como sincronização de geofences, sincronização de Feature Flag ou rastreamento de desinstalação. A carga útil é recebida silenciosamente para o usuário. |
| `image_url`        | String    | Especifica o URL associado à imagem da notificação. |
| `braze_properties` | Objeto    | Representa as propriedades do Braze associadas à campanha (pares chave-valor). |
| `ios`              | Objeto    | Representa campos específicos do iOS. |
| `android`          | Objeto    | Representa campos específicos do Android. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Etapa 3: Ativar o deep linking (opcional)

Para ativar a Braze para lidar com deep linkings dentro de componentes React quando uma notificação por push for clicada, siga as etapas adicionais.

{% tabs %}
{% tab Expo %}
Nosso [app de amostra BrazeProject](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) contém um exemplo completo de deep linking implementado. Para saber mais sobre o que são deep linkings, consulte nosso [artigo de perguntas frequentes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

{% endtab %}
{% tab Android %}
No Android, a configuração de deep links é idêntica à [configuração de deep links em apps nativos do Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-4-add-deep-links). Se quiser que o SDK da Braze manipule automaticamente os deep links de push, defina `androidHandlePushDeepLinksAutomatically: true` em seu `app.json`.

{% endtab %}
{% tab iOS %}
### Etapa 3.1: Adicionar recursos de deep linking

Para iOS, adicione `populateInitialUrlFromLaunchOptions` ao método `didFinishLaunchingWithOptions` de seu AppDelegate. Por exemplo:

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
  [[BrazeReactUtils sharedInstance] populateInitialUrlFromLaunchOptions:launchOptions];

  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}
```

### Etapa 3.2: Configurar o tratamento de deep linking

Use o método `Linking.getInitialURL()` para deep links que abrem o aplicativo e o método `Braze.getInitialURL` para deep links dentro de notificações por push que abrem o aplicativo quando ele não está em execução. Por exemplo:

```javascript
Linking.getInitialURL()
  .then(url => {
    if (url) {
      console.log('Linking.getInitialURL is ' + url);
      showToast('Linking.getInitialURL is ' + url);
      handleOpenUrl({ url });
    }
  })
  .catch(err => console.error('Error getting initial URL', err));

// Handles deep links when an iOS app is launched from a hard close via push click.
Braze.getInitialURL(url => {
  if (url) {
    console.log('Braze.getInitialURL is ' + url);
    showToast('Braze.getInitialURL is ' + url);
    handleOpenUrl({ url });
  }
});
```
{% alert note %}
A Braze fornece essa solução alternativa, pois a API de vinculação do React Native não oferece suporte a esse cenário devido a uma condição de corrida na inicialização do app.
{% endalert %}
{% endtab %}
{% endtabs %}

## Etapa 4: Teste a exibição de notificações por push

Nesse ponto, você deve poder enviar notificações aos dispositivos. Siga as etapas a seguir para testar sua integração push.

{% alert note %}
A partir do macOS 13, em determinados dispositivos, você pode testar as notificações por push do iOS em um simulador iOS 16+ executado no Xcode 14 ou superior. Para mais informações, consulte [as Notas de versão do Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

1. Defina um usuário ativo no aplicativo React chamando o método `Braze.changeUserId('your-user-id')`.
2. Vá para **Campaigns (Campanhas** ) e crie uma nova campanha de notificação por push. Escolha as plataformas que você gostaria de testar.
3. Crie sua notificação de teste e vá para a guia **Teste**. Adicione o mesmo `user-id` que o usuário teste e clique em **Send Test (Enviar teste**). Você deverá receber a notificação em seu dispositivo em breve.

![Uma campanha de push Braze mostrando que você pode adicionar seu próprio ID de usuário como um destinatário de teste para testar sua notificação por push.]({% image_buster /assets/img/react-native/push-notification-test.png %} "Teste de Campanha de Push")

## Encaminhamento de push do Android para FMS adicionais

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

## Configuração de extensões de app com o Expo

### Capacitação de notificações por push avançadas para iOS

{% alert tip %}
As notificações por push avançadas estão disponíveis para Android por padrão.
{% endalert %}

Para ativar notificações por push avançadas no iOS usando o Expo, configure a propriedade `enableBrazeIosRichPush` como `true` em seu objeto `expo.plugins` em `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosRichPush": true
        }
      ]
    ]
  }
}
```

Por fim, adicione o identificador de pacote para essa extensão de app à configuração de credenciais de seu projeto: `<your-app-bundle-id>.BrazeExpoRichPush`. Para obter mais detalhes sobre esse processo, consulte [Uso de extensões de app com o Expo Application Services](#app-extensions).

### Ativando o Push Stories para iOS

{% alert tip %}
As stories por push estão disponíveis para Android por padrão.
{% endalert %}

Para ativar os stories por push no iOS usando o Expo, é necessário ter um grupo de app definido para seu aplicativo. Para saber mais, veja [Adicionando um grupo de app]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/#adding-an-app-group).

Em seguida, configure a propriedade `enableBrazeIosPushStories` para `true` e atribua o ID do grupo de app a `iosPushStoryAppGroup` em seu objeto `expo.plugins` em `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.company.myApp.PushStories"
        }
      ]
    ]
  }
}
```

Por fim, adicione o identificador de pacote para essa extensão de app à configuração de credenciais de seu projeto: `<your-app-bundle-id>.BrazeExpoPushStories`. Para obter mais detalhes sobre esse processo, consulte [Uso de extensões de app com o Expo Application Services](#app-extensions).

{% alert warning %}
Se estiver usando stories por push com o Expo Application Services, use o sinalizador `EXPO_NO_CAPABILITY_SYNC=1` ao executar `eas build`. Há um problema conhecido na linha de comando que remove o recurso Grupos de app do perfil de provisionamento de sua extensão.
{% endalert %}

### Uso de extensões de app com o Expo Application Services {#app-extensions}

Se estiver usando o Expo Application Services (EAS) e tiver ativado `enableBrazeIosRichPush` ou `enableBrazeIosPushStories`, será necessário declarar os identificadores de pacote correspondentes para cada extensão de app em seu projeto. Há várias maneiras de abordar essa etapa, dependendo de como seu projeto está configurado para gerenciar a assinatura de código com o EAS.

Uma abordagem é usar a configuração `appExtensions` em seu arquivo `app.json` seguindo [a documentação de extensões de app](https://docs.expo.dev/build-reference/app-extensions/) da Expo. Como alternativa, você pode definir a configuração `multitarget` em seu arquivo `credentials.json` seguindo a [documentação sobre credenciais de localização](https://docs.expo.dev/app-signing/local-credentials/#multi-target-project) da Expo.

