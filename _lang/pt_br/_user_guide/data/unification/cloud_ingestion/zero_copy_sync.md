---
nav_title: Personalização de cópia zero
article_title: Personalização de cópia zero usando CDI
page_order: 4
page_type: reference
description: "Esta página fornece uma visão geral de como acionar telas de brasagem usando CDI."
---

# Personalização de cópia zero usando CDI

> Saiba como sincronizar os acionadores do Canvas usando CDI para personalização de cópia zero. Esse recurso acessa informações específicas do usuário da sua solução de armazenamento de dados e as transmite para um Canvas de destino. As etapas do Canvas podem, opcionalmente, incluir campos de personalização que não são mantidos nos perfis de usuário do Braze.

{% alert important %}
Os acionadores do CDI Canvas estão atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Sincronização de acionadores do Canvas

### Etapas de início rápido

Se você já estiver familiarizado com o Braze CDI, observe que a configuração de uma sincronização de gatilho do Canvas segue de perto o processo de [integrações de CDI de dados do usuário]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/), com as seguintes ressalvas:

- Somente identificadores externos de ID ou alias de usuário são compatíveis. E-mail e números de telefone não são identificadores compatíveis.  
- Somente os usuários existentes do Braze podem ser sincronizados. Não é possível criar novos usuários.  
- `properties` substitui a coluna `payload`. Essa é uma cadeia de caracteres JSON dos campos que você deseja usar como propriedades de entrada do Canvas para personalização.

Para começar, selecione o tipo de dados **Canvas Triggers** ao criar uma nova sincronização.

### Uso de acionadores do Canvas 

#### Etapa 1: Configurar a fonte de dados para acionadores do Canvas

{% tabs %}
{% tab Snowflake %}

##### Etapa 1.1: Configure sua tabela de origem no Snowflake

Você pode usar os nomes do exemplo a seguir ou escolher seus próprios nomes de banco de dados, esquema e tabela. Você também pode usar uma visualização ou uma visualização materializada em vez de uma tabela.  

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id or alias_name and alias_label is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     PROPERTIES VARCHAR(16777216)
);
```

Você pode nomear o banco de dados, o esquema e a tabela como quiser, mas os nomes das colunas devem corresponder à definição anterior.

* `UPDATED_AT`: A hora em que essa linha foi atualizada ou adicionada à tabela. Somente as linhas adicionadas ou atualizadas desde a última sincronização serão sincronizadas.  
* `external_id` ou `alias_name` e `alias_label` como a coluna de identificador de usuário. Eles identificam os usuários para os quais você deseja acionar as mensagens do Canvas.  
  * `EXTERNAL_ID`: Identifica o usuário a ser inserido no Canvas. Isso deve corresponder ao valor `external_id` usado no Braze.  
  * `ALIAS_NAME` e `ALIAS_LABEL`: Essas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas somente um alias_name por `alias_label`.  
* `PROPERTIES`: Uma cadeia de caracteres JSON de campos a serem disponibilizados como propriedades de personalização em seu Canvas. Deve conter informações específicas do usuário.

{% alert note %}
As propriedades não são necessárias para cada linha ou usuário. No entanto, os valores das propriedades devem ser uma cadeia de caracteres JSON válida. Insira uma cadeia de caracteres `{}` vazia se não houver propriedades para a linha.
{% endalert %}

##### Etapa 1.2: Configurar credenciais

Configure uma função, um depósito e um usuário e conceda as permissões adequadas. Se você já tiver credenciais de uma sincronização existente, poderá reutilizá-las, mas certifique-se de estender o acesso à tabela de origem dos acionadores do Canvas.  

```sql

CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

CREATE USER BRAZE_INGESTION_USER;
GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;

```

##### Etapa 1.3: Configurar políticas de rede

Se a sua conta tiver políticas de rede, permita a lista de IPs do Braze para habilitar a conexão do serviço CDI. Para obter a lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional).  

{% endtab %}
{% tab Redshift %}

##### Etapa 1.1: Configure sua tabela de origem no Redshift

Você pode usar os nomes do exemplo a seguir ou escolher seus próprios nomes de banco de dados, esquema e tabela. Você também pode usar uma visualização ou uma visualização materializada em vez de uma tabela.

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC (
    updated_at timestamptz default sysdate not null,
    --at least one of external_id or alias_name and alias_label is required
    external_id varchar not null,.
    --if using user alias, both alias_name and alias_label are required
    alias_label varchar,
    alias_name varchar,
    properties varchar(max)
 );
```

