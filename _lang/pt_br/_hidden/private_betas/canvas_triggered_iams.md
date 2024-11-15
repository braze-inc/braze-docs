---
article_title: Mensagens no app na canva
permalink: /canvas_triggered_in-app_messages/
page_type: reference
description: "Este artigo de referência descreve os recursos e as nuances específicas das mensagens no app do Canvas, que podem ser adicionadas ao Canvas para exibir envios de mensagens sofisticadas."
---

# Mensagens no app no Canva

> As mensagens no app podem ser adicionadas como parte da jornada do canva para mostrar mensagens ricas quando o cliente se engaja com o aplicativo. Este artigo descreve os recursos e as nuances específicas das mensagens no app do Canva.

Antes de continuar, você já deve ter [criado seu Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) e configurado as opções de postergação e público.

No construtor do Canva, adicione uma etapa [de Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) e selecione **Mensagem no app** como seu **canal de envio de mensagens**. Você pode personalizar [quando sua mensagem expirará](#in-app-message-expiration) e qual [comportamento de avanço](#advancement-behavior) ela terá.

## Mensagens no app disparadas

{% alert important %}
As ações-gatilho para mensagens no app estão atualmente em acesso antecipado. Entre em contato com seu gerente de conta se estiver interessado em participar deste acesso antecipado.<br><br>Anteriormente, não havia a opção de selecionar um disparo, o que significava que as mensagens no app eram sempre disparadas no início da sessão. Agora, há uma opção para selecionar um gatilho, o que significa que as mensagens no app podem ser disparadas no início da sessão ou por eventos e compras personalizados. As mensagens no app criadas antes desse recurso terão o início da sessão como disparador.
{% endalert %}

Depois que as postergações passam e as opções de público são verificadas, as mensagens no app são definidas para serem transmitidas quando um usuário chega à etapa Mensagem. Se um usuário iniciar uma sessão e executar o evento de gatilho para a mensagem no app, o usuário verá a mensagem no app. 

Para etapas do Canva que têm entrada acionada por ação, os usuários podem entrar no Canvas no meio da sessão. As mensagens no app não são definidas para serem ativadas até que uma sessão seja iniciada, portanto, se um usuário estiver no meio da sessão quando chegar à etapa Mensagem, ele não receberá a mensagem no app até que inicie outra sessão e dispare o comando relevante.

## Expiração de mensagens no app

No criador de mensagens no app, você pode escolher quando a mensagem no app expirará. Durante esse tempo, a mensagem no app ficará aguardando para ser visualizada até atingir a data de vencimento. Depois que a mensagem no app é enviada, ela pode ser visualizada uma única vez.

![]({% image_buster /assets/img_archive/canvas_expiration2.png %}){: style="max-width:85%"}

| Opção | Descrição | Exemplo |
|---|---|---|
| **Uma duração após a etapa está disponível** | Define a mensagem no app para expirar em relação a quando a etapa se torna disponível para o usuário. | Uma mensagem no app com expiração de dois dias ficaria disponível após o término da postergação da etapa e a verificação das opções do público. Em seguida, ficaria disponível por dois dias (48 horas) e, durante esses dois dias, os usuários poderão ver a mensagem no app se abrirem o aplicativo. |
| **Em uma data e horário específicas** | Selecione uma data e hora específicas em que a mensagem no app não estará mais disponível. | Se tiver uma venda que termina em 30 de novembro de 2024, selecione essa opção para que os usuários não vejam mais a mensagem no app associada quando a venda terminar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Casos de uso

Quando você deve usar esse recurso? A Braze recomenda enfaticamente que você considere o uso desse recurso em suas canvas promocionais e de integração.

{% tabs %}
  {% tab Promocional %}

As promoções, os cupons e as vendas geralmente têm datas de expiração rígidas. O Canva a seguir deve alertar seus usuários, nos momentos mais oportunos, de que há uma promoção que eles podem usar e, talvez, influenciar uma compra. Essa promoção expira em 28 de fevereiro de 2019, às 11h15 no fuso horário de sua empresa.

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

Como você pode ver, as mensagens no app expiram quando a promoção expira para evitar discrepâncias entre as mensagens e a experiência do cliente.

  {% endtab %}
  {% tab Integração do usuário %}

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
    <td>mensagem no app dos dias 3 a 6</td>
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

Essas mensagens push são espaçadas em torno de uma mensagem no app para garantir que o usuário tenha visitado o aplicativo e iniciado sua integração. Isso ajuda a evitar qualquer spam ou envio de mensagens fora de ordem que poderiam dissuadir os usuários de visitar seu aplicativo e, em vez disso, criar uma ordem fluida e sensata para as experiências iniciais deles no app.

  {% endtab %}
{% endtabs %}


## Priorização de mensagens no app

Um usuário pode disparar duas mensagens no app dentro do seu Canva ao mesmo tempo. Quando isso acontecer, o Braze seguirá a seguinte ordem de prioridade para determinar qual mensagem no app será exibida. 

Selecione **Definir prioridade exata** e arraste diferentes etapas do Canva para reordenar sua prioridade para o Canvas. Por padrão, as primeira etapas de uma variante do canva serão exibidas antes das últimas. Depois que as etapas estiverem em sua ordem preferida de priorização, selecione **Aplicar classificação**.

![]({% image_buster /assets/img_archive/canvas_priority2.png %}){: style="max-width:85%"}

### Fazer alterações em rascunhos de telas ativas

Se você fizer alterações na prioridade de mensagens no app em **Configurações** de **envio** de um rascunho de um Canvas ativo, essas alterações serão aplicadas diretamente ao Canvas ativo quando o classificador de prioridades for fechado. No entanto, em uma etapa do canva, o classificador de prioridades será atualizado quando o rascunho for iniciado, pois as configurações da etapa do canva se aplicam em um nível de etapa. 

## Comportamento de avanço

Os componentes de mensagens avançam automaticamente todos os usuários que entram na etapa. Observe que ele não espera que a mensagem no app seja disparada ou exibida. Não há necessidade de especificar o comportamento de avanço de mensagens, o que simplifica a configuração da etapa geral.

Quando um usuário entra em uma etapa de mensagem no app, ele avança imediatamente para fora dela, em vez de ficar retido na janela de expiração. Nesse caso, ter uma etapa de postergação na jornada do usuário pode ser útil.

Se quiser implementar a opção **Advance when message sent**, adicione uma [jornada de público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) separada para filtrar os usuários que não receberam a etapa anterior.

{% details Editor de tela original %}

{% alert important %}
Desde 28 de fevereiro de 2023, não é mais possível criar ou duplicar canvas usando o editor original. Esta seção está disponível para referência ao entender como o comportamento de avanço funciona para etapas com mensagens no app.
{% endalert %}

As telas criadas no editor original precisam especificar um comportamento de avanço - os critérios para avançar em seu componente Canvas. As [etapas com apenas mensagens no app](#steps-iam-only) têm opções de avanço diferentes das [etapas com vários tipos de mensagens](#steps-multiple-channels) (como push ou envio de e-mail). Para mensagens no app em um fluxo de trabalho do Canvas Flow, essa opção é definida para sempre avançar imediatamente o público.

A entrega baseada em ação não está disponível para etapas do Canva com mensagens no app. As etapas do canva com mensagens no app devem ser agendadas. Em vez disso, as mensagens no app do Canvas aparecerão na primeira vez que o usuário abrir o app (disparadas pela sessão inicial) depois que a mensagem programada no componente do Canvas tiver sido enviada a ele.

Se houver várias mensagens no app em um Canva, o usuário deverá iniciar várias sessões para receber cada uma dessas mensagens individuais.

![]({% image_buster /assets/img/iam-advancement-behavior.png %})

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

![]({% image_buster /assets/img/push-advancement-behavior.png %})

{% alert important %}
Quando a opção **Todo o público** for selecionada, a mensagem no app ficará disponível até expirar, mesmo que o usuário tenha passado para as etapas seguintes. Se não quiser que a mensagem no app esteja ativa quando as próximas etapas do canva forem entregues, verifique se a expiração é mais curta do que a postergação nas etapas subsequentes.
{% endalert %}

{% enddetails %}

## Ações de gatilho

Você pode escolher entre as seguintes ações-gatilho para direcionar seus usuários:

- **Faça a compra:** Direcionamento para usuários que fazem qualquer compra ou uma compra específica
- **Iniciar sessão:** Direcionamento para usuários que iniciam uma sessão em qualquer aplicativo ou em um aplicativo específico
- **Executar evento personalizado:** Direcionamento aos usuários que realizam o evento personalizado selecionado

Um usuário precisa entrar na etapa do Canva, iniciar uma sessão e, em seguida, disparar para receber uma mensagem no app. Isso significa que não há suporte para atualizações no meio da sessão. Por exemplo, se o disparo for para iniciar uma sessão, o usuário só precisará entrar na etapa do Canva e iniciar uma sessão para receber a mensagem no app. Se o disparador não for para iniciar uma sessão, o usuário deverá entrar na etapa do Canva, iniciar uma sessão e, em seguida, executar o disparador para receber a mensagem no app.

!["Fazer uma compra específica" selecionada como ação-gatilho.]({% image_buster /assets/img_archive/canvas_trigger_actions.png %}){: style="max-width:85%"}

Os seguintes recursos do Canva não estão disponíveis com mensagens no app, portanto, não serão aplicados às mensagens no app, mesmo que estejam ativados.

- Intelligent Timing
- Limite de taxa
- Limite de frequência
- Critérios de saída
- Horário de silêncio

## Propriedades de eventos personalizados em um Canva

Há suporte para propriedades de eventos personalizados em mensagens no app para o Canva. No entanto, essas propriedades são do evento personalizado ou da compra que dispara a mensagem no app, que está localizada na etapa Mensagem, e não na jornada de ação anterior.
