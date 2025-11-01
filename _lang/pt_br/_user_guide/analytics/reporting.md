---
nav_title: Seus relatórios
article_title: Seus relatórios
page_order: 7
layout: dev_guide
guide_top_header: "Seus relatórios"
guide_top_text: "Seus dados são muito importantes para você, portanto, temos a capacidade de várias opções de relatórios no Braze (não incluindo o <a href='/docs/user_guide/data/distribution/braze_currents/'>Currents</a>). Se você não souber por onde começar, consulte a <a href='/docs/user_guide/analytics/reporting/#reports-overview'>Visão geral dos relatórios</a> para obter orientação sobre quais relatórios e análises você pode usar para responder a perguntas comuns sobre estratégia de marketing."

page_type: landing
description: "Esta página de destino contém artigos sobre as opções de relatórios disponíveis no Braze (não incluindo o Currents), incluindo relatórios de segmentos, relatórios de engajamento, o criador de relatórios e muito mais."
tool: Reports
search_rank: 2
guide_featured_title: "Artigos de seção"
guide_featured_list:
  - name: Glossário de métricas de relatórios
    link: /docs/user_guide/analytics/reporting/report_metrics/
    image: /assets/img/braze_icons/book-closed.svg
  - name: Dados do segmento
    link: /docs/viewing_and_understanding_segment_data/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Relatórios de engajamento
    link: /docs/user_guide/analytics/reporting/engagement_reports/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: Criador de relatórios
    link: /docs/user_guide/analytics/reporting/report_builder/
    image: /assets/img/braze_icons/tool-01.svg
  - name: Criador de painel
    link: /docs/user_guide/analytics/reporting/dashboard_builder/
    image: /assets/img/braze_icons/tool-01.svg

guide_menu_title: "More articles"
guide_menu_list:
  - name: Configuração de relatórios
    link: /docs/user_guide/analytics/reporting/configuring_reporting/
    image: /assets/img/braze_icons/settings-01.svg
  - name: Análise de campanhas
    link: /docs/user_guide/analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: Análise do Canvas
    link: /docs/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/
    image: /assets/img/braze_icons/line-chart-down-01.svg
  - name: Eventos personalizados
    link: /docs/user_guide/data/custom_data/custom_events/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: Relatório de funil
    link: /docs/user_guide/analytics/reporting/funnel_reports/
    image: /assets/img/braze_icons/flag-02.svg
  - name: Relatório de controle global
    link: /docs/user_guide/engagement_tools/testing/global_control_group/
    image: /assets/img/braze_icons/globe-04.svg
  - name: Relatório de retenção
    link: /docs/user_guide/analytics/reporting/retention_reports/
    image: /assets/img/braze_icons/user-check-01.svg
  - name: Dados de receita
    link: /docs/user_guide/data/export_braze_data/exporting_revenue_data/
    image: /assets/img/braze_icons/piggy-bank-02.svg
  - name: Relatório de receita
    link: /docs/user_guide/analytics/reporting/revenue_report/
    image: /assets/img/braze_icons/piggy-bank-02.svg
  - name: Informações sobre o segmento
    link: /docs/user_guide/engagement_tools/segments/segment_insights/#segment-insights
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Relatório do Grupo de Controle Global
    link: /docs/user_guide/analytics/reporting/global_control_group_reporting/
    image: /assets/img/braze_icons/globe-slated-02.svg
---

# Visão geral dos relatórios

## Qual variante venceu?

{% tabs local %}
{% tab Campaign Analytics %}
**Análise de campanhas**

Use o [Campaign Analytics]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) para obter atualizações em tempo real sobre os resultados de alto nível de cada campanha e variante dentro dessa campanha, bem como detalhes em nível de mensagem. Você pode ajustar o intervalo de datas para entender o desempenho da campanha ao longo do tempo e visualizar suas mensagens para lembrar o que estava testando.

{% endtab %}

{% tab Canvas Analytics %}
**Análise do Canvas**

Use [o Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para obter estatísticas de primeira linha sobre seu Canvas e ver o desempenho de sua estratégia de mensagens. Abra qualquer Canvas ao vivo para ver as principais estatísticas de desempenho, como:

- Número de mensagens enviadas dentro do Canvas
- Número total de vezes que os clientes entraram no Canvas
- Quantos clientes converteram
- Receita gerada pelo Canvas
- Público total estimado

<br>

**Desempenho por variante**

[Analise as variantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) em um Canvas ao vivo para visualizar as taxas de conversão calculadas automaticamente para cada evento de conversão. Você também pode visualizar os cálculos de aumento e confiança para cada variante e evento de conversão em um formato de tabela fácil de comparar.

Você pode responder a mais perguntas com este relatório:

- Houve confiança estatisticamente significativa?
- Qual foi o desempenho da Variante 1 em relação à Variante 2?

{% endtab %}

{% tab Report Builder %}
**Criador de relatórios**

Use o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) para comparar os resultados de várias campanhas ou Canvases em uma única exibição e determinar rapidamente quais estratégias de engajamento tiveram maior impacto em suas principais métricas.

