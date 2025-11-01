---
nav_title: Extensiones de segmento CDI
article_title: Extensiones de segmento CDI
page_order: 0
page_type: reference
alias: /cdi_segment_extensions/
tool: 
- Segments
description: "Este artículo te mostrará cómo configurar la orientación por ubicación, que te permite segmentar a los usuarios por ubicación."

---

# Extensiones de segmento CDI

> Con Braze [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/) (CDI), puedes configurar una conexión directa desde tu almacén de datos o sistema de almacenamiento de archivos a Braze para sincronizar datos relevantes de usuarios o catálogos de forma recurrente.

{% alert warning %}
Las extensiones de segmento CDI consultan directamente tu almacén de datos, por lo que incurrirás en todos los costes asociados a la ejecución de estas consultas en tu almacén de datos. Las extensiones de segmento CDI no consumen [créditos de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#monitoring-your-sql-segments-usage), no cuentan para tu límite de extensiones de segmento y no registran puntos de datos.
{% endalert %}

## Requisitos previos

Para utilizar los datos de tu almacén de datos para la segmentación dentro de tu espacio de trabajo Braze, tendrás que crear un [origen conectado]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/) y, a continuación, crear un segmento CDI dentro de tus [Extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). Las extensiones de segmento CDI te permiten escribir SQL que consulte directamente tu propio almacén de datos utilizando los datos disponibles a través de tus conexiones CDI, y crear un grupo de usuarios al que dirigirte dentro de Braze.

## Crear un segmento CDI

### Paso 1: Configura tu fuente

Antes de crear tu primera extensión de segmento CDI, configura un nuevo origen conectado con tu almacén de datos siguiendo los pasos de [Fuentes conectadas]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/).

### Paso 2: Crear un segmento

En primer lugar, crea una nueva [Extensión de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) y, a continuación, selecciona **Actualización completa**.

\![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

Para tu origen de datos, elige **Tablas de datos CDI**.

\![]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

Como parte de tu configuración CDI, puedes seleccionar entre diferentes conexiones para utilizarlas en las extensiones de segmento CDI. Cada conexión tiene un conjunto específico de tablas de datos. Tu equipo de desarrolladores puede configurar tus conexiones y tablas de datos durante la configuración del CDI.

Para ver las tablas de datos disponibles, incluyendo su esquema y las descripciones disponibles, selecciona **Referencia**. Cuando estés preparado, selecciona una conexión.

\![]({% image_buster /assets/img/segment/connection_schema_with_descriptions.png %}){: style="max-width:100%;"}

A continuación, escribe el SQL para tu segmento utilizando [la sintaxis SQL de Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#writing-sql).

Ten en cuenta que todas las extensiones de segmento CDI deben utilizar `external_user_id` como columna seleccionada, y que tu `external_user_id` debe coincidir con la establecida en Braze para los usuarios. Si los resultados de tu consulta incluyen usuarios que no existen en Braze, esos usuarios serán ignorados. Braze no creará nuevos usuarios basándose en la salida de tu extensión de segmento CDI.

{% alert tip %}
Para saber cómo puedes obtener una vista previa de tus extensiones de segmento, administrar tus extensiones de segmento y ejecutar actualizaciones automatizadas de los miembros, consulta [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/).
{% endalert %}

Por último, puedes [utilizar esta Extensión de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-5-use-your-extension-in-a-segment) dentro de un segmento Braze para enviar una campaña o Canvas a esta audiencia.

## Consideraciones

- Una extensión de segmento sólo puede hacer referencia a datos de una conexión, no de varias.    
- Una extensión de segmento puede utilizar uno de los siguientes elementos como origen de datos: Datos CDI o datos Braze Snowflake (Currents). No puedes mezclar orígenes de datos dentro de una Extensión de segmento, pero puedes crear varias Extensiones de segmento para referenciarlas juntas dentro de un segmento.

## Solución de problemas

- Tu consulta podría agotarse cuando alcance tu tiempo máximo de ejecución, que se configura para cada sincronización de conexión en la página de **Ingesta de datos en la nube**. La duración máxima permitida es de 60 minutos.
- Asegúrate de que tu SQL está escrito utilizando la sintaxis adecuada para tu almacén de datos. 
