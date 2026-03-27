---
nav_title: Performance
article_title: Relatório de performance
page_order: 1
description: "Saiba como usar o relatório de performance para comparar grupos de tratamento e grupos de controle no BrazeAI Decisioning Studio."
---

# Relatório de performance

> O relatório de performance mostra como o seu agente de decisão performa em comparação com os grupos de controle. Este guia explica o que cada seção do relatório representa, como as métricas são calculadas e como interpretar os resultados.

## Como o relatório é construído

Seu relatório de performance é construído em camadas, totalmente personalizado para o seu caso de uso. Trabalhando em colaboração com a sua equipe:

1. A Braze define o que conta como uma ação (como um envio, clique, compra ou conversão).
2. A Braze define como medir essa ação diariamente (volume, receita, pessoas únicas e similares).
3. A Braze define a métrica de negócios que você deseja ver (como taxa de conversão ou receita por usuário).
4. Regras de tempo e segmentação são aplicadas.
5. A guia **Performance** exibe os resultados.

Nada no dashboard cria novos dados. Ele visualiza resultados diários armazenados com base nessas definições.

## Intervalo de datas e grupos de comparação

No topo do dashboard, você escolhe:

- **Intervalo de datas**: O período de tempo do relatório.
- **Grupos de comparação**: Os grupos sendo comparados (como Decisioning Studio versus Business as Usual).
- **Agregação**: A configuração de agregação do gráfico (Diária, média móvel de 7 dias ou média móvel de 30 dias).
- **Segmentos**: Quaisquer segmentos aplicados. Eles são configurados de forma personalizada com a sua equipe de AI Expert Services.
- **Eventos da linha do tempo**: Se deseja sobrepor eventos configurados da linha do tempo no gráfico para ajudar você a entender mudanças ou eventos que podem impactar a performance.

![Relatório de performance mostrando os grupos de comparação, agregação, segmentos e filtros de eventos da linha do tempo no topo, junto com o seletor de intervalo de datas no canto superior direito.]({% image_buster /assets/img/decisioning_studio/reporting_performance_date_range.png %})

Essas seleções determinam quais dias são incluídos, quais grupos são comparados, como a linha de tendência é suavizada e qual população você está visualizando.

{% alert important %}
Alterar a configuração de agregação (como média móvel de 7 dias) afeta apenas a exibição do gráfico. Isso não altera os dados armazenados.
{% endalert %}

Se você não conseguir selecionar uma data recente no seletor de datas, essa data provavelmente está desabilitada para refletir um atraso temporário nos dados. Normalmente, leva alguns dias para que os dados do seu CDP cheguem ao Decisioning Studio de forma confiável.

## Cartões de KPI

Os cartões de KPI no lado esquerdo do relatório mostram os indicadores-chave de desempenho configurados para o seu caso de uso, como:

- LTV Incremental / Cliente
- Conversões / Cliente
- Cancelamentos de inscrição / Cliente

Cada cartão representa o KPI calculado ao longo de todo o intervalo de datas selecionado. Este é um valor do período completo, não uma média diária. Por exemplo, se você vê "LTV Incremental / Cliente = 3,192", isso reflete a performance ao longo de todo o período selecionado.

![Relatório de performance mostrando os cartões de resumo de KPI no lado esquerdo, incluindo métricas como LTV Incremental / Cliente, Conversões / Cliente e Cancelamentos de inscrição / Cliente.]({% image_buster /assets/img/decisioning_studio/reporting_performance_kpi_cards.png %})

## Gráfico de tendência de KPI

Use o gráfico para entender tendências ao longo do tempo, mudanças de performance e efeitos de sazonalidade ou timing. Use o cartão de KPI para entender o impacto geral ao longo de todo o período. O gráfico central mostra o mesmo KPI do cartão superior, mas calculado por dia. Cada ponto representa o valor do KPI daquele dia. Se você tiver a média móvel de 7 dias selecionada, cada ponto reflete uma média móvel, que suaviza a volatilidade diária.

![Relatório de performance mostrando o gráfico de tendência central intitulado LTV Incremental / Cliente, com linhas para Decisioning Studio e Business as Usual BAU Group plotadas ao longo do tempo.]({% image_buster /assets/img/decisioning_studio/reporting_performance_trend_chart.png %})