Confira esta página para:

- Crie um relatório de campanhas e Canvases da última semana ou mês, calcule métricas críticas e compartilhe com seus colegas de equipe.
- Compare o desempenho entre variantes para testes multivariados e Canvases.
- Determine qual canal de mensagens obteve a maior conversão ou engajamento em uma campanha ou Canvas específico.
- Rastrear tendências gerais de desempenho de um grupo de campanhas ou Canvases (como todas as mensagens relacionadas a uma tag "newsletters").

Você pode responder a mais perguntas com esse recurso:

- Qual foi o desempenho da primeira versão do meu e-mail de boas-vindas em comparação com a segunda versão?
- Quais foram minhas taxas médias de abertura de push deste mês em comparação com o mês passado, para uma determinada tag?
- Qual boletim informativo do mês teve o maior número de conversões?

{% endtab %}
{% endtabs %}

## Qual variante teve maior impacto na retenção?

{% tabs local %}
{% tab Retention Reports %}
**Relatórios de retenção**

Use os Relatórios de retenção para [campanhas]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) ou [Canvases]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) para medir a retenção de usuários que realizaram um evento selecionado em uma campanha específica.

Confira este relatório para:

- Determine a eficácia de uma mensagem para reengajar os usuários a longo prazo, analisando a ocorrência de diferentes eventos até um mês após o recebimento de uma campanha.
- Compare a ocorrência de diferentes eventos entre as variantes de um [teste A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

Você pode responder a mais perguntas com este relatório:

- Qual variante teve maior impacto na retenção?
- Por quanto tempo meus clientes que receberam essa campanha continuarão a usar meu aplicativo depois disso?
- Qual foi o impacto dessa campanha na retenção após um dia? Depois de 30 dias?

{% alert note %} Os Relatórios de retenção não estão disponíveis para campanhas acionadas por SMS e API. {% endalert %}

{% endtab %}
{% tab Funnel Report %}

Use relatórios de funil para [campanhas]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) ou [Canvases]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) para analisar as jornadas de seus clientes após o recebimento de uma campanha. Você pode escolher quais eventos nativos ou personalizados incluir em cada análise de funil e, em seguida, analisar o desempenho de cada variante em relação ao funil de conversão selecionado.

Confira este relatório para:

- Entenda em que ponto do funil de conversão os usuários saíram e identifique oportunidades para mensagens de reengajamento.
- Visualize as conversões de um evento que não foi originalmente incluído como um evento de conversão ao configurar a campanha.
- Analise o funil de compras usando uma série de ações (como "Qual a porcentagem de clientes que receberam um e-mail, iniciaram uma sessão, adicionaram um item ao carrinho e depois compraram?").

Você pode responder a mais perguntas com este relatório:

- Em que ponto do caminho para a conversão meus clientes caem?
- Como posso aprimorar minhas estratégias de marketing?

{% endtab %}
{% endtabs%}

## Qual é o grau de envolvimento dos meus usuários?

{% tabs local %}
{% tab Report Builder %}

Use o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) para comparar os resultados de várias campanhas ou Canvases em uma única exibição e determinar rapidamente quais estratégias de engajamento tiveram maior impacto em suas principais métricas.

Confira esta página para:

- Crie um relatório de campanhas e Canvases da última semana ou mês, calcule métricas críticas e compartilhe com seus colegas de equipe.
- Determine qual canal de mensagens obteve a maior conversão ou engajamento em uma campanha ou Canvas específico.
- Rastrear tendências gerais de desempenho de um grupo de campanhas ou Canvases (como todas as mensagens relacionadas a uma tag "newsletters").

Você pode responder a mais perguntas com esse recurso:

- Qual foi o desempenho da primeira versão do meu e-mail de boas-vindas em comparação com a segunda versão?
- Quais foram minhas taxas médias de abertura de push deste mês em comparação com o mês passado, para uma determinada tag?
- Qual boletim informativo do mês teve o maior número de conversões?

{% endtab %}
{% tab Overview Data %}
**Visão geral dos dados**

Use a página [Overview (Visão geral]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/) ) para obter um resumo de alto nível das principais métricas relacionadas ao desempenho do seu aplicativo e uma visão da base de usuários do seu aplicativo.

