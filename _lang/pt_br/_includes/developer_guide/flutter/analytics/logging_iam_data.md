{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Envio de mensagens de registro de dados

Para registrar análises de dados usando o `BrazeInAppMessage`, passe as referências de instância para a função de análises desejada:

- `logInAppMessageClicked`
- `logInAppMessageImpression`
- `logInAppMessageButtonClicked` (juntamente com o índice de botões)

Por exemplo:

```dart
// Log a click
braze.logInAppMessageClicked(inAppMessage);
// Log an impression
braze.logInAppMessageImpression(inAppMessage);
// Log button index `0` being clicked
braze.logInAppMessageButtonClicked(inAppMessage, 0);
```

## Acesso a dados de mensagens

Para acessar os dados de mensagens no app no seu aplicativo Flutter, o site `BrazePlugin` suporta o envio de dados de mensagens no app usando [o Dart Streams](https://dart.dev/tutorials/language/streams).

O objeto `BrazeInAppMessage` é compatível com um subconjunto de campos disponíveis nos objetos do modelo nativo, incluindo `uri`, `message`, `header`, `buttons`, `extras`, entre outros.

### Etapa 1: Ouça os dados de mensagens no app na camada Dart

Para receber os dados da mensagem no app na camada Dart, use o código abaixo para criar um `StreamSubscription` e chamar `braze.subscribeToInAppMessages()`. Lembre-se de `cancel()` a inscrição de fluxo quando ela não for mais necessária.

```dart
// Create stream subscription
StreamSubscription inAppMessageStreamSubscription;

inAppMessageStreamSubscription = braze.subscribeToInAppMessages((BrazeInAppMessage inAppMessage) {
  // Handle in-app messages
}

// Cancel stream subscription
inAppMessageStreamSubscription.cancel();
```

Para obter um exemplo, consulte [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) em nosso app de amostra.

### Etapa 2: Encaminhar dados de mensagens no app a partir da camada nativa

Para receber os dados na camada Dart da etapa 1, adicione o seguinte código para encaminhar os dados da mensagem no app a partir das camadas nativas.

{% tabs %}
{% tab Android %}

Os dados das mensagens no app são encaminhados automaticamente da camada Android.

{% endtab %}
{% tab iOS %}
{% subtabs %}

Você pode encaminhar dados de mensagens no app de duas maneiras:

{% subtab UI Delegate %}

1. Implemente o delegado `BrazeInAppMessageUIDelegate` conforme descrito no artigo do iOS sobre o [delegado de mensagens no app](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. Atualize a [implementação do delegado `willPresent` ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv) para chamar `BrazePlugin.process(inAppMessage)`.
{% endsubtab %}

{% subtab custom presenter %}
1. Certifique-se de ter ativado a interface do usuário de mensagens no app e defina o endereço `inAppMessagePresenter` como seu apresentador personalizado.
```swift
    let inAppMessageUI = CustomInAppMessagePresenter()
    braze.inAppMessagePresenter = inAppMessageUI
```
2. Crie sua classe de apresentador personalizada e acesse `BrazePlugin.process(inAppMessage)` em [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/present(message:)-f2ra).
```swift
class CustomInAppMessagePresenter: BrazeInAppMessageUI {
  override func present(message: Braze.InAppMessage) {
    // Pass in-app message data to the Dart layer.
    BrazePlugin.processInAppMessage(message)

    // If you want the default UI to display the in-app message.
    super.present(message: message)
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Etapa 3: Repetição do retorno de chamada para mensagens no app (opcional)

Para armazenar mensagens no app disparadas antes que o retorno de chamada esteja disponível e reproduzi-las depois que ele for definido, adicione a seguinte entrada ao mapa `customConfigs` ao inicializar o `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
