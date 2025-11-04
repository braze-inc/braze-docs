# Banners: Perguntas frequentes

> Estas são as respostas às perguntas mais frequentes sobre Banners no Braze. Para saber mais sobre informações gerais, consulte [Sobre Banners]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}).

## Quando as atualizações do Banner são exibidas para os usuários?

Os banners são atualizados com os dados mais recentes sempre que você chama o método de atualização - não há necessidade de reenviar ou atualizar sua campanha de banner.

## Quantas colocações posso solicitar em uma sessão?

Em uma única solicitação de atualização, você pode solicitar um máximo de 10 colocações. Para cada um que você solicitar, o Braze retornará o Banner de maior prioridade para o qual o usuário é elegível. Solicitações adicionais retornarão um erro.

Para saber mais, consulte [Solicitações de posicionamento]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %}).

## Quantas campanhas de banner podem estar ativas simultaneamente?

Cada espaço de trabalho pode suportar até 200 campanhas ativas do Banner. Se esse limite for atingido, você precisará arquivar [ou desativar]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) uma campanha existente antes de criar uma nova.

## Para campanhas que compartilham um posicionamento, qual banner é exibido primeiro?

Se um usuário se qualificar para várias campanhas de banner que compartilham o mesmo posicionamento, será exibido o banner com a prioridade mais alta. Para saber mais, consulte [Prioridade do banner]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %}).

## Posso usar banners em meu feed de cartão de conteúdo existente?

Os Banners são diferentes dos Cartões de conteúdo, o que significa que você não pode usar Banners e Cartões de conteúdo no mesmo feed. Para substituir os feeds de cartão de conteúdo de banner existentes, você precisará [criar posicionamentos em seu app ou site]({{site.baseurl}}/developer_guide/banners/placements/).

## Os usuários podem descartar manualmente um Banner?

Não. Os usuários não podem descartar manualmente os banners. No entanto, é possível controlar a visibilidade do Banner gerenciando a elegibilidade do segmento de usuário. Quando um usuário não atende mais aos critérios de direcionamento de uma campanha de banner, ele não a verá novamente em sua próxima sessão.

Por exemplo, se você exibir um banner promocional até que um usuário faça uma compra, o registro de usuários de eventos como `purchase_completed` pode remover esse usuário do segmento direcionado, ocultando efetivamente o banner nas sessões subsequentes.

## Posso exportar a análise de dados da campanha de Banners usando a API do Braze?

Sim. Você pode usar o [ponto de extremidade`/campaigns/data_series` ]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) para obter dados sobre quantas campanhas do Banner foram visualizadas, clicadas ou convertidas.

## Quando os usuários são segmentados?

Os usuários são segmentados no início da sessão. Se os segmentos segmentados de uma campanha dependerem de atributos personalizados, eventos personalizados ou outros atributos de direcionamento, eles deverão estar presentes no usuário no início da sessão.

## Como posso criar Banners para garantir a menor latência?

Quanto mais simples for o envio de mensagens em seu banner, mais rápido ele será renderizado. É melhor testar sua campanha de banner em relação à latência esperada para seu caso de uso. Por exemplo, não deixe de testar as atribuições do Liquid, como `catalog_items`.

## Todas as tags Liquid são compatíveis?

Não. No entanto, a maioria das tags Liquid é compatível com mensagens de banner, exceto `catalog_items`, que é renderizado novamente usando a [tag`:rerender` ]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid).

## Posso capturar eventos de clique?

Os eventos de clique são capturados somente se uma ação ao clicar for definida em um elemento `logClick` e for chamada usando a [ponte JS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#javascript-bridge).
