---
nav_title: Envio de mensagens no app
article_title: Entrega de mensagem no app para Android e FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Este artigo de referência aborda o envio de mensagens no app para Android e FireOS, listando diferentes tipos de disparo, semântica de entrega e etapas de disparo de eventos."
channel:
  - in-app messages

---

# Envio de mensagens no app

> Este artigo de referência aborda o envio de mensagens no app para Android e FireOS, listando diferentes tipos de disparo, semântica de entrega e etapas de disparo de eventos.

## Tipos de disparo

Nosso produto de mensagem no app permite que você dispare uma exibição de mensagem no app devido a vários tipos diferentes de eventos: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` e `Push Click`. Além disso, os disparos `Specific Purchase` e `Custom Event` contêm filtros de propriedade robustos.

{% alert note %}
As mensagens no app disparadas só funcionam com eventos personalizados registrados por meio do SDK da Braze. As mensagens no app não podem ser disparadas por meio da API ou por eventos da API (como eventos de compra). Certifique-se de verificar como [registrar eventos personalizados]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/).
{% endalert %}

## Semântica de entrega

Todas as mensagens no app para as quais um usuário é elegível são entregues ao dispositivo do usuário no [início da sessão]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#session-lifecycle). Após a entrega, o SDK fará a pré-busca de ativos para que estejam disponíveis imediatamente no momento do disparo, minimizando a latência da exibição.

Quando um evento de gatilho tiver mais de uma mensagem no app elegível associada a ele, só será entregue a mensagem no app com a prioridade mais alta.

Pode haver alguma latência para mensagens no app que são exibidas imediatamente na entrega (como início de sessão e clique no push) devido aos recursos não serem pré-carregados.

## Intervalo de tempo mínimo entre disparos

Por padrão, limitamos a frequência das mensagens no app para uma vez a cada 30 segundos para garantir uma experiência de usuário de qualidade.

Para substituir esse valor, defina `com_braze_trigger_action_minimum_time_interval_seconds` no seu `braze.xml` via:

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## Disparo de evento do lado do servidor

Por padrão, as mensagens no app são disparadas por eventos personalizados registrados pelo SDK. Se você quiser disparar mensagens no app por eventos enviados pelo servidor, também é possível.

Para ativar esse recurso, um push silencioso é enviado para o dispositivo, o que permite que um retorno de chamada de push personalizado registre um evento baseado em SDK. Posteriormente, esse evento do SDK disparará a mensagem no app voltada para o usuário.

### Etapa 1: Crie um retorno de chamada push para receber o push silencioso

Registre seu retorno de chamada de push personalizado para ouvir uma notificação por push silenciosa específica. Para saber mais, consulte [Integração push padrão do Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback).

Dois eventos serão registrados para que a mensagem no app seja entregue, um pelo servidor e outro de dentro do seu retorno de chamada push personalizado. Para garantir que o mesmo evento não seja duplicado, o evento registrado a partir do seu retorno de chamada push deve seguir uma convenção de nomenclatura genérica, por exemplo, "evento de gatilho de mensagem no app", e não o mesmo nome do evento enviado pelo servidor. Se isso não for feito, a segmentação e os dados de usuários podem ser afetados por eventos duplicados sendo registrados para uma única ação do usuário.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endtab %}
{% endtabs %}

### Etapa 2: Crie uma campanha de push

Crie uma [campanha de push silenciosa]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/) acionada via o evento enviado pelo servidor.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

A campanha push deve incluir extras de pares de chave-valor que indiquem que esta campanha push é enviada para registrar um evento personalizado do SDK. Este evento será usado para disparar a mensagem no app.

![Dois conjuntos de pares chave-valor: IS_SERVER_EVENT definido como "true" e CAMPAIGN_NAME definido como "example campaign name".]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

O código de exemplo de retorno de chamada push anterior reconhece os pares de chave/valor e registra o evento personalizado apropriado do SDK.

Caso você queira incluir alguma propriedade de evento para anexar ao seu evento "in-app message trigger", passe-as nos pares de chave/valor da carga útil do push. Neste exemplo, foi incluído o nome da campanha da mensagem no app subsequente. Seu retorno de chamada de push personalizado pode então passar o valor como o parâmetro da propriedade do evento ao registrar o evento personalizado.

### Etapa 3: Crie uma campanha de mensagem no app

Crie sua campanha de mensagem no app visível para o usuário no dashboard da Braze. Esta campanha deve ter uma entrega baseada em ação e ser acionada a partir do evento personalizado registrado dentro do seu retorno de chamada push personalizado.

No exemplo a seguir, a mensagem no app específica a ser acionada foi configurada enviando a propriedade do evento como parte do push silencioso inicial.

![Uma campanha de entrega baseada em ação em que uma mensagem no app será disparada quando "campaign_name" for igual a "IAM campaign name example".]({% image_buster /assets/img_archive/iam_event_trigger.png %})

Se um evento enviado pelo servidor for registrado enquanto o app não estiver em primeiro plano, o evento será registrado, mas a mensagem no app não será exibida. Caso você queira que o evento seja postergado até que o aplicativo esteja em primeiro plano, uma verificação deve ser incluída no seu receptor de push personalizado para dispensar ou postergar o evento até que o app tenha entrado em primeiro plano.

## Mensagens locais no app

Mensagens no app podem ser criadas dentro do app e exibidas localmente em tempo real. Todas as opções de personalização disponíveis no dashboard também estão disponíveis localmente. Isso é particularmente útil para exibir mensagens que você deseja disparar no app em tempo real.

{% tabs %}
{% tab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endtab %}
{% endtabs %}

{% alert important %}
Não exiba mensagens no app quando o teclado virtual estiver exibido na tela, pois a renderização é indefinida nessa circunstância.
{% endalert %}

### Acionando manualmente a exibição de mensagem no app

O seguinte método exibirá manualmente sua mensagem no app:

{% tabs %}
{% tab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endtab %}
{% endtabs %}

