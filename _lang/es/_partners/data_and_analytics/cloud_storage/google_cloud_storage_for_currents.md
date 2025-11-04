---
nav_title: Google Cloud Storage
article_title: Google Cloud Storage
alias: /partners/google_cloud_storage_for_currents/
description: "Este artículo de referencia describe la asociación entre Braze y Google Cloud Storage, un almacenamiento de objetos masivamente escalable para datos no estructurados."
page_type: partner
tool: Currents
search_tag: Partner

---

# Google Cloud Storage

> [Google Cloud Storage](https://cloud.google.com/storage/) es un sistema de almacenamiento de objetos masivo y escalable para datos no estructurados ofrecido por Google como parte del paquete de productos Cloud Computing.

{% alert important %}
Si cambias de proveedor de almacenamiento en la nube, ponte en contacto con tu administrador del éxito del cliente de Braze para que te ayude a configurar y validar tu nueva integración.
{% endalert %}

La integración de Braze y Google Cloud Storage te permite transmitir datos de Currents a Google Cloud Storage. Posteriormente, puede utilizar un proceso ETL (Extract, Transform, Load) para transferir sus datos a otras ubicaciones, como Google BigQuery.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Google Cloud Storage | Se necesita una cuenta de Google Cloud Storage para beneficiarse de esta asociación. |
| Currents | Para volver a exportar datos a Google Cloud Storage, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) en tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

Para integrarse con Google Cloud Storage, debe configurar las credenciales adecuadas que permitan a Braze obtener información sobre los buckets de almacenamiento en los que se está escribiendo (`storage.buckets.get`) y crear objetos dentro de ese bucket (`storage.objects.create`). 

Para ello, siga las siguientes instrucciones, que le guiarán a través de la creación de un rol y una cuenta de servicio que generarán una clave privada para utilizarla en su integración de Currents.

### Paso 1: Crear rol

Crea un nuevo rol en tu consola de Google Cloud Platform accediendo a **IAM & admin** > **Roles** > **\+ Crear rol**.

![]({% image_buster /assets/img/gcs1.png %})

Dale un nombre al rol, luego selecciona **+Añadir permisos** y elige lo siguiente:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

{% alert note %}
El permiso `storage.objects.delete` es opcional. Permite a Braze limpiar los archivos incompletos.<br><br>En raras circunstancias, Google Cloud puede finalizar las conexiones antes de tiempo, lo que provoca que Braze escriba archivos incompletos en Google Cloud Storage. En la mayoría de los casos, Braze volverá a intentarlo y creará un nuevo archivo con los datos correctos, dejando el archivo antiguo en Google Cloud Storage.
{% endalert %}

Cuando hayas terminado, selecciona **Crear**.

![]({% image_buster /assets/img/gcs2.png %})

### Paso 2: Crear una nueva cuenta de servicio

#### Paso 2.1: Crear la cuenta de servicio

Crea una nueva cuenta de servicio en tu consola de Google Cloud Platform accediendo a **IAM y admin** > **Cuentas de servicio** y seleccionando **Crear cuenta de servicio**.

![]({% image_buster /assets/img/gcs3.png %})

A continuación, asigna un nombre a la cuenta de servicio y concédele acceso al rol personalizado que acabas de crear.

![En Google Cloud Platform, en la página de creación de servicios, escribe el nombre de tu rol en el campo "Seleccionar un rol".]({% image_buster /assets/img/gcs4.png %})

#### Paso 2.2: Crear una clave

En la parte inferior de la página, utilice el botón **Crear clave** para crear una clave privada **JSON** y utilizarla en Braze. Una vez creada la clave, se descargará en tu máquina.

![]({% image_buster /assets/img/gcs5.png %})

### Paso 3: Configurar corrientes en Braze

En Braze, ve a **Corrientes** > **\+ Crear corriente** > **Exportación de datos de Google Cloud Storage** e indica tu nombre de integración y tu correo electrónico de contacto.

A continuación, sube tu clave privada JSON en **Credenciales JSON** de CGS e indica tu nombre de contenedor de CGS y el prefijo de CGS (opcional). 

{% alert important %}
Es importante que mantengas actualizado tu archivo de credenciales; si las credenciales de tu conector caducan, el conector dejará de enviar eventos. Si esto persiste durante más de **48 horas**, los eventos del conector se eliminarán y los datos se perderán permanentemente.
{% endalert %}

![La página Google Cloud Storage Currents en Braze. En esta página existen campos para el nombre de la integración, el correo electrónico de contacto, la credencial JSON de la GCS, el nombre de contenedor de la GCS y el prefijo.]({% image_buster /assets/img/gcs6.png %})

Por último, desplácese hasta la parte inferior de la página y seleccione los eventos de participación en mensajes o los eventos de comportamiento del cliente que desea exportar. Cuando hayas terminado, lanza tu Corriente.

### Paso 4: Configurar las exportaciones de Google Cloud Storage

Para configurar las exportaciones de Google Cloud Storage (GCS), vaya a **Socios tecnológicos** > **Google Cloud Storage**, introduzca sus credenciales de GCS y seleccione **Convertir este destino en el destino predeterminado de exportación de datos**.

Ten en cuenta que la organización y el contenido de los archivos exportados serán idénticos en todas las integraciones de AWS S3, Microsoft Azure y Google Cloud Storage.

{% alert important %}
Asegúrate de introducir el valor JSON completo [generado por Google Cloud](https://cloud.google.com/iam/docs/keys-create-delete).
{% endalert %}

![La página de Google Cloud Storage en el panel de Braze.]({% image_buster /assets/img/gcs7.png %}){: style="max-width:70%;"}

### Paso 5: Comprueba las credenciales de tu cuenta de servicio (opcional)

Tu cuenta del servicio IAM de Google Cloud debe tener los siguientes permisos:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Para verificar estos permisos en el panel de Braze, ve a la página **Google Cloud Storage** y, a continuación, selecciona **Probar credenciales**.

![La sección de credenciales de Google Cloud Storage en el panel de Braze.]({% image_buster /assets/img/gcs8.png %}){: style="max-width:70%;"}

## Comportamiento de la exportación

Los usuarios que hayan integrado una solución de almacenamiento de datos en la nube e intenten exportar API, informes de cuadros de mando o informes CSV experimentarán lo siguiente:

- Todas las exportaciones de la API no devolverán una URL de descarga en el cuerpo de la respuesta y deberán recuperarse a través del almacenamiento de datos.
- Todos los informes del panel de control y los informes CSV se enviarán al correo electrónico de los usuarios para su descarga (sin necesidad de permisos de almacenamiento) y se guardarán en el almacenamiento de datos.

## Solución de problemas

### Las credenciales de Google Cloud Storage no son válidas

Si recibes el siguiente error al intentar introducir tus credenciales:

```
Google Cloud Storage Credentials are invalid. Please ensure that your credentials string, bucket name, and prefix are valid. You do not have read permission.
```

Asegúrate de que tu cuenta del servicio IAM de Google Cloud tiene los siguientes permisos:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Tras la verificación, puedes [comprobar tus credenciales en el panel de Braze](#step-5-test-your-service-account-credentials-optional).
