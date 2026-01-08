---
article_title: PREGUNTAS FRECUENTES
hidden: true
permalink: /onboarding_faq/
excerpt_separator: ""
page_type: glossary
layout: onboarding_faq
description: "Esta página contiene una recopilación de las preguntas más frecuentes, ordenadas por categorías."

---

{% multi_lang_include video.html id="keAZAlBR9zc" source="youtube" %}


<!--- Users --->

{% api %}

### ¿Cómo gestiono los datos de usuario anónimos?

{% apitags %}
Usuarios
{% endapitags %}

Inicialmente, cuando se reconoce un perfil de usuario a través del SDK, Braze crea un perfil de usuario anónimo con un `braze_id` asociado: un identificador de usuario único que es configurado por Braze.

Para realizar un seguimiento más exhaustivo de los usuarios anónimos, puedes implementar [alias de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases) que te permitan etiquetar a los usuarios anónimos con un identificador. Estos usuarios pueden ser exportados utilizando sus alias, o referenciados por la API.

Si un perfil de usuario anónimo con un alias es reconocido posteriormente con un `external_id`, será tratado como un perfil de usuario identificado normal, pero conservará su alias existente y podrá seguir siendo referenciado por ese alias.

Para los usuarios de alias que quieras fusionar con usuarios identificados, puedes fusionar cualquier campo que sea pertinente para el perfil real que quieras conservar. Tendrías que exportar esos datos antes de eliminarlos del perfil de alias utilizando nuestro [punto final Exportar perfil de usuario por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). A continuación, puedes utilizar nuestro [punto final Seguimiento de usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para publicar estos eventos en el perfil que mantuviste. Esto conservará los datos que quieras mantener, como los atributos que se registraron anteriormente en un perfil, pero no en el otro.

Para obtener un desglose completo de los diferentes métodos de recopilación de datos de usuario nuevos y existentes en Braze, consulta [las mejores prácticas de recopilación de datos]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/).

{% endapi %}
{% api %}

### ¿Cómo puedo importar usuarios que ya he recopilado e identificado fuera de Braze?

{% apitags %}
Usuarios
{% endapitags %}

Para importar usuarios previamente identificados, puedes subir un CSV a Braze, o enviar los datos a través de la API.

#### CSV

Puedes subir y actualizar perfiles de usuario mediante archivos CSV desde **Audiencia** > Importar **usuarios.** Al importar tus datos de clientes, tendrás que especificar el identificador único de cada cliente, también conocido como `external_id`.

Antes de iniciar la importación en CSV, es importante que tu equipo de ingeniería sepa cómo se identificarán los usuarios en Braze. Normalmente sería un ID de base de datos utilizado internamente. Esto debería alinearse con la forma en que los usuarios serán identificados por el SDK de Braze en móviles y Web, de modo que cada cliente tenga un único perfil de usuario dentro de Braze en todos sus dispositivos. Más información sobre el [ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) Braze.

Cuando proporciones un `external_id` en tu importación, Braze actualizará cualquier usuario existente con el mismo `external_id` o creará un nuevo usuario identificado con ese `external_id` establecido si no se encuentra ninguno.

Para más información y para descargar plantillas de importación de usuarios en CSV, consulta [importación de usuarios]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

#### API

