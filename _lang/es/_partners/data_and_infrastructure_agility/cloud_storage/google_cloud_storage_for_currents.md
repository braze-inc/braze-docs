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



- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

{% alert note %}
 <br><br>En raras circunstancias, Google Cloud puede finalizar las conexiones antes de tiempo, lo que provoca que Braze escriba archivos incompletos en Google Cloud Storage. 
{% endalert %}



![]({% image_buster /assets/img/gcs2.png %})

### Paso 2: 

#### Paso 2.1: 

Crea una nueva cuenta de servicio en tu consola de Google Cloud Platform accediendo a **IAM y admin** > **Cuentas de servicio** y seleccionando **Crear cuenta de servicio**.

![]({% image_buster /assets/img/gcs3.png %})

A continuación, asigna un nombre a la cuenta de servicio y concédele acceso al rol personalizado que acabas de crear.



#### Paso 2.2: Crear una clave

En la parte inferior de la página, utilice el botón **Crear clave** para crear una clave privada **JSON** y utilizarla en Braze. Una vez creada la clave, se descargará en tu máquina.

![]({% image_buster /assets/img/gcs5.png %})

### Paso 3: Configurar corrientes en Braze

En Braze, ve a **Corrientes** > **\+ Crear corriente** > **Exportación de datos de Google Cloud Storage** e indica tu nombre de integración y tu correo electrónico de contacto.

A continuación, sube tu clave privada JSON en **Credenciales JSON** de CGS e indica tu nombre de contenedor de CGS y el prefijo de CGS (opcional). 

{% alert important %}
Es importante que mantengas actualizado tu archivo de credenciales; si las credenciales de tu conector caducan, el conector dejará de enviar eventos. Si esto persiste durante más de **48 horas**, los eventos del conector se eliminarán y los datos se perderán permanentemente.
{% endalert %}

![La página Google Cloud Storage Currents en Braze. 

Por último, desplácese hasta la parte inferior de la página y seleccione los eventos de participación en mensajes o los eventos de comportamiento del cliente que desea exportar. Cuando hayas terminado, lanza tu Corriente.

### Paso 4: 

Para configurar las exportaciones de Google Cloud Storage (GCS), vaya a **Socios tecnológicos** > **Google Cloud Storage**, introduzca sus credenciales de GCS y seleccione **Convertir este destino en el destino predeterminado de exportación de datos**.



{% alert important %}

{% endalert %}



### Paso 5: 



- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`





## Comportamiento de la exportación

Los usuarios que hayan integrado una solución de almacenamiento de datos en la nube e intenten exportar API, informes de cuadros de mando o informes CSV experimentarán lo siguiente:

- Todas las exportaciones de la API no devolverán una URL de descarga en el cuerpo de la respuesta y deberán recuperarse a través del almacenamiento de datos.
- Todos los informes del panel de control y los informes CSV se enviarán al correo electrónico de los usuarios para su descarga (sin necesidad de permisos de almacenamiento) y se guardarán en el almacenamiento de datos.

## Solución de problemas

### 



```
Google Cloud Storage Credentials are invalid. Please ensure that your credentials string, bucket name, and prefix are valid. You do not have read permission.
```



- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`


