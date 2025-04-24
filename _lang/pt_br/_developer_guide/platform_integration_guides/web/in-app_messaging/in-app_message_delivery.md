---
nav_title: Entrega de mensagem no app
article_title: Entrega de mensagem no app para a web
platform: Web
channel: in-app messages
page_order: 4
page_type: reference
description: "Este artigo descreve a entrega de mensagem no app pelo SDK da Braze, abrangente a exibição manual de mensagens no app ou o envio de mensagens locais no app e mensagens de intenção de saída."

---

# entrega de mensagem no app

> Este artigo descreve a entrega de mensagem no app pelo SDK da Braze, abrangente a exibição manual de mensagens no app ou o envio de mensagens locais no app e mensagens de intenção de saída.

## Tipos de disparo

Nosso produto de mensagem no app permite que você disparar uma exibição de mensagem no app como resultado de vários tipos de eventos diferentes: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` e `Push Click`. Além disso, os disparos `Specific Purchase` e `Custom Event` contêm filtros de propriedade robustos.

{% alert note %}
As mensagens no app disparadas só funcionam com eventos personalizados registrados por meio do SDK da Braze. As mensagens no app não podem ser disparadas por meio da API ou por eventos da API (como eventos de compra). Se você está trabalhando com um app web, confira como [registrar eventos personalizados]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/#tracking-custom-events).
{% endalert %}

## Semântica de entrega

Todas as mensagens no app para as quais um usuário é elegível são automaticamente baixadas para o dispositivo do usuário ou navegador ao iniciar uma sessão e são acionadas de acordo com as regras de entrega da mensagem. Para saber mais sobre a semântica de início de sessão do SDK, leia sobre nossa [documentação do ciclo de vida de sessões]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/#session-lifecycle).

## Intervalo de tempo mínimo entre gatilhos

Por padrão, limitamos a frequência das mensagens no app para uma vez a cada 30 segundos para garantir uma experiência de qualidade para o usuário. Para substituir este valor, você pode passar a opção de configuração `minimumIntervalBetweenTriggerActionsInSeconds` para sua função [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize):

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## Exibição manual de mensagem no app

Se você não quiser que seu site exiba imediatamente novas mensagens no app quando elas forem acionadas, você pode desativar a exibição automática e registrar seus próprios assinantes de exibição. 

Primeiro, encontre e remova a chamada para `braze.automaticallyShowInAppMessages()` do snippet de carregamento. Em seguida, crie sua própria lógica para lidar com uma mensagem no app disparada, onde você mostra ou não a mensagem. 

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use Braze's built-in display capabilities, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
Se você não remover `braze.automaticallyShowInAppMessages()` do seu site ao chamar `braze.showInAppMessage`, a mensagem pode ser exibida duas vezes.
{% endalert %}

O parâmetro `inAppMessage` será uma subclasse [`braze.InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) ou um objeto [`braze.ControlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.controlmessage.html), tendo cada um vários métodos de inscrição de eventos de ciclo de vida. Consulte a [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) para a documentação completa.

Apenas uma [`Modal`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#modal-in-app-messages) ou [`Full`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#full-in-app-messages) mensagem no app pode ser exibida por vez. Se você tentar mostrar um segundo modal ou uma mensagem completa enquanto outra já estiver sendo exibida, `braze.showInAppMessage` retornará falso, e a segunda mensagem não será exibida.

## Mensagens locais no app

Mensagens no app também podem ser criadas dentro do seu site e exibidas localmente em tempo real. Todas as opções de personalização disponíveis no dashboard também estão disponíveis localmente. Isso é particularmente útil para exibir mensagens que você deseja disparar no app em tempo real. No entanto, a análise de dados dessas mensagens criadas localmente não estará disponível no dashboard do Braze.

```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## Mensagens de intenção de saída

Mensagens no app de intenção de saída aparecem quando os visitantes estão prestes a sair do seu site. Eles fornecem outra oportunidade para comunicar informações importantes aos usuários enquanto não interrompem sua experiência em seu site. 

Para enviar essas mensagens, primeiro adicione uma biblioteca de intenção de saída, como esta [biblioteca de código aberto](https://github.com/carlsednaoui/ouibounce) ao seu site. Em seguida, use o seguinte snippet para registrar "exit intent" como um evento personalizado. Campanhas de mensagens no app podem ser criadas no dashboard usando "exit intent" como o evento-gatilho personalizado.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```


