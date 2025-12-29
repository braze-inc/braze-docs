---
nav_title: Fontes conectadas
article_title: Fontes conectadas
description: "Esta página aborda como usar a ingestão de dados do Braze Cloud para sincronizar dados relevantes com sua integração do Snowflake, Redshift, BigQuery e Databricks."
page_order: 2
page_type: reference

---

# Fontes conectadas

> As fontes conectadas são uma alternativa de cópia zero à sincronização direta de dados com o recurso Cloud Data Ingestion (CDI) do Braze. Uma fonte conectada consulta diretamente seu data warehouse para criar novos segmentos sem copiar nenhum dos dados subjacentes para o Braze. 

Depois de adicionar uma fonte conectada ao seu espaço de trabalho no Braze, você pode criar um segmento CDI nas Extensões de Segmento. As CDI Segment Extensions permitem que você escreva SQL que consulte diretamente seu data warehouse (usando dados disponibilizados por meio de sua CDI Connected Source) e crie e mantenha um grupo de usuários que podem ser direcionados no Braze. 

Para obter mais informações sobre como criar um segmento com essa fonte, consulte [Extensões de segmento CDI]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/).

{% alert warning %}
Como as fontes conectadas são executadas diretamente no seu data warehouse, você incorrerá em todos os custos associados à execução dessas consultas no data warehouse. As fontes conectadas não registram pontos de dados, e as extensões de segmento CDI não consomem créditos de segmento SQL.
{% endalert %}

## Integração de fontes conectadas

### Etapa 1: Conecte seus recursos

As fontes conectadas de ingestão de dados na nuvem exigem algumas configurações no Braze e em sua instância. Siga estas etapas para configurar a integração - algumas etapas serão realizadas em seu data warehouse e outras serão realizadas em seu painel do Braze.

{% tabs %}
{% tab Snowflake %}
**Em seu data warehouse**
1. Criar uma função e conceder permissões para consultar e criar tabelas em um esquema.
2. Configure seu depósito e conceda acesso a essa função.
3. Crie um usuário para essa função.
4. Dependendo de sua configuração, talvez seja necessário permitir IPs do Braze em sua política de rede do Snowflake.

**No painel de controle do Braze**

{: start="5"}
5\. Crie uma nova fonte conectada no painel do Braze.
6\. Configure os detalhes de sincronização para a fonte conectada.
7\. Recupere a chave pública fornecida no painel de controle do Braze.

**Em seu data warehouse**