Você pode nomear o banco de dados, o esquema e a tabela como quiser, mas os nomes das colunas devem corresponder à definição anterior.

* `UPDATED_AT`: A hora em que essa linha foi atualizada ou adicionada à tabela. Somente as linhas adicionadas ou atualizadas desde a última sincronização serão sincronizadas.  
* `external_id` ou `alias_name` e `alias_label` como a coluna de identificador de usuário. Eles identificam os usuários para os quais você deseja acionar as mensagens do Canvas.  
  * `EXTERNAL_ID`: Identifica o usuário a ser inserido no Canvas. Isso deve corresponder ao valor `external_id` usado no Braze.  
  * `ALIAS_NAME` e `ALIAS_LABEL`: Essas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e alias_label especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas somente um `alias_name` por `alias_label`.  
* `PROPERTIES`: Uma cadeia de caracteres JSON de campos a serem disponibilizados como propriedades de personalização em seu Canvas. Deve conter informações específicas do usuário.

{% alert note %}
As propriedades não são necessárias para cada linha ou usuário. No entanto, os valores das propriedades são uma cadeia de caracteres JSON válida. Insira uma cadeia de caracteres `{}` vazia se não houver propriedades para a linha.
{% endalert %}

##### Etapa 1.2: Configurar credenciais

Configure uma função, um depósito e um usuário e conceda as permissões adequadas. Se você já tiver credenciais de uma sincronização existente, poderá reutilizá-las, mas certifique-se de estender o acesso à tabela de origem dos acionadores do Canvas.

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE CANVAS_TRIGGERS_SYNC TO braze_user;
```

##### Etapa 1.3: Configurar políticas de rede 

Se a sua conta tiver políticas de rede, permita a lista de IPs do Braze para habilitar a conexão do serviço CDI. Para obter a lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=redshift#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab BigQuery %}

##### Etapa 1.1: Crie um novo projeto ou conjunto de dados para sua tabela de origem (opcional)

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

##### Etapa 1.2: Configure sua tabela de origem no BigQuery
Consulte o seguinte ao criar sua tabela de origem:  

| Nome do campo | Tipo | Necessário? | 
| :---- | :---- | :---- | 
| **`UPDATED_AT`** | Carimbo de data/hora | Sim | 
| **`PROPERTIES`** | JSON | Sim | 
| **`EXTERNAL_ID`** | STRING | NULLABLE | 
| **`ALIAS_NAME`** | STRING | NULLABLE | 
| **`ALIAS_LABEL`** | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
As propriedades não são necessárias para cada linha ou usuário. No entanto, os valores das propriedades são uma cadeia de caracteres JSON válida. Insira uma cadeia de caracteres `{}` vazia se não houver propriedades para a linha.
{% endalert %}

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id or alias_name and alias_label is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  properties JSON
);
```

##### Etapa 1.3: Configurar credenciais

Crie um usuário e conceda permissões. Se você já tiver credenciais de outra sincronização, poderá reutilizá-las, desde que elas tenham acesso à tabela de acionadores de tela.

