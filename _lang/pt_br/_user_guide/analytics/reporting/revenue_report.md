---
nav_title: Relatório de receitas
article_title: Relatório de receitas
page_type: reference
description: "Esta página descreve como usar a página Relatório de receita para visualizar dados sobre a receita em períodos específicos de tempo, a receita de um produto específico e a receita total do app."
tool: Reports
---

# Relatório de receitas

> A página "Relatório de receita" permite visualizar dados sobre a receita em períodos específicos, a receita de um produto específico e a receita total do seu app.

Para visualizar um relatório de sua receita no dashboard, acesse **Análise de dados** > **Relatório de receita**. 

## Personalização do relatório de receita

Você pode personalizar seu relatório de receita selecionando um intervalo de datas, os apps a serem relatados e os parâmetros.

![A página "Revenue Report" mostra o gráfico "Performance Over Time" com "Revenue" definido como parâmetro.]({% image_buster /assets/img/revenue_report.png %})

### Filtragem por data e aplicativos

Selecione o intervalo de datas para seu relatório de receita e, se desejar, um aplicativo específico ou uma seleção de aplicativos.

### Filtragem por parâmetros

O gráfico **Performance Over Time** mostra os dados de diferentes parâmetros, que podem ser selecionados no menu suspenso **Statistics for (Estatísticas para** ). Opcionalmente, você pode detalhar os dados de determinados parâmetros no menu suspenso **Detalhamento**.

Você pode visualizar os seguintes dados no **gráfico Performance Over Time**:
- Fórmulas de KPI
- Compras
    - (Opcional) Compras por produto
- Receita
    - (Opcional) Receita por segmento
    - (Opcional) Receita por produto
- Receita por hora
    - (Opcional) Receita por hora por segmento
- Receita por usuário

## Compreensão dos cálculos de receita

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrico</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">Receitas por tempo de vida</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">Valor de tempo de vida por usuário</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">Receita média diária</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-purchases">Compras diárias</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">Receitas diárias por usuário</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

## Visualização do detalhamento do produto

Consulte a tabela **Detalhamento de produtos** para obter uma lista dos produtos comprados durante o intervalo de datas selecionado, quantos de cada produto foram comprados e a receita gerada por cada produto.

![A tabela "Product Breakdown" (Detalhamento do produto) mostra as colunas "Product Name" (Nome do produto), "Purchased" (Comprado) e "Revenue" (Receita).]({% image_buster /assets/img/revenue_report_product_breakdown.png %})


