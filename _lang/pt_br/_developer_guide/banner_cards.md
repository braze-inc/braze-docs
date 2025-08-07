---
page_order: 2.2
nav_title: Cartões de Banner
article_title: Cartões de Banner
description: "Esta landing page contém todos os assuntos relacionados a cartões de banner, incluindo artigos sobre como criar cartões de banner e casos de uso."
channel:
- Banners
---

# Cartões de Banner

> Com os Cartões Banner, você pode criar mensagens personalizadas para seus usuários enquanto amplia o alcance de seus outros canais, como e-mail ou notificações por push. Semelhante aos [Cartões de Conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about), você pode incorporar cartões diretamente em seu app ou site, o que permite que você interaja com os usuários através de uma experiência que parece natural.

{% alert important %}
Os cartões de banner estão atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar desse acesso antecipado.
{% endalert %}

## Casos de uso

Como os Cartões Banner nunca expiram e são auto-personalizados toda vez que um usuário inicia uma nova sessão, eles são ótimos para:

- Destacar conteúdo em destaque
- Notificar usuários sobre eventos futuros
- Compartilhar atualizações sobre programas de fidelidade

## Sobre os Cartões Banner

### Expiração do cartão

Por padrão, os Cartões Banner não expiram—no entanto, você pode escolher uma data de término, se necessário.

### IDs de colocação {#placement-ids}

As colocações de Cartões Banner são exclusivas para cada espaço de trabalho e podem ser usadas em 10 campanhas dentro de um único espaço de trabalho. Além disso, as colocações dentro de cada espaço de trabalho devem ter um ID exclusivo atribuído. Você criará colocações e atribuirá IDs quando você [criar uma campanha de Cartão Banner]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns/) ou [incorporar Cartões Banner em seu app]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards/).

{% alert important %}
Evite modificar os IDs de colocação após lançar uma campanha de Cartão Banner.
{% endalert %}

### Prioridade do cartão {#card-priority}

Quando várias campanhas referenciam o mesmo ID de colocação, os cartões são exibidos em ordem de nível de prioridade. Por padrão, os Cartões Banner recém-criados são definidos como médio, mas você pode [definir manualmente a prioridade]({{site.baseurl}}/developer_guide/banner_cards/creating_banner_cards/#set-card-priority) como alta, média ou baixa. Se vários cartões compartilharem o mesmo nível de prioridade, o cartão mais novo será exibido primeiro.

### Métricas

Estas são as métricas mais importantes dos Cartões Banner. Para uma lista completa de métricas, definições e cálculos, consulte o [Glossário de Métricas de Relatório]({{site.baseurl}}/user_guide/data/report_metrics/).

| Métrico | Definição |
| --- | --- |
| [Total de impressões]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#total-impressions) | O número de vezes que a mensagem foi carregada e aparece na tela de um usuário, independentemente da interação anterior (por exemplo, se um usuário vê uma mensagem duas vezes, ele será contado duas vezes). |
| [Impressões únicas]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#unique-impressions) | O número total de usuários que receberam e visualizaram uma determinada mensagem em um dia. Cada usuário é contado apenas uma vez. |
| [Total de cliques]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#total-clicks) | O número total (e a porcentagem) de usuários que clicaram na mensagem entregue, independentemente de o mesmo usuário clicar várias vezes. |
| [Cliques únicos projetados]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#unique-clicks) | O número distinto de destinatários que clicaram em uma mensagem pelo menos uma vez e é medido por [`dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/). Cada usuário é contado apenas uma vez. |
| [Conversões primárias]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#primary-conversions-a-or-primary-conversion-event) | O número de vezes que um evento definido ocorreu após a interação ou a visualização de uma mensagem recebida de uma campanha do Braze. Esse evento definido é determinado por você ao criar a campanha. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Próximos passos

Agora que você sabe sobre os Cartões de Banner, está pronto para os próximos passos:

- [Criando campanhas de Cartão de Banner]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns/)
- [Incorporando Cartões de Banner no seu app]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards/)
