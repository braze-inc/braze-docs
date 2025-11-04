---
nav_title: Census
article_title: Importación de cohortes de Census
description: "Este artículo de referencia describe la funcionalidad de importación de cohortes de Census, una plataforma de integración de datos que te permite crear dinámicamente segmentos de usuarios específicos con datos de tu almacén de datos."
page_type: partner
search_tag: Partner

---

# Importación de cohortes de Census

> Este artículo describe cómo importar cohortes de usuarios de [Census](https://www.getcensus.com/) a Braze. Para más información sobre la integración de Census, consulta el [artículo principal sobre Census]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/census/).

## Integración de importación de cohortes

### Paso 1: Crear conexión de servicio Braze

Para integrar Census en la plataforma Census, ve a la pestaña **Conexiones** y selecciona **Nuevo destino** para crear una nueva conexión de servicio Braze.

En la ventana que aparece, asigna un nombre a esta conexión e indica la URL de tu punto final Braze, la clave de API REST Braze y la clave de importación de datos. La clave de importación de datos es necesaria para sincronizar cohortes y se puede encontrar en Braze yendo a **Integraciones de socios** > **Socios tecnológicos** > **Census**.

![]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### Paso 2: Crear una sincronización del censo

Para sincronizar clientes con Braze, debe crear una sincronización. Aquí definirá dónde sincronizar los datos y cómo desea que se asignen los campos entre las dos plataformas.

1. Vaya a la pestaña **Sincronizaciones** y seleccione **Nueva sincronización**.<br><br> 
2. En el compositor, seleccione el modelo de datos fuente de su almacén de datos.<br><br>
3. Configura dónde se sincronizará el modelo. Selecciona **Braze** como destino y **Usuario y cohorte** como objeto a sincronizar.<br>![En la pregunta "Selecciona un destino", se selecciona "Braze" como conexión y se enumeran varios objetos.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. Selecciona la **Columna Fuente** que identifica a los usuarios que se van a añadir a una cohorte, y selecciona **ID de usuario externo** como **Tipo de identificador**.<br><br>
5. En el desplegable **Nombre de la cohorte**, selecciona una cohorte, crea una cohorte o selecciona una Columna de origen para rellenar el nombre de la cohorte.<br><br>
6. Utiliza el desplegable **Cuando se elimina un registro de los datos de origen** para seleccionar lo que les ocurre a los usuarios cuando se eliminan del conjunto de datos de origen, como **No hacer nada** o **Eliminar registro coincidente de la cohorte**.<br><br>
7. Por último, asigne los campos de datos del censo a los campos Braze equivalentes.<br>![Censo mapeado]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
8. Confirma los detalles y crea la sincronización. 

¡Ahora puedes ejecutar tu sincronización!

Durante una sincronización, los campos que mapees se sincronizarán primero con el objeto de usuario para actualizar lo que ya existe en Braze. Después, el usuario actualizado se añadirá a la cohorte especificada.

Tras la sincronización, puedes crear y añadir un segmento Braze con un filtro de cohorte de Census a futuras campañas y Canvas Braze para dirigirte a esos usuarios. 

{% alert note %}
Al utilizar la integración de Census y Braze, Census sólo enviará los deltas (datos cambiantes) en cada sincronización a Braze.
{% endalert %}

{% alert important %}
Sólo se añadirán o eliminarán de una cohorte los usuarios que ya existan en Braze. La importación de cohortes no creará nuevos usuarios en Braze.
{% endalert %}

## Coincidencia de usuarios

Los usuarios identificados pueden coincidir por su `external_id` o `alias`. Los usuarios anónimos pueden ser emparejados por su `device_id`. Los usuarios identificados que fueron creados originalmente como usuarios anónimos no pueden ser identificados por su `device_id`, y deben ser identificados por su `external_id` o `alias`.

