---
nav_title: Relatórios e Insights
article_title: Relatórios e Insights
page_order: 3
description: "Saiba como visualizar os relatórios do BrazeAI Decisioning Studio™ no Braze, para que você possa entender como as decisões baseadas em IA afetam suas campanhas."
---

# Relatórios e Insights

> Saiba como visualizar os relatórios do BrazeAI Decisioning Studio™ no Braze, para que você possa entender como as decisões baseadas em IA afetam suas campanhas. Desde as métricas de desempenho até a integridade dos dados e as alterações no sistema, esses relatórios ajudam você a entender os resultados, solucionar problemas e tomar decisões informadas com confiança.

## Pré-requisitos

Antes de poder visualizar os relatórios do Decisioning Studio no Braze, você precisará:

- Ter um contrato ativo para o Braze e o BrazeAI Decisioning Studio™. 
- Entre em contato com seu CSM para habilitar o BrazeAI Decisioning Studio™ para você em seu nome.
- Tenha um agente do BrazeAI Decisioning Studio™ ao vivo.

## Visualização de relatórios {#view}

Para visualizar métricas de agentes de um estúdio de decisão no Braze, acesse **AI Decisioning** > **BrazeAI Decisioning Studio™** e, em seguida, selecione um agente.

Tela inicial de relatórios do BrazeAI Decisioning Studio™ mostrando um painel com vários cartões de relatório. Cada cartão exibe um tipo de relatório, como Desempenho, Insights, Diagnóstico e Linha do tempo, com breves descrições e ícones para cada um.]( {% image_buster /assets/img/decisioning_studio/reporting_home.png %} )

Aqui, você pode visualizar relatórios como desempenho, insights, diagnósticos e linhas do tempo. Para obter mais detalhes, consulte [Relatórios disponíveis](#reports).

## Alteração de datas de relatórios

Após [abrir um relatório](#view), você pode alterar o intervalo de datas selecionando uma nova data inicial e final no menu suspenso do calendário.

O seletor de intervalo de datas do BrazeAI Decisioning Studio™ é aberto com um menu suspenso de calendário. O calendário exibe datas de início e término selecionáveis para personalizar a exibição do relatório.]({% image_buster /assets/img/decisioning_studio/reporting_change_date_range.png %}){: style="max-width:50%;"}

Você também pode definir uma data de início padrão ou escolher datas a serem sempre excluídas. As datas excluídas serão filtradas de todos os relatórios desse agente.

Para definir ou excluir datas, selecione <i class="fa-solid fa-gear"></i> **Settings** e, em seguida, altere a data padrão ou exclua as datas conforme necessário.

\![Painel de configurações aberto no BrazeAI Decisioning Studio™ mostrando opções para definir uma data de início padrão e excluir datas específicas dos relatórios. O painel exibe duas seções denominadas Data de início padrão e Excluir datas. Em Excluir datas, várias datas são listadas com caixas de seleção ao lado de cada uma.]({% image_buster /assets/img/decisioning_studio/reporting_set_exclude_dates.png %})

## Relatórios disponíveis {#reports}

### Desempenho

O relatório de desempenho oferece métricas de agente de alto nível que comparam grupos de tratamento (do Braze) a um ou mais grupos de controle (como receita). Ele oferece suporte a duas visões diferentes: **Árvore****de tendências** e **de motoristas**.

Por padrão, o relatório usa a visualização **Tendências**, que compara o desempenho do BrazeAI™ ao longo do tempo em relação aos seus grupos de controle e acompanha a evolução do aumento.

Visualização de tendências do relatório de desempenho mostrando um gráfico de linhas comparando o desempenho do BrazeAI™ e do grupo de controle ao longo do tempo. O gráfico exibe duas linhas rotuladas como BrazeAI™ e Controle, com o eixo y rotulado como Uplift e o eixo x mostrando as datas. Uma legenda identifica cada grupo por cor.]({% image_buster /assets/img/decisioning_studio/reporting_agent_performance_trending.png %})

Como alternativa, você pode selecionar **Árvore de** drivers para visualizar como os principais drivers de valor estão vinculados às métricas de destino, ajudando-o a entender melhor a relação entre eles.

