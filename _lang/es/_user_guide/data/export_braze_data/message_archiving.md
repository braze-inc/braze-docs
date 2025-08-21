---
nav_title: Archivado de mensajes
article_title: Archivado de mensajes
alias: "/message_archiving/"
page_order: 0
page_type: reference
description: "Este artículo de referencia trata sobre el archivado de mensajes, una función que permite guardar una copia de los mensajes enviados a los usuarios."

---

# Archivo de mensajes

> El archivado de mensajes le permite guardar una copia de los mensajes enviados a los usuarios con fines de archivado o cumplimiento en su bucket de AWS S3, contenedor de Azure Blob Storage o bucket de Google Cloud Storage. <br><br> Este artículo explica cómo configurar el archivo de mensajes, las referencias a las cargas útiles JSON y las preguntas más frecuentes.

El archivado de mensajes está disponible como característica adicional. Para empezar a archivar mensajes, ponte en contacto con tu administrador del éxito del cliente de Braze.

## Cómo funciona

Cuando esta característica está activada, si has conectado un contenedor de almacenamiento en la nube a Braze y lo has marcado como destino predeterminado de exportación de datos, Braze escribirá un archivo JSON comprimido con gzip en tu contenedor de almacenamiento en la nube por cada mensaje enviado a un usuario a través de tus canales seleccionados (correo electrónico, SMS/MMS o push). 

