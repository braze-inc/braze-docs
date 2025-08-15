---
nav_title: Integrações de data warehouse
article_title: Integrações de data warehouse
description: "Esta página aborda como usar a ingestão de dados do Braze Cloud para sincronizar dados relevantes com sua integração do Snowflake, Redshift, BigQuery e Databricks."
page_order: 2
page_type: reference

---

# Integrações de armazenamento de data warehouse

> Esta página aborda como usar a ingestão de dados do Braze Cloud (CDI) para sincronizar dados relevantes com sua integração do Snowflake, Redshift, BigQuery e Databricks.

## Configuração de integrações de data warehouse

As integrações de ingestão de dados na nuvem exigem algumas configurações no lado da Braze e na instância do seu data warehouse. Siga estas etapas para configurar a integração:

{% tabs %}
{% tab Snowflake %}
1. Em sua instância do Snowflake, configure as tabelas ou exibições que deseja sincronizar com o Braze.
2. Crie uma nova integração no dashboard do Braze.
3. Recupere a chave pública fornecida no dashboard da Braze e [anexe-a ao usuário do Snowflake para autenticação](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Teste a integração e inicie a sincronização.

{% alert tip %}
O [guia de início rápido do Snowflake](https://quickstarts.snowflake.com/guide/braze_cdi/index.html) fornece um código de amostra e percorre as etapas necessárias para criar um pipeline automatizado usando o Snowflake Streams e o CDI para sincronizar dados para o Braze.
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. Certifique-se de que o acesso do Braze seja permitido às tabelas do Redshift que você deseja sincronizar. O Braze se conectará ao Redshift pela Internet.
2. Em sua instância do Redshift, configure as tabelas ou exibições que deseja sincronizar com o Braze.
3. Crie uma nova integração no dashboard do Braze.
4. Teste a integração e inicie a sincronização.
{% endtab %}
{% tab BigQuery %}
1. Crie uma conta de serviço e permita o acesso ao(s) projeto(s) e conjunto(s) de dados do BigQuery que contêm os dados que você deseja sincronizar.  
2. Em sua conta do BigQuery, configure as tabelas ou visualização(ões) que deseja sincronizar com o Braze.   
3. Crie uma nova integração no dashboard do Braze.  
4. Teste a integração e inicie a sincronização.  
{% endtab %}
{% tab Databricks %}
1. Crie uma conta de serviço e permita o acesso ao(s) projeto(s) e conjunto(s) de dados do Databricks que contêm os dados que você deseja sincronizar.  
2. Em sua conta do Databricks, configure as tabelas ou exibições que deseja sincronizar com o Braze.   
3. Crie uma nova integração no dashboard do Braze.  
4. Teste a integração e inicie a sincronização.

{% alert important %}
Pode haver de dois a cinco minutos de tempo de aquecimento quando a Braze se conectar às instâncias do SQL Classic e Pro, o que levará a postergações durante a configuração e o teste da conexão, bem como no início das sincronizações programadas. O uso de uma instância de SQL sem servidor minimizará o tempo de aquecimento e melhorará a taxa de transferência da consulta, mas poderá resultar em custos de integração ligeiramente mais altos.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. Crie uma entidade de serviço e permita o acesso ao espaço de trabalho do Fabric que será usado para sua integração.   
2. Em seu espaço de trabalho do Fabric, configure as tabelas ou exibições que deseja sincronizar com o Braze.   
3. Crie uma nova integração no dashboard do Braze.  
4. Teste a integração e inicie a sincronização.
{% endtab %}
{% endtabs %}

### Etapa 1: Configurar tabelas ou exibições

{% tabs %}
{% tab Snowflake %}

#### Etapa 1.1: Preparar a mesa

```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216),
     --If you include both email and phone, we will use the email as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

Você pode nomear o banco de dados, o esquema e a tabela como quiser, mas os nomes das colunas devem corresponder à definição anterior.

- `UPDATED_AT` - A hora em que essa linha foi atualizada ou adicionada à tabela. Sincronizaremos apenas as linhas que foram adicionadas ou atualizadas desde a última sincronização.
- **Colunas de identificador de usuário** \- Sua tabela pode conter uma ou mais colunas de identificador de usuário. Cada linha deve conter apenas um identificador (`external_id`, a combinação de `alias_name` e `alias_label`, `braze_id`, `email` ou `phone`). Uma tabela de origem pode ter colunas para um, dois, três, quatro ou todos os cinco tipos de identificadores.
    - `EXTERNAL_ID` - Isso identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado no Braze. 
    - `ALIAS_NAME` e `ALIAS_LABEL` \- Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário do Braze. Isso é gerado pelo SDK da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da ingestão de dados na nuvem. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário.
    - `EMAIL` - O endereço de e-mail do usuário. Se houver vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade para atualizações. Se você incluir e-mail e telefone, usaremos o e-mail como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se houver vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade nas atualizações. 
- `PAYLOAD` - Essa é uma string JSON dos campos que você deseja sincronizar com o usuário no Braze.

#### Etapa 1.2: Configurar a função e as permissões do banco de dados

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Atualize os nomes conforme necessário, mas as permissões devem corresponder ao exemplo anterior.

#### Etapa 1.3: Configurar warehouse e dar acesso à função na Braze

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
O depósito precisa ter o sinalizador de **retomada automática** ativado. Caso contrário, você precisará conceder à Braze privilégios adicionais `OPERATE` no warehouse para que possamos ativá-lo quando for o momento de executar a consulta.
{% endalert %}

#### Etapa 1.4: Configurar usuário

```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Após essa etapa, você compartilhará as informações de conexão com o Braze e receberá uma chave pública para anexar ao usuário.

{% alert note %}
Ao conectar diferentes espaços de trabalho à mesma conta do Snowflake, é necessário criar um usuário exclusivo para cada espaço de trabalho do Braze em que estiver criando uma integração. Em um espaço de trabalho, é possível reutilizar o mesmo usuário em todas as integrações, mas a criação da integração falhará se um usuário na mesma conta do Snowflake for duplicado em todos os espaços de trabalho.
{% endalert %}

#### Etapa 1.5: Permitir IPs do Braze na política de rede do Snowflake (opcional)

Dependendo da configuração de sua conta do Snowflake, talvez seja necessário permitir os seguintes endereços IP em sua política de rede do Snowflake. Para saber mais sobre como ativar isso, consulte a documentação relevante do Snowflake sobre a [modificação de uma política de rede](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### Etapa 1.1: Preparar a mesa 

Opcionalmente, configure um novo banco de dados e esquema para manter sua tabela de origem
```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
Crie uma tabela (ou visualização) para usar em sua integração CDI
```json
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, we will use the email as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

Você pode nomear o banco de dados, o esquema e a tabela como quiser, mas os nomes das colunas devem corresponder à definição anterior.

- `UPDATED_AT` - A hora em que essa linha foi atualizada ou adicionada à tabela. Sincronizaremos apenas as linhas que foram adicionadas ou atualizadas desde a última sincronização.
- **Colunas de identificador de usuário** \- Sua tabela pode conter uma ou mais colunas de identificador de usuário. Cada linha deve conter apenas um identificador (`external_id`, a combinação de `alias_name` e `alias_label`, `braze_id`, `email` ou `phone`). Uma tabela de origem pode ter colunas para um, dois, três, quatro ou todos os cinco tipos de identificadores.
    - `EXTERNAL_ID` - Isso identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado no Braze. 
    - `ALIAS_NAME` e `ALIAS_LABEL` \- Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário do Braze. Isso é gerado pelo SDK da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da ingestão de dados na nuvem. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário.
    - `EMAIL` - O endereço de e-mail do usuário. Se houver vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade para atualizações. Se você incluir e-mail e telefone, usaremos o e-mail como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se houver vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade nas atualizações. 
- `PAYLOAD` - Essa é uma string JSON dos campos que você deseja sincronizar com o usuário no Braze.
 
#### Etapa 1.2: Criar usuário e conceder permissões 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Essas são as permissões mínimas necessárias para esse usuário. Se estiver criando várias integrações CDI, talvez você queira conceder permissões a um esquema ou gerenciar as permissões usando um grupo. 

#### Etapa 1.3: Permitir acesso aos IPs do Braze

Se você tiver um firewall ou outras políticas de rede, deverá conceder à Braze acesso à rede para sua instância do Redshift. Um exemplo de ponto de extremidade de URL do Redshift é "example-cluster.ap-northeast-2.redshift.amazonaws.com".

Alguns aspectos importantes a saber:
- Também pode ser necessário alterar seus grupos de segurança para permitir que o Braze acesse seus dados no Redshift.
- Certifique-se de permitir explicitamente o tráfego de entrada nos IPs da tabela e na porta usada para consultar seu cluster Redshift (o padrão é 5439). Você deve permitir explicitamente a conectividade TCP do Redshift nessa porta, mesmo que as regras de entrada estejam definidas como "permitir tudo".
- O endpoint do cluster Redshift deve ser acessível publicamente para que o Braze se conecte ao seu cluster.
     - Se não quiser que o cluster do Redshift seja acessível publicamente, você pode configurar uma instância VPC e EC2 para usar um túnel SSH para acessar os dados do Redshift. Para saber mais, confira esta [postagem do Centro de Conhecimento da AWS](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine).
 
Permita o acesso dos seguintes IPs correspondentes à região de seu dashboard do Braze.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### Etapa 1.1: Preparar a mesa 

Opcionalmente, configure um novo projeto ou conjunto de dados para manter sua tabela de origem.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Crie uma ou mais tabelas para usar em sua integração CDI com os seguintes campos:

```json
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id, alias_name and alias_label, or braze_id is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, we will use the email as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| Nome do campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | OBRIGATÓRIO |
| `PAYLOAD`| JSON | OBRIGATÓRIO |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

Você pode nomear o projeto, o conjunto de dados e a tabela como quiser, mas os nomes das colunas devem corresponder à definição anterior.

- `UPDATED_AT` - A hora em que essa linha foi atualizada ou adicionada à tabela. Sincronizaremos apenas as linhas que foram adicionadas ou atualizadas desde a última sincronização.
- **Colunas de identificador de usuário** \- Sua tabela pode conter uma ou mais colunas de identificador de usuário. Cada linha deve conter apenas um identificador (`external_id`, a combinação de `alias_name` e `alias_label`, `braze_id`, `email` ou `phone`). Uma tabela de origem pode ter colunas para um, dois, três, quatro ou todos os cinco tipos de identificadores.
    - `EXTERNAL_ID` - Isso identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado no Braze. 
    - `ALIAS_NAME` e `ALIAS_LABEL` \- Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário do Braze. Isso é gerado pelo SDK da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da ingestão de dados na nuvem. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário.
    - `EMAIL` - O endereço de e-mail do usuário. Se houver vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade para atualizações. Se você incluir e-mail e telefone, usaremos o e-mail como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se houver vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade nas atualizações.
   e-mail varchar,
   phone_number varchar,
- `PAYLOAD` - Essa é uma string JSON dos campos que você deseja sincronizar com o usuário no Braze.

#### Etapa 1.2: Criar uma conta de serviço e conceder permissões 

Crie uma conta de serviço no GCP para o Braze usar para se conectar e ler dados de sua(s) tabela(s). A conta de serviço deve ter as permissões abaixo: 

- **Usuário de conexão do BigQuery:** Isso permitirá que a Braze faça conexões
- **Usuário do BigQuery:** Isso fornecerá acesso à Braze para executar consultas, ler metadados de conjuntos de dados e listar tabelas.
- **Visualizador de dados do BigQuery:** Isso fornecerá acesso à Braze para visualizar conjuntos de dados e seus conteúdos.
- **Usuário do BigQuery Job:** Isso fornecerá acesso ao Braze para executar trabalhos

Depois de criar a conta de serviço e conceder permissões, gere uma chave JSON. Para saber mais sobre como fazer isso [,](https://cloud.google.com/iam/docs/keys-create-delete) clique [aqui](https://cloud.google.com/iam/docs/keys-create-delete). Você atualizará isso para o dashboard da Braze mais tarde. 

#### Etapa 1.3: Permitir acesso aos IPs do Braze    

Se você tiver políticas de rede em vigor, deverá conceder à Braze acesso de rede à sua instância do Big Query. Permita o acesso dos IPs abaixo correspondentes à região de seu Braze dashboard.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### Etapa 1.1: Preparar a mesa 

Opcionalmente, configure um novo catálogo ou esquema para manter sua tabela de origem.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Crie uma ou mais tabelas para usar em sua integração CDI com os seguintes campos:


```json
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id, alias_name and alias_label, or braze_id is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, we will use the email as the primary identifier
  email STRING,
  phone STRING,
  payload STRING, STRUCT, or MAP
);
```


| Nome do campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | OBRIGATÓRIO |
| `PAYLOAD`| STRING, STRUCT ou MAP | OBRIGATÓRIO |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

Você pode nomear o esquema e a tabela como quiser, mas os nomes das colunas devem corresponder à definição anterior.

- `UPDATED_AT` - A hora em que essa linha foi atualizada ou adicionada à tabela. Sincronizaremos apenas as linhas que foram adicionadas ou atualizadas desde a última sincronização.
- **Colunas de identificador de usuário** \- Sua tabela pode conter uma ou mais colunas de identificador de usuário. Cada linha deve conter apenas um identificador (`external_id`, a combinação de `alias_name` e `alias_label`, `braze_id`, `email` ou `phone`). Uma tabela de origem pode ter colunas para um, dois, três, quatro ou todos os cinco tipos de identificadores.
    - `EXTERNAL_ID` - Isso identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado no Braze. 
    - `ALIAS_NAME` e `ALIAS_LABEL` \- Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário do Braze. Isso é gerado pelo SDK da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da ingestão de dados na nuvem. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário. 
    - `EMAIL` - O endereço de e-mail do usuário. Se houver vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade para atualizações. Se você incluir e-mail e telefone, usaremos o e-mail como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se houver vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade nas atualizações. 
- `PAYLOAD` - Essa é uma string ou struct dos campos que você deseja sincronizar com o usuário no Braze.

#### Etapa 1.2: Criar um token de acesso  

Para que o Braze acesse o Databricks, é necessário criar um token de acesso pessoal.

1. No seu espaço de trabalho do Databricks, selecione seu nome de usuário do Databricks na barra superior e, em seguida, selecione **Configurações do usuário** no menu suspenso.
2. Na guia Tokens de acesso, selecione **Gerar novo token**.
3. Digite um comentário que o ajude a identificar esse token, como "Braze CDI", e altere o tempo de vida do token para nenhum tempo de vida, deixando a caixa Tempo de vida (dias) vazia (em branco).
4. Selecione **Generate (Gerar**).
5. Copie o token exibido e, em seguida, selecione **Concluído**.

Mantenha o token em um local seguro até que seja necessário inseri-lo no dashboard do Braze durante a etapa de criação de credenciais.

#### Etapa 1.3: Permitir acesso aos IPs do Braze    

Se você tiver políticas de rede em vigor, deverá conceder à Braze acesso de rede à sua instância do Databricks. Permita o acesso dos IPs abaixo correspondentes à região de seu Braze dashboard.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### Etapa 1.1: Configurar a entidade de serviço e conceder acesso
O Braze se conectará ao seu armazém Fabric usando uma entidade de serviço com autenticação Entra ID. Você criará uma nova entidade de serviço para o Braze usar e concederá acesso aos recursos do Fabric conforme necessário. O Braze precisará dos seguintes detalhes para se conectar:    

* ID do locatário (também chamado de diretório) para sua conta do Azure 
* ID da entidade principal (também chamada de ID do aplicativo) para a entidade principal do serviço 
* Segredo do cliente para autenticação do Braze

1. No portal do Azure, navegue até o centro de administração do Microsoft Entra e, em seguida, Registros de app 
2. Selecione **\+ Novo registro** em **Identidade** > **Aplicativos** > **Registros de app**.
3. Digite um nome e selecione `Accounts in this organizational directory only` como o tipo de conta compatível. Em seguida, selecione **Registrar**. 
4. Selecione o aplicativo (service principal) que acabou de criar e navegue até **Certificados e segredos** > **\+ Novo segredo de cliente**.
5. Digite uma descrição para o segredo e defina um período de vencimento para o segredo. Em seguida, selecione **Adicionar**. 
6. Note o segredo do cliente criado para ser usado na configuração do Braze. 

{% alert note %}
O Azure não permite o vencimento ilimitado dos segredos da entidade de serviço. Lembre-se de atualizar as credenciais antes que elas expirem para manter o fluxo de dados para o Braze.
{% endalert %}

#### Etapa 1.2: Conceder acesso aos recursos do Fabric 
Você fornecerá acesso para que o Braze se conecte à sua instância do Fabric. No seu portal de administração do Fabric, navegue até **Configurações** > **Governança e insights** > **Portal de administração** > **Configurações do locatário**.    

* Nas **configurações do desenvolvedor**, ative a opção "Service principals can use Fabric APIs" para que o Braze possa se conectar usando o Microsoft Entra ID.
* Nas **configurações do OneLake**, ative a opção "Users can access data stored in OneLake with apps external to Fabric" para que o principal do serviço possa acessar os dados de um app externo.


#### Etapa 1.3: Preparar a mesa
O Braze oferece suporte a tabelas e exibições em Fabric Warehouses. Se precisar criar um novo data warehouse, acesse **Criar > Data Warehouse > Warehouse** no console Fabric. 

```json
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
  --If you include both email and phone, we will use the email as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

Você pode nomear o depósito, o esquema e a tabela ou visualização como quiser, mas os nomes das colunas devem corresponder à definição anterior.

- `UPDATED_AT` - A hora em que essa linha foi atualizada ou adicionada à tabela. Sincronizaremos apenas as linhas que foram adicionadas ou atualizadas desde a última sincronização.
- **Colunas de identificador de usuário** \- Sua tabela pode conter uma ou mais colunas de identificador de usuário. Cada linha deve conter apenas um identificador (`external_id`, a combinação de `alias_name` e `alias_label`, `braze_id`, `email` ou `phone`). Uma tabela de origem pode ter colunas para um, dois, três, quatro ou todos os cinco tipos de identificadores.
    - `EXTERNAL_ID` - Isso identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado no Braze. 
    - `ALIAS_NAME` e `ALIAS_LABEL` \- Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário do Braze. Isso é gerado pelo SDK da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da ingestão de dados na nuvem. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário.
    - `EMAIL` - O endereço de e-mail do usuário. Se houver vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade para atualizações. Se você incluir e-mail e telefone, usaremos o e-mail como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se houver vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade nas atualizações. 
- `PAYLOAD` - Essa é uma string JSON dos campos que você deseja sincronizar com o usuário no Braze.


#### Etapa 1.4: Obter a string de conexão do warehouse 
Você precisará do endpoint SQL do seu depósito para que o Braze possa se conectar. Para recuperar isso, acesse o **espaço de trabalho** no Fabric e, na lista de itens, passe o mouse sobre o nome do depósito e selecione **Copiar string de conexão SQL**.

![A página "Fabric Console" no Microsoft Azure, onde os usuários devem recuperar a string de conexão do SQL.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### Etapa 1.5: Permitir IPs do Braze no firewall (opcional)

Dependendo da configuração de sua conta Microsoft Fabric, talvez seja necessário permitir os seguintes endereços IP em seu firewall para permitir o tráfego do Braze. Para saber mais sobre como ativar esse recurso, consulte a documentação relevante sobre o [Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Etapa 2: Crie uma nova integração no dashboard do Braze

{% tabs %}
{% tab Snowflake %}

No Braze Dashbord, vá para **Configurações de dados** > **Ingestão de dados na nuvem**, selecione **Criar nova sincronização de dados** e, em seguida, selecione **Importação do Snowflake**.

#### Etapa 2.1: Adicionar informações de conexão do Snowflake e tabela de origem

Insira as informações de seu data warehouse do Snowflake e da tabela de origem e, em seguida, prossiga para a próxima etapa.

![A página "Create new import sync" (Criar nova sincronização de importação) do Snowflake no dashboard do Braze com os dados de exemplo inseridos na etapa 1: Configurar conexão.]({% image_buster /assets/img/cloud_ingestion/ingestion_1.png %})

#### Etapa 2.2: Configurar detalhes de sincronização

Em seguida, escolha um nome para sua sincronização e insira os e-mails dos contatos. Usaremos essas informações de contato para notificá-lo sobre quaisquer erros de integração, como a remoção inesperada do acesso à tabela.

Os e-mails de contato receberão apenas notificações de erros globais ou de nível de sincronização, como tabelas ausentes, permissões e outros. Eles não receberão edições em nível de linha. Os erros globais indicam problemas críticos com a conexão que impedem a execução das sincronizações. Esses problemas podem incluir o seguinte:

- Problemas de conectividade
- Falta de recursos
- Problemas de permissões
- (Somente para sincronizações de catálogos) A camada do catálogo está sem espaço

![A página "Create new import sync" (Criar nova sincronização de importação) do Snowflake no dashboard do Braze com os dados de exemplo inseridos na etapa 2: Configurar informações da sincronização.]({% image_buster /assets/img/cloud_ingestion/ingestion_2.png %})

Você também escolherá o tipo de dados e a frequência de sincronização. A frequência pode variar de cada 15 minutos a uma vez por mês. Usaremos o fuso horário configurado em seu dashboard do Braze para agendar a sincronização recorrente. Os tipos de dados compatíveis são Atributos personalizados, Eventos personalizados e Eventos de compra, e o tipo de dados de uma sincronização não pode ser alterado após a criação. 

#### Adicione uma chave pública ao usuário do Braze

Nesse ponto, você deve voltar ao Snowflake para concluir a configuração. Adicione a chave pública exibida no dashboard ao usuário que você criou para que o Braze se conecte ao Snowflake.

Para obter mais informações sobre como fazer isso, consulte a [documentação do Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Se você quiser alternar as chaves a qualquer momento, podemos gerar um novo par de chaves e fornecer a você a nova chave pública.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```
{% endtab %}
{% tab Redshift %}

No Braze Dashbord, acesse **Configurações de dados** > **Ingestão de dados na nuvem**, selecione **Criar nova sincronização de dados** e, em seguida, selecione **Importação do Amazon Redshift**.

#### Etapa 2.1: Adicionar informações de conexão e tabela de origem do Redshift

Insira as informações de seu data warehouse Redshift e da tabela de origem. Se estiver usando um túnel de rede privada, alterne o controle deslizante e insira as informações do túnel. Em seguida, prossiga para a próxima etapa.

![A página "Criar nova sincronização de importação" para o Redshift no dashboard do Braze, definida como Etapa 1: Configurar conexão.]({% image_buster /assets/img/cloud_ingestion/ingestion_6.png %})

#### Etapa 2.2: Configurar detalhes de sincronização

Em seguida, escolha um nome para sua sincronização e insira os e-mails dos contatos. Usaremos essas informações de contato para notificá-lo sobre quaisquer erros de integração, como a remoção inesperada do acesso à tabela.

Os e-mails de contato receberão apenas notificações de erros globais ou de nível de sincronização, como tabelas ausentes, permissões e outros. Eles não receberão edições em nível de linha. Os erros globais indicam problemas críticos com a conexão que impedem a execução das sincronizações. Esses problemas podem incluir o seguinte:

- Problemas de conectividade
- Falta de recursos
- Problemas de permissões
- (Somente para sincronizações de catálogos) A camada do catálogo está sem espaço

![A página "Criar nova sincronização de importação" para Redshift no dashboard do Braze com alguns dados de exemplo adicionados à etapa 2: Configurar informações da sincronização.]({% image_buster /assets/img/cloud_ingestion/ingestion_7.png %})

Você também escolherá o tipo de dados e a frequência de sincronização. A frequência pode variar de cada 15 minutos a uma vez por mês. Usaremos o fuso horário configurado em seu dashboard do Braze para agendar a sincronização recorrente. Os tipos de dados compatíveis são Atributos personalizados, Eventos personalizados e Eventos de compra, e o tipo de dados de uma sincronização não pode ser alterado após a criação.
{% endtab %}
{% tab BigQuery %}

No Braze Dashbord, acesse **Configurações de dados** > **Ingestão de dados na nuvem**, selecione **Criar nova sincronização de dados** e, em seguida, selecione **Importação do Google BigQuery**.

#### Etapa 2.1: Adicionar informações de conexão do BigQuery e tabela de origem

Faça upload da chave JSON e forneça um nome para a conta de serviço e, em seguida, insira os detalhes de sua tabela de origem.

![A página "Criar nova sincronização de importação" para o Redshift no dashboard do Braze, definida como Etapa 1: Configurar conexão.]({% image_buster /assets/img/cloud_ingestion/ingestion_11.png %})

#### Etapa 2.2: Configurar detalhes de sincronização

Em seguida, escolha um nome para sua sincronização e insira os e-mails dos contatos. Usaremos essas informações de contato para notificá-lo sobre quaisquer erros de integração, como a remoção inesperada do acesso à tabela.

Os e-mails de contato receberão apenas notificações de erros globais ou de nível de sincronização, como tabelas ausentes, permissões e outros. Eles não receberão edições em nível de linha. Os erros globais indicam problemas críticos com a conexão que impedem a execução das sincronizações. Esses problemas podem incluir o seguinte:

- Problemas de conectividade
- Falta de recursos
- Problemas de permissões
- (Somente para sincronizações de catálogos) A camada do catálogo está sem espaço

![A página "Criar nova sincronização de importação" para o Redshift no dashboard do Braze, definida como Etapa 2: Configurar informações da sincronização.]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

Você também escolherá o tipo de dados e a frequência de sincronização. A frequência pode variar de cada 15 minutos a uma vez por mês. Usaremos o fuso horário configurado em seu dashboard do Braze para agendar a sincronização recorrente. Os tipos de dados suportados são Atributos personalizados, Eventos personalizados, Eventos de compra e Exclusões de usuários. O tipo de dados de uma sincronização não pode ser alterado após a criação. 

{% endtab %}
{% tab Databricks %}

No Braze Dashbord, acesse **Configurações de dados** > **Ingestão de dados na nuvem**, selecione **Criar nova sincronização de dados** e, em seguida, selecione **Importação do Databricks**.

#### Etapa 2.1: Adicionar informações de conexão e tabela de origem do Databricks

Insira as informações do data warehouse e da tabela de origem do Databricks e prossiga para a próxima etapa.

![A página "Criar nova sincronização de importação" para o Redshift no dashboard do Braze, definida como Etapa 1: Configurar conexão.]({% image_buster /assets/img/cloud_ingestion/ingestion_16.png %})

#### Etapa 2.2: Configurar detalhes de sincronização

Em seguida, escolha um nome para sua sincronização e insira os e-mails dos contatos. Usaremos essas informações de contato para notificá-lo sobre quaisquer erros de integração, como a remoção inesperada do acesso à tabela.

Os e-mails de contato receberão apenas notificações de erros globais ou de nível de sincronização, como tabelas ausentes, permissões e outros. Eles não receberão edições em nível de linha. Os erros globais indicam problemas críticos com a conexão que impedem a execução das sincronizações. Esses problemas podem incluir o seguinte:

- Problemas de conectividade
- Falta de recursos
- Problemas de permissões
- (Somente para sincronizações de catálogos) A camada do catálogo está sem espaço

![A página "Criar nova sincronização de importação" para o Redshift no dashboard do Braze, definida como Etapa 2: Configurar informações da sincronização.]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

Você também escolherá o tipo de dados e a frequência de sincronização. A frequência pode variar de cada 15 minutos a uma vez por mês. Usaremos o fuso horário configurado em seu dashboard do Braze para agendar a sincronização recorrente. Os tipos de dados suportados são atributos personalizados, eventos personalizados, eventos de compra e exclusões de usuários. O tipo de dados de uma sincronização não pode ser alterado após a criação. 

{% endtab %}
{% tab Microsoft Fabric %}

#### Etapa 2.1: Configurar uma sincronização de ingestão de dados na nuvem

Você criará uma nova sincronização de dados para o Microsoft Fabric. No painel do Braze, acesse **Configurações de dados** > **Ingestão de dados na nuvem**, selecione **Criar nova sincronização de dados** e, em seguida, selecione **Importação do Microsoft Fabric**.

#### Etapa 2.2: Adicionar informações de conexão e tabela de origem do Microsoft Fabric

Insira as informações de suas credenciais do Microsoft Fabric warehouse e da tabela de origem e prossiga para a próxima etapa.

- Credentials Name é um rótulo para essas credenciais no Braze, você pode definir um valor útil aqui
- Consulte as etapas na seção 1 para obter detalhes sobre como recuperar o Tenant ID, o Principal ID, o Client Secret e a Connection String

![A página "Criar nova sincronização de importação" para o Redshift no dashboard do Braze, definida como Etapa 1: Configurar conexão.]({% image_buster /assets/img/cloud_ingestion/fabric_setup_1.png %})

#### Etapa 2.3: Configurar detalhes de sincronização

Em seguida, configure os seguintes detalhes para sua sincronização: 

- Nome da sincronização 
- Tipo de dados - Os tipos de dados suportados são atributos personalizados, eventos personalizados, eventos de compra, catálogos e exclusões de usuários. O tipo de dados de uma sincronização não pode ser alterado após a criação. 
- Frequência de sincronização - A frequência pode variar de cada 15 minutos a uma vez por mês. Usaremos o fuso horário configurado em seu dashboard do Braze para agendar a sincronização recorrente. 
  - As sincronizações não recorrentes podem ser disparadas manualmente ou por meio da [API]({{site.baseurl}}/api/endpoints/cdi) 

![A página "Criar nova sincronização de importação" do Microsoft Fabric no dashboard do Braze, definida como Etapa 2: Configurar informações da sincronização.]({% image_buster /assets/img/cloud_ingestion/fabric_setup_2.png %})


#### Etapa 2.4: Configurar preferências de notificação

Em seguida, insira os e-mails de contato. Usaremos essas informações de contato para notificá-lo sobre quaisquer erros de integração, como remoção inesperada de acesso à tabela, ou alertar quando linhas específicas não forem atualizadas.

Por padrão, os e-mails de contato receberão apenas notificações de erros globais ou de nível de sincronização, como tabelas ausentes, permissões e outros. Os erros globais indicam problemas críticos com a conexão que impedem a execução das sincronizações. Esses problemas podem incluir o seguinte:

- Problemas de conectividade
- Falta de recursos
- Problemas de permissões
- (Somente para sincronizações de catálogos) A camada do catálogo está sem espaço

Você também pode configurar alertas para problemas no nível da linha ou optar por receber um alerta sempre que uma sincronização for executada com êxito. 

![A página "Criar nova sincronização de importação" do Microsoft Fabric no dashboard do Braze, definida como Etapa 3: Configure preferências de notificação.]({% image_buster /assets/img/cloud_ingestion/fabric_setup_3.png %})


{% endtab %}

{% endtabs %}

### Etapa 3: Conexão de teste

{% tabs %}
{% tab Snowflake %}

Retorne ao dashboard do Braze e selecione **Testar conexão**. Se for bem-sucedido, você verá uma prévia dos dados. Se, por algum motivo, não conseguirmos nos conectar, exibiremos uma mensagem de erro para ajudá-lo a solucionar o problema.

![A página "Criar nova sincronização de importação" para o Snowflake no dashboard do Braze com a etapa 3: "Test connection" (Teste de conexão) exibindo uma chave pública RSA.]({% image_buster /assets/img/cloud_ingestion/ingestion_3.png %})
{% endtab %}

{% tab Redshift %}
{% subtabs local %}
{% subtab Public Network %}
Retorne ao dashboard do Braze e selecione **Testar conexão**. Se for bem-sucedido, você verá uma prévia dos dados. Se, por algum motivo, não conseguirmos nos conectar, exibiremos uma mensagem de erro para ajudá-lo a solucionar o problema.

![A página "Criar nova sincronização de importação" para o Redshift no dashboard do Braze, definida como Etapa 3: Testar conexão.]({% image_buster /assets/img/cloud_ingestion/ingestion_8.png %})
{% endsubtab %}

{% subtab Private Network %}
Retorne ao dashboard do Braze e selecione **Testar conexão**. Se for bem-sucedido, você verá uma prévia dos dados. Se, por algum motivo, não conseguirmos nos conectar, exibiremos uma mensagem de erro para ajudá-lo a solucionar o problema.

![A página "Create new import sync" (Criar nova sincronização de importação) para a Redshift Private Network no dashboard do Braze, com a etapa 4: "Test connection" (Teste de conexão) exibindo uma chave pública RSA.]({% image_buster /assets/img/cloud_ingestion/ingestion_19.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab BigQuery %}

Depois que todos os detalhes de configuração de sua sincronização forem inseridos, selecione **Testar conexão**. Se for bem-sucedido, você verá uma prévia dos dados. Se, por algum motivo, não conseguirmos nos conectar, exibiremos uma mensagem de erro para ajudá-lo a solucionar o problema.

![A página "Criar nova sincronização de importação" para o Redshift no dashboard do Braze, definida como Etapa 3: Testar conexão.]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}

{% tab Databricks %}

Depois que todos os detalhes de configuração de sua sincronização forem inseridos, selecione **Testar conexão**. Se for bem-sucedido, você verá uma prévia dos dados. Se, por algum motivo, não conseguirmos nos conectar, exibiremos uma mensagem de erro para ajudá-lo a solucionar o problema.

![A página "Criar nova sincronização de importação" para o Redshift no dashboard do Braze, definida como Etapa 3: Testar conexão.]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}
{% tab Microsoft Fabric %}

Depois que todos os detalhes de configuração de sua sincronização forem inseridos, selecione **Testar conexão**. Se for bem-sucedido, você verá uma prévia dos dados. Se, por algum motivo, não conseguirmos nos conectar, exibiremos uma mensagem de erro para ajudá-lo a solucionar o problema.

![A página "Criar nova sincronização de importação" do Microsoft Fabric no dashboard do Braze, definida como Etapa 4: Testar conexão.]({% image_buster /assets/img/cloud_ingestion/fabric_setup_4.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Você deve testar com êxito uma integração antes que ela possa passar do estado Rascunho para o estado Ativo. Se você precisar sair da página de criação, sua integração será salva e você poderá acessar novamente a página de detalhes para fazer alterações e testes.  
{% endalert %}

## Configure integrações ou usuários adicionais (opcional)

{% tabs %}
{% tab Snowflake %}
Você pode configurar várias integrações com o Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à conta do Snowflake.

![A página "Create new import sync" (Criar nova sincronização de importação) do Snowflake no dashboard do Braze, com o menu suspenso "Select credentials" (Selecionar credenciais) aberto na etapa 1: Configurar conexão.]({% image_buster /assets/img/cloud_ingestion/ingestion_4.png %})

Se você reutilizar o mesmo usuário e função em todas as integrações, **não** precisará passar pela etapa de adicionar a chave pública novamente.
{% endtab %}
{% tab Redshift %}
Você pode configurar várias integrações com o Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do Snowflake ou do Redshift.

![A página "Create new import sync" (Criar nova sincronização de importação) do Snowflake no dashboard do Braze, com o menu suspenso "Select credentials" (Selecionar credenciais) aberto na etapa 1: Configurar conexão.]({% image_buster /assets/img/cloud_ingestion/ingestion_9.png %})

Se você reutilizar o mesmo usuário em várias integrações, não será possível excluir o usuário no dashboard do Braze até que ele seja removido de todas as sincronizações ativas.
{% endtab %}
{% tab BigQuery %}

Você pode configurar várias integrações com o Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do BigQuery.

![A página "Create new import sync" (Criar nova sincronização de importação) do Snowflake no dashboard do Braze, com o menu suspenso "Select credentials" (Selecionar credenciais) aberto na etapa 1: Configurar conexão.]({% image_buster /assets/img/cloud_ingestion/ingestion_14.png %})

Se você reutilizar o mesmo usuário em várias integrações, não será possível excluir o usuário no dashboard do Braze até que ele seja removido de todas as sincronizações ativas.

{% endtab %}
{% tab Databricks %}

Você pode configurar várias integrações com o Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do Databricks.

![A página "Create new import sync" (Criar nova sincronização de importação) do Snowflake no dashboard do Braze, com o menu suspenso "Select credentials" (Selecionar credenciais) aberto na etapa 1: Configurar conexão.]({% image_buster /assets/img/cloud_ingestion/ingestion_17.png %})

Se você reutilizar o mesmo usuário em várias integrações, não será possível excluir o usuário no dashboard do Braze até que ele seja removido de todas as sincronizações ativas.

{% endtab %}
{% tab Microsoft Fabric %}

Você pode configurar várias integrações com o Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do Fabric.

Se você reutilizar o mesmo usuário em várias integrações, não será possível excluir o usuário no dashboard do Braze até que ele seja removido de todas as sincronizações ativas.

{% endtab %}
{% endtabs %}

## Executando a sincronização

{% tabs %}
{% tab Snowflake %}
Quando ativada, sua sincronização será executada de acordo com a programação configurada durante a instalação. Se você quiser executar a sincronização fora da programação normal de testes ou buscar os dados mais recentes, selecione **Sync Now (Sincronizar agora**). Essa execução não afetará as sincronizações futuras programadas regularmente.

![A página "Data Import" (Importação de dados) do Snowflake no dashboard do Braze exibe a opção "Sync now" (Sincronizar agora) no menu de elipses verticais.]({% image_buster /assets/img/cloud_ingestion/ingestion_5.png %})

{% endtab %}
{% tab Redshift %}
Quando ativada, sua sincronização será executada de acordo com a programação configurada durante a instalação. Se você quiser executar a sincronização fora da programação normal de testes ou buscar os dados mais recentes, selecione **Sync Now (Sincronizar agora**). Essa execução não afetará as sincronizações futuras programadas regularmente.

![A página "Data Import" (Importação de dados) do Snowflake no dashboard do Braze exibe a opção "Sync now" (Sincronizar agora) no menu de elipses verticais.]({% image_buster /assets/img/cloud_ingestion/ingestion_10.png %})

{% endtab %}
{% tab BigQuery %}

Quando ativada, sua sincronização será executada de acordo com a programação configurada durante a instalação. Se você quiser executar a sincronização fora da programação normal de testes ou buscar os dados mais recentes, selecione **Sync Now (Sincronizar agora**). Essa execução não afetará as sincronizações futuras programadas regularmente.

![A página "Data Import" (Importação de dados) do Snowflake no dashboard do Braze exibe a opção "Sync now" (Sincronizar agora) no menu de elipses verticais.]({% image_buster /assets/img/cloud_ingestion/ingestion_15.png %})

{% endtab %}
{% tab Databricks %}

Quando ativada, sua sincronização será executada de acordo com a programação configurada durante a instalação. Se você quiser executar a sincronização fora da programação normal de testes ou buscar os dados mais recentes, selecione **Sync Now (Sincronizar agora**). Essa execução não afetará as sincronizações futuras programadas regularmente.

![A página "Data Import" (Importação de dados) do Snowflake no dashboard do Braze exibe a opção "Sync now" (Sincronizar agora) no menu de elipses verticais.]({% image_buster /assets/img/cloud_ingestion/ingestion_18.png %})

{% endtab %}
{% tab Microsoft Fabric %}

Quando ativada, sua sincronização será executada de acordo com a programação configurada durante a instalação. Se você quiser executar a sincronização fora da programação normal de testes ou buscar os dados mais recentes, selecione **Sync Now (Sincronizar agora**). Essa execução não afetará as sincronizações futuras programadas regularmente.

{% endtab %}

{% endtabs %}