{: start="8"}
8\. Anexe a chave pública do painel do Braze ao [usuário do Snowflake para autenticação](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Quando terminar, você poderá usar a fonte conectada para criar uma ou mais extensões de segmento CDI.
{% endtab %}

{% tab Redshift %}
1. Configure os dados de origem e os recursos necessários em seu ambiente Redshift.
2. Crie uma nova fonte conectada no painel do Braze.
4. Teste a integração.
5. Use a fonte conectada para criar uma ou mais extensões de segmento CDI.
{% endtab %}

{% tab BigQuery %}
1. Configure os dados de origem e os recursos necessários em seu ambiente BigQuery.
2. Crie uma conta de serviço e permita o acesso ao(s) projeto(s) e conjunto(s) de dados do BigQuery que contêm os dados que você deseja sincronizar.  
3. Crie uma nova fonte conectada no painel do Braze.
4. Teste a integração.
5. Use a fonte conectada para criar uma ou mais extensões de segmento CDI.
{% endtab %}

{% tab Databricks %}
1. Configure os dados de origem e os recursos necessários em seu ambiente Databricks.
2. Crie uma conta de serviço e permita o acesso ao(s) projeto(s) e conjunto(s) de dados do Databricks que contêm os dados que você deseja sincronizar.  
3. Crie uma nova fonte conectada no painel do Braze.
4. Teste a integração.
5. Use a fonte conectada para criar uma ou mais extensões de segmento CDI.

{% alert important %}
Pode haver de dois a cinco minutos de tempo de aquecimento quando o Braze se conectar às instâncias Classic e Pro SQL, o que levará a atrasos durante a configuração e o teste da conexão, bem como durante a criação e a atualização da extensão de segmento CDI. O uso de uma instância de SQL sem servidor minimizará o tempo de aquecimento e melhorará o rendimento da consulta, mas poderá resultar em custos de integração um pouco mais altos.
{% endalert %}

{% endtab %}

{% tab Microsoft Fabric %}
1. Crie uma entidade de serviço e permita o acesso ao espaço de trabalho do Fabric que será usado para sua integração.   
2. Em seu espaço de trabalho do Fabric, configure os dados de origem e conceda permissões à entidade de serviço 
3. Crie uma nova fonte conectada no painel do Braze.
4. Teste a integração.
5. Use a fonte conectada para criar uma ou mais extensões de segmento CDI.
{% endtab %}

{% endtabs %}

### Etapa 2: Configure seu data warehouse

Configure os dados de origem e os recursos necessários em seu ambiente de data warehouse. A fonte conectada pode fazer referência a uma ou mais tabelas, portanto, certifique-se de que o usuário do Braze tenha permissão para acessar todas as tabelas desejadas na fonte conectada.

{% tabs %}
{% tab Snowflake %}
#### Etapa 2.1: Criar uma função e conceder permissões

Crie uma função para sua fonte conectada usar. Essa função será usada para gerar a lista de tabelas disponíveis em suas Extensões de segmento CDI e para consultar tabelas de origem para criar novos segmentos. Depois que a fonte conectada for criada, o Braze descobrirá os nomes e a descrição de todas as tabelas disponíveis para o usuário no esquema da fonte.

Você pode optar por conceder acesso a todas as tabelas em um esquema ou conceder privilégios somente a tabelas específicas. Todas as tabelas às quais a função Braze tem acesso estarão disponíveis para consulta na extensão de segmento CDI.

A permissão `create table` é necessária para que o Braze possa criar uma tabela com os resultados de sua consulta de extensão de segmento CDI antes de atualizar o segmento no Braze. O Braze criará uma tabela temporária por segmento, e a tabela só persistirá enquanto o Braze estiver atualizando o segmento.

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT CREATE TABLE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to all current and future tables or views in the schema
GRANT SELECT ON ALL TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to specific tables or views in the schema
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;

```

#### Etapa 2.2: Configurar o depósito e conceder acesso à função Braze

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
O depósito precisa ter o sinalizador de **retomada automática** ativado. Se não for, você precisará conceder ao Braze privilégios adicionais `OPERATE` no depósito para que o Braze o ative quando for o momento de executar a consulta.
{% endalert %}

#### Etapa 2.3: Configurar o usuário
```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Você compartilhará informações de conexão com o Braze e receberá uma chave pública para anexar ao usuário em uma etapa posterior.

{% alert note %}
Ao conectar diferentes espaços de trabalho à mesma conta do Snowflake, você deve criar um usuário exclusivo para cada espaço de trabalho do Braze em que estiver criando uma integração. Em um espaço de trabalho, você pode reutilizar o mesmo usuário em todas as integrações, mas a criação da integração falhará se um usuário na mesma conta do Snowflake for duplicado em todos os espaços de trabalho.
{% endalert %}

#### Etapa 2.4: Permitir IPs do Braze em sua política de rede do Snowflake (opcional)

Dependendo da configuração da sua conta do Snowflake, talvez seja necessário permitir os seguintes endereços IP na sua política de rede do Snowflake. Para obter mais informações sobre como fazer isso, consulte a documentação relevante do Snowflake sobre a [modificação de uma política de rede](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include data_centers.md datacenters='ips' %}
{% endtab %}

{% tab Redshift %}
#### Etapa 2.1: Criar usuário e conceder permissões 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Crie um usuário para sua fonte conectada usar. Esse usuário será usado para gerar a lista de tabelas disponíveis em suas Extensões de segmento CDI e para consultar tabelas de origem para criar novos segmentos. Depois que a fonte conectada for criada, o Braze descobrirá os nomes e a descrição de todas as tabelas disponíveis para o usuário no esquema da fonte. Se estiver criando várias integrações CDI, talvez você queira conceder permissões a um esquema ou gerenciar as permissões usando um grupo. 

Você pode optar por conceder acesso a todas as tabelas em um esquema ou conceder privilégios somente a tabelas específicas. Todas as tabelas às quais a função Braze tem acesso estarão disponíveis para consulta na extensão de segmento CDI. Certifique-se de conceder acesso a todas as novas tabelas ao usuário quando elas forem criadas ou defina permissões padrão para o usuário. 

A permissão `create table` é necessária para que o Braze possa criar uma tabela com os resultados de sua consulta de extensão de segmento CDI antes de atualizar o segmento no Braze. O Braze criará uma tabela temporária por segmento, que só persistirá enquanto o Braze atualizar o segmento.


#### Etapa 2.2: Permitir acesso aos IPs do Braze    

Se você tiver um firewall ou outras políticas de rede, deverá conceder ao Braze acesso à rede para sua instância do Redshift. Permita o acesso dos IPs abaixo correspondentes à região de seu painel do Braze. 

Talvez você também precise alterar seus grupos de segurança para permitir que o Braze acesse seus dados no Redshift. Certifique-se de permitir explicitamente o tráfego de entrada nos IPs abaixo e na porta usada para consultar o cluster do Redshift (o padrão é 5439). Você deve permitir explicitamente a conectividade TCP do Redshift nessa porta, mesmo que as regras de entrada estejam definidas como "permitir tudo". Além disso, é importante que o endpoint do cluster Redshift seja acessível publicamente para que o Braze se conecte ao seu cluster.

Se não quiser que o cluster do Redshift seja acessível publicamente, você pode configurar uma instância VPC e EC2 para usar um túnel ssh para acessar os dados do Redshift. Para obter mais informações, consulte [AWS: Como posso acessar um cluster privado do Amazon Redshift a partir do meu computador local?](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab BigQuery %}
#### Etapa 2.1: Criar uma conta de serviço e conceder permissões 

Crie uma conta de serviço no GCP para o Braze usar para se conectar e ler os dados de sua(s) tabela(s). A conta de serviço deve ter as permissões abaixo: 

- **Usuário de conexão do BigQuery:** Permite que o Braze faça conexões.
- **Usuário do BigQuery:** Fornece acesso ao Braze para executar consultas, ler metadados de conjuntos de dados e listar tabelas.
- **Visualizador de dados do BigQuery:** Fornece acesso ao Braze para visualizar conjuntos de dados e seus conteúdos.
- **Usuário do BigQuery Job:** Fornece acesso ao Braze para executar trabalhos.
- **bigquery.tables.create** Fornece acesso ao Braze para criar tabelas temporárias durante a atualização do segmento.

Crie uma conta de serviço para ser usada por sua fonte conectada. Esse usuário será usado para gerar a lista de tabelas disponíveis em suas Extensões de segmento CDI e para consultar tabelas de origem para criar novos segmentos. Depois que a fonte conectada for criada, o Braze descobrirá os nomes e a descrição de todas as tabelas disponíveis para o usuário no esquema da fonte. 

Você pode optar por conceder acesso a todas as tabelas em um conjunto de dados ou conceder privilégios somente a tabelas específicas. Todas as tabelas às quais a função Braze tem acesso estarão disponíveis para consulta na extensão de segmento CDI. 

A permissão `create table` é necessária para que o Braze possa criar uma tabela com os resultados de sua consulta de extensão de segmento CDI antes de atualizar o segmento no Braze. O Braze criará uma tabela temporária por segmento, e a tabela só persistirá enquanto o Braze estiver atualizando o segmento. 

Depois de criar a conta de serviço e conceder permissões, gere uma chave JSON. Para obter mais informações, consulte [Google Cloud: Criar e excluir chaves de conta de serviço](https://cloud.google.com/iam/docs/keys-create-delete). Você fará o upload disso para o painel do Braze mais tarde.

#### Etapa 2.2: Permitir acesso aos IPs do Braze    

Se você tiver políticas de rede em vigor, deverá conceder ao Braze acesso de rede à sua instância do Big Query. Permita o acesso dos IPs abaixo correspondentes à região de seu painel do Braze.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Databricks %}
#### Etapa 2.1: Criar um token de acesso  

Para que o Braze acesse o Databricks, é necessário criar um token de acesso pessoal.

1. No espaço de trabalho do Databricks, selecione seu nome de usuário do Databricks na barra superior e, em seguida, selecione **User Settings (Configurações do usuário** ) no menu suspenso.
2. Certifique-se de que a conta de serviço tenha privilégios `CREATE TABLE` no esquema usado para a fonte conectada. 
3. Na guia **Access tokens (Tokens de acesso** ), selecione **Generate new token (Gerar novo token**).
4. Insira um comentário que o ajude a identificar esse token, como "Braze CDI", e altere o tempo de vida do token para nenhum tempo de vida, deixando a caixa Tempo de vida (dias) vazia (em branco).
5. Selecione **Generate (Gerar**).
6. Copie o token exibido e selecione **Concluído**.

Esse token será usado para gerar a lista de tabelas disponíveis em suas CDI Segment Extensions e para consultar tabelas de origem para criar novos segmentos. Depois que a fonte conectada for criada, o Braze descobrirá os nomes e a descrição de todas as tabelas disponíveis para o usuário no esquema da fonte. 

Você pode optar por conceder acesso a todas as tabelas em um esquema ou conceder privilégios somente a tabelas específicas. Todas as tabelas às quais a função Braze tem acesso estarão disponíveis para consulta na extensão de segmento CDI.

A permissão `create table` é necessária para que o Braze possa criar uma tabela com os resultados de sua consulta de extensão de segmento CDI antes de atualizar o segmento no Braze. O Braze criará uma tabela temporária por segmento, que só persistirá enquanto o Braze atualizar o segmento. 

Mantenha o token em um local seguro até que seja necessário inseri-lo no painel do Braze durante a etapa de criação de credenciais.

#### Etapa 2.2: Permitir acesso aos IPs do Braze    

Se você tiver políticas de rede em vigor, deverá conceder ao Braze acesso de rede à sua instância do Databricks. Permita o acesso dos IPs abaixo correspondentes à região de seu painel do Braze.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Microsoft Fabric %}
#### Etapa 2.1: Conceder acesso aos recursos do Fabric 
O Braze se conectará ao seu armazém Fabric usando uma entidade de serviço com autenticação Entra ID. Você criará uma nova entidade de serviço para ser usada pelo Braze e concederá acesso aos recursos do Fabric conforme necessário. O Braze precisará dos seguintes detalhes para se conectar:    