Este fichero contendrá los campos definidos en [Referencias de ficheros](#file-references) y reflejará los mensajes finales planificados enviados al usuario. Cualquier valor de plantilla definido en su campaña (por ejemplo, {% raw %}`{{${first_name}}}`{% endraw %}) mostrará el valor final que el usuario recibió basado en la información de su perfil. Esto te permite conservar una copia del mensaje enviado para satisfacer requisitos de cumplimiento, auditoría o atención al cliente.

Si configuras credenciales para varios proveedores de almacenamiento en la nube, el archivado de mensajes sólo se exportará al marcado explícitamente como destino predeterminado de exportación de datos. Si no se proporciona ningún valor predeterminado explícito y se conecta un bucket de AWS S3, el archivado de mensajes se cargará en ese bucket.

{% alert important %}
Activar esta característica afectará a la velocidad de entrega de tus mensajes, ya que la carga del archivo se realiza inmediatamente antes de enviar el mensaje para mantener la precisión. La latencia introducida por el archivado de mensajes dependerá del proveedor de almacenamiento en la nube y del rendimiento y tamaño de los documentos guardados.
{% endalert %}

El JSON se guardará en su cubo de almacenamiento utilizando la siguiente estructura de claves:

`sent_messages/{channel, one of: email, push, sms}/{MD5 digest of downcased: email address, push token, or E.164 phone number}/{campaign or Canvas step API ID}/{dispatch ID}.json.gz`

Un archivo de ejemplo puede tener este aspecto:

`sent_messages/email/819baa08d8d7e77e19d4666f5fc6050b/ee965cb2-8934-4b0a-acf1-91c899c2f915/651fd10b282850b39e1169c13975234b.json.gz`

{% alert note %}
El resumen MD5 sólo puede calcularse utilizando una dirección de correo electrónico, un token de notificaciones push o un número de teléfono E.164 conocidos. No se puede invertir un compendio MD5 conocido para obtener la dirección de correo electrónico, el token de notificaciones push o el número de teléfono de E.164.
{% endalert %}

{% alert tip %}
**¿Tienes problemas para encontrar tus tokens de notificaciones push en tus contenedores?**<br>
Braze reduce tus tokens de notificaciones push antes de aplicarles el hash. El resultado es que el token de notificaciones push `Test_Push_Token12345` se reduce a `test_push_token12345` en la ruta de claves con el hash `32b802170652af2b5624b695f34de089`.
{% endalert %}

## Configurar el archivado de mensajes

Esta sección te guía en la configuración del archivo de mensajes para tu espacio de trabajo. Antes de continuar, confirme que su empresa ha adquirido y activado el archivado de mensajes.

### Paso 1: Conecta un contenedor de almacenamiento en la nube

Si aún no lo has hecho, conecta un contenedor de almacenamiento en la nube a Braze. Para conocer los pasos, consulte la documentación de nuestros socios sobre [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/), [Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) o [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).

### Paso 2: Seleccionar canales para archivar mensajes

La página de configuración de **Archivado de mensajes** controla qué canales guardarán una copia de los mensajes enviados en tu cubo de almacenamiento en la nube.

Para seleccionar canales:

1. Vaya a **Configuración** > **Archivo de mensajes**.
2. Selecciona tus canales.
3. Seleccione **Guardar cambios**.

![La página Archivado de mensajes tiene tres canales para seleccionar: Email, Push, and SMS.]({% image_buster /assets/img/message_archiving_settings.png %})

{% alert note %}
Si no ve el **Archivo de mensajes** en **Configuración**, confirme que su empresa ha adquirido y activado el archivo de mensajes.
{% endalert %}

## Referencias de archivos

Las siguientes son referencias de la carga útil JSON entregada a su cubo de almacenamiento en la nube cada vez que se envía un mensaje. Consulte nuestro repositorio de ejemplos de código para ver [archivos de ejemplo de archivo de mensajes](https://github.com/braze-inc/braze-examples/tree/main/message-archiving).

{% tabs %}
{% tab Correo electrónico %}

```json
{
  "version" : 1, //numerical version of the json structure
  "to": ToAddress, ("customer@example.com")
  "subject": SubjectLine ("20% off coupon inside!"),
  "from_name": DisplayName ("Braze"),
  "from_address": FromAddress ("no-reply@braze.com"),
  "html_body": HtmlBody,
  "plaintext_body": PlainTextBody,
  "amp_body": AMPEmailBody,
  "extras": Extra hash—for SendGrid users, this will be passed to SendGrid as Unique Arguments,
  "headers": HashOfHeaders,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessageVariationApiId, // may not be available,
  "attachments": Array of JSON Objects containing 'bytes' and 'file_name', // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is a from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

El campo `extras` al que se hace referencia en esta carga útil procede de los pares clave-valor añadidos en el campo **Email Extras** al redactar un correo electrónico. Para enviar datos de vuelta a Currents, consulta [Extras de mensajes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/).

![]({% image_buster /assets/img_archive/email_extras.png %}){: style="max-width:60%" }

{% endtab %}
{% tab SMS/MMS %}

```json
{
  "version" : 1 //numerical version of the json structure
  "to": PhoneNumber, ("+15555555555"),
  "body": Body ("Hi there!"),
  "subscription_group": SubscriptionGroupExternalId,
  "provider": StringOfProviderName,
  "media_urls": ArrayOfString, // indicates a message is MMS
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is a from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% tab Push %}

```json
{
  "version" : 1, //numerical version of the json structure
  "to": PushToken,
  "payload": JsonOfEntirePushPayload,
  "platform": one of "android_push" | "ios_push" | "kindle_push" | "web_push",
  "app_id": ApiKeyOfApp,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is from a Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% endtabs %}

## Preguntas más frecuentes

### ¿Qué plantillas no se incluyen en la carga útil?

Las modificaciones realizadas después de que el mensaje salga de Braze no se reflejarán en el archivo guardado en tu contenedor de almacenamiento en la nube. Esto incluye las modificaciones que hacen nuestros socios de entrega de correo, como envolver los enlaces para el seguimiento de los clics e insertar píxeles de seguimiento.

### ¿Qué mensajes hay bajo el valor "no asociado" en la ruta de la campaña?

Cuando un mensaje se envía fuera de una campaña o Canvas, el ID de la campaña en el nombre del archivo será "no asociado". Esto ocurrirá cuando envíes mensajes de prueba desde el panel, cuando Braze envíe autorespuestas SMS/MMS o cuando los mensajes enviados a través de la API no especifiquen un ID de campaña.

### ¿Cómo puedo encontrar más información sobre este envío?

Puedes utilizar `external_id` o `dispatch_id` junto con `user_id` para cruzar el mensaje de la plantilla con nuestros datos de Currents y encontrar más información, como la fecha y hora en que se entregó, si el usuario abrió el mensaje o hizo clic en él, etc.

### ¿Cómo se gestionan los reintentos?

Si no se puede acceder a tu contenedor de almacenamiento en la nube, Braze lo reintentará hasta tres veces con un [jitter de retroceso](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter). Braze gestiona automáticamente los reintentos del límite de velocidad de AWS S3.

### ¿Qué ocurre si mis credenciales no son válidas?

Si tus credenciales de almacenamiento en la nube dejan de ser válidas en algún momento, Braze no podrá guardar ningún mensaje en tu contenedor de almacenamiento en la nube, y esos mensajes se perderán. Te recomendamos que configures tus [preferencias de notificación]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/notification_preferences/) para Amazon Web Services, Google Cloud Services o Azure (Microsoft Cloud Services) para que recibas alertas de cualquier problema con las credenciales.

### ¿Por qué la marca de tiempo de mi archivo `sent_at` difiere ligeramente de la marca de tiempo enviada en Currents?

La copia renderizada se carga inmediatamente antes de enviar el mensaje al usuario. Debido a los tiempos de carga del almacenamiento en la nube, puede haber un retraso de unos segundos entre la marca de tiempo `sent_at` de la copia renderizada y el momento real en que se produce el envío.

### ¿Puedo crear un nuevo contenedor específico para archivar mensajes manteniendo el contenedor actual utilizado para los datos de Currents?

No. Si estás interesado en crear estos contenedores específicos, envía [tus comentarios sobre el producto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

### ¿Se escriben los datos archivados en una carpeta específica de un contenedor existente, de forma similar a como se estructuran las exportaciones de datos de Currents?

Los datos se escriben en una sección `sent_messages` del contenedor. Consulta [Cómo funciona](#how-it-works) para más detalles.

