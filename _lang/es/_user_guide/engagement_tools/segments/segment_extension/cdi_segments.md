---
nav_title: Segmentos CDI
article_title: Segmentos CDI
page_order: 0
page_type: reference
tool: 
- Segments
description: "En este artículo se explica cómo configurar la segmentación por ubicación, que permite segmentar a los usuarios por ubicación."

---

# Segmentos CDI

> Con Braze [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/) (CDI), puede configurar una conexión directa desde su almacén de datos o sistema de almacenamiento de archivos a Braze para sincronizar datos relevantes de usuarios o catálogos de forma recurrente.

{% alert warning %}
Esta función consulta directamente su almacén de datos, por lo que incurrirá en todos los costes asociados a la ejecución de estas consultas en su almacén de datos. Los segmentos CDI no consumen [créditos de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#monitoring-your-sql-segments-usage), no cuentan para su límite de extensión de segmento y no consumen puntos de datos.
{% endalert %}

## Requisitos previos

Para utilizar los datos de su almacén de datos para la segmentación dentro de su espacio de trabajo Braze, tendrá que crear una [fuente conectada]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/) y, a continuación, crear un segmento CDI dentro de sus [extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). Los segmentos CDI le permiten escribir SQL que consulta directamente su propio almacén de datos utilizando los datos disponibles a través de sus conexiones CDI, y crear un grupo de usuarios a los que puede dirigirse dentro de Braze.

## Creación de un segmento CDI

### Paso 1: Configura tu fuente

Antes de crear su primer Segmento CDI, configure una nueva Fuente Conectada con su almacén de datos siguiendo los pasos en [Fuentes Conectadas]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/).

### Paso 2: Crear un segmento

En primer lugar, cree una nueva [Extensión de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) y, a continuación, seleccione **Actualización completa**.

![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

Para tu origen de datos, elige **Tablas de datos CDI**.

![]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

Como parte de su configuración CDI, puede seleccionar entre diferentes conexiones para utilizar en segmentos CDI. Cada conexión tiene un conjunto específico de tablas de datos. Su equipo de desarrollo puede configurar sus conexiones y tablas de datos durante la configuración de CDI.

Para ver las tablas de datos disponibles, seleccione **Referencia**. Cuando estés listo, selecciona una conexión.

![]({% image_buster /assets/img/segment/connection_schema.png %}){: style="max-width:100%;"}

A continuación, escribe el SQL para tu segmento utilizando [la sintaxis SQL de Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#writing-sql).

Tenga en cuenta que todos los segmentos CDI deben utilizar `external_user_id` como columna seleccionada, y su `external_user_id` debe coincidir con el establecido en Braze para los usuarios. Si los resultados de la consulta incluyen usuarios que no existen en Braze, dichos usuarios serán ignorados. Braze no creará nuevos usuarios basándose en la salida de su segmento CDI.

{% alert tip %}
Para obtener más información sobre cómo obtener una vista previa del segmento, gestionarlo y ejecutar actualizaciones automáticas de los miembros, consulte [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/).
{% endalert %}

Por último, puede [utilizar esta Extensión de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-5-use-your-extension-in-a-segment) dentro de un segmento Braze para enviar una campaña o Canvas a este público.

## Consideraciones

- Una extensión de segmento sólo puede hacer referencia a datos de una conexión, no de varias.    
- Una extensión de segmento puede utilizar una de las siguientes fuentes de datos: Datos CDI o datos Braze Snowflake (Corrientes). No se pueden mezclar fuentes de datos dentro de una Extensión de Segmento, pero se pueden crear múltiples Extensiones de Segmento para referenciarlas juntas dentro de un segmento.

## Solución de problemas

- Su consulta podría agotarse cuando alcance su tiempo máximo de ejecución, que se configura para cada sincronización de conexión en la página de **ingestión de datos en la nube**. La duración máxima permitida es de 60 minutos.
- Asegúrese de que su SQL está escrito utilizando la sintaxis adecuada para su almacén de datos. 
