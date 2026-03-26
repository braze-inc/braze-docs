---
nav_title: Insights
article_title: Relatório de insights
page_order: 2
description: "Saiba como usar o relatório de insights para entender como as opções de recomendação no seu banco de ações são geradas no BrazeAI Decisioning Studio."
---

# Relatório de insights

> Os insights mostram como as diversas opções de recomendação no seu banco de ações são geradas, como a seleção de blocos. Existem dois relatórios de insights diferentes: **Preferências do agente** e **SHAPs**.

{% tabs local %}
{% tab agent preferences %}
O relatório **Preferências do agente** ajuda você a identificar tendências sazonais e avaliar a relevância das escolhas no banco de ações, orientando decisões informadas para atualizações.

![Relatório de preferências do agente mostrando um gráfico de barras comparando a frequência com que diferentes opções de recomendação foram selecionadas em um período específico. O gráfico exibe várias barras coloridas, cada uma representando uma opção de recomendação do banco de ações, com o eixo y indicando a porcentagem de vezes escolhida e o eixo x listando os nomes das opções.]({% image_buster /assets/img/decisioning_studio/reporting_insights_agent_preferences.png %})

Consulte a tabela a seguir para mais detalhes sobre este relatório:

| Campo | Descrição |
|-------|-------------|
| Dimensão | O atributo usado para organizar os resultados, como canal, campanha ou plataforma. |
| Grupo de comparação | Os grupos que você deseja comparar no seu relatório. Você pode selecionar múltiplos grupos de comparação. |
| Parâmetro | A métrica aplicada a esse atributo, como aberturas, cliques ou taxa de conversão. |
| Segmento faturável | O [segmento de público]({{site.baseurl}}/user_guide/engagement_tools/segments/) que você criou na Braze. |
| Opção             | A opção de recomendação específica selecionada do banco de ações. |
| Descrição        | Uma breve explicação do que a opção representa.            |
| Nº de vezes escolhida  | A contagem total de quantas vezes a opção foi selecionada.         |
| % de vezes escolhida   | A porcentagem do total de seleções em que esta opção foi escolhida. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab SHAPs %}
O relatório **SHAPs** usa o modelo Shapley Additive exPlanations (SHAP) para ajudar você a quantificar como cada recurso ou variável contribui para o seu agente de recomendação. Cada ponto no gráfico representa um SHAP, e a distribuição dos pontos representa uma noção geral do impacto direcional de um recurso.

![Gráfico do relatório SHAPs exibindo um gráfico de barras horizontais com múltiplas barras coloridas representando diferentes recursos ou variáveis. Cada barra mostra o impacto de um recurso no agente de recomendação, com o eixo x indicando o valor SHAP e o eixo y listando nomes de recursos como Recência, Frequência e Canal. O gráfico visualiza como cada recurso contribui positiva ou negativamente para as previsões do agente.]({% image_buster /assets/img/decisioning_studio/reporting_insights_shaps.png %})

{% endtab %}
{% endtabs %}