O gráfico e o cartão de KPI são projetados para mostrar coisas diferentes. O gráfico mostra a performance diária ("Como foi a performance a cada dia?"). O cartão de KPI mostra a performance do período completo ("Como foi a performance ao longo de todo o período?"). Para métricas de taxa, eles respondem a perguntas diferentes.

Considere o seguinte exemplo com estas taxas de conversão:

- Dia 1: 10 conversões de 100 clientes = 10%
- Dia 2: 2 conversões de 10 clientes = 20%

O gráfico mostra ambos. O cartão de KPI recalcula combinando os dois dias (12 conversões / 110 clientes = 10,9%), não uma média de 10% e 20%.

## Gráfico de uplift

O gráfico de uplift mostra a diferença percentual entre seus grupos de comparação. Ele é calculado como: **(Grupo Primário - Grupo de Comparação) / Grupo de Comparação**. Isso é calculado dinamicamente com base nos valores do gráfico de KPI.

![Relatório de performance mostrando o gráfico de porcentagem de Uplift no lado direito, exibindo a diferença percentual entre o Decisioning Studio e o grupo BAU ao longo do tempo.]({% image_buster /assets/img/decisioning_studio/reporting_performance_uplift.png %})

{% alert important %}
O uplift não é armazenado. Ele é calculado a partir dos resultados de KPI. Se o uplift mudar, é porque o KPI subjacente mudou.
{% endalert %}

## Tabela agregada

A tabela na parte inferior do relatório mostra os totais brutos ao longo do intervalo de datas selecionado, como:

- LTV incremental total
- Total de clientes
- Valor de KPI derivado

Esta seção reforça a relação entre as diferentes visualizações:

- O cartão de KPI é um cálculo em nível de período.
- O gráfico é um cálculo diário.
- A tabela mostra os totais subjacentes que compõem o KPI.

![Relatório de performance mostrando a tabela agregada na parte inferior, com colunas para Grupo, LTV Incremental, Cliente e LTV Incremental / Cliente para cada grupo de comparação.]({% image_buster /assets/img/decisioning_studio/reporting_performance_aggregate_table.png %})

## Árvore de drivers

A árvore de drivers decompõe um KPI em seus componentes. Por exemplo, LTV Incremental / Cliente pode se decompor em:

- Conversões / Cliente
- Receita por Conversão

![Relatório de performance na visualização de Árvore de Drivers, mostrando um diagrama hierárquico que decompõe KPIs como LTV Incremental / Cliente em componentes como Conversões / Cliente e Cliques / Cliente.]({% image_buster /assets/img/decisioning_studio/reporting_performance_driver_tree.png %})

As árvores de drivers usam as mesmas definições de KPI do restante do dashboard e não introduzem nenhuma matemática nova. Elas ajudam a explicar o que está impulsionando a performance. Se uma definição de KPI mudar, gráficos, cartões, uplift e árvores de drivers são todos atualizados juntos.

## Perguntas frequentes

### Como os segmentos funcionam?

Os segmentos permitem que você analise a performance por grupos definidos, como níveis de engajamento, características do cliente, tipo de dispositivo ou outras features configuradas.

A associação a segmentos é configurada de forma personalizada para o seu caso de uso e calculada diariamente. Isso significa que o segmento passado de um cliente reflete quem ele era naquele dia. Se o comportamento dele mudar depois, os dias históricos permanecem inalterados. Isso preserva a precisão histórica e evita que os relatórios mudem retroativamente.

### O relatório de performance para agentes Go versus Pro é diferente?

Os KPIs para casos de uso Go são definidos automaticamente e padronizados, já que todos os casos de uso Go têm a mesma métrica-alvo: cliques únicos.

### Por que não consigo selecionar certas datas recentes?

O seletor de datas pode não permitir a seleção dos dias mais recentes. Isso é intencional. Os relatórios podem aplicar atrasos de ativação, atrasos de disponibilidade de dados ou datas explicitamente excluídas. Essas proteções evitam que dados incompletos ou instáveis apareçam nos seus resultados.

Se você precisar de esclarecimentos sobre o período do seu relatório ou regras de disponibilidade de dados, entre em contato com o seu AI Success Manager para obter a configuração específica do seu caso de uso.

### Qual é a diferença entre KPIs de "volume" e de "taxa"?

Os KPIs geralmente se dividem em duas categorias:

- **Métricas de volume** (como total de conversões, receita total ou total de cliques) respondem: "Quanto aconteceu?"
- **Métricas de taxa** (como taxa de conversão, receita por usuário ou taxa de cliques) respondem: "Com que eficiência aconteceu?"

