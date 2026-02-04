# Banners: Perguntas frequentes

> Estas são respostas para perguntas frequentes sobre Banners no Braze. Para mais informações gerais, veja [Sobre Banners]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}).

## Quando as atualizações de Banner aparecem para os usuários?

Os Banners são atualizados com seus dados mais recentes sempre que você chama o método de atualização—não há necessidade de reenviar ou atualizar sua campanha de Banner.

## Quantas colocações posso solicitar em uma sessão?

Em uma única solicitação de atualização, você pode solicitar um máximo de 10 colocações. Para cada uma que você solicitar, o Braze retornará o Banner de maior prioridade para o qual um usuário é elegível. Solicitações adicionais retornarão um erro.

Para mais informações, veja [Solicitações de colocação]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %}).

## Quantas campanhas de Banner podem estar ativas simultaneamente?

Cada espaço de trabalho pode suportar até 200 campanhas de Banner ativas. Se esse limite for atingido, você precisará [arquivar ou desativar]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) uma campanha existente antes de criar uma nova.

## Para campanhas que compartilham uma colocação, qual Banner é exibido primeiro?

Se um usuário se qualificar para várias campanhas de Banner que compartilham a mesma colocação, o Banner com a maior prioridade será exibido. Para mais informações, veja [Prioridade do Banner]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %}).

## Posso usar Banners no meu feed de Cartão de Conteúdo existente?

Os Banners são diferentes dos Cartões de Conteúdo, o que significa que você não pode usar Banners e Cartões de Conteúdo no mesmo feed. Para substituir feeds de Cartão de Conteúdo existentes por Banners, você precisará [criar colocações em seu app ou site]({{site.baseurl}}/developer_guide/banners/placements/).

## Posso disparar um banner com base nas ações do usuário?

Embora os Banners não suportem [entrega baseada em ação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery), você pode direcionar usuários com base em suas ações passadas usando segmentação e prioridade.

Por exemplo, para mostrar um Banner especial apenas para usuários que completaram um `purchase` evento:
1. **Direcionamento:** Em sua campanha, direcione um segmento de usuários que tenham realizado o evento personalizado `purchase` pelo menos uma vez.
2. **Prioridade:** Se você tiver um Banner geral para todos os usuários e este Banner específico para compradores direcionando o mesmo local, defina a prioridade do Banner específico para **Alta** e o Banner geral para **Média** ou **Baixa**.

Quando o usuário inicia uma nova sessão ou atualiza os Banners após realizar a ação, a Braze avalia sua elegibilidade. Se eles corresponderem ao segmento "Compra", o Banner de alta prioridade será exibido.


## Os usuários podem dispensar manualmente um Banner?

Não. Os usuários não podem dispensar manualmente os Banners. No entanto, você pode controlar a visibilidade do Banner gerenciando a elegibilidade do segmento de usuários. Quando um usuário não atende mais aos critérios de direcionamento para uma campanha de Banner, ele não o verá novamente em sua próxima sessão.

Por exemplo, se você exibir um Banner promocional até que um usuário faça uma compra, registrar um evento como `purchase_completed` pode remover esse usuário do segmento direcionado, efetivamente ocultando o Banner em sessões subsequentes.

## Posso exportar análises de campanhas de Banners usando a API da Braze?

Sim. Você pode usar o [`/campaigns/data_series` endpoint]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) para obter dados sobre quantas campanhas de Banner foram visualizadas, clicadas ou convertidas.

## Quando os usuários são segmentados?

Os usuários são segmentados no início da sessão. Se os segmentos direcionados de uma campanha dependem de atributos personalizados, eventos personalizados ou outros atributos de direcionamento, eles devem estar presentes no usuário no início da sessão.

## Como posso compor Banners para garantir a menor latência?

Quanto mais simples a mensagem em seu Banner, mais rápido ele será renderizado. É melhor testar sua campanha de Banner em relação à latência esperada para seu caso de uso. Por exemplo, certifique-se de testar atributos Liquid como `catalog_items`.

## Todos os tags Liquid são suportados?

Não. No entanto, a maioria dos tags Liquid é suportada para mensagens de Banner, exceto por `catalog_items` que são re-renderizados usando a tag [`:rerender` tag]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid).

## Posso capturar eventos de clique?

Eventos de clique são capturados apenas se uma ação de clique for definida em um elemento `logClick` e for chamada usando o [JS bridge]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#javascript-bridge).
