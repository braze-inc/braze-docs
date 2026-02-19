{% multi_lang_include developer_guide/prerequisites/android.md %}

## Gatilhos de mensagem

### Tipos de disparo

As mensagens no app são acionadas automaticamente quando o SDK registra um dos seguintes tipos de eventos personalizados: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` e `Push Click`. Observe que os gatilhos `Specific Purchase` e `Custom Event` também contêm filtros de propriedade robustos.

{% alert note %}
As mensagens no app não podem ser acionadas através da API ou por eventos da API—apenas eventos personalizados registrados pelo SDK. Para saber mais sobre registro, veja [Registro de Eventos Personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

### Semântica de entrega

Todas as mensagens no app elegíveis são entregues ao dispositivo de um usuário no início de sua sessão. Quando entregues, o SDK irá pré-carregar os ativos, para que estejam disponíveis no momento do acionamento, minimizando a latência de exibição. Se o evento de gatilho tiver mais de uma mensagem no app elegível, apenas a mensagem com a maior prioridade será entregue.

Para mais informações sobre a semântica de início de sessão do SDK, veja [Ciclo de Vida da Sessão]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android).

### Limite de taxa

Por padrão, limitamos a frequência das mensagens no app para uma vez a cada 30 segundos para garantir uma experiência de usuário de qualidade.

Para substituir esse valor, defina `com_braze_trigger_action_minimum_time_interval_seconds` no seu `braze.xml` via:

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## Pares de valores chave

Quando você cria uma campanha no Braze, pode definir pares chave-valor como `extras`, que o objeto de mensagens no app pode usar para enviar dados para seu app. Por exemplo:

{% tabs %}
{% tab JAVA %}
```java
Map<String, String> getExtras()
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endtab %}
{% endtabs %}

{% alert note %}
Para mais informações, consulte o [Documentação K](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721).
{% endalert %}

## Desabilitando gatilhos automáticos

Para evitar que mensagens no app sejam acionadas automaticamente:

1. Use sempre o inicializador de integração automática, que está habilitado por padrão a partir da versão `2.2.0`.
2. Defina o padrão da operação de mensagem no app como `DISCARD` adicionando a seguinte linha ao seu arquivo `braze.xml`.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

## Acionando mensagens manualmente

Por padrão, mensagens no app são acionadas automaticamente quando o SDK registra um evento personalizado. No entanto, você pode acionar manualmente uma mensagem usando os seguintes métodos.

### Usando um evento do lado do servidor

Para acionar uma mensagem no app usando um evento enviado pelo servidor, envie uma notificação push silenciosa para o dispositivo, que permite que um retorno de chamada de push personalizado registre um evento baseado no SDK. Esse evento então acionará a mensagem no app voltada para o usuário.

#### Etapa 1: Crie um retorno de chamada push para receber o push silencioso

Registre [seu retorno de chamada de push personalizado]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#push-callback) para escutar uma notificação push silenciosa específica.

No exemplo a seguir, dois eventos serão registrados para a mensagem no app ser entregue, um pelo servidor e um de dentro do seu retorno de chamada push personalizado. Para garantir que o mesmo evento não seja duplicado, o evento registrado a partir do seu retorno de chamada push deve seguir uma convenção de nomenclatura genérica, por exemplo, "evento de gatilho de mensagem no app", e não o mesmo nome do evento enviado pelo servidor. Se isso não for feito, a segmentação e os dados de usuários podem ser afetados por eventos duplicados sendo registrados para uma única ação do usuário.

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

#### Etapa 2: Crie uma campanha de push

Crie uma [campanha de push silenciosa]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) acionada via o evento enviado pelo servidor.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

A campanha push deve incluir extras de pares de chave-valor que indiquem que esta campanha push é enviada para registrar um evento personalizado do SDK. Este evento será usado para disparar a mensagem no app.

![Dois conjuntos de pares chave-valor: IS_SERVER_EVENT definido como "true", e CAMPAIGN_NAME definido como "nome da campanha de exemplo".]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

O código de exemplo de retorno de chamada push anterior reconhece os pares de chave/valor e registra o evento personalizado apropriado do SDK.

Caso você queira incluir alguma propriedade de evento para anexar ao seu evento "in-app message trigger", passe-as nos pares de chave/valor da carga útil do push. Neste exemplo, foi incluído o nome da campanha da mensagem no app subsequente. Seu retorno de chamada de push personalizado pode então passar o valor como o parâmetro da propriedade do evento ao registrar o evento personalizado.

#### Etapa 3: Crie uma campanha de mensagem no app

Crie sua campanha de mensagem no app visível para o usuário no dashboard da Braze. Esta campanha deve ter uma entrega baseada em ação e ser acionada a partir do evento personalizado registrado dentro do seu retorno de chamada push personalizado.

No exemplo a seguir, a mensagem no app específica a ser acionada foi configurada enviando a propriedade do evento como parte do push silencioso inicial.

![Uma campanha de entrega baseada em ação onde uma mensagem no app será disparada quando "campaign_name" for igual a "exemplo de nome da campanha IAM."]({% image_buster /assets/img_archive/iam_event_trigger.png %})

Se um evento enviado pelo servidor for registrado enquanto o app não estiver em primeiro plano, o evento será registrado, mas a mensagem no app não será exibida. Caso você queira que o evento seja postergado até que o aplicativo esteja em primeiro plano, uma verificação deve ser incluída no seu receptor de push personalizado para dispensar ou postergar o evento até que o app tenha entrado em primeiro plano.

### Exibindo uma mensagem pré-definida

Para exibir manualmente uma mensagem no app pré-definida, use o seguinte método:

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

### Exibindo uma mensagem em tempo real 

Você também pode criar e exibir mensagens locais no app em tempo real, usando as mesmas opções de personalização disponíveis no dashboard. Para fazer isso:

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
