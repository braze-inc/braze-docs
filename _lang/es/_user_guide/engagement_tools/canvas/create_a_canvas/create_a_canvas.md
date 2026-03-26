---
nav_title: Crear un Canvas
article_title: Crear un Canvas
page_order: 0
page_type: reference
description: "En este artículo de referencia se cubren los pasos necesarios para crear, mantener y probar un Canvas."
tool: Canvas
search_rank: 1
---

# Crear un Canvas

> En este artículo de referencia se cubren los pasos necesarios para crear, mantener y probar un Canvas. Sigue esta guía o consulta nuestro [curso de Braze Learning sobre Canvas](https://learning.braze.com/quick-overview-canvas-setup).

{% details Ampliar para ver los detalles del editor original de Canvas %}
Ya no puedes crear ni duplicar Canvas utilizando la experiencia original de Canvas. Braze recomienda [clonar tus Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/) en el editor más actual.
{% enddetails %}

## Crear un Canvas

### Paso 1: Configurar un nuevo Canvas 

Primero, ve a **Mensajería** > **Canvas** y, a continuación, selecciona **Crear Canvas**.

El Canvas Builder te guiará paso a paso en la configuración de tu Canvas, desde la asignación de un nombre hasta la configuración de eventos de conversión y la introducción de los usuarios adecuados en el recorrido del cliente. Selecciona cada una de las pestañas siguientes para ver los ajustes que puedes realizar en cada paso de la construcción.

{% tabs local %}
  {% tab Basics %}
    Aquí configurarás los aspectos básicos de tu Canvas:
    - Ponle nombre a tu Canvas
    - Añadir equipos
    - Añadir etiquetas
    - Asignar eventos de conversión, y elegir sus tipos de evento y fechas límite

    Learn more about the [Basics step](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab Entry Schedule %}
    Aquí decidirás cómo y cuándo tus usuarios entrarán en tu Canvas:
    - Programado: Se trata de una entrada en Canvas basada en el tiempo
    - Basado en la acción: Tu usuario entrará en tu Canvas después de realizar una acción definida
    - Desencadenado por API: Utiliza una solicitud API para introducir usuarios en tu Canvas

    Learn more about the [Entry Schedule step](#step-2b-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Target Audience %}
    Aquí seleccionarás tu audiencia objetivo:
    - Crea tu audiencia añadiendo segmentos y filtros
    - Ajustar los límites de entrada y reentrada en Canvas
    - Ver un resumen de tu audiencia objetivo

    Learn more about the [Target Audience step](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab Send Settings %}
    Aquí seleccionarás tu configuración de envío de Canvas:
    - Selecciona tu configuración de suscripción
    - Establece un límite de velocidad de envío para tus mensajes de Canvas
    - Activar y configurar las horas tranquilas

    Learn more about the [Send Settings step](#step-2d-select-your-send-settings).
  {% endtab %}
  {% tab Build Canvas %}
    Aquí construirás tu Canvas.

    Learn how to [build your Canvas](#step-3-build-your-canvas) using the Canvas builder.
  {% endtab %}
  {% tab Summary %}
    Aquí encontrarás el resumen de los datos de tu Canvas. Si tienes activado el [flujo de trabajo de aprobación de Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/), puedes aprobar los detalles de Canvas listados antes de lanzarlo.

  {% endtab %}
{% endtabs %}

#### Paso 1.1: Empieza con lo básico de Canvas

Aquí nombrarás tu Canvas, asignarás [equipos]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams) y crearás o añadirás [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags). También puedes asignar eventos de conversión para el Canvas.

{% alert tip %}
Etiqueta tus Canvas para que sea fácil encontrarlos y crear informes a partir de ellos. Por ejemplo, al utilizar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), puedes filtrar por determinadas etiquetas.
{% endalert %}

![La página de detalles de Canvas, con campos para el nombre, la descripción, la ubicación y las etiquetas de Canvas.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

##### Elegir eventos de conversión

Elige el tipo de evento de conversión y, a continuación, selecciona las conversiones que deseas registrar. Estos [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) medirán la eficacia de tu Canvas. 

![Evento de conversión primaria A con el tipo de evento de conversión Realiza compra para registrar las conversiones de los usuarios que realizan cualquier compra dentro de un plazo de conversión de tres días.]({% image_buster /assets/img/add_canvas_conversions.png %})

Si tu Canvas tiene múltiples variantes o un grupo de control, Braze utilizará este evento de conversión para determinar la mejor variación para alcanzar este objetivo de conversión. Utilizando la misma lógica, puedes crear varios eventos de conversión.

#### Paso 1.2: Determina tu horario de entrada en Canvas

Puedes elegir una de las tres formas en que los usuarios pueden entrar en tu Canvas. 

##### Tipos de horarios de entrada

{% tabs local %}
  {% tab Scheduled Delivery %}
    Con la entrega programada, los usuarios entrarán en un horario, de forma similar a como se programaría una campaña. Puedes inscribir a los usuarios en un Canvas en cuanto se lance, introducirlos en su recorrido en algún momento en el futuro o de forma recurrente (diaria, semanal o mensualmente). 
    
   Si seleccionas una programación recurrente mensual, ten en cuenta que algunos meses pueden no tener el día seleccionado. Por ejemplo, supongamos que configuras un Canvas para que se envíe mensualmente el día 31. En este escenario, Braze envía el último día de ese mes, como el 30 de abril, porque el 31 de abril no existe.

    En este ejemplo, según las opciones basadas en el tiempo, los usuarios entran en este Canvas todos los martes a las 12 p. m. en su zona horaria local cada semana, comenzando el 14 de noviembre de 2025 hasta el 31 de diciembre de 2025.

    ![La página «Horario de entrada» con el tipo establecido en «Programado». Debido a la selección, se muestran opciones basadas en el tiempo, incluyendo frecuencia, hora de inicio, recurrencia, días y más.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Action-Based Delivery %}
    Con la entrega basada en acciones, los usuarios entrarán en el Canvas y empezarán a recibir mensajes cuando realicen determinadas acciones, como abrir tu aplicación, realizar una compra o desencadenar un evento personalizado.

    Puedes controlar otros aspectos del comportamiento del Canvas desde la ventana **Audiencia de entrada**, incluyendo reglas de reelegibilidad y configuración de limitación de frecuencia. Ten en cuenta que la entrega basada en acciones no está disponible para componentes de Canvas con mensajes dentro de la aplicación.

    ![Un ejemplo de entrega basada en acciones. Los usuarios entrarán en el Canvas si realizan una compra con una ventana de entrada que comienza a la 1:30 p. m. del 10 de junio de 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

  {% endtab %}
  {% tab API-Triggered Delivery %}
    Con la entrega desencadenada por API, los usuarios entrarán en tu Canvas y comenzarán a recibir mensajes después de que se hayan añadido utilizando el [punto de conexión `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) a través de la API. En el dashboard, puedes encontrar un ejemplo de solicitud cURL que hace esto, así como asignar opcionalmente [`context`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) utilizando el [objeto de contexto]({{site.baseurl}}/api/objects_filters/context_object/). 

    ![Un ejemplo de entrega desencadenada por API con un ID de Canvas y un ejemplo de solicitud cURL.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    Puedes usar los siguientes puntos de conexión para la entrega desencadenada por API:
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

Tras seleccionar tu método de entrega, ajusta la configuración para que coincida con tu caso de uso y luego continúa con la configuración de tu audiencia objetivo.

{% details Comportamiento de deduplicación para Canvas que usan el editor original %}
En caso de que la ventana de reelegibilidad sea inferior a la duración máxima del Canvas, se permitirá a un usuario volver a entrar y recibir los mensajes de más de un componente. En el caso extremo de que la reentrada de un usuario llegue al mismo componente que su entrada anterior, Braze deduplicará los mensajes de ese componente. 

Si un usuario vuelve a entrar en el Canvas, llega al mismo componente que su entrada anterior y es elegible para un mensaje dentro de la aplicación por cada entrada, el usuario recibirá el mensaje dos veces (dependiendo de la prioridad de los mensajes dentro de la aplicación) siempre que vuelva a abrir una sesión dos veces.
{% enddetails %}

#### Paso 1.3: Configura tu audiencia objetivo de entrada

Solo los usuarios que cumplan los criterios definidos podrán acceder al recorrido en el paso **Audiencia objetivo**, lo que significa que Braze evalúa primero la idoneidad de la audiencia objetivo **antes de que** los usuarios accedan al recorrido de Canvas. Por ejemplo, si deseas dirigirte a nuevos usuarios, puedes seleccionar un segmento de usuarios que utilizaron tu aplicación por primera vez hace menos de una semana.

En **Controles de entrada**, puedes limitar el número de usuarios cada vez que se programa la ejecución de Canvas. Para los Canvas basados en acciones y desencadenados por API, este límite se produce a cada hora UTC. 

{% multi_lang_include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

##### Prueba tu audiencia

Después de añadir segmentos y filtros a tu audiencia objetivo, puedes comprobar si tu audiencia está configurada según lo esperado [buscando un usuario]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) para confirmar si coincide con los criterios de la audiencia.

![El campo «Búsqueda de usuario», que te permite buscar por ID de usuario externo o ID de Braze.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

##### Seleccionar controles de entrada

Los controles de entrada determinan si se permite a los usuarios volver a entrar en un Canvas. También puedes limitar el número de personas que podrían acceder a este Canvas mediante una cadencia seleccionada en función del tipo de horario de entrada:

- **Programado:** Vida útil del Canvas o cada vez que se programa el Canvas
- **Basado en acciones:** Por hora, por día o durante toda la vida útil del Canvas
- **Desencadenado por API:** Por hora, por día o durante toda la vida útil del Canvas

Por ejemplo, si tienes un Canvas basado en acciones y seleccionas **Limitar el volumen de entradas** y estableces el campo **Entradas máximas** en 5000 usuarios con **Diario** como cadencia límite, el Canvas solo enviará mensajes a 5000 usuarios al día.

![La página «Controles de entrada» muestra casillas de verificación para «Permitir a los usuarios volver a entrar en Canvas» y «Limitar el volumen de entradas». Esto último te permite establecer el número máximo de entradas y elegir una cadencia que depende del tipo de programación de entradas (por ejemplo, la duración del Canvas o cada vez que el Canvas está programado para una entrada programada, y cada hora, cada día o la duración del Canvas para entradas basadas en acciones y desencadenadas por API).]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Braze no recomienda seleccionar **Cada vez que Canvas esté programado** para el calentamiento de IP, ya que esto puede provocar un aumento en los volúmenes de envío.
{% endalert %}

##### Establecer criterios de salida

La configuración de los [criterios de salida]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) determina qué usuarios deseas que salgan de un Canvas. Si un usuario realiza el evento de excepción o coincide con los segmentos y filtros, no recibirá más mensajes.

##### Cálculo de la población objetivo

En la sección **Población objetivo**, puedes ver un resumen de tu audiencia, como los segmentos seleccionados y los filtros adicionales, y un desglose de cuántos usuarios son alcanzables por canal de mensajería. Para calcular el número exacto de usuarios alcanzables de tu audiencia objetivo en lugar de la estimación predeterminada, selecciona [Calcular estadísticas exactas]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics).

Ten en cuenta que:

- Calcular las estadísticas exactas puede llevar unos minutos. Esta función solo calcula las estadísticas exactas a nivel de segmento, no a nivel de filtro o grupo de filtros.
- En el caso de segmentos grandes, es normal que se produzcan ligeras variaciones incluso cuando se calculan estadísticas exactas. Se espera que la precisión de esta característica sea del 99,999 % o superior.

Para ver estadísticas adicionales, como los ingresos medios durante la vida útil de los usuarios objetivo, selecciona **Mostrar estadísticas adicionales**.

![Desglose de la población objetivo con opción de calcular estadísticas exactas.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

##### ¿Por qué el número de audiencia objetivo puede diferir del número de usuarios alcanzables?

{% multi_lang_include segments.md section='Differing audience size' %}

#### Paso 1.4: Selecciona tu configuración de envío

Selecciona **Configuración de envío** para editar los ajustes de suscripción, activar la limitación de velocidad y activar las horas tranquilas. Al activar la [limitación de velocidad]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-canvas-components) o la [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping), puedes aliviar la presión de marketing que se ejerce sobre tus usuarios y asegurarte de no enviarles demasiados mensajes.

En el caso de los Canvas dirigidos a los canales de correo electrónico y push, es posible que desees limitar tu Canvas para que solo los usuarios que hayan optado explícitamente por la adhesión voluntaria reciban el mensaje (excluyendo a los usuarios suscritos o dados de baja). Por ejemplo, supongamos que tienes tres usuarios con diferentes estados de suscripción:

- **El usuario A** está suscrito al correo electrónico y tiene activada la función push. Este usuario no recibe el correo electrónico pero recibirá el push.
- **El usuario B** tiene la adhesión voluntaria al correo electrónico, pero no está habilitado para push. Este usuario recibirá el correo electrónico pero no recibirá el push.
- **El usuario C** ha optado por la adhesión voluntaria al correo electrónico y está habilitado para push. Este usuario recibirá tanto el correo electrónico como el push.

Para ello, configura los **Ajustes de suscripción** para enviar este Canvas «solo a los usuarios que hayan dado su consentimiento». Esta opción garantizará que solo los usuarios que hayan optado por recibirla reciban tu correo electrónico, y Braze solo enviará tu push a los usuarios que estén habilitados para push de forma predeterminada. 

Estos ajustes de suscripción se aplican en cada paso, lo que significa que no hay ningún efecto sobre la audiencia de entrada. Por lo tanto, esta configuración se utiliza para evaluar la elegibilidad de un usuario para recibir cada paso en Canvas.

{% alert important %}
Con esta configuración, no incluyas ningún filtro en el paso **Audiencia objetivo** que limite la audiencia a un solo canal (por ejemplo, `Foreground Push Enabled = True` o `Email Subscription = Opted-In`).
{% endalert %}

Si lo deseas, especifica las horas tranquilas (el tiempo durante el cual no se enviarán tus mensajes) para tu Canvas. Marca **Activar horas tranquilas** en tu **Configuración de envío**. A continuación, selecciona tus horas tranquilas en la hora local de tu usuario y la acción que seguirá si el mensaje se desencadena dentro de esas horas tranquilas.

![La página «Horas tranquilas» muestra una casilla para habilitar las horas tranquilas. Si se habilita, se puede establecer la hora de inicio, la hora de finalización y el comportamiento de alternativa.]({% image_buster /assets/img/quiet_hours.png %})

### Paso 2: Construye tu Canvas

{% alert tip %}
¡Ahorra tiempo y agiliza tu creación de Canvas utilizando las [plantillas de Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/#available-braze-templates)! Explora nuestra biblioteca de plantillas prediseñadas para encontrar una que se adapte a tu caso de uso y personalízala para satisfacer tus necesidades específicas.
{% endalert %}

#### Paso 2.1: Añadir una variante

![El botón «Añadir variante» seleccionado para mostrar un menú contextual con la opción «Añadir variante».]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

Selecciona **Añadir variante** y añade una nueva variante a tu Canvas. Las variantes representan un recorrido que realizarán tus usuarios y pueden contener múltiples pasos y ramificaciones.

Puedes añadir variantes adicionales seleccionando el botón <i class="fas fa-plus-circle"></i> más. Cuando añadas nuevas variantes, podrás ajustar cómo se distribuirán tus usuarios entre ellas para poder comparar y analizar la eficacia de las distintas estrategias de interacción.

![Dos variantes de ejemplo en un Canvas de Braze.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
Por defecto, la asignación de variantes en Canvas se bloquea cuando los usuarios entran en el Canvas, lo que significa que si un usuario entra por primera vez en una variante, esa será su variante cada vez que vuelva a entrar en el Canvas. Sin embargo, hay formas de eludir este comportamiento. <br><br>Para ello, puedes crear un generador de números aleatorios utilizando Liquid, ejecutarlo al principio de la entrada de cada usuario en Canvas, almacenar el valor como un atributo personalizado y, a continuación, utilizar ese atributo para dividir aleatoriamente a los usuarios.

{% details Ampliar para ver los pasos %}

1. Crea un atributo personalizado para almacenar tu número aleatorio. Ponle un nombre fácil de localizar, como "lottery_number" o "random_assignment". Puedes crear el atributo [en tu dashboard]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) o mediante llamadas API a nuestro [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).<br><br>
2. Crea una campaña webhook al principio de tu Canvas. Esta campaña será el medio en el que crearás tu número aleatorio y lo almacenarás como atributo personalizado. Consulta [Crear un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook) para obtener más información. Establece la URL de nuestro punto de conexión `/users/track`.<br><br>
3. Crea el generador de números aleatorios. Puedes hacerlo con el código [que se describe aquí](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486), que aprovecha la hora de entrada única de cada usuario para crear un número aleatorio. Establece el número resultante como una variable Liquid dentro de tu campaña webhook.<br><br>
4. Formatea la llamada `/users/track` en tu campaña webhook para que establezca el atributo personalizado que creaste en el paso 1 con el número aleatorio que has generado en el perfil de tu usuario actual. Cuando este paso se ejecute, habrás conseguido crear un número aleatorio que cambiará cada vez que un usuario entre en tu campaña.<br><br>
5. Ajusta las ramas de tu Canvas para que, en lugar de estar divididas por variantes elegidas al azar, se dividan en función de las reglas de audiencia. En las reglas de audiencia de cada rama, establece el filtro de audiencia según tu atributo personalizado. <br><br>Por ejemplo, una rama puede tener "lottery_number es menor que 3" como filtro de audiencia, mientras que otra rama puede tener "lottery_number es mayor que 3 y menor que 6" como filtro de audiencia.

{% enddetails %}
{% endalert %}

#### Paso 2.2: Añadir pasos en Canvas

Puedes añadir más pasos a tu flujo de trabajo de Canvas arrastrando y soltando componentes desde la barra lateral **Componentes**. O bien, selecciona el botón <i class="fas fa-plus-circle"></i> más para añadir un componente con el menú desplegable.

{% alert tip %}
Cuando empieces a añadir más pasos, puedes cambiar el nivel de zoom para centrarte en los detalles o abarcar todo el recorrido del usuario. Acércate con <kbd>Shift</kbd> + <kbd>+</kbd> o aléjate con <kbd>Shift</kbd> + <kbd>-</kbd>.
{% endalert %}

![La ventana de búsqueda de componentes añade un paso de retraso al Canvas de Braze.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
Puedes añadir hasta 200 pasos en un Canvas. Si tu Canvas supera los 200 pasos, pueden producirse problemas de carga.
{% endalert %}

##### Duración máxima

A medida que el recorrido de tu Canvas aumenta en pasos, la duración máxima es el mayor tiempo posible que un usuario puede tardar en completar este Canvas. Se calcula sumando los retrasos y las ventanas de activación de cada paso de cada variante para el camino más largo. Por ejemplo, si tu Canvas tiene un paso de retraso con un retraso de 3 días y un paso de mensaje, la duración máxima de tu Canvas será de 3 días.

##### Editar un paso

¿Quieres editar un paso de tu recorrido de usuario? Comprueba cómo hacerlo en función de tu flujo de trabajo en Canvas.

Puedes editar cualquier paso del flujo de trabajo de Canvas seleccionando cualquiera de los componentes. Por ejemplo, digamos que deseas editar tu primer paso, un componente de [retraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), en tu flujo de trabajo a un día específico. Selecciona el paso para ver su configuración y ajusta tu retraso al 1 de marzo. Esto significa que el 1 de marzo, tus usuarios pasarán al siguiente paso en tu Canvas.

![Un ejemplo de paso «Retraso» con el retraso establecido en «Hasta un día específico».]({% image_buster /assets/img_archive/edit_delay_flow.png %})

También puedes editar y ajustar rápidamente la **Configuración de acción** de tu paso [Rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) para retener a los usuarios durante un periodo de tiempo. Esto prioriza su próximo camino en función de las acciones durante este período de evaluación.

![El segundo paso en el Canvas, «Configuración de acciones», con una ventana de evaluación establecida en 1 día.]({% image_buster /assets/img_archive/action_paths_flow.png %})

Los componentes ligeros de Canvas permiten una experiencia de edición sencilla, por lo que ajustar los detalles más sutiles de tu Canvas es más fácil. 

##### Mensajes en Canvas

Edita los mensajes de un componente de Canvas para controlar los mensajes que enviará un paso concreto. Canvas puede enviar mensajes push por correo electrónico, móvil y web, así como webhooks para integrarse con otros sistemas. De forma similar a las campañas, puedes utilizar determinadas plantillas de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) para personalizar tus mensajes.

{% alert tip %}
¿Sabías que puedes incluir nombres de componentes de Canvas en tus mensajes y plantillas de enlaces?<br>
Utiliza la etiqueta de Liquid `campaign.${name}` en Canvas para mostrar el nombre del componente de Canvas actual.
{% endalert %}

El componente Mensaje gestiona los mensajes enviados a los usuarios. Puedes seleccionar tus **canales de mensajería** y ajustar la **configuración de entrega** para optimizar tu mensajería en Canvas. Para más detalles sobre este componente, consulta [Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

![El paso «Configurar mensajes», con la opción «Canales de mensajería» seleccionada, muestra la lista de canales de mensajería disponibles, como push para Android, tarjetas de contenido, correo electrónico y más.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Selecciona **Hecho** cuando hayas terminado de configurar tu componente de Canvas.

{% tabs local %}
{% tab Canvas Entry Properties %}

El [objeto `context`]({{site.baseurl}}/api/objects_filters/context_object) se configura en el paso **Horario de entrada** de la creación de un Canvas e indica el desencadenante que introduce a un usuario en un Canvas. Estas propiedades también pueden acceder a las propiedades de las cargas útiles de entrada en los Canvas desencadenados por API. Ten en cuenta que el objeto `context` puede tener un tamaño máximo de 50 KB. 

Utiliza el siguiente Liquid cuando hagas referencia a estas propiedades creadas al entrar en el Canvas: {% raw %} ``context.${property_name}`` {% endraw %}. Ten en cuenta que los eventos deben ser eventos personalizados o eventos de compra para ser utilizados de esta manera.

{% raw %}
Por ejemplo, considera la siguiente solicitud: `\"context\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Puedes añadir la palabra "shoes" a un mensaje con este Liquid ``{{context.${product_name}}}``.
{% endraw %}

{% endtab %}

{% tab Event Properties %}
Las propiedades del evento son las propiedades establecidas por ti en los eventos personalizados y compras. Estos `event_properties` se pueden utilizar en campañas con entrega basada en acciones, así como en Canvas. 

En Canvas, las propiedades de eventos personalizados y de compra se pueden utilizar en Liquid en cualquier paso de mensaje que siga a un paso de rutas de acción. Utiliza este Liquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} cuando hagas referencia a estos `event_properties`. Estos eventos deben ser eventos personalizados o eventos de compra para ser utilizados de esta forma en el componente Mensaje.

En el primer paso de mensaje que sigue a una ruta de acción, puedes utilizar `event_properties` relacionados con el evento al que se hace referencia en esa ruta de acción. Puedes tener otros pasos (que no sean otro paso de rutas de acción o mensaje) entre este paso de rutas de acción y el paso de mensaje. Ten en cuenta que solo tendrás acceso a `event_properties` si tu paso de mensaje puede remontarse a una ruta que no sea El resto en un paso de ruta de acción.

{% endtab %}
{% endtabs %}

#### Paso 2.3: Editar conexiones

Para mover una conexión entre pasos, selecciona la flecha que conecta los dos componentes y selecciona un componente diferente. Para eliminar la conexión, selecciona la flecha seguida de **Cancelar conexión** en el pie de página del compositor de Canvas.

### Paso 3: Añadir un grupo de control

Puedes añadir un grupo de control a tu Canvas seleccionando el botón <i class="fas fa-plus-circle"></i> más para añadir una nueva variante. 

Braze realizará un seguimiento de las conversiones de los usuarios incluidos en el grupo de control, aunque no recibirán ningún mensaje. Para que la prueba sea precisa, realizaremos un seguimiento del número de conversiones de tus variantes y del grupo de control durante exactamente el mismo periodo de tiempo, como se muestra en la pantalla de selección del evento de conversión. 

Puedes ajustar la distribución entre tus mensajes haciendo doble clic en las cabeceras de **Nombre de variante**.

En este ejemplo, tenemos nuestro Canvas dividido en dos variantes. La variante 1 cuenta con el 70 % de los usuarios. La segunda variante es un grupo de control con el 30 % restante de usuarios.

![Una variante de ejemplo en un Canvas de Braze, donde el 70 % va a la «Variante 1», que retrasa 1 día en el primer paso, y luego envía un mensaje en el segundo paso. El 30 % restante se destina a un «Control» que no tiene ningún paso de seguimiento.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

#### Intelligent Selection para Canvas

Las funciones de Intelligent Selection ya están disponibles en los Canvas multivariantes. De forma similar a la característica [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) para campañas multivariantes, Intelligent Selection para Canvas analiza el rendimiento de cada variante en Canvas y ajusta el porcentaje de usuarios que se canalizan a través de cada variante. Esta distribución se basa en las métricas de rendimiento de cada variante para maximizar el número total esperado de conversiones.

Ten en cuenta que los Canvas multivariantes no solo te permiten probar el texto, sino también el momento y los canales. Gracias a Intelligent Selection, puedes probar los Canvas de forma más eficaz y confiar en que tus usuarios realizarán el mejor recorrido posible en Canvas.

![La opción «Intelligent Selection» está habilitada en la página «Editar distribución de variantes». A medida que analiza y optimiza el Canvas, muestra una barra horizontal a través de la página dividida en varias secciones, cada una de las cuales varía en color y tamaño. Esto es solo una representación visual y no se correlaciona con ningún análisis específico.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

Intelligent Selection para Canvas optimiza tus resultados de Canvas realizando ajustes graduales en tiempo real de la distribución de usuarios clasificados en cada variante. Cuando el algoritmo estadístico determine un ganador decisivo entre tus variantes, descartará las variantes con bajo rendimiento e incluirá a todos los futuros destinatarios elegibles del Canvas en las variantes ganadoras. 

Por esta razón, Intelligent Selection funciona mejor en Canvas en los que entran nuevos usuarios con frecuencia.

### Paso 4: Guardar y lanzar

Cuando hayas terminado de crear tu Canvas, selecciona **Lanzar Canvas** para guardarlo y lanzarlo. Una vez que hayas lanzado tu Canvas, podrás ver los análisis de tu recorrido a medida que vayan llegando en la página **Detalles del Canvas**. 

También puedes guardar tu Canvas como borrador por si necesitas volver a él.

![Un ejemplo de Canvas en Braze.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
¿Necesitas modificar tu Canvas después del lanzamiento? ¡Pues puedes hacerlo! Para más información, consulta [Editar Canvas después del lanzamiento]({{site.baseurl}}/post-launch_edits/).
{% endalert %}