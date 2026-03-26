---
nav_title: Personalização sem cópia
article_title: Personalização sem cópia usando CDI
page_order: 4
page_type: reference
description: "Esta página fornece uma visão geral de como disparar os Braze Canvases usando o CDI."
---

# Personalização sem cópia usando CDI

> Aprenda a sincronizar gatilhos do Canvas usando CDI para personalização sem cópia. Esse recurso acessa informações específicas do usuário a partir da sua solução de armazenamento de dados e as transmite para um Canvas de destino. As etapas do canva podem incluir, opcionalmente, campos de personalização que não são mantidos nos perfis de usuário da Braze.

{% multi_lang_include early_access_beta_alert.md feature='CDI Canvas triggers' %}

## Sincronização de gatilhos do canva

### Etapas para início rápido

Se você já está familiarizado com o CDI da Braze, observe que a configuração para uma sincronização de gatilho do Canvas segue de perto o processo para [integrações CDI de dados de usuários]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/), com as seguintes ressalvas:

- Apenas identificadores de ID externo ou alias de usuário são aceitos. E-mails e números de telefone não são identificadores aceitos.  
- Apenas usuários existentes da Braze podem ser sincronizados. Não é possível criar novos usuários.  
- `properties` substitui a coluna `payload`. Esta é uma string JSON dos campos que você deseja usar como propriedades de entrada do canva para personalização.

Para começar, selecione o tipo de dados **Canvas Triggers** ao criar uma nova sincronização.

### Usando gatilhos do Canvas 

#### Etapa 1: Configurar fonte de dados para gatilhos do Canvas

{% tabs %}
{% tab Snowflake %}

##### Etapa 1.1: Configure sua tabela de origem no Snowflake

Você pode usar os nomes no exemplo a seguir ou escolher seus próprios nomes de banco de dados, esquema e tabela. Você também pode usar uma view ou uma view materializada em vez de uma tabela.  

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

Você pode nomear o banco de dados, o esquema e a tabela como desejar, mas os nomes das colunas devem corresponder à definição anterior.

* `UPDATED_AT`: A hora em que esta linha foi atualizada ou adicionada à tabela. A Braze sincroniza as linhas em que `UPDATED_AT` é posterior ao último valor sincronizado. Linhas no exato timestamp de limite podem ser ressincronizadas se novas linhas compartilharem o mesmo timestamp.  
* `external_id` ou `alias_name` e `alias_label` como coluna de identificador do usuário. Estes identificam os usuários para os quais você deseja disparar o envio de mensagens do Canvas.  
  * `EXTERNAL_ID`: Identifica o usuário que entrará no Canvas. Esse valor deve corresponder ao valor `external_id` usado na Braze.  
  * `ALIAS_NAME` e `ALIAS_LABEL`: Essas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um alias_name por `alias_label`.  
* `PROPERTIES`: Uma string JSON de campos para disponibilizar como propriedades de personalização no seu Canvas. Deve conter informações específicas do usuário.

{% alert note %}
As propriedades não são necessárias para todas as linhas ou usuários. No entanto, os valores das propriedades devem ser uma string JSON válida. Insira uma string `{}` vazia se não houver propriedades para a linha.
{% endalert %}

##### Etapa 1.2: Configurar credenciais

Configure uma função, um warehouse e um usuário, e conceda as permissões adequadas. Se você já possui credenciais de uma sincronização existente, pode reutilizá-las, mas certifique-se de estender o acesso à tabela de origem dos gatilhos do Canvas.  

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

Se sua conta tiver políticas de rede, inclua os IPs da Braze na lista de permissões para ativar a conexão do serviço CDI. Para obter a lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional).  

{% endtab %}
{% tab Redshift %}

##### Etapa 1.1: Configure sua tabela de origem no Redshift

Você pode usar os nomes no exemplo a seguir ou escolher seus próprios nomes de banco de dados, esquema e tabela. Você também pode usar uma view ou uma view materializada em vez de uma tabela.

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

