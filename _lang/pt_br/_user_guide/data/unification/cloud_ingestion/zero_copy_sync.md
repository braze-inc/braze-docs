---
nav_title: Personalização sem cópia
article_title: Personalização sem cópia usando CDI
page_order: 4
page_type: reference
description: "Esta página fornece uma visão geral de como disparar Canvases do Braze usando CDI."
---

# Personalização sem cópia usando CDI

> Aprenda como sincronizar disparadores de Canvas usando CDI para personalização sem cópia. Este recurso acessa informações específicas do usuário da sua solução de armazenamento de dados e as passa para um Canvas de destino. Os passos do Canvas podem opcionalmente incluir campos de personalização que não são persistidos nos perfis de usuário do Braze.

{% include early_access_beta_alert.md feature='CDI Canvas triggers' %}

## Sincronizando disparadores de Canvas

### Passos para início rápido

Se você já está familiarizado com o CDI do Braze, note que a configuração para uma sincronização de disparador de Canvas segue de perto o processo para [integrações de CDI de dados do usuário]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/), com as seguintes ressalvas:

- Apenas identificadores de ID externo ou alias de usuário são suportados. E-mails e números de telefone não são identificadores suportados.  
- Apenas usuários existentes do Braze podem ser sincronizados. Novos usuários não podem ser criados.  
- `properties` substitui a coluna `payload`. Esta é uma string JSON dos campos que você deseja usar como propriedades de entrada do Canvas para personalização.

Para começar, selecione o tipo de dado **Disparadores de Canvas** ao criar uma nova sincronização.

### Usando disparadores de Canvas 

#### Etapa 1: Configurar fonte de dados para disparadores de Canvas

{% tabs %}
{% tab Snowflake %}

##### Etapa 1.1: Configure sua tabela de origem no Snowflake

Você pode usar os nomes no exemplo a seguir ou escolher seus próprios nomes de banco de dados, esquema e tabela. Você também pode usar uma visão ou uma visão materializada em vez de uma tabela.  

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

Você pode nomear o banco de dados, esquema e tabela como desejar, mas os nomes das colunas devem corresponder à definição anterior.

* `UPDATED_AT`: O momento em que esta linha foi atualizada ou adicionada à tabela. Apenas as linhas adicionadas ou atualizadas desde a última sincronização serão sincronizadas.  
* Ou `external_id` ou `alias_name` e `alias_label` como a coluna identificadora do usuário. Esses identificam os usuários para os quais você deseja disparar o envio de mensagens do Canvas.  
  * `EXTERNAL_ID`: Identifica o usuário a ser inserido no Canvas. Esse valor deve corresponder ao valor `external_id` usado no Braze.  
  * `ALIAS_NAME` e `ALIAS_LABEL`: Essas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador único, e `alias_label` especifica o tipo de alias. Os usuários podem ter múltiplos aliases com rótulos diferentes, mas apenas um alias_name por `alias_label`.  
* `PROPERTIES`: Uma string JSON de campos para disponibilizar como propriedades de personalização no seu Canvas. Isso deve conter informações específicas do usuário.

{% alert note %}
Propriedades não são obrigatórias para cada linha ou usuário. No entanto, os valores das propriedades devem ser uma string JSON válida. Insira uma string `{}` vazia se não houver propriedades para a linha.
{% endalert %}

##### Etapa 1.2: Configurar credenciais

Configurar um papel, armazém e usuário, e conceder as permissões adequadas. Se você já tiver credenciais de uma sincronização existente, pode reutilizá-las, mas certifique-se de estender o acesso à tabela de origem dos disparadores do Canvas.  

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

Se sua conta tiver políticas de rede, adicione os IPs do Braze à lista de permissões para habilitar a conexão do serviço CDI. Para a lista de IPs, veja [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional).  

{% endtab %}
{% tab Redshift %}

##### Etapa 1.1: Configure sua tabela de origem no Redshift

