---
nav_title: Sincronizar e Excluir Dados do Catálogo
article_title: Sincronizar e Excluir Dados do Catálogo
page_order: 4
page_type: reference
description: "Esta página fornece uma visão geral de como sincronizar os dados do catálogo."

---

# Sincronizar e excluir dados do catálogo

> Esta página aborda como sincronizar os dados do catálogo.
 
## Etapa 1: Criar um novo catálogo

Antes de criar uma nova integração de ingestão de dados na nuvem (CDI) para [catálogos]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/), você precisa criar um novo catálogo ou identificar um catálogo existente que deseja usar para a integração. Existem algumas maneiras de criar um novo catálogo e qualquer uma delas funcionará para a integração CDI:
- Faça upload de um [CSV]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#method-1-upload-csv)
- Crie um catálogo no [dashboard da Braze]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#method-2-create-in-browser) ou durante a configuração do CDI.
- Crie um catálogo usando o [endpoint de criação de catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)

Quaisquer alterações no esquema do catálogo (por exemplo, adicionar novos campos ou alterar o tipo de campo) devem ser feitas através do dashboard do catálogo antes que os dados atualizados sejam sincronizados através do CDI. Recomendamos fazer essas atualizações quando a sincronização estiver pausada ou não programada para ser executada para evitar conflitos entre os dados do seu data warehouse e o esquema no Braze.

## Etapa 2: Integrar a Ingestão de Dados na Nuvem com dados de catálogo
A configuração para uma sincronização de catálogo segue de perto o processo para [integrações CDI de dados do usuário]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations#product-setup). 

{% tabs %}
{% tab Snowflake %}

1. Configure uma tabela de origem no Snowflake. Você pode usar os nomes no exemplo a seguir ou escolher seus próprios nomes de banco de dados, esquema e tabela. Você também pode usar uma visão ou uma visão materializada em vez de uma tabela.
  ```json
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
         UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
         --ID of the catalog item to be created or updated
         ID VARCHAR(16777216) NOT NULL,
         --Catalog fields and values that should be added or updated
         PAYLOAD VARCHAR(16777216) NOT NULL,
         --The catalog item associated with this ID should be deleted
         DELETED BOOLEAN
    );
    ```
