---
nav_title: Rastrear sessões
article_title: Rastrear sessões através do SDK Braze
page_order: 3.3
description: "Aprenda como rastrear sessões através do SDK Braze."

---

# Rastrear sessões

> Aprenda como rastrear sessões através do SDK Braze.

{% alert note %}
Para SDKs wrapper não listados, use o método nativo Android ou Swift relevante.
{% endalert %}

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## Inscrever-se para receber atualizações de sessões

### Etapa 1: Inscrever-se para receber atualizações

Para se inscrever em atualizações de sessão, use o método `subscribeToSessionUpdates()`.

{% tabs %}
{% tab web %}
Neste momento, a inscrição em atualizações de sessão não é suportada para o SDK Web Braze.
{% endtab %}

{% tab android %}
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
Se você registrar um retorno de chamada de fim de sessão, ele será acionado quando o app retornar ao primeiro plano. A duração da sessão é medida desde que o app é aberto ou colocado em primeiro plano, até que ele seja fechado ou colocado em segundo plano.

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

Para se inscrever em um fluxo assíncrono, você pode usar [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) em vez disso.

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
{% endtabs %}

### Etapa 2: Testar rastreamento de sessão (opcional)

Para testar o rastreamento de sessão, inicie uma sessão em seu dispositivo, depois abra o dashboard do Braze e procure o usuário relevante. No perfil do usuário, selecione **Visão Geral das Sessões**. Se as métricas forem atualizadas como esperado, o rastreamento de sessão está funcionando corretamente.

![A seção de visão geral das sessões de um perfil de usuário mostrando o número de sessões, data da última utilização e data da primeira utilização.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
Detalhes específicos do app são mostrados apenas para usuários que usaram mais de um app.
{% endalert %}

## Alterando o tempo limite padrão da sessão {#change-session-timeout}

Você pode alterar a duração do tempo que passa antes que uma sessão expire automaticamente.

{% tabs %}
{% tab web %}
Por padrão, o tempo limite da sessão é definido para `30` minutos. Para mudar isso, passe a opção `sessionTimeoutInSeconds` para sua função [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize). Pode ser definido para qualquer inteiro maior ou igual a `1`. 

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}

{% tab android %}
Por padrão, o tempo limite da sessão é definido para `10` segundos. Para mudar isso, abra seu arquivo `braze.xml` e adicione o parâmetro `com_braze_session_timeout`. Ele pode ser definido como qualquer inteiro maior ou igual a `1`.

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab swift %}
Por padrão, o tempo limite da sessão é definido para `10` segundos. Para mudar isso, defina `sessionTimeout` no objeto `configuration` que é passado para [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class). Pode ser definido para qualquer inteiro maior ou igual a `1`.

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
{% endtabs %}

{% alert note %}
Se você definir um tempo limite de sessão, toda a semântica da sessão será automaticamente estendida para o tempo limite definido.
{% endalert %}
