{% multi_lang_include developer_guide/prerequisites/web.md %}

## Envio de mensagens

## Tipos de disparo

As mensagens no app são disparadas automaticamente quando o SDK registra um dos seguintes tipos de eventos personalizados: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, e `Push Click`. Note que os disparadores `Specific Purchase` e `Custom Event` também contêm filtros de propriedade robustos.

{% alert note %}
As mensagens no app não podem ser disparadas pela API ou por eventos da API - somente eventos personalizados registrados pelo SDK. Para saber mais sobre registro, consulte [Registro de eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

### Semântica de entrega

Todas as mensagens no app elegíveis são enviadas para o dispositivo do usuário no início da sessão. Quando entregue, o SDK fará a pré-busca de ativos para que eles estejam disponíveis no momento do disparo, minimizando a latência da exibição. Se o evento de gatilho tiver mais de uma mensagem elegível no app, somente a mensagem com a prioridade mais alta será entregue.

Para saber mais sobre a semântica de início de sessão do SDK, consulteSession[Lifecycle (Ciclo de vida]({{site.baseurl}}/developer_guide/platform_integration_guides/analytics/tracking_sessions/) da sessão).

### Limites de taxa

Por padrão, você pode enviar uma mensagem no app uma vez a cada 30 segundos.

Para substituir isso, adicione a seguinte propriedade à sua configuração do Braze - antes que a instância do Braze seja inicializada. Você pode defini-lo como qualquer número inteiro positivo, que representa o intervalo de tempo mínimo em segundos. Por exemplo:

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## Pares de valores chave

Ao criar uma campanha no Braze, você pode definir pares de valores-chave como `extras`, que o objeto de mensagens no app pode usar para enviar dados ao seu aplicativo. Por exemplo:

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

## Desativação de disparos automáticos

Para evitar que as mensagens no app sejam disparadas automaticamente:

Remova a chamada para `braze.automaticallyShowInAppMessages()` em seu snippet de carregamento e, em seguida, crie uma lógica personalizada para lidar com a exibição ou não de mensagens no app.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the Braze built-in display capabilities, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
Se você não remover `braze.automaticallyShowInAppMessages()` do seu site e depois chamar `braze.showInAppMessage`, a mensagem poderá ser exibida várias vezes.
{% endalert %}

O parâmetro `inAppMessage` será uma subclasse [`braze.InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) ou um objeto [`braze.ControlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.controlmessage.html), tendo cada um vários métodos de inscrição de eventos de ciclo de vida. Consulte a [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) para a documentação completa.

Apenas uma [`Modal`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=modal&sdktab=web) ou [`Full`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=full&sdktab=web) mensagem no app pode ser exibida por vez. Se você tentar mostrar um segundo modal ou uma mensagem completa enquanto outra já estiver sendo exibida, `braze.showInAppMessage` retornará falso, e a segunda mensagem não será exibida.

## Envio manual de mensagens

### Envio de mensagens em tempo real

Mensagens no app também podem ser criadas dentro do seu site e exibidas localmente em tempo real. Todas as opções de personalização disponíveis no dashboard também estão disponíveis localmente. Isso é particularmente útil para exibir mensagens que você deseja disparar no app em tempo real. No entanto, a análise de dados dessas mensagens criadas localmente não estará disponível no dashboard do Braze.

```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## Envio de mensagens de intenção de saída

As mensagens de intenção de saída são mensagens no app não disruptivas usadas para comunicar informações importantes aos visitantes antes que eles saiam do site.

Para configurar disparos para esses tipos de mensagem, implemente uma biblioteca de intenção de saída em seu site (como a [biblioteca de código aberto do ouibounce](https://github.com/carlsednaoui/ouibounce)) e, em seguida, use o código a seguir para registrar `'exit intent'` como um evento personalizado no Braze. Agora, suas futuras campanhas de mensagens no app podem usar esse tipo de mensagem como um disparador de evento personalizado.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
