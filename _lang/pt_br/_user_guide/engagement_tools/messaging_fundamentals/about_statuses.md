---
nav_title: Status
article_title: Status da campanha e do Canvas
page_order: 1
description: "Saiba mais sobre os status de campanhas e Canvases e como usá-los no painel."
tool:
    - Campaigns
    - Canvas
---

# Status da campanha e do Canvas

> Saiba mais sobre status para campanhas e Canvases e como você pode usá-los no painel.

## Filtragem por status

Para filtrar suas campanhas ou Canvases por status, selecione **All Statuses (Todos os status**) e, em seguida, escolha um status.

O menu suspenso "Todos os status" no painel do Braze.]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## Alteração do status

Para alterar o status de uma campanha ou Canvas, selecione o menu <i class="fas fa-ellipsis-vertical"></i> e, em seguida, escolha um status.

Uma lista de Canvases no painel do Braze, com o menu aberto para um dos Canvases.]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## Status disponíveis

Esses são os status disponíveis para campanhas e Canvases:

| Status | Descrição |
| --- | --- |
| Ativo | Campanhas ativas e Canvases estão em processo de envio. Por padrão, você verá campanhas ativas e Canvases nas respectivas páginas. |
| Rascunho | Os rascunhos de campanhas e Canvases são salvos, mas não são lançados. Para continuar editando e começar a enviar, você pode selecionar o rascunho acessando **Messaging (Mensagens)** no painel do Braze e selecionando **Canvas** ou **Campaigns**. |
| Arquivado | Campanhas arquivadas e Canvases são mensagens que não estão mais sendo enviadas. Essas campanhas e Canvases também são removidas dos gráficos de estatísticas na seção [**Início**]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard) e [**Receita**]({{site.baseurl}}/user_guide/analytics/reporting/revenue_report) páginas.|
| Parado | Campanhas e Canvases interrompidas são pausadas, mas você ainda pode editá-las. Para retomar, selecione o menu <i class="fas fa-ellipsis-vertical"></i> e, em seguida, **Resume (Retomar**). Para obter mais informações, consulte [Comportamento do Canvas interrompido](#stopped-canvas-behavior). |
| Inativo | Quando uma campanha ou Canvas não estiver mais enviando mensagens, o Braze atribuirá a ela um status ocioso para ajudar a classificar e gerenciar sua lista de campanhas e Canvases. Você pode visualizar quais campanhas ou Canvases serão automaticamente interrompidas e a data de interrupção associada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comportamento do Canvas interrompido {#stopped-canvas-behavior}

Quando um Canvas é interrompido, ocorre o seguinte:

- **Mensagens programadas:** Suas mensagens agendadas não serão enviadas, independentemente da posição de um usuário no Canvas. Isso também inclui usuários que estavam na fila devido à limitação de taxa.
- **Envios de e-mail:** Os envios de e-mail podem não ser interrompidos imediatamente, pois o provedor de serviços de e-mail (ESP) pode continuar processando as solicitações existentes.
- **Etapas de atraso:** Os usuários em uma [etapa de atraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) permanecerão lá normalmente, mas sairão do Canvas quando o período definido terminar.

Para retomar o Canvas, selecione o menu <i class="fas fa-ellipsis-vertical"></i> e, em seguida, **Resume (Retomar**). Quando reativadas, todas as mensagens interrompidas anteriormente serão enviadas conforme programado, desde que o horário programado ainda não tenha passado.

## Práticas recomendadas

### Monitore suas mensagens por status

Você pode monitorar suas mensagens por status para analisar os detalhes de desempenho. Por exemplo, se você tiver uma série de campanhas ativas, poderá avaliar o desempenho de cada campanha com suas métricas de engajamento e fazer ajustes conforme necessário. Se, em vez disso, você tiver alguns Canvases parados, poderá considerar se eles devem ser retomados para envio de mensagens ou totalmente arquivados.

{% alert tip %}
Procurando outras maneiras de se manter organizado? Adicione [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags) para fornecer mais contexto em um relance.
{% endalert %}

### Auditar suas mensagens ativas

Ao realizar auditorias de suas campanhas e Canvases ativos, você pode avaliar a relevância e o desempenho e remover ou atualizar quaisquer campanhas e Canvases desatualizados para manter suas mensagens atualizadas.
