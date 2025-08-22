---
nav_title: "Configuração do pipeline de eventos ETL"
article_title: Configuração do pipeline de eventos ETL do Snowflake
page_order: 2
description: "Esta página de parceiro oferece um exemplo de configuração de uma consulta de cliques de e-mail para referência ao configurar suas próprias consultas."
page_type: partner
search_tag: Partner

---

# Configuração do pipeline de eventos ETL

> Esta página de parceiro oferece um exemplo de configuração de uma consulta de cliques de e-mail para referência ao configurar suas próprias consultas.

Você pode usar essa consulta de cliques em e-mails para analisar as interações com e-mails específicos em suas campanhas e Canvas do Braze.

## Configure esta consulta

Crie um banco de dados para `BRAZE` e, se não houver nenhum, crie um banco de dados para `BRAZE_CURRENTS;`:

```sql
use schema BRAZE_CURRENTS.public;

create or replace stage braze_currents.public.braze_data
url='s3://tl-braze/'
credentials = (AWS_KEY_ID = 'XXXXXXXXX' AWS_SECRET_KEY = 'YYYYYY' );

create file format braze_currents.public.currents_avro type = 'avro' compression = 'auto';

alter stage braze_currents.public.braze_data set file_format = braze_currents.public.currents_avro;

show stages;
```

Use o seguinte comando para criar sua tabela:

```sql
CREATE TABLE
  braze_currents.public.users_messages_email_click (
    id STRING,
    user_id STRING,
    external_user_id STRING,
    time INT,
    timezone STRING,
    campaign_id STRING,
    campaign_name STRING,
    message_variation_id STRING,
    canvas_id STRING,
    canvas_name STRING,
    canvas_variation_id STRING,
    canvas_step_id STRING,
    send_id STRING,
    dispatch_id STRING,
    email_address STRING,
    url STRING,
    sending_ip STRING,
    user_agent STRING
  );
```

Use o seguinte comando para criar ou substituir seu pipe:

```sql
CREATE OR REPLACE PIPE
  pipe_users_messages_email_click
    auto_ingest=true AS

COPY INTO
  braze_currents.public.users_messages_email_click
  FROM
  (select
    $1:id::STRING,
    $1:user_id::STRING,
    $1:external_user_id::STRING,
    $1:time::INT,
    $1:timezone::STRING,
    $1:campaign_id::STRING,
    $1:campaign_name::STRING,
    $1:message_variation_id::STRING,
    $1:canvas_id::STRING,
    $1:canvas_name::STRING,
    $1:canvas_variation_id::STRING,
    $1:canvas_step_id::STRING,
    $1:send_id::STRING,
    $1:dispatch_id::STRING,
    $1:email_address::STRING,
    $1:url::STRING,
    $1:sending_ip::STRING,
    $1:user_agent::STRING

    FROM
    @braze_currents.public.braze_data/currents/dataexport.prod-03.S3.integration.YOUR_INTEGRATION_ID_HERE/event_type=users.messages.email.click/);

show pipes;
```

## Faça mais com este exemplo de consulta

Copie o endereço `notification_channel` da saída do comando anterior e use-o ao configurar as notificações do bucket S3.

Sincronize manualmente do S3 para o Snowflake para o seguinte nome de canal fornecido:
```sql
ALTER PIPE
  pipe_users_messages_email_click
  refresh ;
```

Verifique o status do pipe, que mostrará quando a mensagem foi encaminhada do S3 para o Snowflake:
```sql
SELECT
  SYSTEM$PIPE_STATUS(
    'pipe_users_messages_email_click'
  )
```

Por fim, mostre o histórico de cópias da tabela selecionando `*` de:
```sql
table(braze_currents.information_schema.copy_history(table_name=>'users_messages_email_click', start_time=> dateadd(hours, -1, current_timestamp())));
```