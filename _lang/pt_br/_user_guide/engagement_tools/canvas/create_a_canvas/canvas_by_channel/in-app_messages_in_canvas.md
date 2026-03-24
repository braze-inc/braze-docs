---
nav_title: Mensagem no app
article_title: Mensagens no app na canva
alias: "/canvas_in-app_messages/"
page_order: 2
page_type: reference
description: "Este artigo de referência descreve os recursos e as nuances específicos das mensagens no app que podem ser adicionados ao Canvas para exibir envios de mensagens sofisticadas."
tool: Canvas
channel: in-app messages

---

# Mensagens no app no Canva

> É possível adicionar mensagens no app como parte da jornada do Canva para mostrar mensagens ricas quando o cliente se engaja com o aplicativo.

## Como funciona?

Antes de poder usar mensagens no app em seu Canvas, certifique-se de ter um [canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) configurado com opções de postergação e público.

No construtor de canva, adicione uma etapa de [Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) e selecione **Mensagem no App** como seu **canal de envio de mensagens**. Você pode personalizar [quando sua mensagem expirará](#in-app-message-expiration) e qual [comportamento de avanço](#advancement-behavior) ela terá.

## Adicionar uma mensagem no app à jornada do usuário

Para adicionar uma mensagem no app ao seu Canva, faça o seguinte:

1. Adicione uma etapa de [Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) à jornada do usuário.
2. Selecione **Mensagem no app** para seu **canal de envio de mensagens**. 
3. Determine [quando sua mensagem expirará](#in-app-message-expiration) e qual [comportamento de avanço](#advancement-behavior-options) ela terá.

## Mensagens no app disparadas

Você pode selecionar um gatilho para suas mensagens no app serem disparadas no início da sessão, ou por eventos e compras personalizados.

Após qualquer postergação e as opções de público serem verificadas, as mensagens no app são ativadas quando um usuário chega à etapa de Mensagem. Se um usuário iniciar uma sessão e realizar o evento de gatilho para a mensagem no app, o usuário verá a mensagem no app. 

Para etapas do Canva que têm entrada acionada por ação, os usuários podem entrar no Canvas no meio da sessão. As mensagens no app não são ativadas até que uma sessão comece, então se um usuário estiver no meio de uma sessão quando chegar à etapa de Mensagem, ele não receberá a mensagem no app até que inicie outra sessão e realize o gatilho relevante.

## Expiração de mensagens no app

Você pode escolher quando a mensagem no app irá expirar. Durante esse tempo, a mensagem no app ficará aguardando para ser visualizada até atingir a data de vencimento. Depois que a mensagem no app é enviada, ela pode ser visualizada uma única vez.

![A seção de Controles de Mensagem de uma etapa de Mensagem para uma mensagem no app. A mensagem no app irá expirar três dias após a etapa estar disponível.]({% image_buster /assets/img_archive/canvas_expiration2.png %}){: style="max-width:90%"}

| Opção | Descrição | Exemplo |
|---|---|---|
| **Uma duração após a etapa está disponível** | Define a mensagem no app para expirar em relação a quando a etapa se torna disponível para o usuário. | Uma mensagem no app com uma expiração de dois dias se tornaria disponível quando o usuário entra na etapa de Mensagem e as opções de público são verificadas. Qualquer postergação antes de chegar a esta etapa viria de etapas de Delay anteriores no seu canva. A mensagem no app estaria então disponível por 2 dias (48 horas) a partir do momento em que o usuário entra na etapa, e durante esses dois dias, os usuários podem ver a mensagem no app se abrirem o app. |
| **Em uma data e horário específicas** | Selecione uma data e hora específicas quando a mensagem no app não estará mais disponível. | Se você tiver uma promoção que termina em 30 de novembro de 2024, selecione esta opção para que os usuários não vejam mais a mensagem no app associada quando a promoção terminar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Casos de uso

A Braze recomenda que você considere usar este recurso em seus Canvases promocionais e de integração.

{% tabs %}
  {% tab Promotional %}

As promoções, os cupons e as vendas geralmente têm datas de expiração rígidas. O Canva a seguir deve alertar seus usuários, nos momentos mais oportunos, de que há uma promoção que eles podem usar e, talvez, influenciar uma compra. Esta promoção expira em 28 de fevereiro de 2019, às 11:15 da manhã no fuso horário da sua empresa.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>Etapa do canva</th>
    <th>Postergação</th>
    <th>Público</th>
    <th>Canal</th>
    <th>Expiração</th>
    <th>Avançar</th>
    <th>Informações</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Dia 1: 50% de desconto</td>
    <td>Nenhuma</td>
    <td>Tudo a partir da entrada</td>
    <td>Push</td>
    <td>N/D</td>
    <td>Avançar público após postergação</td>
    <td>Push inicial que alerta seus usuários sobre a promoção. O objetivo é levar os usuários ao seu app para aproveitar a promoção.</td>
  </tr>
  <tr>
    <td>No app: 50% de desconto</td>
    <td>Nenhuma</td>
    <td>Tudo a partir da entrada</td>
    <td>Mensagem no app</td>
    <td><b>Expira em:</b> 28/2/2019 11:15 AM Horário da empresa</td>
    <td>Mensagem no app visualizada</td>
    <td>O usuário agora abriu o app e receberá essa mensagem, seja ou não por causa da mensagem push anterior.</td>
  </tr>
  <tr>
    <td>Lembrete de 50% de desconto</td>
    <td>1 dia após o usuário receber a etapa anterior</td>
    <td>Tudo a partir da entrada <br><br><b>Filtro:</b> A última compra foi feita há mais de uma semana</td>
    <td>Mensagem no app</td>
    <td><b>Expira em:</b> 28/2/2019 11:15 AM Horário da empresa</td>
    <td>Nenhum (última mensagem no Canva)</td>
    <td>O usuário recebeu a mensagem no app na etapa anterior, mas não fez uma compra, apesar de estar no app. <br><br>Essa mensagem tem o objetivo de atrair ainda mais o usuário para fazer uma compra usando a promoção.</td>
  </tr>
</tbody>
</table>

As mensagens no app expiram quando a promoção expira para evitar discrepâncias entre a mensagem e a experiência do cliente.

  {% endtab %}
  {% tab User Onboarding %}

Sua primeira impressão com um usuário é, talvez, a mais crítica. Isso pode ser decisivo para futuras visitas ao seu app. Suas comunicações iniciais com o usuário devem ter um tempo sensato e incentivar visitas frequentes ao seu app para promover o uso.

<table class="tg">
<thead>
  <tr>
    <th>Etapa do canva</th>
    <th>Postergação</th>
    <th>Público</th>
    <th>Canal</th>
    <th>Expiração</th>
    <th>Avançar</th>
    <th>Informações</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Envio de e-mail de boas-vindas</td>
    <td>Nenhuma</td>
    <td>Tudo a partir da entrada</td>
    <td>E-mail</td>
    <td>N/D</td>
    <td>Avanço do público após a postergação</td>
    <td>Envio de e-mail inicial que dá as boas-vindas aos seus usuários em um projeto, associação ou outro programa de integração. <br><br>O objetivo é levar os usuários ao seu app para iniciar a integração.</td>
  </tr>
  <tr>
    <td>Mensagem no app do Dia 3-6</td>
    <td>3 dias após o usuário receber a etapa anterior</td>
    <td>Tudo a partir da entrada</td>
    <td>Mensagem no app</td>
    <td><b>Expira:</b> 3 dias após a etapa estar disponível</td>
    <td>Mensagem no app ao vivo</td>
    <td>Se o usuário tiver agido de acordo com o e-mail e tiver sido direcionado para o app, ele receberá a mensagem no app desejada para continuar ou lembrá-lo da integração e de quaisquer requisitos associados a ela.</td>
  </tr>
  <tr>
    <td>Push do dia 5 </td>
    <td>2 dias após o usuário receber a etapa anterior</td>
    <td>Tudo a partir da entrada</td>
    <td>Push</td>
    <td>N/D</td>
    <td>Mensagem enviada</td>
    <td>Depois que os usuários receberem a mensagem no app, eles receberão um push de acompanhamento para continuar a integração.</td>
  </tr>
</tbody>
</table>

Essas mensagens push são espaçadas em torno de uma mensagem no app para garantir que o usuário tenha visitado o app e iniciado sua integração. Isso ajuda a prevenir qualquer spam ou envio de mensagens fora de ordem que possa desestimular os usuários a visitar seu app, e em vez disso, criar uma ordem fluida e sensata para suas experiências iniciais com seu app.

  {% endtab %}
{% endtabs %}


## Priorização de mensagens no app

Um usuário pode disparar duas mensagens no app dentro do seu Canva ao mesmo tempo. Quando isso acontecer, o Braze seguirá a seguinte ordem de prioridade para determinar qual mensagem no app será exibida. 

Selecione **Definir prioridade exata** e arraste diferentes etapas do Canva para reordenar sua prioridade para o Canva. Por padrão, as primeira etapas de uma variante do canva serão exibidas antes das últimas. Depois que suas etapas estiverem na ordem de priorização preferida, selecione **Aplicar ordenação**.

![O organizador de prioridade com duas etapas "Bem-vindo IAM" e "Followup IAM".]({% image_buster /assets/img_archive/canvas_priority2.png %}){: style="max-width:85%"}

### Fazendo alterações em rascunhos de Canvases ativos

Se você fizer alterações na prioridade da mensagem no app em **Configurações de Envio** de um rascunho de um Canvas ativo, essas alterações são aplicadas diretamente ao Canvas ativo quando o organizador de prioridade é fechado. No entanto, em uma etapa de Mensagem, o organizador de prioridade será atualizado quando o rascunho for lançado, uma vez que as configurações da etapa do Canva se aplicam em nível de etapa. 

## Comportamento de avanço

As etapas de Mensagem avançam automaticamente todos os usuários que entram na etapa. Observe que não espera que a mensagem no app seja disparada ou exibida. Não há necessidade de especificar o comportamento de avanço de mensagens, o que simplifica a configuração da etapa geral.

Quando um usuário entra em uma etapa de mensagem no app, ele avança imediatamente para fora dela em vez de ser retido pela janela de expiração. Nesse caso, ter uma etapa de Postergação na jornada do usuário pode ser útil.

Para usar a opção **Avançar quando a mensagem for enviada**, adicione um [caminho do público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) separado para filtrar usuários que não receberam a etapa anterior.

{% details Original Canvas editor %}

Não é mais possível criar ou duplicar Canvas usando o editor original. Esta seção está disponível para referência ao entender como o comportamento de avanço funciona para etapas com mensagens no app.

As telas criadas no editor original precisam especificar um comportamento de avanço - os critérios para avançar em seu componente Canvas. [Etapas com apenas mensagens no app](#steps-iam-only) têm opções de avanço diferentes de [etapas com múltiplos tipos de mensagens](#steps-multiple-channels) (como push ou e-mail). Para mensagens no app no fluxo de trabalho atual do Canva, esta opção está definida para sempre avançar imediatamente o público.

A entrega baseada em ação não está disponível para etapas do Canva com mensagens no app. As etapas do canva com mensagens no app devem ser agendadas. Em vez disso, as mensagens no app do Canvas aparecerão na primeira vez que o usuário abrir o app (disparadas pela sessão inicial) depois que a mensagem programada no componente do Canvas tiver sido enviada a ele.

Se houver várias mensagens no app em um Canva, o usuário deverá iniciar várias sessões para receber cada uma dessas mensagens individuais.

{% alert important %}
Quando **Advance When In-App Message Live** for selecionado, a mensagem no app ficará disponível até expirar, mesmo que o usuário tenha passado para as etapas seguintes. Se você não quiser que a mensagem no app esteja ativa quando as próximas etapas do Canva forem entregues, certifique-se de que a expiração seja menor do que a postergação nas etapas subsequentes.
{% endalert %}

#### Etapas com vários canais {#steps-multiple-channels}

As etapas com uma mensagem no app e outro canal têm as seguintes opções de avanço:

| Opção | Descrição |
|---|---|---|
| Avançar quando uma mensagem for enviada | Os usuários devem receber uma notificação por e-mail, webhook ou push, ou visualizar a mensagem no app para avançar para as etapas subsequentes no Canva.  <br> <br>  Se a mensagem no app expirar e o usuário não tiver recebido o envio de e-mail, webhook ou push, ou não tiver visualizado a mensagem no app, ele sairá do Canvas e não avançará para as etapas subsequentes. |
| Avançar público imediatamente | Todos no público da etapa avançam para as próximas etapas após o término da postergação, quer tenham visto a mensagem notada ou não. <br> <br> Os usuários devem corresponder ao segmento da etapa e aos critérios de filtro para avançar para as próximas etapas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Quando a opção **Todo o público** for selecionada, a mensagem no app ficará disponível até expirar, mesmo que o usuário tenha passado para as etapas seguintes. Se não quiser que a mensagem no app esteja ativa quando as próximas etapas do canva forem entregues, verifique se a expiração é mais curta do que a postergação nas etapas subsequentes.
{% endalert %}

{% enddetails %}

## Ações de gatilho

Você pode escolher entre as seguintes ações de disparo para segmentar seus usuários:

- **Fazer Compra:** Segmentar usuários que fazem qualquer compra ou uma compra específica
- **Iniciar Sessão:** Segmentar usuários que iniciam uma sessão em qualquer app ou em um app específico
- **Realizar evento personalizado:** Alvo usuários que realizam o evento personalizado selecionado (o evento personalizado deve ser enviado usando o SDK).

Um usuário precisa entrar na etapa do canva, iniciar uma sessão e então realizar o disparo para receber uma mensagem no app. Isso significa que atualizações durante a sessão não são suportadas. Por exemplo, se o disparo for para iniciar uma sessão, o usuário só precisa entrar na etapa do canva e iniciar uma sessão para receber a mensagem no app. Se o disparo não for para iniciar uma sessão, o usuário precisa entrar na etapa do canva, iniciar uma sessão e então realizar o disparo para receber a mensagem no app.

!["Fazer Uma Compra Específica" selecionado como a ação-gatilho.]({% image_buster /assets/img_archive/canvas_trigger_actions.png %}){: style="max-width:90%"}

Os seguintes recursos do canva não estão disponíveis com mensagens no app, então não serão aplicados às suas mensagens no app, mesmo que estejam ativados.

- Intelligent Timing
- Limite de taxa
- Limite de frequência
- Critérios de saída
- Horário de silêncio

## Propriedades de eventos personalizados em um Canva

Propriedades de evento personalizado em mensagens no app para o canva são suportadas. No entanto, essas propriedades são do evento personalizado ou compra que dispara a mensagem no app, que está localizada na etapa da Mensagem, não no caminho de ação anterior.

## Considerações

Aqui estão algumas considerações ao enviar mensagens no app em um canva.

- Se o usuário nunca reiniciar o app ou nunca iniciar uma sessão, o app não conseguirá descobrir se o usuário é elegível para a mensagem no app, o que significa que uma mensagem no app não será enviada.
- Quando o primeiro clique ocorre e há uma variável de contexto do canva (propriedades de entrada do canva), e um usuário reentra no canva cinco vezes, a Braze pegará a quinta entrada e usará essa variável de contexto na mensagem no app.
- Um usuário pode ser elegível para até 10 mensagens no app dentro da mesma etapa do canva. Por exemplo, se um canva permite reentrada e um usuário entra no canva 11 vezes, ele só receberá 10 mensagens no app se nenhuma tiver expirado.
