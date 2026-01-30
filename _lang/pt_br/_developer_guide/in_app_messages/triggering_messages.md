---
nav_title: Mensagens de gatilho
article_title: Acione mensagens no app através do SDK Braze
page_order: 0.2
description: "Aprenda como acionar mensagens no app através do SDK Braze."
platform: 
  - Android
  - FireOS
  - Swift
  - Web
---

# Acione mensagens no app

> Aprenda como acionar mensagens no app através do SDK Braze.

## Gatilhos e entrega de mensagens

As mensagens no app são acionadas quando o SDK registra um dos seguintes tipos de eventos personalizados: `Session Start`, `Push Click`, `Any Purchase`, `Specific Purchase` e `Custom Event` (os dois últimos contendo filtros de propriedade robustos).

No início da sessão de um usuário, o Braze entregará todas as mensagens no app elegíveis para seu dispositivo, enquanto simultaneamente pré-carrega ativos para minimizar a latência de exibição. Se o evento de gatilho tiver mais de uma mensagem no app elegível, apenas a mensagem com a maior prioridade será entregue. Para mais informações, veja [Lifecycle da Sessão]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/#about-the-session-lifecycle).

{% alert note %}
Mensagens no app não podem ser acionadas através da API ou por eventos da API—apenas eventos personalizados registrados pelo SDK. Para saber mais sobre registro, veja [Registro de Eventos Personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

## Pares de valores chave

Quando você cria uma campanha no Braze, pode definir pares chave-valor como `extras`, que o objeto de mensagens no app pode usar para enviar dados para seu app.

{% tabs %}
{% tab web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}
```java
Map<String, String> getExtras()
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Para mais informações, consulte o [Documentação K](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721).
{% endalert %}
{% endtab %}

{% tab swift %}
O seguinte exemplo usa lógica personalizada para definir a apresentação de uma mensagem no app com base em seus pares chave-valor em `extras`. Para um exemplo completo de personalização, confira [nosso app de exemplo](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

{% subtabs %}
{% subtab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Desabilitando gatilhos automáticos

Por padrão, as mensagens no app são acionadas automaticamente. Para desabilitar isso:

{% tabs %}

{% tab web %}
Remova a chamada para `braze.automaticallyShowInAppMessages()` dentro do seu snippet de carregamento, e então crie lógica personalizada para lidar com a exibição ou não exibição de uma mensagem no app.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the display capabilities in Braze, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
Se você chamar `braze.showInAppMessage` sem remover `braze.automaticallyShowInAppMessages()`, as mensagens podem ser exibidas duas vezes.
{% endalert %}

Para um controle mais avançado sobre o tempo das mensagens, incluindo adiamento e restauração de mensagens acionadas, consulte nosso [Tutorial: Adiar e restaurar mensagens disparadas]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages).
{% endtab %}

{% tab android %}
1. Implemente o [`IInAppMessageManagerListener`](https://www.braze.com/docs/developer_guide/in_app_messages/customization/?sdktab=android&tab=global%20listener#android_step-1-implement-the-custom-manager-listener) para definir um ouvinte personalizado.
2. Atualize seu método [`beforeInAppMessageDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-displayed.html) para retornar [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-c-a-r-d/index.html).

