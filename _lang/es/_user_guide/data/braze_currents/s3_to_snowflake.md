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
Si tiene casos de uso más específicos y desea que Braze preste servicio a su instancia de Currents, póngase en contacto con su gestor de cuenta de Braze y pregúntele sobre Braze Data Professional Services.
{% endalert %}

## Cómo funciona

El proceso Extraer, Cargar, Transformar (ELT) es un proceso automatizado que traslada los datos a [Snowflake](https://www.snowflake.com/), lo que te permitirá utilizar [los bloques de Looker de Braze](https://marketplace.looker.com/marketplace/directory) para visualizar esos datos en Looker y ayudarte a obtener información y comentarios sobre tus campañas, lienzos y segmentos.

Una vez que haya configurado una exportación de Currents a S3 y esté recibiendo datos de eventos en directo, puede configurar su canalización de ELT en directo en Snowflake configurando los siguientes componentes:

-   [Colas de AWS SQS](#aws-sqs-queues)
-   [Snowpipes Auto-Ingest](#auto-ingest-snowpipes)

## Configuración de las colas de AWS SQS

**Los Snowpipes Auto-ingest** dependen de las colas SQS para el envío de notificaciones desde S3 a Snowpipe. Este proceso es gestionado por Snowflake tras configurar SQS.

### Paso 1: Configurar la etapa externa S3

{% alert note %}
En esta fase se crean las tablas de tu base de datos.
{% endalert %}

1. Cuando configure Currents en Braze, especifique una ruta de carpeta para que sus archivos Currents sigan su bucket de S3. Aquí utilizamos ```currents```, la ruta predeterminada de la carpeta.

2. Crea lo siguiente en el orden indicado:
  En AWS, crea un nuevo **par de claves pública-privada** para el bucket de S3 deseado, con concesiones acordes a los requisitos de seguridad de tu organización.
  2.2. En Snowflake, cree una base de datos y un esquema de su elección (denominados ```currents``` y ```public``` en el siguiente ejemplo).
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
4\. Por último, utiliza el comando `show pipes;` para mostrar la información de tu SQS. El nombre de la cola SQS será visible en una nueva columna llamada `NOTIFICATION_CHANNEL` porque esta canalización se creó como autoanálisis.

### Paso 2: Crear eventos del contenedor

1. En AWS, navega hasta el contenedor correspondiente del nuevo escenario de Snowflake. A continuación, en la pestaña **Propiedades**, vaya a **Eventos**.

![Pestaña Propiedades de AWS]({% image_buster /assets/img/aws-properties.png %}){: height="50%" width="50%"}

{: start="2"}
2\. Cree nuevos eventos para cada conjunto de Datos Corrientes, según sea necesario[(Mensajería]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/), [Comportamiento del Usuario]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)), o ambos.

![Crear un nuevo evento en AWS]({% image_buster /assets/img/aws-events.png %}){: height="50%" width="50%"}

{: start="3"}
3\. Marque la casilla correspondiente para el objeto crear notificaciones, así como el ARN en la parte inferior del formulario (de la columna del canal de notificación en Snowflake).

## Configuración de Snowpipes Auto-ingest {#auto-ingest-snowpipes}

Para que la configuración de AWS SQS produzca las tablas correctas, debes definir adecuadamente la estructura de los datos entrantes utilizando los siguientes ejemplos y esquemas determinados en nuestra documentación de Currents para [eventos de interacción con mensajes o mensajería]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/), [eventos de comportamiento del usuario o del cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/), o ambos.

Es fundamental estructurar tus tablas de acuerdo con los esquemas de Braze Currents, ya que Braze Currents cargará continuamente datos en ellas a través de campos específicos con tipos de datos específicos. Por ejemplo, un `user_id` se cargará como cadena y se denominará `user_id` en los datos de Currents.

{% alert note %}
  En función de su integración con Currents, es posible que deba configurar distintos eventos (como [Eventos de participación en mensajes o Eventos de mensajería]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) y [Eventos de comportamiento de usuarios o clientes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)). También puedes escribir un guión para parte o la totalidad de este proceso.
{% endalert %}

{% tabs %}
  {% tab Eventos de comportamiento del usuario %}

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
Debe repetir los comandos `CREATE TABLE` y `CREATE PIPE` para cada tipo de evento.
{% endalert %}

 {% endtab %}
 {% tab Eventos de mensajería %}

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
Debe repetir los comandos `CREATE TABLE` y `CREATE PIPE` para cada tipo de evento.
{% endalert %}

  {% endtab %}
{% endtabs %}

Para ver los tipos de análisis que puede realizar con Braze Currents, consulte nuestros [Bloques Looker](https://github.com/llooker?q=braze).

{% alert note %}
Ponte en contacto con tu director de cuentas Braze si tienes alguna pregunta o si te interesa que Braze te guíe en este proceso.
{% endalert %}

