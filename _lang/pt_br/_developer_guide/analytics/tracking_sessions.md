---
nav_title: Rastrear sessões
article_title: Rastrear sessões através do SDK da Braze
page_order: 3.3
description: "Aprenda como rastrear sessões através do SDK da Braze."

---

# Rastrear sessões

> Aprenda como rastrear sessões através do SDK da Braze.

{% alert note %}
Para wrapper SDKs não listados, use o método nativo relevante do Android ou Swift.
{% endalert %}

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## Definindo inatividade

Entender como a inatividade é definida e medida é fundamental para gerenciar ciclos de vida de sessão de forma eficaz no SDK Web. Inatividade refere-se a um período durante o qual o SDK Web da Braze não detecta nenhum evento rastreado do usuário.

### Como a inatividade é medida

O SDK Web rastreia a inatividade com base em [eventos rastreados pelo SDK]({{site.baseurl}}/user_guide/data/activation/custom_data/events/#events). O SDK mantém um temporizador interno que é redefinido cada vez que um evento rastreado é enviado. Se nenhum evento rastreado pelo SDK ocorrer dentro do período de tempo limite configurado, a sessão é considerada inativa e termina.

Para saber mais sobre como o ciclo de vida da sessão é implementado no SDK Web, veja o código-fonte de gerenciamento de sessão no [repositório do Braze Web SDK no GitHub](https://github.com/braze-inc/braze-web-sdk/blob/master/src/session.ts).

**O que conta como atividade por padrão:**
- Abrir ou atualizar o app web
- Interagir com elementos de UI da Braze (como [mensagens no app]({{site.baseurl}}/developer_guide/in_app_messages/) ou [Cartões de conteúdo]({{site.baseurl}}/developer_guide/content_cards/))
- Chamar métodos do SDK que enviam eventos rastreados (como [eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/) ou [atualizações de atributos do usuário]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/))

**O que não conta como atividade por padrão:**
- Alternar para uma guia de navegador diferente
- Minimizar a janela do navegador
- Eventos de foco ou desfoque do navegador
- Rolagem ou movimentos do mouse na página

{% alert note %}
O SDK Web não rastreia automaticamente mudanças de visibilidade do navegador, troca de guia ou foco do usuário. No entanto, você pode rastrear essas interações em nível de navegador implementando ouvintes de eventos personalizados usando a [API de Visibilidade da Página](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API) do navegador e enviando [eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web) para a Braze. Para um exemplo de implementação, consulte [Rastreamento de inatividade personalizada](#tracking-custom-inactivity).
{% endalert %}

### Configuração de tempo limite de sessão

Por padrão, o SDK Web considera uma sessão inativa após 30 minutos sem nenhum evento rastreado. Você pode personalizar esse limite ao inicializar o SDK usando o parâmetro `sessionTimeoutInSeconds`. Para detalhes sobre como configurar esse parâmetro, incluindo exemplos de código, veja [Alterando o tempo limite padrão da sessão](#changing-the-default-session-timeout).

### Exemplo: Entendendo cenários de inatividade

Considere o seguinte cenário:

1. Um usuário abre seu site, e o SDK inicia uma sessão chamando [`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession).
2. O usuário troca para uma guia de navegador diferente para visualizar outro site por 30 minutos.
3. Durante esse tempo, nenhum evento rastreado pelo SDK ocorre no seu site.
4. Após 30 minutos de inatividade, a sessão termina automaticamente.
5. Quando o usuário volta para a guia do seu site e aciona um evento do SDK (como visualizar uma página ou interagir com o conteúdo), uma nova sessão começa.

### Rastreamento de inatividade personalizada

Se você precisar rastrear inatividade com base na visibilidade do navegador ou troca de guia, implemente ouvintes de eventos personalizados no seu código JavaScript. Use eventos do navegador, como `visibilitychange`, para detectar quando os usuários saem da sua página e envie manualmente [eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/) para a Braze ou chame [`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession) quando apropriado.

```javascript
// Example: Track when user switches away from tab
document.addEventListener('visibilitychange', function() {
  if (document.hidden) {
    // User switched away - optionally log a custom event
    braze.logCustomEvent('tab_hidden');
  } else {
    // User returned - optionally start a new session and/or log an event
    // braze.openSession();
    braze.logCustomEvent('tab_visible');
  }
});
```

Para saber mais sobre o registro de eventos personalizados, consulte [Registro de eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/). Para detalhes sobre o ciclo de vida da sessão e configuração de tempo limite, consulte [Alterando o tempo limite padrão da sessão](#change-session-timeout).

## Inscrever-se para receber atualizações de sessão

### Etapa 1: Inscrever-se para receber atualizações

Para se inscrever em atualizações de sessão, use o método `subscribeToSessionUpdates()`.

{% tabs %}
{% tab web %}
Neste momento, a inscrição para atualizações de sessão não é suportada pelo SDK Web da Braze.
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
Se você registrar um retorno de chamada de fim de sessão, ele será acionado quando o app retornar ao primeiro plano. A duração da sessão é medida desde o momento em que o app é aberto ou colocado em primeiro plano até que ele seja fechado ou colocado em segundo plano.

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

Para assinar um fluxo assíncrono, você pode usar [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream).

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

{% tab react native %}
O SDK React Native não expõe um método para assinar atualizações de sessão diretamente. O ciclo de vida da sessão é gerenciado pelo SDK nativo subjacente, então, para assinar atualizações, use a abordagem da plataforma nativa na guia **Android** ou **Swift**.
{% endtab %}
{% endtabs %}

### Etapa 2: Testar rastreamento de sessão (opcional)

Para testar o rastreamento de sessão, inicie uma sessão no seu dispositivo, depois abra o dashboard da Braze e procure o usuário relevante. No perfil do usuário, selecione **Visão Geral das Sessões**. Se as métricas forem atualizadas como esperado, o rastreamento de sessão está funcionando corretamente.

![A seção de visão geral das sessões de um perfil de usuário mostrando o número de sessões, data da última utilização e data da primeira utilização.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
Informações específicas do app são mostradas apenas para usuários que usaram mais de um app.
{% endalert %}

## Alterando o tempo limite padrão da sessão {#change-session-timeout}

Você pode alterar a duração do tempo que passa antes que uma sessão expire automaticamente.

{% tabs %}
{% tab web %}
Por padrão, o tempo limite da sessão é definido como `30` minutos. Para alterar isso, passe a opção `sessionTimeoutInSeconds` para sua função [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize). Pode ser definido como qualquer inteiro maior ou igual a `1`. 

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}

{% tab android %}
Por padrão, o tempo limite da sessão é definido como `10` segundos. Para alterar isso, abra seu arquivo `braze.xml` e adicione o parâmetro `com_braze_session_timeout`. Pode ser definido como qualquer inteiro maior ou igual a `1`.

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab swift %}
Por padrão, o tempo limite da sessão é definido como `10` segundos. Para alterar isso, defina `sessionTimeout` no objeto `configuration` que é passado para [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class). Pode ser definido como qualquer inteiro maior ou igual a `1`.

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

{% tab react native %}
O SDK React Native depende dos SDKs nativos para gerenciar sessões. Para alterar o tempo limite padrão da sessão, configure-o na camada nativa:

- **Android:** Defina `com_braze_session_timeout` no seu arquivo `braze.xml`. Para detalhes, selecione a guia **Android**.
- **iOS:** Defina `sessionTimeout` no seu objeto `Braze.Configuration`. Para detalhes, selecione a guia **Swift**.
{% endtab %}
{% endtabs %}

{% alert note %}
Se você definir um tempo limite de sessão, todas as semânticas de sessão serão automaticamente estendidas para o tempo limite definido.
{% endalert %}

## Solução de problemas

### Perfil de usuário tem 0 sessões

Um perfil de usuário pode ter 0 sessões se o usuário foi criado fora do SDK:

- **Criado pela API REST:** Se um usuário é criado através do endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) com um `app_id` na requisição, o perfil aparece associado a esse app, mas não possui dados de sessão porque o SDK nunca foi inicializado para esse usuário.
- **Criado por importação CSV:** Se um usuário é importado por [CSV]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) sem valores para os campos de primeira ou última sessão, o perfil existe com 0 sessões.