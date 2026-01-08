---
nav_title: Crear un Canvas
article_title: Crear un Canvas
page_order: 0
page_type: reference
description: "Este artículo de referencia cubre los pasos necesarios para crear, mantener y probar un Canvas."
tool: Canvas
search_rank: 1
---

# Crear un Canvas

> Este artículo de referencia cubre los pasos necesarios para crear, mantener y probar un Canvas. Sigue esta guía o consulta nuestro [curso de Braze Learning en Canvas](https://learning.braze.com/quick-overview-canvas-setup).

{% details Original Canvas editor %}
Ya no puedes crear o duplicar Lienzos utilizando la experiencia original de Canvas. Braze recomienda [clonar tus Lienzos]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/) al editor más actual.
{% enddetails %}

## Crear un Canvas

### Paso 1: Configurar un nuevo Canvas 

Primero, ve a **Mensajería** > **Canvas** y, a continuación, selecciona **Crear Canvas**.

El constructor de Canvas te guiará paso a paso en la configuración de tu Canvas, desde ponerle nombre hasta configurar eventos de conversión y atraer a los usuarios adecuados a tu recorrido del cliente. Selecciona cada una de las pestañas siguientes para ver qué configuraciones puedes ajustar para cada paso de la construcción.

{% tabs local %}
  {% tab Basics %}
    Aquí configurarás los aspectos básicos de tu Canvas:
    \- Ponle nombre a tu Canvas
    \- Añadir equipos
    \- Añadir etiquetas
    \- Asigna eventos de conversión, y elige sus tipos de evento y fechas límite

    Learn more about the [Basics step](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab Entry Schedule %}
    Aquí decidirás cómo y cuándo entrarán tus usuarios en tu Canvas:
    \- Programado: Se trata de una entrada en Canvas basada en el tiempo
    \- Basado en la acción: Tu usuario entrará en tu Canvas después de realizar una acción definida
    \- Desencadenado por la API: Utiliza una solicitud API para introducir usuarios en tu Canvas

    Learn more about the [Entry Schedule step](#step-2b-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Target Audience %}
    Aquí seleccionarás tu audiencia objetivo:
    \- Crea tu audiencia añadiendo segmentos y filtros
    \- Ajusta los límites de entrada y reentrada en Canvas
    \- Ver un resumen de tu audiencia objetivo

    Learn more about the [Target Audience step](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab Send Settings %}
    Aquí seleccionarás tu configuración de envío de Canvas:
    \- Selecciona tu configuración de suscripción
    \- Establece un límite de velocidad de envío para tus mensajes de Canvas
    \- Habilitar y configurar horas tranquilas

    Learn more about the [Send Settings step](#step-2d-select-your-send-settings).
  {% endtab %}
  {% tab Build Canvas %}
    Aquí construirás tu Canvas.

    Learn how to [build your Canvas](#step-3-build-your-canvas) using the Canvas builder.
  {% endtab %}
  {% tab Summary %}
    Aquí encontrarás el resumen de tus datos de Canvas. Si tienes activado el [flujo de trabajo de aprobación del Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/), puedes aprobar los detalles del Canvas listados antes de lanzarlo.

  {% endtab %}
{% endtabs %}

#### Paso 1.1: Empieza con lo básico de Canvas

Aquí, darás nombre a tu Canvas, asignarás [Equipos]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams) y crearás o añadirás [Etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags). También puedes asignar eventos de conversión para el Canvas.

{% alert tip %}
Etiqueta tus Lienzos para que sea fácil encontrarlos y crear informes a partir de ellos. Por ejemplo, al utilizar [el Generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), puedes filtrar por etiquetas concretas.
{% endalert %}

\![La página de detalles del Canvas, con campos para el nombre, la descripción, la ubicación y las etiquetas del Canvas.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

##### Elige eventos de conversión

Elige el tipo de evento de conversión y, a continuación, selecciona las conversiones que quieres registrar. Estos [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) medirán la eficacia de tu Canvas. 

\![Evento de conversión primaria A con el tipo de evento de conversión Realiza una compra para registrar las conversaciones de los usuarios que realizan cualquier compra dentro de un plazo de conversión de tres días.]({% image_buster /assets/img/add_canvas_conversions.png %})

Si tu Canvas tiene múltiples variantes o un grupo de control, Braze utilizará este evento de conversión para determinar la mejor variante para alcanzar este objetivo de conversión. Utilizando la misma lógica, puedes crear varios eventos de conversión.

#### Paso 1.2: Determina tu horario de entrada en Canvas

Puedes elegir una de las tres formas en que los usuarios pueden entrar en tu Canvas. 

##### Tipos de horarios de entrada

{% tabs local %}
  {% tab Scheduled Delivery %}
    Con la entrega programada, los usuarios entrarán en un horario, de forma similar a como programarías una campaña. Puedes inscribir a los usuarios en un Canvas en cuanto se lance, introducirlos en su recorrido en algún momento en el futuro, o de forma recurrente (diaria, semanal o mensualmente). 

    In this example, based on the time-based options, users will enter this Canvas every Tuesday at 12 pm in their local time zone every week, beginning November 14, 2025 until December 31, 2025.

    ![The "Entry Schedule" page with the type set to "Scheduled". Due to the selection, time-based options are shown, including frequency, start time, recurrence, days, and more.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Action-Based Delivery %}
    Con la entrega basada en acciones, los usuarios entrarán en el Canvas y empezarán a recibir mensajes cuando realicen acciones concretas, como abrir tu aplicación, realizar una compra o desencadenar un evento personalizado.

    You can control other aspects of the Canvas behavior from the **Entry Audience** window, including rules for re-eligibility and frequency capping settings. Note that action-based delivery is unavailable for Canvas components with in-app messages.

    ![An example of action-based delivery. Users will enter the Canvas if they make a purchase with an entry window beginning at 1:30 pm on June 10, 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

  {% endtab %}
  {% tab API-Triggered Delivery %}
    Con la entrega desencadenada por la API, los usuarios entrarán en tu Canvas y empezarán a recibir mensajes después de haberse añadido mediante el [punto final`/canvas/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) a través de la API. En el panel, puedes encontrar un ejemplo de solicitud cURL que hace esto, así como asignar opcionales [`canvas_entry_properties`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) utilizando el [objeto de propiedades de entrada Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). 

    ![An example of API-triggered delivery with a Canvas ID and an example of a cURL request.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    You can use the following endpoints for API-triggered delivery:
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

Tras seleccionar tu método de entrega, ajusta la configuración para que coincida con tu caso de uso, y luego continúa con la configuración de tu audiencia objetivo.

{% details Deduplicate behavior for Canvases using the original editor %}
En caso de que la ventana de reelegibilidad sea inferior a la duración máxima del Canvas, se permitirá a un usuario volver a entrar y recibir los mensajes de más de un componente. En el caso extremo de que la reentrada de un usuario llegue al mismo componente que su entrada anterior, Braze deduplicará los mensajes de ese componente. 

Si un usuario vuelve a entrar en el Canvas, llega al mismo componente que su entrada anterior y es elegible para recibir un mensaje dentro de la aplicación por cada entrada, el usuario recibirá el mensaje dos veces (dependiendo de la prioridad de los mensajes dentro de la aplicación) siempre que vuelva a abrir una sesión dos veces.
{% enddetails %}

#### Paso 1.3: Configura tu audiencia objetivo de entrada

Sólo los usuarios que coincidan con tus criterios definidos pueden entrar en el recorrido en el paso en Canvas **Audiencia objetivo**, lo que significa que Braze evalúa primero la elegibilidad de la audiencia objetivo **antes de** que los usuarios entren en el recorrido en Canvas. Por ejemplo, si quieres dirigirte a nuevos usuarios, puedes seleccionar un segmento de usuarios que utilizaron tu aplicación por primera vez hace menos de una semana.

En **Controles de entrada**, puedes limitar el número de usuarios cada vez que se programe la ejecución del Canvas. Para los Lienzos basados en acciones y desencadenantes de API, este límite se produce a cada hora UTC. 

{% alert important %}
Evita configurar una campaña basada en acciones o Canvas con el mismo desencadenante que el filtro de audiencia (como un atributo modificado o la realización de un evento personalizado). Puede darse una [condición de carrera]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions) en la que el usuario no esté en la audiencia en el momento de realizar el evento desencadenante, lo que significa que no recibirá la campaña ni entrará en el Canvas.
{% endalert %}

##### Pon a prueba a tu audiencia

Después de añadir segmentos y filtros a tu audiencia objetivo, puedes probar si tu audiencia está configurada como esperabas [buscando a un usuario]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) para confirmar si coincide con los criterios de audiencia.

\![El campo "Búsqueda de usuarios", que te permite buscar por ID externo de usuario o ID de Braze.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:100%;"}{: style="max-width:80%;"}

##### Seleccionar controles de entrada

Los controles de entrada determinan si se permite a los usuarios volver a entrar en un Canvas. También puedes limitar el número de personas que potencialmente entrarían en este Canvas según una cadencia seleccionada (diariamente, durante toda la vida del Canvas o cada vez que se programe el Canvas). 

Por ejemplo, si seleccionas **Limitar volumen de entradas** y estableces el campo **Entradas máximas** en 5.000 usuarios con **Diariamente** como cadencia límite, entonces el Canvas sólo enviará a 5.000 usuarios al día.

La página "Controles de entrada" muestra las casillas de verificación "Permitir a los usuarios volver a entrar en Canvas" y "Limitar el volumen de entrada". Esto último te permite establecer el máximo de entradas y si quieres limitar diariamente, durante toda la vida del Canvas, o cada vez que se programe el Canvas.]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Braze no recomienda utilizar la característica **Cada vez que se programa el Canvas** para el calentamiento de IP, ya que puede provocar un aumento del volumen de envíos.
{% endalert %}

##### Configuración de los criterios de salida

La configuración de los [criterios de salida]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) determina qué usuarios quieres que salgan de un Canvas. Si un usuario realiza el evento de excepción o coincide con los segmentos y filtros, no recibirá más mensajes.

##### Cálculo de la población objetivo

En la sección **Población objetivo**, puedes ver un resumen de tu audiencia, como los segmentos seleccionados y los filtros adicionales, y un desglose de cuántos usuarios son alcanzables por canal de mensajería. Para calcular el número exacto de usuarios alcanzables de tu audiencia objetivo en lugar de la estimación predeterminada, selecciona [Calcular estadísticas exactas]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics).

Toma nota:

- Calcular las estadísticas exactas puede llevar unos minutos de ejecución. Esta función sólo calcula las estadísticas exactas a nivel de segmento, no a nivel de filtro o grupo de filtros.
- En los segmentos grandes, es normal que se produzcan ligeras variaciones incluso al calcular las estadísticas exactas. Se espera que la precisión de esta característica sea del 99,999% o superior.

Para ver estadísticas adicionales, como los ingresos medios durante la vida útil de los usuarios objetivo, selecciona **Mostrar estadísticas adicionales**.

Desglose de la población objetivo con opción de calcular estadísticas exactas.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

##### Por qué el recuento de la audiencia objetivo puede diferir del recuento de usuarios alcanzables

{% multi_lang_include segments.md section='Differing audience size' %}

#### Paso 1.4: Selecciona tu configuración de envío

Selecciona **Configuración de envío** para editar la configuración de tu suscripción, activar el límite de tasa y activar las horas tranquilas. Activando [la limitación de tasa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-canvas-components) o la [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping), puedes aliviar la presión de marketing sobre tus usuarios y asegurarte de que no les envías demasiados mensajes.

Para los Canvas dirigidos a canales de correo electrónico y push, puede que quieras limitar tu Canvas para que sólo reciban el mensaje los usuarios que hayan optado explícitamente por ello (excluyendo a los usuarios suscritos o dados de baja). Por ejemplo, supongamos que tienes tres usuarios con diferentes estados de adhesión voluntaria:

- **El usuario A** está suscrito al correo electrónico y está habilitado para push. Este usuario no recibe el correo electrónico pero recibirá el push.
- **El usuario B** tiene la adhesión voluntaria al correo electrónico, pero no está habilitado para push. Este usuario recibirá el correo electrónico pero no recibe el push.
- **El usuario C** ha optado por la adhesión voluntaria al correo electrónico y está habilitado para push. Este usuario recibirá tanto el correo electrónico como el push.

Para ello, configura la **Configuración de suscripción** para enviar este Canvas "sólo a usuarios con adhesión voluntaria". Esta opción garantizará que sólo los usuarios con adhesión voluntaria reciban tu correo electrónico, y Braze sólo enviará tu push a los usuarios que estén habilitados para push de forma predeterminada. 

Estas configuraciones de suscripción se aplican paso a paso, lo que significa que no afectan a la audiencia de entrada. Así, esta configuración se utiliza para evaluar si un usuario es elegible para recibir cada paso en Canvas.

{% alert important %}
Con esta configuración, no incluyas ningún filtro en el paso **Audiencia objetivo** que limite la audiencia a un único canal (por ejemplo, `Foreground Push Enabled = True` o `Email Subscription = Opted-In`).
{% endalert %}

Si lo deseas, especifica Horas tranquilas (el tiempo durante el cual no se enviarán tus mensajes) para tu Canvas. Marca **Habilitar horas tranquilas** en tu **configuración de envío**. A continuación, selecciona tus Horas Tranquilas en la hora local de tu usuario y qué acción seguirá si el mensaje se desencadena dentro de esas Horas Tranquilas.

La página "Horas tranquilas" muestra una casilla de verificación para habilitar las horas tranquilas. Si se habilita, se puede establecer la hora de inicio, la hora de finalización y el comportamiento de alternativa.]({% image_buster /assets/img/quiet_hours.png %})

### Paso 2: Construye tu Canvas

{% alert tip %}
¡Ahorra tiempo y agiliza tu creación de Canvas utilizando [las plantillas Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/#available-braze-templates)! Navega por nuestra biblioteca de plantillas prediseñadas para encontrar una que se adapte a tu caso de uso y personalízala para satisfacer tus necesidades específicas.
{% endalert %}

#### Paso 2.1: Añadir una variante

\![El botón "Añadir variante" seleccionado para mostrar un menú contextual con la opción "Añadir variante".]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

Selecciona **Añadir variante** y añade una nueva variante a tu Canvas. Las variantes representan un viaje que realizarán tus usuarios y pueden contener múltiples pasos y ramificaciones.

Puedes añadir variantes adicionales seleccionando el botón <i class="fas fa-plus-circle"></i> más. Cuando añadas nuevas variantes, podrás ajustar cómo se distribuirán tus usuarios entre ellas para que puedas comparar y analizar la eficacia de las distintas estrategias de interacción.

\![Dos variantes de ejemplo en un Canvas de Braze.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
Por defecto, la asignación de variantes en Canvas se bloquea cuando los usuarios entran en el Canvas, lo que significa que si un usuario introduce por primera vez una variante, ésa será su variante cada vez que vuelva a entrar en el Canvas. Sin embargo, hay formas de eludir este comportamiento. <br><br>Para ello, puedes crear un generador de números aleatorios utilizando Liquid, ejecutarlo al principio de la entrada de cada usuario en Canvas, almacenar el valor como un atributo personalizado y, a continuación, utilizar ese atributo para dividir aleatoriamente a los usuarios.

{% details Expand for steps %}

1. Crea un atributo personalizado para almacenar tu número aleatorio. Ponle un nombre fácil de localizar, como "lottery_number" o "random_assignment".. Puedes crear el atributo [en tu panel]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) o mediante llamadas a la API a nuestro [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).<br><br>
2. Crea una campaña webhook al principio de tu Canvas. Esta campaña será el medio en el que crees tu número aleatorio y lo almacenes como atributo personalizado. Para más información, consulta [Crear un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook). Establece la URL de nuestro punto final `/users/track`.<br><br>
3. Crea el generador de números aleatorios. Puedes hacerlo con el código que [se indica aquí](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486), que aprovecha la hora única de entrada de cada usuario para crear un número aleatorio. Establece el número resultante como una variable Liquid dentro de tu campaña webhook.<br><br>
4. Da formato a la llamada `/users/track` de tu campaña webhook para que establezca el atributo personalizado que creaste en el paso 1 en el número aleatorio que has generado en el perfil de tu usuario actual. Cuando se ejecute este paso, habrás conseguido crear un número aleatorio que cambia cada vez que un usuario entra en tu campaña.<br><br>
5. Ajusta las ramas de tu Canvas para que, en lugar de estar divididas por variantes elegidas al azar, lo estén en función de las reglas de la audiencia. En las reglas de audiencia de cada rama, establece el filtro de audiencia según tu atributo personalizado. <br><br>Por ejemplo, una rama puede tener "lottery_number es menor de 3" como filtro de audiencia, mientras que otra rama puede tener "lottery_number es mayor de 3 y menor de 6" como filtro de audiencia.

{% enddetails %}
{% endalert %}

#### Paso 2.2: Añadir pasos en Canvas

Puedes añadir más pasos a tu flujo de trabajo Canvas arrastrando y soltando componentes desde la barra lateral **Componentes**. O bien, selecciona el botón más <i class="fas fa-plus-circle"></i> para añadir un componente con el menú emergente.

{% alert tip %}
Cuando empieces a añadir más pasos, puedes cambiar el nivel de zoom para centrarte en los detalles o abarcar todo el recorrido del usuario. Amplía con <kbd>Mayúsculas</kbd> + <kbd>+</kbd> o reduce con <kbd>Mayúsculas</kbd> + <kbd>-</kbd>.
{% endalert %}

La ventana de búsqueda de componentes añade un paso en Canvas de Braze.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
Puedes añadir hasta 200 pasos en un Canvas. Si tu Canvas supera los 200 pasos, pueden producirse problemas de carga.
{% endalert %}

##### Duración máxima

A medida que tu recorrido en Canvas aumenta en pasos, la duración máxima es el mayor tiempo posible que un usuario puede tardar en completar este Canvas. Se calcula sumando los retrasos y las ventanas de desencadenamiento de cada paso de cada variante para el camino más largo. Por ejemplo, si tu Canvas tiene un paso de Retraso con un retraso de 3 días y un paso de Mensaje, la duración máxima de tu Canvas será de 3 días.

##### Editar un paso

¿Quieres editar un paso de tu recorrido de usuario? ¡Comprueba cómo hacerlo en función de tu flujo de trabajo en Canvas!

Puedes editar cualquier paso de tu flujo de trabajo Canvas seleccionando cualquiera de los componentes. Por ejemplo, supongamos que quieres editar tu primer paso, un componente [Retraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), en tu flujo de trabajo a un día concreto. Selecciona el paso para ver su configuración y ajusta tu retraso al 1 de marzo. Esto significa que el 1 de marzo tus usuarios pasarán al siguiente paso en tu Canvas.

\![Un ejemplo de paso "Retraso" con el retraso ajustado a "Hasta un día concreto".]({% image_buster /assets/img_archive/edit_delay_flow.png %})

O puedes editar y ajustar rápidamente la **Configuración de Acción** de tu paso [Rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) para retener a los usuarios durante un periodo de tiempo. Esto prioriza su próxima trayectoria basándose en las acciones realizadas durante este periodo de evaluación.

\![El segundo paso en Canvas, "Configuración de la acción", con una ventana de evaluación fijada en 1 día.]({% image_buster /assets/img_archive/action_paths_flow.png %})

Los componentes ligeros de Canvas permiten una experiencia de edición sencilla, por lo que ajustar los detalles más sutiles de tu Canvas es más fácil. 

##### Mensajes en Canvas

Edita los mensajes de un componente Canvas para controlar los mensajes que enviará un paso concreto. Canvas puede enviar mensajes por correo electrónico, móvil y push web, y webhooks para integrarse con otros sistemas. De forma similar a las campañas, puedes utilizar determinadas plantillas [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) para personalizar tus mensajes.

{% alert tip %}
¿Sabías que puedes incluir nombres de componentes de Canvas en tus mensajes y plantillas de enlaces?<br>
Utiliza la etiqueta de Liquid `campaign.${name}` en Canvas para mostrar el nombre del componente actual de Canvas.
{% endalert %}

El componente Mensajes gestiona los mensajes enviados a los usuarios. Puedes seleccionar tus **canales de mensajería** y ajustar **la configuración de entrega** para optimizar tu mensajería en Canvas. Para más detalles sobre este componente, consulta [Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

\![El paso "Configurar mensajes", con la opción "Canales de mensajería" seleccionada, que muestra la lista de canales de mensajería disponibles, como push de Android, tarjetas de contenido, correo electrónico, etc.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Selecciona **Hecho** cuando hayas terminado de configurar tu componente Canvas.

{% tabs local %}
{% tab Canvas Entry Properties %}

Los `canvas_entry_properties` se configuran en el paso Horario de entrada de la creación de un Canvas e indican el desencadenante que introduce a un usuario en un Canvas. Estas propiedades también pueden acceder a las propiedades de las cargas útiles de entrada en los Lienzos desencadenados por la API. Nota que el objeto `canvas_entry_properties` puede ser de hasta 50 KB. 

Utiliza el siguiente Liquid cuando hagas referencia a estas propiedades de entrada: {% raw %} ``canvas_entry_properties.${property_name}`` {% endraw %}. Ten en cuenta que los eventos deben ser eventos personalizados o eventos de compra para poder utilizarlos de esta forma.

{% raw %}
Por ejemplo, considera la siguiente petición: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Podrías añadir la palabra "zapatos" a un mensaje con este Liquid ``{{canvas_entry_properties.${product_name}}}``.
{% endraw %}

{% endtab %}

{% tab Event Properties %}
Las propiedades del evento son las propiedades establecidas por ti en eventos personalizados y compras. Estos `event_properties` pueden utilizarse tanto en campañas con entrega basada en acciones como en Lienzos. 

En Canvas, las propiedades del evento personalizado y del evento de compra pueden utilizarse en Liquid en cualquier paso de Mensaje que siga a un paso de Ruta de acción. Utiliza este Liquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} cuando hagas referencia a estos `event_properties`. Estos eventos deben ser eventos personalizados o eventos de compra para poder utilizarlos de esta forma en el componente Mensaje.

En el primer paso de Mensaje que sigue a una Ruta de acción, puedes utilizar `event_properties` relacionado con el evento al que se hace referencia en esa Ruta de acción. Puedes tener otros pasos (que no sean otras Rutas de Acción o pasos de Mensaje) entre este paso de Rutas de Acción y el paso de Mensaje. Ten en cuenta que sólo tendrás acceso a `event_properties` si tu paso Mensaje puede remontarse a una ruta que no sea Todos los demás en un paso Ruta de acción

{% endtab %}
{% endtabs %}

#### Paso 2.3: Editar conexiones

Para mover una conexión entre pasos, selecciona la flecha que conecta los dos componentes y selecciona un componente diferente. Para eliminar la conexión, selecciona la flecha seguida de **Cancelar conexión** en el pie de página del compositor de Canvas.

### Paso 3: Añadir un grupo de control

Puedes añadir un grupo de control a tu Canvas seleccionando el botón <i class="fas fa-plus-circle"></i> más para añadir una nueva variante. 

Braze hará un seguimiento de las conversiones de los usuarios que se coloquen en el grupo de control, aunque no recibirán ningún mensaje. Para preservar la precisión de la prueba, haremos un seguimiento del número de conversiones de tus variantes y del grupo de control durante exactamente el mismo tiempo, como se muestra en la pantalla de selección del evento de conversión. 

Puedes ajustar la distribución entre tus mensajes haciendo doble clic en las cabeceras de **Nombre de variante**.

En este ejemplo, tenemos nuestro Canvas dividido en dos variantes. La variante 1 tiene el 70% de los usuarios. La segunda variante es un grupo de control con el 30% restante de usuarios.

\![Una variante de ejemplo en un Canvas de Braze, donde el 70% va a la "Variante 1", que se retrasa 1 día en el primer paso, y luego envía un mensaje en el segundo paso. El otro 30% va a un "Control" que no tiene ningún paso de seguimiento.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

#### Intelligent Selection para Canvas

Las funciones de Intelligent Selection están ahora disponibles en los Lienzos multivariantes. De forma similar a la característica Intelligent [Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) para Campañas multivariantes, Intelligent Selection para Canvas analiza el rendimiento de cada variante de Canvas y ajusta el porcentaje de usuarios que se embudan a través de cada variante. Esta distribución se basa en las métricas de rendimiento de cada variante para maximizar el número total esperado de conversiones.

Ten en cuenta que los lienzos multivariantes no sólo te permiten probar el texto, sino también el momento y los canales. Mediante la Intelligent Selection, puedes probar Canvas de forma más eficaz y confiar en que tus usuarios realizarán el mejor recorrido posible por Canvas.

La opción "Intelligent Selection" está habilitada en la página "Editar distribución de variantes". A medida que analiza y optimiza el Canvas, muestra una barra horizontal a través de la página dividida en varias secciones, cada una de las cuales varía en color y tamaño. Esto es sólo una representación visual y no se correlaciona con ningún análisis específico.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

Intelligent Selection para Canvas optimiza tus resultados en Canvas realizando ajustes graduales en tiempo real de la distribución de usuarios clasificados en cada variante. Cuando el algoritmo estadístico determine un ganador decisivo entre tus variantes, descartará las variantes de menor rendimiento y clasificará a todos los futuros destinatarios elegibles del Canvas en las Variantes Ganadoras. 

Por esta razón, Intelligent Selection funciona mejor en Lienzos en los que entran nuevos usuarios con frecuencia.

### Paso 4: Guardar e iniciar

Cuando hayas terminado de crear tu Canvas, selecciona **Lanzar Canvas** para guardarlo y lanzarlo. Una vez que hayas lanzado tu Canvas, podrás ver los análisis de tu recorrido a medida que vayan llegando en la página **Detalles del Canvas**. 

También puedes guardar tu Canvas como borrador si necesitas volver a él.

\![Un ejemplo de Canvas en Braze.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
¿Necesitas editar tu Canvas después del lanzamiento? ¡Pues sí que puedes! Consulta [Editar lienzos después del lanzamiento]({{site.baseurl}}/post-launch_edits/) para obtener más información.
{% endalert %}

