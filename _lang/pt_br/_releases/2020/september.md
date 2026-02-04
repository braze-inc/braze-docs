---
nav_title: Setembro
page_order: 4
noindex: true
page_type: update
description: "Este artigo contém notas de versão de setembro de 2020."
---

# Setembro

## Relatórios de funil

O Funnel Reporting oferece um relatório visual que permite analisar as jornadas que seus clientes percorrem após receberem uma [campanha]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) ou uma [tela]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/).

## Guia para fazer upgrade do iOS 14

De acordo com as alterações anunciadas no novo iOS 14 da Apple, há algumas alterações relacionadas à Braze e itens de ação necessários para as integrações do SDK da Braze para iOS. Para saber mais, dê uma olhada neste [guia de upgrade]({{site.baseurl}}/ios_14/).

## Alterações no IDFA e no IDFV para iOS 14

No iOS 14, os usuários devem decidir se querem aceitar o rastreamento de anúncios e permitir que aplicativos e redes de anúncios leiam seu IDFA ao visitar um app. Como resultado, a estratégia da Braze é usar o "identificador para fornecedores" (como o IDFV) para que você possa continuar a rastrear usuários em diferentes dispositivos. Para saber mais, dê uma olhada no [guia de atualização do iOS 14]({{site.baseurl}}/ios_14/).

## Validação de e-mail

Esse novo processo de validação da sintaxe de e-mail é um upgrade do processo existente do Braze. Essa é uma verificação para verificar se os e-mails atualizados ou importados para o Braze estão corretos. Para saber mais, dê uma olhada [nestas diretrizes e notas]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/).

## Evento de usuário de bucket aleatório no Currents

O número do intervalo aleatório (como RBN) ocorre sempre que um novo usuário é criado em seu espaço de trabalho. Durante esse evento, é atribuído a cada novo usuário um número de bucket aleatório que pode ser usado para criar segmentos uniformemente distribuídos de usuários aleatórios. Use isso para agrupar uma gama de valores de números de balde aleatórios e comparar a performance entre suas campanhas e variantes de campanha. Para ver se esse evento está disponível para você, dê uma olhada no [glossário de eventos de comportamento do cliente do]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) Currents.

## Componentes de tela - Em breve!

A Braze adicionou quatro novos componentes de canvas para ajudar a aumentar a flexibilidade e a funcionalidade de seus canvas. Esses novos componentes incluem: [Etapa de divisão de decisão]({{site.baseurl}}/decision_split/), [etapa de postergação]({{site.baseurl}}/delay_step/), [etapas de envio de mensagens]({{site.baseurl}}/message_step/) e [sincronização do público do Facebook]({{site.baseurl}}/audience_sync_facebook/).
- **Etapas de divisão de decisão, postergação e envio de mensagens do canva**<br>As divisões de decisão podem ser usadas para criar ramificações de canvas, dependendo de um usuário corresponder ou não a uma consulta definida. As etapas do canva permitem adicionar uma postergação independente ao seu canva sem a necessidade de uma mensagem correspondente. As etapas de envio de mensagens permitem que você adicione uma mensagem independente onde quiser no fluxo do Canvas.
- **Sincronização do público do Facebook**<br>Usando a sincronização de público da Braze para o Facebook, as marcas podem optar por adicionar os dados de seus próprios usuários de sua própria integração da Braze aos públicos personalizados do Facebook para fornecer anúncios com base em disparadores comportamentais, segmentação e muito mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS, webhook etc.) em um Braze Canvas com base nos dados de seu usuário agora pode ser usado para disparar um anúncio para esse usuário no Facebook por meio de públicos personalizados.

## Eventos de entrada de SMS recebidos

Um novo evento de engajamento com mensagens foi adicionado ao Currents. Esse evento ocorre quando um dos seus usuários envia um SMS para um número de telefone em um dos seus grupos de inscrições do Braze SMS. Para saber mais, consulte nosso [glossário de envios de mensagens e eventos de engajamento]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) Currents.