| Permissão | Finalidade |
| :---- | :---- |
| Usuário de conexão do BigQuery | Permite que o Braze se conecte. |
| Usuário do BigQuery | Permite que o Braze execute consultas, leia metadados e liste tabelas. |
| Visualizador de dados do BigQuery | Permite que o Braze visualize conjuntos de dados e conteúdos. |
| Usuário do BigQuery Job | Permite que o Braze execute trabalhos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Após conceder as permissões, gere uma chave JSON. Consulte [Criar e excluir chaves](https://cloud.google.com/iam/docs/keys-create-delete) para obter instruções. Você fará o upload no painel de controle do Braze mais tarde.

##### Etapa 1.4: Configurar políticas de rede 
Se a sua conta tiver políticas de rede, permita a lista de IPs do Braze para habilitar a conexão do serviço CDI. Para obter a lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=bigquery#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Databricks %}

##### Etapa 1.1: Crie um catálogo ou esquema para sua tabela de origem.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

#### Etapa 1.2: Configure sua tabela de origem no Databricks

Consulte o seguinte ao criar sua tabela de origem:

| Nome do campo | Tipo | Necessário |
| :---- | :---- | :---- |
| `UPDATED_AT` | Carimbo de data/hora | Sim |
| `PROPERTIES` | JSON | Sim |
| `EXTERNAL_ID` | STRING |  NULLABLE |
| `ALIAS_NAME` | STRING | NULLABLE |
| `ALIAS_LABEL` | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Você pode nomear o esquema e a tabela como quiser, mas os nomes das colunas devem corresponder à definição anterior.

* `UPDATED_AT`: A hora em que essa linha foi atualizada ou adicionada à tabela. Somente as linhas adicionadas ou atualizadas desde a última sincronização serão sincronizadas.  
* `external_id` ou `alias_name` e `alias_label` como a coluna de identificador de usuário. Eles identificam os usuários para os quais você deseja acionar as mensagens do Canvas.  
  * `EXTERNAL_ID`: Identifica o usuário a ser inserido no Canvas. Isso deve corresponder ao valor `external_id` usado no Braze.  
  * `ALIAS_NAME` e `ALIAS_LABEL`: Essas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas somente um alias_name por `alias_label`.  
* `PROPERTIES`: Uma string ou struct de campos a serem disponibilizados como propriedades de personalização em seu Canvas. Deve conter informações específicas do usuário.

{% alert note %}
As propriedades não são necessárias para cada linha ou usuário. No entanto, os valores das propriedades devem ser cadeias de caracteres JSON válidas. Insira uma cadeia de caracteres `{}` vazia se não houver propriedades para a linha.
{% endalert %}

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id or alias_name and alias_label is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  properties STRING, STRUCT, or MAP
);
```

##### Etapa 1.3: Configurar credenciais 

Crie um token de acesso pessoal no Databricks:

1. Selecione seu nome de usuário e, em seguida, selecione **User Settings (Configurações do usuário).**  
2. Na guia **Access tokens (Tokens de acesso** ), selecione **Generate new token (Gerar novo token).**  
3. Adicione um comentário para identificar o token, como "Braze CDI".  
4. Deixe **Lifetime (days)** em branco para que não haja expiração e selecione **Generate (Gerar**).  
5. Copie e salve o token com segurança para uso no painel de controle do Braze.

##### Etapa 1.4: Configurar políticas de rede 

Se a sua conta tiver políticas de rede, permita a lista de IPs do Braze para habilitar a conexão do serviço CDI. Para obter a lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=databricks#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Fabric %}

##### Etapa 1.1: Configure sua tabela de origem no Fabric

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PROPERTIES VARCHAR NOT NULL,
  --at least one of external_id or alias_name and alias_label is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR
)
GO
```

##### Etapa 1.2: Configurar credenciais 

Crie uma entidade de serviço e conceda permissões. Se você já tiver credenciais de outra sincronização, poderá reutilizá-las - apenas certifique-se de que elas tenham acesso à tabela de contas.

##### Etapa 1.3: Configurar políticas de rede 

Se a sua conta tiver políticas de rede, permita a lista de IPs do Braze para habilitar a conexão do serviço CDI. Para obter a lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=microsoft%20fabric#step-15-allow-braze-ips-in-firewall-optional).

{% endtab %}
{% tab File Storage %}

Para sincronizar os acionadores do Canvas a partir do armazenamento de arquivos, crie um arquivo de origem com os seguintes campos.

