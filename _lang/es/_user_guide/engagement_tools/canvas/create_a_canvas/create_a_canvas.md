---
nav_title: Crear un lienzo
article_title: Crear un lienzo
page_order: 0
page_type: reference
description: "En este artículo de referencia se cubren los pasos necesarios para crear, mantener y probar un Canvas."
tool: Canvas
search_rank: 1
---

# Crear un lienzo

> En este artículo de referencia se cubren los pasos necesarios para crear, mantener y probar un Canvas. Sigue esta guía o consulta nuestro [curso de Braze Learning en Canvas](https://learning.braze.com/quick-overview-canvas-setup).

{% details Editor de lienzos original %}
Ya no puedes crear o duplicar Lienzos utilizando la experiencia original de Canvas. Braze recomienda [clonar tus Lienzos en Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% enddetails %}

## Crear un lienzo

### Paso 1: Configurar un nuevo Canvas 

Primero, ve a **Mensajería** > **Canvas** y, a continuación, selecciona **Crear Canvas**.

El Canvas Builder le guiará paso a paso en la configuración de su Canvas, desde la asignación de un nombre hasta la configuración de eventos de conversión y la introducción de los usuarios adecuados en el recorrido del cliente. Seleccione cada una de las pestañas siguientes para ver los ajustes que puede realizar en cada paso de la construcción.

{% tabs local %}
  {% tab Conceptos básicos %}
    Aquí configurarás los aspectos básicos de tu Canvas:
    \- Ponga nombre a su lienzo
    \- Añadir equipos
    \- Añadir etiquetas
    \- Asignar eventos de conversión, y elegir sus tipos de evento y fechas límite

    Learn more about the [Basics step](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab Horario de entrada %}
    Aquí decidirás cómo entrarán tus usuarios en tu Canvas:
    \- Programado: Se trata de una entrada en Canvas basada en el tiempo
    \- Basado en la acción: Tu usuario entrará en tu Canvas después de realizar una acción definida
    \- Activado por API: Utiliza una solicitud API para introducir usuarios en tu Canvas

    Learn more about the [Entry Schedule step](#step-2b-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Audiencia objetivo %}
    Aquí seleccionará su público objetivo:
    \- Crea tu audiencia añadiendo segmentos y filtros
    \- Ajustar los límites de entrada y reentrada en el lienzo
    \- Ver un resumen de tu audiencia objetivo

    Learn more about the [Target Audience step](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab Configuración de envío %}
    Aquí seleccionarás tu configuración de envío de Canvas:
    \- Selecciona tu configuración de suscripción
    \- Establece un límite de velocidad de envío para tus mensajes Canvas
    \- Activar y configurar las horas de silencio

    Learn more about the [Send Settings step](#step-2d-select-your-send-settings).
  {% endtab %}
  {% tab Crear Canvas %}
    Aquí construirás tu Canvas.

    Learn how to [build your Canvas](#step-3-build-your-canvas) using the Canvas builder.
  {% endtab %}
  {% tab Resumen %}
    Aquí encontrarás el resumen de los datos de tu Canvas. Si tienes activado el [flujo de trabajo de aprobación de Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/), puedes aprobar los detalles de Canvas listados antes de lanzarlo.

  {% endtab %}
{% endtabs %}

#### Paso 1.1: Empieza con lo básico de Canvas

Aquí, nombrará su Lienzo, asignará [Equipos]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams) y creará o añadirá [Etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags). También puede asignar eventos de conversión para el lienzo.

{% alert tip %}
Etiqueta tus lienzos para que sea fácil encontrarlos y crear informes a partir de ellos. Por ejemplo, al utilizar [el Generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), puede filtrar por determinadas etiquetas.
{% endalert %}

![La página de detalles del Canvas, con campos para el nombre, descripción, ubicación y etiquetas del Canvas.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

##### Elegir eventos de conversión

Elija el tipo de evento de conversión y, a continuación, seleccione las conversiones que desea registrar. Estos [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) medirán la eficacia de tu Canvas. 

![Evento de conversión primaria A con el tipo de evento de conversión Realiza una compra para registrar las conversaciones de los usuarios que realizan cualquier compra dentro de un plazo de conversión de tres días.]({% image_buster /assets/img/add_canvas_conversions.png %})

Si su Canvas tiene múltiples variantes o un grupo de control, Braze utilizará este evento de conversión para determinar la mejor variación para alcanzar este objetivo de conversión. Utilizando la misma lógica, puede crear varios eventos de conversión.

#### Paso 1.2: Determina tu horario de entrada en Canvas

Puedes elegir una de las tres formas en que los usuarios pueden entrar en tu Canvas. 

##### Tipos de horarios de entrada

{% tabs local %}
  {% tab Entrega programada %}
    Con la entrega programada, los usuarios entrarán en un horario, de forma similar a como se programaría una campaña. Puede inscribir a los usuarios en un Canvas en cuanto se lance, introducirlos en su recorrido en algún momento en el futuro o de forma recurrente (diaria, semanal o mensualmente). 

    In this example, based on the time-based options, users will enter this Canvas every Tuesday at 12 pm in their local time zone every week, beginning November 14, 2025 until December 31, 2025.

    ![The "Entry Schedule" page with the type set to "Scheduled". Due to the selection, time-based options are shown, including frequency, start time, recurrence, days, and more.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Ejecución basada en la acción %}
    Con la entrega basada en acciones, los usuarios entrarán en el Canvas y empezarán a recibir mensajes cuando realicen determinadas acciones, como abrir tu aplicación, realizar una compra o activar un evento personalizado.

    You can control other aspects of the Canvas behavior from the **Entry Audience** window, including rules for re-eligibility and frequency capping settings. Note that action-based delivery is unavailable for Canvas components with in-app messages.

    ![An example of action-based delivery. Users will enter the Canvas if they make a purchase with an entry window beginning at 1:30 pm on June 10, 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

  {% endtab %}
  {% tab Entrega activada por API %}
    Con la entrega activada por la API, los usuarios entrarán en tu Canvas y comenzarán a recibir mensajes después de que se hayan añadido utilizando el [punto final`/canvas/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) a través de la API. En el dashboard, puedes encontrar un ejemplo de petición cURL que hace esto así como asignar opcionales [`canvas_entry_properties`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) utilizando el [objeto de propiedades de entrada Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). 

    ![An example of API-triggered delivery with a Canvas ID and an example of a cURL request.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    You can use the following endpoints for API-triggered delivery:
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

Tras seleccionar tu método de entrega, ajusta la configuración para que coincida con tu caso de uso, y luego continúa con la configuración de tu audiencia objetivo.

{% details Comportamiento de deduplicación para los lienzos que utilizan el editor original %}
En caso de que la ventana de reelegibilidad sea inferior a la duración máxima del Canvas, se permitirá a un usuario volver a entrar y recibir los mensajes de más de un componente. En el caso extremo de que la reentrada de un usuario llegue al mismo componente que su entrada anterior, Braze deduplicará los mensajes de ese componente. 

Si un usuario vuelve a entrar en el Canvas, llega al mismo componente que su entrada anterior y puede recibir un mensaje in-app por cada entrada, el usuario recibirá el mensaje dos veces (dependiendo de la prioridad de los mensajes in-app) siempre que vuelva a abrir una sesión dos veces.
{% enddetails %}

#### Paso 1.3: Configura tu audiencia objetivo de entrada

Puede establecer el público objetivo de su lienzo en el paso **Público objetivo**. Sólo los usuarios que cumplen los criterios definidos pueden entrar en el recorrido, lo que significa que Braze evalúa primero la elegibilidad del público objetivo antes de que los usuarios entren en el recorrido de Canvas. Por ejemplo, si desea dirigirse a nuevos usuarios, puede seleccionar un segmento de usuarios que utilizaron su aplicación por primera vez hace menos de una semana.

En **Controles de entrada**, puede limitar el número de usuarios cada vez que se programe la ejecución del lienzo. Para los Canvas basados en acciones y desencadenantes de API, este límite se produce a cada hora UTC. 

{% alert warning %}
Evite configurar una campaña basada en acciones o Canvas con el mismo desencadenante que el filtro de audiencia (como un atributo modificado o la realización de un evento personalizado). Puede producirse una condición de carrera en la que el usuario no se encuentre entre el público en el momento de realizar el evento desencadenante, lo que significa que no recibirá la campaña ni entrará en el Canvas.  
{% endalert %}

##### Prueba tu audiencia

Después de añadir segmentos y filtros a su público objetivo, puede comprobar si su público está configurado según lo esperado [buscando un usuario]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) para confirmar si coincide con los criterios del público.

![El campo "Búsqueda de usuarios", que te permite buscar por ID de usuario externo o ID de Braze.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:100%;"}{: style="max-width:80%;"}

##### Seleccionar controles de entrada

Los controles de entrada determinan si se permite a los usuarios volver a entrar en un lienzo. También puedes limitar el número de personas que potencialmente entrarían en este Canvas según una cadencia seleccionada (diariamente, durante toda la vida del Canvas o cada vez que se programe el Canvas). 

Por ejemplo, si seleccionas **Limitar volumen de entradas** y estableces el campo **Entradas máximas** en 5.000 usuarios con **Diariamente** como cadencia límite, entonces el Canvas sólo enviará a 5.000 usuarios al día.

![La página "Controles de entrada" muestra las casillas de verificación "Permitir a los usuarios volver a entrar en Canvas" y "Limitar el volumen de entrada". Esto último te permite establecer el máximo de entradas y si quieres limitar diariamente, durante toda la vida del Canvas, o cada vez que se programe el Canvas.]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Braze no recomienda utilizar la característica **Cada vez que se programa el Canvas** para el calentamiento de IP, ya que puede provocar un aumento del volumen de envíos.
{% endalert %}

##### Establecer criterios de salida

La configuración de los [criterios de salida]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) determina qué usuarios desea que salgan de un lienzo. Si un usuario realiza el evento de excepción o coincide con los segmentos y filtros, no recibirá más mensajes.

##### Cálculo de la población objetivo

En la sección **Población objetivo**, puedes ver un resumen de tu audiencia, como los segmentos seleccionados y los filtros adicionales, y un desglose de cuántos usuarios son alcanzables por canal de mensajería. Para calcular el número exacto de usuarios alcanzables de tu audiencia objetivo en lugar de la estimación predeterminada, selecciona [Calcular estadísticas exactas]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics).

Toma nota:

- Calcular las estadísticas exactas puede llevar unos minutos. Esta función sólo calcula las estadísticas exactas a nivel de segmento, no a nivel de filtro o grupo de filtros.
- En el caso de segmentos grandes, es normal que se produzcan ligeras variaciones incluso cuando se calculan estadísticas exactas. Se espera que la precisión de esta característica sea del 99,999 % o superior.

Para ver estadísticas adicionales, como los ingresos medios durante la vida útil de los usuarios objetivo, selecciona **Mostrar estadísticas adicionales**.

![Desglose de la población objetivo con opción de calcular estadísticas exactas.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

##### Por qué el recuento de la audiencia objetivo puede diferir del recuento de usuarios alcanzables

{% multi_lang_include segments.md section='Diferentes tamaños de audiencia' %}

#### Paso 1.4: Selecciona tu configuración de envío

Seleccione **Configuración de envío** para editar los ajustes de suscripción, activar la limitación de velocidad y activar las horas de silencio. Activando [la limitación de tasa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-canvas-components) o la [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping), puedes aliviar la presión de marketing sobre tus usuarios y asegurarte de que no les envías demasiados mensajes.

En el caso de los lienzos dirigidos a los canales de correo electrónico y push, es posible que desee limitar su lienzo para que sólo los usuarios que hayan optado explícitamente por recibir el mensaje (excluyendo a los usuarios suscritos o dados de baja). Por ejemplo, supongamos que tiene tres usuarios con diferentes estados de suscripción:

- **El usuario A** está suscrito al correo electrónico y tiene activada la función push. Este usuario no recibe el correo electrónico pero recibirá el push.
- **El usuario B** tiene la adhesión voluntaria al correo electrónico, pero no está habilitado para push. Este usuario recibirá el email pero no recibirá el push.
- **El usuario C** ha optado por la adhesión voluntaria al correo electrónico y está habilitado para push. Este usuario recibirá tanto el correo electrónico como el push.

Para ello, configure **los Ajustes de suscripción** para enviar este lienzo "sólo a los usuarios que hayan dado su consentimiento". Esta opción garantizará que sólo los usuarios que hayan optado por recibirla reciban su correo electrónico, y Braze sólo enviará su push a los usuarios que estén habilitados para push de forma predeterminada. 

Estos ajustes de suscripción se aplican en cada paso, lo que significa que no hay ningún efecto sobre el público de entrada. Por lo tanto, esta configuración se utiliza para evaluar la elegibilidad de un usuario para recibir cada paso de Canvas.

{% alert important %}
Con esta configuración, no incluyas ningún filtro en el paso **Audiencia objetivo** que limite la audiencia a un único canal (por ejemplo, `Push Enabled = True` o `Email Subscription = Opted-In`).
{% endalert %}

Si lo desea, especifique Horas de silencio (el tiempo durante el cual no se enviarán sus mensajes) para su Lienzo. Marque **Activar horas de silencio** en la **Configuración de envío**. A continuación, seleccione sus Horas de Silencio en la hora local de su usuario y la acción que seguirá si el mensaje se activa dentro de esas Horas de Silencio.

![La página "Horas tranquilas" muestra una casilla para habilitar las horas tranquilas. Si se habilita, se puede establecer la hora de inicio, la hora de finalización y el comportamiento de alternativa.]({% image_buster /assets/img/quiet_hours.png %})

### Paso 2: Construye tu Canvas

{% alert tip %}
¡Ahorra tiempo y agiliza tu creación de Canvas utilizando [las plantillas de Braze]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/#available-braze-templates) Canvas! Navega por nuestra biblioteca de plantillas prediseñadas para encontrar una que se adapte a tu caso de uso y personalízala para satisfacer tus necesidades específicas.
{% endalert %}

#### Paso 2.1: Añadir una variante

![Selecciona el botón "Añadir variante" para mostrar un menú contextual con la opción "Añadir variante".]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

Seleccione **Añadir variante** y añada una nueva variante a su lienzo. Las variantes representan un viaje que realizarán sus usuarios y pueden contener múltiples pasos y ramificaciones.

Puede añadir variantes adicionales seleccionando el botón <i class="fas fa-plus-circle"></i> más. Cuando añada nuevas variantes, podrá ajustar cómo se distribuirán sus usuarios entre ellas para poder comparar y analizar la eficacia de las distintas estrategias de captación.

![Dos variantes de ejemplo en un Canvas de Braze.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
Por defecto, la asignación de variantes del lienzo se bloquea cuando los usuarios entran en el lienzo, lo que significa que si un usuario introduce por primera vez una variante, esa será su variante cada vez que vuelva a entrar en el lienzo. Sin embargo, hay formas de eludir este comportamiento. <br><br>Para ello, puede crear un generador de números aleatorios utilizando Liquid, ejecutarlo al principio de la entrada Canvas de cada usuario, almacenar el valor como un atributo personalizado y, a continuación, utilizar ese atributo para dividir aleatoriamente a los usuarios.

{% details Expandir por pasos %}

1. Crea un atributo personalizado para almacenar tu número aleatorio. Ponle un nombre fácil de localizar, como "número_lotería" o "asignación_aleatoria". Puedes crear el atributo [en tu panel]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) o a través de llamadas API a nuestro [punto final `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).<br><br>
2. Crea una campaña webhook al principio de tu Canvas. Esta campaña será el medio en el que creará su número aleatorio y lo almacenará como atributo personalizado. Consulte [Crear un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook) para obtener más información. Establezca la URL de nuestro punto final `/users/track`.<br><br>
3. Crea el generador de números aleatorios. Puedes hacerlo con el código que [se indica aquí](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486), que aprovecha la hora única de entrada de cada usuario para crear un número aleatorio. Establezca el número resultante como una variable Liquid dentro de su campaña webhook.<br><br>
4. Formatea la llamada `/users/track` en tu campaña webhook para que establezca el atributo personalizado que creaste en el paso 1 en el número aleatorio que has generado en el perfil de tu usuario actual. Cuando este paso se ejecute, habrá conseguido crear un número aleatorio que cambiará cada vez que un usuario entre en su campaña.<br><br>
5. Ajuste las ramas de su lienzo para que, en lugar de estar divididas por variantes elegidas al azar, se dividan en función de las reglas de audiencia. En las reglas de audiencia de cada rama, establezca el filtro de audiencia según su atributo personalizado. <br><br>Por ejemplo, una rama puede tener "número_lotería es menor que 3" como filtro de audiencia, mientras que otra rama puede tener "número_lotería es mayor que 3 y menor que 6" como filtro de audiencia.

{% enddetails %}
{% endalert %}

#### Paso 2.2: Añadir pasos en Canvas

Puede añadir más pasos a su flujo de trabajo Canvas arrastrando y soltando componentes desde la barra lateral **Componentes**. O bien, seleccione el botón más <i class="fas fa-plus-circle"></i> para añadir un componente con el menú desplegable.

{% alert tip %}
Cuando empiece a añadir más pasos, puede cambiar el nivel de zoom para centrarse en los detalles o abarcar todo el recorrido del usuario. Acércate con <kbd>Shift</kbd> + <kbd>+</kbd> o aléjate con <kbd>Shift</kbd> + <kbd>-</kbd>.
{% endalert %}

![La ventana de búsqueda de componentes añade un paso en Canvas de Braze.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert warning %}
Un lienzo creado con el flujo del lienzo puede contener hasta 200 pasos. Si su lienzo supera los 200 pasos, se producirán problemas de carga.
{% endalert %}

##### Duración máxima

A medida que el recorrido de tu Canvas aumenta en pasos, la duración máxima es el mayor tiempo posible que un usuario puede tardar en completar este Canvas. Se calcula sumando los retrasos y las ventanas de activación de cada paso de cada variante para el camino más largo. Por ejemplo, si su Canvas tiene un paso de Retraso con un retraso de 3 días y un paso de Mensaje, la duración máxima de tu Canvas será de 3 días.

##### Editar un paso

¿Quieres editar un paso de tu recorrido de usuario? Comprueba cómo hacerlo en función de tu flujo de trabajo en Canvas.

Puede editar cualquier paso de su flujo de trabajo Canvas Flow seleccionando cualquiera de los componentes. Por ejemplo, digamos que desea editar su primer paso, un componente de [Retraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), en su flujo de trabajo a un día específico. Selecciona el paso para ver su configuración y ajusta tu retraso al 1 de marzo. Esto significa que el 1 de marzo, tus usuarios pasarán al siguiente paso en tu Canvas.

![Un ejemplo de paso "Retraso" con el retraso ajustado a "Hasta un día concreto".]({% image_buster /assets/img_archive/edit_delay_flow.png %})

También puede editar y ajustar rápidamente la **Configuración de acción** de su paso [Rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) para retener a los usuarios durante un periodo de tiempo. Esto prioriza su próximo camino basado en las acciones durante este período de evaluación.

![El segundo paso en Canvas, "Configuración de la acción", con una ventana de evaluación fijada en 1 día.]({% image_buster /assets/img_archive/action_paths_flow.png %})

Los componentes ligeros de Canvas permiten una experiencia de edición sencilla, por lo que ajustar los detalles más sutiles de tu Canvas es más fácil. 

##### Mensajes en Canvas

Edite los mensajes de un componente del lienzo para controlar los mensajes que enviará un paso concreto. Canvas puede enviar mensajes push por correo electrónico, móvil y web, así como webhooks para integrarse con otros sistemas. De forma similar a las campañas, puede utilizar determinadas plantillas de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) para personalizar sus mensajes.

{% alert tip %}
¿Sabías que puedes incluir nombres de componentes de Canvas en tus mensajes y plantillas de enlaces?<br>
Utilice la etiqueta `campaign.${name}` Liquid en Canvas para mostrar el nombre del componente Canvas actual.
{% endalert %}

El componente Mensaje gestiona los mensajes enviados a los usuarios. Puedes seleccionar tus **canales de mensajería** y ajustar **la configuración de entrega** para optimizar tu mensajería en Canvas. Para más detalles sobre este componente, consulta [Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

![El paso "Configurar mensajes", con la opción "Canales de mensajería" seleccionada, que muestra la lista de canales de mensajería disponibles, como push de Android, tarjetas de contenido, correo electrónico, etc.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Seleccione **Hecho** cuando haya terminado de configurar su componente Canvas.

{% tabs local %}
{% tab Propiedades de entrada del lienzo %}

Las `canvas_entry_properties` se configuran en el paso Horario de entrada de la creación de un Canvas e indican el desencadenante que introduce a un usuario en un Canvas. Estas propiedades también pueden acceder a las propiedades de las cargas útiles de entrada en los lienzos activados por API. Nota que el objeto `canvas_entry_properties` puede ser de hasta 50 KB. 

Utilice el siguiente Líquido cuando haga referencia a estas propiedades de entrada: {% raw %} ``canvas_entry_properties.${property_name}`` {% endraw %}. Tenga en cuenta que los eventos deben ser eventos personalizados o eventos de compra para ser utilizados de esta manera.

{% raw %}
Por ejemplo, considere la siguiente petición: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Puede añadir la palabra "zapatos" a un mensaje con este líquido ``{{canvas_entry_properties.${product_name}}}``.
{% endraw %}

{% endtab %}

{% tab Propiedades de los eventos %}
Las propiedades de los eventos son las propiedades establecidas por usted en los eventos y compras personalizados. Estos `event_properties` se pueden utilizar en campañas con entrega basada en la acción, así como Lienzos. 

En el Flujo del lienzo, las propiedades de eventos personalizados y eventos de compra se pueden utilizar en Liquid en cualquier paso de Mensaje que siga a un paso de Rutas de acción. Utilice este líquido {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} cuando haga referencia a estos `event_properties`. Estos eventos deben ser eventos personalizados o eventos de compra para ser utilizados de esta forma en el componente Mensaje.

En el primer paso de Mensaje que sigue a una Ruta de Acción, puede utilizar `event_properties` relacionado con el evento al que se hace referencia en esa Ruta de Acción. Puede tener otros pasos (que no sean otro paso de Rutas de acción o Mensaje) entre este paso de Rutas de acción y el paso de Mensaje. Ten en cuenta que solo tendrás acceso a `event_properties` si tu paso de Mensaje puede remontarse a una ruta que no sea Todos los demás en un paso de Ruta de acción.

{% endtab %}
{% endtabs %}

#### Paso 2.3: Editar conexiones

Para mover una conexión entre pasos, seleccione la flecha que conecta los dos componentes y seleccione un componente diferente. Para eliminar la conexión, seleccione la flecha seguida de **Cancelar conexión** en el pie de página del compositor Canvas.

### Paso 3: Añadir un grupo de control

Puede añadir un grupo de control a su lienzo seleccionando el botón <i class="fas fa-plus-circle"></i> más para añadir una nueva variante. 

Braze realizará un seguimiento de las conversiones de los usuarios incluidos en el grupo de control, aunque no recibirán ningún mensaje. Para que la prueba sea precisa, realizaremos un seguimiento del número de conversiones de sus variantes y del grupo de control durante exactamente el mismo periodo de tiempo, como se muestra en la pantalla de selección del evento de conversión. 

Puede ajustar la distribución entre sus mensajes haciendo doble clic en las cabeceras de **los nombres de las variantes**.

En este ejemplo, tenemos nuestro Canvas dividido en dos variantes. La variante 1 cuenta con el 70% de los usuarios. La segunda variante es un grupo de control con el 30% restante de usuarios.

![Una variante de ejemplo en un Canvas de Braze, donde el 70% va a la "Variante 1", que retrasa 1 día el primer paso, y luego envía un mensaje en el segundo paso. El otro 30% va a un "Control" que no tiene ningún paso de seguimiento.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

#### Selección inteligente para Canvas

Las funciones de selección inteligente ya están disponibles en los lienzos multivariantes. De forma similar a la característica Intelligent [Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) para Campañas multivariantes, Intelligent Selection para Canvas analiza el rendimiento de cada variante de Canvas y ajusta el porcentaje de usuarios que se embudan a través de cada variante. Esta distribución se basa en las métricas de rendimiento de cada variante para maximizar el número total esperado de conversiones.

Tenga en cuenta que los lienzos multivariantes no sólo le permiten probar el texto, sino también el momento y los canales. Gracias a la selección inteligente, puede probar los lienzos de forma más eficaz y confiar en que sus usuarios realizarán el mejor recorrido posible por el lienzo.

![La opción "Intelligent Selection" está habilitada en la página "Editar distribución de variantes". A medida que analiza y optimiza el Canvas, muestra una barra horizontal a través de la página dividida en varias secciones, cada una de las cuales varía en color y tamaño. Esto es sólo una representación visual y no se correlaciona con ningún análisis específico.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

La Selección Inteligente para Canvas optimiza sus resultados de Canvas realizando ajustes graduales en tiempo real de la distribución de usuarios clasificados en cada variante. Cuando el algoritmo estadístico determine un ganador decisivo entre tus variantes, descartará las variantes de menor rendimiento y clasificará a todos los futuros destinatarios elegibles del Canvas en las Variantes Ganadoras. 

Por esta razón, la Selección Inteligente funciona mejor en Lienzos en los que entran nuevos usuarios con frecuencia.

### Paso 4: Guardar y lanzar

Cuando hayas terminado de crear tu Canvas, selecciona **Lanzar Canvas** para guardarlo y lanzarlo. Una vez que haya lanzado su lienzo, podrá ver los análisis de su trayecto a medida que vayan llegando en la página **de detalles del lienzo**. 

También puedes guardar tu lienzo como borrador por si necesitas volver a él.

![Un ejemplo de Canvas en Braze.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
¿Necesita modificar su lienzo después del lanzamiento? ¡Pues sí que puedes! Para más información, consulte [Editar lienzos después del lanzamiento]({{site.baseurl}}/post-launch_edits/).
{% endalert %}

