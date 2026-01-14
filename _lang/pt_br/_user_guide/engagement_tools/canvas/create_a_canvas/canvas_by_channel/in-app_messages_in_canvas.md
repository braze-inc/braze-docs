---
nav_title: Mensagens no aplicativo
article_title: Mensagens no aplicativo no Canvas
alias: "/canvas_in-app_messages/"
page_order: 2
page_type: reference
description: "Este artigo de referência descreve os recursos e as nuances específicos das mensagens in-app que você pode adicionar ao Canvas para exibir mensagens sofisticadas."
tool: Canvas
channel: in-app messages

---

# Mensagens in-app no Canvas

> Você pode adicionar mensagens in-app como parte da jornada do Canvas para exibir mensagens avançadas quando o cliente se envolver com o aplicativo.

## Como funciona

Antes de usar mensagens in-app em seu Canvas, certifique-se de ter um [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) configurado com opções de atraso e público.

No construtor do Canvas, adicione uma etapa [de Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) e selecione **Mensagem no aplicativo** como seu **canal de mensagens**. Você pode personalizar [quando sua mensagem expirará](#in-app-message-expiration) e qual [comportamento de avanço](#advancement-behavior) ela terá.

## Adicionar uma mensagem in-app à jornada do usuário

Para adicionar uma mensagem no aplicativo ao seu Canvas, faça o seguinte:

1. Adicione uma etapa [de Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) à jornada do usuário.
2. Selecione **In-App Message** para seu **canal de mensagens**. 
3. Determine [quando sua mensagem expirará](#in-app-message-expiration) e qual [comportamento de avanço](#advancement-behavior-options) ela terá.

## Mensagens acionadas no aplicativo

Você pode selecionar um acionador para que suas mensagens in-app sejam acionadas no início da sessão ou por eventos e compras personalizados.

Depois que os atrasos passam e as opções de público-alvo são verificadas, as mensagens in-app são definidas para serem exibidas quando um usuário chega à etapa Mensagem. Se um usuário iniciar uma sessão e executar o evento de disparo para a mensagem in-app, ele verá a mensagem in-app. 

Para as etapas do Canvas que têm entrada acionada por ação, os usuários podem entrar no Canvas no meio da sessão. As mensagens in-app não são definidas para serem ativadas até o início de uma sessão, portanto, se um usuário estiver no meio de uma sessão quando chegar à etapa Mensagem, ele não receberá a mensagem in-app até iniciar outra sessão e executar o acionador relevante.

## Expiração de mensagens no aplicativo

Você pode escolher quando a mensagem no aplicativo expirará. Durante esse período, a mensagem no aplicativo ficará esperando para ser visualizada até atingir a data de expiração. Depois que a mensagem no aplicativo é enviada, ela pode ser visualizada uma única vez.

\![A seção Controles de mensagem de uma etapa de mensagem para uma mensagem in-app. A mensagem no aplicativo expirará três dias depois que a etapa estiver disponível.]({% image_buster /assets/img_archive/canvas_expiration2.png %}){: style="max-width:90%"}

| Opção | Descrição | Exemplo |
|---|---|---|
| **Uma duração após a etapa está disponível** | Define a mensagem in-app para expirar em relação a quando a etapa se torna disponível para o usuário. | Uma mensagem in-app com expiração de dois dias ficaria disponível quando o usuário entrasse na etapa Mensagem e as opções de público fossem marcadas. Quaisquer atrasos antes de chegar a essa etapa seriam provenientes das etapas anteriores de Atraso em seu Canvas. A mensagem no aplicativo ficaria disponível por dois dias (48 horas) a partir do momento em que o usuário entrasse na etapa e, durante esses dois dias, os usuários poderiam ver a mensagem no aplicativo se abrissem o aplicativo. |
| **Em uma data e hora específicas** | Selecione uma data e hora específicas em que a mensagem no aplicativo não estará mais disponível. | Se você tiver uma venda que termina em 30 de novembro de 2024, selecione essa opção para que os usuários não vejam mais a mensagem in-app associada quando a venda terminar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Casos de uso

A Braze recomenda que você considere o uso desse recurso em seus Canvases promocionais e de integração.

{% tabs %}
  {% tab Promotional %}

As promoções, os cupons e as vendas geralmente têm datas de validade rígidas. O Canvas a seguir deve alertar seus usuários, nos momentos mais oportunos, de que há uma promoção que eles podem usar e, talvez, influenciar uma compra. Essa promoção expira em 28 de fevereiro de 2019, às 11h15 no fuso horário de sua empresa.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>Etapa da tela</th>
    <th>Atraso</th>
    <th>Público</th>
    <th>Canal</th>
    <th>Vencimento</th>
    <th>Avanço</th>
    <th>Detalhes</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Dia 1: 50% de desconto</td>
    <td>Nenhum</td>
    <td>Tudo a partir da entrada</td>
    <td>Empurrar</td>
    <td>N/A</td>
    <td>Audiência prévia após o atraso</td>
    <td>Push inicial que alerta seus usuários sobre a promoção. Isso tem como objetivo levar os usuários ao seu aplicativo para aproveitar a promoção.</td>
  </tr>
  <tr>
    <td>No aplicativo: 50% de desconto</td>
    <td>Nenhum</td>
    <td>Tudo a partir da entrada</td>
    <td>Mensagem no aplicativo</td>
    <td><b>Expira por:</b> 2/28/2019 11:15 AM Horário da empresa</td>
    <td>Mensagem no aplicativo visualizada</td>
    <td>O usuário agora abriu o aplicativo e receberá essa mensagem, seja ou não por causa da mensagem push anterior.</td>
  </tr>
  <tr>
    <td>Lembrete de 50% de desconto</td>
    <td>1 dia após o usuário receber a etapa anterior</td>
    <td>Tudo a partir da entrada <br><br><b>Filtro:</b> A última compra foi feita há mais de uma semana</td>
    <td>Mensagem no aplicativo</td>
    <td><b>Expira por:</b> 2/28/2019 11:15 AM Horário da empresa</td>
    <td>Nenhum (última mensagem no Canvas)</td>
    <td>O usuário recebeu a mensagem in-app na etapa anterior, mas não fez uma compra, apesar de estar no aplicativo. <br><br>Essa mensagem tem o objetivo de atrair ainda mais o usuário para fazer uma compra usando a promoção.</td>
  </tr>
</tbody>
</table>

As mensagens no aplicativo expiram quando a promoção expira para evitar discrepâncias entre as mensagens e a experiência do cliente.

  {% endtab %}
  {% tab User Onboarding %}

Sua primeira impressão com um usuário é, talvez, a mais crítica. Isso pode ser decisivo para futuras visitas ao seu aplicativo. Suas comunicações iniciais com o usuário devem ser programadas de forma sensata e incentivar visitas frequentes ao aplicativo para promover o uso.

<table class="tg">
<thead>
  <tr>
    <th>Etapa da tela</th>
    <th>Atraso</th>
    <th>Público</th>
    <th>Canal</th>
    <th>Vencimento</th>
    <th>Avanço</th>
    <th>Detalhes</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>E-mail de boas-vindas</td>
    <td>Nenhum</td>
    <td>Tudo a partir da entrada</td>
    <td>E-mail</td>
    <td>N/A</td>
    <td>Avanço do público após o atraso</td>
    <td>E-mail inicial que dá as boas-vindas aos seus usuários em um projeto, associação ou outro programa de integração. <br><br>O objetivo é levar os usuários ao seu aplicativo para iniciar a integração.</td>
  </tr>
  <tr>
    <td>Dia 3-6 mensagem no aplicativo</td>
    <td>3 dias após o usuário receber a etapa anterior</td>
    <td>Tudo a partir da entrada</td>
    <td>Mensagem no aplicativo</td>
    <td><b>Expira:</b> 3 dias após a etapa estar disponível</td>
    <td>Mensagem no aplicativo ao vivo</td>
    <td>Se o usuário tiver agido de acordo com o e-mail e tiver sido direcionado para o aplicativo, ele receberá a mensagem desejada no aplicativo para continuar ou lembrá-lo da integração e de quaisquer requisitos associados a ela.</td>
  </tr>
  <tr>
    <td>Empurrar no dia 5 </td>
    <td>2 dias após o usuário receber a etapa anterior</td>
    <td>Tudo a partir da entrada</td>
    <td>Empurrar</td>
    <td>N/A</td>
    <td>Mensagem enviada</td>
    <td>Depois que os usuários receberem a mensagem no aplicativo, eles receberão um push de acompanhamento para continuar a integração.</td>
  </tr>
</tbody>
</table>

Essas mensagens push são espaçadas em torno de uma mensagem no aplicativo para garantir que o usuário tenha visitado o aplicativo e iniciado sua integração. Isso ajuda a evitar qualquer spam ou mensagem fora de ordem que possa dissuadir os usuários de visitar seu aplicativo e, em vez disso, criar uma ordem fluida e sensata para as experiências iniciais deles com seu aplicativo.

  {% endtab %}
{% endtabs %}


## Priorização de mensagens in-app

Um usuário pode acionar duas mensagens in-app no Canvas ao mesmo tempo. Quando isso acontecer, o Braze seguirá a seguinte ordem de prioridade para determinar qual mensagem no aplicativo será exibida. 

Selecione **Definir prioridade exata** e arraste diferentes etapas do Canvas para reordenar sua prioridade no Canvas. Por padrão, as etapas anteriores em uma variante do Canvas serão exibidas antes das etapas posteriores. Depois que as etapas estiverem em sua ordem preferida de priorização, selecione **Aplicar classificação**.

O classificador de prioridades com duas etapas: "Welcome IAM" e "Followup IAM".]({% image_buster /assets/img_archive/canvas_priority2.png %}){: style="max-width:85%"}

### Fazer alterações em rascunhos de telas ativas

Se você fizer alterações na prioridade de mensagens no aplicativo em **Configurações** de **envio** de um rascunho de um Canvas ativo, essas alterações serão aplicadas diretamente ao Canvas ativo quando o classificador de prioridades for fechado. No entanto, em uma etapa de Mensagem, o classificador de prioridades será atualizado quando o rascunho for iniciado, pois as configurações da etapa do Canvas se aplicam em um nível de etapa. 

## Comportamento de avanço

As etapas de mensagem avançam automaticamente todos os usuários que entram na etapa. Observe que ele não espera que a mensagem in-app seja acionada ou exibida. Não há necessidade de especificar o comportamento de avanço da mensagem, o que simplifica a configuração da etapa geral.

Quando um usuário entra em uma etapa de mensagem in-app, ele sai dela imediatamente, em vez de ser retido pela janela de expiração. Nesse caso, ter uma etapa de Atraso na jornada do usuário pode ser útil.

Para usar a opção **Advance when message sent**, adicione um [caminho de público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) separado para filtrar os usuários que não receberam a etapa anterior.

{% details Original Canvas editor %}

Não é mais possível criar ou duplicar Canvases usando o editor original. Esta seção está disponível para referência ao entender como o comportamento de avanço funciona para etapas com mensagens in-app.

As telas criadas no editor original precisam especificar um comportamento de avanço - os critérios de avanço no componente Canvas. [As etapas com apenas mensagens in-app](#steps-iam-only) têm opções de avanço diferentes das [etapas com vários tipos de mensagens](#steps-multiple-channels) (como push ou e-mail). Para mensagens in-app no fluxo de trabalho atual do Canvas, essa opção é definida para sempre avançar imediatamente o público.

A entrega baseada em ação não está disponível para etapas do Canvas com mensagens no aplicativo. As etapas do Canvas com mensagens no aplicativo devem ser agendadas. Em vez disso, as mensagens in-app do Canvas aparecerão na primeira vez que o usuário abrir o aplicativo (acionado pela sessão inicial) depois que a mensagem programada no componente Canvas tiver sido enviada a ele.

Se você tiver várias mensagens in-app em um Canvas, o usuário deverá iniciar várias sessões para receber cada uma dessas mensagens individuais.

{% alert important %}
Quando **Advance When In-App Message Live** for selecionado, a mensagem in-app ficará disponível até expirar, mesmo que o usuário tenha passado para as etapas seguintes. Se você não quiser que a mensagem in-app esteja ativa quando as próximas etapas do Canvas forem entregues, certifique-se de que a expiração seja mais curta do que o atraso nas etapas subsequentes.
{% endalert %}

#### Etapas com vários canais {#steps-multiple-channels}

As etapas com uma mensagem in-app e outro canal têm as seguintes opções de avanço:

| Opção | Descrição |
|---|---|---|
| Avanço quando a mensagem é enviada | Os usuários devem receber uma notificação por e-mail, webhook ou push, ou visualizar a mensagem no aplicativo para avançar para as etapas subsequentes no Canvas.  <br> <br>  Se a mensagem in-app expirar e o usuário não tiver recebido o e-mail, webhook ou push, ou não tiver visualizado a mensagem in-app, ele sairá do Canvas e não avançará para as etapas subsequentes. |
| Avanço imediato do público | Todos no público-alvo da etapa avançam para as próximas etapas após o término do atraso, independentemente de terem visto ou não a mensagem registrada. <br> <br> Os usuários devem corresponder ao segmento da etapa e aos critérios de filtro para avançar para as próximas etapas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Quando a opção **Entire Aud** ience for selecionada, a mensagem in-app ficará disponível até expirar, mesmo que o usuário tenha passado para as etapas seguintes. Se você não quiser que a mensagem in-app esteja ativa quando as próximas etapas do Canvas forem entregues, verifique se a expiração é menor do que o atraso nas etapas subsequentes.
{% endalert %}

{% enddetails %}

## Ações de acionamento

Você pode escolher entre as seguintes ações de acionamento para direcionar seus usuários:

- **Faça a compra:** Direcionar usuários que fazem qualquer compra ou uma compra específica
- **Iniciar sessão:** Segmente usuários que iniciam uma sessão em qualquer aplicativo ou em um aplicativo específico
- **Executar evento personalizado:** Usuários-alvo que realizam o evento personalizado selecionado (o evento personalizado deve ser enviado usando o SDK).

Um usuário precisa entrar na etapa do Canvas, iniciar uma sessão e, em seguida, executar o acionador para receber uma mensagem no aplicativo. Isso significa que não há suporte para atualizações no meio da sessão. Por exemplo, se o acionador for para iniciar uma sessão, o usuário só precisará entrar na etapa do Canvas e iniciar uma sessão para receber a mensagem in-app. Se o acionador não for para iniciar uma sessão, o usuário terá que entrar na etapa do Canvas, iniciar uma sessão e, em seguida, executar o acionador para receber a mensagem in-app.

\!["Make A Specific Purchase" (Fazer uma compra específica) selecionado como a ação de acionamento.]({% image_buster /assets/img_archive/canvas_trigger_actions.png %}){: style="max-width:90%"}

Os seguintes recursos do Canvas não estão disponíveis nas mensagens in-app, portanto, não serão aplicados às suas mensagens in-app, mesmo que estejam ativados.

- Cronograma inteligente
- Limitação de taxa
- Limite de frequência
- Critérios de saída
- Horas de silêncio

## Propriedades de eventos personalizados em um Canvas

Há suporte para propriedades de eventos personalizados em mensagens in-app para o Canvas. No entanto, essas propriedades são do evento personalizado ou da compra que aciona a mensagem in-app, que está localizada na etapa Mensagem, e não no caminho de ação anterior.

## Considerações

Aqui estão algumas considerações ao enviar mensagens no aplicativo em um Canvas.

- Se o usuário nunca reiniciar o aplicativo ou nunca iniciar uma sessão, o aplicativo não conseguirá descobrir se o usuário está qualificado para a mensagem in-app, o que significa que a mensagem in-app não será enviada.
- Quando ocorrer o primeiro clique e houver uma variável de contexto do Canvas (propriedades de entrada do Canvas), e um usuário entrar novamente em um Canvas cinco vezes, o Braze pegará a quinta entrada e usará essa variável de contexto na mensagem no aplicativo.
- Um usuário só pode ser elegível para 10 mensagens in-app por vez. Por exemplo, se um usuário passar por diferentes etapas do Canvas para 10 mensagens in-app, você só poderá ter até 10 dessas etapas.