Para cargar usuarios a través de la API, puedes utilizar nuestro [punto final Seguimiento de usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para importarlos a Braze.

Si no estás seguro de si el usuario ya existe en Braze, puedes implementar nuestro [punto final Exportar perfil de usuario por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para verificarlo. Si identificas que el usuario ya existe en Braze, puedes utilizar nuestro punto final `/users/track` para publicar los nuevos datos que te gustaría añadir al perfil de usuario que ya existe en Braze.

{% alert note %}
Ten en cuenta los siguientes matices cuando utilices el punto final `/users/track`:

- Al crear usuarios de sólo alias a través de este punto final, debes establecer explícitamente el indicador `_update_existing_only` en false.
- Al actualizar el estado de suscripción con este punto final, se actualizará tanto el usuario especificado por su ID externo (como Usuario1) como el estado de suscripción de cualquier usuario con el mismo correo electrónico que ese usuario (Usuario1).
{% endalert %}

{% endapi %}
{% api %}

### ¿Cuál es la diferencia entre los estados de suscripción push?

{% apitags %}
Usuarios
{% endapitags %}

Hay tres opciones de estado de suscripción push: suscrito, adhesión voluntaria y cancelar suscripción.

Por predeterminado, para que tu usuario reciba tus mensajes a través de push, su estado de suscripción push debe ser suscrito o de adhesión voluntaria, y debe estar habilitado para push. Puedes anular esta configuración si es necesario al redactar un mensaje.

|Estado de adhesión voluntaria|Descripción|
|---|---|
|Suscrito| Estado predeterminado de la suscripción push cuando se crea un perfil de usuario en Braze. |
|Adhesión voluntaria| Un usuario ha expresado explícitamente su preferencia por recibir notificaciones push. Braze cambiará automáticamente el estado de adhesión voluntaria de un usuario a `Opted-In` si acepta un mensaje de adhesión voluntaria.<br><br>Esto no se aplica a usuarios con Android 12 o inferior.|
|Cancelar suscripción| Un usuario se da de baja explícitamente de push a través de tu aplicación o de otros métodos que tu marca proporcione. Por defecto, las campañas push de Braze sólo se dirigen a los usuarios que están en `Subscribed` o `Opted-in` para push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
{% api %}

### ¿Qué pasa si he identificado usuarios duplicados?

{% apitags %}
Usuarios
{% endapitags %}

Si has identificado usuarios duplicados, tendrás que limpiar esos perfiles de usuario. Puedes hacerlo mediante los siguientes pasos:

1. Exporta los perfiles de usuario utilizando nuestro punto final `/users/export/ids`.
2. Identifica el perfil de usuario correcto (en última instancia, tu equipo tendrá que decidir cuál es la información correcta) y o bien:
    - Fusiona los campos que sean pertinentes para el perfil real que quieras conservar utilizando el punto final `/user/track`.
    - Elimina el perfil duplicado y no útil sin fusionar ningún dato utilizando el punto final usuarios/eliminar. Después de eliminar un perfil de usuario, **no hay forma de recuperar la información**.

{% alert important %}
Te recomendamos que primero importes los nuevos perfiles de usuario con el `external_id` correcto y los atributos y eventos personalizados correspondientes. Una vez eliminados los perfiles de usuario, no se pueden recuperar, por lo que la eliminación debe ser el último paso.
{% endalert %}

Algunas cosas adicionales a tener en cuenta:

- Cualquier dato de interacción (como campañas o Lienzos recibidos) en perfiles de usuario duplicados se perderá. La única forma de conservar el contexto histórico de interacción es añadirlo como atributo personalizado (como un atributo personalizado de matriz de todas las campañas o Lienzos recibidos).
- Al migrar perfiles de usuario, también depende de tu equipo decidir qué perfil de usuario de los duplicados se conservará. Braze no puede decidir ni proporcionarte una lista de perfiles a eliminar.  
- En última instancia, será importante que tu equipo evalúe el proceso de registro desde la experiencia de tus usuarios y se asegure de que sólo llamas al método `changeUser()` cuando un usuario se identifica.

{% endapi %}
{% api %}

<!-- Segments -->

### ¿Cómo creo un segmento cuando importo un grupo de usuarios a través de CSV?

{% apitags %}
Segmentos
{% endapitags %}

Para importar tu archivo CSV, ve a la página **Importación de** usuarios, en la sección Usuarios. La tabla **Importaciones** recientes muestra hasta veinte de tus importaciones más recientes, sus nombres de archivo, el número de líneas del archivo, el número de líneas importadas con éxito, el total de líneas de cada archivo y el estado de cada importación.

El panel **Importar CSV** contiene instrucciones de importación y un botón para iniciar la importación. Haz clic en **Seleccionar archivo CSV** y selecciona el archivo que te interese. A continuación, antes de hacer clic en **Iniciar importación**, tienes la opción de indicar a Braze qué hacer con esta lista en "Qué quieres que hagamos con los usuarios de este CSV".

Selecciona **Importar usuarios en este CSV y haz posible también reorientar este lote específico de usuarios como un grupo**, y luego selecciona **Generar automáticamente un segmento a partir de los usuarios que se importan de este CSV**. Después de hacer clic en **Iniciar importación**, Braze cargará tu archivo, comprobará los encabezados de columna y los tipos de datos de cada columna, y creará un segmento.

Para descargar una plantilla CSV, consulta [importación de usuarios]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

{% endapi %}
{% api %}

### ¿Qué tipos de filtros puedo utilizar al crear un segmento?

{% apitags %}
Segmentos
{% endapitags %}

El SDK de Braze te proporciona un potente arsenal de filtros para segmentar y dirigirte a tus usuarios en función de características y atributos específicos. Puedes utilizar el glosario de [Filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) para buscar o acotar estos filtros por Categoría de filtro (Datos personalizados, Actividad de usuario, Reorientación, Actividad de marketing, Atributos de usuario, Atribución de instalación, Actividad social, Pruebas, Otros).

{% endapi %}
{% api %}

### ¿Cómo configuro la segmentación por ubicación para poder segmentar a los usuarios según su ubicación más reciente y utilizarla en mis campañas y estrategias basadas en la ubicación?

{% apitags %}
Segmentos
{% endapitags %}

Ve a la página **Segmentos**, en Interacción, para ver todos tus segmentos de usuarios actuales. En esta página puedes crear y nombrar nuevos segmentos. Para empezar, haz clic en **Crear segmento** y dale un nombre a tu segmento.

Una vez que hayas creado tu segmento, añade un filtro `Most Recent Location` para dirigirte a los usuarios según el último lugar en el que utilizaron tu aplicación. Puedes resaltar a los usuarios en una región circular estándar o crear una región poligonal personalizada.

- Para las regiones circulares, puedes mover el origen y ajustar el radio de ubicación de tu segmentación.
- Para las regiones poligonales, puedes designar más específicamente qué zonas deseas incluir en tu segmento.

{% alert tip %}
¿Te interesa aprovechar las ventajas de la orientación por ubicación con la ayuda de un socio de Braze? Consulta nuestros [socios de ubicación contextual]({{site.baseurl}}/partners/message_personalization/) Braze disponibles.
{% endalert %}

{% endapi %}
{% api %}

### ¿Cómo puedo dirigirme a listas precisas de usuarios en función de su evento personalizado y su comportamiento de compra en los últimos 365 días?

{% apitags %}
Segmentos
{% endapitags %}

¡Puedes utilizar las [extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)! Las extensiones de segmento te habilitan para dirigirte a una lista de usuarios más precisa de lo que podrías hacerlo con un segmento normal.

Puedes crear hasta 10 extensiones de segmento por espacio de trabajo. Una vez generadas estas listas de extensiones, se pueden incluir o excluir como filtro en tus segmentos. Al crear una Extensión de segmento, también puedes especificar que la lista se regenere una vez cada 24 horas.

1. En Interacciones, amplía **Segmentos** y haz clic en **Extensión de segmento**.
2. En la tabla Extensiones de segmento, haz clic en **\+ Crear nueva extensión**.
3. Nombra tu extensión de segmento describiendo el tipo de usuarios por los que pretendes filtrar. Esto garantizará que esta extensión pueda descubrirse fácilmente y con precisión al aplicarla como filtro en tu segmento.
4. Selecciona entre un criterio de compra o de evento personalizado para la segmentación.
5. Elige a qué artículo comprado o evento personalizado específico quieres dirigir tu lista de usuarios. 
6. Elige cuántas veces (más, menos o igual) tendría que haber completado el usuario el evento, y cuántos días mirar hacia atrás, hasta 365 días.

Para aumentar la precisión de la segmentación, puedes seleccionar **Añadir filtros de propiedad** y segmentar en función de las propiedades específicas de tu compra o evento personalizado. Braze admite la segmentación de propiedades de eventos basada en objetos de cadena, numéricos, booleanos y temporales.

También admitimos la segmentación basada en [propiedades de eventos anidados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

Las extensiones de segmento dependen del almacenamiento a largo plazo de las propiedades del evento y no tienen el límite de 30 días de almacenamiento de propiedades del evento personalizado. Esto significa que puedes consultar las propiedades del evento rastreadas en el último año, y el seguimiento no espera hasta que se haya configurado primero la extensión.

{% alert note %}
El uso de propiedades del evento dentro de las extensiones de segmento no afecta al uso de punto de datos.
{% endalert %}

{% endapi %}
{% api %}

#### Mantener actualizadas las extensiones de segmento

{% apitags %}
Segmentos
{% endapitags %}

Puedes especificar si quieres que esta extensión represente una única instantánea en el tiempo, o si quieres que se regenere diariamente. Tu extensión siempre empezará a procesarse después del guardado inicial. Si quieres que la extensión se regenere diariamente, selecciona **Regenerar extensión diariamente** y la regeneración comenzará a procesarse hacia la medianoche de cada día en la zona horaria de tu empresa.

Cuando hayas terminado, haz clic en **Guardar**. Tu prórroga comenzará a tramitarse. El tiempo que tarda en generarse tu extensión depende del número de usuarios que tengas, de cuántos eventos personalizados o eventos de compra estés capturando y de cuántos días estés mirando atrás en el historial.

Por último, después de haber creado una extensión, puedes utilizarla como filtro al crear un segmento o definir una audiencia para una campaña o Canvas. Empieza por elegir `Braze Segment Extension` en la lista de filtros de la sección **Atributos de usuario**. En la lista de filtrar Extensiones de segmento de Braze, elige la extensión que deseas incluir o excluir en este segmento. Para ver los criterios de la extensión, haz clic en **Ver detalles de la extensión**. Ahora puedes proceder como de costumbre a crear tu segmento.

{% endapi %}
{% api %}

<!-- Campaigns -->

### ¿Cómo se crea una campaña multicanal?

{% apitags %}
Campañas
{% endapitags %}

Para crear una campaña multicanal, ve a la página **Campañas**, selecciona **Crear campaña** y, a continuación, **Campaña multicanal**. Cuando estés dentro de una campaña multicanal, selecciona **Añadir canal de mensajería** en la pestaña de composición para añadir los canales que desees. Haz clic en los iconos de canal que aparecen para alternar entre diferentes creadores de mensajes a medida que construyes el texto de tu campaña para los diferentes canales.

{% endapi %}
{% api %}

### ¿Cómo puedo empezar a probar y optimizar las campañas?

{% apitags %}
Campañas
{% endapitags %}

¡Crear campañas multivariantes y ejecutar Lienzos con múltiples variantes es una forma estupenda de empezar! Por ejemplo, puedes realizar una [campaña multivariante]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) para probar un mensaje que tenga diferentes copias o líneas del asunto. Los lienzos con múltiples variantes son útiles para probar flujos de trabajo completos.

{% endapi %}
{% api %}

### ¿Por qué hay una diferencia entre el número de destinatarios únicos y el número de envíos para una campaña o Canvas determinado?

{% apitags %}
Campañas
{% endapitags %}

Una posible explicación de esta diferencia podría deberse a que la campaña o el Canvas tuvieran activada la reelegibilidad. Al tener esto activado, los usuarios que cumplan los requisitos del segmento y la configuración de entrega podrán recibir el mensaje más de una vez. Si la reelegibilidad no está activada, la explicación probable de la diferencia entre envíos y destinatarios únicos puede deberse a que los usuarios tienen varios dispositivos en distintas plataformas asociados a sus perfiles.

Por ejemplo, si tienes un Canvas que tiene notificaciones push tanto de iOS como de Web, un usuario determinado con dispositivos móviles y de escritorio podría recibir más de un mensaje.

{% endapi %}
{% api %}

### ¿Qué ofrece la entrega según la zona horaria local?

{% apitags %}
Campañas
{% endapitags %}

La entrega según la zona horaria local te permite entregar campañas de mensajería a un segmento basado en la zona horaria individual de un usuario. Sin entrega según la zona horaria local, las campañas se programarán según la configuración de la zona horaria de tu empresa en Braze.

Por ejemplo, una empresa con sede en Londres que envíe una campaña a las 12 de la noche llegará a los usuarios de la costa oeste de Estados Unidos a las 4 de la madrugada. Si tu aplicación sólo está disponible en determinados países, puede que esto no suponga un riesgo para ti; de lo contrario, ¡te recomendamos encarecidamente que evites enviar notificaciones push de madrugada a tu base de usuarios!

{% endapi %}
{% api %}

### ¿Cómo reconoce Braze la zona horaria de un usuario?

{% apitags %}
Campañas
{% endapitags %}

Braze determinará automáticamente la zona horaria del usuario a partir de su dispositivo. Está diseñado para soportar la precisión de la zona horaria y la cobertura total de tus usuarios. Los usuarios creados a través de la API de usuario o de otra forma sin zona horaria tendrán la zona horaria de tu empresa como zona horaria predeterminada hasta que sean reconocidos en tu aplicación por el SDK.

Puedes comprobar la zona horaria de tu empresa en la [configuración de la misma]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/).

{% endapi %}
{% api %}

### ¿Cómo programo una campaña de zona horaria local?

{% apitags %}
Campañas
{% endapitags %}

Al programar una campaña, tienes que elegir enviarla a una hora determinada y, a continuación, seleccionar **Enviar campaña a los usuarios de su zona horaria local**.

Braze recomienda encarecidamente que todas las campañas de zonas horarias locales se programen con 24 horas de antelación. Dado que una campaña de este tipo debe enviarse a lo largo de todo un día, programarlas con 24 horas de antelación permite que tu mensaje llegue a todo tu segmento. Sin embargo, puedes programar estas campañas con menos de 24 horas de antelación si es necesario. Ten en cuenta que Braze no enviará mensajes a los usuarios que hayan incumplido la hora de envío en más de 1 hora.

Por ejemplo, si es la 1 de la tarde y programas una campaña de zona horaria local para las 3 de la tarde, la campaña se enviará inmediatamente a todos los usuarios cuya hora local sea las 3-4 de la tarde, pero no a los usuarios cuya hora local sea las 5 de la tarde. Además, la hora de envío que elijas para tu campaña tiene que no haber ocurrido todavía en la zona horaria de tu empresa.

Editar una campaña de zona horaria local programada con menos de 24 horas de antelación no alterará la programación del mensaje. Si decides editar una campaña de zona horaria local para enviarla a una hora posterior (por ejemplo, a las 19:00 en lugar de a las 18:00), los usuarios que estaban en el segmento objetivo cuando se eligió la hora de envío original seguirán recibiendo el mensaje a la hora original (18:00). Si editas una zona horaria local para que se envíe a una hora más temprana (por ejemplo, a las 16:00 en lugar de a las 17:00), la campaña se seguirá enviando a todos los miembros del segmento a la hora original (17:00).

{% alert note %}
Para los pasos en Canvas, los usuarios no necesitan estar en el paso durante 24 horas para recibir el siguiente paso para la entrega según la zona horaria local.
{% endalert %}

Si has permitido que los usuarios vuelvan a ser elegibles para la campaña, volverán a recibirla a la hora original (17:00 h). Sin embargo, para todas las apariciones posteriores de tu campaña, tus mensajes sólo se enviarán a la hora que hayas actualizado.

{% endapi %}
{% api %}

### ¿Cuándo entran en vigor los cambios en las campañas de las zonas horarias locales?

{% apitags %}
Campañas
{% endapitags %}

Los segmentos objetivo de las campañas en zonas horarias locales deben incluir al menos un margen de 48 horas para cualquier filtro basado en la hora, con el fin de garantizar la entrega a todo el segmento. Por ejemplo, considera un segmento dirigido a usuarios en su segundo día con los siguientes filtros:

- Aplicación utilizada por primera vez hace más de 1 día
- Aplicación utilizada por primera vez hace menos de 2 días

La entrega según la zona horaria local puede pasar por alto a los usuarios de este segmento en función de la hora de entrega y de la zona horaria local de los usuarios. Esto se debe a que un usuario puede abandonar el segmento en el momento en que su zona horaria desencadena la entrega.

{% endapi %}
{% api %}

### ¿Qué cambios puedo hacer en las campañas programadas antes del lanzamiento?

{% apitags %}
Campañas
{% endapitags %}

Cuando se programa la campaña, hay que editar todo lo que no sea la composición de los mensajes antes de ponerlos en cola para enviarlos. Como en todas las campañas, no puedes editar los eventos de conversión una vez lanzada la campaña.

{% endapi %}
{% api %}

### ¿Cuál es la "zona segura" antes de que se pongan en cola los mensajes de una campaña programada?

{% apitags %}
Campañas
{% endapitags %}

- Las campañas programadas una sola vez pueden editarse hasta la hora de envío programada.
- Las campañas programadas recurrentes pueden editarse hasta la hora de envío programada.
- Las campañas con hora de envío local pueden editarse hasta 24 horas antes de la hora de envío programada.
- Las campañas con la hora de envío óptima pueden editarse hasta 24 horas antes del día en que está previsto que se envíe la campaña.

{% endapi %}
{% api %}

### ¿Qué pasa si hago una edición dentro de la "zona segura"?

{% apitags %}
Campañas
{% endapitags %}

Cambiar la hora de envío de las campañas dentro de este plazo puede provocar comportamientos no deseados, por ejemplo:

- Braze no enviará mensajes a los usuarios que hayan sobrepasado la hora de envío en más de una hora.
- Los mensajes que ya estaban en cola pueden seguir enviándose a la hora originalmente en cola, en lugar de a la hora ajustada.

{% endapi %}
{% api %}

### ¿Qué debo hacer si ya ha pasado la "zona segura"?

{% apitags %}
Campañas
{% endapitags %}

Para garantizar que las campañas funcionan como se desea, recomendamos detener la campaña actual (esto detendrá cualquier mensaje en cola). A continuación, puedes duplicar la campaña, realizar los cambios necesarios y lanzar la nueva campaña. Puede que tengas que excluir de esta campaña a usuarios que ya hayan recibido la primera campaña.

Asegúrate de reajustar las horas de programación de la campaña para permitir el envío según la zona horaria.

{% endapi %}
{% api %}

### ¿Cuándo evalúa Braze a los usuarios para la entrega según la zona horaria local?

{% apitags %}
Campañas
{% endapitags %}

Para la entrega según la zona horaria local, Braze evalúa a los usuarios para determinar si son elegibles para la entrada durante estas dos instancias:

- A la hora de Samoa (UTC+13) del día programado
- A la hora local del día programado

Para que un usuario sea elegible para la entrada, debe ser elegible para ambas comprobaciones. Por ejemplo, si el lanzamiento de un Canvas está programado para el 7 de agosto de 2021 a las 14.00 h de la zona horaria local, dirigirse a un usuario ubicado en Nueva York requeriría las siguientes comprobaciones para ser elegible:

- Nueva York el 6 de agosto de 2021 a las 21.00 horas
- Nueva York el 7 de agosto de 2021 a las 2 pm

El usuario tiene que estar en el segmento 24 horas antes del lanzamiento. Si el usuario no es elegible en la primera comprobación, Braze no intentará la segunda comprobación.

{% endapi %}
{% api %}

### ¿Por qué el número de usuarios que entran en una campaña no coincide con el esperado?

{% apitags %}
Campañas
{% endapitags %}

El número de usuarios que entran en una campaña puede diferir del que esperabas debido a cómo se evalúan las audiencias y los desencadenantes. En Braze, la audiencia se evalúa antes del desencadenamiento (a menos que se utilice un [desencadenamiento por cambio de atributo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Esto hará que los usuarios abandonen la campaña si no forman parte inicialmente de tu audiencia seleccionada antes de que se evalúe cualquier acción desencadenante.

{% endapi %}
{% api %}

<!-- Canvases -->

### ¿Qué ocurre si la audiencia y la hora de envío son idénticas para un Canvas que tiene una variante, pero múltiples ramas?

{% apitags %}
Lienzos
{% endapitags %}

Ponemos en cola un trabajo para cada paso: se ejecutan más o menos al mismo tiempo y uno de ellos "gana". En la práctica, esto puede ordenarse de forma algo uniforme, pero es probable que tenga al menos un ligero sesgo hacia el paso que se creó primero.

Además, no podemos dar garantías sobre cómo será exactamente esa distribución. Si quieres garantizar una división uniforme, añade un filtro de [número de contenedor aleatorio]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/).

{% endapi %}
{% api %}

### ¿Qué ocurre cuando detienes un Canvas?

{% apitags %}
Lienzos
{% endapitags %}

Cuando detienes un Canvas, se aplica lo siguiente:

- Se impedirá a los usuarios entrar en el Canvas.
- No se enviarán más mensajes, a pesar de dónde se encuentre el usuario en el flujo.
    - **Excepción:** Los Lienzos de correo electrónico no se detendrán inmediatamente. Después de que las solicitudes de envío vayan a SendGrid, no hay nada que podamos hacer para impedir que se entreguen al usuario.

{% alert note %}
Al detener un Canvas no saldrán los usuarios que estén esperando en un paso. Si vuelves a habilitar el Canvas y los usuarios siguen esperando, completarán el paso y pasarán al siguiente componente. Sin embargo, si ha pasado el tiempo en el que el usuario debería haber pasado al siguiente componente, saldrá del Canvas.
{% endalert %}

{% endapi %}
{% api %}

### ¿Cuándo se desencadena un evento de excepción?

{% apitags %}
Lienzos
{% endapitags %}

Los eventos de excepción sólo se desencadenan mientras el usuario está esperando recibir el componente Canvas al que está asociado. Si un usuario realiza una acción por adelantado, no se desencadenará el evento de excepción.

Si quieres exceptuar a los usuarios que hayan realizado un determinado evento con antelación, utiliza [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) en su lugar.

{% endapi %}
{% api %}

### ¿Cómo afecta la edición de un Canvas a los usuarios que ya están en él?

{% apitags %}
Lienzos
{% endapitags %}

Si editas algunos de los pasos de un Canvas de varios pasos, los usuarios que ya estaban en la audiencia pero no han recibido los pasos recibirán la versión actualizada del mensaje. Ten en cuenta que esto sólo ocurrirá si aún no han sido evaluados para el paso.

Para más información sobre lo que puedes o no puedes editar después del lanzamiento, consulta [Cambiar tu Canvas después del lanzamiento]({{site.baseurl}}/post-launch_edits/).

{% endapi %}
{% api %}

### ¿Cómo se realiza el seguimiento de las conversiones de los usuarios en un Canvas?

{% apitags %}
Lienzos
{% endapitags %}

Un usuario sólo puede convertir una vez por entrada en Canvas.

Las conversiones se asignan al mensaje más reciente recibido por el usuario para esa entrada. El bloque de resumen al principio de un Canvas refleja todas las conversiones realizadas por los usuarios dentro de esa ruta, hayan recibido o no un mensaje. Cada paso posterior sólo mostrará las conversiones que se produjeron mientras ese fue el paso más reciente que recibió el usuario.

{% details Use cases %}

#### Caso de uso 1

Hay una ruta Canvas con 10 notificaciones push y el evento de conversión es "inicio de sesión" ("Abre la aplicación"):

- El usuario A abre la aplicación después de entrar, pero antes de recibir el primer mensaje.
- El usuario B abre la aplicación después de cada notificación push.

**Resultado:**
El resumen mostrará dos conversiones, mientras que los pasos individuales mostrarán una conversión de uno en el primer paso y cero en todos los pasos siguientes.

{% alert note %}
Si las Horas tranquilas están activas cuando se produce el evento de conversión, se aplican las mismas reglas.
{% endalert %}

#### Caso de uso 2

Hay un paso en Canvas con Horas tranquilas:

1. El usuario entra en el Canvas.
2. El primer paso no tiene retraso, pero está dentro de las horas tranquilas, por lo que el mensaje se suprime.
3. El usuario realiza el evento de conversión.

**Resultado:**
El usuario contará como convertido en la variante en Canvas global, pero no el paso, ya que no recibió el paso.

{% enddetails %}

{% endapi %}
{% api %}

### Al observar el número de usuarios únicos, ¿es más preciso el análisis de Canvas o el segmentador?

{% apitags %}
Lienzos
{% endapitags %}

El segmentador es una estadística más precisa para los datos de usuario únicos que las estadísticas de Canvas o de campaña. Esto se debe a que las estadísticas de Canvas y de campaña son números que Braze incrementa cuando ocurre algo, lo que significa que hay variables que podrían hacer que este número fuera diferente al del segmentador. Por ejemplo, los usuarios pueden convertir más de una vez para un Canvas o una campaña.  

{% endapi %}
{% api %}

### ¿Por qué el número de usuarios que entran en un Canvas no coincide con el esperado?

{% apitags %}
Lienzos
{% endapitags %}

El número de usuarios que entran en un Canvas puede diferir del que esperabas debido a cómo se evalúan las audiencias y los desencadenantes. En Braze, la audiencia se evalúa antes del desencadenamiento (a menos que se utilice un desencadenamiento [por cambio de atributo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) ). Esto hará que los usuarios abandonen el Canvas si no forman parte de tu audiencia seleccionada antes de que se evalúe cualquier acción desencadenante.

{% endapi %}
{% api %}

<!-- Analytics -->

### ¿Qué métricas mide Braze?

{% apitags %}
Análisis
{% endapitags %}

Dependiendo del canal, Braze mide una serie de métricas que te habilitan para determinar el éxito de una campaña e informar sobre las futuras. Puedes encontrar una lista completa en nuestro [glosario de métricas de los informes]({{site.baseurl}}/user_guide/data/report_metrics/).

{% endapi %}
{% api %}

### ¿Cómo se calculan los ingresos en Braze?

{% apitags %}
Análisis
{% endapitags %}

En la página **Ingresos**, puedes ver datos sobre ingresos o compras durante periodos de tiempo concretos, para un producto específico, o los ingresos o compras totales de tu aplicación. Estas cifras de ingresos se generan a partir de las compras realizadas por los destinatarios de la campaña dentro de un determinado periodo de conversión.

Dicho esto, es importante tener en cuenta que Braze es una herramienta de marketing y no de gestión de ingresos. Nuestro [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) no admite devoluciones ni cancelaciones, por lo que puedes ver discrepancias al comparar los datos con otras herramientas.

{% endapi %}
{% api %}

### ¿Qué capacidades de información habilita Currents?

{% apitags %}
Análisis
{% endapitags %}

Nuestra herramienta Currents transmite continuamente tanto datos de interacción con los mensajes como datos de comportamiento del cliente a uno de nuestros muchos socios de datos, lo que te permite utilizar los datos únicos y valiosos que crea Braze para potenciar tus esfuerzos de inteligencia empresarial y análisis en otros socios de primera clase.

Estos datos van más allá de las métricas de interacción con los mensajes, y también pueden incluir cifras más complejas, como el rendimiento de los atributos personalizados y los eventos. Para más detalles, consulta nuestro [glosario de eventos Currents]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/).

{% endapi %}
{% api %}

### ¿Cómo puedo programar un informe de interacción recurrente?

{% apitags %}
Análisis
{% endapitags %}

Para programar un informe de interacción recurrente, haz lo siguiente:

1. En tu cuenta del panel, ve a **Informes de interacción**, en **Datos**.
2. Haz clic en **\+ Crear informe nuevo**.
3. Añade las [campañas y mensajes de Canvas]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#manually-select-campaigns-or-canvases) (individualmente o [por etiquetas]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases)) que quieras compilar en tu informe.
4. [Añade estadísticas]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#add-statistics-to-your-report) a tu informe.
5. Selecciona la compresión y el eliminador para tu informe.
6. Introduce las direcciones de correo electrónico de los usuarios de Braze que deben recibir este informe.
7. Selecciona el [periodo de]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#time-frame) tiempo a partir del cual quieres que tu informe ejecute datos.
8. Selecciona los [intervalos (diario, semanal, etc.)]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#data-display) en los que deseas ver el desglose de tus datos.
9. Programa tu informe para que [se envíe inmediatamente]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#send-immediately) o en un [momento futuro especificado]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#send-at-designated-time).
10. Ejecuta el informe, ¡y ábrelo en tu correo electrónico cuando llegue!

{% endapi %}
{% api %}

### ¿Cuál es la diferencia entre los informes de interacción y el generador de informes?

{% apitags %}
Análisis
{% endapitags %}

Los informes de interacción te proporcionan CSV de estadísticas de interacción para mensajes específicos de campañas y Canvases a través de un correo electrónico desencadenado. Determinados datos se agregan a nivel de campaña o Canvas frente al nivel de variante o paso individual. Los informes no se guardan en el panel, y volver a ejecutar el informe puede dar lugar a estadísticas actualizadas.

El generador de informes te permite comparar los resultados de varias campañas o Canvases en una sola vista, para que puedas determinar fácilmente qué estrategias de interacción han tenido un mayor impacto en tus métricas clave. Tanto para las campañas como para los Lienzos, puedes exportar tus datos y guardar tu informe para consultarlo en el futuro.

Para más información sobre los usos de los informes y análisis en Braze, consulta el [resumen de informes]({{site.baseurl}}/user_guide/analytics/reporting/reports_overview/).

{% endapi %}
