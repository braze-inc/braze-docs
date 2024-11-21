---
nav_title: "Configuración del canal de eventos ETL"
article_title: Configuración de la canalización de eventos ETL Snowflake
page_order: 2
description: "Esta página de socio ofrece un ejemplo de configuración de una consulta de clics de correo electrónico como referencia para configurar sus propias consultas."
page_type: partner
search_tag: Partner

---

# Configuración del canal de eventos ETL

> Esta página asociada ofrece un ejemplo de configuración de una consulta de clics de correo electrónico que puede utilizar como referencia para configurar sus propias consultas.

Puede utilizar esta consulta de clics de correo electrónico para analizar las interacciones con correos electrónicos específicos en sus campañas Braze y Canvases.

## Configure esta consulta

Cree una base de datos para `BRAZE`, luego cree una base de datos si no existe ninguna para `BRAZE_CURRENTS;`:

```sql
use schema BRAZE_CURRENTS.public;

create or replace stage braze_currents.public.braze_data
url='s3://tl-braze/'
credentials = (AWS_KEY_ID = 'XXXXXXXXX' AWS_SECRET_KEY = 'YYYYYY' );

create file format braze_currents.public.currents_avro type = 'avro' compression = 'auto';

alter stage braze_currents.public.braze_data set file_format = braze_currents.public.currents_avro;

show stages;
```

Utilice el siguiente comando para crear su tabla:

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

Utiliza el siguiente comando para crear o sustituir tu canalización:

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

## Haz más con este ejemplo de consulta

Copie la dirección `notification_channel` de la salida del comando anterior y utilícela para configurar las notificaciones de los buckets de S3.

Sincroniza manualmente desde S3 a Snowflake para el siguiente nombre de canalización dado:
```sql
ALTER PIPE
  pipe_users_messages_email_click
  refresh ;
```

Comprueba el estado de la canalización, que mostrará cuándo se reenvió el mensaje desde S3 a Snowflake:
```sql
SELECT
  SYSTEM$PIPE_STATUS(
    'pipe_users_messages_email_click'
  )
```

Por último, muestra el historial de copias de la tabla seleccionando `*` desde:
```sql
table(braze_currents.information_schema.copy_history(table_name=>'users_messages_email_click', start_time=> dateadd(hours, -1, current_timestamp())));
```