Você pode nomear o banco de dados, o esquema e a tabela como desejar, mas os nomes das colunas devem corresponder à definição anterior.

* `UPDATED_AT`: A hora em que esta linha foi atualizada ou adicionada à tabela. A Braze sincroniza as linhas em que `UPDATED_AT` é posterior ao último valor sincronizado. Linhas no exato timestamp de limite podem ser ressincronizadas se novas linhas compartilharem o mesmo timestamp.  
* `external_id` ou `alias_name` e `alias_label` como coluna de identificador do usuário. Estes identificam os usuários para os quais você deseja disparar o envio de mensagens do Canvas.  
  * `EXTERNAL_ID`: Identifica o usuário que entrará no Canvas. Esse valor deve corresponder ao valor `external_id` usado na Braze.  
  * `ALIAS_NAME` e `ALIAS_LABEL`: Essas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e alias_label especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.  
* `PROPERTIES`: Uma string JSON de campos para disponibilizar como propriedades de personalização no seu Canvas. Deve conter informações específicas do usuário.

{% alert note %}
As propriedades não são necessárias para todas as linhas ou usuários. No entanto, os valores das propriedades devem ser uma string JSON válida. Insira uma string `{}` vazia se não houver propriedades para a linha.
{% endalert %}

##### Etapa 1.2: Configurar credenciais

