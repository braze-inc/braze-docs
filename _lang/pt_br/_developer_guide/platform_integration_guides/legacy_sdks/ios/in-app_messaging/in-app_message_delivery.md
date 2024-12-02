---
nav_title: Envio de mensagens no app
article_title: Envio de mensagens no app para iOS
platform: iOS
page_order: 3
description: "Este artigo de referência aborda o envio de mensagens no app para iOS, listando diferentes tipos de disparo, semântica de entrega e etapas de disparo de eventos."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Envio de mensagens no app

## Tipos de disparo

Nosso produto de mensagens no app permite disparar a exibição de mensagens no app como resultado de vários tipos de eventos diferentes: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` e `Push Click`. Além disso, os disparos `Specific Purchase` e `Custom Event` contêm filtros de propriedade robustos.

{% alert note %}
As mensagens no app disparadas só funcionam com eventos personalizados registrados por meio do SDK da Braze. As mensagens no app não podem ser disparadas por meio da API ou por eventos da API (como eventos de compra). Se estiver trabalhando com iOS, visite nosso artigo sobre [rastreamento de eventos personalizados]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/) para saber mais.
{% endalert %}

## Semântica de entrega

Todas as mensagens no app para as quais um usuário é elegível são entregues ao dispositivo do usuário no início da sessão. No caso de duas mensagens no app serem disparadas por um evento, será mostrada a mensagem no app com a prioridade mais alta. Para saber mais sobre a semântica de início de sessão do SDK, leia sobre nosso [ciclo de vida de sessão]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-lifecycle). Após a entrega, o SDK fará a pré-busca de ativos para que estejam disponíveis imediatamente no momento do disparo, minimizando a latência da exibição.

Quando um evento-gatilho tiver mais de uma mensagem no app elegível associada a ele, somente a mensagem no app com a prioridade mais alta será entregue.

Pode haver alguma latência para mensagens no app que são exibidas imediatamente após a entrega (início da sessão, push click) devido ao fato de os ativos não serem pré-processados.

## Intervalo de tempo mínimo entre disparos

Por padrão, limitamos as mensagens no app a uma vez a cada 30 segundos para proporcionar uma experiência de qualidade para o usuário.

Você pode alterar esse valor em `ABKMinimumTriggerTimeIntervalKey` no parâmetro `appboyOptions` passado para `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Defina `ABKMinimumTriggerTimeIntervalKey` como o valor inteiro que deseja como tempo mínimo em segundos entre as mensagens no app:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:[ABKMinimumTriggerTimeIntervalKey : 5])
```

{% endtab %}
{% endtabs %}

## Falha ao encontrar um disparador correspondente

Quando a Braze não conseguir encontrar um gatilho correspondente para um determinado evento, ela chamará o método [noMatchingTriggerForEvent:name:](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html#ab4d57b13c51545d487227945a37d4ab8) de [`ABKInAppMessageControllerDelegate`](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html). Implemente esse método em sua classe adotando o protocolo de delegação para lidar com esse cenário. 

## Envio local de mensagens no app

### A pilha de mensagens no app

#### Exibição de mensagens no app

Quando um usuário for elegível para receber uma mensagem no app, `ABKInAppMessageController` receberá a mensagem no app mais recente da pilha de mensagens no app. A pilha só mantém na memória as mensagens no app armazenadas e é limpa entre as inicializações do app a partir do modo suspenso.

{% alert important %}
Não exiba mensagens no app quando o teclado for exibido na tela, pois a renderização é indefinida nessa circunstância.
{% endalert %}

#### Adição de mensagens no app à pilha

Os usuários são elegíveis para receber uma mensagem no app nas seguintes situações:

- Um evento de gatilho de mensagem no app é disparado
- Evento de início da sessão
- O app é aberto a partir de uma notificação por push

As mensagens no app disparadas são colocadas na pilha quando o evento-gatilho é disparado. Se várias mensagens no app estiverem na pilha e aguardando para serem exibidas, o Braze exibirá primeiro a mensagem no app recebida mais recentemente (última a entrar, primeira a sair).

#### Retorno de mensagens no app à pilha

Uma mensagem no app disparada pode ser retornada à pilha nas seguintes situações:

- A mensagem no app é disparada quando o app estiver em segundo plano.
- Outra mensagem no app está visível no momento.
- O [método delegado de interface]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#in-app-message-delegate) obsoleto `beforeInAppMessageDisplayed:withKeyboardIsUp:` não foi implementado, e o teclado em exibição no momento.
- O [método delegado]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#core-in-app-message-delegate) `beforeInAppMessageDisplayed:` ou o [método delegado de interface]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#in-app-message-delegate) `beforeInAppMessageDisplayed:withKeyboardIsUp:` obsoleto retornou `ABKDisplayInAppMessageLater`.

#### Descarte de mensagens no app

Uma mensagem no app disparada será descartada nas seguintes situações:

- O [método delegado]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#core-in-app-message-delegate) `beforeInAppMessageDisplayed:` ou o [método delegado de interface]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#in-app-message-delegate) `beforeInAppMessageDisplayed:withKeyboardIsUp:` obsoleto retornou `ABKDiscardInAppMessage`.
- O ativo (imagem ou arquivo ZIP) da mensagem no app não foi baixado.
- A mensagem no app está pronta para ser exibida, mas ultrapassou o tempo limite.
- A orientação do dispositivo não corresponde à orientação da mensagem no app disparada.
- A mensagem no app é uma mensagem no app completa, mas não tem imagem.
- A mensagem no app é uma mensagem modal no app somente de imagem, mas não tem imagem.

#### Enfileirar manualmente a exibição de mensagens no app

Para exibir uma mensagem no app em outros momentos no app, você poderá exibir manualmente a mensagem no app que estiver mais à frente na pilha chamando o método a seguir:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance].inAppMessageController displayNextInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()!.inAppMessageController.displayNextInAppMessage()
```

{% endtab %}
{% endtabs %}

### Criação e exibição de mensagens no app em tempo real

As mensagens no app também podem ser criadas localmente no aplicativo e exibidas via Braze. Isso é particularmente útil para exibir mensagens que você deseja disparar no app em tempo real. A Braze não é compatível com a análise de dados em mensagens no app criadas localmente.

{% tabs %}
{% tab OBJECTIVE C %}

```objc
  ABKInAppMessageSlideup *customInAppMessage = [[ABKInAppMessageSlideup alloc] init];
  customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
  customInAppMessage.duration = 2.5;
  customInAppMessage.extras = @{@"key" : @"value"};
  [[Appboy sharedInstance].inAppMessageController addInAppMessage:customInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
  let customInAppMessage = ABKInAppMessageSlideup.init()
  customInAppMessage.message = "YOUR_CUSTOM_SLIDEUP_MESSAGE"
  customInAppMessage.duration = 2.5
  customInAppMessage.extras = ["key": "value"]
  Appboy.sharedInstance()!.inAppMessageController.add(customInAppMessage)
```

{% endtab %}
{% endtabs %}

