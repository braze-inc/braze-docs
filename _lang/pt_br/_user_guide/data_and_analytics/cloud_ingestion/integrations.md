---
nav_title: Integrações de data warehouse
article_title: Integrações de data warehouse
description: "Este artigo de referência aborda como usar a ingestão de dados do Braze Cloud para sincronizar dados relevantes com sua integração do Snowflake, Redshift, BigQuery e Databricks."
page_order: 2
page_type: reference

---

# Integrações de armazenamento de data warehouse

> Este artigo aborda como usar aiIngestão de dados para nuvem da Braze (CDI) para sincronizar dados relevantes com sua integração do Snowflake, Redshift, BigQuery e Databricks.

## Configuração do produto

As integrações de ingestão de dados na nuvem exigem algumas configurações no lado da Braze e em sua instância. Siga estas etapas para configurar a integração:

{% tabs %}
{% tab Snowflake %}
1. Em sua instância do Snowflake, configure a(s) tabela(s) ou visualização(ões) que deseja sincronizar com o Braze.
2. Crie uma nova integração no dashboard do Braze.
3. Recupere a chave pública fornecida no dashboard da Braze e [anexe-a ao usuário do Snowflake para autenticação](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Teste a integração e inicie a sincronização.
{% endtab %}
{% tab Redshift %}
1. Certifique-se de que o acesso do Braze seja permitido às tabelas do Redshift que você deseja sincronizar. O Braze se conectará ao Redshift pela Internet.
2. Em sua instância do Redshift, configure a(s) tabela(s) ou visualização(ões) que deseja sincronizar com o Braze.
3. Crie uma nova integração no dashboard do Braze.
4. Teste a integração e inicie a sincronização.
{% endtab %}
{% tab BigQuery %}
1. Crie uma conta de serviço e permita o acesso ao(s) projeto(s) e conjunto(s) de dados do BigQuery que contêm os dados que você deseja sincronizar.  
2. Em sua conta do BigQuery, configure a(s) tabela(s) ou visualização(ões) que deseja sincronizar com o Braze.   
3. Crie uma nova integração no dashboard do Braze.  
4. Teste a integração e inicie a sincronização.  
{% endtab %}
{% tab Databricks %}
1. Crie uma conta de serviço e permita o acesso ao(s) projeto(s) e conjunto(s) de dados do Databricks que contêm os dados que você deseja sincronizar.  
2. Em sua conta do Databricks, configure a(s) tabela(s) ou visualização(ões) que deseja sincronizar com o Braze.   
3. Crie uma nova integração no dashboard do Braze.  
4. Teste a integração e inicie a sincronização.

{% alert important %}
Pode haver de dois a cinco minutos de tempo de aquecimento quando a Braze se conectar às instâncias do SQL Classic e Pro, o que levará a postergações durante a configuração e o teste da conexão, bem como no início das sincronizações programadas. O uso de uma instância de SQL sem servidor minimizará o tempo de aquecimento e melhorará a taxa de transferência da consulta, mas poderá resultar em custos de integração ligeiramente mais altos.
{% endalert %}

{% endtab %}
{% endtabs %}

### Etapa 1: Configurar tabelas ou exibições

{% tabs %}
{% tab Snowflake %}

#### Etapa 1: Preparar a mesa

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
- **Colunas de identificador de usuário** \- Sua tabela pode conter uma ou mais colunas de identificador de usuário. Cada linha deve conter apenas um identificador: `external_id`, a combinação de `alias_name` e `alias_label`, ou `braze_id`. Uma tabela de origem pode conter colunas para um, dois ou todos os três tipos de identificadores. 
    - `EXTERNAL_ID` - Isso identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado no Braze. 
    - `ALIAS_NAME` e `ALIAS_LABEL` \- Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário do Braze. Isso é gerado pelo SDK da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da ingestão de dados na nuvem. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário.
    - `EMAIL` - O endereço de e-mail do usuário. Se houver vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade para atualizações. Se você incluir e-mail e telefone, usaremos o e-mail como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se houver vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade nas atualizações. 
- `PAYLOAD` - Essa é uma string JSON dos campos que você deseja sincronizar com o usuário no Braze.

#### Etapa 2: Configurar a função e as permissões do banco de dados

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Atualize os nomes conforme necessário, mas as permissões devem corresponder ao exemplo anterior.

#### Etapa 3: Configurar warehouse e dar acesso à função na Braze

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
O depósito precisará ter o sinalizador de **retomada automática** ativado. Caso contrário, você precisará conceder à Braze privilégios adicionais `OPERATE` no warehouse para que possamos ativá-lo quando for o momento de executar a consulta.
{% endalert %}

#### Etapa 4: Configurar usuário

```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Após essa etapa, você compartilhará as informações de conexão com o Braze e receberá uma chave pública para anexar ao usuário.

{% alert note %}
Ao conectar diferentes espaços de trabalho à mesma conta do Snowflake, é necessário criar um usuário exclusivo para cada espaço de trabalho do Braze em que estiver criando uma integração. Em um espaço de trabalho, é possível reutilizar o mesmo usuário em todas as integrações, mas a criação da integração falhará se um usuário na mesma conta do Snowflake for duplicado em todos os espaços de trabalho.
{% endalert %}

#### Etapa 5: Permitir IPs do Braze na política de rede do Snowflake (opcional)

Dependendo da configuração de sua conta do Snowflake, talvez seja necessário permitir os seguintes endereços IP em sua política de rede do Snowflake. Para saber mais sobre como ativar isso, consulte a documentação relevante do Snowflake sobre a [modificação de uma política de rede](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

| Para as instâncias `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07` | Para as instâncias `EU-01` e `EU-02` |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`
{% endtab %}
{% tab Redshift %}

#### Etapa 1: Preparar a mesa 

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
- Colunas de identificador de usuário. Sua tabela pode conter uma ou mais colunas de identificador de usuário. Cada linha deve conter apenas um identificador ( `external_id`, a combinação de `alias_name` e `alias_label`, ou `braze_id`. Uma tabela de origem pode conter colunas para um, dois ou todos os três tipos de identificadores. 
    - `EXTERNAL_ID` - Isso identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado no Braze. 
    - `ALIAS_NAME` e `ALIAS_LABEL` \- Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário do Braze. Isso é gerado pelo SDK da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da ingestão de dados na nuvem. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário.
    - `EMAIL` - O endereço de e-mail do usuário. Se houver vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade para atualizações. Se você incluir e-mail e telefone, usaremos o e-mail como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se houver vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade nas atualizações. 
- `PAYLOAD` - Essa é uma string JSON dos campos que você deseja sincronizar com o usuário no Braze.
 
#### Etapa 2: Criar usuário e conceder permissões 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Essas são as permissões mínimas necessárias para esse usuário. Se estiver criando várias integrações CDI, talvez você queira conceder permissões a um esquema ou gerenciar as permissões usando um grupo. 

#### Etapa 3: Permitir acesso aos IPs do Braze

Se você tiver um firewall ou outras políticas de rede, deverá conceder à Braze acesso à rede para sua instância do Redshift. Um exemplo de ponto de extremidade de URL do Redshift é "example-cluster.ap-northeast-2.redshift.amazonaws.com".

Alguns aspectos importantes a saber:
- Também pode ser necessário alterar seus grupos de segurança para permitir que o Braze acesse seus dados no Redshift.
- Certifique-se de permitir explicitamente o tráfego de entrada nos IPs da tabela e na porta usada para consultar seu cluster Redshift (o padrão é 5439). Você deve permitir explicitamente a conectividade TCP do Redshift nessa porta, mesmo que as regras de entrada estejam definidas como "permitir tudo".
- O endpoint do cluster Redshift deve ser acessível publicamente para que o Braze se conecte ao seu cluster.
     - Se não quiser que o cluster do Redshift seja acessível publicamente, você pode configurar uma instância VPC e EC2 para usar um túnel SSH para acessar os dados do Redshift. Para saber mais, confira esta [postagem do Centro de Conhecimento da AWS](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine).
 
Permita o acesso dos seguintes IPs correspondentes à região de seu dashboard do Braze.

| Para as instâncias `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07` | Para as instâncias `EU-01` e `EU-02` |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`
{% endtab %}
{% tab BigQuery %}

#### Etapa 1: Preparar a mesa 

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
- Colunas de identificador de usuário. Sua tabela pode conter uma ou mais colunas de identificador de usuário. Cada linha deve conter apenas um identificador: `external_id`, a combinação de `alias_name` e `alias_label`, ou `braze_id`. Uma tabela de origem pode conter colunas para um, dois ou todos os três tipos de identificadores. 
    - `EXTERNAL_ID` - Isso identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado no Braze. 
    - `ALIAS_NAME` e `ALIAS_LABEL` \- Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário do Braze. Isso é gerado pelo SDK da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da ingestão de dados na nuvem. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário.
    - `EMAIL` - O endereço de e-mail do usuário. Se houver vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade para atualizações. Se você incluir e-mail e telefone, usaremos o e-mail como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se houver vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade nas atualizações.
   e-mail varchar,
   phone_number varchar,
- `PAYLOAD` - Essa é uma string JSON dos campos que você deseja sincronizar com o usuário no Braze.

#### Etapa 2: Criar uma conta de serviço e conceder permissões 

Crie uma conta de serviço no GCP para o Braze usar para se conectar e ler dados de sua(s) tabela(s). A conta de serviço deve ter as permissões abaixo: 

- **Usuário de conexão do BigQuery:** Isso permitirá que a Braze faça conexões
- **Usuário do BigQuery:** Isso fornecerá acesso à Braze para executar consultas, ler metadados de conjuntos de dados e listar tabelas.
- **Visualizador de dados do BigQuery:** Isso fornecerá acesso à Braze para visualizar conjuntos de dados e seus conteúdos.
- **Usuário do BigQuery Job:** Isso fornecerá acesso ao Braze para executar trabalhos

Depois de criar a conta de serviço e conceder permissões, gere uma chave JSON. Para saber mais sobre como fazer isso [,](https://cloud.google.com/iam/docs/keys-create-delete) clique [aqui](https://cloud.google.com/iam/docs/keys-create-delete). Você atualizará isso para o dashboard da Braze mais tarde. 

#### Etapa 3: Permitir acesso aos IPs do Braze    

Se você tiver políticas de rede em vigor, deverá conceder à Braze acesso de rede à sua instância do Big Query. Permita o acesso dos IPs abaixo correspondentes à região de seu Braze dashboard.  

| Para as instâncias `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07` | Para as instâncias `EU-01` e `EU-02` |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`

{% endtab %}
{% tab Databricks %}

#### Etapa 1: Preparar a mesa 

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
  payload STRING
);
```


| Nome do campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | OBRIGATÓRIO |
| `PAYLOAD`| STRING ou STRUCT | OBRIGATÓRIO |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

Você pode nomear o esquema e a tabela como quiser, mas os nomes das colunas devem corresponder à definição anterior.

- `UPDATED_AT` - A hora em que essa linha foi atualizada ou adicionada à tabela. Sincronizaremos apenas as linhas que foram adicionadas ou atualizadas desde a última sincronização.
- Colunas de identificador de usuário. Sua tabela pode conter uma ou mais colunas de identificador de usuário. Cada linha deve conter apenas um identificador: `external_id`, a combinação de `alias_name` e `alias_label`, ou `braze_id`. Uma tabela de origem pode conter colunas para um, dois ou todos os três tipos de identificadores. 
    - `EXTERNAL_ID` - Isso identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado no Braze. 
    - `ALIAS_NAME` e `ALIAS_LABEL` \- Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário do Braze. Isso é gerado pelo SDK da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da ingestão de dados na nuvem. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário. 
    - `EMAIL` - O endereço de e-mail do usuário. Se houver vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade para atualizações. Se você incluir e-mail e telefone, usaremos o e-mail como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se houver vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade nas atualizações. 
- `PAYLOAD` - Essa é uma string ou struct dos campos que você deseja sincronizar com o usuário no Braze.

#### Etapa 2: Criar um token de acesso  

Para que a Braze acesse o Databricks, é necessário criar um token de acesso pessoal.

1. No seu espaço de trabalho do Databricks, selecione seu nome de usuário do Databricks na barra superior e, em seguida, selecione **Configurações do usuário** no menu suspenso.
2. Na guia Tokens de acesso, selecione **Gerar novo token**.
3. Digite um comentário que o ajude a identificar esse token, como "Braze CDI", e altere o tempo de vida do token para nenhum tempo de vida, deixando a caixa Tempo de vida (dias) vazia (em branco).
4. Selecione **Generate (Gerar**).
5. Copie o token exibido e, em seguida, selecione **Concluído**.

Mantenha o token em um local seguro até que seja necessário inseri-lo no dashboard do Braze durante a etapa de criação de credenciais.

#### Etapa 3: Permitir acesso aos IPs do Braze    

Se você tiver políticas de rede em vigor, deverá conceder à Braze acesso de rede à sua instância do Databricks. Permita o acesso dos IPs abaixo correspondentes à região de seu Braze dashboard.  

| Para as instâncias `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07` | Para as instâncias `EU-01` e `EU-02` |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`

{% endtab %}

{% endtabs %}

### Etapa 2: Crie uma nova integração no dashboard do Braze

{% tabs %}
{% tab Snowflake %}

Acesse **Integrações de parceiros** > **Parceiros de tecnologia**. Localize a página do Snowflake e selecione **Criar nova sincronização de importação**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), acesse **Technology Partners**.
{% endalert %}

