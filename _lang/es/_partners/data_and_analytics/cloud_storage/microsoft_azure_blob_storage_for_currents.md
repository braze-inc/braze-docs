---
nav_title: Microsoft Azure Blob Storage
article_title: Microsoft Azure Blob Storage
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "Este artículo de referencia describe la asociación entre Braze Currents y Microsoft Azure Blog Storage, un almacenamiento de objetos masivamente escalable para datos no estructurados."
page_type: partner
tool: Currents
search_tag: Partner

---

# Microsoft Azure Blob Storage

> [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) es un almacenamiento de objetos masivamente escalable para datos no estructurados ofrecido por Microsoft como parte de la línea de productos Azure.

{% alert important %}
Si cambias de proveedor de almacenamiento en la nube, ponte en contacto con tu administrador del éxito del cliente de Braze para que te ayude a configurar y validar tu nueva integración.
{% endalert %}

La integración de Braze y Microsoft Azure Blob Storage te permite exportar datos a Azure y transmitir datos a Currents. Más tarde, puedes utilizar un proceso ETL (Extraer, Transformar, Cargar) para transferir tus datos a otras ubicaciones.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de almacenamiento de Microsoft Azure y Azure | Se necesita una cuenta de Microsoft Azure y de almacenamiento Azure para aprovechar esta asociación. |
| Currents | Para exportar datos a Currents, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) para tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

Para integrarte con Microsoft Azure Blob Storage, debes tener una cuenta de almacenamiento y una cadena de conexión que permita a Braze exportar datos a Azure o transmitir datos a Currents.

### Paso 1: Crear una cuenta de almacenamiento

En Microsoft Azure, ve a **Cuentas de almacenamiento** en la barra lateral y haz clic en **\+ Añadir** para crear una nueva cuenta de almacenamiento. A continuación, proporciona un nombre de cuenta de almacenamiento. No será necesario actualizar otras configuraciones predeterminadas. Por último, selecciona **Revisar + crear**. 

Aunque ya tengas una cuenta de almacenamiento, te recomendamos que crees una nueva específicamente para tus datos de Braze.

![]({% image_buster /assets/img/azure-currents-step-1.png %})

### Paso 2: Obtener la cadena de conexión

Una vez desplegada la cuenta de almacenamiento, ve al menú **Claves de acceso** desde la cuenta de almacenamiento y toma nota de la cadena de conexión.

Microsoft proporciona dos claves de acceso para mantener las conexiones utilizando una clave mientras se regenera la otra. Sólo necesitas la cadena de conexión de uno de ellos.

{% alert note %}
Braze utiliza la cadena de conexión de este menú, no la clave.
{% endalert %}

![]({% image_buster /assets/img/azure-currents-step-2.png %})

### Paso 3: Crear un contenedor de servicio blob

Navega hasta el menú **Blobs** en la sección **Servicio Blob** de tu cuenta de almacenamiento. Crea un Contenedor de Servicio Blob dentro de la cuenta de almacenamiento que creaste anteriormente. 

Proporciona un nombre para tu Contenedor de Servicios Blob. No será necesario actualizar otras configuraciones predeterminadas.

![]({% image_buster /assets/img/azure-currents-step-3.png %})

### Paso 4: Configurar Currents

En Braze, ve a **Currents > + Crear corriente > Exportación de datos Azure Blob** e indica el nombre de tu integración y tu correo electrónico de contacto.

A continuación, proporciona tu cadena de conexión, el nombre del contenedor y el prefijo BlobStorage (opcional).

![La página Microsoft Azure Blob Sstorage de Currents en Braze. En esta página existen campos para el nombre de la integración, el correo electrónico de contacto, la cadena de conexión, el nombre del contenedor y el prefijo.]({% image_buster /assets/img/maz.png %})

Por último, desplázate hasta la parte inferior de la página y selecciona los eventos de interacción con los mensajes o los eventos de comportamiento del cliente que deseas exportar. Cuando hayas terminado, lanza tu Current.

### Paso 5: Configurar la exportación de datos a Azure

A continuación se configuran las credenciales que se utilizan para:
1. Exportación de segmentos a través de la API
2. Exportación de CSV (campaña, segmento, exportación de datos de usuario de Canvas a través del panel)
3. Informes de interacción

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** > **Microsoft Azure** y proporciona tu cadena de conexión, el nombre del contenedor de almacenamiento Azure y el prefijo de almacenamiento Azure.

A continuación, asegúrate de que está marcada la casilla **Hacer de este el destino predeterminado de la exportación de** datos, así te asegurarás de que los datos exportados se envían a Azure. Cuando hayas terminado, guarda tu integración.

![La página de exportación de datos de Microsoft Azure en Braze. En esta página existen campos para la cadena de conexión, el nombre del contenedor y el prefijo.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
Es importante que mantengas actualizada tu cadena de conexión; si las credenciales de tu conector caducan, este dejará de enviar eventos. Si esto persiste durante más de **48 horas**, los eventos del conector se eliminarán y los datos se perderán permanentemente.
{% endalert %}

## Comportamiento de la exportación

Los usuarios que hayan integrado una solución de almacenamiento de datos en la nube e intenten exportar API, informes de cuadros de mando o informes CSV experimentarán lo siguiente:

- Todas las exportaciones de la API no devolverán una URL de descarga en el cuerpo de la respuesta y deberán recuperarse a través del almacenamiento de datos.
- Todos los informes del panel y los informes CSV se enviarán al correo electrónico del usuario para su descarga (sin necesidad de permisos de almacenamiento) y se realizará una copia de seguridad en el almacenamiento de datos. 
