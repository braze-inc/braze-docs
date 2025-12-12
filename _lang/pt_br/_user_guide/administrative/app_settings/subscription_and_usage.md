---
nav_title: Faturamento
article_title: Faturamento
alias: /subscription_and_usage/
page_order: 25
page_type: reference
description: "Este artigo de referência aborda a página Billing (Faturamento), onde você pode monitorar e verificar seu consumo de dados."
tool: Dashboard
search_rank: 5
---

# Faturamento

> Saiba como usar a página **Faturamento** para monitorar e verificar seu consumo de dados em espaços de trabalho, aplicativos e fontes de eventos. Este artigo aborda as diferentes seções da página e as informações que elas podem fornecer.

Para navegar até a página **Faturamento**, vá para **Configurações** > **Faturamento**.

A página **Faturamento** inclui as seguintes guias:

- [Assinaturas e uso](#subscriptions-and-usage)
- [Eventos e atributos mais usados por aplicativo](#most-used-events-and-attributes-by-app)
- [Uso total de pontos de dados](#total-data-points-dashboard)

## Assinaturas e uso

A guia **Subscriptions and Usage (Assinaturas e uso** ) inclui gráficos de uso e os detalhes do seu contrato.

### Gráficos de uso

Aqui, você encontrará gráficos de uso que se aplicam aos seus espaços de trabalho. Você pode descobrir que seu próprio painel mostra diferentes métricas de uso com base nos produtos que você comprou. 

\![Gráfico de uso mostrando os visitantes únicos mensais]({% image_buster /assets/img/subscription_and_billing4.png %}){: style="max-width:90%;"}

Esses gráficos podem mostrar usuários ativos mensais, visitantes únicos mensais e envios de e-mail. Gráficos de uso como esses são particularmente úteis ao tentar orçar o uso e obter uma compreensão mais profunda de quais espaços de trabalho contribuem para o uso geral.

### Detalhes do contrato

Os detalhes do contrato listam as datas de início e término de seu contrato atual com a Braze.

## Eventos e atributos mais usados por aplicativo

Em **Most Used Events and Attributes By App (Eventos e atributos mais usados por aplicativo**), você pode verificar os drivers de seu atributo e o uso de pontos de dados de eventos personalizados. 

\![Eventos e atributos mais usados por aplicativo]({% image_buster /assets/img/most_used_events_attributes_time.png %})

Para cada aplicativo, você pode selecionar **Ver detalhamento** para visualizar uma contagem estimada de cada atributo personalizado, atributo de perfil e evento personalizado específico para o período de tempo selecionado, bem como a porcentagem das atualizações de atributos e eventos desse aplicativo que foram geradas por esse atributo ou evento. 

Guia Detalhamento de eventos e atributos mais usados por aplicativo]({% image_buster /assets/img/most_used_events_attributes_2.png %}){: style="max-width:60%"}

Detalhamentos de dados como esses podem ajudá-lo a entender quais pontos de dados específicos estão consumindo grandes porcentagens de sua cota. Recomendamos que você monitore essas informações periodicamente para se certificar de que não está gastando pontos de dados de forma acidental e desnecessária. Seu gerente de sucesso do cliente pode fornecer orientação para aproveitar ao máximo seu plano atual ou oferecer opções para maior flexibilidade. 

## Painel de controle do total de pontos de dados

A guia **Total Data Points Usage (Uso total de pontos de dados** ) oferece uma visão detalhada do uso de seus pontos de dados. É possível visualizar todos os dados dessa seção agregados por semanas ou meses.

\![Filtragem do uso de pontos de dados por semanas]({% image_buster /assets/img/subscription_and_billing2.png %})

### Detalhes do contrato

Aqui, você encontrará informações sobre quando seu contrato atual do Braze começa e termina, bem como os pontos de dados alocados e uma soma de todos os pontos de dados que foram usados até o momento em seu contrato atual.

Os campos dessa seção são definidos da seguinte forma:

- **Tipo de contrato:** Estrutura de prazo de faturamento, anual ou plurianual.
- **Data de início e término do contrato:** Data de início e término de todo o contrato.
- **Pontos de dados alocados:** A quantidade de pontos de dados alocados no contrato por período de faturamento.
- **Uso do ponto de dados do contrato:** Um total cumulativo de todos os pontos de dados registrados durante a vida útil do contrato e não é redefinido no próximo período de faturamento.

\![Seção Detalhes do contrato da guia Uso total de pontos de dados]({% image_buster /assets/img/contract_details.png %})

### Dados de faturamento da empresa

#### Uso total de pontos de dados no nível do aplicativo

Esse gráfico mostra o uso de pontos de dados em todos os aplicativos.

\![App Level Total Data Point Usage mostra os pontos de dados usados para cada aplicativo.]({% image_buster /assets/img/app_level_total.png %})

Selecione um dos totais para visualizar a tabela **Data Point Usage Over Time (Uso de pontos de dados ao longo do tempo** ), que mostra os totais de pontos de dados semanais para cada espaço de trabalho.  As linhas que têm uma coluna **App Name** em branco representam pontos de dados que não estão associados a nenhum aplicativo (como pontos de dados usados em solicitações que não especificam um `app_id`).

Uso de pontos de dados ao longo do tempo mostrando o total de pontos de dados semanais para dois espaços de trabalho.]({% image_buster /assets/img/data_point_usage_time.png %})

#### Uso de pontos de dados do espaço de trabalho

Esse gráfico permite que você avalie o uso total de pontos de dados de uma empresa por espaço de trabalho. Esse gráfico permite que você avalie como cada espaço de trabalho está contribuindo para o uso de pontos de dados da empresa.

Gráfico de uso de pontos de dados do espaço de trabalho para dois espaços de trabalho]({% image_buster /assets/img/appgroup_datapoint_usage.png %}){: style="max-width:90%;"}

#### Uso de pontos de dados do ciclo de faturamento por fonte de evento

Esse gráfico permite que você visualize como o uso de pontos de dados está distribuído em diferentes fontes de eventos, como diferentes atributos de API, eventos personalizados e sessões.

Uso de pontos de dados do ciclo de faturamento por fonte de eventos exibindo a alocação de pontos de dados entre diferentes fontes de eventos.]({% image_buster /assets/img/event_source_stats.png %})

#### Uso de pontos de dados ao longo do tempo

Esse gráfico permite que você veja rapidamente o uso total de pontos de dados em comparação com a quantidade de pontos de dados alocados.

Uso de pontos de dados ao longo do tempo, contrastando os pontos de dados alocados no ciclo de faturamento atual com o total em execução]({% image_buster /assets/img/company_data_point_usage_time.png %}){: style="max-width:90%;"}