Volume e taxa contam histórias diferentes. Uma campanha pode gerar maior volume, mas menor eficiência, ou vice-versa. Ao interpretar os resultados, sempre confirme qual tipo de KPI você está analisando.

### O que significa "único" (ou "distinto")?

Quando uma métrica é definida como "única", os indivíduos são deduplicados usando um identificador específico (normalmente cliente). Cada pessoa é contada uma vez por dia.

"Único por dia" é diferente de "único ao longo de todo o intervalo de datas." Se você vir contagens únicas diárias somadas ao longo de vários dias, o mesmo indivíduo pode aparecer mais de uma vez (uma vez por dia em que interagiu). Isso é intencional.

Se você precisar entender como a unicidade foi definida na sua configuração, entre em contato com o seu AI Success Manager.

### Por que este relatório pode diferir de outro sistema?

Se o seu relatório de Performance não corresponder a outro dashboard (como um ESP, ferramenta de análise de dados ou relatório interno de BI), isso não significa necessariamente que algo está errado. Sistemas diferentes frequentemente aplicam definições e regras diferentes. Razões comuns incluem:

- **Regras de atribuição:** Algumas métricas aplicam lógica de atribuição, o que significa que apenas a atividade que atende a critérios definidos é contada. Se outro sistema conta toda a atividade sem lógica de atribuição, os totais podem diferir.
- **Filtragem de engajamento de máquina e bot:** Engajamento conhecido gerado por máquinas ou bots (como varreduras de segurança automatizadas ou cliques não humanos) é filtrado para garantir que a performance reflita o comportamento humano real. Algumas plataformas incluem essas interações em seus totais.
- **Definições diferentes de "único":** Neste relatório, a unicidade é normalmente aplicada por dia. Outro sistema pode calcular a unicidade ao longo de todo o período de uma campanha. Essas são perguntas de negócios diferentes e produzem números diferentes.
- **Intervalo de datas e regras de disponibilidade de dados:** Os relatórios podem aplicar atrasos de ativação, atrasos de disponibilidade de dados ou datas excluídas. Outro sistema pode incluir dados muito recentes ou incompletos, criando divergências temporárias.
- **Diferenças de volume versus taxa:** Um sistema pode mostrar o volume total (como total de conversões), enquanto outro mostra uma taxa (como conversões por cliente). Sempre confirme que você está comparando o mesmo tipo de métrica.

### Por que o número no gráfico não corresponde ao cartão de resumo?

O gráfico e o cartão de resumo respondem a perguntas diferentes:

- **Gráfico:** Mostra a performance diária. Cada ponto reflete o KPI calculado para aquele dia individual.
- **Cartão de resumo:** Mostra a performance do período completo. Ele recalcula o KPI ao longo de todo o intervalo de datas selecionado.

Use o gráfico para entender a volatilidade do dia a dia, efeitos de timing e mudanças de performance ao longo do tempo. Use o cartão de resumo para entender o impacto geral ao longo do período.

Considere este exemplo com a seguinte taxa de conversão:

- Dia 1: 10 conversões de 100 clientes = 10%
- Dia 2: 2 conversões de 10 clientes = 20%

O gráfico mostra 10% no Dia 1 e 20% no Dia 2. O cartão de resumo calcula a performance combinando os dois dias: 12 conversões totais de 110 clientes = 10,9%. Ele não faz a média de 10% e 20%.

### Qual é a abordagem recomendada para contagens "únicas"?

Ao medir comportamento único (como clicadores ou conversores únicos), a unicidade é aplicada por dia. Por exemplo:

- Dia 1: Clientes que clicaram: A, B, C = 3 únicos
- Dia 2: Clientes que clicaram: B, C, D = 3 únicos

O gráfico mostra 3 no Dia 1 e 3 no Dia 2. Ao longo dos dois dias, você pode ver 3 + 3 = 6. Os clientes B e C são contados uma vez por dia, o que é intencional.

Essa configuração responde: "Quantos engajamentos únicos de clientes aconteceram ao longo dos dias?" Ela não responde: "Quantos clientes individuais interagiram pelo menos uma vez ao longo de todo o período?"

Se o seu objetivo é unicidade em nível de período (indivíduos únicos ao longo de toda a campanha ou trimestre), essa é uma abordagem de modelagem diferente. Entre em contato com o seu AI Success Manager para orientação sobre como projetar isso.