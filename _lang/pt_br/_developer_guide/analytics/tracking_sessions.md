---
nav_title: Sessões de rastreamento
article_title: Rastreamento de sessões por meio do SDK do Braze
page_order: 3.3
description: "Saiba como rastrear sessões por meio do SDK do Braze."

---

# Sessões de rastreamento

> Saiba como rastrear sessões por meio do SDK do Braze.

{% alert note %}
Para SDKs de wrapper não listados, use o método nativo relevante do Android ou Swift.
{% endalert %}

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## Inscrever-se para receber atualizações de sessões

### Etapa 1: Inscrever-se para receber atualizações

Para assinar as atualizações da sessão, use o método `subscribeToSessionUpdates()`.

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab java %}

```java
Braze.getInstance(this).subscribeToSessionUpdates(new IEventSubscriber<SessionStateChangedEvent>() {
  @Override
  public void trigger(SessionStateChangedEvent message) {
    if (message.getEventType() == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
      // A session has just been started
    }
  }
});
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
Se você registrar um retorno de chamada de ponta a ponta da sessão, ele será acionado quando o app retornar ao primeiro plano. A duração da sessão é medida a partir do momento em que o app é aberto, ou em primeiro plano, até o momento em que é fechado, ou em segundo plano.

{% subtabs %}
{% subtab swift %}
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

Para assinar um fluxo assíncrono, você pode usar [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) em vez disso.

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
{% endsubtab %}

{% subtab objective-c %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
No momento, a assinatura de atualizações de sessão não é compatível com o SDK do Braze.
{% endtab %}
{% endtabs %}

### Etapa 2: Rastreamento de sessões de teste (opcional)

Para testar o rastreamento de sessão, inicie uma sessão em seu dispositivo, abra o dashboard do Braze e pesquise o usuário relevante. No perfil do usuário, selecione **Sessions Overview (Visão geral das sessões**). Se as métricas forem atualizadas conforme o esperado, o rastreamento de sessão está funcionando corretamente.

![A seção de visão geral das sessões de um perfil de usuário mostrando o número de sessões, a data da última utilização e a data da primeira utilização.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
Os detalhes específicos do aplicativo são mostrados apenas para usuários que usaram mais de um aplicativo.
{% endalert %}

## Alteração do tempo limite padrão da sessão {#change-session-timeout}

Você pode alterar o período de tempo decorrido antes que uma sessão seja automaticamente encerrada.

{% tabs %}
{% tab Android %}
Por padrão, o tempo limite da sessão é definido como `10` segundos. Para alterar isso, abra seu arquivo `braze.xml` e adicione o parâmetro `com_braze_session_timeout`. Ele pode ser definido como qualquer número inteiro maior ou igual a `1`.

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab swift %}
Por padrão, o tempo limite da sessão é definido como `10` segundos. Para alterar isso, defina `sessionTimeout` no objeto `configuration` que é passado para [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class). Ele pode ser definido como qualquer número inteiro maior ou igual a `1`.

{% subtabs %}
{% subtab swift %}
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
{% endsubtab %}
{% subtab objective-c %}

```objc
// Sets the session timeout to 60 seconds
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                  endpoint:brazeEndpoint];
configuration.sessionTimeout = 60;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
Por padrão, o tempo limite da sessão é definido como `30` minutos. Para alterar isso, passe a opção `sessionTimeoutInSeconds` para sua função [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) função. Ele pode ser definido como qualquer número inteiro maior ou igual a `1`. 

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}
{% endtabs %}

{% alert note %}
Se você definir um tempo limite da sessão, toda a semântica da sessão será automaticamente estendida até o tempo limite definido.
{% endalert %}
