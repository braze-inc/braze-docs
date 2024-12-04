---
nav_title: Rastreamento de sessão
article_title: Rastreamento de sessão para iOS
platform: Swift
page_order: 0
search_rank: 1
description: "Este artigo de referência mostra como inscrever-se para receber atualizações de sessão para o Swift SDK."

---

# Rastreamento de sessão

> O Braze SDK informa os dados da sessão usados pelo dashboard do Braze para calcular o engajamento do usuário e outras análises essenciais para entender seus usuários. 

Nosso SDK gera pontos de dados de "início de sessão" e "encerramento de sessão" que contabilizam a duração da sessão e a contagem de sessões visualizáveis no dashboard do Braze com base na seguinte semântica de sessão.

## Ciclo de vida da sessão

Uma sessão é iniciada quando você chama `Braze.init(configuration:)`. Por padrão, isso ocorre quando a notificação `UIApplicationWillEnterForegroundNotification` é disparada (quando o app entra em primeiro plano). O fim da sessão ocorre quando o aplicativo sai do primeiro plano (por exemplo, quando a notificação `UIApplicationDidEnterBackgroundNotification` é disparada ou quando o aplicativo morre).

{% alert note %}
Se precisar forçar uma nova sessão, basta mudar de usuário.
{% endalert %}

## Personalização do tempo limite da sessão

Você pode definir o `sessionTimeout` como o valor inteiro desejado em seu objeto `configuration` passado para [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class).

{% tabs %}
{% tab swift %}

```swift
// Sets the session timeout to 60 seconds
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.sessionTimeout = 60;
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab Objective C %}

```objc
// Sets the session timeout to 60 seconds
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                  endpoint:brazeEndpoint];
configuration.sessionTimeout = 60;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

Se você tiver definido um tempo limite da sessão, a semântica da sessão se estenderá até esse tempo limite personalizado.

{% alert note %}
O valor mínimo para `sessionTimeout` é 1 segundo. O valor padrão é 10 segundos.
{% endalert %}

## Teste de rastreamento de sessão

Para detectar sessões por meio de seu usuário, localize-o no dashboard e navegue até **Sessions Overview (Visão geral das sessões** ) no perfil do usuário. Você pode confirmar que o rastreamento de sessões está funcionando verificando se a métrica "Sessões" aumenta quando você espera que isso aconteça. Os detalhes específicos do aplicativo serão exibidos depois que o usuário tiver usado mais de um aplicativo.

![A seção de visão geral das sessões de um perfil de usuário mostrando o número de sessões, a data da última utilização e a data da primeira utilização.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:40%;"}

Os detalhes específicos do aplicativo serão exibidos apenas se o usuário tiver usado mais de um aplicativo.

## Inscrever-se para receber atualizações de sessões

Para ouvir as atualizações de sessões, use o método [`subscribeToSessionUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/subscribetosessionupdates(_:)). Os eventos de início e fim de sessão só serão registrados quando o app estiver em execução em primeiro plano. Se você registrar um retorno de chamada para os eventos de ponta a ponta da sessão e o aplicativo estiver em segundo plano, o retorno de chamada será disparado quando o app for colocado em primeiro plano novamente. A duração da sessão, no entanto, ainda é medida como o tempo entre a abertura do app ou o primeiro plano até o fechamento do app ou o segundo plano.

{% tabs %}
{% tab swift %}
```swift
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.subscribeToSessionUpdates { event in
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```
{% endtab %}

{% tab Objective C %}
```objc
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
BRZCancellable *cancellable = [AppDelegate.braze subscribeToSessionUpdates:^(BRZSessionEvent * _Nonnull event) {
  switch (event.state) {
    case BRZSessionStateStarted:
      NSLog(@"Session %@ has started", event.sessionId);
      break;
    case BRZSessionStateEnded:
      NSLog(@"Session %@ has ended", event.sessionId);
      break;
    default:
      break;
  }
}];
```
{% endtab %}
{% endtabs %}

Como alternativa, em linguagem Swift, você pode usar o `AsyncStream` [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) para observar alterações assíncronas:

```swift
for await event in braze.sessionUpdatesStream {
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```

