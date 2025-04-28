---
nav_title: Envio de mensagens no app
article_title: Envio de mensagens no app para iOS
platform: Swift
page_order: 2
description: "Este artigo aborda a entrega de mensagens no app do iOS, listando diferentes tipos de gatilho, semântica de entrega e etapas de disparo de eventos para o Swift SDK."
channel:
  - in-app messages

---

# Envio de mensagens no app

> Este artigo de referência fornece uma visão geral da entrega de mensagens no app do iOS, listando diferentes tipos de disparo, semântica de entrega e etapas de disparo de eventos.

## Tipos de disparo

As mensagens no app são disparadas por eventos registrados pelo SDK. Você pode disparar uma mensagem no app a partir dos seguintes tipos de eventos: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, e `Push Click`. Além disso, os disparadores `Specific Purchase` e `Custom Event` contêm filtros de propriedade robustos.

{% alert note %}
As mensagens no app disparadas só funcionam com eventos personalizados registrados por meio do SDK da Braze. As mensagens no app não podem ser disparadas por meio da API ou por eventos da API (como eventos de compra). Se estiver trabalhando com iOS, visite nosso artigo sobre [rastreamento de eventos personalizados]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/) para saber mais.
{% endalert %}

## Ativação de mensagens no app

Para permitir que a Braze exiba mensagens no app, crie uma implementação do protocolo `BrazeInAppMessagePresenter` e atribua-o ao `inAppMessagePresenter` opcional em sua instância da Braze. Você também pode usar o apresentador padrão do Braze UI instanciando um objeto `BrazeInAppMessageUI`.

Será necessário importar a biblioteca `BrazeUI` para acessar a classe `BrazeInAppMessageUI`.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.inAppMessagePresenter = BrazeInAppMessageUI()
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
AppDelegate.braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
```
{% endtab %}
{% endtabs %}

## Semântica de entrega

Todas as mensagens no app para as quais um usuário é elegível são entregues ao dispositivo do usuário no início da sessão. Após a entrega, o SDK fará a pré-busca de ativos para que estejam disponíveis imediatamente no momento do disparo, minimizando a latência da exibição.

Quando um evento-gatilho tiver mais de uma mensagem no app elegível associada a ele, somente a mensagem no app com a prioridade mais alta será entregue.

Pode haver alguma latência para mensagens no app que são exibidas imediatamente após a entrega (início da sessão, push click) devido ao fato de os ativos não serem pré-processados. Para saber mais sobre a semântica de início de sessão do SDK, leia sobre nosso [ciclo de vida de sessão]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/#session-lifecycle).

## Intervalo de tempo mínimo entre disparos

Por padrão, limitamos as mensagens no app a uma vez a cada 30 segundos para facilitar uma experiência de qualidade para o usuário.

Você pode substituir esse valor definindo a propriedade `triggerMinimumTimeInterval` em sua configuração da Braze. Certifique-se de configurar esse valor antes de inicializar sua instância do Braze. Defina `triggerMinimumTimeInterval` como o valor inteiro que deseja como tempo mínimo em segundos entre mensagens no app:

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
  endpoint: "YOUR-BRAZE-ENDPOINT"
)
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5
let braze = Braze(configuration: configuration) 
AppDelegate.braze = braze
```
{% endtab %}
{% tab OBJECTIVE C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% endtabs %}

## Falha ao encontrar um disparador correspondente

Quando a Braze não conseguir encontrar um disparador correspondente para um determinado evento, ela chamará [`BrazeDelegate.(_:noMatchingTriggerForEvent)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:nomatchingtriggerforevent:)-8rt7y/). Implemente esse método em sua classe adotando `BrazeDelegate` para lidar com esse cenário. 

## A pilha de mensagens no app

### Adição de mensagens no app à pilha

Os usuários são elegíveis para receber uma mensagem no app nas seguintes situações:

- Um evento de gatilho de mensagem no app é disparado
- Uma sessão é iniciada
- O app é aberto a partir de uma notificação por push

Quando o evento de gatilho de uma mensagem no app é disparado, ele é colocado em uma "pilha". Se várias mensagens no app estiverem na pilha e aguardando para serem exibidas, o Braze exibirá primeiro a mensagem no app recebida mais recentemente (última a entrar, primeira a sair).

Quando um usuário for elegível para receber uma mensagem no app, o `BrazeInAppMessagePresenter` solicitará a última mensagem no app da pilha de mensagens no app. A pilha só mantém na memória as mensagens no app armazenadas e é limpa entre as inicializações do app a partir do modo suspenso.

### Retornando mensagens no app para a pilha

Uma mensagem no app disparada pode ser retornada à pilha nas seguintes situações:

- A mensagem no app é disparada quando o app estiver em segundo plano.
- Outra mensagem no app está visível no momento.
- O [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` retornou `.reenqueue`.

A mensagem no app disparada será colocada no topo da pilha para exibição posterior quando um usuário for elegível para receber uma mensagem no app.

### Descarte de mensagens no app

Uma mensagem no app disparada será descartada nas seguintes situações:

- O [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` retornou `.discard`.
- O ativo (imagem ou arquivo ZIP) da mensagem no app não foi baixado.
- A mensagem no app está pronta para ser exibida, mas ultrapassou a duração do tempo limite.
- A orientação do dispositivo não corresponde à orientação da mensagem no app disparada.

A mensagem no app será removida da pilha. Após ser descartada, a mensagem no app pode ser disparada posteriormente por outra instância do evento de gatilho.

## Criação e exibição de mensagens no app em tempo real

Se desejar exibir uma mensagem no app em outros momentos do aplicativo, você poderá chamar manualmente o método [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) em seu `inAppMessagePresenter`. As mensagens no app podem ser criadas localmente no aplicativo e exibidas via Braze. Isso é particularmente útil para exibir mensagens que você deseja disparar no app em tempo real.

Note que, ao criar sua própria mensagem no app, você aceita qualquer rastreamento de análise de dados e terá que lidar manualmente com o registro de cliques e impressões usando o site `message.context`.

{% tabs %}
{% tab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
BRZInAppMessageRaw *customInAppMessage = [[BRZInAppMessageRaw alloc] init];
customInAppMessage.type = BRZInAppMessageRawTypeSlideup;
customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
customInAppMessage.slideFrom = BRZInAppMessageRawSlideFromBottom;
customInAppMessage.themes = @{
  @"light": BRZInAppMessageRawTheme.defaultLight,
  @"dark": BRZInAppMessageRawTheme.defaultDark
};
[AppDelegate.braze.inAppMessagePresenter presentMessage:customInAppMessage];
```

{% endtab %}
{% endtabs %}

## Extras de pares de valores chave

`Braze.InAppMessage` Os objetos podem conter pares chave-valor como `extras`. Elas são especificadas no dashboard ao criar uma campanha. Os pares chave-valor podem ser usados para enviar dados para baixo com uma mensagem no app para posterior envio de mensagens pelo seu aplicativo.

Por exemplo, considere um caso em que desejamos personalizar a apresentação de uma mensagem no app com base no conteúdo de seus extras. Poderíamos acessar os pares de valores-chave em sua propriedade `extras` e definir a lógica personalizada a ser executada em torno dela:

{% tabs %}
{% tab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```

{% endtab %}
{% endtabs %}

Para obter uma implementação completa, consulte os exemplos de personalização de mensagens no app em nosso [aplicativo de exemplo](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

