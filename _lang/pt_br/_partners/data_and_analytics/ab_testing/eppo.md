---
nav_title: Eppo
article_title: Eppo
description: "Aprenda como integrar Eppo com Braze."
alias: /partners/eppo/
page_type: partner
search_tag: Partner
---

# Eppo

> [Eppo](https://www.geteppo.com/) é uma plataforma de experimentação de próxima geração que permite que as equipes realizem testes A/B, gerenciem recursos em grande escala e aproveitem insights impulsionados por IA para a tomada de decisões baseada em dados.

*Esta integração é mantida pela Eppo.*

A integração entre Braze e Eppo permite que você configure testes A/B no Braze e analise os resultados no Eppo para descobrir insights e vincular o desempenho das mensagens a métricas de negócios de longo prazo, como receita ou retenção.

## Pré-requisitos

| Requisito                        | Descrição                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------|
| Conta Eppo                       | Uma conta Eppo é necessária para aproveitar esta parceria.                   |
| Currents ou Compartilhamento de Dados Snowflake | Currents ou Compartilhamento de Dados Snowflake é necessário para que o Eppo analise os dados do experimento. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Configure Currents ou Compartilhamento de Dados Snowflake no Braze

O Eppo analisa experimentos diretamente no seu data warehouse. Para ativar a integração, os dados de engajamento de mensagens do Braze devem estar disponíveis no warehouse conectado ao Eppo. Você pode exportar dados de campanha do Braze usando Currents ou acessar dados do Braze na sua instância Snowflake usando [Compartilhamento de Dados Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake).

### Etapa 2: Configure seu experimento em uma campanha ou Canvas do Braze

Você pode usar recursos nativos de testes A/B em suas campanhas e Canvases. Para saber mais, veja [Testes Multivariantes e A/B](https://www.braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing#what-are-multivariate-and-ab-testing).

### Etapa 3: Configure o Eppo para medir experimentos do Braze

Para realizar experimentos usando dados do Braze no Eppo, crie [tabelas de atribuições](https://docs.geteppo.com/data-management/definitions/assignment-sql/) no seu warehouse com base em dados de eventos de mensagens em nível de usuário exportados do Braze. Tabelas separadas são recomendadas para experimentos de Canvas e campanha porque dependem de metadados diferentes.

{% tabs local %}
{% tab canvas experiments %}
Para experimentos de Canvas, as atribuições podem ser criadas de duas maneiras:

- No nível de entrada do canva (`users.canvas.Entry`)
- Ou em uma etapa do experimento do canva (`users.canvas.experimentstep.SplitEntry`)

Nesses casos, campos como `canvas_name`, `experiment_step_id`, `canvas_variation_name` e `experiment_split_id` são usados para definir o nome e a variação do experimento.

{% endtab %}

{% tab campaign experiments %}
Para experimentos de campanha, use eventos de envio (como push, e-mail, SMS) para determinar quando um usuário entrou no experimento. `campaign_name`, `message_variation_name` e `time` são usados para preencher a tabela de atribuição.

{% endtab %}
{% endtabs %}

Para rastrear métricas específicas de mensagens (como cliques ou aberturas), inclua uma **Entidade Secundária** criando um `combined_id` que junta o ID do usuário com o nome da campanha ou do canva. Esta `combined_id` também é usada em suas tabelas de fatos para alinhar métricas com o experimento e a variação corretos.

Eppo usa essas atribuições e tabelas de fatos para analisar resultados, e é recomendável configurar um **Protocolo** no Eppo para padronizar a configuração de experimentos futuros. Para saber mais, consulte [a documentação do Eppo](https://docs.geteppo.com/guides/marketing/integrating-with-braze/).

## Suporte

Para perguntas sobre como configurar Braze Currents, compartilhamento de dados do Snowflake ou configurar campanhas multivariantes, entre em contato com seu gerente de sucesso do cliente da Braze.

Para assistência na configuração do Eppo para medir experimentos da Braze, entre em contato com a equipe de suporte do Eppo.
