---
nav_title: Mensagens no app
article_title: Envio de mensagens no app no Canva
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

Depois que as postergações passarem e as opções de público forem verificadas, a mensagem no app será ativada e os usuários a verão se abrirem o aplicativo. As mensagens no app no Canvas só podem ser disparadas pelo evento de gatilho `start session` — elas não podem ser disparadas por eventos personalizados em um componente do Canvas.

Para etapas do Canva que têm entrada acionada por ação, os usuários podem entrar no Canvas no meio da sessão. No entanto, conforme notado acima, as mensagens no app não serão disparadas até o início da próxima sessão, portanto, esses usuários perderiam a mensagem inicial no app, pois não eram elegíveis para entrar no Canvas antes do início da sessão.

## Adicionar uma mensagem no app à jornada do usuário

Para adicionar uma mensagem no app ao seu Canva, faça o seguinte:

1. Adicione uma etapa de [Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) à jornada do usuário.
2. Selecione **Mensagem no app** para seu **canal de envio de mensagens**. 
3. Determine [quando sua mensagem expirará](#in-app-message-expiration) e qual [comportamento de avanço](#advancement-behavior-options) ela terá.

### Expiração de mensagens no app

No editor de mensagens no app, você pode escolher quando a mensagem no app expirará. Durante esse tempo, a mensagem no app ficará "parada" e aguardará para ser visualizada até atingir a data de vencimento. Depois que a mensagem no app é enviada, ela pode ser visualizada uma única vez.

![][1]

| Opção | Descrição | Exemplo |
|---|---|---|
| A mensagem expira após o período especificado | A primeira opção permite expirar a mensagem no app em relação a quando a etapa se torna disponível para o usuário. | Por exemplo, uma mensagem no app com uma expiração de dois dias ficaria disponível depois que a postergação da etapa passasse e as opções de público fossem verificadas. Em seguida, ficaria disponível por dois dias (48 horas) e, durante esses dois dias, os usuários poderão ver a mensagem no app se abrirem o aplicativo. |
| A mensagem expira em uma data específica | A segunda opção permite que você escolha uma data e hora específicas em que a mensagem no app não estará mais disponível. | Por exemplo, se você tiver uma venda que terminou em uma data e hora específicas, poderá selecionar essa opção para que os usuários não vejam mais a mensagem no app associada quando a venda terminar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Casos de uso

Você pode usar mensagens no app em seus Canvas promocionais e de integração.

{% tabs %}
  {% tab Promocional %}

As promoções, os cupons e as vendas geralmente têm datas de expiração rígidas. O Canva a seguir deve alertar seus usuários, nos momentos mais oportunos, de que há uma promoção que eles podem usar e, talvez, influenciar uma compra. Essa promoção expira em 28 de fevereiro de 2019, às 11h15, no fuso horário da empresa.

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

Como você pode ver, as mensagens push são espaçadas em torno de uma mensagem no app para garantir que o usuário tenha visitado o aplicativo e iniciado sua integração. Isso evitará qualquer spam irritante ou envio de mensagens fora de ordem que possam dissuadir os usuários de visitar seu aplicativo e, em vez disso, criará uma ordem fluida e sensata para as experiências iniciais deles no app.

  {% endtab %}
{% endtabs %}

### Opções de comportamento de avanço

No Canva, as etapas de mensagens avançam automaticamente todos os usuários que entram na etapa. Para usar a opção **Avançar quando uma mensagem for enviada**, adicione uma [jornada do público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) separada para filtrar os usuários que não receberam a etapa anterior.

{% details Comportamento do editor de tela original %}

{% alert important %}
Não é mais possível criar ou duplicar Canvas usando o editor original. Esta seção está disponível para referência ao entender como o comportamento de avanço funciona para etapas com mensagens no app.
{% endalert %}

As telas criadas no editor original precisam especificar um comportamento de avanço - os critérios para avançar em seu componente Canvas. [As etapas com apenas mensagens no app](#steps-iam-only) têm opções de avanço diferentes das [etapas com vários tipos de mensagens](#steps-multiple-channels) (push, e-mail etc.). Para mensagens no app em um fluxo de trabalho do Canvas Flow, essa opção é definida para sempre avançar imediatamente o público.

A entrega baseada em ação não está disponível para etapas do Canva com mensagens no app. As etapas do canva com mensagens no app devem ser agendadas. Em vez disso, as mensagens no app do Canvas aparecerão na primeira vez que o usuário abrir o app (disparadas pela sessão inicial) depois que a mensagem programada no componente do Canvas tiver sido enviada a ele.

Se houver várias mensagens no app em um Canva, o usuário deverá iniciar várias sessões para receber cada uma dessas mensagens individuais.

{% alert important %}
As mensagens no app não podem ser disparadas por eventos no Canva.
{% endalert %}

![][2]

{% alert important %}
Quando **Advance When In-App Message Live** for selecionado, a mensagem no app ficará disponível até expirar, mesmo que o usuário tenha passado para as etapas seguintes. Se você não quiser que a mensagem no app esteja ativa quando as próximas etapas do Canva forem entregues, certifique-se de que a expiração seja menor do que a postergação nas etapas subsequentes.
{% endalert %}

#### Etapas com vários canais {#steps-multiple-channels}

As etapas com uma mensagem no app e outro canal têm as seguintes opções de avanço:

| Opção | Descrição |
|---|---|---|
| Avançar quando uma mensagem for enviada | Os usuários devem receber uma notificação por e-mail, webhook ou push, ou visualizar a mensagem no app para avançar para as etapas subsequentes no Canva.  <br> <br>  Se a mensagem no app expirar e o usuário não tiver recebido o envio de e-mail, webhook ou push, ou não tiver visualizado a mensagem no app, ele sairá do Canvas e não avançará para as etapas subsequentes. |
| Avançar público imediatamente | Todos no público da etapa avançam para as próximas etapas após o término da postergação, quer tenham visto a mensagem notada ou não.  <br> <br> Os usuários devem corresponder ao segmento da etapa e aos critérios de filtro para avançar para as próximas etapas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][3]

{% alert important %}
Quando a opção **Todo o público** for selecionada, a mensagem no app ficará disponível até expirar, mesmo que o usuário tenha passado para as etapas seguintes. Se não quiser que a mensagem no app esteja ativa quando as próximas etapas do canva forem entregues, verifique se a expiração é mais curta do que a postergação nas etapas subsequentes.
{% endalert %}

{% enddetails %}

## Priorização de mensagens no app

Um cliente pode disparar duas mensagens no app em seu canva ao mesmo tempo. Quando isso acontecer, o Braze seguirá a seguinte ordem de prioridade para determinar qual mensagem no app será exibida. Arraste diferentes etapas do Canva para reordenar sua prioridade. Por padrão, as primeira etapas de uma variante do canva serão exibidas antes das últimas.

![]({% image_buster /assets/img_archive/step_priority.png %}){: style="max-width:80%"}

Acesse as **Configurações de envio** da seção Canvas para priorizar as mensagens no app de um Canvas em relação às mensagens no app de outros Canvases e campanhas.

![]({% image_buster /assets/img_archive/canvas_send_settings.png %})

Por padrão, a prioridade dos componentes do Canva é definida como média, sendo que as etapas criadas mais recentemente têm a prioridade relativa mais alta. As prioridades em nível de canvas e de campanha também são padronizadas como médias, sendo que a prioridade relativa mais alta é padronizada para os itens criados mais recentemente.

![]({% image_buster /assets/img_archive/canvas_priority.png %}){: style="max-width:85%"}

### Rascunhos de um Canva ativo

Ao editar um rascunho de um Canva ativo, as alterações na prioridade de mensagem no app em **Configurações de envio** não são salvas com um rascunho. Essas alterações são aplicadas diretamente à tela ativa quando o modal do classificador de prioridades é fechado. No entanto, em uma etapa de Mensagem, o classificador de prioridades será atualizado quando um usuário iniciar o rascunho, já que as configurações da etapa se aplicam em um nível de etapa.

## Propriedades de eventos personalizados em um Canva

A entrega baseada em ação não está disponível para etapas do Canva com mensagens no app. Isso significa que você também não pode usar propriedades de eventos personalizados para essas etapas. 

Para modelar as propriedades do evento no Canvas, recomendamos armazenar as propriedades do evento como atributos personalizados em sua primeira etapa do Canva e personalizar sua mensagem no app com os atributos personalizados na segunda etapa.


[1]: {% image_buster /assets/img/expires-after.png %} "IAM Live"
[2]: {% image_buster /assets/img/iam-advancement-behavior.png %} "IAM Live"
[3]: {% image_buster /assets/img/push-advancement-behavior.png %} "IAM Live"
