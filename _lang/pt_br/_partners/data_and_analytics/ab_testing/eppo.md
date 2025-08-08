---
nav_title: Eppo
article_title: Eppo
description: "Saiba como integrar o Eppo ao Braze."
alias: /partners/eppo/
page_type: partner
search_tag: Partner
---

# Eppo

> [A Eppo](https://www.geteppo.com/) é uma plataforma de experimentação de última geração que ativa as equipes para executar Testes A/B, gerenciar recursos em escala e aproveitar insights orientados por IA para a tomada de decisões orientadas por dados.

*Essa integração é mantida pela Eppo.*

A integração entre o Braze e o Eppo permite que você configure Testes A/B no Braze e analise os resultados no Eppo para descobrir insights e vincular o desempenho das mensagens a métricas comerciais de longo prazo, como receita ou retenção.

## Pré-requisitos

| Requisito                        | Descrição                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------|
| Conta Eppo                       | É necessário ter uma conta Eppo para aproveitar essa parceria.                   |
| Compartilhamento de dados Currents ou Snowflake | O compartilhamento de dados Currents ou Snowflake é necessário para que o Eppo analise os dados do experimento. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Configurar o compartilhamento de dados do Currents ou do Snowflake no Braze

O Eppo analisa experimentos diretamente em seu data warehouse. Para ativar a integração, os dados de engajamento com mensagens do Braze devem estar disponíveis no data warehouse conectado ao Eppo. Você pode exportar dados de campanha do Braze usando Currents ou acessar os dados do Braze em sua instância do Snowflake usando o [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake).

### Etapa 2: Configure seu experimento em uma campanha Braze ou Canva

Você pode usar os recursos nativos de Testes A/B em suas campanhas e Canvas. Para saber mais, consulte [Testes multivariantes e testes A/B](https://www.braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing#what-are-multivariate-and-ab-testing).

### Etapa 3: Configure o Eppo para medir experimentos com Braze

Para executar experimentos usando dados do Braze no Eppo, crie [tabelas de atribuições](https://docs.geteppo.com/data-management/definitions/assignment-sql/) em seu data warehouse com base nos dados de eventos de mensagens no nível do usuário exportados do Braze. Tabelas separadas são recomendadas para experimentos do Canva e da campanha porque elas dependem de metadados diferentes.

{% tabs local %}
{% tab experimentos do canva %}
Para experimentos do Canva, as atribuições podem ser criadas:

- No nível de entrada do Canva (`users.canvas.Entry`)
- Ou em uma etapa do experimento do canva (`users.canvas.experimentstep.SplitEntry`)

Nesses casos, campos como `canvas_name`, `experiment_step_id`, `canvas_variation_name` e `experiment_split_id` são usados para definir o nome e a variação do experimento.

{% endtab %}

{% tab experimentos de campanha %}
Para experimentos de campanha, use eventos de envio (como push, e-mail, SMS) para determinar quando um usuário entrou no experimento. `campaign_name` Os registros `message_variation_name`, `time` e são usados para preencher a tabela de atribuição.

{% endtab %}
{% endtabs %}

Para rastrear métricas específicas de mensagens (como cliques ou aberturas), inclua uma **Entidade Secundária** criando um `combined_id` que junte a ID do usuário com o nome da campanha ou do Canva. Esse `combined_id` também é usado em suas tabelas de fatos para alinhar as métricas com o experimento e a variação corretos.

O Eppo usa essas atribuições e tabelas de fatos para analisar os resultados, e é recomendável configurar um **protocolo** no Eppo para padronizar a configuração de experimentos futuros. Para saber mais, consulte [a documentação do Eppo](https://docs.geteppo.com/guides/marketing/integrating-with-braze/).

## Suporte

Em caso de dúvidas sobre a configuração do Braze Currents, do Snowflake Data Sharing ou da configuração de campanhas multivariantes, entre em contato com seu gerente de sucesso do cliente Braze.

Para obter assistência na configuração do Eppo para medir experimentos Braze, entre em contato com a equipe de suporte da Eppo.