* ID do locatário (também chamado de diretório) para sua conta do Azure 
* ID da entidade principal (também chamada de ID do aplicativo) para a entidade principal do serviço 
* Segredo do cliente para autenticação do Braze

1. No portal do Azure, navegue até o centro de administração do Microsoft Entra e, em seguida, **Registros de aplicativos**.
2. Selecione **\+ Novo registro** em **Identidade > Aplicativos > Registros de aplicativos** 
3. Digite um nome e selecione `Accounts in this organizational directory only` como o tipo de conta compatível. Em seguida, selecione **Register (Registrar**). 
4. Selecione o aplicativo (service principal) que você acabou de criar e, em seguida, navegue até **Certificates & secrets > + New client secret**
5. Insira uma descrição para o segredo e defina um período de expiração para o segredo. Em seguida, selecione **Add (Adicionar**). 
6. Observe o segredo do cliente criado para ser usado na configuração do Braze. 

{% alert note %}
O Azure não permite a expiração ilimitada dos segredos da entidade de serviço. Lembre-se de atualizar as credenciais antes que elas expirem para manter o fluxo de dados para o Braze.
{% endalert %}

#### Etapa 2.2: Conceder acesso aos recursos do Fabric 
Você fornecerá acesso para que o Braze se conecte à sua instância do Fabric. No portal de administração da Fabric, navegue até **Configurações** > **Governança e insights** > **Portal de administração** > **Configurações do locatário**.    

* Nas **configurações do desenvolvedor**, ative a opção "Service principals can use Fabric APIs" para que o Braze possa se conectar usando o Microsoft Entra ID.
* Nas **configurações do OneLake**, ative "Os usuários podem acessar os dados armazenados no OneLake com aplicativos externos ao Fabric" para que o principal do serviço possa acessar os dados de um aplicativo externo.

#### Etapa 2.3: Obter a cadeia de conexão do depósito 

Você precisará do endpoint SQL do seu depósito para que o Braze possa se conectar. Para recuperar o ponto de extremidade SQL, vá para o **espaço de trabalho** no Fabric e, na lista de itens, passe o mouse sobre o nome do depósito e selecione **Copiar cadeia de conexão SQL**.

A página "Fabric Console" no Microsoft Azure, onde os usuários devem recuperar a cadeia de conexão do SQL.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})

#### Etapa 2.4: Permitir IPs do Braze no firewall (opcional)

Dependendo da configuração de sua conta do Microsoft Fabric, talvez seja necessário permitir os seguintes endereços IP em seu firewall para permitir o tráfego do Braze. Para obter mais informações sobre como ativar esse recurso, consulte a documentação relevante sobre o [Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Etapa 3: Criar uma fonte conectada no painel de controle do Braze

{% tabs %}
{% tab Snowflake %}
#### Etapa 3.1: Adicionar informações de conexão e tabela de origem do Snowflake

Crie uma fonte conectada no painel de controle do Braze. Vá para **Configurações de dados** > **Ingestão de dados na nuvem** > **Fontes conectadas** e selecione **Criar nova sincronização de dados** > **Importação do Snowflake**.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Insira as informações do data warehouse do Snowflake e do esquema de origem e prossiga para a próxima etapa.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_1.png %})

#### Etapa 3.2: Configurar detalhes de sincronização

Escolha um nome para a fonte conectada. Esse nome será usado na lista de fontes disponíveis quando você criar uma nova extensão de segmento CDI. 

Configure um tempo máximo de execução para essa fonte. O Braze interromperá automaticamente todas as consultas que excederem o tempo máximo de execução quando estiver criando ou atualizando um segmento. O tempo máximo de execução permitido é de 60 minutos; um tempo de execução menor reduzirá os custos incorridos em sua conta do Snowflake. 

{% alert note %}
Se as consultas estiverem constantemente atingindo o tempo limite e você tiver definido um tempo de execução máximo de 60 minutos, considere tentar otimizar o tempo de execução da consulta ou dedicar um warehouse maior ao usuário do Braze.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_2.png %})

#### Etapa 3.3: Observe a chave pública  

Na etapa **Testar conexão**, anote a chave pública RSA. Você precisará dele para concluir a integração no Snowflake.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_3.png %})

{% endtab %}
{% tab Redshift %}
#### Etapa 3.1: Adicionar informações de conexão e tabela de origem do Redshift

Crie uma fonte conectada no painel de controle do Braze. Vá para **Configurações de dados** > **Ingestão de dados na nuvem** > **Fontes conectadas** e selecione **Criar conexão de dados** > **Importação do Amazon Redshift**.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Insira as informações do data warehouse e do esquema de origem do Redshift e prossiga para a próxima etapa.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_1.png %})

#### Etapa 3.2: Configurar detalhes de sincronização

Escolha um nome para a fonte conectada. Esse nome será usado na lista de fontes disponíveis quando você criar uma nova extensão de segmento CDI. 

Configure um tempo máximo de execução para essa fonte. O Braze interromperá automaticamente todas as consultas que excederem o tempo máximo de execução quando estiver criando ou atualizando um segmento. O tempo máximo de execução permitido é de 60 minutos; um tempo de execução menor reduzirá os custos incorridos em sua conta do Redshift. 

{% alert note %}
Se as consultas estiverem constantemente atingindo o tempo limite e você tiver definido um tempo de execução máximo de 60 minutos, considere tentar otimizar o tempo de execução da consulta ou dedicar um warehouse maior ao usuário do Braze.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_2.png %})

#### Etapa 3.3: Anote a chave pública (opcional)

Se suas credenciais tiverem selecionado **Conectar com túnel SSH**, observe a chave pública RSA na etapa **Testar conexão**. Você precisará dele para concluir a integração no Redshift.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_3.png %})

{% endtab %}
{% tab BigQuery %}
#### Etapa 3.1: Adicionar informações de conexão do BigQuery e tabela de origem

Crie uma fonte conectada no painel de controle do Braze. Vá para **Configurações de dados** > **Ingestão de dados na nuvem** > **Fontes conectadas** e selecione **Criar nova sincronização de dados** > **Importação do Google BigQuery**.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Insira as informações de seu projeto e conjunto de dados do BigQuery e prossiga para a próxima etapa.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_1.png %})

#### Etapa 3.2: Configurar detalhes de sincronização

Escolha um nome para a fonte conectada. Esse nome será usado na lista de fontes disponíveis quando você criar uma nova extensão de segmento CDI. 

Configure um tempo máximo de execução para essa fonte. O Braze interromperá automaticamente todas as consultas que excederem o tempo máximo de execução quando estiver criando ou atualizando um segmento. O tempo máximo de execução permitido é de 60 minutos; um tempo de execução menor reduzirá os custos incorridos em sua conta do BigQuery. 

{% alert note %}
Se as consultas estiverem constantemente atingindo o tempo limite e você tiver definido um tempo de execução máximo de 60 minutos, considere tentar otimizar o tempo de execução da consulta ou dedicar um warehouse maior ao usuário do Braze.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_2.png %})

#### Etapa 3.3: Teste a conexão

Selecione **Testar conexão** para verificar se a lista de tabelas visíveis para o usuário é a esperada e, em seguida, selecione **Concluído**. Sua fonte conectada foi criada e está pronta para ser usada nas CDI Segment Extensions.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Databricks %}
#### Etapa 3.1: Adicionar informações de conexão e tabela de origem do Databricks

Crie uma fonte conectada no painel de controle do Braze. Vá para **Configurações de dados** > **Ingestão de dados na nuvem** > **Fontes conectadas** e selecione **Criar nova sincronização de dados** > **Importação de Databricks**.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Insira as informações de suas credenciais do Databricks e, opcionalmente, o catálogo e o esquema de origem, e prossiga para a próxima etapa.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_databricks_1.png %})

#### Etapa 3.2: Configurar detalhes de sincronização

Escolha um nome para a fonte conectada. Esse nome será usado na lista de fontes disponíveis quando você criar uma nova extensão de segmento CDI. 

Configure um tempo máximo de execução para essa fonte. O Braze interromperá automaticamente todas as consultas que excederem o tempo máximo de execução quando estiver criando ou atualizando um segmento. O tempo máximo de execução permitido é de 60 minutos; um tempo de execução menor reduzirá os custos incorridos em sua conta da Databricks. 

{% alert note %}
Se as consultas estiverem constantemente atingindo o tempo limite e você tiver definido um tempo de execução máximo de 60 minutos, considere tentar otimizar o tempo de execução da consulta ou dedicar um warehouse maior ao usuário do Braze.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_db_2.png %})

#### Etapa 3.3: Teste a conexão

Selecione **Testar conexão** para verificar se a lista de tabelas visíveis para o usuário é a esperada e, em seguida, selecione **Concluído**. Sua fonte conectada foi criada e está pronta para ser usada nas CDI Segment Extensions.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Microsoft Fabric %}
#### Etapa 3.1: Adicionar informações de conexão e tabela de origem do Microsoft Fabric

Crie uma fonte conectada no painel de controle do Braze. Vá para **Configurações de dados** > **Ingestão de dados na nuvem** > **Fontes conectadas** e selecione **Criar nova sincronização de dados** > **Microsoft Fabric Import**.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Insira as informações de suas credenciais do Microsoft Fabric, bem como o warehouse e o esquema de origem, e prossiga para a próxima etapa.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_1.png %})

#### Etapa 3.2: Configurar detalhes de sincronização

Escolha um nome para a fonte conectada. Esse nome será usado na lista de fontes disponíveis quando você criar uma nova extensão de segmento CDI. 

Configure um tempo máximo de execução para essa fonte. O Braze interromperá automaticamente todas as consultas que excederem o tempo máximo de execução quando estiver criando ou atualizando um segmento. O tempo máximo de execução permitido é de 60 minutos; um tempo de execução menor reduzirá os custos incorridos em sua conta do Microsoft Fabric. 

{% alert note %}
Se as consultas estiverem atingindo o tempo limite de forma consistente e você tiver definido um tempo de execução máximo de 60 minutos, considere tentar otimizar o tempo de execução da consulta ou dimensionar a capacidade do Fabric.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_2.png %})

#### Etapa 3.3: Teste a conexão

Selecione **Testar conexão** para verificar se a lista de tabelas visíveis para o usuário é a esperada e, em seguida, selecione **Concluído**. Sua fonte conectada foi criada e está pronta para ser usada nas CDI Segment Extensions.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% endtabs %}

### Etapa 4: Finalizar a configuração do data warehouse

{% tabs %}
{% tab Snowflake %}
Adicione a chave pública que você anotou na última etapa ao seu usuário no Snowflake. Isso permitirá que o Braze se conecte ao Snowflake. Para obter detalhes sobre como fazer isso, consulte a [documentação do Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). 

Se você quiser alternar as chaves a qualquer momento, poderá criar uma nova chave pública acessando **o Gerenciamento de acesso a dados** no **Cloud Data Ingestion** e selecionando **Gerar nova chave** para a respectiva conta.

\![Gerenciamento de acesso a dados para credenciais de acesso a dados do Snowflake, com um botão para gerar nova chave.]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_4.png %})

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Depois de adicionar a chave ao usuário no Snowflake, selecione **Testar conexão** no Braze e, em seguida, selecione **Concluído**. Sua fonte conectada foi criada e está pronta para ser usada nas CDI Segment Extensions.
{% endtab %}

{% tab Redshift %}
Se estiver se conectando com um túnel SSH, adicione a chave pública que você anotou na última etapa ao usuário do túnel SSH. 

Depois de adicionar a chave ao usuário, selecione **Testar conexão** no Braze e, em seguida, selecione **Concluído**. Sua fonte conectada foi criada e está pronta para ser usada nas CDI Segment Extensions.

{% endtab %}
{% tab BigQuery %}
Isso não se aplica ao BigQuery.

{% endtab %}
{% tab Databricks %}
Isso não se aplica ao Databricks.

{% endtab %}
{% tab Microsoft Fabric %}
Isso não se aplica ao Microsoft Fabric.

{% endtab %}
{% endtabs %}

{% alert note %}
Você deve testar com êxito uma fonte antes que ela possa passar do estado "rascunho" para o estado "ativo". Se você precisar sair da página de criação, sua integração será salva e você poderá acessar novamente a página de detalhes para fazer alterações e testes.  
{% endalert %}

## Configuração de integrações ou usuários adicionais (opcional)

{% tabs %}
{% tab Snowflake %}
Você pode configurar várias integrações com o Braze, mas cada integração deve ser configurada para conectar um esquema diferente. Ao criar conexões adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do Snowflake.

Se você reutilizar o mesmo usuário e função em todas as integrações, não precisará adicionar a chave pública novamente.
{% endtab %}

{% tab Redshift %}
Você pode configurar várias origens com o Braze, mas cada origem deve ser configurada para conectar um esquema diferente. Ao criar fontes adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do Redshift.
{% endtab %}

{% tab BigQuery %}
Você pode configurar várias fontes com o Braze, mas cada fonte deve ser configurada para conectar um conjunto de dados diferente. Ao criar fontes adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do BigQuery.
{% endtab %}

{% tab Databricks %}
Você pode configurar várias origens com o Braze, mas cada origem deve ser configurada para conectar um esquema diferente. Ao criar fontes adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do Databricks.
{% endtab %}

{% tab Microsoft Fabric %}
Você pode configurar várias origens com o Braze, mas cada origem deve ser configurada para conectar um esquema diferente. Ao criar fontes adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do Azure.
{% endtab %}
{% endtabs %}

## Usando a fonte conectada

Depois que a fonte for criada, você poderá usá-la para criar uma ou mais extensões de segmento CDI. Para obter mais informações sobre como criar um segmento com essa fonte, consulte a [documentação CDI Segment Extensions (Extensões de segmento CDI]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/)).

{% alert note %}
Se as consultas estiverem constantemente atingindo o tempo limite e você tiver definido um tempo de execução máximo de 60 minutos, considere tentar otimizar o tempo de execução da consulta ou dedicar mais recursos de computação (como um warehouse maior) ao usuário do Braze.
{% endalert %}
