---
nav_title: Preguntas frecuentes
article_title: Currents FAQ
page_order: 9
page_type: reference
description: "Este artículo aborda algunas de las preguntas más frecuentes que surgen al configurar Braze Currents."
tool: Currents
---

# Preguntas más frecuentes

> Esta página ofrece respuestas a algunas preguntas frecuentes sobre Currents.

### ¿Cómo obtengo datos históricos?

Currents es una transmisión de datos en vivo y en tiempo real, lo que significa que los eventos no pueden reproducirse. Sin embargo, puedes almacenar los datos de Currents en un almacén de datos como [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) o [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/), para que puedas actuar sobre eventos pasados según te convenga. Los datos se conservan durante 30 días, pero para obtener más datos históricos, puedes consultar [Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/s3_to_snowflake/).

### ¿Por qué Currents emite los datos en formato Avro y no JSON?

Avro, a diferencia de JSON sin esquema, admite de forma nativa la evolución del esquema. También te beneficiarás de la posibilidad de enviar archivos Avro con menos ancho de banda y ahorrando espacio de almacenamiento, porque Avro es altamente compresible.

### ¿Cómo gestiona Braze la sobrecarga de archivos?

Creamos un proceso de extraer, transformar, cargar (ETL), que te permite extraer grandes cantidades de datos de una base de datos para colocarlos y almacenarlos en otra.

### ¿Dónde debo almacenar estos datos para realizar consultas?

Braze está asociado con varios almacenes de datos en los que puedes guardar tus datos para realizar consultas. Recomendamos utilizar:
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).

### ¿Qué tan fiables son los datos de Currents?

Currents garantiza la entrega "al menos una vez", lo que significa que ocasionalmente pueden escribirse eventos duplicados en tu contenedor de almacenamiento. Si tu caso de uso requiere entrega exactamente una vez, puedes deduplicar eventos utilizando el campo de identificador único (`id`) que se envía con cada evento. Para más detalles, consulta [Semántica de entrega de eventos]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/).

### ¿Con qué frecuencia se sincronizan los datos con Currents?

Los datos se transmiten de forma continua. Braze envía un lote de eventos cada vez que hay un lote completo listo para enviar, o cada 5 minutos, lo que ocurra primero. Para conectores de alto volumen, los datos llegan casi en tiempo real. Para conectores de bajo volumen, espera que los datos lleguen en un plazo de 5 a 30 minutos. Para más detalles, consulta [Umbral de escritura Avro]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/#avro-write-threshold).

{% alert note %}
Si un dispositivo no está conectado a internet, puede haber un retraso en la creación del evento. Esto es más común en los eventos de mensajes dentro de la aplicación, ya que los mensajes dentro de la aplicación pueden desencadenarse sin conexión.
{% endalert %}

### ¿Cómo puedo saber qué eventos están disponibles para Currents?

Para obtener una lista completa de los eventos que registra Currents, consulta los glosarios de [Eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) y [Eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/). Puedes filtrar estos glosarios por tipo de evento (como envíos, entregas o aperturas).

### ¿Se registran todos los eventos de envío en Currents?

Todos los eventos se registran en Currents. No hay escenarios en los que un evento se suprima intencionalmente de la transmisión de Currents.

### ¿Pueden corromperse los datos en Currents?

En circunstancias normales, los datos de Currents no se corrompen. Aunque siempre existe la posibilidad de un problema poco frecuente, no se conocen condiciones en las que los datos se corrompan de forma sistemática.

### ¿Por qué veo datos de eventos personalizados con fechas anteriores a la configuración de mi integración de Currents?

Braze no rellena eventos retroactivamente en Currents. Sin embargo, los eventos personalizados pueden registrarse con una marca de tiempo pasada (por ejemplo, si un dispositivo estaba sin conexión cuando ocurrió el evento y se sincronizó después). En estos casos, la marca de tiempo del evento refleja cuándo ocurrió originalmente, lo que puede ser anterior a la configuración de la integración de Currents.

### ¿Puedo incluir atributos personalizados en los eventos de envío de Currents?

No. Currents no incluye atributos personalizados en los eventos de envío. Currents registra eventos personalizados y eventos de interacción con mensajes. Para obtener una lista completa de los campos disponibles, consulta los [glosarios de eventos]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/).

### ¿Currents incluye etiquetas de campaña o pares clave-valor?

No. Currents no incluye etiquetas de campaña ni pares clave-valor a nivel de mensaje. Como alternativa, puedes usar un canal webhook en la campaña para enviar esta información a tu propio punto de conexión, utilizando [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) para incluir los datos de etiquetas y pares clave-valor mediante plantillas.

### ¿Cómo notifica Braze a los clientes sobre cambios en Currents?

Cuando se producen cambios en Currents (como nuevos campos de eventos o tipos de eventos), Braze envía un correo electrónico a todos los clientes con integraciones de Currents activas que hayan utilizado el dashboard en los últimos 30 días. También puedes consultar el [registro de cambios de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) para ver los últimos cambios.

### ¿Cuánto almacenamiento necesito para los datos de Currents?

Los requisitos de almacenamiento dependen del volumen de eventos y los tipos de eventos que estés exportando. Braze proporciona [eventos de ejemplo en formato Avro](https://github.com/braze-inc/currents-examples/tree/master/sample-data) que puedes usar para estimar el tamaño de los archivos para tu caso de uso.

### ¿Por qué el nombre de la campaña o del paso en Canvas aparece como `NULL` en mis datos de Currents?

Cuando creas una nueva campaña o Canvas, el nombre puede tardar un tiempo en propagarse por todos los sistemas de Braze. Los eventos enviados a través de Currents durante este período pueden tener `NULL` en los campos de nombre (como `campaign_name` o `canvas_step_name`). Esto también es esperado si el nombre se modificó poco antes de que se registraran los eventos. Para evitar esto, espera un tiempo después de crear o renombrar una campaña o un paso en Canvas antes de realizar envíos.

### ¿Qué sucede si mi contenedor de almacenamiento no está disponible cuando Currents intenta escribir datos?

Si tu contenedor de almacenamiento no está disponible en el momento de la transferencia de datos, esos datos se pierden. Braze no puede rellenar retroactivamente los eventos que no se entregaron correctamente. Para evitar la pérdida de datos, asegúrate de que tu contenedor de almacenamiento esté disponible y correctamente configurado en todo momento.

### ¿Con qué frecuencia se actualiza el ID de esquema?

Los ID de esquema son globales para todos los tipos de eventos y se incrementan de forma secuencial. Las actualizaciones pueden ocurrir en cualquier momento, y Braze notificará a los clientes por correo electrónico sobre los próximos cambios. Cada vez que se produce una actualización de esquema para cualquier tipo de evento, se asigna el siguiente ID global disponible. Recomendamos leer los archivos de forma recursiva desde la ruta raíz para gestionar los cambios de ID de esquema. Para más detalles, consulta [Cambios en el esquema Avro]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/#avro-schema-changes).