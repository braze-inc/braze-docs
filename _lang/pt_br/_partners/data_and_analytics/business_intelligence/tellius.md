---
nav_title: Tellius
article_title: Tellius
alias: /partners/tellius/
description: "Este artigo de referência descreve a parceria entre o Braze e a Tellius, uma plataforma de inteligência de decisão e análise aumentada, permitindo que você aproveite os dados, sem depender de engenheiros de BI, para criar dashboards e gerar insights para tomar melhores decisões de marketing."
page_type: partner
search_tag: Partner

---

# Tellius

> [A Tellius](https://www.tellius.com/), uma plataforma de inteligência de decisão e análise aumentada, ativa a capacidade de responder a perguntas sobre seus dados usando a pesquisa em linguagem natural e se aprofundar para entender o "porquê" com insights orientados por IA.

A integração do Braze e da Tellius permite que os usuários aproveitem os dados, sem depender de engenheiros de BI, para criar dashboards e gerar insights para tomar melhores decisões de marketing. Essa integração exige que os dados do Braze sejam armazenados no Snowflake, onde o Tellius pode se conectar diretamente e fazer consultas com integração em modo ao vivo.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da Tellius | É necessário ter uma conta da Tellius para usar a parceria. Você pode começar sua jornada com a Tellius usando uma [avaliação gratuita](https://www.tellius.com/free-trial/)|
| Programa de compartilhamento de dados Snowflake | Para os clientes atuais do Snowflake, entre em contato com seu representante Braze sobre o programa de compartilhamento de dados do Snowflake para canalizar seus dados do Braze para sua instância do Snowflake.|
| Conta de leitor do Snowflake | Para clientes que não são do Snowflake, entre em contato com seu representante da Braze para se informar sobre a possibilidade de obter uma conta de leitor do Snowflake para acessar seus dados da Braze.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Obter acesso ao Braze por meio do Snowflake

A Braze armazena dados granulares de clientes no Snowflake. Você pode aproveitar seus dados do Braze para gerar insights por meio do programa de compartilhamento de dados do Snowflake do Braze ou obtendo uma conta de leitor do Snowflake. 

Siga a [integração do Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) para fazer a configuração. 

### Etapa 2: conecte a Tellius aos dados da Braze no Snowflake

Conecte a Tellius aos dados da Braze no Snowflake por meio de um dos seguintes métodos:

- Acesso direto: Para carregar dados na Tellius, siga as etapas de como [carregar conjuntos de dados](https://help.tellius.com/article/jn6o59d5gk-load-datasets).
- Acesso OAuth: Para obter acesso OAuth ao Snowflake, siga as etapas da [autenticação por OAuth](https://help.tellius.com/article/11517w63b6-oauth-authentication-for-snowflake).

### Etapa 3: Criar Business View no Tellius a partir de dados carregados

Para começar a usar a pesquisa em linguagem natural e os insights automatizados, crie um [Business View](https://help.tellius.com/article/hy9yvh5tom-create-business-view) e selecione conjuntos de dados de sua conexão com o Snowflake.

### Etapa 4: obtenha o máximo de valor de seus dados usando a Tellius

Na Tellius, há uma interface guiada para mostrar a você os recursos da plataforma. Para perguntas adicionais e orientações, consulte a [base de conhecimento](https://help.tellius.com/) completa.