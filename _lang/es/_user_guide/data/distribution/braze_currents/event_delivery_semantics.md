---
nav_title: Semántica de la entrega de eventos
article_title: Semántica de la entrega de eventos
page_order: 3
page_type: reference
description: "Este artículo de referencia describe y define cómo Currents gestiona los datos de eventos de archivos planos que enviamos a los socios de Almacenamiento de Datos."
tool: Currents

---

# Semántica de la entrega de eventos

> Esta página describe y define cómo Currents gestiona los datos de eventos de archivo plano que enviamos a los socios de Almacenamiento de Datos.

Currents para almacenamiento de datos es una transmisión continua de datos desde nuestra plataforma a un contenedor de almacenamiento en una de las [conexiones de]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) nuestro [socio de]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) almacén de datos. Currents escribe archivos Avro en tu contenedor de almacenamiento en umbrales regulares, lo que te permite procesar y analizar los datos de eventos con tu propio conjunto de herramientas de inteligencia empresarial (BI).

{% alert important %}
Este contenido **sólo se aplica a los datos de eventos de archivos planos que enviamos a los socios de almacenamiento de datos (Google Cloud Storage, Amazon S3 y Microsoft Azure Blob Storage)**. <br><br>Para el contenido que se aplica a otros socios, consulta nuestra lista de [socios disponibles]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) y comprueba sus respectivas páginas.
{% endalert %}

## Entrega única

Como sistema de alto rendimiento, Currents proporciona una entrega de eventos "al menos una vez", lo que significa que ocasionalmente pueden escribirse eventos duplicados en tu contenedor de almacenamiento. Esto puede ocurrir cuando se reprocesan eventos de nuestra cola por cualquier motivo.

Si tus casos de uso requieren una entrega "exactamente una vez", puedes utilizar el campo identificador único que se envía con cada evento (`id`) para deduplicar los eventos. Como el archivo sale de nuestro control cuando se escribe en tu contenedor de almacenamiento, no tenemos forma de garantizar la deduplicación desde nuestro lado.

## Marcas de tiempo

Todas las marcas de tiempo exportadas por Currents se envían en la zona horaria UTC. Para algunos eventos en los que está disponible, también se incluye un campo de zona horaria, que entrega el formato de la Autoridad de Números Asignados de Internet (IANA) de la zona horaria local del usuario en el momento del evento.

### Latencia

Los eventos enviados a Braze a través del SDK o la API pueden incluir una marca de tiempo del pasado. El ejemplo más notable es cuando los datos del SDK se ponen en cola, como cuando no hay conectividad móvil. En ese caso, la marca de tiempo del evento reflejará cuándo se generó el evento. Esto significa que un porcentaje de eventos parecerá tener una latencia alta.

## Formato Apache Avro

Las integraciones de almacenamiento de datos de Braze Currents dan salida a los datos en el formato `.avro`. Elegimos [Apache Avro](https://avro.apache.org/) porque es un formato de datos flexible que admite de forma nativa la evolución de esquemas y es compatible con una amplia variedad de productos de datos: 

- Avro es compatible con casi todos los principales almacenes de datos.
- En caso de que desees dejar tus datos en S3, Avro comprime mejor que CSV y JSON, por lo que pagas menos por el almacenamiento y potencialmente puedes utilizar menos CPU para analizar los datos.
- Avro requiere esquemas cuando se escriben o leen datos. Los esquemas pueden evolucionar con el tiempo para gestionar la adición de campos sin romperse.

Currents creará un archivo para cada tipo de evento utilizando el siguiente formato:

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>+<partition>+<offset>.avro
```

{% alert tip %}
¿No puedes ver el código debido a la barra de desplazamiento? Aprende a solucionarlo [aquí]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/).
{% endalert %}

|Filename Segmento |Definición|
|---|---|
| `<your-bucket-prefix>` | El prefijo establecido para esta integración de Currents. |
| `<cluster-identifier>` | Para uso interno de Braze. Será una cadena como "prod-01", "prod-02", "prod-03" o "prod-04". Todos los archivos tendrán el mismo identificador de grupo.|
| `<connection-type-identifier>` | El identificador del tipo de conexión. Las opciones son "S3", "AzureBlob" o "GCS". |
| `<integration-id>` | El ID único de esta integración de Currents. |
| `<event-type>` | El tipo de evento en el archivo. |
| `<date>` | La hora a la que los eventos se ponen en cola en nuestro sistema para ser procesados en la zona horaria UTC. Formato AAAA-MM-DD-HH. |
| `<schema-id>` | Se utiliza para versionar los esquemas de `.avro` para la compatibilidad con versiones anteriores y la evolución de los esquemas. Entero. |
| `<zone>` | Para uso interno de Braze. |
| `<partition>` | Para uso interno de Braze. Entero. |
| `<offset>`| Para uso interno de Braze. Entero. Ten en cuenta que diferentes archivos enviados dentro de la misma hora tendrán un parámetro `<offset>` diferente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Las convenciones para nombrar los archivos pueden cambiar en el futuro. Braze recomienda buscar todas las claves de tu contenedor que tengan el prefijo <your-bucket-prefix>.
{% endalert %}

### Umbral de escritura Avro

En circunstancias normales, Braze escribirá archivos de datos en tu contenedor de almacenamiento cada 5 minutos o cada 15.000 eventos, lo que ocurra antes. Con una carga pesada, podemos escribir archivos de datos más grandes, con hasta 100.000 eventos por archivo.

{% alert important %}
Currents nunca escribirá archivos vacíos.
{% endalert %}

### Cambios en el esquema Avro

De vez en cuando, Braze puede realizar cambios en el esquema Avro cuando se añadan, cambien o eliminen campos. A nuestros efectos, hay dos tipos de cambios: los que rompen y los que no rompen. En todos los casos, se avanzará en `<schema-id>` para indicar que se ha actualizado el esquema. Los eventos Currents escritos en Azure Blob Storage, Google Cloud Storage y Amazon S3 escribirán el `<schema-id>` en la ruta. Por ejemplo `<your-bucket-name0>/<currents-integration-id>/<event-type>/<date-of-event>/<schema-id>/<environment>/<avro-file>`.

#### Cambios sin ruptura

Cuando se añade un campo al esquema Avro, lo consideramos un cambio no rupturista. Los campos añadidos serán siempre campos Avro "opcionales" (como con un valor predeterminado de `null`), por lo que "coincidirán" con esquemas antiguos según la [especificación Avro de resolución de esquemas](http://avro.apache.org/docs/current/spec.html#schema+resolution). Estas adiciones no deben afectar a los procesos existentes de Extraer, Transformar, y Cargar (ETL), ya que el campo simplemente se ignorará hasta que se añada a tu proceso ETL. 

{% alert important %}
Te recomendamos que la configuración de tu ETL sea explícita sobre los campos que procesa, para evitar que se rompa el flujo cuando se añadan nuevos campos.
{% endalert %}

Aunque nos esforzaremos por avisar con antelación en el caso de todos los cambios, podemos incluir cambios no rupturistas en el esquema en cualquier momento.

#### Cambios de última hora

Cuando un campo se elimina o se modifica en el esquema Avro, lo consideramos un cambio de ruptura. Los cambios de rotura pueden requerir modificaciones en los procesos ETL existentes, ya que es posible que los campos que se utilizaban ya no se registren como se esperaba.

Todos los cambios de última hora en el esquema se comunicarán con antelación al cambio.
