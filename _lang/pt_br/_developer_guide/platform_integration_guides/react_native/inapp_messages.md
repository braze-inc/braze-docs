---
nav_title: Mensagens no app
article_title: Mensagens no app para React Native
platform: React Native
page_order: 4
page_type: reference
description: "Este artigo aborda mensagens no aplicativo para apps iOS e Android usando React Native, incluindo personalização e registro de análise de dados."
channel: in-app messages

---

# Integração de mensagem no app

> Mensagens nativas no app são exibidas automaticamente no Android e iOS ao usar React Native. Este artigo aborda a personalização e o registro de análise de dados para suas mensagens no aplicativo para apps usando React Native.

## Acessando dados de mensagem no app

Na maioria dos casos, você pode usar o método `Braze.addListener` para registrar ouvintes de eventos para lidar com dados provenientes de mensagens no app. 

Além disso, você pode acessar os dados da mensagem no app na camada JavaScript chamando o método `Braze.subscribeToInAppMessage` para que os SDKs publiquem um evento `inAppMessageReceived` quando uma mensagem no app for acionada. Passe um retorno de chamada para este método para executar seu próprio código quando a mensagem no app for acionada e recebida pelo ouvinte.

Para personalizar ainda mais o comportamento padrão, ou se você não tiver acesso para personalizar o código nativo do iOS ou Android, recomendamos que você desative a interface do usuário padrão enquanto ainda recebe eventos de mensagem no app da Braze. Para desativar a interface do usuário padrão, passe `false` para o método `Braze.subscribeToInAppMessage` e use os dados da mensagem no app para construir sua própria mensagem em JavaScript. Nota que você precisará [registrar manualmente a análise de dados](#analytics) em suas mensagens se optar por desativar a interface padrão.

```javascript
import Braze from "@braze/react-native-sdk";

// Option 1: Listen for the event directly via `Braze.addListener`.
//
// You may use this method to accomplish the same thing if you don't
// wish to make any changes to the default Braze UI.
Braze.addListener(Braze.Events.IN_APP_MESSAGE_RECEIVED, (event) => {
  console.log(event.inAppMessage);
});

// Option 2: Call `subscribeToInAppMessage`.
//
// Pass in `false` to disable the automatic display of in-app messages.
Braze.subscribeToInAppMessage(false, (event) => {
  console.log(event.inAppMessage);
  // Use `event.inAppMessage` to construct your own custom message UI.
});
```

## Customização avançada

Para incluir uma lógica mais avançada para determinar se deve ou não mostrar uma mensagem no app usando a interface do usuário integrada, implemente mensagens no app através da camada nativa.

{% alert warning %}
Como esta é uma opção de personalização avançada, note que substituir a implementação padrão da Braze também anulará a lógica para emitir eventos de mensagens no app para seus ouvintes JavaScript. Se você deseja continuar usando `Braze.subscribeToInAppMessage` ou `Braze.addListener` conforme descrito em [Accessando dados de mensagem no app](#accessing-in-app-message-data), você precisará lidar com a publicação dos eventos por conta própria.
{% endalert %}

{% tabs %}
{% tab Android %}

Implemente o `IInAppMessageManagerListener` conforme descrito em nosso artigo do Android sobre [Custom Manager Listener]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-manager-listener). Na sua `beforeInAppMessageDisplayed` implementação, você pode acessar os dados `inAppMessage`, enviá-los para a camada JavaScript e decidir mostrar ou não a mensagem nativa com base no valor de retorno.

Para mais informações sobre esses valores, consulte nossa [documentação do Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/).

```java
// In-app messaging
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
    WritableMap parameters = new WritableNativeMap();
    parameters.putString("inAppMessage", inAppMessage.forJsonPut().toString());
    getReactNativeHost()
        .getReactInstanceManager()
        .getCurrentReactContext()
        .getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class)
        .emit("inAppMessageReceived", parameters);
    // Note: return InAppMessageOperation.DISCARD if you would like
    // to prevent the Braze SDK from displaying the message natively.
    return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab iOS %}
### Substituindo o delegate de interface do usuário padrão

Por padrão, [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/) é criado e atribuído quando você inicializa a instância `braze`. `BrazeInAppMessageUI` é uma implementação do protocolo [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) e vem com uma propriedade `delegate` que pode ser usada para personalizar o tratamento de mensagens no app que foram recebidas.

1. Implemente o `BrazeInAppMessageUIDelegate` conforme descrito em [nosso artigo sobre iOS aqui](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. No método delegate`inAppMessage(_:displayChoiceForMessage:)`, você pode acessar os dados `inAppMessage`, enviá-los para a camada JavaScript e decidir mostrar ou não a mensagem nativa com base no valor de retorno.

Para mais detalhes sobre esses valores, consulte nossa [documentação do iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/).

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  // Convert the message to a JavaScript representation.
  NSData *inAppMessageData = [message json];
  NSString *inAppMessageString = [[NSString alloc] initWithData:inAppMessageData encoding:NSUTF8StringEncoding];
  NSDictionary *arguments = @{
    @"inAppMessage" : inAppMessageString
  };

  // Send to JavaScript.
  [self sendEventWithName:@"inAppMessageReceived" body:arguments];

  // Note: Return `BRZInAppMessageUIDisplayChoiceDiscard` if you would like
  // to prevent the Braze SDK from displaying the message natively.
  return BRZInAppMessageUIDisplayChoiceNow;
}
```
{% endsubtab %}
{% endsubtabs %}

Para usar este delegate, atribua-o a `brazeInAppMessagePresenter.delegate` após inicializar a instância `braze`. 

{% alert note %}
`BrazeUI` só pode ser importado em Objective-C ou SWIFT. Se você estiver usando Objective-C++, precisará lidar com isso em um arquivo separado.
{% endalert %}

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  ((BrazeInAppMessageUI *)braze.inAppMessagePresenter).delegate = [[CustomDelegate alloc] init];
  AppDelegate.braze = braze;
}
```
{% endsubtab %}
{% endsubtabs %}

### Substituindo a interface de usuário nativa padrão

Se você deseja personalizar totalmente a apresentação de suas mensagens no app na camada nativa do iOS, conforme o protocolo [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) e atribua seu apresentador personalizado seguindo o exemplo abaixo:

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
Braze *braze = [BrazeReactBridge initBraze:configuration];
braze.inAppMessagePresenter = [[MyCustomPresenter alloc] init];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## análise de dados e métodos de ação

Você pode usar esses métodos passando sua instância`BrazeInAppMessage` para registro análise de dados e realizar ações:

| Método                                                    | Descrição                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `logInAppMessageClicked(inAppMessage)`                    | Registra um clique para os dados da mensagem no app fornecidos.                                    |
| `logInAppMessageImpression(inAppMessage)`                 | Registra uma impressão para os dados da mensagem no app fornecidos.                              |
| `logInAppMessageButtonClicked(inAppMessage, buttonId)`    | Registra um clique no botão para os dados da mensagem no app fornecidos e o ID do botão.               |
| `hideCurrentInAppMessage()`                               | Descarta a mensagem no app atualmente exibida.                                     |
| `performInAppMessageAction(inAppMessage)`                 | Executa a ação para uma mensagem no app.                                            |
| `performInAppMessageButtonAction(inAppMessage, buttonId)` | Executa a ação para um botão de mensagem no app.                                     |

## Teste exibindo uma mensagem no app de exemplo

Siga estas etapas para testar uma mensagem no app de exemplo.

1. Defina um usuário ativo no aplicativo React chamando o método `Braze.changeUserId('your-user-id')`.
2. Vá para **Campanhas** e siga [este guia]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) para criar uma nova campanha de mensagem no app.
3. Componha sua campanha de mensagens no app e vá para a guia **Test**. Adicione o mesmo `user-id` que o usuário teste e clique em **Send Test (Enviar teste**). Você deve conseguir lançar uma mensagem no app no seu dispositivo em breve.

![Uma mensagem no app Braze mostrando que você pode adicionar seu próprio ID de usuário como um destinatário de teste para testar sua mensagem no app.]({% image_buster /assets/img/react-native/iam-test.png %} "Teste de Mensagens no App")

Uma implementação de exemplo pode ser encontrada no BrazeProject, dentro do [React Native SDK](https://github.com/braze-inc/braze-react-native-sdk). Amostras adicionais de implementação do Android e iOS podem ser encontradas no SDK [Android](https://github.com/braze-inc/braze-android-sdk) e no SDK [iOS](https://github.com/braze-inc/braze-swift-sdk).

## modelo de dados de mensagem no app

O modelo de mensagem no app está disponível no SDK do React Native. Braze tem quatro tipos de mensagem no app que compartilham o mesmo modelo de dados: **slideup**, **modal**, **full** e **HTML full**.

### propriedades do modelo de mensagem no app

O modelo de mensagem no app fornece a base para todas as mensagens no app.

|Propriedade          | Descrição                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------------------|
|`inAppMessageJsonString` | A representação JSON da mensagem.                                                                                |
|`message`         | O texto da mensagem.                                                                                                      |
|`header`          | O cabeçalho da mensagem.                                                                                                    |
|`uri`             | O URI associado à ação de clique do botão.                                                                       |
|`imageUrl`        | A URL da imagem da mensagem.                                                                                                 |
|`zippedAssetsUrl` | Os ativos compactados preparados para exibir conteúdo HTML.                                                                    |
|`useWebView`      | Indica se a ação de clique do botão deve redirecionar usando uma visualização da web.                                            |
|`duration`        | A duração de exibição da mensagem.                                                                                          |
|`clickAction`     | O tipo de ação de clique do botão. Os três tipos são: `NEWS_FEED`, `URI` e `NONE`.                                     |
|`dismissType`     | O tipo de fechamento da mensagem. Os dois tipos são: `SWIPE` e `AUTO_DISMISS`.                                                 |
|`messageType`     | O tipo de mensagem no app suportado pelo SDK. Os quatro tipos são: `SLIDEUP`, `MODAL`, `FULL` e `HTML_FULL`.          |
|`extras`          | O dicionário de extras da mensagem. Valor padrão: `[:]`.                                                                   |
|`buttons`         | A lista de botões na mensagem no app.                                                                             |
|`toString()`      | A mensagem como uma string de representação.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para uma referência completa do modelo de mensagem no app, consulte a documentação para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/index.html) e para [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

### propriedades do modelo de botão de mensagem no app

Botões podem ser adicionados às mensagens no app para realizar ações e registrar análise de dados. O modelo de botão fornece a base para todos os botões de mensagem no app.

|Propriedade          | Descrição                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
|`text`            | O texto no botão.                                                                                                     |
|`uri`             | O URI associado à ação de clique do botão.                                                                            |
|`useWebView`      | Indica se a ação de clique do botão deve redirecionar usando uma visualização da web.                                                 |
|`clickAction`     | O tipo de ação de clique processada quando o usuário clica no botão. Os três tipos são: `NEWS_FEED`, `URI` e `NONE`. |
|`id`              | O ID do botão na mensagem.                                                                                               |
|`toString()`      | A representação do botão como uma string.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para uma referência completa do modelo de botão, consulte a documentação para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) e para [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/button).

## Suporte a GIFs

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

