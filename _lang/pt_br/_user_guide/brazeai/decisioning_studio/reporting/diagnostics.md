---
nav_title: Diagnósticos
article_title: Relatório de diagnósticos
page_order: 3
description: "Saiba como usar o relatório de diagnósticos para monitorar a integridade dos dados de saída e entrada no BrazeAI Decisioning Studio."
---

# Relatório de diagnósticos

> O relatório de diagnósticos contém dois tipos diferentes de relatório: **Saída** e **Entrada**.

{% tabs local %}
{% tab outbound %}
O relatório de diagnósticos de saída mostra o volume diário de recomendações geradas e ativadas nos seus públicos. Use-o para identificar problemas de entrega, rastrear picos ou quedas nas ativações e confirmar que as mensagens estão alcançando os grupos certos conforme esperado.

![Relatório de diagnósticos de saída mostrando um gráfico de linhas que rastreia o volume diário de recomendações geradas e ativadas para diferentes grupos de público. O gráfico exibe duas linhas rotuladas como Geradas e Ativadas, com o eixo y representando o número de recomendações e o eixo x mostrando as datas. Uma legenda identifica cada linha por cor. A interface inclui filtros suspensos para intervalo de datas e seleção de público acima do gráfico.]({% image_buster /assets/img/decisioning_studio/reporting_diagnostics_outbound.png %})

{% endtab %}

{% tab inbound %}

O relatório de diagnósticos de entrada monitora a integridade dos seus Data Feeds no BrazeAI<sup>TM</sup>. Ele rastreia informações como contagem de arquivos, tamanhos e volumes de linhas para cada ativo, ajudando você a confirmar que os dados estão fluindo conforme esperado e a solucionar problemas antes que afetem seus agentes ou campanhas.

Você pode usar o menu suspenso para selecionar diferentes métricas do gráfico, como tamanho médio do arquivo ou contagem de arquivos.

![Relatório de diagnósticos de entrada mostrando um gráfico de linhas que rastreia a contagem diária de arquivos e o tamanho médio dos arquivos para ativos de dados entregues ao BrazeAI<sup>TM</sup>. O gráfico exibe duas linhas rotuladas como Contagem de arquivos e Tamanho médio do arquivo em MBs, com o eixo y representando valores e o eixo x mostrando as datas. Acima do gráfico estão filtros suspensos para intervalo de datas e seleção de ativo de dados.]( {% image_buster /assets/img/decisioning_studio/reporting_diagnostics_inbound.png %} )

Consulte a tabela a seguir para mais informações sobre cada métrica no relatório de entrada:

| Campo | Descrição |
|-------|-------------|
| Ativo de dados | O nome do conjunto de dados ou arquivo entregue. |
| Data | A data em que os dados foram recebidos. |
| Hora da última entrega | O horário mais recente em que os dados foram entregues. |
| Contagem de arquivos | O número total de arquivos recebidos. |
| Tamanho máximo do arquivo (MBs) | O tamanho do maior arquivo recebido, em megabytes. |
| Tamanho médio do arquivo (MBs) | O tamanho médio de todos os arquivos recebidos, em megabytes. |
| Contagem de linhas do arquivo | O número total de linhas contidas nos arquivos entregues. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}