2. Set up a role, warehouse, and user and grant proper permissions. If you already have credentials from an existing sync, you can reuse them, but make sure to extend access to the catalog source table.
    ```json
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. If your Snowflake account has network policies, allowlist the Braze IPs so the CDI service can connect. For a list of IPs, refer to the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).
4. In the Braze dashboard, navigate to **Technology Partners** > **Snowflake**, and create a new sync.
5. Enter connection details (or reuse existing credentials) and the source table.
6. Proceed to step 2 of the setup flow, select the “Catalogs” sync type, and input the integration name and schedule. Note that the name of the integration should **exactly match** the name of the catalog you previously created.
7. Choose a sync frequency and proceed to the next step.
8. Add the public key displayed on the dashboard to the user you created for Braze to connect to Snowflake. To complete this step, you will need someone with `SECURITYADMIN` access or higher in Snowflake. 
9. Select **Test Connection** so that everything works as expected. 
10. Save the sync, and use the synced catalog data for all your personalization use cases. 
{% endtab %}
{% tab Redshift %}

1. Set up a source table in Redshift. You can use the names in the following example or choose your own database, schema, and table names. You may also use a view or a materialized view instead of a table.
    ```json
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
       updated_at timestamptz default sysdate not null,
       --ID of the catalog item to be created or updated
       id varchar not null,
       --Catalog fields and values that should be added or updated
       payload varchar(max),
       --The catalog item associated with this ID should be deleted
       deleted boolean
    )
    ```
2. Set up a user and grant proper permissions. If you already have credentials from an existing sync, you can reuse them, but make sure to extend access to the catalog source table.
    {% raw %}
    ```json 
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE CATALOGS_SYNC TO braze_user;
    ```
    {% endraw %}
3. If you have a firewall or other network policies, you must give Braze network access to your Redshift instance. Allow access from the below IPs corresponding to your Braze dashboard’s region. For a list of IPs, refer to the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab BigQuery %}

1. Optionally, set up a new project or dataset to hold your source table. 

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Crie uma ou mais tabelas para usar na sua integração CDI com os seguintes campos:

```json
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  id STRING,
  payload JSON,
  deleted BOOLEAN
);
```

| NOME DO CAMPO | TIPO | MODO |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | OBRIGATÓRIO |
| PAYLOAD | JSON | OBRIGATÓRIO |
| ID | STRING | OBRIGATÓRIO |
| DELETED | BOOLEAN | OPCIONAL |

{:start="2"}

2. Configurar um usuário e conceder as permissões adequadas. Se você já tiver credenciais de uma sincronização existente, poderá reutilizá-las, mas certifique-se de estender o acesso à tabela de origem do catálogo.
A conta de serviço deve ter as permissões abaixo:
- Usuário de conexão do BigQuery: Isso permitirá que a Braze faça conexões.
- Usuário do BigQuery: Isso fornecerá acesso à Braze para executar consultas, ler metadados do conjunto de dados e listar tabelas.
- Visualizador de dados do BigQuery: Isso fornecerá acesso à Braze para visualizar conjuntos de dados e seus conteúdos.
- Usuário do BigQuery Job: Isso fornecerá acesso ao Braze para executar trabalhos<br><br>Depois de criar a conta de serviço e conceder permissões, gere uma chave JSON. Para saber mais, consulte [Criar e excluir chaves](https://cloud.google.com/iam/docs/keys-create-delete). Você atualizará isso no dashboard do Braze mais tarde.

{:start="3"}
3\. Se você tiver políticas de rede em vigor, deve conceder acesso à rede da Braze à sua instância do BigQuery. Para obter uma lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Databricks %}

1. Configurar uma tabela de origem no Databricks. Você pode usar os nomes no exemplo a seguir ou escolher seu catálogo, esquema e nomes de tabelas. Você também pode usar uma visão ou uma visão materializada em vez de uma tabela.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

```json
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  id STRING,
  deleted BOOLEAN,
  payload STRING, STRUCT, or MAP
);
```

| NOME DO CAMPO | TIPO | MODO |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | OBRIGATÓRIO |
| PAYLOAD | STRING, STRUCT ou MAP | OBRIGATÓRIO |
| ID | STRING | OBRIGATÓRIO |
| DELETED | BOOLEAN | NULLABLE |

{:start="2"}

2. Crie um token de acesso pessoal no seu espaço de trabalho do Databricks.

- a. Selecione seu nome de usuário do Databricks e, em seguida, selecione **Configurações do usuário** no menu suspenso.
- b. Na guia **Tokens de acesso**, selecione **Gerar novo token**.
- c. Insira um comentário que o ajude a identificar esse token, como "CDI Braze". 
- d. Altere o tempo de vida do token para nenhum tempo de vida deixando a caixa **Lifetime (days)** em branco. Selecione **Gerar**.
- e. Copie o token exibido e, em seguida, selecione **Concluído**. 
- f. Mantenha o token em um local seguro até que você precise inseri-lo durante a etapa de criação de credenciais no dashboard do Braze.

{:start="3"}
3\. Se você tiver políticas de rede em vigor, deve conceder acesso à rede da Braze à sua instância do Databricks. Para uma lista de IPs, consulte a página [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Microsoft Fabric %}

Crie uma ou mais tabelas para usar em sua integração CDI com os seguintes campos:

```json
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  ID VARCHAR NOT NULL,
  DELETED BIT
)
GO
```

{:start="2"}

2. Configure uma entidade de serviço e conceda as permissões adequadas. Se você já possui credenciais de uma sincronização existente, pode reutilizá-las—apenas certifique-se de estender o acesso à tabela de origem do catálogo. Para saber mais sobre como criar uma nova entidade de serviço e credenciais, consulte a página [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views). 

{:start="3"}
3\. Se você tiver políticas de rede em vigor, deverá conceder à Braze acesso de rede à sua instância do Microsoft Fabric. Para uma lista de IPs, consulte a [Ingestão de Dados na Nuvem]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% endtabs %}

## Como a integração funciona

Cada vez que a sincronização é executada, a Braze puxará todas as linhas onde `UPDATED_AT` está após o último carimbo de data/hora sincronizado. Recomendamos criar uma visualização no seu data warehouse a partir dos dados do seu catálogo para configurar uma tabela de origem que será totalmente atualizada cada vez que uma sincronização for executada. Com visualizações, você não precisará reescrever a consulta cada vez.

Por exemplo, se você tiver uma tabela de dados de produtos (`product_catalog_1`) com `product_id` e três atributos adicionais, você poderá sincronizar a visualização abaixo:

{% tabs %}
{% tab Snowflake %}
```json
CREATE VIEW BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS 
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    product_id as id,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    )as PAYLOAD FROM "product_catalog_1";
```
{% endtab %}
{% tab Redshift %}
```json
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    Product_id as id,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    ) as PAYLOAD FROM "product_catalog_1";
```
{% endtab %}
{% tab BigQuery %}
```json
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    product_id as ID,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD 
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);
```
{% endtab %}
{% tab Databricks %}
```json
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    product_id as ID,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD 
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);
```
{% endtab %}
{% tab Microsoft Fabric %}
```json
CREATE VIEW [braze].[user_update_example]
AS SELECT 
    id as ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[product_catalog] ;
```
{% endtab %}
{% endtabs %}

- Os dados obtidos da integração serão usados para criar ou atualizar itens no catálogo alvo com base no `id` fornecido.
- Se DELETED estiver definido como `true`, o item do catálogo correspondente será excluído.
- A sincronização não consumirá pontos de dados, mas todos os dados sincronizados contarão para o uso total do seu catálogo; esse uso é medido com base no total de dados armazenados, então você não precisa se preocupar em sincronizar apenas os dados alterados.
