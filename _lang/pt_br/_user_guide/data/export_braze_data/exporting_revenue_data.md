---
nav_title: Dados de receita de exportação e receita total
article_title: Dados de receita de exportação e receita total
page_order: 4
page_type: reference
description: "Este artigo de referência aborda como exportar dados e estatísticas de receita."
tool: 
  - Reports

---

# Dados de receita de exportação e receita total

> Esta página aborda a página [Relatório de receita]({{site.baseurl}}/user_guide/analytics/reporting/revenue_report/) do dashboard, onde você pode visualizar dados sobre a receita em períodos específicos, a receita de um produto específico e a receita total do seu app.

Você pode encontrar o **Relatório de receita** em **Análise de dados**.

{% alert tip %}
Procurando outras maneiras de obter dados de receita? Tente adicionar o comportamento de compra (bem como a compra de um produto) a campanhas ou telas como [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/).
{% endalert %}

Para exportar seus dados de receita, selecione <i class="fas fa-bars" title="Menu de contexto do gráfico"></i> no gráfico **Performance Over Time** e selecione sua opção de exportação.

## Gráfico de performance ao longo do tempo

Os dados a seguir podem ser visualizados no gráfico **Performance Over Time (Desempenho ao longo do tempo)**:

- Fórmulas de KPI
- Compras
    - (Opcional) Compras por produto
- Receita
    - (Opcional) Receita por segmento
    - (Opcional) Receita por produto
- Receita por hora
    - (Opcional) Receita por hora por segmento
- Receita por usuário

![Gráfico de receita]({% image_buster /assets/img_archive/Export_revenue_graph.png %})

## Total de receitas

Você pode visualizar as estatísticas de receita, caso a caso, nas páginas [Campaign Analytics]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) ou [Canva Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/). 

{% multi_lang_include metrics.md metric='Total Revenue' %}

{% alert tip %}
Os relatórios de receita não podem ser exportados por meio da API. Para obter ajuda com exportações CSV, consulte a [solução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% comment %}

## Receita direta

Você pode visualizar as seguintes métricas de receita adicionais gerando um Relatório de comparação de campanhas usando o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/):

- [Total em receitas diretas]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-revenue)
- [Total de compras diretas]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-purchases)
- [Compras diretas únicas]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#unique-direct-purchases)
- [Receita por destinatário]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#revenue-per-recipient)

Essas métricas se baseiam na atribuição do último clique, o que significa que a receita será atribuída a uma campanha se essa campanha for a mesma:

1. É a última campanha em que o usuário clicou antes de comprar
    <br>**E**<br>
2. Foi clicado pelo usuário menos de 3 dias antes da compra

{% endcomment %}




