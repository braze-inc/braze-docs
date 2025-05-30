{% multi_lang_include developer_guide/prerequisites/web.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

## Sobre os prompts de soft push

Muitas vezes, é uma boa ideia que os sites implementem um prompt de push "suave", no qual você "prepara" o usuário e defende o envio de notificações por push antes de solicitar a permissão de push. Isso é útil porque o navegador limita a frequência com que você pode solicitar diretamente ao usuário e, se o usuário negar a permissão, você nunca mais poderá solicitá-la novamente.

Como alternativa, se quiser incluir um envio especial de [mensagens]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web) personalizadas, em vez de chamar `requestPushPermission()` diretamente, conforme descrito na [integração]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-2-browser-registration) padrão do [Web push]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-2-browser-registration), use nossas [mensagens disparadas no app]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web).

{% alert tip %}
Isso pode ser feito sem a personalização do SDK usando nosso novo [push primer sem código]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
{% endalert %}

## Configuração de prompts de soft push

{% multi_lang_include archive/web-v4-rename.md %}

### Etapa 1: Crie uma campanha de push primer

Primeiro, você deve criar uma campanha de mensagens no app "Prime for Push" no dashboard da Braze:

1. Crie uma mensagem **modal** no app com o texto e o estilo que desejar. 
2. Em seguida, defina o comportamento ao clicar como **Fechar mensagem**. Esse comportamento será personalizado posteriormente.
3. Adicione um par chave-valor à mensagem em que a chave é `msg-id` e o valor é `push-primer`.
4. Atribua uma ação-gatilho de evento personalizado (como "prime-for-push") à mensagem. Você pode criar o evento personalizado manualmente no dashboard, se necessário.

### Etapa 2: Remover chamadas

Em sua integração do SDK do Braze, localize e remova todas as chamadas para `automaticallyShowInAppMessages()` de seu snippet de carregamento.

### Etapa 3: Integração de atualizações

Por fim, substitua a chamada removida pelo seguinte trecho:

```javascript
import * as braze from "@braze/web-sdk";
// Be sure to remove any calls to braze.automaticallyShowInAppMessages()
braze.subscribeToInAppMessage(function(inAppMessage) {
  // check if message is not a control variant
  if (inAppMessage instanceof braze.inAppMessage) {
    // access the key-value pairs, defined as `extras`
    const keyValuePairs = inAppMessage.extras || {};
    // check the value of our key `msg-id` defined in the Braze dashboard
    if (keyValuePairs["msg-id"] === "push-primer") {
      // We don't want to display the soft push prompt to users on browsers
      // that don't support push, or if the user has already granted/blocked permission
      if (
        braze.isPushSupported() === false ||
        braze.isPushPermissionGranted() ||
        braze.isPushBlocked()
      ) {
        // do not call `showInAppMessage`
        return;
      }

      // user is eligible to receive the native prompt
      // register a click handler on one of the two buttons
      if (inAppMessage.buttons[0]) {
        // Prompt the user when the first button is clicked
        inAppMessage.buttons[0].subscribeToClickedEvent(function() {
          braze.requestPushPermission(
            function() {
              // success!
            },
            function() {
              // user declined
            }
          );
        });
      }
    }
  }

  // show the in-app message now
  braze.showInAppMessage(inAppMessage);
});
```

Quando desejar exibir o prompt de soft push para o usuário, faça uma chamada para `braze.logCustomEvent`com o nome do evento que dispara essa mensagem no app.