Você pode usar os nomes no exemplo a seguir ou escolher seus próprios nomes de banco de dados, esquema e tabela. Você também pode usar uma visão ou uma visão materializada em vez de uma tabela.

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

Você pode nomear o banco de dados, esquema e tabela como desejar, mas os nomes das colunas devem corresponder à definição anterior.

* `UPDATED_AT`: O momento em que esta linha foi atualizada ou adicionada à tabela. Apenas as linhas adicionadas ou atualizadas desde a última sincronização serão sincronizadas.  
* Ou `external_id` ou `alias_name` e `alias_label` como a coluna identificadora do usuário. Esses identificam os usuários para os quais você deseja disparar o envio de mensagens do Canvas.  
  * `EXTERNAL_ID`: Identifica o usuário a ser inserido no Canvas. Esse valor deve corresponder ao valor `external_id` usado no Braze.  
  * `ALIAS_NAME` e `ALIAS_LABEL`: Essas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador único, e alias_label especifica o tipo de alias. Os usuários podem ter múltiplos aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.  
* `PROPERTIES`: Uma string JSON de campos para disponibilizar como propriedades de personalização no seu Canvas. Isso deve conter informações específicas do usuário.

{% alert note %}
Propriedades não são obrigatórias para cada linha ou usuário. No entanto, os valores das propriedades devem ser uma string JSON válida. Insira uma string `{}` vazia se não houver propriedades para a linha.
{% endalert %}

##### Etapa 1.2: Configurar credenciais

