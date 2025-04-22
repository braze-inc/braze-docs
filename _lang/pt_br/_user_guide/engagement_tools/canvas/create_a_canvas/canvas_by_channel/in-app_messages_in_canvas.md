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

 

## Adicionar uma mensagem no app à jornada do usuário

Para adicionar uma mensagem no app ao seu Canva, faça o seguinte:

1. Adicione uma etapa de [Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) à jornada do usuário.
2. Selecione **Mensagem no app** para seu **canal de envio de mensagens**. 
3. Determine [quando sua mensagem expirará](#in-app-message-expiration) e qual [comportamento de avanço](#advancement-behavior-options) ela terá.

## 



  

Para etapas do Canva que têm entrada acionada por ação, os usuários podem entrar no Canvas no meio da sessão. 

## Expiração de mensagens no app

  Depois que a mensagem no app é enviada, ela pode ser visualizada uma única vez.



| Opção | Descrição | Exemplo |
|---|---|---|
|  |  |  Em seguida, ficaria disponível por dois dias (48 horas) e, durante esses dois dias, os usuários poderão ver a mensagem no app se abrirem o aplicativo. |
|  |  |  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Casos de uso



{% tabs %}
  {% tab Promocional %}

As promoções, os cupons e as vendas geralmente têm datas de expiração rígidas. O Canva a seguir deve alertar seus usuários, nos momentos mais oportunos, de que há uma promoção que eles podem usar e, talvez, influenciar uma compra. 

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

 

  {% endtab %}
{% endtabs %}


## Priorização de mensagens no app

 Quando isso acontecer, o Braze seguirá a seguinte ordem de prioridade para determinar qual mensagem no app será exibida. 

 Por padrão, as primeira etapas de uma variante do canva serão exibidas antes das últimas. 



### 

  

## 

  

 





Não é mais possível criar ou duplicar Canvas usando o editor original. Esta seção está disponível para referência ao entender como o comportamento de avanço funciona para etapas com mensagens no app.

As telas criadas no editor original precisam especificar um comportamento de avanço - os critérios para avançar em seu componente Canvas.  Para mensagens no app em um fluxo de trabalho do Canvas Flow, essa opção é definida para sempre avançar imediatamente o público.

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

## 



-  
-  
-  

   





- 
- 
- 
- 
- 

## Propriedades de eventos personalizados em um Canva

 

## 



- 
- 
-  
