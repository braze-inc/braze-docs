---
nav_title: Transferencia de datos de Amazon S3 a Snowflake
article_title: Transferencia de datos de Amazon S3 a Snowflake
page_order: 7
page_type: tutorial
description: "Este artículo te guiará en la transferencia de datos desde el almacenamiento en la nube (como Amazon S3) a un almacén (como Snowflake) mediante el proceso Extraer, Transformar, Cargar (ETL)."
tool: Currents

---

# Transferencia de datos de Amazon S3 a Snowflake

> Si tus datos se encuentran actualmente en Amazon S3, puedes transferirlos a Snowflake o a otro almacén de datos relacional mediante el proceso Extraer, Cargar, Transformar (ELT). Esta página explica cómo hacerlo.

{% alert note %}
Si tienes casos de uso más específicos y quieres que Braze preste servicio a tu instancia de Currents, ponte en contacto con tu director de cuentas de Braze y pregúntale por los Servicios profesionales de datos de Braze.
{% endalert %}

## Cómo funciona

El proceso Extraer, Cargar, Transformar (ELT) es un proceso automatizado que traslada datos a [Snowflake](https://www.snowflake.com/), lo que te permitirá utilizar [los bloques de Looker de Braze](https://marketplace.looker.com/marketplace/directory) para visualizar esos datos en Looker y ayudarte a obtener información y comentarios sobre tus campañas, lienzos y segmentos.

Una vez que tengas configurada la exportación de Currents a S3 y estés recibiendo datos de eventos en vivo, puedes configurar tu canalización de ELT en vivo en Snowflake configurando los siguientes componentes:

-   [Colas AWS SQS](#aws-sqs-queues)
-   [Tubos de nieve autoingestores](#auto-ingest-snowpipes)

## Configurar las colas de AWS SQS

**Los Snowpipes Auto-ingest** dependen de las colas SQS para enviar notificaciones de S3 a Snowpipe. Este proceso lo gestiona Snowflake tras configurar SQS.

### Paso 1: Configura la etapa externa S3

{% alert note %}
En esta fase se crean las tablas de tu base de datos.
{% endalert %}

1. Cuando configures Currents en Braze, especifica una ruta de carpeta para que tus archivos Currents vayan a tu contenedor de S3. Aquí utilizamos ```currents```, la ruta predeterminada de la carpeta.

2. Crea lo siguiente en el orden indicado:
  2.1 En AWS, crea un nuevo **par de claves pública-privada** para el contenedor de S3 deseado, con concesiones acordes a los requisitos de seguridad de tu organización.
  2.2. En Snowflake, crea una base de datos y un esquema de tu elección (denominados ```currents``` y ```public``` en el siguiente ejemplo).
  2.3. Crea un escenario S3 Snowflake (llamado `braze_data`):

```sql
CREATE OR REPLACE STAGE
    currents.public.braze_data
    url='s3://snowpipe-demo/'
    credentials = (AWS_KEY_ID = '...' AWS_SECRET_KEY = '...' );
show stages;
```

{: start="3"}
3\. Define el formato de archivo AVRO para tu escenario.

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
4\. Por último, utiliza el comando `show pipes;` para mostrar la información de tu SQS. El nombre de la cola SQS será visible en una nueva columna llamada `NOTIFICATION_CHANNEL` porque esta tubería se creó como tubería de autoanálisis.

### Paso 2: Crear eventos del contenedor

1. En AWS, navega hasta el contenedor correspondiente de la nueva etapa Snowflake. Después, en la pestaña **Propiedades**, ve a **Eventos**.

\![pestaña Propiedades de AWS]({% image_buster /assets/img/aws-properties.png %}){: height="50%" width="50%"}

{: start="2"}
2\. Crea nuevos eventos para cada conjunto de Datos Currents, según sea necesario[(Mensajería]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/), [Comportamiento del usuario]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)), o ambos.

\![Crear un nuevo evento en AWS]({% image_buster /assets/img/aws-events.png %}){: height="50%" width="50%"}

{: start="3"}
3\. Marca la casilla correspondiente al objeto crear notificaciones, así como el ARN en la parte inferior del formulario (de la columna del canal de notificación en Snowflake).

## Configurar los Snowpipes de autoanálisis {#auto-ingest-snowpipes}

Para que la configuración de AWS SQS produzca las tablas correctas, debes definir adecuadamente la estructura de los datos entrantes utilizando los siguientes ejemplos y esquemas determinados en nuestra documentación de Currents para [eventos de interacción con mensajes o mensajería]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/), [eventos de comportamiento del usuario o del cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/), o ambos.

Es fundamental estructurar tus tablas de acuerdo con los esquemas de Braze Currents, ya que Braze Currents cargará continuamente datos en ellas a través de campos específicos con tipos de datos específicos. Por ejemplo, un `user_id` se cargará como cadena y se llamará `user_id` en los datos de Currents.

{% alert note %}
  Dependiendo de tu integración de Currents, puede que tengas diferentes eventos que debas configurar (como [Eventos de interacción con los mensajes o de mensajería]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) y [Eventos de comportamiento del usuario o del cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)). También puedes escribir un guión para una parte o la totalidad de este proceso.
{% endalert %}

{% tabs %}
  {% tab User Behavior Events %}

1. Crea una tabla `INTO` que cargaremos continuamente utilizando la siguiente estructura del esquema Currents:

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
2\. Crea la tubería `auto_ingest` y especifica:
  2.1. Qué tabla cargar
  2.2 Cómo cargar la siguiente tabla

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
Debes repetir los comandos `CREATE TABLE` y `CREATE PIPE` para cada tipo de evento.
{% endalert %}

 {% endtab %}
 {% tab Messaging Events %}

1. Crea una tabla `INTO` que cargaremos continuamente utilizando la siguiente estructura del esquema Currents:

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
2\. Crea la tubería de carga continua AUTO y especifica:
  2.1. Qué tabla cargar
  2.2 Cómo cargar la siguiente tabla

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
Debes repetir los comandos `CREATE TABLE` y `CREATE PIPE` para cada tipo de evento.
{% endalert %}

  {% endtab %}
{% endtabs %}

Para ver los tipos de análisis que puedes realizar con Braze Currents, consulta nuestros [bloques de Looker](https://github.com/llooker?q=braze).

{% alert note %}
Ponte en contacto con tu director de cuentas Braze si tienes alguna pregunta o si te interesa que Braze te guíe en este proceso.
{% endalert %}