| Campo | Necessário | Descrição |
| :---- | :---- | :---- |
| `EXTERNAL_ID` | Sim, um de `external_id` ou `alias_name`, e `alias_label` | Isso identifica o usuário que você deseja atualizar. Isso deve corresponder ao valor `external_id` usado no Braze. |
| `ALIAS_NAME` e `ALIAS_LABEL` | Sim, um dos sites `external_id` ou `alias_name` e `alias_label` | Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas somente um `alias_name` por `alias_label`. |
| `PROPERTIES` | Sim | Cadeia de caracteres JSON de campos a serem disponibilizados como propriedades de personalização em seu Canvas. Deve conter informações específicas do usuário. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Os nomes de arquivos devem seguir as regras da AWS e ser exclusivos. Acrescente registros de data e hora para ajudar a garantir a exclusividade. Para obter mais informações sobre a sincronização do Amazon S3, consulte [Integrações de armazenamento de arquivos](https://www.braze.com/docs/user_guide/data/cloud_ingestion/file_storage_integrations).
{% endalert %}

{% endtab %}
{% endtabs %}

#### Etapa 2: Configure seu Canvas de destino

1. Configure o Canvas de destino para os acionadores do Canvas. Crie um novo Canvas ou selecione um Canvas acionado por API existente. Consulte [Tipos de programação de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#entry-schedule-types) para obter instruções sobre como criar uma tela com um tipo de programação de entrega acionado por API.
2. Depois de selecionar o tipo de programação de entrega acionada por API, continue com a configuração do Canvas e crie seu Canvas. As telas podem variar de simples envios de mensagem única a complexos fluxos de trabalho de clientes com várias etapas.
3. Nas etapas do Canvas, use [as propriedades de entrada do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) para personalizar as mensagens com campos de propriedades que você planeja sincronizar da tabela de origem.
  * Por exemplo, se na Etapa 1 você instrumentou um campo de propriedades para `account_balance`, você usaria o seguinte modelo Liquid para personalizar sua mensagem: `\{\{canvas_entry_properties.\$\{account_balance\}\}\}`.
5. Depois de criar seu Canvas, inicie-o e prossiga para a [Etapa 3](#step-3-create-your-zero-copy-sync).

#### Etapa 3: Crie sua sincronização de cópia zero

Com a configuração da origem concluída e o Canvas de destino iniciado, crie uma nova sincronização de dados:

1. No Braze, vá para **Data Settings** > **Cloud Data Ingestion**.
1. Configure a conexão inserindo os detalhes da conexão (ou reutilize as credenciais existentes) e a tabela de origem da [Etapa 1](#step-1-set-up-data-source-for-canvas-triggers).
2. Forneça um nome para a integração.
3. Selecione o tipo de dados dos **acionadores do Canvas**.
4. Escolha seu Canvas de destino (na [Etapa 2](#step-2-configure-your-destination-canvas)).
5. Escolha uma frequência de sincronização.
6. Configure as preferências de notificação.
7. Selecione **Testar conexão** para confirmar que tudo está funcionando como esperado. Se estiver se conectando ao Snowflake, primeiro adicione a chave pública exibida no painel ao usuário criado para o Braze para se conectar ao Snowflake. Para concluir essa etapa, você precisará de acesso **SECURITYADMIN** ou superior no Snowflake. 
8. Salve a sincronização para começar a sincronizar os acionadores do Canvas.

Quando a sincronização for executada, os usuários da tabela de origem começarão a entrar no Canvas. Use a análise do Canvas e a página de registros de sincronização da ingestão de dados na nuvem para monitorar o desempenho.

{% alert tip %}  
Revise toda a sua configuração (do comportamento de sincronização à configuração do Canvas) para evitar envios inesperados. As configurações do Canvas, como limitação de taxa, limite de frequência e filtros de segmentação, podem refinar ainda mais a entrega de mensagens.<br><br>Recomendamos realizar um teste com um público pequeno ou de teste antes de implementar casos de uso de produção.
{% endalert %}

### Considerações

Os acionadores do CDI Canvas utilizam o limite de taxa da API REST para `/canvas/trigger/send`. Se você estiver usando esse endpoint simultaneamente com os acionadores do CDI Canvas e sua integração com a API REST, espere que o uso combinado conte para o seu limite de taxa.

Embora os acionadores do CDI Canvas estejam em acesso antecipado, considere os detalhes a seguir:

* Até 5 sincronizações ativas do acionador do Canvas por espaço de trabalho  
* Cada execução de sincronização inserirá os usuários em seu respectivo Canvas de destino a uma taxa máxima de aproximadamente 3,75 milhões de usuários por hora.  
  * Esteja preparado para tempos mais longos de entrada da fonte para a tela quando:  
    * Sincronização de mais de 3,75 milhões de usuários por execução de sincronização.  
    * Usar os acionadores do CDI Canvas quando já estiver saturando o [limite de taxa]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit) da API REST [para `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit).