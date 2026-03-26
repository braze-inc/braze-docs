---
nav_title: Sincronizar e excluir dados do catálogo
article_title: Sincronizar e Excluir Dados do Catálogo
page_order: 4
page_type: reference
description: "Esta página fornece uma visão geral de como sincronizar os dados do catálogo."

---

# Sincronizar e excluir dados do catálogo

> Esta página aborda como sincronizar os dados do catálogo.
 
## Etapa 1: Criar um novo catálogo

Antes de criar uma nova integração de ingestão de dados na nuvem (CDI) para [catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/), você precisa criar um novo catálogo ou identificar um catálogo existente que deseja usar para a integração. Existem algumas maneiras de criar um novo catálogo, e qualquer uma delas funcionará para a integração CDI:
- Faça upload de um [CSV]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-1-upload-csv)
- Crie um catálogo no [dashboard da Braze]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-2-create-in-browser) ou durante a configuração do CDI.
- Crie um catálogo usando o [endpoint de criação de catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)

Quaisquer alterações no esquema do catálogo (por exemplo, adicionar novos campos ou alterar o tipo de campo) devem ser feitas pelo dashboard do catálogo antes que os dados atualizados sejam sincronizados pelo CDI. Recomendamos fazer essas atualizações quando a sincronização estiver pausada ou não programada para ser executada, para evitar conflitos entre os dados do seu data warehouse e o esquema na Braze.

## Etapa 2: Integrar a Ingestão de Dados na Nuvem com dados de catálogo
A configuração para uma sincronização de catálogo segue de perto o processo para [integrações CDI de dados do usuário]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations#product-setup). 

{% tabs %}
{% tab Snowflake %}

1. Configure uma tabela de origem no Snowflake. Você pode usar os nomes no exemplo a seguir ou escolher seus próprios nomes de banco de dados, esquema e tabela. Você também pode usar uma view ou uma view materializada em vez de uma tabela.
  ```sql
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
2. Configure uma role, warehouse e usuário e conceda as permissões adequadas. Se você já tiver credenciais de uma sincronização existente, poderá reutilizá-las, mas certifique-se de estender o acesso à tabela de origem do catálogo.
    ```sql
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. Se a sua conta do Snowflake tiver políticas de rede, adicione os IPs da Braze à lista de permissões para que o serviço CDI possa se conectar. Para uma lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).
4. No dashboard da Braze, navegue até **Technology Partners** > **Snowflake** e crie uma nova sincronização.
5. Insira os detalhes de conexão (ou reutilize credenciais existentes) e a tabela de origem.
6. Prossiga para a etapa 2 do fluxo de configuração, selecione o tipo de sincronização "Catalogs" e insira o nome da integração e o agendamento. Note que o nome da integração deve **corresponder exatamente** ao nome do catálogo que você criou anteriormente.
7. Escolha uma frequência de sincronização e prossiga para a próxima etapa.
8. Adicione a chave pública exibida no dashboard ao usuário que você criou para a Braze se conectar ao Snowflake. Para concluir esta etapa, você precisará de alguém com acesso `SECURITYADMIN` ou superior no Snowflake. 
9. Selecione **Test Connection** para verificar se tudo funciona conforme esperado. 
10. Salve a sincronização e use os dados sincronizados do catálogo para todos os seus casos de uso de personalização. 
{% endtab %}
{% tab Redshift %}

1. Configure uma tabela de origem no Redshift. Você pode usar os nomes no exemplo a seguir ou escolher seus próprios nomes de banco de dados, esquema e tabela. Você também pode usar uma view ou uma view materializada em vez de uma tabela.
    ```sql
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
2. Configure um usuário e conceda as permissões adequadas. Se você já tiver credenciais de uma sincronização existente, poderá reutilizá-las, mas certifique-se de estender o acesso à tabela de origem do catálogo.
    {% raw %}
    ```sql 
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE CATALOGS_SYNC TO braze_user;
    ```
    {% endraw %}
3. Se você tiver um firewall ou outras políticas de rede, deve conceder acesso de rede à Braze para a sua instância do Redshift. Permita o acesso dos IPs abaixo correspondentes à região do seu dashboard da Braze. Para uma lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab BigQuery %}

1. Opcionalmente, configure um novo projeto ou dataset para armazenar sua tabela de origem. 

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Crie uma ou mais tabelas para usar na sua integração CDI com os seguintes campos:

```sql
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