Dê uma olhada nesta página para ver essas estatísticas:

- Usuários vitalícios
- Sessões vitalícias
- Usuários ativos mensais (MAU)
- Usuários ativos diários (DAU)
- Novos usuários
- Aderência
- Sessões diárias
- Sessão diária por MAU

Você pode responder a mais perguntas com esse painel:

- Estou vendo uma melhora na aderência mês a mês?
- Estou vendo um crescimento geral do meu aplicativo para iOS ou Android?
- Qual é o meu volume geral de e-mails neste mês?

{% endtab %}
{% tab Engagement Reports %}
**Relatórios de engajamento**

Use [os Relatórios de envolvimento]({{site.baseurl}}/user_guide/analytics/reporting/engagement_reports/) para configurar uma exportação recorrente por e-mail das estatísticas de envolvimento para campanhas e Canvases selecionados. Esse relatório é o relatório mais personalizável e granular disponível no painel.

Você pode exportar as seguintes estatísticas, dependendo do seu canal de mensagens:

| canal| estatísticas disponíveis|
| ------| --------------|
| E-mail | Envios, aberturas, aberturas exclusivas, cliques, cliques exclusivos, cliques para abrir, cancelamentos de assinatura, devoluções, entregas, spam denunciado |
| Empurrar  | Envios, aberturas, aberturas influenciadas, rejeições, cliques no corpo |
| Empurrar pela Web | Envios, aberturas, rejeições, cliques no corpo |
| Mensagem no aplicativo | Impressões, cliques, cliques no primeiro botão, cliques no segundo botão |
| Webhook  |  Envios, erros |
| SMS | Envios, Envios para a transportadora, Entregas confirmadas, Falhas na entrega, Rejeições |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Você pode responder a mais perguntas com este relatório:

- Qual é o desempenho de todas as minhas mensagens de "retorno"?
- Qual é minha taxa de entrega agregada para minhas campanhas de e-mail?
- Como foi o desempenho de todas as minhas campanhas do Braze em junho? Para 2021 até o momento?
- Quais são as tendências que vejo nos testes multivariados?

{% endtab %}
{% endtabs %}

## Como os comportamentos dos usuários diferem por segmento?

{% tabs local %}
{% tab Segment Data %}
**Dados do segmento**

Se você tiver ativado [o rastreamento analítico]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) para um segmento, abra esse segmento para visualizar [Segment Data (Dados do segmento]({{site.baseurl}}/viewing_and_understanding_segment_data/)). O Segment Data rastreia sessões, eventos personalizados e receita ao longo do tempo para os usuários aplicáveis.

Dê uma olhada nesta página para ver essas estatísticas:

- Número total de:
  - Usuários no seu segmento e qual é a porcentagem da sua base total de usuários
  - Usuários que podem enviar e-mails e que optaram explicitamente por recebê-los
  - Usuários habilitados para push que optaram explicitamente por receber notificações push
- Valor médio do tempo de vida (LTV) para usuários desse segmento
- Lista de ferramentas de engajamento que têm como alvo esse segmento
- Informações sobre o segmento

{% endtab %}
{% tab Segment Insights %}
**Informações sobre o segmento**

[O Segment Insights]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/) permite que você compare os segmentos entre si para entender como as métricas a seguir podem afetar aspectos como duração do ciclo de vida e frequência da sessão:

- Dados demográficos
- Plataformas
- Status de adesão
- Preferências de categoria
- Recebimento de campanha

Você pode responder a mais perguntas com este relatório:

- Qual foi a frequência de sessão dos usuários que receberam meu Canvas de integração em comparação com os do grupo de controle?
- Qual é a diferença na duração do ciclo de vida dos usuários que optaram pelo push em relação aos usuários que optaram pelo e-mail e em relação aos usuários que optaram por ambos?

{% endtab %}
{% tab Custom Events %}
**Eventos personalizados**

Use a página [Custom Events (Eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-analytics) ) para monitorar a frequência com que um evento personalizado ocorreu, bem como a última vez que cada usuário o realizou para segmentação.

Confira esta página para:

- Monitorar a frequência de eventos personalizados
- Monitorar eventos personalizados por segmento
- Analisar como as campanhas afetam a atividade de eventos personalizados
- Criar e monitorar [fórmulas de KPI]({{site.baseurl}}/user_guide/data/creating_a_formula/)
- Solucionar problemas de rastreamento de eventos personalizados

{% endtab %}
{% endtabs %}

## Minha campanha proporcionou um retorno sobre o investimento?

{% tabs local %}
{% tab Revenue Data %}
**Dados de receita**

