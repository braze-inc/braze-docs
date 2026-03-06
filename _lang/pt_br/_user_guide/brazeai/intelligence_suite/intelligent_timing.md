---
nav_title: Intelligent Timing
article_title: Intelligent Timing
page_order: 1.3
description: "Este artigo oferece uma visão geral do Intelligent Timing (anteriormente Intelligent Delivery) e como você pode usar esse recurso em suas campanhas e Canvas."
---

# [![Curso Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligent Timing

> Use o Intelligent Timing para enviar sua mensagem a cada usuário no momento ideal de entrega determinado pela Braze, ou seja, quando o usuário tem maior probabilidade de interagir (abrir ou clicar). Assim você pode verificar mais facilmente que está enviando mensagens no momento preferido dos usuários, o que pode aumentar o engajamento.

## Sobre o Intelligent Timing

A Braze calcula o momento ideal de entrega com base em uma análise estatística das interações passadas dos usuários com seu app e com cada canal de mensagem. São usados dados de interação como:

- Horários de sessão
- Aberturas diretas de push
- Aberturas influenciadas de push
- Cliques em e-mail
- Aberturas de e-mail (excluindo [aberturas de máquina]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens))
- Cliques em SMS (somente com [encurtamento de links SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) e rastreamento avançado ativados)

Se um usuário não tiver dados de interação relevantes para calcular o momento ideal, você pode especificar um horário de fallback.

## Casos de uso

- Enviar campanhas recorrentes que não são sensíveis ao tempo
- Automatizar campanhas com usuários em vários fusos horários
- Ao enviar mensagens para seus usuários mais engajados (eles terão a maioria dos dados de interação)

Para etapas detalhadas de configuração em campanhas e Canvas, horários silenciosos, horário de fallback, limitações e FAQ, consulte a versão completa deste artigo no índice à esquerda ou na ajuda do dashboard da Braze.
