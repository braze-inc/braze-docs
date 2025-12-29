---
nav_title: Rastreamento de análise de segmentos
article_title: Rastreamento do Segment Analytics
page_order: 8
page_type: reference
description: "Este artigo de referência aborda o rastreamento de análise de segmentos e como visualizar a receita e as compras ao longo do tempo, as sessões ao longo do tempo e os eventos personalizados ao longo do tempo."
tool: 
  - Segments
  - Reports
---

# Rastreamento de análise de segmentos

> Quando o rastreamento analítico está ativado para um segmento, você pode visualizar sessões, eventos personalizados e receita ao longo do tempo para esse segmento.

Se você não ativar o rastreamento analítico para um segmento, ainda poderá acessar [estatísticas em tempo real]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#segment-statistics) para esse segmento e direcionar seus usuários com campanhas. A única diferença é se você pode acessar as ferramentas de análise específicas mencionadas nesta página.

## Ativação da análise de segmentos

Na seção **Segment Details** da página de um segmento, ative **o Analytics Tracking**.

\![Alternância de rastreamento do Analytics para um segmento]({% image_buster /assets/img_archive/A_Tracking_2.png %})

Um aplicativo pode ter o rastreamento ativado para até 25 segmentos. A Braze recomenda rastrear segmentos que são importantes para você analisar ao entender os efeitos de suas campanhas sobre sessões, receita e compras.

## Visualização de receitas e compras ao longo do tempo

Vá para **Analytics** > **Revenue Report** para visualizar os dados de [receita e compras ao longo do tempo para esse segmento]({{site.baseurl}}/user_guide/data/export_braze_data/exporting_revenue_data/).

\![Dados de receita por segmento]({% image_buster /assets/img_archive/Revenue.png %})

Para comparar visualmente os dados do segmento para qualquer intervalo de tempo personalizado, adicione ou remova segmentos do gráfico. Selecione **By Segment (Por segmento** ) no menu suspenso Breakdown ( **Detalhamento** ) e, em seguida, selecione seus segmentos em **Breakdown values (Valores de detalhamento**).

Selecione qualquer nome de segmento acima do gráfico para ativar ou desativar a visibilidade das métricas desse segmento.

\![Receita para vários segmentos]({% image_buster /assets/img_archive/segment_revenue_multiple.png %})

## Sessões ao longo do tempo

Da mesma forma, você pode encontrar dados sobre [sessões ao longo do tempo para esse segmento específico]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data) na página **inicial**.

Dados da sessão por segmento]({% image_buster /assets/img_archive/events_over_time2.png %})

## Visualizar eventos personalizados ao longo do tempo

Visualize dados sobre [eventos personalizados ao longo do tempo para segmentos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics) acessando **Analytics** > **Custom Events Report**.

## Uso de modelos do Query Builder

Quando o rastreamento analítico está ativado, você pode usar os modelos de relatório do Query Builder para detalhar as métricas de desempenho de campanhas, Canvas, variantes e etapas por segmentos. Para saber mais, confira [os dados do Segment]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment).

