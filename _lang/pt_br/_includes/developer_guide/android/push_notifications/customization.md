{% multi_lang_include developer_guide/prerequisites/android.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Uso de um retorno de chamada para eventos push {#push-callback}

A Braze fornece um retorno de chamada [`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html) para quando notificações por push são recebidas, abertas ou descartadas. Recomenda-se colocar este retorno de chamada no seu `Application.onCreate()` para não perder nenhum evento que ocorra enquanto seu aplicativo não estiver em execução.

{% alert note %}
Se anteriormente usava um Receptor de Transmissão Personalizado para essa funcionalidade em seu aplicativo, você pode removê-lo com segurança em favor desta opção de integração.
{% endalert %}

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final BrazeNotificationPayload parsedData = event.getNotificationPayload();

  //
  // The type of notification itself
  //
  final boolean isPushOpenEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_OPENED;
  final boolean isPushReceivedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_RECEIVED;
  // Sent when a user has dismissed a notification
  final boolean isPushDeletedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_DELETED;

  //
  // Notification data
  //
  final String pushTitle = parsedData.getTitleText();
  final Long pushArrivalTimeMs = parsedData.getNotificationReceivedTimestampMillis();
  final String deeplink = parsedData.getDeeplink();

  //
  // Custom KVP data
  //
  final String myCustomKvp1 = parsedData.getBrazeExtras().getString("my first kvp");
  final String myCustomKvp2 = parsedData.getBrazeExtras().getString("my second kvp");
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).subscribeToPushNotificationEvents { event ->
    val parsedData = event.notificationPayload

    //
    // The type of notification itself
    //
    val isPushOpenEvent = event.eventType == BrazePushEventType.NOTIFICATION_OPENED
    val isPushReceivedEvent = event.eventType == BrazePushEventType.NOTIFICATION_RECEIVED
    // Sent when a user has dismissed a notification
    val isPushDeletedEvent = event.eventType == BrazePushEventType.NOTIFICATION_DELETED

    //
    // Notification data
    //
    val pushTitle = parsedData.titleText
    val pushArrivalTimeMs = parsedData.notificationReceivedTimestampMillis
    val deeplink = parsedData.deeplink

    //
    // Custom KVP data
    //
    val myCustomKvp1 = parsedData.brazeExtras.getString("my first kvp")
    val myCustomKvp2 = parsedData.brazeExtras.getString("my second kvp")
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Com os botões de ação de notificação, as intenções `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` são acionadas quando os botões com ações `opens app` ou `deep link` são clicados. A administração de deep linking e extras permanece a mesma. Os botões com ações do `close` não disparam as intenções do `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` e dispensam a notificação automaticamente.
{% endalert %}

{% alert important %}
Crie seu ouvinte de notificação por push em `Application.onCreate` para garantir que o ouvinte seja disparado depois que um usuário final tocar em uma notificação enquanto o app estiver em um estado finalizado.
{% endalert %}

## Personalização da exibição de notificações {#customization-display}

### Etapa 1: Crie sua fábrica de notificações personalizada

Em alguns cenários, você pode querer personalizar as notificações por push de maneiras que seriam complicadas ou não estariam disponíveis no lado do servidor. Para que você tenha controle total sobre a exibição de notificações, adicionamos a capacidade de definir seus próprios [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) para criar objetos de notificação para serem exibidos pelo Braze.

Se um `IBrazeNotificationFactory` personalizado for definido, o Braze chamará o método `createNotification()` de sua fábrica no recebimento do push antes que a notificação seja exibida ao usuário. O Braze transmitirá um `Bundle` contendo dados de envio do Braze e outro `Bundle` contendo pares de chave-valor personalizados enviados por meio do dashboard ou das APIs de envio de mensagens:

O Braze passará um arquivo [`BrazeNotificationPayload`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/index.html) contendo dados da notificação por push da Braze.

{% tabs %}
{% tab JAVA %}

```java
// Factory method implemented in your custom IBrazeNotificationFactory
@Override
public Notification createNotification(BrazeNotificationPayload brazeNotificationPayload) {
  // Example of getting notification title
  String title = brazeNotificationPayload.getTitleText();

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  String customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Factory method implemented in your custom IBrazeNotificationFactory
override fun createNotification(brazeNotificationPayload: BrazeNotificationPayload): Notification {
  // Example of getting notification title
  val title = brazeNotificationPayload.getTitleText()

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  val customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key")
}
```

{% endtab %}
{% endtabs %}

Você pode retornar `null` de seu método personalizado `createNotification()` para não mostrar a notificação, usar `BrazeNotificationFactory.getInstance().createNotification()` para obter nosso objeto padrão `notification` para esses dados e modificá-lo antes da exibição ou gerar um objeto `notification` completamente separado para exibição.

{% alert note %}
Para obter a documentação sobre as chaves de dados push da Braze, consulte o [SDK do Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html).
{% endalert %}

### Etapa 2: Defina sua fábrica de notificações personalizada

Para instruir a Braze a usar sua fábrica de notificações personalizada, use o método `setCustomBrazeNotificationFactory` para definir seu [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html):

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(IBrazeNotificationFactory brazeNotificationFactory);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(brazeNotificationFactory: IBrazeNotificationFactory)
```

{% endtab %}
{% endtabs %}

O local recomendado para definir seu `IBrazeNotificationFactory` personalizado é no método (não na atividade) do ciclo de vida do aplicativo `Application.onCreate()`. Isso permitirá que a fábrica de notificações seja definida corretamente sempre que o processo do seu app estiver ativo.

{% alert important %}
Criar sua própria notificação do zero é um caso de uso avançado e deve ser feito somente com testes completos e um profundo conhecimento da funcionalidade push da Braze. Por exemplo, é preciso garantir que a notificação por push seja aberta corretamente.
{% endalert %}

Para cancelar sua configuração personalizada [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) e retornar ao tratamento padrão do Braze para push, passe o endereço `null` para o nosso configurador de fábrica de notificações personalizadas:

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(null);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(null)
```

{% endtab %}
{% endtabs %}

## Renderização de texto multicolorido

Na versão 3.1.1 do SDK do Braze, o HTML pode ser enviado a um dispositivo para renderizar texto multicolorido em notificações por push.

![Uma mensagem push do Android "Multicolor Push test message" em que as letras são de cores diferentes, em itálico e com uma cor de fundo.]({% image_buster /assets/img/multicolor_android_push.png %}){: style="max-width:40%;"}

Esse exemplo é renderizado com o seguinte HTML:

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>

<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

Lembre-se de que o Android limita quais elementos e tags HTML são válidos em suas notificações por push. Por exemplo, `marquee` não é permitido.

{% alert important %}
A renderização de texto multicolorido é específica do dispositivo e pode não ser exibida com base no dispositivo ou na versão do Android.
{% endalert %}

Para renderizar texto multicolorido em uma notificação por push, você pode atualizar seu site `braze.xml` ou `BrazeConfig`:

{% tabs local %}
{% tab braze.xml %}
Adicione o seguinte em `braze.xml`:

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```
{% endtab %}

{% tab BrazeConfig %}
Adicione o seguinte em seu [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

{% subtabs local %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setPushHtmlRenderingEnabled(true)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setPushHtmlRenderingEnabled(true)
    .build()
Braze.configure(this, brazeConfig)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Tags HTML suportadas

Atualmente, o Google não lista as tags HTML compatíveis com o Android diretamente em sua documentação - essas informações só podem ser encontradas no [arquivo `Html.java` do repositório Git](https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/text/Html.java). Tenha isso em mente ao consultar a tabela a seguir, pois essas informações foram extraídas desse arquivo e as tags HTML suportadas podem estar sujeitas a alterações.

<table>
  <thead>
    <tr>
      <th>Categoria</th>
      <th>Tag HTML</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">Estilo básico de texto</td>
      <td><code>&lt;b&gt;</code>, <code>&lt;strong&gt;</code></td>
      <td>Texto em negrito</td>
    </tr>
    <tr>
      <td><code>&lt;i&gt;</code>, <code>&lt;em&gt;</code></td>
      <td>Texto em itálico</td>
    </tr>
    <tr>
      <td><code>&lt;u&gt;</code></td>
      <td>Texto sublinhado</td>
    </tr>
    <tr>
      <td><code>&lt;s&gt;</code>, <code>&lt;strike&gt;</code>, <code>&lt;del&gt;</code></td>
      <td>Texto riscado</td>
    </tr>
    <tr>
      <td><code>&lt;sup&gt;</code></td>
      <td>Texto sobrescrito</td>
    </tr>
    <tr>
      <td><code>&lt;sub&gt;</code></td>
      <td>Texto de inscrição</td>
    </tr>
    <tr>
      <td><code>&lt;tt&gt;</code></td>
      <td>Texto em monoespaço</td>
    </tr>
    <tr>
      <td rowspan="3">Tamanho/Fonte</td>
      <td><code>&lt;big&gt;</code>, <code>&lt;small&gt;</code></td>
      <td>Alterações no tamanho relativo do texto</td>
    </tr>
    <tr>
      <td><code>&lt;font color="..."&gt;</code></td>
      <td>Define a cor do primeiro plano</td>
    </tr>
    <tr>
      <td><code>&lt;span&gt;</code> (com CSS em linha)</td>
      <td>Estilos em linha (e.g., cor, plano de fundo)</td>
    </tr>
    <tr>
      <td rowspan="4">Parágrafo e bloco</td>
      <td><code>&lt;p&gt;</code>, <code>&lt;div&gt;</code></td>
      <td>Seções em nível de bloco</td>
    </tr>
    <tr>
      <td><code>&lt;br&gt;</code></td>
      <td>Quebra de linha</td>
    </tr>
    <tr>
      <td><code>&lt;blockquote&gt;</code></td>
      <td>Bloco citado</td>
    </tr>
    <tr>
      <td><code>&lt;ul&gt;</code> + <code>&lt;li&gt;</code></td>
      <td>Lista não ordenada com marcadores</td>
    </tr>
    <tr>
      <td>Títulos</td>
      <td><code>&lt;h1&gt;</code> - <code>&lt;h6&gt;</code></td>
      <td>Títulos (vários tamanhos)</td>
    </tr>
    <tr>
      <td rowspan="2">Links e imagens</td>
      <td><code>&lt;a href="..."&gt;</code></td>
      <td>Link clicável</td>
    </tr>
    <tr>
      <td><code>&lt;img src="..."&gt;</code></td>
      <td>Imagem inline</td>
    </tr>
    <tr>
      <td>Outros em linha</td>
      <td><code>&lt;em&gt;</code>, <code>&lt;strong&gt;</code>, <code>&lt;dfn&gt;</code>, <code>&lt;cite&gt;</code></td>
      <td>Sinônimos de itálico ou negrito</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Renderização de imagens em linha

### Como funciona?

Você pode exibir uma imagem maior em sua notificação por push do Android usando o push de imagem em linha. Com esse design, os usuários não precisarão expandir manualmente o push para ampliar a imagem. Ao contrário das notificações por push normais do Android, as imagens inline por push têm uma proporção de 3:2.

![]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="max-width:50%;"}

### Compatibilidade

Embora você possa enviar imagens em linha para qualquer dispositivo, os dispositivos e SDKs que não atenderem às versões mínimas exibirão uma imagem padrão. Para que as imagens em linha sejam exibidas corretamente, são necessários o SDK do Braze para Android v10.0.0+ e um dispositivo com Android M+. O SDK também deve estar ativado para que a imagem seja renderizada.

{% alert note %}
Os dispositivos que executam o Android 12 serão renderizados de forma diferente devido a alterações nos estilos de notificação por push personalizados.
{% endalert %}

### Envio de um push de imagem em linha

Ao criar uma mensagem push para Android, esse recurso está disponível no menu suspenso **Notification Type (Tipo de notificação** ).

![O editor de campanhas push mostra o local do menu suspenso "Notification Type" (acima da prévia padrão do push).]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})

## Configurações

Há muitas configurações avançadas disponíveis para notificações por push do Android enviadas pelo dashboard do Braze. Este artigo descreverá esses recursos e como usá-los com sucesso.

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

### ID da notificação {#notification-id}

Um **ID de Notificação** é um identificador único para uma categoria de mensagem de sua escolha que informa o serviço de envio de mensagens a respeitar apenas a mensagem mais recente desse ID. Definir um ID de notificação permite que você envie apenas a mensagem mais recente e relevante, em vez de uma pilha de mensagens desatualizadas e irrelevantes.

### Prioridade de entrega de mensagem do Firebase {#fcm-priority}

O campo [Prioridade de entrega de mensagem do Firebase](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) permite que você controle se um push é enviado com prioridade "normal" ou "alta" para o Firebase Cloud Messaging.

### Time to live (TTL) {#ttl}

O campo **TTL** permite que você defina um tempo personalizado para armazenar mensagens com o serviço de push de envio de mensagens. Os valores padrão para TTL são quatro semanas para FCM e 31 dias para ADM.

### Texto resumido {#summary-text}

O texto de resumo permite que você defina texto adicional na visualização expandida da notificação. Ele também serve como legenda para notificações com imagens.

![Uma mensagem do Android com o título "Este é o título da notificação." e o texto de resumo "Este é o texto de resumo da notificação."]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

O texto do resumo será exibido sob o corpo da mensagem na exibição expandida. 

![Uma mensagem do Android com o título "Este é o título da notificação." e o texto de resumo "Este é o texto de resumo da notificação."]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Para notificações por push que incluem imagens, o texto da mensagem será mostrado na exibição recolhida, enquanto o texto do resumo será exibido como a legenda da imagem quando a notificação for expandida. 

### URIs personalizados {#custom-uri}

O recurso **Custom URI** permite que você especifique um URL da Web ou um recurso do Android para navegar quando a notificação for clicada. Se nenhum URI personalizado for especificado, clicar na notificação leva os usuários para o seu app. Você pode usar o URI personalizado para deep link dentro do seu app e direcionar os usuários para recursos que existem fora do seu app. Isso pode ser especificado por meio da [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) ou de nosso dashboard, em **Advanced Settings (Configurações avançadas)**, no criador de mensagens push, conforme ilustrado:

![A configuração avançada de deep linking no criador do Braze.]({% image_buster /assets/img_archive/deep_link.png %})

### Prioridade de exibição de notificação {#notification-priority}

{% alert important %}
A configuração Prioridade de exibição de notificação não é mais usada em dispositivos com Android O ou mais recente. Para dispositivos mais novos, defina a prioridade por meio da [configuração do canal de notificação](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

O nível de prioridade de uma notificação por push afeta a forma como a notificação é exibida na bandeja de notificações em relação a outras notificações. Também pode afetar a velocidade e a maneira de entrega, pois mensagens normais e de baixa prioridade podem ser enviadas com uma latência ligeiramente maior ou agrupadas para preservar a vida útil da bateria, enquanto mensagens de alta prioridade são sempre enviadas imediatamente.

No Android O, a prioridade de notificação se tornou uma propriedade dos canais de notificação. Você precisará trabalhar com seu desenvolvedor para definir a prioridade de um canal durante sua configuração e, em seguida, usar o dashboard para selecionar o canal adequado ao enviar seus sons de notificação. Para dispositivos que executam versões do Android anteriores ao O, a especificação de um nível de prioridade para notificações do Android é possível por meio do dashboard do Braze e da API de envio de mensagens. 

Para enviar mensagens para toda a sua base de usuários com uma prioridade específica, recomendamos especificar indiretamente a prioridade por meio da [configuração do canal de envio de](https://developer.android.com/training/notify-user/channels#importance) mensagens (para direcionar dispositivos O+) *e* enviar a prioridade individual a partir do dashboard (para direcionar dispositivos <O).

Os níveis de prioridade que você pode definir em notificações por push do Android ou Fire OS são:

| Prioridade | Descrição/Utilização Pretendida | `priority` valor (para mensagens de API) |
|----------|--------------------------|-------------------------------------|
| Máx.      | Mensagens urgentes ou críticas de tempo | `2` |
| Alta     | Comunicação importante, como uma nova mensagem de um amigo | `1` |
| Padrão  | A maioria das notificações - use se sua mensagem não se enquadrar explicitamente em nenhum dos outros tipos de prioridade | `0` |
| Baixa      | Informações que você deseja que os usuários saibam, mas que não exigem ação imediata | `-1` |
| Mín.      | Informações contextuais ou de fundo. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para saber mais, consulte a documentação [de notificação](http://developer.android.com/design/patterns/notifications.html) do [Android](http://developer.android.com/design/patterns/notifications.html) do Google.

### Sons {#sounds}

No Android O, os sons de notificação se tornaram uma propriedade dos canais de notificação. Você precisará trabalhar com seu desenvolvedor para definir o som de um canal durante sua configuração e, em seguida, usar o dashboard para selecionar o canal adequado ao enviar suas notificações.

Para dispositivos executando versões do Android anteriores ao O, o Braze permite que você defina o som de uma mensagem push individual através do criador do dashboard. Você pode fazer isso especificando um recurso de som local no dispositivo (por exemplo, `android.resource://com.mycompany.myapp/raw/mysound`). Especificar "padrão" neste campo reproduzirá o som de notificação padrão no dispositivo. Isso pode ser especificado por meio da [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) ou do dashboard em **Configurações avançadas** no criador do push.

![A configuração avançada de som no criador do Braze.]({% image_buster /assets/img_archive/sound_android.png %})

Digite o URI completo do recurso de som (por exemplo, `android.resource://com.mycompany.myapp/raw/mysound`) no prompt do dashboard.

Para enviar mensagens a toda a sua base de usuários com um som específico, recomendamos especificar indiretamente o som por meio da [configuração do canal de envio de mensagens](https://developer.android.com/training/notify-user/channels) (para direcionar dispositivos O+) *e* enviar o som individual a partir do dashboard (para direcionar dispositivos <O).