Para um controle mais avançado sobre o tempo das mensagens, incluindo exibição posterior e reencaminhamento, consulte nossa página [Personalizando Mensagens](https://www.braze.com/docs/developer_guide/in_app_messages/customization/?tab=global%20listener&subtab=kotlin#android_step-2-instruct-braze-to-use-the-custom-manager-listener).
{% endtab %}

{% tab swift %}
1. Implemente o delegado `BrazeInAppMessageUIDelegate` em seu app. Para um guia completo, consulte [Tutorial: UI de Mensagem no App](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
2. Atualize seu método delegado `inAppMessage(_:displayChoiceForMessage:)` para retornar `.discard`.

Para um controle mais avançado sobre o tempo das mensagens, incluindo adiamento e restauração de mensagens acionadas, consulte nosso [Tutorial: Adiar e restaurar mensagens disparadas]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages).
{% endtab %}

{% tab flutter %}
1. Verifique se você está usando o inicializador de integração automática, que é habilitado por padrão nas versões `2.2.0` e posteriores.
2. Defina o padrão da operação de mensagem no app como `DISCARD` adicionando a seguinte linha ao seu arquivo `braze.xml`.
    ```xml
    <string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
    ```
{% endtab %}

{% tab unity %}
{% subtabs %}
{% subtab Android %}
Para Android, desmarque **Exibir Automaticamente Mensagens no App** no editor de configuração do Braze. Alternativamente, você pode definir `com_braze_inapp_show_inapp_messages_automatically` para `false` no `braze.xml` do seu projeto Unity.

A operação inicial de exibição de mensagem no app pode ser configurada no Braze usando a "Operação Inicial de Exibição do Gerenciador de Mensagens no App".
{% endsubtab %}

{% subtab iOS %}
Para iOS, defina ouvintes de objetos de jogo no editor de configuração do Braze e certifique-se de que **Braze Exibe Mensagens no App** não esteja selecionado.

A operação inicial de exibição de mensagem no app pode ser configurada no Braze usando a "Operação Inicial de Exibição do Gerenciador de Mensagens no App".
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Substituindo o limite de frequência padrão

Por padrão, você pode enviar uma mensagem no app uma vez a cada 30 segundos. Para substituir isso, adicione a seguinte propriedade ao seu arquivo de configuração antes que a instância do Braze seja inicializada. Este valor será usado como o novo limite de frequência em segundos.

{% tabs %}
{% tab web %}
```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```
{% endtab %}

{% tab android %}
```xml
<integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
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
{% endsubtab %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Disparando mensagens manualmente

Por padrão, mensagens no app são disparadas automaticamente quando o SDK registra um evento personalizado. No entanto, além disso, você pode disparar mensagens manualmente usando os seguintes métodos.

### Usando um evento do lado do servidor

{% tabs %}
{% tab web %}
Neste momento, o SDK Web Braze não suporta a ativação manual de mensagens usando eventos do lado do servidor.
{% endtab %}

{% tab android %}
Para disparar uma mensagem no app usando um evento enviado pelo servidor, envie uma notificação por push silenciosa para o dispositivo, o que permite que um retorno de chamada personalizado registre um evento baseado no SDK. Esse evento então disparará a mensagem no app voltada para o usuário.

#### Etapa 1: Crie um retorno de chamada push para receber o push silencioso

Registre seu retorno de chamada de push personalizado para ouvir uma notificação por push silenciosa específica. Para saber mais, consulte [Configuração de notificações por push]({{site.baseurl}}/developer_guide/push_notifications#android_setting-up-push-notifications).

Dois eventos serão registrados para que a mensagem no app seja entregue, um pelo servidor e outro de dentro do seu retorno de chamada push personalizado. Para garantir que o mesmo evento não seja duplicado, o evento registrado a partir do seu retorno de chamada push deve seguir uma convenção de nomenclatura genérica, por exemplo, "evento de gatilho de mensagem no app", e não o mesmo nome do evento enviado pelo servidor. Se isso não for feito, a segmentação e os dados de usuários podem ser afetados por eventos duplicados sendo registrados para uma única ação do usuário.

{% subtabs %}
{% subtab JAVA %}

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

{% endsubtab %}
{% subtab KOTLIN %}

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

{% endsubtab %}
{% endsubtabs %}

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

![Uma campanha de entrega baseada em ação onde uma mensagem no app será disparada quando "campaign_name" for igual a "exemplo de nome da campanha IAM".]({% image_buster /assets/img_archive/iam_event_trigger.png %})

Se um evento enviado pelo servidor for registrado enquanto o app não estiver em primeiro plano, o evento será registrado, mas a mensagem no app não será exibida. Caso você queira que o evento seja postergado até que o aplicativo esteja em primeiro plano, uma verificação deve ser incluída no seu receptor de push personalizado para dispensar ou postergar o evento até que o app tenha entrado em primeiro plano.
{% endtab %}

{% tab swift %}
#### Etapa 1: Lidar com push silencioso e pares chave-valor

Implemente a seguinte função e chame-a dentro do [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`: método](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/):

{% subtabs %}
{% subtab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endsubtab %}
{% endsubtabs %}

Quando o push silencioso é recebido, um evento registrado pelo SDK "disparar mensagem no app" será registrado no perfil do usuário. 

