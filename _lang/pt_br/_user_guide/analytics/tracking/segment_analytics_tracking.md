---
nav_title: Rastreamento da análise de dados por segmento
article_title: Rastreamento da análise de dados por segmento
page_order: 8
page_type: reference
description: "Este artigo de referência aborda o rastreamento da análise de dados do segmento e como visualizar a receita e as compras ao longo do tempo, as sessões ao longo do tempo e os eventos personalizados ao longo do tempo."
tool: 
  - Segments
  - Reports
---

# Rastreamento de análise de dados por segmento

> Quando a análise de dados está ativada para um segmento, você pode visualizar sessões, eventos personalizados e receita ao longo do tempo para esse segmento.

Se você não ativar o rastreamento da análise de dados para um segmento, ainda poderá acessar [estatísticas em tempo real]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#segment-statistics) para esse segmento e direcionar seus usuários com campanhas. A única diferença é se você pode acessar as ferramentas de análise específicas mencionadas nesta página.

## Ativação da análise de dados do segmento

Na seção **Segment Details** da página de um segmento, ative **o rastreamento do Analytics**.

![Alternância de rastreamento de análise de dados para um segmento]({% image_buster /assets/img_archive/A_Tracking_2.png %})

Um app pode ter o rastreamento ativado para até 25 segmentos. O Braze recomenda o rastreamento de segmentos que são importantes para sua análise ao entender os efeitos de suas campanhas sobre sessões, receita e compras.

## Visualização da receita e das compras ao longo do tempo

Acesse **Análise** **de dados** > **Relatório de receita** para visualizar os dados sobre [receita e compras ao longo do tempo para esse segmento]({{site.baseurl}}/user_guide/data/export_braze_data/exporting_revenue_data/).

![Dados de receita por segmento]({% image_buster /assets/img_archive/Revenue.png %})

Para comparar visualmente os dados do segmento para qualquer intervalo de tempo personalizado, adicione ou remova segmentos do gráfico. Selecione **By Segment (Por segmento** ) no menu suspenso Breakdown ( **Detalhamento** ) e, em seguida, selecione seus segmentos em **Breakdown values (Valores de detalhamento)**.

Selecione qualquer nome de segmento acima do gráfico para ativar ou desativar a visibilidade das métricas desse segmento.

![Receita de vários segmentos]({% image_buster /assets/img_archive/segment_revenue_multiple.png %})

## Sessões ao longo do tempo

Da mesma forma, você pode encontrar dados sobre [sessões ao longo do tempo para esse segmento específico]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data) na página **inicial**.

![Dados da sessão por segmento]({% image_buster /assets/img_archive/events_over_time2.png %})

## Visualizar eventos personalizados ao longo do tempo

Visualize dados sobre [eventos personalizados ao longo do tempo para segmentos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics) acessando **Analytics** > **Custom Events Report**.

## Uso de modelos do Query Builder

Quando a análise de dados está ativada, você pode usar os modelos de relatório do Criador de consultas para detalhar as métricas de performance de campanhas, Canvas, variantes e etapas de segmentos. Para saber mais, confira os [dados do segmento]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment).

