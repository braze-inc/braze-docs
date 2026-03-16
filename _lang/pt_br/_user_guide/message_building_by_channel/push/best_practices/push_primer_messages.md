---
nav_title: Mensagens no app com cartilha push
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

Este recurso requer [comportamento ao clicar no botão](#button-actions), que é suportado nas seguintes versões mínimas ou posteriores:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Além disso, note os seguintes detalhes específicos da plataforma:

{% tabs local %}
{% tab android %}
|Versão do SO|Informações adicionais|
\|----------|----------------------|
| **Android 12 e anteriores** | Implementar primers de push não é recomendado porque o push é ativado por padrão. |
| **Android 13+** | Se um usuário negar seu prompt de permissão de push duas vezes, o Android bloqueia novos prompts—incluindo mensagens de primer de push do Braze. Para conceder permissão após isso, os usuários devem ativar manualmente o push para seu app nas configurações do dispositivo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab swift %}
### Informações gerais

- O prompt de push pode ser exibido apenas uma vez por instalação, imposto pelo sistema operacional.
- O prompt não é exibido se a configuração de push do app estiver explicitamente ativada ou desativada. Ele só é exibido para usuários com [autorização provisória](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - **A configuração de push do app está ativada:** O Braze não exibe a mensagem no app, pois o usuário já optou por participar.
  - **A configuração de push do app está desativada:** Você precisa redirecionar o usuário para as configurações de notificação por push do seu app nas configurações do dispositivo.

### Remoção manual do código

A mensagem no app que você configurou usando este tutorial chama automaticamente o código nativo do prompt de push quando um usuário clica no botão da mensagem no app. Para evitar a solicitação de permissão de notificação por push duas vezes ou no momento errado, o desenvolvedor deve modificar qualquer integração de notificação por push existente que tenha implementado para garantir que a mensagem no app seja o primeiro primer de notificação por push que os usuários vejam.

Sua equipe de desenvolvimento deve revisar sua implementação de notificações por push para seu app ou site e remover manualmente qualquer código que solicite permissão para push. Por exemplo, remova referências ao seguinte código:

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

Primeiro, [crie uma mensagem no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/), depois selecione o tipo e layout da sua mensagem.

Para garantir que você tenha espaço suficiente para sua mensagem e botões, use um layout de mensagem em tela cheia ou modal. Se você escolher tela cheia, note que uma imagem é necessária.

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

Para melhores práticas e recursos adicionais, consulte [Criando prompts de aceitação personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Etapa 3: Especificar o comportamento do botão {#button-actions}

Para adicionar botões à sua mensagem no app, arraste dois blocos de **Botão** para sua mensagem, que atuam como os botões primário e secundário na sua mensagem no app. Você também pode arrastar uma linha para sua mensagem e, em seguida, arrastar os botões para a linha, para que os botões fiquem na mesma linha horizontal (em vez de empilhados um sobre o outro). Recomendamos "Permitir notificações" e "Agora não" como botões iniciais, mas existem muitos prompts de botões diferentes que você pode atribuir.

Depois de adicionar o texto do botão, especifique o comportamento ao clicar em cada botão:

- **Botão 1:** Defina essa opção como "Fechar mensagem". Esse é seu botão secundário ou a opção "Not now" (Agora não).
- **Botão 2:** Defina essa opção como "Request Push Permission" (Solicitar permissão de push). Esse é o botão principal ou a opção "Permitir notificações".

![Compositor de mensagem no app com dois botões: "Permitir notificações" e "Agora não".]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## Etapa 4: Programação de entrega

Para definir o envio do push primer em um momento relevante, é necessário programar a mensagem no app como uma mensagem baseada em ação com **Perform Custom Event** como a ação-gatilho.

Embora o momento ideal varie, o Braze sugere esperar até que um usuário conclua algum tipo de [ação de alto valor](https://www.braze.com/resources/videos/mapping-high-value-actions), indicando que ele está começando a ver valor em seu app ou site, ou quando houver uma necessidade convincente que as notificações por push possam atender (por exemplo, depois que ele fizer um pedido e você quiser oferecer a ele informações de rastreamento de envio). Dessa forma, a solicitação é benéfica para o cliente e não apenas para sua marca.

![Configurações de entrega baseada em ação para enviar a usuários que realizaram o evento personalizado de "Adicionar à Lista de Desejos".]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## Etapa 5: Usuários-alvo

O objetivo de uma campanha de introdução de push é solicitar aos usuários em qualquer dispositivo onde eles ainda não concederam permissões de push. Isso pode incluir usuários de primeira viagem ou usuários existentes que obtêm um novo dispositivo ou reinstalam seu aplicativo.

{% alert important %}
**Supressão automática com introdução de push sem código**: Se você usar a introdução de push sem código (a ação do botão "Solicitar Permissão de Push"), não precisa adicionar filtros de inscrição por push à sua segmentação. O SDK suprime automaticamente a mensagem no app em dispositivos que já possuem um token de push ativo, independentemente do status de push do usuário em outros dispositivos. Para mais informações sobre direcionamento de usuários com múltiplos dispositivos, consulte [Direcionamento de usuários com múltiplos dispositivos](#targeting-users-with-multiple-devices).
{% endalert %}

Se você não estiver usando a introdução de push sem código, adicione um filtro onde `Foreground Push Enabled For App is false`. Esse filtro identifica instalações individuais do app que ainda não estão optadas para notificações por push em primeiro plano.

{% alert important %}
Usar um filtro em nível de usuário como `Push Subscription Status is not Opted In` exclui usuários que já estão optados em outro dispositivo, impedindo que eles recebam o prompt em seu novo dispositivo.
{% endalert %}

Além disso, você pode decidir quais segmentos adicionais considera mais apropriados. Por exemplo, você pode direcionar usuários que concluíram uma segunda compra, usuários que acabaram de criar uma conta para se tornarem membros ou até mesmo usuários que visitam seu app mais de duas vezes por semana. O direcionamento de usuários para esses segmentos cruciais aumenta a probabilidade de aceitação e capacitação de usuários por push.

### Direcionamento de usuários com múltiplos dispositivos

Como a Braze captura dados de usuários no nível do perfil em vez do nível do dispositivo, direcionar usuários que possuem múltiplos dispositivos pode ser desafiador. Filtros de inscrição por push na segmentação incluem ou excluem usuários com base no estado de inscrição de um único dispositivo, em vez do estado de inscrição do dispositivo específico direcionado. Além disso, estados provisórios no iOS adicionam complexidade, já que esses dispositivos tecnicamente têm tokens de push em primeiro plano, mas os usuários não estão explicitamente optados.

#### O problema com filtros de inscrição push

Quando um usuário tem vários dispositivos com diferentes estados de inscrição push, os filtros de inscrição push na sua segmentação podem falhar em direcionar alguns dispositivos. Considere estes cenários:

{% details Scenario 1: User has two devices on different platforms %}

**O usuário tem dois dispositivos:**
- Dispositivo A: Android, optou por receber push
- Dispositivo B: iOS, não optou por receber push

**Filtros de segmento que não funcionam:**
- `Push enabled = false` - O usuário está habilitado para push em seu dispositivo Android, então ele não se enquadra no segmento. O segmento não inclui o dispositivo iOS.
- `Push subscription status is not opted in` - O usuário está habilitado para push em seu dispositivo Android, então ele não se enquadra no segmento. O segmento não inclui o dispositivo iOS.

**Filtros de segmento que funcionam:**
- `Push enabled for iOS = false` - O usuário está habilitado para push em seu dispositivo Android, mas estamos apenas direcionando dispositivos iOS, então o usuário se enquadra no segmento. O segmento inclui o dispositivo iOS.

{% enddetails %}

{% details Scenario 2: User has two iOS devices with different states %}

**O usuário tem dois dispositivos iOS:**
- Dispositivo A: Optou por receber push
- Dispositivo B: Habilitado provisoriamente, mas não optou por receber

**Filtros de segmento que não funcionam:**
- `Push enabled = false` - O Dispositivo A está optado para push, então o usuário não se enquadra no segmento. O segmento não inclui o Dispositivo B.
- `Provisionally opted in = true` - O Dispositivo A está totalmente optado, o que significa que não está em um estado provisório. O usuário não se enquadra no segmento. O segmento não inclui o Dispositivo B.
- `Push enabled for app > iOS = false` - O Dispositivo A está optado para push no iOS, então o usuário não se enquadra no segmento. O segmento não inclui o Dispositivo B.
- `Push subscription status is not opted in` - O Dispositivo A está optado para push, então o usuário não se enquadra no segmento. O segmento não inclui o Dispositivo B.

**Resultado:** Usar qualquer combinação desses filtros de push resulta no segmento excluindo pelo menos um dispositivo.

{% enddetails %}

{% details Scenario 3: User has three or more devices on the same OS %}

**O usuário tem três dispositivos:**
- Dispositivo A: Optou por receber push
- Dispositivo B: Não optado para push
- Dispositivo C: Não optado para push

**Filtros de segmento que não funcionam:**
- `Push enabled = false` - O Dispositivo A está optado para push, então o usuário não se enquadra no segmento. O segmento não inclui os Dispositivos B e C.
- `Push enabled for app > X = false` - O Dispositivo A está optado para push no app especificado, então o usuário não se enquadra no segmento. O segmento não inclui os Dispositivos B e C.
- `Push subscription status is not opted in` - O Dispositivo A está optado para push, então o usuário não se enquadra no segmento. O segmento não inclui os Dispositivos B e C.

**Resultado:** Usar qualquer combinação desses filtros de push deixa pelo menos um dispositivo sem alvo.

{% enddetails %}

#### Solução: Use o primer de push sem código

A solução recomendada é usar o primer de push sem código (a ação do botão "Solicitar Permissão para Push") sem filtros adicionais de segmentação de status de push.

{% alert important %}
**Supressão automática**: O primer de push sem código suprime automaticamente em dispositivos que já possuem um token de push ativo. O SDK verifica se um usuário em seu dispositivo específico já possui um token de push. Se o SDK descobrir que o usuário já optou por participar (por exemplo, a partir de uma solicitação anterior ou via configurações do dispositivo), o SDK suprime automaticamente a mensagem no app sem a necessidade de filtros adicionais de segmentação. O primer aparece em todos os outros cenários, incluindo se um usuário estiver provisoriamente optado para push.
{% endalert %}

O benefício de usar o primer de push sem código é que a funcionalidade é suportada pelo SDK da Braze. Como o SDK pode detectar o status do token de push no dispositivo específico que exibe a mensagem, você não precisa depender de filtros de segmentação em nível de perfil que podem excluir usuários com múltiplos dispositivos.

#### Considerações

**Primer de push sem código necessário**: Você deve usar o primer de push sem código para que a supressão automática funcione. Se você configurar lógica personalizada ou links profundos em vez de usar a ação "Solicitar Permissão para Push", o SDK não consegue identificar que você está tentando exibir um primer de push. Isso resulta na exibição da mensagem, independentemente do estado de inscrição desse dispositivo.

**Suprimindo para usuários que optaram por sair**: Você pode querer suprimir a mensagem no app para usuários que optaram explicitamente por sair do push (por exemplo, a partir da solicitação nativa ou configurações do dispositivo) e redirecionar esses usuários com uma campanha de nutrição separada. Para fazer isso, use a seguinte lógica Liquid em combinação com o primer sem código:

{% raw %}
```liquid
{% if targeted_device.${foreground_push_enabled} == false %} 
{% abort_message('user turned off push notifications') %} 
{% endif %}
- message goes here -
```
{% endraw %}

O filtro Liquid `targeted_device` considera apenas o dispositivo onde a mensagem está sendo exibida, em vez do perfil do usuário. Nesse dispositivo, `foreground_push_enabled` é definido como `true` quando há um token de push ativo em primeiro plano e definido como `false` quando o sistema operacional informa que as notificações por push foram desativadas (por exemplo, o usuário as desligou explicitamente). Para dispositivos completamente novos que ainda não responderam a um estado de permissão de push, `foreground_push_enabled` não está definido e não tem valor. Como a condição Liquid verifica especificamente `{% raw %}``false`{% endraw %}, ela suprime o primer apenas para dispositivos com uma opção de saída explícita, enquanto dispositivos nesse estado desconhecido ainda se qualificam e podem receber o primer de push.

## Etapa 6: Eventos de conversão

O Braze sugere configurações padrão para conversões, mas você pode querer configurar [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) em torno de primers push.