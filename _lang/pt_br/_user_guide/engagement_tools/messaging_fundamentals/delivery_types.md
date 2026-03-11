---
nav_title: Tipos de entrega e entrada
article_title: Tipos de Entrega e Entrada
page_order: 5
page_type: reference
description: "Este artigo de referência descreve os tipos de entrega para campanhas, tipos de entrada para Canvases e os recursos baseados em tempo ao configurar uma campanha ou Canvas."
tool:
    - Campaigns
    - Canvas
---

# Tipos de entrega e entrada

> No Braze, existem três maneiras diferentes de agendar sua mensagem: agendada, baseada em ação e acionada por API. Escolher como e quando sua mensagem será entregue é crucial para desenvolver uma mensagem eficaz. 

Para campanhas, o tipo de entrega determina quando seus usuários entrarão na sua campanha e quando ela será enviada. Como um Canvas é construído como uma jornada contínua do usuário, o conceito de envio de mensagens de agendamento é referido como um tipo de entrada.

| Entrega<nobr> e tipos de entrada | Descrição                                                                                                                                                                                                                                                                                                                                      |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Agendado**       | Esse tipo de agendamento é projetado para mensagens únicas que você deseja enviar imediatamente, como campanhas sobre um evento atual. <br><br>Ao enviar mensagens de teste destinadas apenas a você ou sua equipe, essa opção permite que você as entregue imediatamente.                                                                                   |
| **Baseado em ação**    | Mensagens de entrega baseadas em ação, ou campanhas e Canvases acionados por eventos, são muito eficazes para mensagens transacionais ou baseadas em conquistas. Você pode acioná-las para enviar após um usuário completar um determinado evento, em vez de enviar sua mensagem em determinados dias.                                                                                           |
| **Disparadas pela API**   | Mensagens acionadas por API permitem que você gerencie o texto da mensagem, testes multivariantes e regras de re-eligibilidade no dashboard do Braze, enquanto aciona a entrega desse conteúdo a partir de seus próprios servidores e sistemas. <br><br>A solicitação da API para disparar a mensagem também pode incluir dados adicionais a serem modelados na mensagem em tempo real. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Opções baseadas em tempo

{% tabs %}
{% tab campaign %}
Você pode escolher entre as seguintes opções ao usar entrega agendada:

- Envie assim que a campanha for lançada
- Enviar em um horário determinado
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)
{% endtab %}

{% tab canvas %}
Com a entrega programada, os usuários entrarão em uma programação de tempo, da mesma forma que você programaria uma campanha. Você pode inscrever usuários em um Canvas assim que ele for lançado ou em um horário designado.

### Horários designados

Você pode escolher enviar seu Canvas em uma frequência de entrada específica, incluindo apenas uma vez, diariamente, semanalmente ou mensalmente. Para Canvases com entrega agendada recorrente, você pode definir a recorrência para permitir que os usuários entrem no Canvas até 30 vezes designadas.
{% endtab %}
{% endtabs %}

## Opções baseadas em ação

{% tabs %}
{% tab campaign %}
A entrega baseada em ação enviará campanhas para usuários que realizam uma ação específica. Após essa ação ocorrer, você pode decidir quando enviar a campanha: imediatamente, após um tempo específico, em um horário específico ou em um momento no futuro.
{% endtab %}

{% tab canvas %}
As opções baseadas em ação determinam quais ações (ou disparadores) um usuário precisa realizar para entrar em um canva e a que momento específico eles podem começar a entrar. Por exemplo, você poderia avaliar seus usuários pelas seguintes ações:

- Abrindo seu app
- Adição de um endereço de e-mail
- Inserção de um local

### Janela de entrada

A janela de entrada do seu canva determina quais usuários podem entrar no canva no horário de início designado (e horário de término opcional). Semelhante às campanhas baseadas em ação, você pode escolher inserir usuários em seu fuso horário local.
{% endtab %}
{% endtabs %}

## Opções de disparo de API

{% tabs %}
{% tab campaign %}
Quando você seleciona disparo de API como sua opção de entrega, você receberá um ID de campanha para identificar qual campanha enviar com o [`/campaigns/trigger/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#prerequisites).
{% endtab %}

{% tab canvas %}
Quando você seleciona disparo de API como seu tipo de entrada, você receberá um ID de canva para identificar qual campanha enviar com o [`/canvas/trigger/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).
{% endtab %}
{% endtabs %}