Configure um papel, armazém e usuário e conceda as permissões adequadas. Se você já tiver credenciais de uma sincronização existente, pode reutilizá-las, mas certifique-se de estender o acesso à tabela de origem dos disparadores do Canvas.

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE CANVAS_TRIGGERS_SYNC TO braze_user;
```

##### Etapa 1.3: Configurar políticas de rede 

Se sua conta tiver políticas de rede, adicione os IPs do Braze à lista de permissões para habilitar a conexão do serviço CDI. Para a lista de IPs, veja [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=redshift#step-13-allow-access-to-braze-ips).

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
| **`UPDATED_AT`** | Data e hora | Sim | 
| **`PROPERTIES`** | JSON | Sim | 
| **`EXTERNAL_ID`** | STRING | NULLABLE | 
| **`ALIAS_NAME`** | STRING | NULLABLE | 
| **`ALIAS_LABEL`** | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Propriedades não são obrigatórias para cada linha ou usuário. No entanto, os valores das propriedades devem ser uma string JSON válida. Insira uma string `{}` vazia se não houver propriedades para a linha.
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

Crie um usuário e conceda permissões. Se você já tiver credenciais de outra sincronização, pode reutilizá-las desde que tenham acesso à tabela de gatilhos do canva.

| Permissão | Finalidade |
| :---- | :---- |
| Usuário de Conexão do BigQuery | Permite que o Braze se conecte. |
| Usuário do BigQuery | Permite que o Braze execute consultas, leia metadados e liste tabelas. |
| Visualizador de Dados do BigQuery | Permite que o Braze visualize conjuntos de dados e conteúdos. |
| Usuário de Trabalho do BigQuery | Permite que o Braze execute trabalhos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Após conceder permissões, gere uma chave JSON. Veja [Chaves criar e excluir](https://cloud.google.com/iam/docs/keys-create-delete) para instruções. Você fará upload dela no dashboard do Braze mais tarde.

##### Etapa 1.4: Configurar políticas de rede 
Se sua conta tiver políticas de rede, adicione os IPs do Braze à lista de permissões para habilitar a conexão do serviço CDI. Para a lista de IPs, veja [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=bigquery#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Databricks %}

##### Etapa 1.1: Crie um catálogo ou esquema para sua tabela de origem.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

#### Etapa 1.2: Configure sua tabela de origem no Databricks

Consulte o seguinte ao criar sua tabela de origem:

| Nome do campo | Tipo | Obrigatória |
| :---- | :---- | :---- |
| `UPDATED_AT` | Data e hora | Sim |
| `PROPERTIES` | JSON | Sim |
| `EXTERNAL_ID` | STRING |  NULLABLE |
| `ALIAS_NAME` | STRING | NULLABLE |
| `ALIAS_LABEL` | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Você pode nomear o esquema e a tabela como desejar, mas os nomes das colunas devem corresponder à definição anterior.

* `UPDATED_AT`: O momento em que esta linha foi atualizada ou adicionada à tabela. Apenas as linhas adicionadas ou atualizadas desde a última sincronização serão sincronizadas.  
* Ou `external_id` ou `alias_name` e `alias_label` como a coluna identificadora do usuário. Esses identificam os usuários para os quais você deseja disparar o envio de mensagens do Canvas.  
  * `EXTERNAL_ID`: Identifica o usuário a ser inserido no Canvas. Esse valor deve corresponder ao valor `external_id` usado no Braze.  
  * `ALIAS_NAME` e `ALIAS_LABEL`: Essas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador único, e `alias_label` especifica o tipo de alias. Os usuários podem ter múltiplos aliases com rótulos diferentes, mas apenas um alias_name por `alias_label`.  
* `PROPERTIES`: Uma string ou estrutura de campos para disponibilizar como propriedades de personalização em seu canva. Isso deve conter informações específicas do usuário.

{% alert note %}
Propriedades não são obrigatórias para cada linha ou usuário. No entanto, os valores das propriedades devem ser strings JSON válidas. Insira uma string `{}` vazia se não houver propriedades para a linha.
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

1. Selecione seu nome de usuário e, em seguida, selecione **Configurações do Usuário.**  
2. Na aba **Tokens de Acesso**, selecione **Gerar novo token.**  
3. Adicione um comentário para identificar o token, como “Braze CDI”.  
4. Deixe **Duração (dias)** em branco para não expirar, e então selecione **Gerar**.  
5. Copie e salve o token com segurança para uso no dashboard do Braze.

##### Etapa 1.4: Configurar políticas de rede 

Se sua conta tiver políticas de rede, adicione os IPs do Braze à lista de permissões para habilitar a conexão do serviço CDI. Para a lista de IPs, veja [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=databricks#step-13-allow-access-to-braze-ips).

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

Crie um principal de serviço e conceda permissões. Se você já tiver credenciais de outra sincronização, pode reutilizá-las—apenas certifique-se de que elas tenham acesso à tabela de contas.

##### Etapa 1.3: Configurar políticas de rede 

Se sua conta tiver políticas de rede, adicione os IPs do Braze à lista de permissões para habilitar a conexão do serviço CDI. Para a lista de IPs, veja [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=microsoft%20fabric#step-15-allow-braze-ips-in-firewall-optional).

{% endtab %}
{% tab File Storage %}

Para sincronizar os gatilhos do canva a partir do armazenamento de arquivos, crie um arquivo de origem com os seguintes campos.

| Campo | Obrigatória | Descrição |
| :---- | :---- | :---- |
| `EXTERNAL_ID` | Sim, um de `external_id` ou `alias_name`, e `alias_label` | Isso identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado no Braze. |
| `ALIAS_NAME` e `ALIAS_LABEL` | Sim, um de `external_id` ou `alias_name` e `alias_label` | Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador único, e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`. |
| `PROPERTIES` | Sim | String JSON de campos para disponibilizar como propriedades de personalização em seu canva. Isso deve conter informações específicas do usuário. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Os nomes dos arquivos devem seguir as regras da AWS e ser únicos. Anexe carimbos de data e hora para ajudar a garantir a exclusividade. Para mais informações sobre a sincronização do Amazon S3, veja [Integrações de Armazenamento de Arquivos](https://www.braze.com/docs/user_guide/data/cloud_ingestion/file_storage_integrations).
{% endalert %}

{% endtab %}
{% endtabs %}

#### Etapa 2: Configure seu Canvas de destino

1. Configure seu Canvas de destino para os gatilhos do Canvas. Crie um novo ou selecione um Canvas acionado por API existente. Consulte [Tipos de agendamento de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#entry-schedule-types) para instruções sobre como criar um canvas com um tipo de agendamento de entrega acionado por API.
2. Após selecionar o tipo de agendamento de entrega acionado por API, continue com a configuração do Canvas e construa seu Canvas. Os Canvases podem variar de envios simples de mensagens únicas a fluxos de trabalho complexos de clientes com várias etapas.
3. Dentro das etapas do seu Canvas, use [Propriedades de entrada do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) para personalizar mensagens com campos de propriedades que você planeja sincronizar da sua tabela de origem.
  * Por exemplo, se na Etapa 1 você instrumentou um campo de propriedades para `account_balance`, você usaria a seguinte modelagem Liquid para personalizar sua mensagem: `\{\{canvas_entry_properties.\$\{account_balance\}\}\}`.
5. Após construir seu Canvas, lance-o e prossiga para [Etapa 3](#step-3-create-your-zero-copy-sync).

#### Etapa 3: Crie sua sincronização de cópia zero

Com a configuração da sua origem concluída e o Canvas de destino lançado, crie uma nova sincronização de dados:

1. No Braze, vá para **Configurações de Dados** > **Ingestão de Dados na Nuvem**.
1. Configure a conexão inserindo os detalhes da conexão (ou reutilize credenciais existentes) e a tabela de origem de [Etapa 1](#step-1-set-up-data-source-for-canvas-triggers).
2. Forneça um nome para a integração.
3. Selecione o tipo de dados **Gatilhos do Canvas**.
4. Escolha seu Canvas de destino (da [Etapa 2](#step-2-configure-your-destination-canvas)).
5. Escolha uma frequência de sincronização.
6. Configure as preferências de notificação.
7. Selecione **Test Connection** para confirmar que tudo funciona como esperado. Se conectando ao Snowflake, primeiro adicione a chave pública exibida no dashboard ao usuário criado para o Braze se conectar ao Snowflake. Para completar esta etapa, você precisará de acesso **SECURITYADMIN** ou superior no Snowflake. 
8. Salve a sincronização para começar a sincronizar os disparadores do Canvas.

Quando a sincronização for executada, os usuários na sua tabela de origem começarão a entrar no Canvas. Use a análise de dados do Canvas e a página de logs de sincronização de Ingestão de Dados na Nuvem para monitorar a performance.

{% alert tip %}  
Revise toda a sua configuração (desde o comportamento da sincronização até a configuração do Canvas) para evitar envios inesperados. Configurações do Canvas, como limite de frequência, controle de frequência e filtros de segmentação, podem refinar ainda mais a entrega de mensagens.<br><br>Recomendamos realizar um teste com um público pequeno ou de teste antes de implementar casos de uso em produção.
{% endalert %}

### Considerações

Os disparadores do Canvas CDI utilizam o limite de frequência da sua API REST para `/canvas/trigger/send`. Se você estiver usando este endpoint simultaneamente com os disparadores do Canvas CDI e sua integração com a API REST, espere que o uso combinado conte para o seu limite de frequência.

Enquanto os disparadores do Canvas CDI estão em acesso antecipado, considere os seguintes detalhes:

* Até 5 sincronizações ativas de disparadores do Canvas por espaço de trabalho  
* Cada execução de sincronização entrará usuários em seu respectivo Canvas de destino a uma taxa máxima de aproximadamente 3,75 milhões de usuários por hora.  
  * Esteja preparado para tempos de entrada mais longos de origem para Canvas quando:  
    * Sincronizando mais de 3,75 milhões de usuários por execução de sincronização.  
    * Usando disparadores do Canvas CDI quando já saturando o [limite de frequência da sua API REST para `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit).