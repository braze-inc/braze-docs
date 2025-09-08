---
nav_title: Mensagens no app do Push Primer
article_title: Mensagens no app do Push Primer
page_order: 1
page_type: reference
description: "Este artigo aborda os pré-requisitos para o envio de mensagens no app e como configurá-las."
channel: push

---

# Mensagens no app com cartilha push

![Envio de mensagens no app para aplicativos de streaming. A notificação diz: "Receber notificações por push do Movie Cannon? As notificações podem incluir novos filmes, programas de TV ou outros avisos e podem ser desativadas a qualquer momento."]({% image_buster /assets/img_archive/push_primer_iam.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> Você só tem uma chance de pedir permissão aos usuários por push, portanto, otimizar o registro de push é crucial para maximizar o alcance das suas mensagens push. Para ajudar a conseguir isso, você pode usar mensagens no app para explicar que tipo de mensagens seus usuários podem esperar receber se optarem pela aceitação, antes de mostrar a eles o pedido de aceitação push nativo. Isso é chamado de push primer.

Para criar uma mensagem no app com push primer na Braze, você pode usar o comportamento ao clicar no botão "Solicitar permissão de push" ao criar uma mensagem no app para iOS, Android ou Web.

## Pré-requisitos

Esse recurso requer [o comportamento ao clicar em um botão](#button-actions), que é compatível com as seguintes versões mínimas ou posteriores:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Além disso, observe os seguintes detalhes específicos da plataforma:

{% tabs local %}
{% tab Android %}
|Versão do sistema operacional|Informações adicionais|
\|----------|----------------------|
| **Android 12 e versões anteriores** A implementação de primers push não é recomendada porque o push é aceito por padrão. |
| **Android 13+** | Se um usuário negar duas vezes a solicitação de permissão de envio de mensagens, o Android bloqueará outras solicitações, inclusive as mensagens de push do Braze. Para conceder permissão depois disso, os usuários devem ativar manualmente o push para o seu app nas configurações do dispositivo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab swift %}
### Informações gerais

- O prompt push pode ser exibido apenas uma vez por instalação, o que é imposto pelo sistema operacional.
- O prompt não será exibido se a configuração push do app estiver explicitamente ativada ou desativada; ele será exibido apenas para usuários com [autorização provisória](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - **A configuração push do app está ativada:** O Braze não mostrará a mensagem no app, pois o usuário já fez a aceitação.
  - **A configuração push do app está desativada:** Será necessário redirecionar o usuário para as configurações de notificação por push do seu app nas configurações do dispositivo.

### Remoção manual do código

A mensagem no app que você configurou usando este tutorial chamará o código de prompt push nativo automaticamente quando um usuário clicar no botão de mensagem no app. Para evitar a solicitação de permissão de notificação por push duas vezes ou no momento errado, o desenvolvedor deve modificar qualquer integração de notificação por push existente que tenha implementado para garantir que a mensagem no app seja o primeiro primer de notificação por push que os usuários vejam.

Sua equipe de desenvolvimento deve revisar a implementação de notificações por push para seu app ou site e remover manualmente qualquer código que solicite permissão de push. Por exemplo, você removeria as referências ao seguinte código:

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
requestAuthorizationWithOptions
```
{% endsubtab %}
{% subtab swift %}
```swift
requestAuthorization
```
{% endsubtab %}
{% subtab JavaScript %}
```javascript
braze.requestPushPermission()
// or
appboy.registerAppboyPushMessages()
```
{% endsubtab %}
{% subtab Java %}
```java
android.permission.POST_NOTIFICATIONS
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Etapa 1: Crie uma mensagem no app

Primeiro, [crie uma mensagem no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) e, em seguida, selecione o tipo e o layout da mensagem.

Para garantir que haja espaço suficiente para a mensagem e os botões, use um layout de tela cheia ou de mensagem modal. Se escolher tela cheia, note que é necessária uma imagem.

## Etapa 2: Crie sua mensagem

Agora é hora de adicionar sua cópia! Lembre-se de que um push primer deve preparar o usuário para ativar as notificações por push. No corpo da mensagem, sugerimos destacar os motivos pelos quais os usuários devem ativar as notificações por push. Seja específico quanto ao tipo de notificações que você deseja enviar e o valor que elas podem oferecer.

Por exemplo, um app de notícias pode usar o seguinte push primer:

```plaintext
Breaking news on the go! Enable push notifications to get alerts for major stories and topics that matter to you.
```

Enquanto um app de streaming pode usar o seguinte:

```plaintext
Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time.
```

Para obter práticas recomendadas e recursos adicionais, consulte [Criação de pedidos de aceitação personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Etapa 3: Especificar o comportamento do botão {#button-actions}

Para adicionar botões à sua mensagem no app, arraste dois blocos de **botões** para a mensagem, que funcionarão como os botões primário e secundário da mensagem no app. Também é possível arrastar uma linha para a mensagem e, em seguida, arrastar os botões para a linha, de modo que os botões fiquem na mesma linha horizontal (em vez de empilhados uns sobre os outros). Recomendamos "Allow notifications" (Permitir notificações) e "Not now" (Agora não) como botões iniciais, mas você pode atribuir vários avisos de botões diferentes.

Depois de adicionar o texto do botão, especifique o comportamento ao clicar em cada botão:

- **Botão 1:** Defina essa opção como "Fechar mensagem". Esse é seu botão secundário ou a opção "Not now" (Agora não).
- **Botão 2:** Defina essa opção como "Request Push Permission" (Solicitar permissão de push). Esse é o botão principal ou a opção "Permitir notificações".

![Criador de mensagens no app com dois botões: "Allow notifications" (Permitir notificações) e "Not now" (Não agora).]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## Etapa 4: Programação de entrega

Para definir o envio do push primer em um momento relevante, é necessário programar a mensagem no app como uma mensagem baseada em ação com **Perform Custom Event** como a ação-gatilho.

Embora o momento ideal varie, o Braze sugere esperar até que um usuário conclua algum tipo de [ação de alto valor](https://www.braze.com/resources/videos/mapping-high-value-actions), indicando que ele está começando a ver valor em seu app ou site, ou quando houver uma necessidade convincente que as notificações por push possam atender (por exemplo, depois que ele fizer um pedido e você quiser oferecer a ele informações de rastreamento de envio). Dessa forma, a solicitação é benéfica para o cliente e não apenas para sua marca.

![Configurações de entrega baseada em ação para enviar aos usuários que realizaram o evento personalizado de "Adicionar à lista de observação".]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## Etapa 5: Usuários-alvo

Como o objetivo de uma campanha de mensagens push é solicitar que os usuários aceitem o envio de mensagens, não é recomendável direcionar os usuários que já aceitaram. Para isso, adicione um segmento ou filtro em que `Push Subscription Status is not Opted In`.

Além disso, você pode decidir quais segmentos adicionais considera mais apropriados. Por exemplo, você pode direcionar usuários que concluíram uma segunda compra, usuários que acabaram de criar uma conta para se tornarem membros ou até mesmo usuários que visitam seu app mais de duas vezes por semana. O direcionamento de usuários para esses segmentos cruciais aumenta a probabilidade de aceitação e capacitação de usuários por push.

## Etapa 6: Eventos de conversão

O Braze sugere configurações padrão para conversões, mas você pode querer configurar [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) em torno de primers push.