Use a página [Receita]({{site.baseurl}}/user_guide/data/export_braze_data/exporting_revenue_data/) para rastrear a receita e as compras em períodos específicos ou a receita ou as compras totais do seu aplicativo.

Dê uma olhada nesta página para ver essas estatísticas:

- Resultados da fórmula de KPI
- Número de compras de produtos
- Receita para diferentes segmentos
- Receita de diferentes produtos
- Receita por hora
- Receita por hora para diferentes segmentos
- Receita por usuário

{% endtab %}
{% tab Global Control Group Report %}
**Relatório do Grupo de Controle Global**

Depois de configurar um [Grupo de Controle Global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/), use o [Relatório de Controle Global]({{site.baseurl}}/user_guide/analytics/reporting/global_control_group_reporting/) para avaliar o impacto do seu marketing no Braze como um todo. Esse relatório permite comparar os comportamentos dos usuários que recebem mensagens com os comportamentos dos usuários que não recebem, proporcionando uma melhor compreensão de como suas campanhas e Canvases estão contribuindo para suas metas de negócios.

Confira esta página para:

- Meça facilmente o impacto e o aumento incremental de campanhas e Canvases em sessões e eventos personalizados.
- Randomize e exclua automaticamente os membros do grupo de controle do recebimento de mensagens.
- Exportar membros do grupo de controle para análise posterior.

Mais perguntas que você pode responder com o relatório:

- Qual foi o efeito geral do envio de mensagens da Braze no comportamento do cliente?
- Qual é o ROI do Braze como uma plataforma (para renovação ou discussões com as partes interessadas)?

{% endtab %}
{% endtabs %}

## Quais campanhas devo realizar em seguida?

{% tabs local %}
{% tab Funnel Report %}

Use relatórios de funil para [campanhas]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) ou [Canvases]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) para analisar as jornadas de seus clientes após o recebimento de uma campanha. Você pode escolher quais eventos nativos ou personalizados incluir em cada análise de funil e, em seguida, analisar o desempenho de cada variante em relação ao funil de conversão selecionado.

Confira este relatório para:

- Entenda em que ponto do funil de conversão os usuários saíram e identifique oportunidades para mensagens de reengajamento.
- Visualize as conversões de um evento que não foi originalmente incluído como um evento de conversão ao configurar a campanha.
- Analise o funil de compras usando uma série de ações (como "Qual a porcentagem de clientes que receberam um e-mail, iniciaram uma sessão, adicionaram um item ao carrinho e depois compraram?").

Você pode responder a mais perguntas com este relatório:

- Em que ponto do caminho para a conversão meus clientes caem?
- Como posso aprimorar minhas estratégias de marketing?

{% endtab %}
{% tab Predictive Churn %}
**Churn preditivo**

[O Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_churn/) é o primeiro modelo do [Braze Predictive Suite]({{site.baseurl}}/user_guide/brazeai/). Use o Predictive Churn para definir e gerar previsões, fornecendo uma abordagem proativa para minimizar a rotatividade futura.

Como cada empresa define churn e retenção de forma diferente, você pode simplesmente inserir suas definições no Predictive Churn, e o Braze fará o resto. Você também pode criar campanhas ou Canvases para agir com base nas previsões ou criar segmentos para análise posterior.

Você pode responder a mais perguntas com esse recurso:

- Quantos dos meus usuários ideais correm o risco de perder o interesse?
- Quais comportamentos ou atributos os meus usuários em risco têm em comum?

{% endtab %}
{% tab Report Builder %}
**Criador de relatórios**

Use o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) para comparar os resultados de várias campanhas ou Canvases em uma única exibição e determinar rapidamente quais estratégias de engajamento tiveram maior impacto em suas principais métricas.

Confira esta página para:

- Crie um relatório de campanhas e Canvases da última semana ou mês, calcule métricas críticas e compartilhe com seus colegas de equipe.
- Compare o desempenho entre variantes para testes multivariados e Canvases.
- Determine qual canal de mensagens obteve a maior conversão ou engajamento em uma campanha ou Canvas específico.
- Rastrear tendências gerais de desempenho de um grupo de campanhas ou Canvases (como todas as mensagens relacionadas a uma tag "newsletters").

Você pode responder a mais perguntas com esse recurso:

- Qual foi o desempenho da primeira versão do meu e-mail de boas-vindas em comparação com a segunda versão?
- Quais foram minhas taxas médias de abertura de push deste mês em comparação com o mês passado, para uma determinada tag?
- Qual boletim informativo do mês teve o maior número de conversões?

{% endtab %}
{% endtabs %}
