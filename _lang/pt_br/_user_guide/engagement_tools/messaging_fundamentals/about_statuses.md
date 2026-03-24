---
nav_title: Statuses
article_title: Status de Campanhas e Canvases
page_order: 11
description: "Saiba mais sobre os status de campanhas e Canvases e como usá-los no dashboard."
tool:
    - Campaigns
    - Canvas
---

# Status de Campanhas e Canvases

> Saiba mais sobre os status de campanhas e Canvases e como você pode usá-los no dashboard.

## Filtrando por status

Para filtrar suas campanhas ou Canvases por status, selecione **Todos os Status**, e depois escolha um status.

![O dropdown 'Todos os Status' no dashboard do Braze.]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## Mudando o status

Para mudar o status de uma campanha ou Canvas, selecione o menu <i class="fas fa-ellipsis-vertical"></i>, e depois escolha um status.

![Uma lista de Canvases no dashboard do Braze, com o menu aberto para um dos Canvases.]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## Status disponíveis

Estes são os status disponíveis para campanhas e Canvases:

| Status | Descrição |
| --- | --- |
| Ativo | Campanhas e Canvases ativos estão em processo de envio. Por padrão, você verá campanhas e Canvases ativos nas respectivas páginas. |
| Rascunho | Rascunhos de campanhas e Canvases estão salvos, mas não lançados. Para continuar editando e começar a enviar, você pode selecionar o rascunho acessando **Envio de Mensagens** no dashboard do Braze e selecionando **Canvas** ou **Campanhas**. |
| Arquivado | Campanhas e Canvases arquivados são mensagens que não estão mais sendo enviadas. Essas campanhas e Canvases também são removidos dos gráficos estatísticos nas páginas [**Início**]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard) e [**Receita**]({{site.baseurl}}/user_guide/analytics/reporting/revenue_report).|
| Interrompido | Campanhas e Canvases parados estão pausados, mas você ainda pode editá-los. Para retomar um Canvas, vá para a etapa **Resumo** do construtor de Canvas e selecione **Retomar Canvas**. Para campanhas, selecione o menu <i class="fas fa-ellipsis-vertical"></i>, e depois **Retomar**. Para mais informações, consulte [Comportamento do Canvas parado](#stopped-canvas-behavior). |
| Sem atividade | Quando uma campanha ou Canvas não estiver mais enviando mensagens, a Braze atribuirá a ele um status de inatividade para ajudar a organizar e gerenciar sua lista de campanhas e Canvases. Você pode visualizar quais campanhas ou Canvases serão automaticamente interrompidos e a data de parada associada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comportamento do Canvas parado {#stopped-canvas-behavior}

Quando um Canvas é parado, o seguinte ocorre:

- **Mensagens agendadas:** Suas mensagens agendadas não serão enviadas, independentemente da posição de um usuário no Canvas. Isso também inclui usuários que estavam na fila devido a limitação de taxa.
- **Envios de e-mail:** Os envios de e-mail podem não parar imediatamente, pois seu prestador de serviço de e-mail (ESP) pode continuar processando suas solicitações existentes.
- **Etapas de postergação:** Usuários em uma [etapa de postergação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) permanecerão lá normalmente, mas sairão do Canvas quando o período definido terminar.
- **Alterações de rascunho:** Quaisquer alterações de rascunho no Canvas serão descartadas quando o Canvas for parado.

Para retomar o Canvas, acesse a **Resumo** etapa do construtor de Canvas e selecione **Retomar Canvas**. Quando reativados, quaisquer mensagens que foram paradas anteriormente serão enviadas conforme agendado—desde que o horário agendado ainda não tenha passado.

## Melhores práticas

### Monitore suas mensagens por status

Você pode monitorar suas mensagens por status para revisar os detalhes de desempenho. Por exemplo, se você tiver uma série de campanhas ativas, pode avaliar o desempenho de cada campanha com suas métricas de engajamento e fazer ajustes conforme necessário. Se, em vez disso, você tiver alguns Canvases parados, pode considerar se eles devem ser retomados para envio de mensagens ou arquivados completamente.

{% alert tip %}
Procurando mais maneiras de se manter organizado? Adicione [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags) para fornecer mais contexto de relance.
{% endalert %}

### Audite suas mensagens ativas

Ao realizar auditorias de suas campanhas ativas e Canvases, você pode avaliar a relevância e a performance, e remover ou atualizar quaisquer campanhas e Canvases desatualizados para manter seu envio de mensagens atualizado.