#### Etapa 1: Adicionar informações de conexão do Snowflake e tabela de origem

Insira as informações de seu data warehouse do Snowflake e da tabela de origem e, em seguida, prossiga para a próxima etapa.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_1.png %})

#### Etapa 2: Configurar detalhes de sincronização
Em seguida, escolha um nome para sua sincronização e insira os e-mails dos contatos. Usaremos essas informações de contato para notificá-lo sobre quaisquer erros de integração, como a remoção inesperada do acesso à tabela.

Os e-mails de contato receberão apenas notificações de erros globais ou de nível de sincronização, como tabelas ausentes, permissões e outros. Eles não receberão edições em nível de linha. Os erros globais indicam problemas críticos com a conexão que impedem a execução das sincronizações. Esses problemas podem incluir o seguinte:

- Problemas de conectividade
- Falta de recursos
- Problemas de permissões
- (Somente para sincronizações de catálogos) A camada do catálogo está sem espaço

![]({% image_buster /assets/img/cloud_ingestion/ingestion_2.png %})

Você também escolherá o tipo de dados e a frequência de sincronização. A frequência pode variar de cada 15 minutos a uma vez por mês. Usaremos o fuso horário configurado em seu dashboard do Braze para agendar a sincronização recorrente. Os tipos de dados compatíveis são Atributos personalizados, Eventos personalizados e Eventos de compra, e o tipo de dados de uma sincronização não pode ser alterado após a criação. 