{% alert important %}
Devido a uma mensagem por push ser usada para registrar um evento personalizado registrado pelo SDK, a Braze precisará armazenar um token por push para cada usuário para ativar essa solução. Para usuários de iOS, a Braze só armazenará um token a partir do momento em que o usuário receber o prompt de push do sistema operacional. Antes disso, o usuário não estará acessível usando push, e a solução anterior não será possível.
{% endalert %}

#### Etapa 2: Crie uma campanha de push silenciosa

Crie uma [campanha de push silenciosa]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift), que é disparada pelo evento enviado pelo servidor. 

![Uma campanha de mensagem no app baseada em ação que será entregue aos usuários cujos perfis de usuário têm o evento personalizado "server_event".]({% image_buster /assets/img_archive/iosServerSentPush.png %})

A campanha de push precisa incluir extras de pares chave-valor, que indicam que esta campanha de push é enviada para registrar um evento personalizado do SDK. Este evento será usado para disparar a mensagem no app.

![Uma campanha de mensagem no app baseada em ação que tem dois pares chave-valor. "CAMPAIGN_NAME" definido como "exemplo de nome da mensagem no app", e "IS_SERVER_EVENT" definido como "true".]({% image_buster /assets/img_archive/iOSServerPush.png %})

O código dentro do método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` verifica a chave `IS_SERVER_EVENT` e registra um evento personalizado do SDK se estiver presente.

Você pode alterar o nome do evento ou as propriedades do evento enviando o valor desejado dentro do par chave-valor extras da carga útil push. Ao registrar o evento personalizado, esses extras podem ser usados como parâmetro do nome do evento ou como uma propriedade do evento.

#### Etapa 3: Crie uma campanha de mensagem no app

Crie sua campanha de mensagem no app visível para o usuário no dashboard da Braze. Esta campanha deve ter uma entrega baseada em ação e ser acionada a partir do evento personalizado registrado dentro do método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

No exemplo a seguir, a mensagem no app específica a ser acionada foi configurada enviando a propriedade do evento como parte do push silencioso inicial.

![Uma campanha de mensagem no app baseada em ação que será entregue aos usuários que realizam o evento personalizado "Disparar mensagem no app" onde "campaign_name" é igual a "Exemplo de Nome da Campanha IAM".]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Note que essas mensagens no app só serão disparadas se o push silencioso for recebido enquanto o aplicativo estiver em primeiro plano.
{% endalert %}
{% endtab %}
{% endtabs %}

### Exibindo uma mensagem pré-definida

Para exibir manualmente uma mensagem no app pré-definida, use o seguinte método:

{% tabs %}
{% tab web %}
```javascript
braze.requestInAppMessageDisplay();
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```
{% endtab %}
{% endtabs %}

### Exibindo uma mensagem em tempo real 

Você também pode criar e exibir mensagens locais no app em tempo real, usando as mesmas opções de personalização disponíveis no dashboard. Para fazer isso:

{% tabs %}
{% tab web %}
```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Não exiba mensagens no app quando o teclado virtual estiver exibido na tela, pois a renderização é indefinida nessa circunstância.
{% endalert %}
{% endtab %}

{% tab swift %}
Chame manualmente o método [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) em seu `inAppMessagePresenter`. Por exemplo:

{% subtabs %}
{% subtab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

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

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
Ao criar sua própria mensagem no app, você opta por não participar de qualquer rastreamento de análise e terá que gerenciar manualmente o registro de cliques e impressões usando seu `message.context`.
{% endalert %}
{% endtab %}

{% tab unity %}
Para exibir a próxima mensagem na pilha, use o método `DisplayNextInAppMessage()`. As mensagens serão salvas nesta pilha se `DISPLAY_LATER` ou `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` forem escolhidos como a ação de exibição da mensagem no app.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```
{% endtab %}
{% endtabs %}

## Mensagens de intenção de saída para a Web

Mensagens de intenção de saída são mensagens no app não disruptivas usadas para comunicar informações importantes aos visitantes antes que eles deixem seu site.

Para configurar disparadores para esses tipos de mensagem no Web SDK, implemente uma biblioteca de intenção de saída em seu site (como [a biblioteca de código aberto do ouibounce](https://github.com/carlsednaoui/ouibounce)), e então use o seguinte código para registrar `'exit intent'` como um evento personalizado no Braze. Agora suas futuras campanhas de mensagens no app podem usar esse tipo de mensagem como um disparador de evento personalizado.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