Visualização em árvore do driver do relatório de desempenho mostrando um diagrama hierárquico que mapeia os principais drivers de valor para as métricas de destino. O diagrama exibe vários nós conectados, cada um rotulado com um nome de driver ou métrica, ilustrando como diferentes fatores contribuem para o desempenho geral.]({% image_buster /assets/img/decisioning_studio/reporting_performance_drivertree.png %})

Para comparar o desempenho entre dois grupos, use os menus suspensos para selecionar os critérios de comparação desejados. Consulte a tabela a seguir para obter mais detalhes:

| Campo | Descrição |
|-------|-------------|
| Grupos de comparação | Os grupos que você deseja comparar em seu relatório. |
| Agregação | A forma como o relatório agrupa os dados, como totais, médias ou porcentagens. |
| Segmentos | Os [segmentos de público-alvo]({{site.baseurl}}/user_guide/engagement_tools/segments/) que você criou no Braze. |
| Eventos da linha do tempo | Os eventos específicos mostrados ao longo do tempo, como envios de mensagens, aberturas ou conversões. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Insights

Os insights mostram como são geradas as várias opções de recomendação em seu banco de ações, como SL ou seleção de blocos. Há dois relatórios de insights diferentes: **Preferências do agente** e **SHAPs**.

{% tabs local %}
{% tab agent preferences %}
O relatório de **preferências do agente** o ajuda a identificar tendências sazonais e a avaliar a relevância das escolhas no banco de ações, orientando decisões informadas para atualizações.

Relatório de preferências do agente mostrando um gráfico de barras que compara a frequência com que diferentes opções de recomendação foram selecionadas em um período de tempo específico. O gráfico exibe várias barras coloridas, cada uma representando uma opção de recomendação do banco de ações, com o eixo y rotulado como porcentagem do tempo escolhido e o eixo x listando os nomes das opções.]({% image_buster /assets/img/decisioning_studio/reporting_insights_agent_preferences.png %})

Consulte a tabela a seguir para obter mais detalhes sobre esse relatório:

| Campo | Descrição |
|-------|-------------|
| Dimensão | O atributo usado para organizar os resultados, como canal, campanha ou plataforma. |
| Grupo de comparação | Os grupos que você deseja comparar em seu relatório. Você pode selecionar vários grupos de comparação, até NUM. |
| Parâmetro | A métrica aplicada a esse atributo, como aberturas, cliques ou taxa de conversão. |
| Segmento | O [segmento de público-alvo]({{site.baseurl}}/user_guide/engagement_tools/segments/) que você criou no Braze. |
| Opção             | A opção de recomendação específica selecionada no banco de ações. |
| Descrição        | Uma breve explicação do que a opção representa.            |
| \# Número de vezes escolhido  | A contagem total da frequência com que a opção foi selecionada.         |
| % do tempo escolhido   | A porcentagem do total de seleções em que essa opção foi escolhida. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab shaps %}
O relatório **SHAPs** usa o modelo SHapley Additive exPlanations (SHAP) para ajudá-lo a quantificar como cada recurso ou variável contribui para o seu modelo de recomendação. Cada ponto no gráfico representa um SHAP e a distribuição dos pontos representa um senso geral do impacto direcional de um recurso.

Gráfico de relatório de SHAPs exibindo um gráfico de barras horizontais com várias barras coloridas representando diferentes recursos ou variáveis. Cada barra mostra o impacto de um recurso no modelo de recomendação, com o eixo x rotulado como valor SHAP e o eixo y listando os nomes dos recursos, como Recency, Frequency e Channel. O gráfico visualiza como cada recurso contribui positiva ou negativamente para as previsões do modelo.]({% image_buster /assets/img/decisioning_studio/reporting_insights_shaps.png %})

{% endtab %}
{% endtabs %}

### Diagnóstico

O relatório de diagnóstico contém dois tipos diferentes de relatório: **De saída** e **de entrada**.

