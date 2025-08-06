---
nav_title: Buenas prácticas
hidden: true
---

# Buenas prácticas en materia de identificadores y ciclo de vida de los usuarios

## Recopilación de datos

Más información sobre cómo recopila datos Braze:
- [Recopilación de datos del SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/)
- [Mejores prácticas de recopilación de datos]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/)
- [Ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)

## Identificadores de soldadura

- `braze_id`: Identificador asignado por Braze, inalterable y asociado a un usuario concreto cuando se crea en nuestra base de datos.
- `external_id`: Un identificador asignado por el cliente, normalmente un UUID. Recomendamos a los clientes que asignen la dirección `external_id` cuando el usuario pueda ser identificado de forma inequívoca. Una vez identificado un usuario, no puede volver a ser anónimo.
- `user_alias`: Un identificador alternativo único que el cliente puede asignar como medio de referenciar al usuario por un ID antes de que se le asigne un `external_id`. Los alias de usuario pueden fusionarse posteriormente con otros alias o con un `external_id` cuando haya uno disponible a través del punto final Braze [User identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
    - Dentro del punto final [User identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/), el campo `merge_behavior` puede utilizarse para especificar qué datos del perfil de alias de usuario deben persistir en el perfil de usuario conocido.
    - Tenga en cuenta que para que el alias de usuario sea un perfil enviable, debe seguir incluyendo el correo electrónico y/o el teléfono como atributo estándar en el perfil.
- `device_id`: Un identificador específico del dispositivo generado automáticamente. Un perfil de usuario puede tener asociado un número de `device_ids`. Por ejemplo, un usuario que haya iniciado sesión en su cuenta en el ordenador del trabajo, el ordenador de casa, la tableta y la aplicación iOS tendría 4 `device_ids` asociados a su perfil.
- Dirección de correo electrónico y número de teléfono:
    - Se admite como identificador en el punto final de seguimiento de usuarios Braze. 
    - Cuando se utiliza la dirección de correo electrónico o los números de teléfono como identificador dentro de una solicitud, hay tres resultados posibles:
        1. Si no existe un usuario con este correo electrónico/teléfono en Braze, se creará un perfil de usuario de sólo correo electrónico/sólo teléfono, y los datos de la solicitud se añadirán al perfil.
        2. Si ya existe un perfil con este correo electrónico/teléfono en Braze, se actualizará para incluir los datos enviados en la solicitud.
        3. En un caso de uso con más de un perfil con este correo electrónico/teléfono, se dará prioridad al perfil actualizado más recientemente.
    - Tenga en cuenta que si existe un perfil de usuario de sólo correo electrónico/sólo teléfono y luego se crea un perfil identificado con el mismo correo electrónico/teléfono (como otro perfil con la misma dirección de correo electrónico Y un ID externo), Braze creará un segundo perfil. Las actualizaciones posteriores irán al perfil con el ID externo.
        - Los dos perfiles pueden fusionarse utilizando el punto final Braze [/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) 

## Gestión de usuarios anónimos

Para un caso de uso en el que necesite crear o actualizar un perfil de usuario en Braze sin tener acceso a `external_id`, se puede pasar otro identificador, como una dirección de correo electrónico o un número de teléfono, al punto final [Exportar usuario por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) de Braze para determinar si existe un perfil para el usuario en Braze. 

```json
{
 "email_address": "test@braze.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

Si existe un usuario en Braze con ese correo electrónico o teléfono, se devolverá su perfil. En caso contrario, se devolverá un array "users" vacío. La ventaja de utilizar el punto final de exportación para determinar si ya existe un usuario con esa dirección de correo electrónico es que esto le permitirá determinar si hay algún perfil de usuario anónimo asociado al usuario. Por ejemplo, un perfil anónimo creado a través del SDK (que tendrá `braze_id`) o un perfil de alias de usuario creado previamente. 

Si la solicitud no devuelve un perfil de usuario, puede elegir entre crear un alias de usuario o crear un usuario sólo de correo electrónico:

### Alias de usuario

Utilice el punto final de seguimiento de usuarios para crear un alias de usuario, utilizando el identificador elegido como nombre del alias. Al incluir `_update_existing_only` como `false` dentro del objeto de atributo, evento o compra donde se define el nuevo alias de usuario, puede crear el perfil de alias y añadir atributos, eventos y compras a ese perfil simultáneamente. 

Para que el alias de usuario sea un perfil enviable, debe incluir la dirección de correo electrónico en el campo `email`, como se muestra a continuación.

```json
{
   "attributes": [
   {
     "user_alias" : {
       "alias_name" : "test@braze.com",
       "alias_label" : "email"
     },
     "email": "test@braze.com",
     "_update_existing_only": false,
     "string_attribute": "sherman",
     "boolean_attribute_1": true,
     "integer_attribute": 25,
     "array_attribute": ["banana", "apple"]
   }
   ]
}
```

Más adelante podrá identificar y combinar este alias de usuario con un `external_id` cuando haya uno disponible a través de nuestro punto final [Identificar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). 

### Creación de un usuario sólo por correo electrónico

Utilice la dirección de correo electrónico como identificador en el endpoint de seguimiento del usuario. 

```json
{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}
```
{% alert important %}
Esta funcionalidad se encuentra actualmente en acceso anticipado.
{% endalert %}

## Sincronización de datos con perfiles de usuario

[Seguimiento del usuario]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- Se trata de un punto final de acceso público que puede crear y actualizar usuarios en Braze, como el registro de atributos en el perfil de usuario. Este punto final tiene un límite de velocidad de 50.000 peticiones por minuto aplicado a nivel de espacio de trabajo.
- Cuando utilices este punto final, incluye la clave `partner` como se muestra en nuestra documentación para socios.

[Ingesta de datos de Cloud]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/#what-is-cloud-data-ingestion)
- De forma similar al punto final de seguimiento del usuario, los datos pueden sincronizarse con los perfiles de usuario a través de Cloud Data Ingestion. Al utilizar esta herramienta, los atributos, eventos y compras se registran en los perfiles configurando y conectando la tabla o vista del almacén de datos que desea sincronizar con el espacio de trabajo Braze deseado.

[Puntos de datos]({{site.baseurl}}/user_guide/data/data_points/)
- Braze tiene un modelo de consumo de puntos de datos en el que se incurre en puntos de datos por "escritura" en el perfil del usuario, independientemente de si el valor ha cambiado. Por este motivo, recomendamos que sólo se envíen a Braze los atributos que hayan cambiado. 

## Envío de audiencias de usuarios a Braze

[Documentación del socio de importación de cohortes]({{site.baseurl}}/partners/isv_partners/cohort_import/)<br>
- Las audiencias de usuarios pueden sincronizarse con Braze como una cohorte utilizando los puntos finales de la API de importación de cohortes Braze. En lugar de que estas audiencias se almacenen en el perfil del usuario como atributos de usuario, los clientes pueden crear y dirigirse a esta cohorte a través de un filtro de marca de socio dentro de nuestra herramienta de segmentación. Esto puede hacer que encontrar y dirigirse a un segmento concreto de usuarios sea más fácil y sencillo para los clientes.
- Los criterios de valoración de la importación de cohortes no son públicos y son específicos de cada socio. Por este motivo, las sincronizaciones con los puntos finales de cohorte no contarán para los límites de velocidad del espacio de trabajo de un cliente. 

[Seguimiento del usuario]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)<br>
- Se trata de un punto final de acceso público que se puede utilizar inmediatamente para crear usuarios en Braze denotando a un usuario en un público concreto a través de un atributo de usuario. La principal diferencia entre este punto final y el punto final de importación de cohortes es que las audiencias enviadas mediante este punto final se almacenarían en el perfil del usuario, mientras que el punto final de importación de cohortes se mostraría como un relleno en nuestra herramienta de segmentación. Este punto final tiene un límite de velocidad de 50.000 peticiones por minuto aplicado a nivel de espacio de trabajo.
- Cuando utilices este punto final, asegúrate de que incluyes la clave `partner` como se indica en nuestra [documentación para socios]({{site.baseurl}}/partners/isv_partners/api_partner).

[Puntos de datos]({{site.baseurl}}/user_guide/data/data_points/)<br>
- Braze tiene un modelo de consumo de puntos de datos en el que se incurre en puntos de datos por "escritura" en el perfil del usuario, independientemente de si el valor ha cambiado.
- Los puntos de datos se producen tanto por la importación de cohortes como por los puntos finales de seguimiento del usuario.

## Transmisión de análisis de interacción al socio

### Currents

Currents es una herramienta de análisis de interacción de mensajes casi en tiempo real en Braze. Esto transmitirá datos a nivel de usuario sobre todos los envíos, entregas, aperturas, clics, etc., de campañas y lienzos enviados desde el espacio de trabajo del cliente. Un par de cosas a tener en cuenta: Los precios de Currents son por conector para el cliente, por lo que todos los nuevos socios de Currents deben pasar por un proceso de EA. Pedimos a nuestros socios que cuenten con cinco clientes como parte de la EA antes de crear la interfaz de usuario personalizada y poner el conector a disposición del público. 
- [Documentación para socios]({{site.baseurl}}/partners/isv_partners/currents_integration/)
- [Eventos de compromiso de mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/): todos los clientes que adquieran un conector Currents tendrán acceso a estos eventos.
- [Eventos de comportamiento del usuario]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/): no todos los clientes que adquieren un conector de corriente adquieren un conector de "todos los eventos" que incluya estos eventos. 

### Compartir datos Snowflake

Los clientes que adquieran un conector Snowflake Data Share tendrán acceso automático tanto a los eventos de compromiso de mensajes como a los de comportamiento del usuario. Cuando se utilice Snowflake Data Share como integración del socio, Braze proporcionará una parte a la instancia de Snowflake del socio en nombre del cliente. Como nota, el intercambio de datos entre regiones supone un precio más elevado para nuestros clientes, por lo que pedimos a los socios que deseen integrarse con Snowflake la orientación de que necesitan una cuenta en `US-EAST-1` y/o `EU-CENTRAL-1`
- [Documentación para socios]({{site.baseurl}}/partners/isv_partners/currents_integration/)

## Creación y activación de campañas y lienzos

### Creación de activos en Braze
Braze ofrece una serie de puntos finales que permiten a los clientes y socios crear/actualizar plantillas de correo electrónico y bloques de contenido dentro del espacio de trabajo del cliente. Estas plantillas y bloques de contenido pueden, a su vez, utilizarse en todas las campañas y lienzos Braze del cliente.
- Plantillas de correo electrónico
    - [Crear punto final de plantilla]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)
    - [Actualizar el punto final de la plantilla]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/#rate-limit)
- [Bloques de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) 
    - [Crear punto final de bloque de contenido]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
    - [Actualizar el bloque de contenido punto final]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)

### Campañas y lienzos activados por API

Los clientes pueden configurar campañas y lienzos para que se activen mediante la API. Las solicitudes de API para activar estas campañas pueden utilizarse para personalizar y segmentar aún más la campaña introduciendo propiedades de activación de API y parámetros de audiencia o destinatario. 
- [Activación de campañas a través de la API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body)
    - Las campañas son mensajes singulares, como correos electrónicos individuales.
- [Activación de lienzos mediante API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#request-body)
    - Canvas es una interfaz unificada en la que los profesionales del marketing pueden crear campañas con múltiples mensajes y pasos para formar un viaje cohesivo. Al activar un lienzo, está introduciendo un usuario en el flujo del lienzo, donde seguirá recibiendo mensajes hasta que deje de cumplir los criterios del lienzo. 
- [Propiedades de desencadenar API/Propiedades de entrada en Canvas]({{site.baseurl}}/api/objects_filters/trigger_properties_object) 
    - Datos que pueden introducirse dinámicamente en el mensaje en el momento del envío.

### Campañas API
Cuando se crean campañas de API (diferentes de las campañas activadas por API mencionadas anteriormente), el panel Braze sólo se utiliza para generar un `campaign_id`, que permite al cliente realizar un seguimiento de los análisis para la elaboración de informes de campaña. El propio mensaje de la campaña se define dentro de la solicitud de la API. 
- [Enviar campaña API inmediatamente]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)
- [Programar una campaña API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)

### Enviar ID
Utiliza el punto final Braze para generar un ID de envío que pueda utilizarse para desglosar los análisis de campaña por envío. Por ejemplo, si se crea una `campaign_id` (campaña API) por ubicación, se podría generar un ID de envío por envío para realizar un seguimiento del rendimiento de los diferentes mensajes para una ubicación concreta. 
- [Enviar ID]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)

## Contenido conectado

El contenido conectado se puede utilizar en cualquier tipo de canal para realizar una solicitud de API al punto final especificado en el momento del envío y rellenar el mensaje con lo que se devuelva en la respuesta.

La versatilidad de Connected Contents hace que sea una función utilizada por muchos de nuestros clientes para insertar contenidos que no viven o no pueden vivir en Braze. Algunos de los casos de uso más comunes que vemos son:
- Plantillas de contenido de blogs o artículos en mensajes
- Recomendaciones de contenido
- Metadatos del producto
- Localización y traducción

Cosas a tener en cuenta:
- Braze no cobra por las llamadas a la API y no contarán para tu asignación de puntos de datos.
- Hay un límite de 1 MB para las respuestas de Contenido conectado.
- Las llamadas a Contenido Conectado se realizarán cuando se envíe el mensaje, excepto en el caso de los mensajes in-app, que realizarán esta llamada cuando se visualice el mensaje.
- Las llamadas de contenido conectado no siguen redirects.Braze requiere que el tiempo de respuesta del servidor sea inferior a 2 segundos por razones de rendimiento; si el servidor tarda más de 2 segundos en responder, el contenido no se insertará.
- Los sistemas de Braze pueden realizar la misma llamada a la API de contenido conectado más de una vez por destinatario. Esto se debe a que Braze puede necesitar realizar una llamada a la API de contenido conectado para representar la carga útil de un mensaje, y las cargas útiles de los mensajes pueden representarse varias veces por destinatario para validación, lógica de reintento u otros fines internos. 

Consulte estos artículos para obtener más información sobre los contenidos conectados:
- [Hacer una llamada de contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)
- [Anular contenidos conectados]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content)
- [Reintentos de contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries)

