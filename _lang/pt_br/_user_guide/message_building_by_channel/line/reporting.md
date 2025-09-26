---
nav_title: Relatórios
article_title: Relatórios LINE
page_order: 4
description: "Este artigo de referência aborda as métricas LINE usadas no Braze, bem como a forma de visualizá-las em suas campanhas LINE."
page_type: reference
channel:
 - LINE
alias: /line/reporting/
---

# Relatórios LINE

> Depois de lançar sua campanha ou o Canvas, você pode visualizar as principais métricas na página de detalhes da campanha ou na análise de dados do Canvas. Este artigo aborda onde você pode encontrar essas métricas e o que elas representam.

{% alert tip %}
Está procurando definições para os termos e métricas em seu relatório? Consulte o [glossário de métricas do relatório]({{site.baseurl}}/user_guide/data/report_metrics/).
{% endalert %}

## Análise de dados da campanha

Na guia **Análise de dados da campanha**, você pode visualizar seus relatórios em uma série de painéis. Você pode ver mais ou menos do que os listados nas seções abaixo, mas cada um tem sua finalidade.

{% alert note %}
As estatísticas de abertura e relacionadas a cliques para o LINE são calculadas somente se mais de 20 usuários realizarem o evento em um determinado dia.
{% endalert %}

### Detalhes da campanha

O painel **Campaign Details (Detalhes da campanha** ) mostra uma visão geral de alto nível da performance de suas mensagens LINE.

Examine esse painel para ver as métricas gerais, como o número de mensagens enviadas para o número de destinatários, a taxa de conversão primária e a receita total gerada por essa mensagem. Você também pode revisar as configurações de entrega, público e conversão nessa página.

#### Grupos de controle

Para medir o impacto de uma mensagem LINE individual, é possível adicionar um [grupo de controle]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) a um Testes A/B. O painel de nível superior **Campaign Details** não inclui métricas da variante Control Group.

### Performance da LINE

O painel **LINE Performance** descreve o desempenho de sua mensagem em várias dimensões. As métricas nesse painel variam de acordo com o canal de envio de mensagens escolhido e com o fato de estar ou não executando um teste multivariante. Você pode clicar no ícone <i class="fa fa-eye preview-icon"></i> **Preview** para visualizar sua mensagem para cada variante ou canal.

![O painel "Desempenho da LINHA" mostra métricas para duas variantes.]({% image_buster /assets/img/line/line_performance.png %})

Se quiser simplificar sua visualização, selecione **\+ Add/Remove Columns (Adicionar/remover colunas** ) e limpe todas as métricas que desejar. Por padrão, todas as métricas são exibidas.

#### Métricas LINE

Aqui estão algumas das principais métricas da LINE que você pode ver em sua análise de dados. Para ver as definições de todas as métricas LINE usadas no Braze, consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data/report_metrics/).

| Prazo | Definição |
| --- | --- |
| Envios | O número total de envios comunicados com sucesso entre Braze e LINE. Isso não significa que a mensagem foi recebida pelo usuário. |
| Aberturas únicas projetadas | O número total de mensagens LINE enviadas que foram abertas pelos usuários após um limite mínimo de 20 mensagens por dia foi alcançado. |
| Total de aberturas | O número total de vezes que as mensagens LINE enviadas foram abertas pelos usuários após um limite mínimo de 20 mensagens por dia foi alcançado. |
| Cliques únicos projetados | O número total de mensagens LINE enviadas que foram clicadas pelos usuários, após um limite mínimo de 20 mensagens por dia ter sido alcançado. |
| Total de cliques | O número total de vezes que as mensagens LINE enviadas foram clicadas pelos usuários após um limite mínimo de 20 mensagens por dia ter sido alcançado. |
{: .reset-td-br-1 .reset-td-br-2 }

### Desempenho histórico

O painel **Desempenho histórico** permite que você visualize as métricas do painel **Desempenho de mensagens** como um gráfico ao longo do tempo. Use os filtros na parte superior do painel para modificar as estatísticas e os canais mostrados no gráfico. O intervalo de tempo desse gráfico sempre refletirá o intervalo de tempo especificado na parte superior da página.

Para obter um detalhamento dia a dia, selecione o menu de hambúrguer <i class="fas fa-bars"></i> e selecione **Baixar CSV** para receber uma exportação CSV do relatório.

### Detalhes do evento de conversão
 
O painel **Detalhes do evento de conversão** mostra a performance de seus eventos de conversão para sua campanha. Para saber mais, consulte [Eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation).

### Correlação de conversão

O painel **Correlação de conversões** oferece insight sobre quais atribuições e comportamentos do usuário ajudam ou prejudicam os resultados definidos para as campanhas. Para saber mais, consulte [Correlação de conversão]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation).


