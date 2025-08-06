---
nav_title: Amperity
article_title: Amperity
alias: /partners/amperity/
description: "Este artículo de referencia describe la asociación entre Braze y Amperity, una plataforma integral de datos de clientes empresariales, que permite sincronizar usuarios de Amperity, unificar datos, enviar datos mediante buckets de AWS S3 a Braze y mucho más."
page_type: partner
search_tag: Partner

---

# Amperity

> [Amperity](https://amperity.com/) es una plataforma integral de datos de clientes empresariales que ayuda a las marcas a conocer a sus clientes, tomar decisiones estratégicas y adoptar sistemáticamente las medidas adecuadas para servir mejor a sus consumidores. Amperity proporciona funciones inteligentes de unificación de la gestión de datos, análisis, información y activación.

_Esta integración está mantenida por Amperity._

{% multi_lang_include video.html id="06G0lxaSjgk" align="right" %}

La integración de Braze y Amperity ofrece una visión unificada de sus clientes en las dos plataformas. Esta integración le permite:
- **Sincronizar perfiles de clientes**: Asigne datos de usuario y atributos personalizados de Amperity a Braze. 
- **Crea y envía audiencias**: Cree segmentos que devuelvan a Braze listas de clientes activos y sus atributos personalizados asociados, y envíelos a Braze.
- **Gestionar la actualización de datos**: Controla la frecuencia de envío de actualizaciones de atributos personalizados a Braze.
- **Unificar los datos**: Unifique los datos en varias plataformas compatibles con Amperity y Braze.
- **Sincroniza los datos de Braze con Amazon S3**: Utilice Braze Currents para integrar los datos de participación de las campañas Braze, lo que le permite sincronizar los datos con Amazon S3 en formato Apache Avro.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Amperity | Se necesita una [cuenta de Amperity](https://amperity.com/request-a-demo) para beneficiarse de esta asociación. |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos `users.track`. <br> Puede crearse en el panel de control de Braze accediendo a **Developer Console** > **Rest API Key** > **Create New API Key**. |
| Instancia de soldadura | Puedes obtener tu instancia de Braze a través de tu administrador de incorporación a Braze o en la [página de resumen de la API]({{site.baseurl}}/api/basics#endpoints). |
| Punto final REST Braze | La URL de tu punto final Braze. Tu punto final dependerá de tu instancia de Braze. |
| Conector de corriente (opcional) | El conector S3 Currents. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Mapeado de datos

Tanto los atributos estándar como los personalizados pueden enviarse de Amperity a Braze, lo que permite enriquecer los perfiles de los clientes en Braze con datos de diversas fuentes a través de Amperity. Los atributos específicos que puede enviar dependerán de los datos de su sistema Amperity y de los atributos que haya configurado en Braze.

Lea a continuación para conocer estos atributos.

### Atributos estándar 

[Los atributos del perfil]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) describen quiénes son sus clientes. A menudo se asocian a la identidad del cliente, por ejemplo:
- Nombres
- Fechas de nacimiento
- Direcciones de correo electrónico
- Números de teléfono

### Atributos personalizados 

[Los atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) en Braze son campos determinados por su marca. Si desea que Amperity gestione atributos personalizados que ya existen en Braze, alinee la salida que se envía desde Amperity con los nombres que ya están en su espacio de trabajo Braze. Esto puede incluir lo siguiente:
- Historial de compras
- Estatus de lealtad
- Niveles de valor
- Datos recientes sobre el compromiso

Verifique los nombres de los atributos personalizados que se enviarán a Braze desde Amperity. Amperity añadirá un atributo personalizado siempre que no haya un nombre coincidente.

Los atributos personalizados sólo se actualizarán para aquellos usuarios que tengan un `external_id` o `braze_id` coincidente en Braze.

### Audiencias Amperity

Las audiencias sincronizadas desde Amperity a Braze se registrarán en los perfiles de usuario como atributos personalizados. A continuación, pueden utilizarse para dirigirse a esos usuarios en Braze.

![Lista desplegable de filtros con atributos personalizados que se muestran en la categoría Datos personalizados.]({% image_buster /assets/img/amperity/custom_attributes_filters.png %}){: style="max-width:60%;"}

![Lista desplegable de atributos personalizados como "l12m_frequency" y "l12m_monetary".]({% image_buster /assets/img/amperity/search_custom_attributes_filters.png %}){: style="max-width:40%;"}

### Tipos de datos

Los tipos de datos admitidos son:
- Booleano
- Fecha
- Fecha y hora
- Decimal
- Flotante
- Entero
- Cadena
- Varchar

El tipo de datos utilizado depende de la naturaleza del atributo. Por ejemplo, una dirección de correo electrónico sería una cadena, mientras que la edad de un cliente podría ser un número entero.

### Duplicación de atributos

Evite enviar atributos personalizados que dupliquen campos predeterminados del perfil de usuario. Por ejemplo, las fechas de nacimiento deben enviarse a Braze como un campo de perfil de usuario llamado "dob" para que coincida con el atributo estándar de Braze. Si se envían como "birthday", "Birthdate" o cualquier otra cadena, se creará un atributo personalizado y los valores del campo "dob" no se actualizarán.

### Puntos de datos

Amperity realiza un seguimiento de los cambios entre las sincronizaciones con Braze y el estado de los envíos en general. Amperity sólo enviará a Braze los miembros de la lista y otros atributos elegidos que hayan cambiado desde la última sincronización.  

## Integración

### Paso 1: Capturar detalles de configuración para Braze

1. Crea una clave de API REST Braze para tu espacio de trabajo Braze con los permisos `users.track` en **Datos de usuario**. El endpoint `users.track` sincroniza la audiencia de Amperity con Braze como un atributo personalizado.
2. Determina el [punto final de la API REST]({{site.baseurl}}/api/basics#endpoints) para tu instancia de Braze. Por ejemplo, si tu URL de Braze es `https://dashboard-03.braze.com`, tu punto final de la API REST es `https://rest.iad-03.braze.com` y tu instancia es "US-03".
3. Determine una lista de [campos de perfil de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) y [atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) que pueden enviarse a Braze desde Amperity.

### Paso 2: Configurar Braze como destino-Operador DataGrid

#### Paso 2a: Construir la tabla de perfiles de clientes

Cree una nueva tabla llamada "Braze Customer Attributes" dentro de su base de datos Customer 360 en Amperity. Esta tabla debe contener todos los atributos de Braze que su marca desea gestionar desde Amperity, incluidos tanto los campos de perfil de usuario predeterminados requeridos por Braze como cualquier atributo personalizado. Utilice SQL para definir la estructura de esta tabla como se muestra en [la documentación de Amperity](https://docs.amperity.com/datagrid/destination_braze.html#customer-profiles-table).

#### Paso 2b: Nombrar, validar y guardar la tabla

Nombra la tabla "Braze Customer Attributes" y guárdala. Verifique que la tabla es accesible al **Editor de Segmentos** y al editor **Editar Atributos** dentro de las campañas.

#### Paso 2c: Añadir Braze como destino

En la plataforma Amperity, vaya a la pestaña **Destinos**. Busque la opción de añadir un nuevo destino. Entre las opciones disponibles, seleccione **Braze**.

![La sección Nuevo destino con el nombre "API Braze", la descripción "Enviar atributos de audiencia a Braze" y el plugin "Braze".]({% image_buster /assets/img/amperity/destination_name.png %}){: style="max-width:60%;"}

#### Paso 2d: Configurar los detalles del destino

En **Configuración de Braze**, proporcione las credenciales de Braze y la configuración de destino, como se muestra en [la documentación de Amperity](https://docs.amperity.com/datagrid/destination_braze.html#add-destination). Introduzca los datos de configuración recogidos en el último paso y defina el identificador Braze. Los identificadores disponibles son:
- `braze_id`: Identificador Braze asignado automáticamente, inalterable y asociado a un usuario concreto cuando se crea en Braze.
- `external_id`: Un identificador asignado por el cliente, normalmente un UUID. 

![La sección de configuración de Braze con una instancia de "US-03", un identificador de usuario de "external_id", un nombre de segmento en blanco, un contenedor de S3 de "amperity-training-abc123" y una carpeta de S3 de "braze-attributes".]({% image_buster /assets/img/amperity/braze_settings.png %}){: style="max-width:60%;"}

#### Paso 2e: Añadir un modelo de datos

En la pestaña **Destinos**, abra el menú del destino Braze y seleccione **Añadir plantilla de datos**. Introduzca un nombre y una descripción para la plantilla (por ejemplo, "Braze" y "Enviar atributos personalizados a Braze"), verifique el acceso de los usuarios empresariales y compruebe todos los ajustes de configuración. 

Si alguna configuración necesaria no se configuró como parte del destino, configúrela como parte de la plantilla de datos. Guarde el modelo de datos.

![La sección Nombre de la plantilla de datos con el nombre "Atributos de audiencia Braze" y la descripción "Enviar atributos de audiencia a Braze".]({% image_buster /assets/img/amperity/data_template_name.png %}){: style="max-width:60%;"}

#### Paso 2f: Guardar la configuración 

Después de rellenar los datos necesarios, guarda la configuración. Ahora que Braze está configurado como destino, los usuarios de Amp360 y AmpIQ pueden sincronizar datos con Braze.

### Paso 3: Sincronizar datos con Braze

Asegúrate de que Braze está habilitado para tu inquilino de Amperity. Si no es así, póngase en contacto con su operador de DataGrid o con un representante de Amperity para obtener ayuda.

A continuación, siga las instrucciones de sincronización de Amp360 o AmpIQ según corresponda a su empresa.

#### Opción de sincronización 1: Envía los resultados de la consulta a Braze a través de Amp360

Los usuarios de Amp360 pueden utilizar SQL para escribir consultas de forma libre y, a continuación, configurar una programación que envíe los resultados a Braze.

##### Paso 1: Crear una consulta en Amperity

Vaya a la función de consulta de Amperity y cree una consulta SQL que genere el conjunto de datos de clientes deseado. Los resultados deben incluir los atributos específicos que desea enviar a Braze. Consulte este ejemplo de consulta de Amperity para obtener una lista de usuarios con sus historiales de compra.

##### Paso 2: Añadir una nueva orquestación en Amperity

1. Vaya a la sección **Orquestación** y haga clic en la opción para añadir una nueva orquestación. 
2. Especifica qué debe hacer la orquestación. Esto suele implicar especificar la consulta SQL que debe ejecutarse y dónde deben enviarse los resultados. En este caso, seleccione la consulta SQL que creó para generar la lista de clientes activos y especifique Braze como destino de los resultados.
3. Define cuándo y con qué frecuencia debe ejecutarse la orquestación. Por ejemplo, puedes ejecutar la orquestación diariamente a una hora determinada.
4. Guarde la orquestación después de configurarla a su gusto. Se añadirá a tu lista de orquestaciones en Amperity.
5. Pruebe la orquestación para asegurarse de que funciona como se espera. Puede hacerlo activando manualmente la orquestación y comprobando los resultados en Braze.

##### Paso 3: Ejecutar la orquestación 

Ejecute la orquestación para ejecutar la consulta y enviar los resultados a Braze. Esto puede hacerse manualmente o según el calendario que hayas establecido en los ajustes de orquestación.

#### Opción de sincronización 2: Enviar audiencias a Braze mediante AmpIQ

Los usuarios de AmpIQ pueden crear segmentos en Amperity a través de una interfaz no SQL y sincronizarlos con destinos posteriores como Braze. Los usuarios pueden seleccionar destinos y, a continuación, configurar una lista de atributos que se enviarán a cada destino.

##### Paso 1: Crear un segmento en Amperity 

Cree un segmento en Amperity que devuelva una lista de clientes. Este segmento debe estar asociado a los atributos personalizados que desea actualizar en Braze.

{% alert note %}
Consulte la documentación de Amperity para ver ejemplos de los distintos tipos de segmentos que puede enviar a Braze.
{% endalert %}

##### Paso 2: Crear una campaña en Amperity

1. Vaya a la sección **Campaña** y haga clic en la opción para crear una nueva campaña.
2. Dale a tu campaña un nombre descriptivo y único que te ayude a identificarla más adelante, sobre todo si tienes varias campañas.
3. Seleccione el segmento de clientes al que desea dirigirse con esta campaña. Este debería ser el segmento que creó anteriormente. <br>![El campo desplegable de los segmentos a excluir de la segmentación.]({% image_buster /assets/img/amperity/select_segments.png %}){: style="max-width:50%;"}<br><br>
4. Elija los datos que desea enviar como parte de la campaña. Esto puede incluir una serie de atributos del cliente. ![El modal Editar atributos de la campaña permite seleccionar un destino y atributos del cliente. ]({% image_buster /assets/img/amperity/edit_campaign_attributes.png %}){: style="max-width:90%;"}<br><br>
5. Seleccione **Braze** como destino al que se enviarán los datos de la campaña.
6. Elija cuándo y con qué frecuencia desea que se ejecute la campaña. Puede ser un acontecimiento puntual o un programa recurrente.
7. Guarde su campaña y ejecute una prueba para asegurarse de que funciona como se espera.

##### Paso 3: Ejecutar la campaña

Ejecute la campaña para enviar el segmento a Braze. Esto puede hacerse manualmente o según el calendario que haya establecido en la configuración de la campaña.


### Uso de la amperiosidad con corrientes de soldadura fuerte
Para enviar los datos de Braze Currents a Amperity:
1. [Configura una Braze Currents]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/) para enviar datos a un contenedor de S3 de Amazon.
2. Configure Amperity para [leer archivos Apache Avro de ese bucket de Amazon S3](https://docs.amperity.com/datagrid/source_amazon_s3.html).
3. Configure las fuentes y automatice las cargas de datos mediante flujos de trabajo estándar.


