---
nav_title: Tealium
article_title: Tealium
page_order: 1
alias: /partners/tealium/
description: "Este artículo de referencia describe la asociación entre Braze y Tealium, un centro de datos universal que te habilita para conectar datos móviles, Web y alternativos con otras fuentes de terceros."
page_type: partner
search_tag: Partner

---

# Tealium

> [Tealium](https://tealium.com/) es un centro de datos universal y una plataforma de datos de los clientes compuesta por EventStream, AudienceStream e iQ Tag Management que te habilita para conectar datos móviles, web y alternativos de fuentes de terceros. La conexión de Tealium con Braze permite un flujo de datos de eventos personalizados, atributos de usuario y compras que le permiten actuar sobre sus datos en tiempo real.

![Un gráfico resumen de Tealium que muestra cómo encajan los distintos productos Tealium y la plataforma Braze para activar campañas de canales cruzados en tiempo real.]({% image_buster /assets/img/tealium/tealium_overview.png %}){: style="border:0;"}

La integración de Braze y Tealium le permite realizar un seguimiento de sus usuarios y enviar datos a varios proveedores de análisis de usuarios. Tealium te permite:
- Sincronice las audiencias de Tealium con [AudienceStream]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_audience_stream/) con Braze para utilizarlas en la personalización de campañas y Canvases de Braze o en la creación de segmentos.
- [Importar datos entre plataformas](#choose-your-integration-type). Braze ofrece tanto una integración [en paralelo](#side-by-side-sdk-integration) de SDK para tus aplicaciones Android, iOS y Web, como una integración [de servidor a servidor](#server-to-server-integration) que puede utilizarse en cualquier plataforma que pueda informar de datos de eventos.<br><br>

{% tabs %}
{% tab EventStream %}
Tealium EventStream es un centro de recopilación de datos y API que se sitúa en el centro de tus datos. EventStream gestiona toda la cadena de suministro de datos, desde la configuración y la instalación hasta la identificación, validación y mejora de los datos de usuario entrantes. EventStream actúa en tiempo real con fuentes de eventos y conectores. Las siguientes son las características que componen el [EventStream](https://docs.tealium.com/server-side/getting-started/eventstream-api-hub/introduction/).
- Fuentes de datos (instalación y recogida de datos)
- Eventos en directo (inspección de datos en tiempo real)
- Especificaciones y atributos de los eventos (requisitos y validación de la capa de datos)
- Fuentes de eventos (tipos de eventos filtrados)
- Conectores de eventos (acciones del centro API)

{% endtab %}
{% tab AudienceStream %}

Tealium AudienceStream es un motor de segmentación de clientes omnicanal y de acción en tiempo real. AudienceStream toma los datos que fluyen hacia EventStream y crea perfiles de visitantes que representan los atributos más importantes del compromiso de sus clientes con su marca. Consulte nuestro artículo sobre [AudienceStream]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_audience_stream/) para conocer los pasos de configuración.

{% endtab %}
{% tab Administrador de etiquetas iQ %}
Tealium iQ le permite activar código en sus aplicaciones utilizando una etiqueta en la interfaz de usuario de gestión de etiquetas de Tealium iQ. Esta etiqueta recopilará, controlará y entregará datos de eventos de plataformas móviles y web, lo que le permitirá configurar una implementación nativa de Braze sin añadir código específico de Braze a sus aplicaciones. Los usuarios pueden optar por integrar Mobile Remote Commands a través de iQ Tag Management o archivos de configuración JSON (enfoque recomendado de Tealium). Los usuarios que utilicen Braze Web SDK deben realizar la integración a través de la etiqueta web iQ.

Para saber más sobre los pros y los contras de cada método, consulta la siguiente sección [del administrador de etiquetas Tealium iQ](#mobile-remote-commands).
{% endtab %}
{% endtabs %}

{% alert important %}
Tealium ofrece acciones de conector por lotes y no por lotes. El conector no por lotes debe utilizarse cuando las solicitudes en tiempo real sean importantes para el caso de uso y no haya preocupación por superar las especificaciones del límite de velocidad de la API de Braze. Si tiene alguna pregunta, póngase en contacto con el servicio de asistencia de Braze o con su gestor de atención al cliente.<br><br>

En el caso de los conectores por lotes, las solicitudes se ponen en cola hasta que se alcanza uno de los siguientes umbrales:<br><br>
- Número máximo de solicitudes: 75
- Tiempo máximo desde la solicitud más antigua: 10 minutos
- Tamaño máximo de las solicitudes: 1 MB

Tealium no procesa por lotes los eventos de consentimiento (preferencias de suscripción) ni los eventos de eliminación de usuarios por defecto.
{% endalert %}

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Tealium | Para beneficiarse de esta asociación, es necesario disponer de una [cuenta Tealium](https://my.tealiumiq.com/) con acceso al servidor y/o al cliente. | 
| Fuente instalada y [bibliotecas](https://docs.tealium.com/platforms/) fuente de Tealium | Origen de los datos enviados a Tealium, como aplicaciones móviles, sitios web o servidores backend.<br><br>Debe instalar las bibliotecas en su aplicación, sitio o servidor antes de poder configurar correctamente un conector Tealium. |
| Punto final REST y SDK de Braze | La URL de tu punto final REST o SDK. Tu punto final dependerá de la [URL Braze de tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
| Clave de identificación de la aplicación Braze (sólo en modo lateral) | La clave de identificación de tu aplicación. <br><br>Se encuentra en el **panel de Braze > Administrar configuración > Clave de API**. |
| Versión del código (sólo en paralelo) | Corresponde a la versión del SDK y debe estar en formato major.minor (por ejemplo, 3.2 y no 3.0.1). La versión del código debe ser 3.0 o superior. |
| Clave REST API (sólo de servidor a servidor) | Una clave de API REST Braze con permisos `users.track` y `users.delete`. <br><br>Se puede crear en **el panel de Braze > Consola para desarrolladores > Clave de API REST > Crear nueva clave de API**.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Elija su tipo de integración

| Integración | Detalles |
| ----------- | ------- |
| [De lado a lado](#side-by-side-sdk-integration) | Utiliza el SDK de Tealium para traducir los eventos a las llamadas nativas de Braze, lo que permite acceder a características más profundas y un uso más completo de Braze que la integración de servidor a servidor.<br><br>Si piensas utilizar comandos remotos Braze, ten en cuenta que Tealium no admite todos los métodos Braze (por ejemplo, las tarjetas de contenido). Para utilizar un método Braze que no esté asignado a través de un comando remoto correspondiente, tendrá que invocar el método añadiendo código Braze nativo a su código base.|
| [De servidor a servidor](#server-to-server-integration) | Reenvía los datos de Tealium a los puntos finales de la API REST de Braze.<br><br>No es compatible con las funciones de la interfaz de usuario Braze, como la mensajería dentro de la aplicación, las tarjetas de contenido o las notificaciones push. También existen datos capturados automáticamente, como los campos a nivel de dispositivo, que no están disponibles a través de este método.<br><br>Considera una integración en paralelo si deseas utilizar estas características.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración de SDK en paralelo

### Comandos a distancia

Los comandos remotos son una función de las bibliotecas Tealium para iOS y Android que permiten realizar llamadas desde el SDK de Tealium -a través de los servidores Braze- a Braze. El módulo de comandos remotos Braze instalará y creará automáticamente las bibliotecas Braze necesarias y se encargará de toda la renderización de mensajes y el seguimiento analítico. Para utilizar el mando a distancia móvil Braze, necesitarás tener instaladas bibliotecas Tealium en tus aplicaciones.

Tealium ofrece dos formas de integrar Mobile Remote Command; además, no hay pérdida de funcionalidad entre los tipos de integración y el código nativo subyacente es idéntico.

| Método de mando a distancia móvil | Pros | Contras |
| --- | --- | --- |
| **Etiqueta de mando a distancia** | Modifique fácilmente las asignaciones y los datos enviados al mando a distancia mediante la interfaz de usuario de Tealium iQ.<br><br>Esto nos permite enviar datos o eventos adicionales a un SDK de terceros después de que la aplicación ya esté en la tienda de aplicaciones, sin que el cliente tenga que actualizar la aplicación. | El módulo de administrador de etiquetas de la aplicación se basa en una webview oculta para procesar JavaScript. |
| **Fichero de configuración JSON**<br>[(Recomendado](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#how-it-works)) | Utilizar el método JSON elimina la necesidad de tener una webview oculta en la aplicación y reduce enormemente el consumo de memoria.<br><br>El archivo JSON puede alojarse de forma remota o local dentro de la aplicación del cliente. | Por el momento, no hay interfaz de usuario para gestionar esto, por lo que requiere un poco de esfuerzo adicional.<br><br>Nota: Tealium está trabajando en la adición de una interfaz de usuario de gestión que va a resolver este problema y llevar el mismo nivel de flexibilidad a los comandos remotos JSON como lo han hecho con la versión de gestión de iQ Tag |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Utilice las asignaciones de datos de comandos remotos Braze mobile para establecer atributos de usuario predeterminados y atributos personalizados y realizar un seguimiento de las compras y los eventos personalizados. Consulte la tabla siguiente para conocer los métodos de soldadura correspondientes.

| Mando a distancia | Método Braze |
| -------------- | ------------ |
| appendcustomarrayattribute | addToCustomAttributeArrayWithKey()|
| notificación por correo electrónico | setEmailNotificationSubscriptionType() |
| incrementaratributopersonalizado | incrementCustomAttribute() |
| Initalizar | startWithApiKey() |
| logcustomevent | logEventoPersonalizado() |
| registrocompra | logCompra() |
| pushnotification | setPushNotificationSubscriptionType() |
| eliminaratributopersonalizado | setCustomAttributeWithKey() |
| setcustomattribute | setCustomAttributeArrayWithKey() |
| setcustomarrayattribute | setCustomAttributeArrayWithKey() |
| setlastknownlocation | setLastKnownLocationWithLatitude() |
| unsetcustomattribute | unsetCustomAttributeWithKey() |
| useralias | addAlias() |
| atributo de usuario | ABKUser() |
| identificador de usuario | cambiarUsuario() |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Puede encontrar más detalles sobre cómo configurar el comando remoto móvil Braze y una descripción general de los métodos compatibles en la documentación para desarrolladores de Tealium:
- [Mando a distancia](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#json-template)
- [Etiqueta de mando a distancia](https://docs.tealium.com/client-side-tags/braze-mobile-remote-command-tag/)

{% alert important %}
Los comandos remotos móviles Braze no son compatibles con todos los métodos y canales de mensajería Braze (por ejemplo, las tarjetas de contenido). Para utilizar un método Braze que no esté asignado a través de un comando remoto correspondiente, tendrá que invocar el método directamente añadiendo código Braze nativo a su código base.
{% endalert%}

### Etiqueta SDK Web Braze

Utiliza la etiqueta SDK Braze Web para desplegar el SDK Braze Web en tu sitio web. [Tealium iQ Tag Management](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/) permite a los clientes añadir Braze como etiqueta dentro del panel de control de Tealium para realizar un seguimiento de la actividad de los visitantes. Los profesionales del marketing suelen utilizar las etiquetas para conocer la eficacia de la publicidad en línea, el marketing por correo electrónico y la personalización de sitios web.

1. En Tealium, ve a **iQ > Etiquetas > + Añadir etiqueta > Braze Web SDK**.
2. En el cuadro de diálogo Configuración de etiquetas, introduzca la clave API (su clave de identificador de la aplicación Braze), la URL base (punto final del SDK Braze) y [la versión del código del SDK Braze Web](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md). También puede activar el registro para registrar información en la consola web con fines de depuración.
3. En el cuadro de diálogo [Reglas de carga](https://docs.tealium.com/iq-tag-management/load-rules/about/), elija "Cargar en todas las páginas" o seleccione **Crear regla** para determinar cuándo y dónde cargar una instancia de esta etiqueta en su sitio.
4. En las **[Asignaciones de datos](https://docs.tealium.com/iq-tag-management/data-mappings/about/)** seleccione **Crear asignaciones** para asignar datos Tealium a Braze. Las variables de destino de la etiqueta SDK Web de Braze están integradas en la pestaña **Mapeado de datos** de la etiqueta. En [las tablas siguientes](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/) se enumeran las categorías de destino disponibles y se describe cada nombre de destino.
5. Selecciona el **Acabado**.

### Recursos de integración en paralelo

- Mando a distancia iOS: [Documentación de Tealium](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [repositorio GitHub de Tealium](https://github.com/Tealium/tealium-ios-braze-remote-command)
- Mando a distancia Android: [Documentación de Tealium](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [repositorio GitHub de Tealium](https://github.com/Tealium/tealium-android-braze-remote-command)
- Etiqueta SDK Web: [Documentación sobre Tealium](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)

## Integración de servidor a servidor

Esta integración reenvía datos de Tealium a la API REST de Braze.

La integración de servidor a servidor no es compatible con las funciones de la interfaz de usuario Braze, como la mensajería dentro de la aplicación, las tarjetas de contenido o las notificaciones push. También existen datos capturados automáticamente (como los campos a nivel de dispositivo) que no están disponibles a través de este método.

Si deseas utilizar estos datos y estas características, considera nuestra integración de SDK [en paralelo]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium/#side-by-side-sdk-integration).

### Paso 1: Configurar una fuente

Tealium requiere que primero configures una fuente de datos válida para que tu conector se nutra de ella.
1. En la barra lateral de Tealium, en **el lado del servidor**, ve a **Fuentes > Fuentes de datos > + Añadir origen de datos**.
2. Localiza la plataforma que desees dentro de las categorías disponibles, y nombra tu fuente, este es un campo obligatorio.<br>![]({% image_buster /assets/img/tealium/data_source.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
3. En las opciones de **Especificaciones del evento**, elija las [especificaciones del evento](https://docs.tealium.com/server-side/event-specifications/about/) que desea incluir. Las especificaciones de eventos le ayudan a identificar los nombres de los eventos y los atributos necesarios para realizar un seguimiento en su instalación. Estas especificaciones se aplicarán a los eventos entrantes.<br>![]({% image_buster /assets/img/tealium/event_specs.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>Tómate un tiempo para pensar qué datos son más valiosos para ti y qué especificaciones parecen las más adecuadas para tu caso de uso. También hay disponibles [especificaciones personalizadas para eventos](https://docs.tealium.com/iq-tag-management/events/about/). <br>
4. El siguiente diálogo avanza al paso **Obtener Código**. El código base y el código de seguimiento de eventos proporcionados aquí le servirán de guía para la instalación. Descargue el PDF proporcionado si desea compartir estas instrucciones con su equipo. Seleccione **Guardar y continuar** cuando haya terminado.<br>
5. Ahora podrá ver su fuente guardada, así como añadir o eliminar especificaciones de eventos. <br>![]({% image_buster /assets/img/tealium/braze_connection.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>Desde la vista detallada de la fuente de datos puede realizar las siguientes acciones:
- Ver y copiar la clave de la fuente de datos
- Ver instrucciones de instalación
- Volver a la página **Obtener código** 
- Añadir o eliminar especificaciones de eventos
- Navegue para ver los eventos en directo relacionados con una especificación de evento
- Y más...<br>
6. Por último, seleccione **Guardar / Publicar** en la parte superior de la página. Si no publicas tu fuente, no podrás encontrarla al configurar tu conector Braze.

Consulte [Fuentes de datos](https://docs.tealium.com/server-side/data-sources/about-data-sources/) para obtener más instrucciones sobre cómo configurar y editar su fuente de datos.

### Paso 2: Crear un conector de eventos

Un conector es una integración entre Tealium y otro proveedor utilizada para transmitir datos. Estos conectores contienen acciones que representan las API compatibles de sus socios. 

1. Desde la barra lateral en Tealium bajo **Server-Side**, navegue a **EventStream > Event Connectors**.
2. Selecciona el botón azul **\+ Añadir conector** para buscar en el mercado de conectores. En el nuevo cuadro de diálogo que aparece, utiliza la búsqueda rápida para encontrar el conector **Braze**.
3. Para añadir este conector, haz clic en la ficha del conector **Braze**. Al hacer clic, puede ver el resumen de la conexión y una lista de la información necesaria, las acciones admitidas y las instrucciones de configuración. La configuración consta de tres pasos: origen, configuración y acción.

#### Fuente

Una vez configurada la fuente, vuelve a la página del conector Braze en **EventStream** > **Conectores de eventos** > **\+ Añadir conector** > **Braze**. 

A continuación, selecciona el origen de datos que acabas de crear y, en **Fuente de eventos**, selecciona **Todos los eventos** o una especificación de eventos concreta, la ruta recomendada para enviar a Braze sólo los valores modificados. Seleccione **Continuar**.

#### Configuración

A continuación, selecciona **Añadir conector** en la parte inferior de la página. Da un nombre a tu conector y proporciona aquí tu punto final de la API Braze y tu clave de API REST Braze.

![]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

Si ya ha creado un conector anteriormente, puede utilizar uno existente de la lista de conectores disponibles y modificarlo para adaptarlo a sus necesidades con el icono del lápiz o eliminarlo con el icono de la papelera. 

#### Acción

A continuación, asigna un nombre a tu acción de conector y selecciona un tipo de acción que enviará datos según la asignación que configures. Aquí, asignará atributos, eventos y compras Braze a nombres de atributos, eventos y compras Tealium.

{% alert important %}
No todos los campos ofrecidos son obligatorios.

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Usuario de seguimiento - Lote y no lote %}

Esta acción le permite realizar un seguimiento de los atributos de usuario, evento y compra en una sola acción.

| Parámetros | Descripción |
| ---------- | ----------- |
| ID de usuario | Utilice este campo para asignar el campo ID de usuario Tealium a su equivalente Braze. Asigna uno o más atributos de ID de usuario. Cuando se especifican varios ID, se elige el primer valor que no está en blanco según el siguiente orden de prioridad: ID externo, ID Braze, Nombre de alias y Etiqueta de alias.<br><br>\- El ID externo y el ID Braze no deben especificarse si se importan tokens push.<br>\- Si se especifica un alias de usuario, deben establecerse el nombre y la etiqueta del alias. <br><br>Para más información, consulta el [punto final de `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze. |
| Atributos del usuario | Utiliza los nombres de campo de perfil de usuario Braze existentes para actualizar los valores de perfil de usuario en el panel Braze o añade tus propios datos de [atributo]({{site.baseurl}}/api/objects_filters/user_attributes_object/) personalizado de [usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/) a los perfiles de usuario.<br><br>\- Por defecto, se crearán nuevos usuarios si no existe ninguno.<br>\- Si configura **Actualizar sólo existentes** en `true`, sólo se actualizarán los usuarios existentes y no se creará ningún usuario nuevo.<br>\- Si un atributo Tealium está vacío, se convertirá en nulo y se eliminará del perfil de usuario Braze. Los enriquecimientos deben utilizarse si no deben enviarse valores nulos a Braze para eliminar un atributo de usuario. |
| Modificar los atributos del usuario | Utilice este campo para aumentar o disminuir ciertos atributos de usuario<br><br>\- Los atributos enteros pueden incrementarse con enteros positivos o negativos.<br>\- Los atributos de las matrices pueden modificarse añadiendo o eliminando valores de las matrices existentes. |
| Evento | Un evento representa una ocurrencia única de un evento personalizado por un usuario particular en una marca de tiempo. Utilice este campo para rastrear y asignar atributos de evento como los del [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object/) Braze. <br><br>\- El atributo de evento `Name` es necesario para cada evento asignado.<br>\- El atributo de evento `Time` se establece automáticamente en now a menos que se asigne explícitamente. <br>\- Por defecto, se crearán nuevos eventos si no existe ninguno. Estableciendo `Update Existing Only` a `true`, sólo se actualizarán los eventos existentes, y no se creará ningún evento nuevo.<br>\- Mapa de atributos de tipo array para añadir múltiples eventos. Los atributos de tipo array deben tener la misma longitud.<br>\- Se pueden utilizar atributos de valor único y aplicarlos a cada evento. |
| Plantilla de eventos | Proporcionar plantillas de eventos a las que hacer referencia en los datos del cuerpo. Las plantillas pueden utilizarse para transformar los datos antes de enviarlos a Braze. Consulte la [Guía de plantillas](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) de Tealium para obtener más información. |
| Variable de plantilla de evento | Proporcione variables de plantilla de eventos como entrada de datos. Consulte la [Guía de Variables de Plantilla](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) de Tealium para obtener más información. |
| Compra | Utilice este campo para rastrear y asignar atributos de compra del usuario como los del [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) Braze.<br><br>\- Los atributos de compra `Product ID`, `Currency` y `Price` son necesarios para cada compra mapeada.<br>\- El atributo de compra `Time` se establece automáticamente en now a menos que se asigne explícitamente.<br>\- Por defecto, se crearán nuevas compras si no existe ninguna. Si configura `Update Existing Only` en `true`, sólo se actualizarán las compras existentes y no se creará ninguna compra nueva.<br>\- Asignar atributos de tipo array para añadir múltiples artículos de compra. Los atributos de tipo array deben tener la misma longitud.<br>\- Se pueden utilizar atributos de valor único y se aplicarán a cada artículo.|
| Plantilla de compra | Las plantillas pueden utilizarse para transformar los datos antes de enviarlos a Braze.<br>\- Defina una plantilla de compra si necesita compatibilidad con objetos anidados.<br>\- Cuando se define una plantilla de compra, la configuración establecida en la sección de compras de su acción será ignorada.<br>\- Consulte la [Guía de plantillas](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) de Tealium para obtener más información.|
| Variable del modelo de compra | Proporcione variables de plantilla de productos como entrada de datos. Consulte la [Guía de Variables de Plantilla](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) de Tealium para obtener más información. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_example.png %})

{% endtab %}
{% tab Eliminar usuario - No lote %}

Esta acción te permite eliminar usuarios del panel de Braze.

| Parámetros | Descripción |
| ---------- | ----------- |
| ID de usuario | Utilice este campo para asignar el campo ID de usuario de Tealium a su equivalente en Braze. <br><br>\- Asigna uno o más atributos de ID de usuario. Cuando se especifican varios ID, se elige el primer valor que no está en blanco según el siguiente orden de prioridad: ID externo, ID Braze, Nombre de alias y Etiqueta de alias.<br>\- Al especificar un alias de usuario, deben establecerse tanto el Nombre de alias como la Etiqueta de alias.<br><br>Para más información, consulta el [punto final `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) de Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_delete.png %})

Si desea modificar las opciones elegidas, seleccione **Atrás** para editar o **Finalizar** para completar.

{% endtab %}
{% endtabs %}

Seleccione **Continuar**.

Tu conector aparece ahora en la lista de conectores de tu página de inicio de Tealium. <br>![]({% image_buster /assets/img/tealium/summary_list.png %}){: style="max-width:80%;"}

Asegúrate de seleccionar **Guardar / Publicar** para tu conector cuando hayas terminado. Las acciones que configuraste se dispararán ahora cuando se cumplan las conexiones desencadenantes. 

### Paso 3: Pruebe su conector Tealium

Una vez que el conector esté en funcionamiento, debes probarlo para asegurarte de que funciona correctamente. La forma más sencilla de comprobarlo es utilizar **la Herramienta de Rastreo de** Tealium. Para empezar a utilizar Trace, asegúrese de que ha añadido la extensión de navegador Tealium Tools.

1. Para iniciar una nueva traza, seleccione **Traza** en la barra lateral, en Opciones **del lado del servidor**. Selecciona **Iniciar** y captura el ID de rastreo.
2. Abre la extensión del navegador e introduce el ID de rastreo en AudienceStream Trace.
3. Examina el registro en tiempo real.
4. Busca la acción que quieras validar seleccionando la entrada **Acciones desencadenantes** para ampliarla.
5. Busca la acción que quieras validar y visualiza el estado del registro. 

Consulta la [documentación de Trace](https://docs.tealium.com/server-side/connectors/trace/about/) de Tealium para obtener instrucciones más detalladas sobre la aplicación de la herramienta Trace de Tealium.

## Demostración de integración

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Posibles excesos de puntos de datos

Hay tres formas principales en las que puedes incurrir accidentalmente en excedentes de datos al integrar Braze a través de Tealium:

#### Envío de datos duplicados: envíe sólo deltas de atributos Braze

Tealium no envía deltas Braze de atributos de usuario. Por ejemplo, si tiene una acción EventStream que rastrea el nombre, el correo electrónico y el número de teléfono móvil de un usuario, Tealium enviará los tres atributos a Braze cada vez que se active la acción. Tealium no buscará lo que ha cambiado o se ha actualizado y sólo enviará esa información.

**Solución**: <br>Puede comprobar su backend para evaluar si un atributo ha cambiado o no y, en caso afirmativo, llamar a los métodos pertinentes de Tealium para actualizar el perfil del usuario. **Esto es lo que suelen hacer los usuarios que integran Braze directamente.** <br>**O**<br> Si no almacena su propia versión de un perfil de usuario en su backend y no puede saber si los atributos cambian o no, puede utilizar AudienceStream y
[crear enriquecimientos](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/) para enviar atributos de usuario sólo cuando los valores hayan cambiado. Consulte la documentación de Tealium sobre [las reglas de enriquecimiento](https://docs.tealium.com/server-side-connectors/braze-connector/).

#### Envío de datos irrelevantes o sobrescritura innecesaria de datos.

Si tienes varios EventStreams que se dirigen a la misma fuente de eventos, **todas las acciones habilitadas para ese conector** se dispararán automáticamente cada vez que se desencadene una sola acción, \*\*esto también podría dar lugar a que se sobrescriban datos en Braze y se consuman puntos de datos innecesarios.\\i

**Solución**: <br>Configure una especificación de evento o feed independiente para realizar un seguimiento de cada acción. <br>**O**<br> Desactiva las acciones (o conectores) que no quieras que se activen utilizando los botones del panel de control de Tealium.

#### Inicializar Braze demasiado pronto

Los usuarios que se integren con Tealium utilizando la etiqueta SDK de la Web de Braze pueden ver un aumento espectacular de sus MAU. **Si Braze se inicializa al cargar la página, Braze creará un perfil anónimo cada vez que un internauta navegue por el sitio web por primera vez.** Algunos pueden querer rastrear el comportamiento del usuario sólo cuando los usuarios han completado alguna acción, como "Iniciar sesión" o "Ver vídeo", para reducir su recuento de MAU.

**Solución**: <br>Configure [reglas de carga](https://docs.tealium.com/iq-tag-management/load-rules/about/) para determinar exactamente cuándo y dónde se carga una etiqueta en su sitio. 

