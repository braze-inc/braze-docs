---
nav_title: Práticas recomendadas
article_title: Práticas recomendadas do Canvas
page_order: 1
description: "Este artigo fornece algumas práticas recomendadas para criar e personalizar jornadas de usuário com o Canvas e o Canvas Flow."
tool: Canvas

---

# Práticas recomendadas do Canvas

> Este artigo fornece algumas práticas recomendadas para criar e personalizar jornadas de usuário com o Canvas e o Canvas Flow.

## Identifique seu objetivo

Mergulhe no que, quem e por quê!
- O que você está tentando ajudar os usuários a realizar?
- Quem são os usuários que você está tentando alcançar?
- Por que você está criando esse Canvas?

## Misturar e combinar

Desbloqueie novas combinações de jornadas de usuário com os [componentes do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/).
- Divida seus usuários com o [Decision Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/) e crie fluxos de trabalho diferentes.
- Espace suas jornadas de usuário com uma etapa [de Atraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/).
- Adicione [mensagens autônomas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) em qualquer lugar que desejar no fluxo do Canvas. 

## Criar mensagens mais ricas

Atraia seus usuários com mensagens mais ricas.

- Crie [mensagens in-app]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) para Canvases de integração para aproveitar ao máximo sua primeira impressão.
- Introduza [os Content Cards]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/content-cards_in_canvas/) em uma jornada do Canvas para ofertas promocionais e notificações por push.

## Teste suas jornadas de usuário

Determine o impacto de suas mensagens do Canvas incorporando grupos de controle. Dessa forma, você pode entender como seu Canvas foi recebido!

- Nomeie cada etapa do seu Canvas para identificar a jornada do usuário.
- Aproveite o componente [Experiment Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) na jornada do usuário para atribuir aleatoriamente os usuários a diferentes caminhos criados por você. 
- Diversifique suas jornadas de usuário com etapas de Atraso e Mensagem para ajudar a descobrir qual caminho é mais eficaz.
- Verifique o [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para ver o desempenho de cada componente na jornada do usuário.
- [Edite seu Canvas]({{site.baseurl}}/post-launch_edits/) após o lançamento inicial.

## Agendamento de suas telas

{% alert note %}
O Canvas impedirá que você use o envio programado com um horário que já tenha passado. No entanto, é possível lançar um Canvas exatamente no mesmo minuto em que a campanha está programada (ou nos segundos anteriores). Isso pode fazer com que o Canvas perca o horário de entrada programado e os usuários não entrem no Canvas. Recomendamos o envio imediato de Canvases caso alguma campanha seja editada minutos após o horário de envio programado.
{% endalert %}

Para as etapas do Canvas, considere os seguintes detalhes ao programar seu Canvas:

- As alterações no cronograma serão aplicadas apenas aos usuários que ainda não estão esperando para receber a etapa.
- Por padrão, as alterações no Audience se aplicam a todos os usuários, a menos que você programe as alterações para serem aplicadas aos usuários que não estão esperando para receber a etapa.
- Editar um Canvas que está programado para ser entregue assim que for implantado e selecionar **Atualizar** fará com que ele seja enviado.
