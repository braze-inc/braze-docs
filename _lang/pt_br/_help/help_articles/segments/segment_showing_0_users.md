---
nav_title: Usuários ausentes no segmento
article_title: Usuários ausentes no segmento
page_order: 1

page_type: solution
description: "Este artigo de ajuda o orienta nas etapas de solução de problemas se nenhum usuário estiver aparecendo no seu segmento, mas você prevê mais."
tool: Segments
---

# Usuários ausentes no segmento

Há duas soluções possíveis quando você está vendo `0` usuários, mas previa mais:
* [Calcular estatísticas exatas](#calculate-exact-statistics)
* [Verificar a transferência de dados](#verify-data-transfer)

## Calcular estatísticas exatas

As estatísticas do segmento podem estar fornecendo uma estimativa. A estimativa é calculada com base em uma amostra aleatória com um intervalo de confiança de 95% de que o resultado está dentro de `+/- 1%`. Quanto menor for a sua base de usuários, mais provável será que o tamanho do seu segmento seja uma estimativa aproximada. Clique em **Calculate Exact Statistics (Calcular estatísticas exatas** ) no painel **Segment Details (Detalhes do segmento** ). Isso calculará o número exato de usuários em seu segmento.

![Painel Segment Details (Detalhes do segmento) que mostra a opção Calculate Exact Statistics (Calcular estatísticas exatas)]({% image_buster /assets/img_archive/trouble8.png %})

## Verificar a transferência de dados

É possível que os dados que você está filtrando não estejam sendo enviados para o Braze. Para verificar quais eventos personalizados estão sendo enviados ao Braze, consulte o [Relatório de eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-analytics).

Selecione o evento personalizado junto com as datas e o app específicos para ver quais dados estão sendo realmente transferidos para o Braze. Se você perceber que `0` dados estão sendo enviados ao Braze, a próxima etapa é avaliar como você está enviando os eventos ao Braze.

![Gráfico que mostra a contagem de eventos personalizados como zero]({% image_buster /assets/img_archive/trouble9.png %})

{% alert important %}
Os dados que você vê no dashboard do Braze podem não ter a mesma sintaxe dos dados que você está enviando ao Braze. Certifique-se de que esses dois itens sejam exatamente iguais.
{% endalert %}

Ainda precisa de ajuda? Abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

_Última atualização em 5 de janeiro de 2021_

