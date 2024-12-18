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

> Saiba como usar a página **Faturamento** para monitorar e verificar seu consumo de dados em espaços de trabalho, apps e fontes de eventos. Este artigo aborda as diferentes seções da página e as informações que elas podem fornecer.

Para navegar até a página **Faturamento**, acesse **Configurações** > **Faturamento**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar esta página selecionando o ícone da sua conta e, em seguida, selecionando **Inscrições e uso**.
{% endalert %}

A página **Faturamento** inclui as seguintes guias:

- [Inscrições e uso](#subscriptions-and-usage)
- [Eventos e atribuições mais usados por aplicativo](#most-used-events-and-attributes-by-app)
- [Total de uso de pontos de dados](#total-data-points-dashboard)

## Inscrições e uso

A guia **Inscrições e uso** inclui gráficos de uso e os detalhes de seu contrato.

### Gráficos de uso

Aqui, você encontrará gráficos de uso que se aplicam aos seus espaços de trabalho. Talvez você descubra que seu próprio dashboard mostra diferentes métricas de uso com base nos produtos que você comprou. 

![Gráfico de uso mostrando os visitantes únicos mensais][3]{: style="max-width:90%;"}

Esses gráficos podem mostrar usuários ativos mensais, visitantes únicos mensais e envios de e-mail. Gráficos de uso como esses são particularmente úteis ao tentar orçar o uso e obter uma compreensão mais profunda de quais espaços de trabalho contribuem para o uso geral.

### Informações do contrato

Os detalhes do contrato listam a data de início e de término de seu contrato atual com o Braze.

## Eventos e atribuições mais usados por aplicativo

Em **Most Used Events and Attributes By App (Eventos e atributos mais usados por aplicativo**), você pode verificar os drivers de seu atributo e o consumo de pontos de dados de eventos personalizados. 

![Eventos e atribuições mais usados por aplicativo][4]

Para cada app, você pode selecionar **Ver detalhamento** para visualizar uma contagem estimada de cada atributo personalizado específico, atributo de perfil e evento personalizado para o período de tempo selecionado, bem como a porcentagem das atualizações de atributo e evento desse app que foram impulsionadas por esse atributo ou evento. 

![Guia Detalhamento dos eventos e atributos mais usados por app][1]

Detalhamentos de dados como esses podem ajudá-lo a entender quais pontos de dados específicos estão ocupando grandes porcentagens de sua cota de dados. Recomendamos que você monitore essas informações periodicamente para se certificar de que não está gastando pontos de dados de maneiras acidentais e desnecessárias. Seu gerente de sucesso do cliente pode fornecer orientações para aproveitar ao máximo seu plano atual ou oferecer opções para maior flexibilidade. 

## Painel de controle do total de pontos de dados

A guia **Total Data Points Usage (Uso total de pontos de dados** ) fornece uma visão detalhada do seu consumo de pontos de dados. É possível visualizar todos os dados dessa seção agregados por semanas ou meses.

![Filtragem do uso de pontos de dados por semanas][2]

### Informações do contrato

Aqui, você encontrará informações sobre quando seu contrato atual do Braze começa e termina, bem como os pontos de dados alocados e uma soma de todos os pontos de dados que foram usados até o momento em seu contrato atual.

Os campos dessa seção são definidos da seguinte forma:

- **Tipo de contrato:** Estrutura de prazo de faturamento, anual ou plurianual.
- **Data de início e término do contrato:** Data de início e término de todo o contrato.
- **Pontos de dados alocados:** A quantidade de pontos de dados alocados no contrato por período de faturamento.
- **Uso do ponto de dados do contrato:** Um total cumulativo de todos os pontos de dados consumidos durante a vida útil do contrato e não é redefinido no próximo período de faturamento.

![Seção Detalhes do contrato da guia Uso total de pontos de dados][5]

### Dados de faturamento da empresa

#### Uso total de pontos de dados no nível do app

Este gráfico mostra o uso de pontos de dados em todos os apps.

![O uso total de pontos de dados no nível do aplicativo mostra os pontos de dados usados para cada aplicativo.][14]

Selecione um dos totais para visualizar a tabela **Uso de pontos de dados ao longo do tempo**, que mostra os totais de pontos de dados semanais para cada espaço de trabalho.  As linhas que têm uma coluna **App Name** em branco representam pontos de dados que não estão associados a nenhum app (como pontos de dados usados em solicitações que não especificam um `app_id`).

![Uso de pontos de dados ao longo do tempo mostrando o total de pontos de dados semanais para dois espaços de trabalho.][15]

#### Uso de pontos de dados do espaço de trabalho

Esse gráfico permite que você avalie o uso total de pontos de dados de uma empresa por espaço de trabalho. Esse gráfico lhe dá a capacidade de avaliar como cada espaço de trabalho está contribuindo para o uso de pontos de dados da empresa.

![Gráfico de uso de pontos de dados do espaço de trabalho para dois espaços de trabalho][7]{: style="max-width:90%;"}

#### Uso de pontos de dados do ciclo de faturamento por fonte de evento

Esse gráfico permite que você visualize como o uso de pontos de dados está distribuído em diferentes fontes de eventos, como diferentes atributos API, eventos personalizados e sessões.

![Billing Cycle Data Point Usage by Event Source (Uso de pontos de dados do ciclo de faturamento por fonte de eventos), que exibe a alocação de pontos de dados entre diferentes fontes de eventos.][13]

#### Uso de pontos de dados ao longo do tempo

Esse gráfico permite que você veja rapidamente o uso total de pontos de dados em relação à quantidade de pontos de dados que lhe foi atribuída.

![Uso de pontos de dados ao longo do tempo, contrastando os pontos de dados alocados no ciclo de faturamento atual com o total em execução][8]{: style="max-width:90%;"}

[1]: {% image_buster /assets/img/most_used_events_attributes_2.png %}
[2]: {% image_buster /assets/img/subscription_and_billing2.png %}
[3]: {% image_buster /assets/img/subscription_and_billing4.png %}
[4]: {% image_buster /assets/img/most_used_events_attributes_time.png %}
[5]: {% image_buster /assets/img/contract_details.png %}
[6]: {% image_buster /assets/img/current_billing_cycle.png %}
[7]: {% image_buster /assets/img/appgroup_datapoint_usage.png %}
[8]: {% image_buster /assets/img/company_data_point_usage_time.png %}
[9]: {% image_buster /assets/img/appgroup_drilldown.png %}
[10]: {% image_buster /assets/img/appgroup_level_datapoint_usage_bycategory.png %}
[11]: {% image_buster /assets/img/appgroup_level_usage_time.png %}
[12]: {% image_buster /assets/img/app_level_stats.png %}
[13]: {% image_buster /assets/img/event_source_stats.png %}
[14]: {% image_buster /assets/img/app_level_total.png %}
[15]: {% image_buster /assets/img/data_point_usage_time.png %}