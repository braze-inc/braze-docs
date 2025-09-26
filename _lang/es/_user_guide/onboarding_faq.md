---
article_title: Preguntas frecuentes
hidden: true
permalink: /onboarding_faq/
excerpt_separator: ""
page_type: glossary
layout: onboarding_faq
description: "Esta página contiene una recopilación de las preguntas más frecuentes, clasificadas por categorías."

---

{% multi_lang_include video.html id="keAZAlBR9zc" source="youtube" %}


<!--- Users --->

{% api %}

### ¿Cómo se gestionan los datos anónimos de los usuarios?

{% apitags %}
Usuarios
{% endapitags %}

Inicialmente, cuando se reconoce un perfil de usuario a través del SDK, Braze crea un perfil de usuario anónimo con un `braze_id` asociado: un identificador de usuario único que establece Braze.

Para realizar un seguimiento más exhaustivo de los usuarios anónimos, puedes implementar [alias de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases) que te permitan etiquetar a los usuarios anónimos con un identificador. A continuación, estos usuarios pueden exportarse utilizando sus alias, o referenciarse mediante la API.

Si un perfil de usuario anónimo con un alias es reconocido posteriormente con un `external_id`, será tratado como un perfil de usuario identificado normal, pero conservará su alias existente y podrá seguir siendo referenciado por ese alias.

Para los usuarios de alias que desee fusionar con usuarios identificados, puede fusionar cualquier campo que sea pertinente para el perfil real que desee conservar. Tendría que exportar esos datos antes de eliminarlos del perfil de alias utilizando nuestro [punto final Exportar perfil de usuario por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). A continuación, puede utilizar nuestro [punto final Seguimiento de usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para publicar estos eventos en el perfil que ha conservado. Esto preservará cualquier dato que desee conservar, como los atributos que se registraron previamente en un perfil, pero no en el otro.

Para obtener un desglose completo de los diferentes métodos de recopilación de datos de usuarios nuevos y existentes en Braze, consulte [las mejores prácticas de recopilación de datos]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/).

{% endapi %}
{% api %}

### ¿Cómo puedo importar usuarios que ya he recopilado e identificado fuera de Braze?

{% apitags %}
Usuarios
{% endapitags %}

Para importar usuarios previamente identificados, puede cargar un CSV en Braze o enviar datos a través de la API.

#### CSV

Puede cargar y actualizar perfiles de usuario mediante archivos CSV desde **Audiencia** > **Importar usuarios**. Al importar los datos de sus clientes, deberá especificar el identificador único de cada cliente, también conocido como `external_id`.

Antes de iniciar la importación de CSV, es importante que su equipo de ingeniería sepa cómo se identificarán los usuarios en Braze. Normalmente se trata de un ID de base de datos utilizado internamente. Esto debería alinearse con la forma en que los usuarios serán identificados por el SDK Braze en móviles y web, de modo que cada cliente tendrá un único perfil de usuario dentro de Braze en todos sus dispositivos. Más información sobre el [ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) Braze.

Cuando proporcione un `external_id` en su importación, Braze actualizará cualquier usuario existente con el mismo `external_id` o creará un nuevo usuario identificado con ese conjunto `external_id` si no se encuentra ninguno.

Para más información y para descargar plantillas de importación de usuarios en CSV, consulta [importación de usuarios]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

#### API