Configure uma função, um warehouse e um usuário e conceda as permissões adequadas. Se você já possui credenciais de uma sincronização existente, pode reutilizá-las, mas certifique-se de estender o acesso à tabela de origem dos gatilhos do Canvas.

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE CANVAS_TRIGGERS_SYNC TO braze_user;
```

##### Etapa 1.3: Configurar políticas de rede 

Se sua conta tiver políticas de rede, inclua os IPs da Braze na lista de permissões para ativar a conexão do serviço CDI. Para obter a lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=redshift#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab BigQuery %}

##### Etapa 1.1: Crie um novo projeto ou conjunto de dados para sua tabela de origem (opcional)

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

##### Etapa 1.2: Configure sua tabela de origem no BigQuery
Consulte a referência a seguir ao criar sua tabela de origem:  

| Nome do campo | Tipo | Obrigatório? | 
| :---- | :---- | :---- | 
| **`UPDATED_AT`** | Timestamp | Sim | 
| **`PROPERTIES`** | JSON | Sim | 
| **`EXTERNAL_ID`** | STRING | NULLABLE | 
| **`ALIAS_NAME`** | STRING | NULLABLE | 
| **`ALIAS_LABEL`** | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
As propriedades não são necessárias para todas as linhas ou usuários. No entanto, os valores das propriedades devem ser uma string JSON válida. Insira uma string `{}` vazia se não houver propriedades para a linha.
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

Crie um usuário e conceda permissões. Se você já possui credenciais de outra sincronização, pode reutilizá-las, desde que tenham acesso à tabela de gatilhos do Canvas.

| Permissão | Finalidade |
| :---- | :---- |
| BigQuery Connection User | Permite que a Braze se conecte. |
| BigQuery User | Permite que a Braze execute consultas, leia metadados e liste tabelas. |
| BigQuery Data Viewer | Permite que a Braze visualize conjuntos de dados e conteúdos. |
| BigQuery Job User | Permite que a Braze execute tarefas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Após conceder as permissões, gere uma chave JSON. Consulte [Criar e excluir chaves](https://cloud.google.com/iam/docs/keys-create-delete) para obter instruções. Você fará o upload posteriormente no dashboard da Braze.

##### Etapa 1.4: Configurar políticas de rede 
Se sua conta tiver políticas de rede, inclua os IPs da Braze na lista de permissões para ativar a conexão do serviço CDI. Para obter a lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=bigquery#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Databricks %}

##### Etapa 1.1: Crie um catálogo ou esquema para sua tabela de origem.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

#### Etapa 1.2: Configure sua tabela de origem no Databricks

Consulte a referência a seguir ao criar sua tabela de origem:

| Nome do campo | Tipo | Obrigatório |
| :---- | :---- | :---- |
| `UPDATED_AT` | Timestamp | Sim |
| `PROPERTIES` | JSON | Sim |
| `EXTERNAL_ID` | STRING |  NULLABLE |
| `ALIAS_NAME` | STRING | NULLABLE |
| `ALIAS_LABEL` | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Você pode nomear o esquema e a tabela como desejar, mas os nomes das colunas devem corresponder à definição anterior.

* `UPDATED_AT`: A hora em que esta linha foi atualizada ou adicionada à tabela. A Braze sincroniza as linhas em que `UPDATED_AT` é posterior ao último valor sincronizado. Linhas no exato timestamp de limite podem ser ressincronizadas se novas linhas compartilharem o mesmo timestamp.  
* `external_id` ou `alias_name` e `alias_label` como coluna de identificador do usuário. Estes identificam os usuários para os quais você deseja disparar o envio de mensagens do Canvas.  
  * `EXTERNAL_ID`: Identifica o usuário que entrará no Canvas. Esse valor deve corresponder ao valor `external_id` usado na Braze.  
  * `ALIAS_NAME` e `ALIAS_LABEL`: Essas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um alias_name por `alias_label`.  
* `PROPERTIES`: Uma string ou estrutura de campos para disponibilizar como propriedades de personalização no seu Canvas. Deve conter informações específicas do usuário.

{% alert note %}
As propriedades não são necessárias para todas as linhas ou usuários. No entanto, os valores das propriedades devem ser strings JSON válidas. Insira uma string `{}` vazia se não houver propriedades para a linha.
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

1. Selecione seu nome de usuário e, em seguida, selecione **User Settings.**  
2. Na guia **Access tokens**, selecione **Generate new token.**  
3. Adicione um comentário para identificar o token, como "Braze CDI".  
4. Deixe o campo **Lifetime (days)** em branco para que não haja expiração e selecione **Generate**.  
5. Copie e salve o token com segurança para uso no dashboard da Braze.

##### Etapa 1.4: Configurar políticas de rede 

Se sua conta tiver políticas de rede, inclua os IPs da Braze na lista de permissões para ativar a conexão do serviço CDI. Para obter a lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=databricks#step-13-allow-access-to-braze-ips).

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

Crie uma entidade de serviço e conceda permissões. Se você já possui credenciais de outra sincronização, pode reutilizá-las — apenas certifique-se de que elas tenham acesso à tabela de contas.

##### Etapa 1.3: Configurar políticas de rede 

Se sua conta tiver políticas de rede, inclua os IPs da Braze na lista de permissões para ativar a conexão do serviço CDI. Para obter a lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=microsoft%20fabric#step-15-allow-braze-ips-in-firewall-optional).

{% endtab %}
{% tab File Storage %}

Para sincronizar os gatilhos do Canvas a partir do armazenamento de arquivos, crie um arquivo de origem com os seguintes campos.

| Campo | Obrigatório | Descrição |
| :---- | :---- | :---- |
| `EXTERNAL_ID` | Sim, um entre `external_id` ou `alias_name` e `alias_label` | Identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado na Braze. |
| `ALIAS_NAME` e `ALIAS_LABEL` | Sim, um entre `external_id` ou `alias_name` e `alias_label` | Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`. |
| `PROPERTIES` | Sim | String JSON de campos a serem disponibilizados como propriedades de personalização no seu Canvas. Deve conter informações específicas do usuário. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Os nomes dos arquivos devem seguir as regras da AWS e ser únicos. Adicione carimbos de data/hora para ajudar a garantir a exclusividade. Para saber mais sobre a sincronização com o Amazon S3, consulte [Integrações de armazenamento de arquivos](https://www.braze.com/docs/user_guide/data/cloud_ingestion/file_storage_integrations).
{% endalert %}

{% endtab %}
{% endtabs %}

#### Etapa 2: Configure seu Canvas de destino

1. Configure o seu Canvas de destino para gatilhos do Canvas. Crie um novo ou selecione um Canvas disparado por API existente. Consulte [Tipos de programação de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#entry-schedule-types) para obter instruções sobre como criar um canva com um tipo de programação de entrega disparado pela API.
2. Após selecionar o tipo de programação de entrega disparada pela API, continue com a configuração do Canvas e crie seu Canvas. Os canvas podem variar desde o envio simples de uma única mensagem até fluxos de trabalho complexos com várias etapas.
3. Nas etapas do Canvas, use as [propriedades de entrada do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) para personalizar mensagens com campos de propriedades que você planeja sincronizar da sua tabela de origem.
  * Por exemplo, se na Etapa 1 você instrumentou um campo de propriedades para `account_balance`, você usaria o seguinte modelo Liquid para personalizar sua mensagem: `\{\{canvas_entry_properties.\$\{account_balance\}\}\}`.
5. Depois de criar seu Canvas, inicie-o e prossiga para a [Etapa 3](#step-3-create-your-zero-copy-sync).

#### Etapa 3: Crie sua sincronização sem cópia

Com a configuração da fonte concluída e o Canvas de destino iniciado, crie uma nova sincronização de dados:

1. Na Braze, acesse **Configurações de dados** > **Ingestão de dados na nuvem**.
1. Configure a conexão inserindo os detalhes da conexão (ou reutilize as credenciais existentes) e a tabela de origem da [Etapa 1](#step-1-set-up-data-source-for-canvas-triggers).
2. Dê um nome à integração.
3. Selecione o tipo de dados **Canvas Triggers**.
4. Escolha o seu Canvas de destino (da [Etapa 2](#step-2-configure-your-destination-canvas)).
5. Escolha uma frequência de sincronização.
6. Configure as preferências de notificação.
7. Selecione **Testar conexão** para confirmar se tudo funciona conforme o esperado. Se estiver conectando ao Snowflake, primeiro adicione a chave pública exibida no dashboard ao usuário criado para a Braze se conectar ao Snowflake. Para concluir esta etapa, você precisará de acesso **SECURITYADMIN** ou superior no Snowflake. 
8. Salve a sincronização para começar a sincronizar os gatilhos do Canvas.

Quando a sincronização for executada, os usuários da sua tabela de origem começarão a entrar no Canvas. Use a análise de dados do Canvas e a página de registros de sincronização da ingestão de dados na nuvem para monitorar a performance.

{% alert tip %}  
Revise toda a sua configuração (desde o comportamento de sincronização até a configuração do Canvas) para evitar envios inesperados. As configurações do Canvas, como limite de taxa, limite de frequência e filtros de segmentação, podem refinar ainda mais a entrega de mensagens.<br><br>Recomendamos realizar um teste com um público pequeno ou experimental antes de implementar casos de uso em produção.
{% endalert %}

### Considerações

Os gatilhos do CDI Canvas utilizam o limite de taxa da sua API REST para `/canvas/trigger/send`. Se você estiver usando esse endpoint simultaneamente com os gatilhos CDI Canvas e sua integração de API REST, espere que o uso combinado seja contabilizado no seu limite de taxa.

Enquanto os gatilhos do CDI Canvas estiverem em acesso antecipado, considere os seguintes detalhes:

* Até 5 sincronizações ativas de gatilhos do Canvas por espaço de trabalho  
* Cada execução de sincronização inserirá os usuários em seu respectivo Canvas de destino a uma taxa máxima de aproximadamente 3,75 milhões de usuários por hora.  
  * Esteja preparado para tempos de entrada mais longos da fonte para o Canvas quando:  
    * Sincronizar mais de 3,75 milhões de usuários por execução de sincronização.  
    * Usar gatilhos do CDI Canvas quando já estiver saturando o [limite de taxa da sua API REST para `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit).