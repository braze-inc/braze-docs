---
nav_title: Transferência de dados do Amazon S3 para o Snowflake
article_title: Transferência de dados do Amazon S3 para o Snowflake
page_order: 7
page_type: tutorial
description: "Este artigo de instruções o orientará na transferência de dados do armazenamento em nuvem (como o Amazon S3) para um data warehouse (como o Snowflake) usando o processo de ETL."
tool: Currents

---

# Transferência de dados do Amazon S3 para o Snowflake

> Se seus dados estiverem atualmente no Amazon S3, você poderá transferi-los para o Snowflake ou outro data warehouse relacional usando o processo ELT (Extract Load Transform). Esta página explica como fazer isso.

{% alert note %}
Se você tiver casos de uso mais específicos e quiser que a Braze faça a manutenção de sua instância do Currents, entre em contato com seu gerente de conta da Braze e pergunte sobre a Braze Data Professional Services.
{% endalert %}

## Como funciona?

O processo Extract, Load, Transform (ELT) é um processo automatizado que move os dados para o [Snowflake](https://www.snowflake.com/), o que lhe permitirá usar os [blocos do Looker do Braze](https://marketplace.looker.com/marketplace/directory) para visualizar esses dados no Looker e ajudar a gerar insights e feedback em suas campanhas, Canvas e segmentos.

Depois de configurar uma exportação do Currents para o S3 e de receber dados de eventos ao vivo, você poderá configurar seu pipeline ELT ao vivo no Snowflake configurando os seguintes componentes:

-   [Filas SQS da AWS](#aws-sqs-queues)
-   [Snowpipes de ingestão automática](#auto-ingest-snowpipes)

## Configuração das filas do AWS SQS

Os **Snowpipes de ingestão automática** dependem de filas SQS para enviar notificações do S3 para o Snowpipe. Esse processo é gerenciado pelo Snowflake após a configuração do SQS.

### Etapa 1: Configurar o estágio S3 externo

{% alert note %}
As tabelas em seu banco de dados são criadas nesse estágio.
{% endalert %}

1. Ao configurar o Currents na Braze, especifique uma jornada de pasta para os arquivos do Currents seguirem para o bucket S3. Aqui usamos ```currents```, a jornada padrão da pasta.

2. Crie os seguintes itens na ordem listada:
  Na AWS, crie um novo **par de chaves público-privadas** para o bucket S3 desejado, com concessões de acordo com os requisitos de segurança de sua organização.
  2.2. No Snowflake, crie um banco de dados e um esquema de sua escolha (denominados ```currents``` e ```public``` no exemplo a seguir).
  2.3. Crie um estágio Snowflake S3 (chamado `braze_data`):

```sql
CREATE OR REPLACE STAGE
    currents.public.braze_data
    url='s3://snowpipe-demo/'
    credentials = (AWS_KEY_ID = '...' AWS_SECRET_KEY = '...' );
show stages;
```

{: start="3"}
3\. Defina o formato de arquivo AVRO para seu palco.

```sql
CREATE FILE FORMAT
    currents.public.currents_avro
    type = 'avro'
    compression = 'auto';
```

```sql
ALTER STAGE
    currents.public.braze_data
SET
    file_format = currents.public.currents_avro;
```

```sql
CREATE OR REPLACE PIPE
  pipe_users_messages_pushnotification_open
    auto_ingest=true AS

COPY INTO
  users_messages_pushnotification_open
          FROM
           (SELECT
             $1:id::STRING,
             $1:user_id::STRING,
             $1:external_user_id::STRING,
              $1:time::INT,
              $1:timezone::STRING,
              $1:app_id::STRING,
              $1:campaign_id::STRING,
              $1:campaign_name::STRING,
              $1:message_variation_id::STRING,
              $1:canvas_id::STRING,
              $1:canvas_name::STRING,
              $1:canvas_variation_id::STRING,
              $1:canvas_step_id::STRING,
              $1:canvas_step_message_variation_id::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING,
              $1:send_id::STRING,
              $1:device_id::STRING,
              $1:button_action_type::STRING,
              $1:button_string::STRING

              FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.messages.pushnotification.Open/);
```

{: start="4"}
4\. Por fim, use o comando `show pipes;` para mostrar suas informações de SQS. O nome da fila SQS ficará visível em uma nova coluna chamada `NOTIFICATION_CHANNEL` porque esse pipe foi criado como um pipe de teste automático.

### Etapa 2: Criar eventos de balde

1. Na AWS, navegue até o bucket correspondente do novo estágio do Snowflake. Em seguida, na guia **Properties (Propriedades** ), acesse **Events (Eventos**).

![Guia Propriedades da AWS]({% image_buster /assets/img/aws-properties.png %}){: height="50%" width="50%"}

{: start="2"}
2\. Crie novos eventos para cada conjunto de Currents Data, conforme necessário [(envio de mensagens]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/), [comportamento do usuário]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)), ou ambos.

![Criação de um novo evento na AWS]({% image_buster /assets/img/aws-events.png %}){: height="50%" width="50%"}

{: start="3"}
3\. Marque a caixa apropriada para as notificações de criação de objeto, bem como o ARN na parte inferior do formulário (da coluna do canal de notificação no Snowflake).

## Configuração de Snowpipes de teste automático {#auto-ingest-snowpipes}

Para garantir que a configuração do AWS SQS produza as tabelas corretas, é necessário definir adequadamente a estrutura dos dados de entrada usando os seguintes exemplos e esquemas determinados em nossa documentação do Currents para [eventos de engajamento com mensagens ou envio de mensagens]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/), [eventos de comportamento do usuário ou do cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/), ou ambos.

É fundamental estruturar suas tabelas de acordo com os esquemas do Braze Currents, pois o Braze Currents carregará continuamente os dados nelas por meio de campos específicos com tipos de dados específicos. Por exemplo, um `user_id` será carregado como uma string e chamado de `user_id` nos dados do Currents.

{% alert note %}
  Dependendo da sua integração com o Currents, pode haver diferentes eventos que devem ser configurados (como [eventos de engajamento com mensagens ou envio de mensagens]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) e [eventos de comportamento do usuário ou do cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)). Você também pode escrever um script para parte ou todo esse processo.
{% endalert %}

{% tabs %}
  {% tab Eventos de comportamento do usuário %}

1. Primeiro, crie uma tabela `INTO` que será carregada continuamente usando a seguinte estrutura do esquema Currents:

```sql
CREATE TABLE
  users_behaviors_app_firstsession (
        id               STRING,
        user_id          STRING,
        external_user_id STRING,
        app_id           STRING,
        time             INT,
        session_id       STRING,
        gender           STRING,
        country          STRING,
        timezone         STRING,
        language         STRING,
        device_id        STRING,
        sdk_version      STRING,
        platform         STRING,
        os_version       STRING,
        device_model     STRING
    );
```

{: start="2"}
2\. Crie o pipe `auto_ingest` e especifique:
  2.1. Qual tabela carregar
  2.2 Como carregar a tabela a seguir

```sql
CREATE OR REPLACE PIPE
  pipe_users_behaviors_app_firstsession
    auto_ingest=true AS

COPY INTO
  users_behaviors_app_firstsession
          FROM
            (SELECT
              $1:id::STRING,
              $1:user_id::STRING,
              $1:external_user_id::STRING,
              $1:app_id::STRING,
              $1:time::INT,
              $1:session_id::STRING,
              $1:gender::STRING,
              $1:country::STRING,
              $1:timezone::STRING,
              $1:language::STRING,
              $1:device_id::STRING,
              $1:sdk_version::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING

              FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.behaviors.app.FirstSession/);
```

{% alert warning %}
Você deve repetir os comandos `CREATE TABLE` e `CREATE PIPE` para cada tipo de evento.
{% endalert %}

 {% endtab %}
 {% tab Eventos de envio de mensagens %}

1. Primeiro, crie uma tabela `INTO` que será carregada continuamente usando a seguinte estrutura do esquema Currents:

```sql
CREATE TABLE
    public_users_messages_pushnotification_open (
        id STRING,
        user_id STRING,
        external_user_id STRING,
        time INT,
        timezone STRING,
        app_id STRING,
        campaign_id STRING,
        campaign_name STRING,
        message_variation_id STRING,
        canvas_id STRING,
        canvas_name STRING,
        canvas_variation_id STRING,
        canvas_step_id STRING,
        canvas_step_message_variation_id STRING,
        platform STRING,
        os_version STRING,
        device_model STRING,
        send_id STRING,
        device_id STRING,
        button_action_type STRING,
        button_string STRING
        );
```

{: start="2"}
2\. Crie o pipe de carga contínua AUTO e especifique:
  2.1. Qual tabela carregar
  2.2 Como carregar a tabela a seguir

```sql
CREATE OR REPLACE PIPE
  pipe_users_messages_pushnotification_open
    auto_ingest=true AS

COPY INTO
  users_messages_pushnotification_open
          FROM
           (SELECT
             $1:id::STRING,
             $1:user_id::STRING,
             $1:external_user_id::STRING,
              $1:time::INT,
              $1:timezone::STRING,
              $1:app_id::STRING,
              $1:campaign_id::STRING,
              $1:campaign_name::STRING,
              $1:message_variation_id::STRING,
              $1:canvas_id::STRING,
              $1:canvas_name::STRING,
              $1:canvas_variation_id::STRING,
              $1:canvas_step_id::STRING,
              $1:canvas_step_message_variation_id::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING,
              $1:send_id::STRING,
              $1:device_id::STRING,
              $1:button_action_type::STRING,
              $1:button_string::STRING

              FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.messages.pushnotification.Open/);
```

{% alert warning %}
Você deve repetir os comandos `CREATE TABLE` e `CREATE PIPE` para cada tipo de evento.
{% endalert %}

  {% endtab %}
{% endtabs %}

Para ver os tipos de análise de dados que você pode realizar usando o Braze Currents, consulte nossos [blocos do Looker](https://github.com/llooker?q=braze).

{% alert note %}
Entre em contato com seu gerente de conta Braze se tiver alguma dúvida ou se estiver interessado em ser orientado pelo Braze durante esse processo.
{% endalert %}

