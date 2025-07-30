---
nav_title: Tipos de entrega e entrada
article_title: Tipos de entrega e entrada
page_order: 5
page_type: reference
description: "Este artigo de referência descreve os tipos de entrega para campanhas, os tipos de entrada para Canvas e os recursos baseados em tempo ao configurar uma campanha ou um Canvas."
tool:
    - Campaigns
    - Canvas
---

# Agendamento de suas mensagens

> No Braze, há três maneiras diferentes de programar sua mensagem: programada, baseada em ação e disparada por API. A escolha de como e quando sua mensagem será transmitida é crucial para o desenvolvimento de uma mensagem eficaz. 

## Tipos de entrega e entrada

Para campanhas, o tipo de entrega determina quando os usuários entrarão na campanha e quando ela será enviada. Como um Canva é criado como uma jornada contínua do usuário, o conceito de envio de mensagens de um agendamento é chamado de tipo de entrada.

| Entrega<nobr> e tipos de entrada | Descrição                                                                                                                                                                                                                                                                                                                                      |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Agendado**       | Esse tipo de programação foi criado para mensagens únicas que você deseja enviar imediatamente, como campanhas sobre um evento atual. <br><br>Ao enviar mensagens de teste destinadas apenas a você ou à sua equipe, essa opção permite que você as entregue imediatamente.                                                                                   |
| **Baseado em ação**    | As mensagens de entrega baseadas em ação, ou campanhas e Canvas disparadas por eventos, são muito eficazes para mensagens transacionais ou baseadas em conquistas. É possível disparar o envio depois que um usuário concluir um determinado evento, em vez de enviar a mensagem em determinados dias.                                                                                           |
| **Disparadas pela API**   | As mensagens acionadas por API permitem gerenciar o texto da mensagem, os testes multivariantes e as regras de reelegibilidade no dashboard do Braze e, ao mesmo tempo, disparar a entrega desse conteúdo a partir de seus próprios servidores e sistemas. <br><br>A solicitação da API para disparar a mensagem também pode incluir dados adicionais a serem modelados na mensagem em tempo real. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Opções baseadas em tempo

{% tabs %}
{% tab campanha %}
Você pode escolher entre as seguintes opções ao usar a entrega programada:

- Envie assim que a campanha for lançada
- Enviar em um horário determinado
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)
{% endtab %}

{% tab canvas %}
Com a entrega programada, os usuários entrarão em uma programação de tempo, da mesma forma que você programaria uma campanha. É possível inscrever usuários em um Canva assim que ele for lançado ou em um horário determinado.

#### Horários designados

Você pode optar por enviar seu Canva em uma frequência de entrada específica, incluindo apenas uma vez, diariamente, semanalmente ou mensalmente. Para Canvas com uma entrega programada recorrente, é possível definir a recorrência para permitir que os usuários entrem no Canvas até 30 vezes designadas.
{% endtab %}
{% endtabs %}

### Opções baseadas em ações

{% tabs %}
{% tab campanha %}
A entrega baseada em ação enviará campanhas aos usuários que realizarem uma ação específica. Depois que essa ação ocorrer, você poderá decidir quando enviar a campanha: imediatamente, após um horário específico, em um horário específico ou em um horário futuro.
{% endtab %}

{% tab canvas %}
As opções baseadas em ações determinam quais ações (ou disparos) um usuário precisa realizar para entrar em um Canva e em que momento específico ele pode começar a entrar. Por exemplo, você pode avaliar seus usuários pelas seguintes ações:

- Abrindo seu aplicativo
- Adição de um endereço de e-mail
- Inserção de um local

#### Janela de entrada

A janela de entrada do seu Canvas determina quais usuários podem entrar no Canvas na hora de início designada (e na hora de ponta opcional). Semelhante às campanhas baseadas em ações, é possível optar por inserir os usuários em seu fuso local.
{% endtab %}
{% endtabs %}

### Opções de disparo da API

{% tabs %}
{% tab campanha %}
Ao selecionar API-triggered como opção de entrega, você receberá um ID de campanha para identificar qual campanha enviar com o [endpoint`/campaigns/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#prerequisites).
{% endtab %}

{% tab canvas %}
Ao selecionar API-triggered como seu tipo de entrada, você receberá um Canva ID para identificar qual campanha enviar com o [endpoint`/canvas/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).
{% endtab %}
{% endtabs %}