#### Adicione uma chave pública ao usuário do Braze
Nesse ponto, você deve voltar ao Snowflake para concluir a configuração. Adicione a chave pública exibida no dashboard ao usuário que você criou para que o Braze se conecte ao Snowflake.

Para obter mais informações sobre como fazer isso, consulte a [documentação do Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Se você quiser alternar as chaves a qualquer momento, podemos gerar um novo par de chaves e fornecer a você a nova chave pública.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```
{% endtab %}
{% tab Redshift %}

Acesse **Integrações de parceiros** > **Parceiros de tecnologia**. Localize a página do Redshift e selecione **Criar nova sincronização de importação**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), acesse **Technology Partners**.
{% endalert %}

#### Etapa 1: Adicionar informações de conexão e tabela de origem do Redshift
Insira as informações de seu data warehouse Redshift e da tabela de origem. Se estiver usando um túnel de rede privada, alterne o controle deslizante e insira as informações do túnel. Em seguida, prossiga para a próxima etapa.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_6.png %})

#### Etapa 2: Configurar detalhes de sincronização
Em seguida, escolha um nome para sua sincronização e insira os e-mails dos contatos. Usaremos essas informações de contato para notificá-lo sobre quaisquer erros de integração, como a remoção inesperada do acesso à tabela.

Os e-mails de contato receberão apenas notificações de erros globais ou de nível de sincronização, como tabelas ausentes, permissões e outros. Eles não receberão edições em nível de linha. Os erros globais indicam problemas críticos com a conexão que impedem a execução das sincronizações. Esses problemas podem incluir o seguinte:

- Problemas de conectividade
- Falta de recursos
- Problemas de permissões
- (Somente para sincronizações de catálogos) A camada do catálogo está sem espaço

![]({% image_buster /assets/img/cloud_ingestion/ingestion_7.png %})

Você também escolherá o tipo de dados e a frequência de sincronização. A frequência pode variar de cada 15 minutos a uma vez por mês. Usaremos o fuso horário configurado em seu dashboard do Braze para agendar a sincronização recorrente. Os tipos de dados compatíveis são Atributos personalizados, Eventos personalizados e Eventos de compra, e o tipo de dados de uma sincronização não pode ser alterado após a criação.
{% endtab %}
{% tab BigQuery %}

Acesse **Integrações de parceiros** > **Parceiros de tecnologia**. Localize a página do BigQuery e selecione **Criar nova sincronização de importação**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), acesse **Technology Partners**.
{% endalert %}

#### Etapa 1: Adicionar informações de conexão do BigQuery e tabela de origem
Faça upload da chave JSON e forneça um nome para a conta de serviço e, em seguida, insira os detalhes de sua tabela de origem.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_11.png %})

#### Etapa 2: Configurar detalhes de sincronização
Em seguida, escolha um nome para sua sincronização e insira os e-mails dos contatos. Usaremos essas informações de contato para notificá-lo sobre quaisquer erros de integração, como a remoção inesperada do acesso à tabela.

Os e-mails de contato receberão apenas notificações de erros globais ou de nível de sincronização, como tabelas ausentes, permissões e outros. Eles não receberão edições em nível de linha. Os erros globais indicam problemas críticos com a conexão que impedem a execução das sincronizações. Esses problemas podem incluir o seguinte:

- Problemas de conectividade
- Falta de recursos
- Problemas de permissões
- (Somente para sincronizações de catálogos) A camada do catálogo está sem espaço

![]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

Você também escolherá o tipo de dados e a frequência de sincronização. A frequência pode variar de cada 15 minutos a uma vez por mês. Usaremos o fuso horário configurado em seu dashboard do Braze para agendar a sincronização recorrente. Os tipos de dados suportados são Atributos personalizados, Eventos personalizados, Eventos de compra e Exclusões de usuários. O tipo de dados de uma sincronização não pode ser alterado após a criação. 

{% endtab %}
{% tab Databricks %}

Acesse **Integrações de parceiros** > **Parceiros de tecnologia**. Localize a página Databricks e selecione **Criar nova sincronização de importação**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), acesse **Technology Partners**.
{% endalert %}

#### Etapa 1: Adicionar informações de conexão e tabela de origem do Databricks
Insira as informações do data warehouse e da tabela de origem do Databricks e prossiga para a próxima etapa.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_16.png %})

#### Etapa 2: Configurar detalhes de sincronização
Em seguida, escolha um nome para sua sincronização e insira os e-mails dos contatos. Usaremos essas informações de contato para notificá-lo sobre quaisquer erros de integração, como a remoção inesperada do acesso à tabela.

Os e-mails de contato receberão apenas notificações de erros globais ou de nível de sincronização, como tabelas ausentes, permissões e outros. Eles não receberão edições em nível de linha. Os erros globais indicam problemas críticos com a conexão que impedem a execução das sincronizações. Esses problemas podem incluir o seguinte:

- Problemas de conectividade
- Falta de recursos
- Problemas de permissões
- (Somente para sincronizações de catálogos) A camada do catálogo está sem espaço

![]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

Você também escolherá o tipo de dados e a frequência de sincronização. A frequência pode variar de cada 15 minutos a uma vez por mês. Usaremos o fuso horário configurado em seu dashboard do Braze para agendar a sincronização recorrente. Os tipos de dados suportados são atributos personalizados, eventos personalizados, eventos de compra e exclusões de usuários. O tipo de dados de uma sincronização não pode ser alterado após a criação. 

{% endtab %}
{% endtabs %}

### Etapa 3: Conexão de teste

{% tabs %}
{% tab Snowflake %}

Retorne ao dashboard do Braze e selecione **Testar conexão**. Se for bem-sucedido, você verá uma prévia dos dados. Se, por algum motivo, não conseguirmos nos conectar, exibiremos uma mensagem de erro para ajudá-lo a solucionar o problema.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_3.png %})
{% endtab %}
{% tab Redshift %}
Retorne ao dashboard do Braze e selecione **Testar conexão**. Se for bem-sucedido, você verá uma prévia dos dados. Se, por algum motivo, não conseguirmos nos conectar, exibiremos uma mensagem de erro para ajudá-lo a solucionar o problema.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_8.png %})
{% endtab %}
{% tab Rede privada Redshift %}

Retorne ao dashboard do Braze e selecione **Testar conexão**. Se for bem-sucedido, você verá uma prévia dos dados. Se, por algum motivo, não conseguirmos nos conectar, exibiremos uma mensagem de erro para ajudá-lo a solucionar o problema.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_19.png %})
{% endtab %}
{% tab BigQuery %}

Depois que todos os detalhes de configuração de sua sincronização forem inseridos, selecione **Testar conexão**. Se for bem-sucedido, você verá uma prévia dos dados. Se, por algum motivo, não conseguirmos nos conectar, exibiremos uma mensagem de erro para ajudá-lo a solucionar o problema.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}
{% tab Databricks %}

Depois que todos os detalhes de configuração de sua sincronização forem inseridos, selecione **Testar conexão**. Se for bem-sucedido, você verá uma prévia dos dados. Se, por algum motivo, não conseguirmos nos conectar, exibiremos uma mensagem de erro para ajudá-lo a solucionar o problema.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Você deve testar com êxito uma integração antes que ela possa passar do estado Rascunho para o estado Ativo. Se você precisar sair da página de criação, sua integração será salva e você poderá acessar novamente a página de detalhes para fazer alterações e testes.  
{% endalert %}

## Configure integrações ou usuários adicionais (opcional)

{% tabs %}
{% tab Snowflake %}
Você pode configurar várias integrações com o Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à conta do Snowflake.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_4.png %})

Se você reutilizar o mesmo usuário e função em todas as integrações, **não** precisará passar pela etapa de adicionar a chave pública novamente.
{% endtab %}
{% tab Redshift %}
Você pode configurar várias integrações com o Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do Snowflake ou do Redshift.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_9.png %})

Se você reutilizar o mesmo usuário em várias integrações, não será possível excluir o usuário no dashboard do Braze até que ele seja removido de todas as sincronizações ativas.
{% endtab %}
{% tab BigQuery %}

Você pode configurar várias integrações com o Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do BigQuery.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_14.png %})

Se você reutilizar o mesmo usuário em várias integrações, não será possível excluir o usuário no dashboard do Braze até que ele seja removido de todas as sincronizações ativas.

{% endtab %}
{% tab Databricks %}

Você pode configurar várias integrações com o Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do Databricks.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_17.png %})

Se você reutilizar o mesmo usuário em várias integrações, não será possível excluir o usuário no dashboard do Braze até que ele seja removido de todas as sincronizações ativas.

{% endtab %}
{% endtabs %}

## Executando a sincronização

{% tabs %}
{% tab Snowflake %}
Quando ativada, sua sincronização será executada de acordo com a programação configurada durante a instalação. Se você quiser executar a sincronização fora da programação normal de testes ou buscar os dados mais recentes, selecione **Sync Now (Sincronizar agora**). Essa execução não afetará as sincronizações futuras programadas regularmente.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_5.png %})

{% endtab %}
{% tab Redshift %}
Quando ativada, sua sincronização será executada de acordo com a programação configurada durante a instalação. Se você quiser executar a sincronização fora da programação normal de testes ou buscar os dados mais recentes, selecione **Sync Now (Sincronizar agora**). Essa execução não afetará as sincronizações futuras programadas regularmente.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_10.png %})

{% endtab %}
{% tab BigQuery %}

Quando ativada, sua sincronização será executada de acordo com a programação configurada durante a instalação. Se você quiser executar a sincronização fora da programação normal de testes ou buscar os dados mais recentes, selecione **Sync Now (Sincronizar agora**). Essa execução não afetará as sincronizações futuras programadas regularmente.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_15.png %})

{% endtab %}
{% tab Databricks %}

Quando ativada, sua sincronização será executada de acordo com a programação configurada durante a instalação. Se você quiser executar a sincronização fora da programação normal de testes ou buscar os dados mais recentes, selecione **Sync Now (Sincronizar agora**). Essa execução não afetará as sincronizações futuras programadas regularmente.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_18.png %})

{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/cloud_ingestion/ingestion_6.png %}
[2]: {% image_buster /assets/img/cloud_ingestion/ingestion_7.png %}
[3]: {% image_buster /assets/img/cloud_ingestion/ingestion_8.png %}
[4]: {% image_buster /assets/img/cloud_ingestion/ingestion_9.png %}
[5]: {% image_buster /assets/img/cloud_ingestion/ingestion_10.png %}
[6]: {% image_buster /assets/img/cloud_ingestion/ingestion_5.png %}
