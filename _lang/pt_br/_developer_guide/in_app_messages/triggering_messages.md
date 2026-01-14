---
nav_title: Gatilhos de mensagens
article_title: Envio de mensagens no app por meio do SDK do Braze
page_order: 0.2
description: "Saiba como disparar mensagens no app por meio do SDK do Braze."
platform: 
  - Android
  - FireOS
  - Swift
  - Web
---

# Envio de mensagens no app

> Saiba como disparar mensagens no app por meio do SDK do Braze.

## Disparos e envio de mensagens

As mensagens no app são disparadas quando o SDK registra um dos seguintes tipos de eventos personalizados: `Session Start`, `Push Click`, `Any Purchase`, `Specific Purchase`,e `Custom Event` (os dois últimos contêm filtros de propriedade robustos).

No início da sessão de um usuário, o Braze entregará todas as mensagens elegíveis no app para o dispositivo e, ao mesmo tempo, fará a pré-busca de ativos para minimizar a latência da exibição. Se o evento de gatilho tiver mais de uma mensagem elegível no app, somente a mensagem com a prioridade mais alta será entregue. Para saber mais, consulte [Ciclo de vida da sessão]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/#session-lifecycle).

{% alert note %}
As mensagens no app não podem ser disparadas pela API ou por eventos da API - somente eventos personalizados registrados pelo SDK. Para saber mais sobre registro, consulte [Registro de eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

## Pares de valores chave

Ao criar uma campanha no Braze, você pode definir pares de valores-chave como `extras`, que o objeto de mensagens no app pode usar para enviar dados ao seu aplicativo.

{% tabs %}
{% tab Android %}
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
Para saber mais, consulte o [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721).
{% endalert %}
{% endtab %}

{% tab swift %}
O exemplo a seguir usa lógica personalizada para definir a apresentação de uma mensagem no app com base em seus pares de valores-chave em `extras`. Para obter um exemplo completo de personalização, confira [nosso app de amostra](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

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
{% endtabs %}

## Desativação de disparos automáticos

Por padrão, as mensagens no app são disparadas automaticamente. Para desativar isso:

{% tabs %}
{% tab Android %}
1. Verifique se está usando o inicializador de integração automática, que é ativado por padrão nas versões `2.2.0` e posteriores.
2. Defina o padrão da operação de mensagem no app como `DISCARD` adicionando a seguinte linha ao seu arquivo `braze.xml`.
    ```xml
    <string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
    ```
{% endtab %}

{% tab swift %}
1. Implemente o delegado `BrazeInAppMessageUIDelegate` em seu app. Para obter um passo a passo completo, consulte [Tutorial: UI de mensagens no app](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
2. Atualize seu método delegado `inAppMessage(_:displayChoiceForMessage:)` para retornar `.discard`.
{% endtab %}

{% tab web %}
Remova a chamada para `braze.automaticallyShowInAppMessages()` em seu snippet de carregamento e, em seguida, crie uma lógica personalizada para lidar com a exibição ou não de uma mensagem no app.

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
Se você ligar para `braze.showInAppMessage` sem remover `braze.automaticallyShowInAppMessages()`, as mensagens poderão ser exibidas duas vezes.
{% endalert %}
{% endtab %}

{% tab Unity %}
{% subtabs %}
{% subtab Android %}
No Android, desmarque a opção **Exibir automaticamente mensagens no app** no editor de configuração do Braze. Como alternativa, você pode definir `com_braze_inapp_show_inapp_messages_automatically` como `false` no `braze.xml` de seu projeto Unity.

A operação inicial de exibição de mensagens no app pode ser definida na configuração do Braze usando a "Operação de exibição inicial do gerenciador de mensagens no app".
{% endsubtab %}

{% subtab iOS %}
Para iOS, defina os ouvintes de objetos de jogo no editor de configuração do Braze e certifique-se de que **Braze Displays In-App Messages** não esteja selecionado.

A operação inicial de exibição de mensagens no app pode ser definida na configuração do Braze usando a "Operação de exibição inicial do gerenciador de mensagens no app".
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Substituir o limite de frequência padrão

Por padrão, você pode enviar uma mensagem no app uma vez a cada 30 segundos. Para substituir isso, adicione a seguinte propriedade ao seu arquivo de configuração antes que a instância do Braze seja inicializada. Esse valor será usado como o novo limite de frequência em segundos.

{% tabs %}
{% tab Android %}
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

{% tab web %}
```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```
{% endtab %}
{% endtabs %}

## Envio manual de mensagens

Por padrão, as mensagens no app são disparadas automaticamente quando o SDK registra um evento personalizado. No entanto, além disso, você pode disparar mensagens manualmente usando os seguintes métodos.

### Usando um evento no lado do servidor

{% tabs %}
{% tab Android %}
Para disparar uma mensagem no app usando um evento enviado pelo servidor, envie uma notificação por push silenciosa para o dispositivo, o que permite que um retorno de chamada por push personalizado registre um evento baseado no SDK. Esse evento disparará a mensagem no app voltada para o usuário.

#### Etapa 1: Crie um retorno de chamada push para receber o push silencioso

Registre seu retorno de chamada de push personalizado para ouvir uma notificação por push silenciosa específica. Para saber mais, consulte [Integração push padrão do Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback).

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

![Dois conjuntos de pares chave-valor: IS_SERVER_EVENT definido como "true" e CAMPAIGN_NAME definido como "example campaign name".]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

O código de exemplo de retorno de chamada push anterior reconhece os pares de chave/valor e registra o evento personalizado apropriado do SDK.

Caso você queira incluir alguma propriedade de evento para anexar ao seu evento "in-app message trigger", passe-as nos pares de chave/valor da carga útil do push. Neste exemplo, foi incluído o nome da campanha da mensagem no app subsequente. Seu retorno de chamada de push personalizado pode então passar o valor como o parâmetro da propriedade do evento ao registrar o evento personalizado.

#### Etapa 3: Crie uma campanha de mensagem no app

Crie sua campanha de mensagem no app visível para o usuário no dashboard da Braze. Esta campanha deve ter uma entrega baseada em ação e ser acionada a partir do evento personalizado registrado dentro do seu retorno de chamada push personalizado.

No exemplo a seguir, a mensagem no app específica a ser acionada foi configurada enviando a propriedade do evento como parte do push silencioso inicial.

![Uma campanha de entrega baseada em ação em que uma mensagem no app será disparada quando "campaign_name" for igual a "IAM campaign name example".]({% image_buster /assets/img_archive/iam_event_trigger.png %})

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

![Uma campanha de mensagens no app com entrega baseada em ação que será entregue aos usuários cujos perfis de usuário tenham o evento personalizado "server_event".]({% image_buster /assets/img_archive/iosServerSentPush.png %})

A campanha de push precisa incluir extras de pares chave-valor, que indicam que esta campanha de push é enviada para registrar um evento personalizado do SDK. Este evento será usado para disparar a mensagem no app.

![Uma campanha de mensagem no app de entrega baseada em ação que possui dois pares chave-valor. "CAMPAIGN_NAME" definido como "Exemplo de nome de mensagem no app" e "IS_SERVER_EVENT" definido como "true".]({% image_buster /assets/img_archive/iOSServerPush.png %})

O código dentro do método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` verifica a chave `IS_SERVER_EVENT` e registra um evento personalizado do SDK se estiver presente.

Você pode alterar o nome do evento ou as propriedades do evento enviando o valor desejado dentro do par chave-valor extras da carga útil push. Ao registrar o evento personalizado, esses extras podem ser usados como parâmetro do nome do evento ou como uma propriedade do evento.

#### Etapa 3: Crie uma campanha de mensagem no app

Crie sua campanha de mensagem no app visível para o usuário no dashboard da Braze. Esta campanha deve ter uma entrega baseada em ação e ser acionada a partir do evento personalizado registrado dentro do método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

No exemplo a seguir, a mensagem no app específica a ser acionada foi configurada enviando a propriedade do evento como parte do push silencioso inicial.

![Uma campanha de mensagens no app com entrega baseada em ação que será entregue aos usuários que executarem o evento personalizado "Disparo de mensagem no app", em que "campaign_name" é igual a "Exemplo de nome de campanha do IAM".]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Note que essas mensagens no app só serão disparadas se o push silencioso for recebido enquanto o aplicativo estiver em primeiro plano.
{% endalert %}
{% endtab %}

{% tab web %}
No momento, o SDK do Braze não oferece suporte ao envio manual de mensagens usando eventos do lado do servidor.
{% endtab %}
{% endtabs %}

### Exibição de uma mensagem predefinida

Para exibir manualmente uma mensagem no app predefinida, use o seguinte método:

{% tabs %}
{% tab Android %}
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

{% tab web %}
```javascript
braze.requestInAppMessageDisplay();
```
{% endtab %}
{% endtabs %}

### Envio de mensagens em tempo real 

Você também pode criar e exibir mensagens locais no app em tempo real, usando as mesmas opções de personalização disponíveis no dashboard. Para isso:

{% tabs %}
{% tab Android %}
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
Chame manualmente o método [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) em seu site `inAppMessagePresenter`. Por exemplo:

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
Ao criar sua própria mensagem no app, você aceita qualquer rastreamento de análise de dados e terá que lidar manualmente com o registro de cliques e impressões usando o site `message.context`.
{% endalert %}
{% endtab %}

{% tab web %}
```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```
{% endtab %}

{% tab Unity %}
Para exibir a próxima mensagem da pilha, use o método `DisplayNextInAppMessage()`. As mensagens serão salvas nessa pilha se `DISPLAY_LATER` ou `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` for escolhido como a ação de exibição de mensagens no app.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```
{% endtab %}
{% endtabs %}

## Mensagens de intenção de saída pela internet

As mensagens de intenção de saída são mensagens no app não disruptivas usadas para comunicar informações importantes aos visitantes antes que eles saiam do seu site.

Para configurar disparos para esses tipos de mensagens no Web SDK, implemente uma biblioteca de intenção de saída em seu site (como [a biblioteca de código aberto do ouibounce](https://github.com/carlsednaoui/ouibounce)) e use o código a seguir para registrar `'exit intent'` como um evento personalizado no Braze. Agora, suas futuras campanhas de mensagens no app podem usar esse tipo de mensagem como um disparador de evento personalizado.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
