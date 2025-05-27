{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Envio de mensagens

### Tipos de disparo

As mensagens no app são disparadas automaticamente quando o SDK registra um dos seguintes tipos de eventos personalizados: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, e `Push Click`. Note que os disparadores `Specific Purchase` e `Custom Event` também contêm filtros de propriedade robustos.

{% alert note %}
As mensagens no app não podem ser disparadas pela API ou por eventos da API - somente eventos personalizados registrados pelo SDK. Para saber mais sobre registro, consulte [Registro de eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift).
{% endalert %}

### Semântica de entrega

Todas as mensagens no app elegíveis são enviadas para o dispositivo do usuário no início da sessão. Quando entregue, o SDK fará a pré-busca de ativos para que eles estejam disponíveis no momento do disparo, minimizando a latência da exibição. Se o evento de gatilho tiver mais de uma mensagem elegível no app, somente a mensagem com a prioridade mais alta será entregue.

Para saber mais sobre a semântica de início de sessão do SDK, consulteSession[Lifecycle (Ciclo de vida]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift) da sessão).

### Limite de frequência padrão

Por padrão, você pode enviar uma mensagem no app uma vez a cada 30 segundos.

Para substituir isso, adicione a propriedade `triggerMinimumTimeInterval` à sua configuração do Braze antes que a instância do Braze seja inicializada. Pode ser definido como qualquer número inteiro positivo e representa o intervalo de tempo mínimo em segundos. Por exemplo:

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

## Pares de valores chave

Ao criar uma campanha no Braze, você pode definir pares de valores-chave como `extras`, que o objeto de mensagens no app pode usar para enviar dados ao seu aplicativo. Por exemplo:

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

## Desativação de disparos automáticos

Para evitar que as mensagens no app sejam disparadas automaticamente:

1. Implemente o delegado `BrazeInAppMessageUIDelegate` conforme descrito no [artigo sobre iOS aqui](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
2. Atualize seu método delegado `inAppMessage(_:displayChoiceForMessage:)` para retornar `.discard`.

## Envio manual de mensagens

### Usando um evento no lado do servidor

Para disparar mensagens no app usando eventos do lado do servidor, envie um push silencioso para o dispositivo para permitir que ele registre um evento baseado no SDK. Este evento do SDK pode, posteriormente, disparar a mensagem no app voltada para o usuário.

#### Etapa 1: Lidar com push silencioso e pares chave-valor

Implemente a seguinte função e chame-a dentro do [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`: método](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/):

{% tabs %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endtab %}
{% endtabs %}

Quando o push silencioso é recebido, um evento registrado pelo SDK "disparar mensagem no app" será registrado no perfil do usuário. 

{% alert important %}
Devido a uma mensagem por push ser usada para registrar um evento personalizado registrado pelo SDK, a Braze precisará armazenar um token por push para cada usuário para ativar essa solução. Para usuários de iOS, a Braze só armazenará um token a partir do momento em que o usuário receber o prompt de push do sistema operacional. Antes disso, o usuário não estará acessível usando push, e a solução anterior não será possível.
{% endalert %}

#### Etapa 2: Crie uma campanha de push silenciosa

Crie uma [campanha de push silenciosa]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift), que é disparada pelo evento enviado pelo servidor. 

![Uma campanha de mensagens no app com entrega baseada em ação que será entregue aos usuários cujos perfis de usuário tenham o evento personalizado "server_event".]({% image_buster /assets/img_archive/iosServerSentPush.png %})

A campanha de push precisa incluir extras de pares chave-valor, que indicam que esta campanha de push é enviada para registrar um evento personalizado do SDK. Este evento será usado para disparar a mensagem no app.

![Uma campanha de mensagem no app de entrega baseada em ação que possui dois pares chave-valor. "CAMPAIGN_NAME" definido como "Exemplo de nome de mensagem no app" e "IS_SERVER_EVENT" definido como "true".]({% image_buster /assets/img_archive/iOSServerPush.png %})

O código dentro do método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` verifica a chave `IS_SERVER_EVENT` e registra um evento personalizado do SDK se estiver presente.

Você pode alterar o nome do evento ou as propriedades do evento enviando o valor desejado dentro do par chave-valor extras da carga útil push. Ao registrar o evento personalizado, esses extras podem ser usados como parâmetro do nome do evento ou como uma propriedade do evento.

#### Etapa 3: Crie uma campanha de mensagem no app

Crie sua campanha de mensagem no app visível para o usuário no dashboard da Braze. Esta campanha deve ter uma entrega baseada em ação e ser acionada a partir do evento personalizado registrado dentro do método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

No exemplo a seguir, a mensagem no app específica a ser acionada foi configurada enviando a propriedade do evento como parte do push silencioso inicial.

![Uma campanha de mensagens no app com entrega baseada em ação que será entregue aos usuários que executarem o evento personalizado "Disparo de mensagem no app", em que "campaign_name" é igual a "Exemplo de nome de campanha do IAM".]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Note que essas mensagens no app só serão disparadas se o push silencioso for recebido enquanto o aplicativo estiver em primeiro plano.
{% endalert %}

### Exibição de um

Para exibir manualmente uma mensagem no app predefinida, use o seguinte método:

```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```

### Envio de mensagens em tempo real

Você também pode exibir mensagens locais no app em tempo real, chamando manualmente o método [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) em seu site `inAppMessagePresenter`. Por exemplo:

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

{% alert note %}
Ao criar sua própria mensagem no app, você aceita qualquer rastreamento de análise de dados e terá que lidar manualmente com o registro de cliques e impressões usando o site `message.context`.
{% endalert %}

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

- A mensagem no app é disparada quando o aplicativo está em segundo plano.
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
