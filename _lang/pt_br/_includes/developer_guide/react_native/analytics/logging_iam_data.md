{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Métodos de registro

Você pode usar esses métodos passando sua instância`BrazeInAppMessage` para registro análise de dados e realizar ações:

| Método                                                    | Descrição                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `logInAppMessageClicked(inAppMessage)`                    | Registra um clique para os dados da mensagem no app fornecidos.                                    |
| `logInAppMessageImpression(inAppMessage)`                 | Registra uma impressão para os dados da mensagem no app fornecidos.                              |
| `logInAppMessageButtonClicked(inAppMessage, buttonId)`    | Registra um clique no botão para os dados da mensagem no app fornecidos e o ID do botão.               |
| `hideCurrentInAppMessage()`                               | Descarta a mensagem no app atualmente exibida.                                     |
| `performInAppMessageAction(inAppMessage)`                 | Executa a ação para uma mensagem no app.                                            |
| `performInAppMessageButtonAction(inAppMessage, buttonId)` | Executa a ação para um botão de mensagem no app.                                     |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Envio de mensagens de dados

Na maioria dos casos, você pode usar o método `Braze.addListener` para registrar ouvintes de eventos para lidar com dados provenientes de mensagens no app. 

Além disso, você pode acessar os dados da mensagem no app na camada JavaScript chamando o método `Braze.subscribeToInAppMessage` para que os SDKs publiquem um evento `inAppMessageReceived` quando uma mensagem no app for acionada. Passe um retorno de chamada para este método para executar seu próprio código quando a mensagem no app for acionada e recebida pelo ouvinte.

Para personalizar a forma como os dados das mensagens são tratados, consulte os exemplos de implementação a seguir:

{% tabs local %}
{% tab basic %}
Para aprimorar o comportamento padrão, ou se você não tiver acesso para personalizar o código nativo do iOS ou do Android, recomendamos que você desative a interface do usuário padrão e, ao mesmo tempo, continue recebendo eventos de mensagens no app com código personalizado do Braze. Para desativar a interface do usuário padrão, passe `false` para o método `Braze.subscribeToInAppMessage` e use os dados da mensagem no app para construir sua própria mensagem em JavaScript. Note que será necessário registrar manualmente a análise de dados em suas mensagens se optar por desativar a IU padrão.

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
{% endtab %}

{% tab advanced %}
Para incluir uma lógica mais avançada para determinar se deve ou não mostrar uma mensagem no app usando a interface do usuário integrada, implemente mensagens no app através da camada nativa.

{% alert warning %}
Como esta é uma opção de personalização avançada, note que substituir a implementação padrão da Braze também anulará a lógica para emitir eventos de mensagens no app para seus ouvintes JavaScript. Se você deseja continuar usando `Braze.subscribeToInAppMessage` ou `Braze.addListener` conforme descrito em [Accessando dados de mensagem no app](#accessing-in-app-message-data), você precisará lidar com a publicação dos eventos por conta própria.
{% endalert %}

{% subtabs %}
{% subtab Android %}
Implemente o `IInAppMessageManagerListener` conforme descrito em nosso artigo do Android sobre [Custom Manager Listener]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners). Na sua `beforeInAppMessageDisplayed` implementação, você pode acessar os dados `inAppMessage`, enviá-los para a camada JavaScript e decidir mostrar ou não a mensagem nativa com base no valor de retorno.

Para mais informações sobre esses valores, consulte nossa [documentação do Android]({{site.baseurl}}/developer_guide/in_app_messages/).

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
{% endsubtab %}
{% subtab iOS %}
### Substituindo o delegate de interface do usuário padrão

Por padrão, [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/) é criado e atribuído quando você inicializa a instância `braze`. `BrazeInAppMessageUI` é uma implementação do protocolo [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) e vem com uma propriedade `delegate` que pode ser usada para personalizar o tratamento de mensagens no app que foram recebidas.

1. Implemente o `BrazeInAppMessageUIDelegate` conforme descrito em [nosso artigo sobre iOS aqui](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. No método delegate`inAppMessage(_:displayChoiceForMessage:)`, você pode acessar os dados `inAppMessage`, enviá-los para a camada JavaScript e decidir mostrar ou não a mensagem nativa com base no valor de retorno.

Para mais detalhes sobre esses valores, consulte nossa [documentação do iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/).

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

Para usar este delegate, atribua-o a `brazeInAppMessagePresenter.delegate` após inicializar a instância `braze`. 

{% alert note %}
`BrazeUI` só pode ser importado em Objective-C ou SWIFT. Se você estiver usando Objective-C++, precisará lidar com isso em um arquivo separado.
{% endalert %}

```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  ((BrazeInAppMessageUI *)braze.inAppMessagePresenter).delegate = [[CustomDelegate alloc] init];
  AppDelegate.braze = braze;
}
```

### Substituindo a interface de usuário nativa padrão

Se você deseja personalizar totalmente a apresentação de suas mensagens no app na camada nativa do iOS, conforme o protocolo [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) e atribua seu apresentador personalizado seguindo o exemplo abaixo:

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
