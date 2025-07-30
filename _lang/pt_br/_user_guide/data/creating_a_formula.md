---
nav_title: Criação de uma fórmula
article_title: Criação de uma fórmula
page_order: 1.2
page_type: reference
description: "Este artigo de referência aborda a criação e o gerenciamento de fórmulas, que o ajudam a entender facilmente as relações complexas existentes em seus dados."
tool: Reports

---
# Criação de uma fórmula

> Ao visualizar a análise de dados no Braze, é possível combinar vários pontos de dados para obter insights valiosos sobre os dados de usuários. Essas fórmulas são chamadas de fórmulas. Use fórmulas para normalizar os dados da série temporal com base no número total de usuários ativos mensais (MAU) e usuários ativos diários (DAU). 

As fórmulas o ajudam a entender as relações complexas que existem em seus dados. Por exemplo, é possível comparar quantos eventos personalizados foram concluídos por usuários ativos diários que se qualificam para um determinado segmento em comparação com a população geral (ou com outro segmento).

## Casos de uso

As fórmulas, especialmente quando combinadas com eventos personalizados, podem ajudá-lo a entender o comportamento do usuário em seu app. As fórmulas também podem fornecer insights mais profundos sobre os padrões de compra do segmento, mesmo que sua empresa use mídia paga em conjunto com o Braze, como o Google Ads ou a TV. 

A seguir, alguns exemplos dos tipos de padrões de comportamento que podem ser detectados com o uso de fórmulas:

- **Aplicativos de viagem por aplicativo:** Se você tiver um evento personalizado para quando o usuário cancelar uma viagem, poderá configurar uma função para Canceled Rides / DAU para descobrir se determinados segmentos de usuários tendem a cancelar mais viagens do que outros.
- **Apps de comércio eletrônico:** Ao configurar uma função para compras de um determinado ID de produto/MAU, você pode comparar a popularidade de um produto promovido recentemente entre segmentos, mesmo que todas as promoções não possam ser rastreadas usando o Braze.
- **Aplicativos de mídia que usam anúncios:** Se a experiência dos usuários for interrompida por anúncios entre clipes de vídeo ou áudio, registrar as saídas no meio do anúncio como um evento personalizado e calcular a proporção de saídas no meio do anúncio / DAU pode ajudar a encontrar os melhores segmentos para direcionamento com uma campanha para inscrições premium sem anúncios.

## Criação de fórmulas

As fórmulas podem ser acessadas nos painéis de estatísticas nas páginas [Página inicial]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/), [Relatório de receitas]({{site.baseurl}}/user_guide/data/export_braze_data/exporting_revenue_data/) e [Relatório de eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) no dashboard. Para visualizar esse painel, acesse o gráfico **Performance Over Time**, altere o menu suspenso **Statistics For (Estatísticas para** ) para **KPI Formulas (Fórmulas de KPI**) e selecione pelo menos uma fórmula de KPI para preencher o gráfico.

![Exibir estatísticas para fórmulas de KPI no dashboard do Braze]({% image_buster /assets/img_archive/kpi_forms.png %})

Para criar uma nova fórmula:

1. Acesse o dashboard apropriado**(Página inicial**, **Relatório de receita** ou **Relatório de eventos personalizados**).
2. Selecione **Manage KPI Formulas (Gerenciar fórmulas de KPI**).
3. Digite um nome para sua fórmula.
4. Selecione os numeradores e denominadores relevantes.
5. Selecione **Salvar**.

## Numeradores e denominadores disponíveis

<style>
  div.small_table + table {
    max-width: 50%;
  }
  div.large_table + table {
    max-width: 75%;
  }
table th:nth-child(1),
table th:nth-child(2),
table th:nth-child(3),
table td:nth-child(1),
table td:nth-child(2),
table td:nth-child(3) {
    width:25%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

### Painel de visão geral

| Numeradores | Denominadores |
| --- | --- |
| DAU | MAU |
| Sessões | DAU |
| | Tamanho do segmento |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Painel de receitas

| Numeradores | Denominadores |
| --- | --- |
| Compras (todas) | DAU |
| Selecione compras (como um cartão-presente ou ID de produto) | MAU |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Dashboard de eventos personalizado

| Numeradores | Denominadores |
| --- | --- |
| Contagem de eventos personalizados | MAU |
|  | DAU |
|  | Tamanho do segmento (somente segmentos que tenham [a análise de dados]({{site.baseurl}}/viewing_and_understanding_segment_data/) ativada podem ser usados) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