Para cargar usuarios a través de la API, puedes utilizar nuestro [punto final Seguimiento de usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para importarlos a Braze.

Si no está seguro de si el usuario ya existe en Braze, puede implementar nuestro [punto final Exportar perfil de usuario por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para verificarlo. Si identifica que el usuario ya existe en Braze, puede utilizar nuestro punto final `/users/track` para publicar los nuevos datos que desea añadir al perfil de usuario que ya existe en Braze.

{% alert note %}
Ten en cuenta los siguientes matices cuando utilices el punto final `/users/track`:

- Al crear usuarios de sólo alias a través de este punto final, debe establecer explícitamente el indicador `_update_existing_only` en false.
- La actualización del estado de suscripción con este punto final actualizará tanto el usuario especificado por su ID externo (como Usuario1) como el estado de suscripción de cualquier usuario con el mismo correo electrónico que ese usuario (Usuario1).
{% endalert %}

{% endapi %}
{% api %}

### ¿Cuál es la diferencia entre los estados de suscripción push?

{% apitags %}
Usuarios
{% endapitags %}

Hay tres opciones de estado de suscripción push: suscrito, adhesión voluntaria y cancelar suscripción.

Por defecto, para que tu usuario reciba tus mensajes a través de push, su estado de suscripción push debe ser suscrito u optado, y debe estar habilitado para push. Puede anular esta configuración si es necesario al redactar un mensaje.

|Estado de adhesión voluntaria|Descripción|
|---|---|
|Suscrito| Estado predeterminado de la suscripción push cuando se crea un perfil de usuario en Braze. |
|Adhesión voluntaria| Un usuario ha expresado explícitamente su preferencia por recibir notificaciones push. Braze cambiará automáticamente el estado de adhesión voluntaria de un usuario a `Opted-In` si acepta un mensaje de adhesión voluntaria.<br><br>Esto no se aplica a usuarios con Android 12 o inferior.|
|No suscrito| Un usuario se da de baja explícitamente de push a través de tu aplicación o de otros métodos que tu marca pone a tu disposición. Por defecto, las campañas push de Braze sólo se dirigen a los usuarios que están en `Subscribed` o `Opted-in` para push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
{% api %}

### ¿Qué pasa si he identificado usuarios duplicados?

{% apitags %}
Usuarios
{% endapitags %}

Si ha identificado usuarios duplicados, tendrá que limpiar esos perfiles de usuario. Puede hacerlo mediante los siguientes pasos:

1. Exporte los perfiles de usuario utilizando nuestro endpoint `/users/export/ids`.
2. Identificar el perfil de usuario correcto (en última instancia, su equipo tendrá que decidir sobre la información correcta) y, o bien:
    - Fusiona los campos que sean pertinentes para el perfil real que quieras conservar utilizando el punto final `/user/track`.
    - Elimina el perfil duplicado y no útil sin fusionar ningún dato utilizando el punto final usuarios/eliminar. Después de eliminar un perfil de usuario, **no hay forma de recuperar la información**.

{% alert important %}
Le recomendamos que primero importe los nuevos perfiles de usuario con la dirección `external_id` correcta y los atributos y eventos personalizados correspondientes. Una vez eliminados los perfiles de usuario, no se pueden recuperar, por lo que la eliminación debe ser el último paso.
{% endalert %}

Algunas cosas adicionales a tener en cuenta:

- Cualquier dato de participación (como campañas o Canvases recibidos) en perfiles de usuario duplicados se perderá. La única forma de conservar el contexto histórico de participación es añadirlo como atributo personalizado (como un atributo personalizado de matriz de todas las campañas o lienzos recibidos).
- Al migrar perfiles de usuario, también depende de su equipo decidir qué perfil de usuario de los duplicados se conservará. Braze no puede decidir ni proporcionarte una lista de perfiles que eliminar.  
- En última instancia, será importante que su equipo evalúe el proceso de registro desde la experiencia de los usuarios y se asegure de que sólo llama al método `changeUser()` cuando un usuario se identifica.

{% endapi %}
{% api %}

<!-- Segments -->

### ¿Cómo puedo crear un segmento cuando importo un grupo de usuarios a través de CSV?

{% apitags %}
Segmentos
{% endapitags %}

Para importar su archivo CSV, vaya a la página de **importación de** usuarios en la sección Usuarios. La tabla de **importaciones recientes** muestra hasta veinte de las importaciones más recientes, sus nombres de archivo, el número de líneas del archivo, el número de líneas importadas correctamente, el total de líneas de cada archivo y el estado de cada importación.

El panel **Importar CSV** contiene instrucciones de importación y un botón para iniciar la importación. Haga clic en **Seleccionar archivo CSV** y seleccione el archivo que le interese. A continuación, antes de hacer clic en **Iniciar importación**, tiene la opción de indicar a Braze qué hacer con esta lista en "Qué desea que hagamos con los usuarios de este CSV".

Selecciona **Importar usuarios en este CSV y haz posible también reorientar este lote específico de usuarios como un grupo**, y luego selecciona **Generar automáticamente un segmento a partir de los usuarios que se importan de este CSV**. Tras hacer clic en **Iniciar importación**, Braze cargará el archivo, comprobará los encabezados de columna y los tipos de datos de cada columna, y creará un segmento.

Para descargar una plantilla CSV, consulta [importación de usuarios]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

{% endapi %}
{% api %}

### ¿Qué tipos de filtros puedo utilizar al crear un segmento?

{% apitags %}
Segmentos
{% endapitags %}

El SDK de Braze te proporciona un potente arsenal de filtros para segmentar y dirigirte a tus usuarios en función de características y atributos específicos. Puede utilizar el glosario de [Filtros de Segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) para buscar o acotar estos filtros por Categoría de Filtro (Datos Personalizados, Actividad de Usuario, Retargeting, Actividad de Marketing, Atributos de Usuario, Atribución de Instalaciones, Actividad Social, Pruebas, Otros).

{% endapi %}
{% api %}

### ¿Cómo configuro la segmentación por ubicación para poder segmentar a los usuarios según su ubicación más reciente y utilizarla en mis campañas y estrategias basadas en la ubicación?

{% apitags %}
Segmentos
{% endapitags %}

Vaya a la página **Segmentos**, en Compromiso, para ver todos sus segmentos de usuarios actuales. En esta página puede crear y nombrar nuevos segmentos. Para empezar, haga clic en **Crear segmento** y asigne un nombre a su segmento.

Una vez que haya creado su segmento, añada un filtro `Most Recent Location` para dirigirse a los usuarios por el último lugar en el que utilizaron su aplicación. Puede resaltar a los usuarios en una región circular estándar o crear una región poligonal personalizada.

- Para las regiones circulares, puede mover el origen y ajustar el radio de ubicación para su segmentación.
- Para las regiones poligonales, puede designar más específicamente qué áreas desea incluir en su segmento.

{% alert tip %}
¿Le interesa aprovechar las ventajas de la orientación por localización con la ayuda de un socio de Braze? Consulta nuestros [socios de ubicación contextual]({{site.baseurl}}/partners/message_personalization/) Braze disponibles.
{% endalert %}

{% endapi %}
{% api %}

### ¿Cómo puedo dirigirme a listas precisas de usuarios en función de su evento personalizado y su comportamiento de compra en los últimos 365 días?

{% apitags %}
Segmentos
{% endapitags %}

Puede utilizar [extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) Las extensiones de segmento le permiten dirigirse a una lista de usuarios más precisa de lo que podría hacerlo con un segmento normal.

Puede crear hasta 10 extensiones de segmento por área de trabajo. Una vez generadas estas listas de extensiones, pueden incluirse o excluirse como filtro en sus segmentos. Al crear una Extensión de segmento, también puede especificar que la lista se regenere una vez cada 24 horas.

1. En Compromisos, expanda **Segmentos** y haga clic en **Extensión de segmento**.
2. En la tabla Extensiones de segmento, haga clic en **\+ Crear nueva extensión**.
3. Nombre su Extensión de Segmento describiendo el tipo de usuarios que pretende filtrar. Esto garantizará que esta extensión pueda descubrirse fácilmente y con precisión al aplicarla como filtro en su segmento.
4. Seleccione entre un criterio de compra o de evento personalizado para la segmentación.
5. Elija a qué artículo comprado o evento personalizado específico desea dirigir su lista de usuarios. 
6. Elija cuántas veces (más, menos o igual) el usuario tendría que haber completado el evento, y cuántos días mirar hacia atrás, hasta 365 días.

Para aumentar la precisión de la segmentación, puede seleccionar **Añadir filtros de propiedades** y segmentar en función de las propiedades específicas de su compra o evento personalizado. Braze admite la segmentación de propiedades de eventos basada en objetos de cadena, numéricos, booleanos y temporales.

También admitimos la segmentación basada en [propiedades de eventos anidados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

Las extensiones de segmento se basan en el almacenamiento a largo plazo de propiedades de eventos y no tienen el límite de almacenamiento de propiedades de eventos personalizados de 30 días. Esto significa que puede consultar las propiedades de eventos rastreadas en el último año, y el rastreo no espera hasta que se haya configurado primero la extensión.

{% alert note %}
El uso de propiedades de eventos dentro de las Extensiones de Segmento no afecta al uso de puntos de datos.
{% endalert %}

{% endapi %}
{% api %}

#### Mantener actualizadas las extensiones de segmento

{% apitags %}
Segmentos
{% endapitags %}

Puedes especificar si quieres esta extensión para representar una simple imagen en el tiempo, o si quieres que la extensión se regenere a diario. Tu extensión siempre comenzará a procesarse después del guardado inicial. Si desea que la extensión se regenere diariamente, seleccione **Regenerar extensión diariamente** y la regeneración comenzará a procesarse alrededor de la medianoche de cada día en la zona horaria de su empresa.

Cuando hayas terminado, haz clic en **Guardar**. Su prórroga comenzará a tramitarse. El tiempo que se tarda en generar la extensión depende del número de usuarios que tengas, de cuántos eventos personalizados o de compra estés capturando y de cuántos días estés mirando hacia atrás en el historial.

Por último, una vez creada una extensión, puede utilizarla como filtro al crear un segmento o definir un público para una campaña o Canvas. Para empezar, seleccione `Braze Segment Extension` en la lista de filtros de la sección **Atributos de usuario**. En la lista de filtros Extensión de segmento Braze, elija la extensión que desea incluir o excluir en este segmento. Para ver los criterios de extensión, haga clic en **Ver detalles de extensión**. Ahora puedes proceder como de costumbre con [la creación de tu segmento.

{% endapi %}
{% api %}

<!-- Campaigns -->

### ¿Cómo se crea una campaña multicanal?

{% apitags %}
Campañas
{% endapitags %}

Para crear una campaña multicanal, vaya a la página **Campañas**, seleccione **Crear campaña** y, a continuación, **Campaña multicanal**. Cuando esté dentro de una campaña multicanal, seleccione **Añadir canal de mensajería** en la pestaña de composición para añadir los canales que desee. Haga clic en los iconos de canal que aparecen para alternar entre los distintos compositores de mensajes a medida que elabora el texto de su campaña para los distintos canales.

{% endapi %}
{% api %}

### ¿Cómo puedo empezar a probar y optimizar las campañas?

{% apitags %}
Campañas
{% endapitags %}

La creación de campañas multivariantes y la ejecución de lienzos con múltiples variantes son una buena forma de empezar. Por ejemplo, puede realizar una [campaña multivariante]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) para probar un mensaje con diferentes copias o líneas de asunto. Los lienzos con múltiples variantes son útiles para probar flujos de trabajo completos.

{% endapi %}
{% api %}

### ¿Por qué existe una diferencia entre el número de destinatarios únicos y el número de envíos para una campaña o un Canvas determinados?

{% apitags %}
Campañas
{% endapitags %}

Una posible explicación de esta diferencia podría deberse a que la campaña o Canvas tuvieran activada la reelegibilidad. Al tenerla activada, los usuarios que cumplan los requisitos del segmento y de la configuración de delivery podrán recibir el mensaje más de una vez. Si la reelegibilidad no está activada, entonces la explicación probable de la diferencia entre envíos y destinatarios únicos puede deberse a que los usuarios tienen múltiples dispositivos a través de plataformas asociadas a sus perfiles.

Por ejemplo, si tienes un Canvas con notificaciones push tanto para iOS como para la web, un usuario determinado con dispositivos móviles y de escritorio podría recibir más de un mensaje.

{% endapi %}
{% api %}

### ¿Qué ofrece la entrega en zona horaria local?

{% apitags %}
Campañas
{% endapitags %}

La entrega en zona horaria local le permite entregar campañas de mensajería a un segmento en función de la zona horaria individual de un usuario. Sin entrega en zona horaria local, las campañas se programarán en función de la configuración de zona horaria de su empresa en Braze.

Por ejemplo, una empresa con sede en Londres que envíe una campaña a las 12 de la noche llegará a los usuarios de la costa oeste de Estados Unidos a las 4 de la madrugada. Si tu aplicación sólo está disponible en determinados países, puede que esto no suponga un riesgo para ti; de lo contrario, te recomendamos encarecidamente que evites enviar notificaciones push de madrugada a tu base de usuarios.

{% endapi %}
{% api %}

### ¿Cómo reconoce Braze la zona horaria de un usuario?

{% apitags %}
Campañas
{% endapitags %}

Braze determinará automáticamente la zona horaria del usuario a partir de su dispositivo. Está diseñado para soportar la precisión de la zona horaria y la cobertura total de sus usuarios. Los usuarios creados a través de la API de usuario o de otro modo sin zona horaria tendrán la zona horaria de su empresa como zona horaria por defecto hasta que sean reconocidos en su aplicación por el SDK.

Puede comprobar la zona horaria de su empresa en la [configuración de la misma]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/).

{% endapi %}
{% api %}

### ¿Cómo programar una campaña de zona horaria local?

{% apitags %}
Campañas
{% endapitags %}

Al programar una campaña, debe elegir enviarla a una hora determinada y, a continuación, seleccionar **Enviar campaña a los usuarios de su zona horaria local**.

Braze recomienda encarecidamente que todas las campañas en zonas horarias locales se programen con 24 horas de antelación. Dado que una campaña de este tipo debe enviarse a lo largo de todo un día, programarlas con 24 horas de antelación permite que su mensaje llegue a todo su segmento. Sin embargo, puedes programar estas campañas con menos de 24 horas de antelación si es necesario. Ten en cuenta que Braze no enviará mensajes a los usuarios que hayan incumplido la hora de envío en más de 1 hora.

Por ejemplo, si es la 1 de la tarde y programa una campaña de zona horaria local para las 3 de la tarde, la campaña se enviará inmediatamente a todos los usuarios cuya hora local sea 3-4 de la tarde, pero no a los usuarios cuya hora local sea 5 de la tarde. Además, la hora de envío que elija para su campaña tiene que no haber ocurrido todavía en la zona horaria de su empresa.

La edición de una campaña de zona horaria local programada con menos de 24 horas de antelación no alterará la programación del mensaje. Si decide editar una campaña de zona horaria local para enviarla a una hora posterior (por ejemplo, a las 19:00 en lugar de a las 18:00), los usuarios que se encontraban en el segmento objetivo cuando se eligió la hora de envío original seguirán recibiendo el mensaje a la hora original (18:00). Si edita una zona horaria local para que se envíe a una hora más temprana (por ejemplo, a las 16:00 en lugar de a las 17:00), la campaña se seguirá enviando a todos los miembros del segmento a la hora original (17:00).

{% alert note %}
Para los pasos de Canvas, los usuarios no necesitan estar en el paso durante 24 horas para recibir el siguiente paso para la entrega de la zona horaria local.
{% endalert %}

Si has permitido que los usuarios vuelvan a ser elegibles para la campaña, volverán a recibirla a la hora original (17:00 h). Sin embargo, para todas las apariciones posteriores de tu campaña, tus mensajes solo se enviarán a la hora que hayas actualizado.

{% endapi %}
{% api %}

### ¿Cuándo entran en vigor los cambios en las campañas de la zona horaria local?

{% apitags %}
Campañas
{% endapitags %}

Los segmentos objetivo para campañas en zonas horarias locales deben incluir al menos una ventana de 48 horas para cualquier filtro basado en la hora para garantizar la entrega a todo el segmento. Por ejemplo, considere un segmento dirigido a usuarios en su segundo día con los siguientes filtros:

- Aplicación utilizada por primera vez hace más de 1 día
- La primera vez que usé la aplicación fue hace menos de 2 días

La entrega en zona horaria local puede pasar por alto a los usuarios de este segmento en función de la hora de entrega y de la zona horaria local de los usuarios. Esto se debe a que un usuario puede abandonar el segmento en el momento en que su zona horaria activa la entrega.

{% endapi %}
{% api %}

### ¿Qué cambios puedo hacer en las campañas programadas antes de su lanzamiento?

{% apitags %}
Campañas
{% endapitags %}

Cuando la campaña está programada, es necesario editar todo lo que no sea la composición de los mensajes antes de ponerlos en cola para su envío. Como en todas las campañas, no se pueden editar los eventos de conversión una vez lanzada la campaña.

{% endapi %}
{% api %}

### ¿Cuál es la "zona segura" antes de que se pongan en cola los mensajes de una campaña programada?

{% apitags %}
Campañas
{% endapitags %}

- Las campañas programadas una sola vez pueden editarse hasta la hora de envío programada.
- Las campañas programadas recurrentes pueden editarse hasta la hora de envío programada.
- Las campañas con hora de envío local pueden editarse hasta 24 horas antes de la hora de envío programada.
- Las campañas con la hora de envío óptima pueden editarse hasta 24 horas antes del día previsto para el envío de la campaña.

{% endapi %}
{% api %}

### ¿Qué ocurre si realizo una edición dentro de la "zona segura"?

{% apitags %}
Campañas
{% endapitags %}

Cambiar la hora de envío en las campañas dentro de este plazo puede provocar comportamientos no deseados, por ejemplo:

- Braze no enviará mensajes a los usuarios que hayan incumplido la hora de envío en más de una hora.
- Los mensajes que ya estaban en cola pueden seguir enviándose a la hora originalmente en cola, en lugar de a la hora ajustada.

{% endapi %}
{% api %}

### ¿Qué debo hacer si la "zona segura" ya ha pasado?

{% apitags %}
Campañas
{% endapitags %}

Para asegurarse de que las campañas funcionan como se desea, recomendamos detener la campaña actual (esto detendrá cualquier mensaje en cola). A continuación, puede duplicar la campaña, realizar los cambios necesarios y lanzar la nueva campaña. Es posible que tenga que excluir de esta campaña a los usuarios que ya hayan recibido la primera campaña.

Asegúrese de reajustar las horas de programación de la campaña para tener en cuenta el envío según la zona horaria.

{% endapi %}
{% api %}

### ¿Cuándo evalúa Braze a los usuarios para la entrega según la zona horaria local?

{% apitags %}
Campañas
{% endapitags %}

Para la entrega en zona horaria local, Braze evalúa la elegibilidad de los usuarios para la entrada durante estas dos instancias:

- A la hora de Samoa (UTC +13) del día programado
- A la hora local del día programado

Para que un usuario sea elegible para la entrada, debe ser elegible para ambas comprobaciones. Por ejemplo, si el lanzamiento de un Canvas está programado para el 7 de agosto de 2021 a las 14.00 horas (zona horaria local), la selección de un usuario ubicado en Nueva York requeriría las siguientes comprobaciones de elegibilidad:

- Nueva York el 6 de agosto de 2021 a las 9 pm
- Nueva York el 7 de agosto de 2021 a las 2 pm

El usuario debe estar en el segmento 24 horas antes del lanzamiento. Si el usuario no cumple los requisitos en la primera comprobación, Braze no intentará la segunda.

{% endapi %}
{% api %}

### ¿Por qué el número de usuarios que entran en una campaña no coincide con el esperado?

{% apitags %}
Campañas
{% endapitags %}

El número de usuarios que entran en una campaña puede diferir del número esperado debido a cómo se evalúan las audiencias y los desencadenantes. En Braze, la audiencia se evalúa antes del desencadenamiento (a menos que se utilice un [desencadenamiento por cambio de atributo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Esto hará que los usuarios abandonen la campaña si inicialmente no forman parte de la audiencia seleccionada antes de que se evalúen las acciones desencadenantes.

{% endapi %}
{% api %}

<!-- Canvases -->

### ¿Qué ocurre si la audiencia y el tiempo de envío son idénticos para un Canvas que tiene una variante, pero múltiples ramas?

{% apitags %}
Canvas
{% endapitags %}

Ponemos en cola un trabajo para cada paso: se ejecutan más o menos al mismo tiempo y uno de ellos "gana". En la práctica, la clasificación puede ser algo uniforme, pero es probable que tenga al menos un ligero sesgo hacia el paso que se creó en primer lugar.

Además, no podemos garantizar cómo será exactamente esa distribución. Si desea garantizar una división uniforme, añada un filtro [de número de cubo aleatorio]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/).

{% endapi %}
{% api %}

### ¿Qué ocurre cuando se detiene un lienzo?

{% apitags %}
Canvas
{% endapitags %}

Cuando detienes un Canvas, se aplica lo siguiente:

- Se impedirá a los usuarios entrar en el Canvas.
- No se enviarán más mensajes, sin importar dónde se encuentre el usuario en el flujo.
    - **Excepción:** Los Canvas de correo electrónico no se detendrán inmediatamente. Después de que las solicitudes de envío vayan a SendGrid, no hay nada que podamos hacer para evitar que se entreguen al usuario.

{% alert note %}
Al detener un Canvas no saldrán los usuarios que estén esperando en un paso. Si vuelve a activar el lienzo y los usuarios siguen esperando, completarán el paso y pasarán al siguiente componente. Sin embargo, si ha transcurrido el tiempo en el que el usuario debería haber pasado al siguiente componente, saldrá del lienzo.
{% endalert %}

{% endapi %}
{% api %}

### ¿Cuándo se desencadena un evento de excepción?

{% apitags %}
Canvas
{% endapitags %}

Los eventos de excepción sólo se desencadenan mientras el usuario está esperando recibir el componente Canvas al que está asociado. Si un usuario realiza una acción por adelantado, el evento de excepción no se desencadenará.

Si desea exceptuar a los usuarios que han realizado un determinado evento con antelación, utilice [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) en su lugar.

{% endapi %}
{% api %}

### ¿Cómo afecta la edición de un lienzo a los usuarios que ya están en él?

{% apitags %}
Canvas
{% endapitags %}

Si edita algunos de los pasos de un Canvas de varios pasos, los usuarios que ya estaban en la audiencia pero no han recibido los pasos recibirán la versión actualizada del mensaje. Ten en cuenta que esto solo ocurrirá si aún no han sido evaluados para el paso.

Para obtener más información sobre lo que puede o no puede editar después del lanzamiento, consulte [Cambiar tu Canvas después del lanzamiento]({{site.baseurl}}/post-launch_edits/).

{% endapi %}
{% api %}

### ¿Cómo se realiza el seguimiento de las conversiones de los usuarios en un Canvas?

{% apitags %}
Canvas
{% endapitags %}

Un usuario sólo puede convertir una vez por entrada de Canvas.

Las conversiones se asignan al mensaje más reciente recibido por el usuario para esa entrada. El bloque de resumen al principio de un Canvas refleja todas las conversiones realizadas por los usuarios dentro de esa ruta, hayan recibido o no un mensaje. Cada paso posterior solo mostrará las conversiones que se produjeron mientras ese era el paso más reciente recibido por el usuario.

{% details Casos de uso %}

#### Caso de uso 1

Hay una ruta de Canvas con 10 notificaciones push y el evento de conversión es «session start» (inicio de sesión) («Opens App» [Abre la aplicación]):

- El usuario A abre la aplicación después de entrar pero antes de recibir el primer mensaje.
- El usuario B abre la aplicación después de cada notificación push.

**Resultado:**
El resumen mostrará dos conversiones, mientras que los pasos individuales mostrarán una conversión de uno en el primer paso y cero en todos los pasos posteriores.

{% alert note %}
Si las Horas de Silencio están activas cuando se produce el evento de conversión, se aplican las mismas reglas.
{% endalert %}

#### Caso de uso 2

Hay un lienzo de un solo paso con las horas de silencio:

1. El usuario entra en el lienzo.
2. El primer paso no tiene retraso, pero está dentro de las Horas de Silencio, por lo que el mensaje se suprime.
3. El usuario realiza el evento de conversión.

**Resultado:**
El usuario contará como convertido en la variante general Canvas, pero no el paso ya que no recibió el paso.

{% enddetails %}

{% endapi %}
{% api %}

### Si nos fijamos en el número de usuarios únicos, ¿es más preciso el análisis de Canvas o el segmentador?

{% apitags %}
Canvas
{% endapitags %}

El segmentador es una estadística más precisa para los datos de usuario único frente a las estadísticas de Canvas o de campaña. Esto se debe a que las estadísticas de Canvas y de campaña son números que Braze incrementa cuando ocurre algo, lo que significa que hay variables que podrían hacer que este número fuera diferente al del segmentador. Por ejemplo, los usuarios pueden convertir más de una vez un Canvas o una campaña.  

{% endapi %}
{% api %}

### ¿Por qué el número de usuarios que entran en un lienzo no coincide con el número esperado?

{% apitags %}
Canvas
{% endapitags %}

El número de usuarios que entran en un Canvas puede diferir del número esperado debido a cómo se evalúan las audiencias y los activadores. En Braze, un público se evalúa antes del desencadenante (a menos que se utilice un desencadenante de [cambio de atributo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) ). Esto hará que los usuarios abandonen el Canvas si no forman parte de su audiencia seleccionada antes de que se evalúe cualquier acción desencadenante.

{% endapi %}
{% api %}

<!-- Analytics -->

### ¿Qué parámetros mide Braze?

{% apitags %}
Análisis
{% endapitags %}

Dependiendo del canal, Braze mide una variedad de métricas que le permiten determinar el éxito de una campaña e informar sobre las futuras. Encontrará una lista completa en nuestro [glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics/).

{% endapi %}
{% api %}

### ¿Cómo se calculan los ingresos en Braze?

{% apitags %}
Análisis
{% endapitags %}

En la página **Ingresos**, puede ver datos sobre ingresos o compras durante periodos de tiempo específicos, para un producto concreto, o los ingresos o compras totales de su aplicación. Estas cifras de ingresos se generan a partir de las compras realizadas por los destinatarios de la campaña dentro de un determinado periodo de conversión.

Dicho esto, es importante tener en cuenta que Braze es una herramienta de marketing y no de administración de ingresos. Nuestro [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) no admite reembolsos ni cancelaciones, por lo que es posible que aparezcan discrepancias al comparar los datos con otras herramientas.

{% endapi %}
{% api %}

### ¿Qué funciones de elaboración de informes permite Currents?

{% apitags %}
Análisis
{% endapitags %}

Nuestra herramienta Currents transmite continuamente datos sobre la participación en la mensajería y el comportamiento de los clientes a uno de nuestros muchos socios de datos, lo que le permite utilizar los datos únicos y valiosos que crea Braze para potenciar sus esfuerzos de inteligencia empresarial y análisis en otros socios de primera clase.

Estos datos van más allá de las métricas de participación en la mensajería, y también pueden incluir cifras más complejas, como el rendimiento de atributos y eventos personalizados. Para más detalles, consulta nuestro [glosario de eventos Currents]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/).

{% endapi %}
{% api %}

### ¿Cómo puedo programar un informe de compromiso recurrente?

{% apitags %}
Análisis
{% endapitags %}

Para programar un informe de compromiso recurrente, haga lo siguiente:

1. En tu cuenta del panel, ve a **Informes de interacción**, en **Datos**.
2. Haga clic en **\+ Crear nuevo informe**.
3. Añada las [campañas y los mensajes Canvas]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#manually-select-campaigns-or-canvases) (individualmente o [por etiqueta]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases)) que desee compilar en su informe.
4. [Añade estadísticas]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#add-statistics-to-your-report) a tu informe.
5. Seleccione la compresión y el eliminador para su informe.
6. Introduzca las direcciones de correo electrónico de los usuarios de Braze que deben recibir este informe.
7. Seleccione el [intervalo de tiempo]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#time-frame) a partir del cual desea que su informe ejecute los datos.
8. Seleccione los [intervalos (diario, semanal, etc.)]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#data-display) en los que desea ver el desglose de sus datos.
9. Programe su informe para que [se envíe inmediatamente]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#send-immediately) o en un [momento futuro especificado]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#send-at-designated-time).
10. Ejecute el informe y ábralo en su correo electrónico cuando le llegue.

{% endapi %}
{% api %}

### ¿Cuál es la diferencia entre los informes de actividad y el generador de informes?

{% apitags %}
Análisis
{% endapitags %}

Los informes de participación le proporcionan CSV de estadísticas de participación para mensajes específicos de campañas y lienzos a través de un correo electrónico activado. Determinados datos se agregan a nivel de campaña o Canvas frente al nivel de variante o paso individual. Los informes no se guardan en el cuadro de mandos, y volver a ejecutar el informe puede dar lugar a estadísticas actualizadas.

El generador de informes le permite comparar los resultados de varias campañas o lienzos en una sola vista para que pueda determinar fácilmente qué estrategias de participación han tenido un mayor impacto en sus métricas clave. Tanto para las campañas como para los lienzos, puede exportar los datos y guardar el informe para consultarlo en el futuro.

Para obtener más información sobre los usos de los informes y análisis en Braze, consulte la [descripción general de los informes]({{site.baseurl}}/user_guide/analytics/reporting/reports_overview/).

{% endapi %}
