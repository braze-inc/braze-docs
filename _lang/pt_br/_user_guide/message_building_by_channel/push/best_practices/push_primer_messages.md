---
nav_title: Envie mensagens in-app do primer de push
article_title: Mensagens In-App do Primer de Push
page_order: 1
page_type: reference
description: "Este artigo cobre os pré-requisitos para mensagens in-app do primer de push e como configurá-las."
channel: push

---

# Envie mensagens in-app do primer de push

\![Mensagem in-app do primer de push para aplicativo de streaming. A notificação diz "Receber notificações push do Movie Cannon? As notificações podem incluir novos filmes, programas de TV ou outros avisos e podem ser desativadas a qualquer momento."]({% image_buster /assets/img_archive/push_primer_iam.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> Você só tem uma chance de pedir permissão de push aos usuários, então otimizar seu registro de push é crucial para maximizar o alcance de suas mensagens de push. Para ajudar a alcançar isso, você pode usar mensagens in-app para explicar que tipo de mensagens seus usuários podem esperar receber se optarem por participar, antes de mostrar a eles o prompt nativo de push. Isso é chamado de primer de push.

Para criar uma mensagem in-app do primer de push no Braze, você pode usar o comportamento de clique no botão "Solicitar Permissão de Push" ao criar uma mensagem in-app para iOS, Android ou Web.

## Pré-requisitos

Este recurso requer [comportamento de clique no botão](#button-actions), que é suportado nas seguintes versões mínimas ou posteriores:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Além disso, observe os seguintes detalhes específicos da plataforma:

{% tabs local %}
{% tab android %}
|Versão do SO|Informações adicionais|
\|----------|----------------------|
| **Android 12 e anteriores** | Implementar primers de push não é recomendado porque o push é optado por padrão. |
| **Android 13+** | Se um usuário negar seu prompt de permissão de push duas vezes, o Android bloqueia novos prompts—incluindo mensagens do primer de push do Braze. Para conceder permissão após isso, os usuários devem habilitar manualmente o push para seu aplicativo nas configurações do dispositivo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab swift %}
### Informações gerais

- O prompt de push pode ser exibido apenas uma vez por instalação, conforme imposto pelo sistema operacional.
- O prompt não será exibido se a configuração de push do aplicativo estiver explicitamente ativada ou desativada, ele será exibido apenas para usuários com [autorização provisória](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - **A configuração de push do aplicativo está ativada:** A Braze não mostrará a mensagem no aplicativo, pois o usuário já optou por participar.
  - **A configuração de push do aplicativo está desativada:** Você precisará redirecionar o usuário para as configurações de notificações push do seu aplicativo dentro das configurações do dispositivo.

### Remoção manual de código

A mensagem no aplicativo que você configurou usando este tutorial chamará automaticamente o código nativo do prompt de push quando um usuário clicar no botão da mensagem no aplicativo. Para evitar solicitar permissão para notificações push duas vezes, ou no momento errado, um desenvolvedor deve modificar qualquer integração existente de notificações push que implementou para garantir que sua mensagem no aplicativo seja o primeiro primer de notificação push que seus usuários veem.

Sua equipe de desenvolvimento deve revisar sua implementação de notificações push para seu aplicativo ou site e remover manualmente qualquer código que solicite permissão para push. Por exemplo, você removeria referências ao seguinte código:

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

## Passo 1: Crie uma mensagem no aplicativo

Primeiro, [crie uma mensagem no aplicativo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/), depois selecione o tipo e o layout da sua mensagem.

Para garantir que você tenha espaço suficiente para sua mensagem e botões, use um layout de mensagem em tela cheia ou modal. Se você escolher a tela cheia, observe que uma imagem é necessária.

## Passo 2: Construa sua mensagem

Agora é hora de adicionar seu texto! Lembre-se de que um primer de push deve preparar o usuário para ativar as notificações push. No corpo da sua mensagem, sugerimos destacar as razões pelas quais seus usuários devem ter as notificações push ativadas. Seja específico sobre que tipo de notificações você deseja enviar e qual valor elas podem fornecer.

Por exemplo, um aplicativo de notícias pode usar o seguinte primer de push:

```plaintext
Breaking news on the go! Enable push notifications to get alerts for major stories and topics that matter to you.
```

Enquanto um aplicativo de streaming pode usar o seguinte:

```plaintext
Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time.
```

Para melhores práticas e recursos adicionais, consulte [Criando prompts de opt-in personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Passo 3: Especifique o comportamento do botão {#button-actions}

Para adicionar botões à sua mensagem no aplicativo, arraste dois blocos de **Botão** para sua mensagem, que atuarão como os botões primário e secundário na sua mensagem no aplicativo. Você também pode arrastar uma linha para sua mensagem e, em seguida, arrastar os botões para a linha, para que os botões fiquem na mesma linha horizontal (em vez de empilhados um em cima do outro). Recomendamos "Permitir notificações" e "Agora não" como botões iniciais, mas existem muitos outros prompts de botão que você pode atribuir.

Depois de adicionar o texto do botão, especifique o comportamento ao clicar para cada botão:

- **Botão 1:** Defina isso como "Fechar Mensagem". Este é seu botão secundário, ou a opção "Agora não".
- **Botão 2:** Defina isso como "Solicitar Permissão para Envio de Notificações". Este é o seu botão principal, ou a opção "Permitir notificações".

\![Compositor de mensagem no aplicativo com dois botões: "Permitir notificações" e "Agora não".]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## Passo 4: Agendar entrega

Para definir seu primer de push para enviar em um momento relevante, você deve agendar sua mensagem no aplicativo como uma mensagem baseada em ação com **Executar Evento Personalizado** como a ação de gatilho.

Embora o momento ideal varie, a Braze sugere esperar até que um usuário complete algum tipo de [ação de alto valor](https://www.braze.com/resources/videos/mapping-high-value-actions), indicando que ele está começando a ver valor em seu aplicativo ou site, ou quando há uma necessidade convincente que as notificações push podem atender (como após fazer um pedido e você deseja oferecer informações de rastreamento de envio). Dessa forma, o aviso é benéfico para o cliente, em vez de apenas para sua marca.

\![Configurações de entrega baseadas em ação para enviar a usuários que realizaram o evento personalizado "Adicionar à Lista de Desejos".]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## Passo 5: Segmentar usuários

O objetivo de uma campanha de primer de push é solicitar usuários em qualquer dispositivo onde eles ainda não concederam permissões de push. Isso pode incluir usuários de primeira viagem ou usuários existentes que obtêm um novo dispositivo ou reinstalam seu aplicativo. Para segmentar corretamente sua campanha de primer de push, adicione um filtro onde `Foreground Push Enabled For App is false`. Esse filtro identifica instalações individuais do aplicativo que ainda não optaram por notificações push em primeiro plano.

{% alert important %}
Usar um filtro em nível de usuário como `Push Subscription Status is not Opted In` excluirá usuários que já optaram por outro dispositivo, impedindo que eles recebam o aviso em seu novo dispositivo.
{% endalert %}

Além disso, você pode decidir quais segmentos adicionais considera mais apropriados. Por exemplo, você pode segmentar usuários que completaram uma segunda compra, usuários que acabaram de criar uma conta para se tornarem membros, ou até mesmo usuários que visitam seu aplicativo mais de duas vezes por semana. Segmentar usuários para esses segmentos cruciais aumenta a probabilidade de os usuários optarem por participar e se tornarem habilitados para push.

## Etapa 6: Eventos de conversão

A Braze sugere configurações padrão para conversões, mas você pode querer configurar [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) em torno de iniciadores de push.

