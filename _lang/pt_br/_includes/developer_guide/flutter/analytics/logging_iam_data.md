{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Registrando dados de mensagens

Para registrar análises de dados usando o `BrazeInAppMessage`, passe a instância para a função de análise de dados desejada:

- `logInAppMessageClicked`
- `logInAppMessageImpression`
- `logInAppMessageButtonClicked` (juntamente com o índice do botão)

Por exemplo:

```dart
// Log a click
braze.logInAppMessageClicked(inAppMessage);
// Log an impression
braze.logInAppMessageImpression(inAppMessage);
// Log button index `0` being clicked
braze.logInAppMessageButtonClicked(inAppMessage, 0);
```

## Acessando dados de mensagens

Para acessar os dados de mensagens no app no seu app Flutter, o `BrazePlugin` oferece suporte ao envio de dados de mensagens no app usando [Dart Streams](https://dart.dev/tutorials/language/streams).

O objeto `BrazeInAppMessage` é compatível com um subconjunto de campos disponíveis nos objetos do modelo nativo, incluindo `uri`, `message`, `header`, `buttons`, `extras`, entre outros.

### Ouvir dados de mensagens no app na camada Dart

Para receber os dados da mensagem no app na camada Dart, use o código abaixo para criar um `StreamSubscription` e chamar `braze.subscribeToInAppMessages()`. Lembre-se de usar `cancel()` na inscrição do stream quando ela não for mais necessária.

```dart
// Create stream subscription
StreamSubscription inAppMessageStreamSubscription;

inAppMessageStreamSubscription = braze.subscribeToInAppMessages((BrazeInAppMessage inAppMessage) {
  // Handle in-app messages
}

// Cancel stream subscription
inAppMessageStreamSubscription.cancel();
```

Para ver um exemplo, consulte [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) no app de amostra do Braze Flutter SDK.

### Encaminhar dados de mensagens no app a partir da camada nativa

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

Os dados de mensagens no app são encaminhados automaticamente a partir das camadas nativas do Android e do iOS. Nenhuma configuração adicional é necessária.

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

Se você estiver usando o Flutter SDK 17.1.0 ou anterior, o encaminhamento de dados de mensagens no app a partir da camada nativa do iOS requer configuração manual. Seu aplicativo provavelmente contém uma das opções a seguir. Para migrar para o Flutter SDK 18.0.0, remova a chamada `BrazePlugin.processInAppMessage(_:)` — o encaminhamento de dados agora é feito automaticamente.

{% subtabs %}
{% subtab UI Delegate %}

Remova a chamada `BrazePlugin.processInAppMessage(_:)` da sua [implementação do delegado `willPresent`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv).

{% endsubtab %}

{% subtab Custom presenter %}

Remova a chamada `BrazePlugin.processInAppMessage(message)` da implementação [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/present(message:)-f2ra) do seu apresentador personalizado:

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

### Reproduzindo o retorno de chamada para mensagens no app (opcional)

Para armazenar mensagens no app disparadas antes que o retorno de chamada esteja disponível e reproduzi-las depois que ele for definido, adicione a seguinte entrada ao mapa `customConfigs` ao inicializar o `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