2. Configure um usuário e conceda as permissões adequadas. Se você já tiver credenciais de uma sincronização existente, poderá reutilizá-las&#8212;mas certifique-se de estender o acesso à tabela de origem do catálogo. 
A conta de serviço deve ter as seguintes permissões:
- BigQuery Connection User: permite que a Braze faça conexões.
- BigQuery User: fornece à Braze acesso para executar consultas, ler metadados do dataset e listar tabelas.
- BigQuery Data Viewer: fornece à Braze acesso para visualizar datasets e seus conteúdos.
- BigQuery Job User: fornece à Braze acesso para executar jobs.<br><br>Depois de criar a conta de serviço e conceder as permissões, gere uma chave JSON. Para saber mais, consulte [Criar e excluir chaves](https://cloud.google.com/iam/docs/keys-create-delete). Você fará upload dessa chave no dashboard da Braze mais tarde.

{:start="3"}
3. Se você tiver políticas de rede em vigor, deve conceder acesso de rede à Braze para a sua instância do BigQuery. Para uma lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Databricks %}

1. Configure uma tabela de origem no Databricks. Você pode usar os nomes no exemplo a seguir ou escolher seu catálogo, esquema e nomes de tabelas. Você também pode usar uma view ou uma view materializada em vez de uma tabela.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

```sql
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

- a. Selecione seu nome de usuário do Databricks e, em seguida, selecione **User Settings** no menu suspenso.
- b. Na guia **Access tokens**, selecione **Generate new token**.
- c. Insira um comentário que ajude a identificar esse token, como "CDI Braze". 
- d. Altere o tempo de vida do token para sem expiração, deixando a caixa **Lifetime (days)** em branco. Selecione **Generate**.
- e. Copie o token exibido e, em seguida, selecione **Done**. 
- f. Mantenha o token em um local seguro até que você precise inseri-lo durante a etapa de criação de credenciais no dashboard da Braze.

{:start="3"}
3. Se você tiver políticas de rede em vigor, deve conceder acesso de rede à Braze para a sua instância do Databricks. Para uma lista de IPs, consulte a página [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Microsoft Fabric %}

Crie uma ou mais tabelas para usar na sua integração CDI com os seguintes campos:

```sql
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

2. Configure um service principal e conceda as permissões adequadas. Se você já tiver credenciais de uma sincronização existente, poderá reutilizá-las&#8212;apenas certifique-se de estender o acesso à tabela de origem do catálogo. Para saber mais sobre como criar um novo service principal e credenciais, consulte a página [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views). 

{:start="3"}
3. Se você tiver políticas de rede em vigor, deverá conceder acesso de rede à Braze para a sua instância do Microsoft Fabric. Para uma lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab S3 %}
Configure seus arquivos de origem no S3 fornecendo arquivos JSON ou CSV. Tenha em mente:

- Os arquivos não podem incluir uma coluna `UPDATED_AT`  
- Você pode incluir um campo `DELETED` opcional para marcar itens para remoção 

{% subtabs %}
{% subtab JSON %}
```jsonl
{"id":"85","payload":"{\"product_name\":\"Product 85\",\"price\":85.85}"}
{"id":"1","payload":"{\"product_name\":\"Product 1\",\"price\":1.01}","deleted":true}
```
{% endsubtab %}

{% subtab CSV %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
{% endsubtab %}
{% endsubtabs %}

Para detalhes de configuração, consulte [Integrações de armazenamento de arquivos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/).

{% endtab %}
{% endtabs %}

## Como a integração funciona

Cada vez que a sincronização é executada, a Braze busca todas as linhas onde `UPDATED_AT` é posterior ao último valor sincronizado. Linhas no timestamp exato do limite podem ser ressincronizadas se novas linhas compartilharem o mesmo timestamp. Recomendamos criar uma view no seu data warehouse a partir dos dados do seu catálogo para configurar uma tabela de origem que será totalmente atualizada cada vez que uma sincronização for executada. Com views, você não precisará reescrever a consulta cada vez.

Por exemplo, se você tiver uma tabela de dados de produtos (`product_catalog_1`) com `product_id` e três atributos adicionais, poderá sincronizar a view abaixo:

{% tabs %}
{% tab Snowflake %}
```sql
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
```sql
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
```sql
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
```sql
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
```sql
CREATE VIEW [braze].[user_update_example]
AS SELECT 
    id as ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[product_catalog] ;
```
{% endtab %}
{% endtabs %}

- Os dados obtidos da integração serão usados para criar ou atualizar itens no catálogo de destino com base no `id` fornecido.
- Se DELETED estiver definido como `true`, o item do catálogo correspondente será excluído.
- A sincronização não registrará pontos de dados, mas todos os dados sincronizados contarão para o seu uso total do catálogo. Esse uso é medido com base no total de dados armazenados, então você não precisa se preocupar em sincronizar apenas dados alterados.