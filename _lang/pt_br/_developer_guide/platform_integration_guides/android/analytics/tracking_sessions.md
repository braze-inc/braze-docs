---
nav_title: Sessões de rastreamento
article_title: Sessões de rastreamento para Android e FireOS
platform: 
  - Android
  - FireOS
page_order: 0
description: "Este artigo de referência mostra como assinar atualizações de sessão para seu aplicativo Android ou FireOS."

---

# Sessões de rastreamento

> O Braze SDK informa os dados da sessão usados pelo dashboard do Braze para calcular o engajamento do usuário e outras análises essenciais para entender seus usuários. Nosso SDK gera pontos de dados de "início de sessão" e "encerramento de sessão" que levam em conta a duração da sessão e a contagem de sessões visualizáveis no dashboard do Braze com base na seguinte semântica de sessão. Este artigo de referência mostra como assinar atualizações de sessão para seu aplicativo Android ou FireOS.

## Ciclo de vida da sessão

Se você integrou o Braze usando nossa recomendação [activity lifecycle callback integration]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android), `openSession()` e `closeSession()` serão chamados automaticamente para cada atividade em seu app. Por padrão, as sessões no Android são abertas na primeira chamada para `openSession()` e são fechadas depois que um app fica fora do primeiro plano por mais de 10 segundos. Observe que chamar `closeSession()` não fecha uma sessão imediatamente. Em vez disso, ele fecha uma sessão em 10 segundos se o usuário não chamar `openSession()` (por exemplo, navegando para outra atividade) nesse intervalo.

Uma sessão do Android é encerrada após 10 segundos sem nenhuma comunicação do host do aplicativo. Isso significa que se um usuário sair do app e retornar 9 segundos depois, a mesma sessão será retomada. Note que, se uma sessão for fechada enquanto o usuário estiver com o aplicativo em segundo plano, esses dados podem não ser transferidos para o servidor até que o aplicativo seja aberto novamente.

{% alert note %}
Se precisar forçar uma nova sessão, basta mudar de usuário.
{% endalert %}

## Personalização do tempo limite da sessão
Para personalizar o tempo limite da sessão, adicione `com_braze_session_timeout` ao seu arquivo [`braze.xml`]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-brazexml). O valor mínimo para `NUMBER_OF_SECONDS_UNTIL_SESSION_TIMEOUT` é 1 segundo.

```xml
<!-- The length of time before a session times out in seconds. The session manager will "re-open" otherwise closed sessions if the call to StartSession comes within this interval. (default is 10) -->
<integer name="com_braze_session_timeout">NUMBER_OF_SECONDS_UNTIL_SESSION_TIMEOUT</integer>
```

## Teste de rastreamento de sessão

Para detectar sessões por meio de seu usuário, localize-o no dashboard e navegue até **App Usage (Uso do aplicativo** ) no perfil do usuário. Você pode confirmar que o rastreamento de sessão está funcionando verificando se a métrica da sessão aumenta quando você espera que isso aconteça.

![Um componente de perfil de usuário que mostra quantas sessões ocorreram, quando o app foi usado pela primeira vez e quando foi usado pela última vez.]({% image_buster /assets/img_archive/test_session.png %})

## Inscrever-se para receber atualizações de sessões

O SDK da Braze fornece um [`subscribeToSessionUpdates`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-session-updates.html) para ouvir as atualizações de sessão:

{% tabs %}
{% tab JAVA %}

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

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endtab %}
{% endtabs %}

