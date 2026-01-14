---
nav_title: Kubit
article_title: Kubit
description: "Este artigo de referência descreve a parceria entre o Braze e o Kubit, uma plataforma de análise de dados sem código e de autoatendimento que fornece insights instantâneos sobre o produto, permitindo a importação de coortes de usuários do Kubit e seu direcionamento para o envio de mensagens do Braze."
alias: /partners/kubit/
page_type: partner
search_tag: Partner

---

# Kubit

> [A Kubit](https://kubit.ai/) é uma plataforma de análise de dados sem código e de autoatendimento que oferece insights instantâneos sobre o produto. 

A integração do Braze e do Kubit permite a [importação de coortes de usuários do Kubit]({{site.baseurl}}/partners/data_and_analytics/cohort_import/kubit/) e seu direcionamento para o envio de mensagens do Braze. Além disso, com o uso do [compartilhamento seguro de dados Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/), é possível integrar a campanha bruta e os dados de impressão do Braze com a análise de dados do produto Kubit para medir o impacto dessas campanhas em tempo real. Essa abordagem fornece insights sobre o ciclo de vida completo dos seus usuários sem exigir nenhum esforço de engenharia.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
|Conta corporativa do Kubit | É necessário ter uma conta empresarial do Kubit para usar a parceria. |
| Correspondência de IDs de usuário | Os dados de seus clientes no Kubit e no Braze devem ter IDs de usuário correspondentes nas duas plataformas. Isso também inclui UUIDs anônimos. Visite nossa [documentação]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android) para ler sobre como o Braze define IDs de usuário. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Analisando dados do Braze no Kubit

Aproveite o [compartilhamento seguro de dados do Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) para compartilhar seus dados brutos de campanha e impressões do Braze com o Kubit para incorporá-los à análise de dados de autoatendimento do Kubit, fornecendo uma visão completa do ciclo de vida dos usuários.

Para referência, aqui estão todos os [campos do Braze]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ed79384e6ac6a97fe3b3d9f76852b7c2) que estão disponíveis para serem incorporados à análise de dados do Kubit. Os detalhes dessa etapa são muito específicos para cada cliente e exigem configurações especiais. Fale com seu gerente de conta da Kubit ou com [support@kubit.ai](support@kubit.ai) para saber mais.