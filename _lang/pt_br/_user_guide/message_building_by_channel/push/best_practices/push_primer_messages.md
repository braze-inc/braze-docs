---
nav_title: Mensagens no app do Push Primer
article_title: Mensagens no app do Push Primer
page_order: 1
page_type: reference
description: "Este artigo aborda os pré-requisitos para o envio de mensagens no app e como configurá-las."
channel: push

---

# Mensagens no app com cartilha push

![Envio de mensagens no app para aplicativos de streaming. A notificação diz: "Receber notificações por push do Movie Cannon? As notificações podem incluir novos filmes, programas de TV ou outros avisos e podem ser desativadas a qualquer momento."][1]{: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> Você só tem uma chance de pedir permissão aos usuários por push, portanto, otimizar o registro de push é crucial para maximizar o alcance das suas mensagens push. Para ajudar a conseguir isso, você pode usar mensagens no app para explicar que tipo de mensagens seus usuários podem esperar receber se optarem pela aceitação, antes de mostrar a eles o pedido de aceitação push nativo. Isso é chamado de push primer.

Para criar uma mensagem no app com push primer na Braze, você pode usar o comportamento ao clicar no botão "Solicitar permissão de push" ao criar uma mensagem no app para iOS, Android ou Web.

## Pré-requisitos

Este guia usa um [comportamento ao clicar](#button-actions) em um botão que só é compatível com as versões mais recentes do SDK. Note que alguns desses SDKs podem ainda não ter sido lançados. Acesse os links a seguir para verificar a versão atual:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

### Notas para equipes de desenvolvimento

#### Android

- **Android 12 ou menos:** A implementação de push primers não é recomendada porque o push é aceito por padrão.
- **Android 13 e superior:** Se quiser ver o aviso várias vezes durante o teste, acesse as configurações do dispositivo e desative o push do app para permitir que o primer seja exibido novamente.

#### iOS

- O prompt do iOS pode ser exibido apenas uma vez por instalação, o que é imposto pelo sistema operacional.
- O prompt não será exibido se a configuração push do app estiver explicitamente ativada ou desativada; ele será exibido apenas para usuários com [autorização provisória](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - Se descobrirmos que a configuração push do app está ativada, o Braze não mostrará a mensagem no app, pois o usuário já tem a aceitação.
  - Se a configuração de notificação por push do aplicativo estiver desativada, encaminhe o usuário para as configurações de notificação do aplicativo no aplicativo de configurações.

##### Remoção manual do código

A mensagem no app que você configurou usando este tutorial chamará o código de prompt push nativo automaticamente quando um usuário clicar no botão de mensagem no app. Para evitar a solicitação de permissão de notificação por push duas vezes ou no momento errado, o desenvolvedor deve modificar qualquer integração de notificação por push existente que tenha implementado para garantir que a mensagem no app seja o primeiro primer de notificação por push que os usuários vejam.

O desenvolvedor deve revisar a implementação de notificações por push para seu app ou site e remover manualmente qualquer código que solicite permissão por push. Por exemplo, procure e remova referências ao seguinte código:

{% tabs %}
{% tab OBJECTIVE C %}
```objc
requestAuthorizationWithOptions
```
{% endtab %}
{% tab swift %}
```swift
requestAuthorization
```
{% endtab %}
{% tab JavaScript %}
```javascript
braze.requestPushPermission()
// or
appboy.registerAppboyPushMessages()
```
{% endtab %}
{% tab Java %}
```java
android.permission.POST_NOTIFICATIONS
```
{% endtab %}
{% endtabs %}

## Etapa 1: Crie uma mensagem no app

[Crie uma mensagem no app][2] como faria normalmente.

Selecione um tipo de mensagem e um layout. Para que você tenha espaço suficiente para explicar quais notificações por push seus usuários podem esperar (e para permitir o uso de botões), o Braze sugere uma mensagem em tela inteira ou modal. Note que, para uma mensagem no app em tela cheia, é necessária uma imagem. 

## Etapa 2: Crie sua mensagem

Agora é hora de adicionar sua cópia! Lembre-se de que um push primer deve preparar o usuário para ativar as notificações por push. No corpo da mensagem, sugerimos destacar os motivos pelos quais os usuários devem ativar as notificações por push. Seja específico quanto ao tipo de notificações que você deseja enviar e o valor que elas podem oferecer.

Por exemplo, um app de notícias pode usar o seguinte push primer:

> Notícias de última hora em movimento! Ative as notificações por push para receber alertas sobre as principais stories e tópicos importantes para você.

Enquanto um app de streaming pode usar o seguinte:

> Receber notificações por push do Movie Cannon? As notificações podem incluir novos filmes, programas de TV ou outros avisos e podem ser desativadas a qualquer momento.

Para obter práticas recomendadas e recursos adicionais, consulte [Criação de pedidos de aceitação personalizados][3].

## Etapa 3: Especificar o comportamento do botão {#button-actions}

Para adicionar botões à sua mensagem no app, adicione texto aos campos de texto **Botão 1** e **Botão 2**, que são os botões secundário e primário em sua mensagem no app, respectivamente. Recomendamos "Allow notifications" (Permitir notificações) e "Not now" (Agora não) como botões iniciais, mas você pode atribuir vários avisos de botões diferentes.

Depois de adicionar o texto do botão, especifique o comportamento ao clicar em cada botão:

- **Botão 1:** Defina essa opção como "Fechar mensagem". Esse é seu botão secundário ou a opção "Not now" (Agora não).
- **Botão 2:** Defina essa opção como "Request Push Permission" (Solicitar permissão de push). Esse é o botão principal ou a opção "Permitir notificações".

![][4]

## Etapa 4: Programação de entrega

Para definir o envio do push primer em um momento relevante, é necessário programar a mensagem no app como uma mensagem baseada em ação com **Perform Custom Event** como a ação-gatilho.

Embora o momento ideal varie, o Braze sugere esperar até que um usuário conclua algum tipo de [ação de alto valor](https://www.braze.com/resources/videos/mapping-high-value-actions), indicando que ele está começando a ver valor em seu app ou site, ou quando houver uma necessidade convincente que as notificações por push possam atender (por exemplo, depois que ele fizer um pedido e você quiser oferecer a ele informações de rastreamento de envio). Dessa forma, a solicitação é benéfica para o cliente e não apenas para sua marca.

![][5]

## Etapa 5: Usuários-alvo

Como o objetivo de uma campanha de mensagens push é solicitar que os usuários aceitem o envio de mensagens, não é recomendável direcionar os usuários que já aceitaram. Para isso, adicione um segmento ou filtro em que `Push Subscription Status is not Opted In`.

Além disso, você pode decidir quais segmentos adicionais considera mais apropriados. Por exemplo, você pode direcionar usuários que concluíram uma segunda compra, usuários que acabaram de criar uma conta para se tornarem membros ou até mesmo usuários que visitam seu app mais de duas vezes por semana. O direcionamento de usuários para esses segmentos cruciais aumenta a probabilidade de aceitação e capacitação de usuários por push.

## Etapa 6: Eventos de conversão

O Braze sugere configurações padrão para conversões, mas você pode querer configurar [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) em torno de primers push.

[1]: {% image_buster /assets/img_archive/push_primer_iam.png %}
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/creating_custom_opt-in_prompts/
[4]: {% image_buster /assets/img_archive/push_primer_button_behavior.png %}
[5]: {% image_buster /assets/img_archive/push_primer_trigger.png %}
