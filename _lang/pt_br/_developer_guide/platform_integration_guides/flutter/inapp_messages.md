---
nav_title: Mensagens no app
article_title: Envio de mensagens no app para o Flutter
platform: Flutter
page_order: 4
page_type: reference
description: "Este artigo aborda as mensagens em apps para iOS e Android usando o Flutter, incluindo personalização e análise de dados de registro."
channel: in-app messages

---

# Integração de mensagens no app

> Saiba como integrar e personalizar mensagens no app para Android e iOS usando o Flutter.

## Ativar a interface do usuário de mensagens no app

Para integrar as mensagens no app do Flutter no iOS, [ative o envio de mensagens no aplicativo usando o Braze Swift SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#enabling-in-app-messages). Não há etapas adicionais para o Android.

## Análise de dados de registro

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

## Desativação da exibição automática

Para desativar a exibição automática de mensagens no app, faça essas atualizações na camada nativa.

{% tabs %}
{% tab Android %}

1. Use sempre o inicializador de integração automática, que está habilitado por padrão a partir da versão `2.2.0`.
2. Defina o padrão da operação de mensagem no app como `DISCARD` adicionando a seguinte linha ao seu arquivo `braze.xml`.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

{% endtab %}
{% tab iOS %}

1. Implemente o delegado `BrazeInAppMessageUIDelegate` conforme descrito no [artigo sobre iOS aqui](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. Atualize seu método delegado `inAppMessage(_:displayChoiceForMessage:)` para retornar `.discard`.

{% endtab %}
{% endtabs %}

## Recebimento de dados de mensagens no app

Para receber dados de mensagens no app em seu app Flutter, o `BrazePlugin` é compatível com o envio de dados de mensagens no app usando o [Dart Streams](https://dart.dev/tutorials/language/streams).

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

### Opção 1 - Usando `BrazeInAppMessageUIDelegate`

1. Implemente o delegado `BrazeInAppMessageUIDelegate` conforme descrito no artigo do iOS sobre o [delegado de mensagens no app](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

2. Atualize a [implementação do delegado `willPresent` ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv) para chamar `BrazePlugin.process(inAppMessage)`.

### Opção 2 - Apresentador de mensagens no app personalizado

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

{% endtab %}
{% endtabs %}

#### Reprodução da chamada de retorno para mensagens no app

Para armazenar mensagens no app disparadas antes que o retorno de chamada esteja disponível e reproduzi-las depois que ele for definido, adicione a seguinte entrada ao mapa `customConfigs` ao inicializar o `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## Teste uma amostra de mensagem no app

Siga estas etapas para testar um exemplo de mensagem no app.

1. Defina um usuário ativo no app React chamando o método `braze.changeUser('your-user-id')`.
2. Vá até a página **Campanhas** em seu dashboard e siga [este guia]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) para criar uma nova campanha de mensagens no app.
3. Crie sua campanha de mensagens no app de teste e vá para a guia **Teste**. Adicione o mesmo `user-id` que o usuário teste e clique em **Send Test (Enviar teste**).
4. Toque na notificação por push e isso deverá exibir a mensagem no app em seu dispositivo.

## Suporte a GIFs

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

![Uma campanha de mensagens no app do Braze mostrando que você pode adicionar seu próprio ID de usuário como um destinatário de teste para testar sua mensagem no app.]({% image_buster /assets/img/react-native/iam-test.png %} "In-App Messaging Test")