{% tabs local %}
{% tab outbound %}
O relatório de diagnóstico de saída mostra o volume diário de recomendações geradas e ativadas em seus públicos. Use-o para identificar problemas de entrega, rastrear picos ou quedas nas ativações e confirmar se as mensagens estão chegando aos grupos certos conforme o esperado.

Relatório de diagnóstico de saída mostrando um gráfico de linhas que rastreia o volume diário de recomendações geradas e ativadas para diferentes grupos de público-alvo. O gráfico exibe duas linhas denominadas Generated (Gerado) e Activated (Ativado), com o eixo y representando o número de recomendações e o eixo x mostrando as datas. Uma legenda identifica cada linha por cor. A interface inclui filtros suspensos para intervalo de datas e seleção de público acima do gráfico.]({% image_buster /assets/img/decisioning_studio/reporting_diagnostics_outbound.png %})

{% endtab %}

{% tab inbound %}

O relatório de diagnóstico de entrada monitora a integridade de seus feeds de dados no BrazeAI™. Ele rastreia detalhes como contagens de arquivos, tamanhos e volumes de linhas para cada ativo, ajudando-o a confirmar que os dados estão fluindo conforme o esperado e a solucionar problemas antes que eles afetem seus modelos ou campanhas.

Você pode usar o menu suspenso para selecionar diferentes métricas de gráfico, como tamanho médio de arquivo ou contagem de arquivos.

Relatório de diagnóstico de entrada mostrando um gráfico de linhas que rastreia a contagem diária de arquivos e o tamanho médio dos arquivos dos ativos de dados entregues ao BrazeAI™. O gráfico exibe duas linhas denominadas Contagem de arquivos e Tamanho médio do arquivo MBs, com o eixo y representando valores e o eixo x mostrando datas. Acima do gráfico, há filtros suspensos para intervalo de datas e seleção de ativos de dados.]( {% image_buster /assets/img/decisioning_studio/reporting_diagnostics_inbound.png %} )

Consulte a tabela a seguir para obter mais detalhes sobre cada métrica no relatório de entrada:

| Campo | Descrição |
|-------|-------------|
| Ativo de dados | O nome do conjunto de dados ou arquivo entregue. |
| Data | A data em que os dados foram recebidos. |
| Último prazo de entrega | A hora mais recente em que os dados foram entregues. |
| Contagem de arquivos | O número total de arquivos recebidos. |
| Tamanho máximo do arquivo (MBs) | O tamanho do maior arquivo recebido, em megabytes. |
| Tamanho médio do arquivo (MBs) | O tamanho médio de todos os arquivos recebidos, em megabytes. |
| Contagem de linhas do arquivo | O número total de linhas contidas nos arquivos entregues. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}

### Linha do tempo

O relatório de linha do tempo fornece um registro visual dos principais eventos juntamente com as métricas de desempenho. Esses eventos incluem execuções de modelos, alterações de configuração, atualizações de grades de proteção e muito mais. As anotações são exibidas diretamente nos gráficos de elevação e em uma guia de linha do tempo dedicada, fornecendo contexto instantâneo para mudanças nos resultados sem a necessidade de rastrear alterações históricas.

Relatório de linha do tempo mostrando um gráfico com métricas de desempenho ao longo do tempo. Os principais eventos, como execuções de modelos, alterações de configuração e atualizações de grades de proteção, são marcados como ícones ao longo da linha do tempo. Abaixo do gráfico, uma tabela lista os eventos com colunas para data, tipo, rótulo, detalhes e visibilidade nos gráficos.]({% image_buster /assets/img/decisioning_studio/reporting_timeline.png %})

Para comparar o desempenho entre dois grupos, use os menus suspensos para selecionar os critérios de comparação desejados. Consulte a tabela a seguir para obter mais detalhes:

| Campo | Descrição |
|-------|-------------|
| Data | A data em que o evento ocorreu. |
| Tipo | A categoria do evento, como atualização do sistema, execução de modelo ou alteração de configuração. |
| Rótulo | O nome ou identificador dado ao evento. |
| Detalhes | Informações adicionais que descrevem o evento. |
| Visível em gráficos | Indica se o evento é exibido em gráficos relacionados. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
