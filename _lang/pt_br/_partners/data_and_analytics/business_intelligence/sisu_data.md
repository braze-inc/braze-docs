---
nav_title: Dados do Sisu
article_title: Dados do Sisu
description: "Este artigo de referência descreve a parceria entre o Braze e a Sisu Data, líder em inteligência de decisão na nuvem, que permite que você entenda, em todas as campanhas ou em nível de campanha, por que as métricas estão mudando e o que gera os melhores resultados."
alias: /partners/sisu_data
page_type: partner
search_tag: Partner
---

# Dados do Sisu

> [A Sisu Data](https://sisudata.com/) é líder em inteligência de decisão na nuvem que usa machine learning para decompor automaticamente a performance das métricas e fornecer insights rápidos, abrangentes e práticos.

A integração entre o Sisu Data e o Braze permite que você entenda, em todas as campanhas ou em nível de campanha, por que as métricas (por exemplo, taxa de abertura, taxa de cliques, taxa de conversão etc.) estão mudando e o que gera os melhores resultados. Depois que esses segmentos são identificados, os usuários da Braze podem materializar os resultados em seu data warehouse ou enviá-los diretamente do Sisu para a Braze para redirecionar e reengajar os usuários.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Sisu | É necessário ter uma conta [no Sisu](https://sisudata.com/) para aproveitar essa parceria. |
| Armazém na nuvem | Essa integração pressupõe que seus dados da Braze estejam armazenados em um data warehouse na nuvem (por exemplo, Snowflake, BigQuery). Para simplificar esse processo de integração, recomendamos a utilização da funcionalidade nativa do Braze via [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Preparar um conjunto de dados

O conjunto de dados deve indicar o KPI que você deseja que o Sisu analise. Por exemplo, se você quiser entender melhor por que as taxas de conversão caíram semana após semana, o registro de alcance deve representar uma conversão semanal. As colunas no conjunto de dados devem ser os possíveis motivos pelos quais a taxa de conversão pode cair.

### Etapa 2: Criar uma métrica  

Depois que o conjunto de dados estiver preparado, você precisará criar uma métrica que faça referência a uma coluna agregada. Como um conjunto de dados pode alimentar várias métricas, o usuário também pode fazer a curadoria de um conjunto de dimensões que devem ou não fazer parte de todas as análises por padrão. Note que os usuários sempre podem continuar a fazer a curadoria no nível da análise.

![]({% image_buster /assets/img/sisudata/metric_creation.png %})

### Etapa 3: Criar uma análise  

Há diferentes análises que os usuários podem criar no Sisu, dependendo do caso de uso. Uma das análises mais comuns é uma análise período a período para entender quais segmentos sofreram mais alterações. Os usuários podem decidir se querem analisar períodos de tempo diários, semanais, mensais ou personalizados, selecionando os períodos de tempo relativos.

Por exemplo, o usuário pode criar uma análise da taxa de conversão mês a mês para um determinado grupo de anúncios e canal de engajamento e entender os principais fatores positivos e negativos.

{% tabs %}
{% tab Principais fatores positivos %}

![]({% image_buster /assets/img/sisudata/kda_result_positive.png %})

{% endtab %}
{% tab Principais fatores negativos %}

![]({% image_buster /assets/img/sisudata/kda_result_negative.png %})

{% endtab %}
{% endtabs %}

A partir daí, você pode se concentrar nos coortes com os quais eles podem querer se engajar ou modificar as campanhas. Por exemplo, a Sisu identificou automaticamente que as notificações por push enviadas às terças-feiras e os e-mails enviados em grandes volumes afetam gravemente a taxa de conversão.

![]({% image_buster /assets/img/sisudata/segment.png %})

### Etapa 4: gravar de volta os resultados no data warehouse

Os usuários podem extrair os resultados do Sisu usando [a API do Sisu](https://docs.sisudata.com/docs/api/#tag/AnalysesService/operation/AnalysesService_AnalysisRunResults) e materializar os segmentos em um data warehouse. Os clientes do Snowflake podem ativar esses segmentos no Braze por meio da [ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/).

Para outros data warehouses, os usuários podem aproveitar uma solução de ativação existente ou entrar em contato com a Sisu para obter ajuda adicional.

## Suporte

Em caso de dúvidas sobre a integração, entre em contato com a Sisu pelo e-mail partners@sisudata.com.

