---
nav_title: Statuses
article_title: Status da campanha e do Canva
page_order: 1
description: "Saiba mais sobre status para campanhas e Canvas e como usá-los no dashboard."
tool:
    - Campaigns
    - Canvas
---

# Status da campanha e do Canva

> Saiba mais sobre status para campanhas e Canvas e como usá-los no dashboard.

## Filtragem por status

Para filtrar suas campanhas ou Canvas por status, selecione **All Statuses (Todos os status**) e, em seguida, escolha um status.

![O menu suspenso "All Statuses" (Todos os status) no dashboard do Braze.]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## Alteração do status

Para alterar o status de uma campanha ou Canva, selecione o menu <i class="fas fa-ellipsis-vertical"></i> e, em seguida, escolha um status.

![Uma lista de telas no dashboard do Braze, com o menu aberto para uma das telas.]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## Status disponíveis

Esses são os status disponíveis para campanhas e telas:

| Status | Descrição |
| --- | --- |
| Ativo | Campanhas ativas e Canvas estão em processo de envio. Por padrão, você verá campanhas ativas e Canvas nas respectivas páginas. |
| Rascunho | Os rascunhos de campanhas e telas são salvos, mas não são lançados. Para continuar editando e começar a enviar, você pode selecionar o rascunho acessando **Envio de mensagens** no dashboard do Braze e selecionando **Canvas** ou **Campaigns**. |
| Arquivado | Campanhas e Canvas arquivadas são mensagens que não estão mais sendo enviadas. Essas campanhas e telas também são removidas dos gráficos de estatísticas na seção [**Início**]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard) e [**Receita**]({{site.baseurl}}/user_guide/analytics/reporting/revenue_report) páginas.|
| Interrompido | Campanhas e telas interrompidas são pausadas, mas você ainda pode editá-las. Para retomar, selecione o menu <i class="fas fa-ellipsis-vertical"></i> e, em seguida, **Resume (Retomar**). Para saber mais, consulte [Comportamento do Canva interrompido](#stopped-canvas-behavior). |
| Sem atividade | Quando uma campanha ou Canvas não estiver mais enviando mensagens, o Braze atribuirá a ela um status sem atividades para ajudar a classificar e gerenciar sua lista de campanhas e Canvas. Você pode ver quais campanhas ou Canvas serão automaticamente interrompidas e a data de interrupção associada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comportamento do Canva interrompido {#stopped-canvas-behavior}

Quando um Canva é interrompido, ocorre o seguinte:

- **Envio de mensagens programadas:** Suas mensagens programadas não serão enviadas, independentemente da posição do usuário no Canva. Isso também inclui usuários que estavam na fila por causa do limite de frequência.
- **Envio de e-mail:** Os envios de e-mail podem não ser interrompidos imediatamente, pois o provedor de serviço de e-mail (ESP) pode continuar processando as solicitações existentes.
- **Etapas de postergação:** Os usuários em uma [etapa do]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) canva permanecerão lá normalmente, mas sairão do Canvas quando o período definido terminar.

Para retomar o Canva, selecione o menu <i class="fas fa-ellipsis-vertical"></i> e, em seguida, **Resume (Retomar**). Quando reativado, todas as mensagens interrompidas anteriormente serão enviadas conforme programado, desde que o horário programado ainda não tenha passado.

## Melhores práticas

### Monitore seus envios de mensagens por status

Você pode monitorar suas mensagens por status para analisar os detalhes de performance. Por exemplo, se você tiver uma série de campanhas ativas, poderá avaliar a performance de cada campanha com suas métricas de engajamento e fazer ajustes conforme necessário. Se, em vez disso, você tiver algumas telas paradas, poderá considerar se elas devem ser retomadas para envio de mensagens ou arquivadas completamente.

{% alert tip %}
Procurando outras maneiras de se manter organizado? Adicione [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags) para fornecer mais contexto em um relance.
{% endalert %}

### Auditoria de suas mensagens ativas

Ao realizar auditorias de suas campanhas e Canvas ativos, você pode avaliar a relevância e a performance e remover ou atualizar quaisquer campanhas e Canvas desatualizados para manter seu envio de mensagens atualizado.
