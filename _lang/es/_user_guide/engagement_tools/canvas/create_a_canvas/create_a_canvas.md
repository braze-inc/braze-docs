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

> En este artículo de referencia se cubren los pasos necesarios para crear, mantener y probar un Canvas. Siga esta guía o consulte nuestro [curso de Braze Learning sobre Canvas](https://learning.braze.com/quick-overview-canvas-setup).

{% details Ampliar para ver los detalles del editor original de Canvas %}
Ya no puede crear o duplicar Canvas utilizando la experiencia original de Canvas. Braze recomienda [clonar sus Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/) al editor más actual.
{% enddetails %}

## Crear un Canvas

### Paso 1: Configurar un nuevo Canvas 

Primero, vaya a **Mensajería** > **Canvas** y, a continuación, seleccione **Crear Canvas**.

El constructor de Canvas le guiará paso a paso en la configuración de su Canvas, desde la asignación de un nombre hasta la configuración de eventos de conversión y la incorporación de los usuarios adecuados en el recorrido del cliente. Seleccione cada una de las siguientes pestañas para ver los ajustes que puede realizar en cada paso del constructor.

{% tabs local %}
  {% tab Basics %}
    Aquí configurará los aspectos básicos de su Canvas:
    - Asigne un nombre a su Canvas
    - Añadir equipos
    - Añadir etiquetas
    - Asignar eventos de conversión y elegir sus tipos de evento y fechas límite

    Learn more about the [Basics step](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab Entry Schedule %}
    Aquí decidirá cómo y cuándo entrarán sus usuarios en su Canvas:
    - Programado: Se trata de una entrada en Canvas basada en el tiempo
    - Basado en la acción: Su usuario entrará en su Canvas después de realizar una acción definida
    - Activado por API: Utilice una solicitud API para introducir usuarios en su Canvas

    Learn more about the [Entry Schedule step](#step-2b-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Target Audience %}
    Aquí seleccionará su audiencia objetivo:
    - Cree su audiencia añadiendo segmentos y filtros
    - Ajuste los límites de entrada y reentrada en Canvas
    - Vea un resumen de su audiencia objetivo

    Learn more about the [Target Audience step](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab Send Settings %}
    Aquí seleccionará la configuración de envío de su Canvas:
    - Seleccione su configuración de suscripción
    - Establezca un límite de velocidad de envío para los mensajes de su Canvas
    - Habilite y configure las horas tranquilas

    Learn more about the [Send Settings step](#step-2d-select-your-send-settings).
  {% endtab %}
  {% tab Build Canvas %}
    Aquí construirá su Canvas.

    Learn how to [build your Canvas](#step-3-build-your-canvas) using the Canvas builder.
  {% endtab %}
  {% tab Summary %}
    Aquí encontrará el resumen de los detalles de su Canvas. Si tiene activado el [flujo de trabajo de aprobación de Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/), puede aprobar los detalles del Canvas listados antes de lanzarlo.

  {% endtab %}
{% endtabs %}

#### Paso 1.1: Empiece con los aspectos básicos de Canvas

Aquí asignará un nombre a su Canvas, asignará [equipos]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams) y creará o añadirá [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags). También puede asignar eventos de conversión para el Canvas.

{% alert tip %}
Etiquete sus Canvas para que sea fácil encontrarlos y crear informes a partir de ellos. Por ejemplo, al utilizar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), puede filtrar por determinadas etiquetas.
{% endalert %}

![La página de detalles del Canvas, con campos para el nombre, descripción, ubicación y etiquetas del Canvas.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

##### Elegir eventos de conversión

Elija el tipo de evento de conversión y, a continuación, seleccione las conversiones que desea registrar. Estos [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) medirán la eficacia de su Canvas. 

![Evento de conversión primaria A con el tipo de evento de conversión Realiza compra para registrar las conversiones de los usuarios que realizan cualquier compra dentro de un plazo de conversión de tres días.]({% image_buster /assets/img/add_canvas_conversions.png %})

Si su Canvas tiene múltiples variantes o un grupo de control, Braze utilizará este evento de conversión para determinar la mejor variación para alcanzar este objetivo de conversión. Utilizando la misma lógica, puede crear varios eventos de conversión.

#### Paso 1.2: Determine su horario de entrada en Canvas

Puede elegir una de las tres formas en que los usuarios pueden entrar en su Canvas. 

##### Tipos de horarios de entrada

{% tabs local %}
  {% tab Scheduled Delivery %}
    Con la entrega programada, los usuarios entrarán según un horario, de forma similar a como se programaría una campaña. Puede inscribir a los usuarios en un Canvas en cuanto se lance, introducirlos en su recorrido en algún momento en el futuro o de forma recurrente (diaria, semanal o mensualmente). 

    En este ejemplo, basándose en las opciones de tiempo, los usuarios entrarán en este Canvas cada martes a las 12 p. m. en su zona horaria local cada semana, comenzando el 14 de noviembre de 2025 hasta el 31 de diciembre de 2025.

    ![La página "Horario de entrada" con el tipo configurado como "Programado". Debido a la selección, se muestran opciones basadas en el tiempo, incluyendo frecuencia, hora de inicio, recurrencia, días y más.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Action-Based Delivery %}
    Con la entrega basada en acciones, los usuarios entrarán en el Canvas y empezarán a recibir mensajes cuando realicen determinadas acciones, como abrir su aplicación, realizar una compra o desencadenar un evento personalizado.

    Puede controlar otros aspectos del comportamiento del Canvas desde la ventana **Audiencia de entrada**, incluidas las reglas de reelegibilidad y la configuración de limitación de frecuencia. Tenga en cuenta que la entrega basada en acciones no está disponible para los componentes de Canvas con mensajes dentro de la aplicación.

    ![Un ejemplo de entrega basada en acciones. Los usuarios entrarán en el Canvas si realizan una compra con una ventana de entrada que comienza a la 1:30 p. m. del 10 de junio de 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

  {% endtab %}
  {% tab API-Triggered Delivery %}
    Con la entrega activada por API, los usuarios entrarán en su Canvas y comenzarán a recibir mensajes después de que se hayan añadido utilizando el [punto final `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) a través de la API. En el panel, puede encontrar un ejemplo de solicitud cURL que hace esto, así como asignar [`context`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) opcionales utilizando el [objeto de contexto]({{site.baseurl}}/api/objects_filters/context_object/). 

    ![Un ejemplo de entrega activada por API con un ID de Canvas y un ejemplo de solicitud cURL.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    Puede utilizar los siguientes puntos finales para la entrega activada por API:
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

Tras seleccionar su método de entrega, ajuste la configuración para que coincida con su caso de uso y luego continúe con la configuración de su audiencia objetivo.

{% details Comportamiento de deduplicación para Canvas que utilizan el editor original %}
En caso de que la ventana de reelegibilidad sea inferior a la duración máxima del Canvas, se permitirá a un usuario volver a entrar y recibir los mensajes de más de un componente. En el caso extremo de que la reentrada de un usuario llegue al mismo componente que su entrada anterior, Braze deduplicará los mensajes de ese componente. 

Si un usuario vuelve a entrar en el Canvas, llega al mismo componente que su entrada anterior y es elegible para un mensaje dentro de la aplicación por cada entrada, el usuario recibirá el mensaje dos veces (dependiendo de la prioridad de los mensajes dentro de la aplicación) siempre que vuelva a abrir una sesión dos veces.
{% enddetails %}

#### Paso 1.3: Configure su audiencia objetivo de entrada

Solo los usuarios que coincidan con los criterios definidos pueden entrar en el recorrido en el paso **Audiencia objetivo**, lo que significa que Braze evalúa primero la elegibilidad de la audiencia objetivo **antes de** que los usuarios entren en el recorrido del Canvas. Por ejemplo, si desea dirigirse a nuevos usuarios, puede seleccionar un segmento de usuarios que utilizaron su aplicación por primera vez hace menos de una semana.

En **Controles de entrada**, puede limitar el número de usuarios cada vez que se programe la ejecución del Canvas. Para los Canvas basados en acciones y activados por API, este límite se produce a cada hora UTC. 

{% include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

##### Pruebe su audiencia

Después de añadir segmentos y filtros a su audiencia objetivo, puede comprobar si su audiencia está configurada según lo esperado [buscando un usuario]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) para confirmar si coincide con los criterios de la audiencia.

![El campo "Búsqueda de usuarios", que le permite buscar por ID externo de usuario o ID de Braze.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

##### Seleccionar controles de entrada

Los controles de entrada determinan si se permite a los usuarios volver a entrar en un Canvas. También puede limitar el número de personas que potencialmente entrarían en este Canvas según una cadencia seleccionada dependiendo del tipo de horario de entrada:

- **Programado:** Durante toda la vida del Canvas o cada vez que se programe el Canvas
- **Basado en la acción:** Por hora, diariamente o durante toda la vida del Canvas
- **Activado por API:** Por hora, diariamente o durante toda la vida del Canvas

Por ejemplo, si tiene un Canvas basado en acciones y selecciona **Limitar volumen de entradas** y establece el campo **Entradas máximas** en 5.000 usuarios con **Diariamente** como cadencia límite, entonces el Canvas solo enviará a 5.000 usuarios al día.

![La página "Controles de entrada" muestra las casillas de verificación "Permitir a los usuarios volver a entrar en Canvas" y "Limitar el volumen de entrada". Esto último le permite establecer el máximo de entradas y elegir una cadencia que depende del tipo de horario de entrada (por ejemplo, durante toda la vida del Canvas o cada vez que se programe el Canvas para entrada programada, y por hora, diariamente o durante toda la vida del Canvas para entrada basada en acciones y activada por API).]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Braze no recomienda seleccionar **Cada vez que se programa el Canvas** para el calentamiento de IP, ya que puede provocar un aumento del volumen de envíos.
{% endalert %}

##### Establecer criterios de salida

La configuración de los [criterios de salida]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) determina qué usuarios desea que salgan de un Canvas. Si un usuario realiza el evento de excepción o coincide con los segmentos y filtros, no recibirá más mensajes.

##### Cálculo de la población objetivo

En la sección **Población objetivo**, puede ver un resumen de su audiencia, como los segmentos seleccionados y los filtros adicionales, y un desglose de cuántos usuarios son alcanzables por canal de mensajería. Para calcular el número exacto de usuarios alcanzables de su audiencia objetivo en lugar de la estimación predeterminada, seleccione [Calcular estadísticas exactas]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics).

Tenga en cuenta que:

- Calcular las estadísticas exactas puede llevar unos minutos. Esta función solo calcula las estadísticas exactas a nivel de segmento, no a nivel de filtro o grupo de filtros.
- En el caso de segmentos grandes, es normal que se produzcan ligeras variaciones incluso cuando se calculan estadísticas exactas. Se espera que la precisión de esta característica sea del 99,999 % o superior.

Para ver estadísticas adicionales, como los ingresos medios durante la vida útil de los usuarios objetivo, seleccione **Mostrar estadísticas adicionales**.

![Desglose de la población objetivo con opción de calcular estadísticas exactas.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

##### Por qué el recuento de la audiencia objetivo puede diferir del recuento de usuarios alcanzables

{% multi_lang_include segments.md section='Differing audience size' %}

#### Paso 1.4: Seleccione su configuración de envío

Seleccione **Configuración de envío** para editar los ajustes de suscripción, activar el límite de velocidad y habilitar las horas tranquilas. Al activar el [límite de velocidad]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-canvas-components) o la [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping), puede aliviar la presión de marketing sobre sus usuarios y asegurarse de que no les envía demasiados mensajes.

En el caso de los Canvas dirigidos a los canales de correo electrónico y push, es posible que desee limitar su Canvas para que solo los usuarios que hayan optado explícitamente por la adhesión voluntaria reciban el mensaje (excluyendo a los usuarios suscritos o que cancelaron su suscripción). Por ejemplo, supongamos que tiene tres usuarios con diferentes estados de suscripción:

- **El usuario A** está suscrito al correo electrónico y tiene habilitado push. Este usuario no recibe el correo electrónico pero recibirá el push.
- **El usuario B** tiene la adhesión voluntaria al correo electrónico, pero no está habilitado para push. Este usuario recibirá el correo electrónico pero no recibirá el push.
- **El usuario C** tiene la adhesión voluntaria al correo electrónico y está habilitado para push. Este usuario recibirá tanto el correo electrónico como el push.

Para ello, configure los **Ajustes de suscripción** para enviar este Canvas "solo a los usuarios que hayan dado su consentimiento". Esta opción garantizará que solo los usuarios con adhesión voluntaria reciban su correo electrónico, y Braze solo enviará su push a los usuarios que estén habilitados para push de forma predeterminada. 

Estos ajustes de suscripción se aplican en cada paso, lo que significa que no hay ningún efecto sobre la audiencia de entrada. Por lo tanto, esta configuración se utiliza para evaluar la elegibilidad de un usuario para recibir cada paso en Canvas.

{% alert important %}
Con esta configuración, no incluya ningún filtro en el paso **Audiencia objetivo** que limite la audiencia a un único canal (por ejemplo, `Foreground Push Enabled = True` o `Email Subscription = Opted-In`).
{% endalert %}

Si lo desea, especifique horas tranquilas (el tiempo durante el cual no se enviarán sus mensajes) para su Canvas. Marque **Habilitar horas tranquilas** en la **Configuración de envío**. A continuación, seleccione sus horas tranquilas en la hora local de su usuario y la acción que seguirá si el mensaje se activa dentro de esas horas tranquilas.

![La página "Horas tranquilas" muestra una casilla para habilitar las horas tranquilas. Si se habilita, se puede establecer la hora de inicio, la hora de finalización y el comportamiento alternativa.]({% image_buster /assets/img/quiet_hours.png %})

### Paso 2: Construya su Canvas

{% alert tip %}
¡Ahorre tiempo y agilice la creación de su Canvas utilizando las [plantillas de Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/#available-braze-templates)! Explore nuestra biblioteca de plantillas prediseñadas para encontrar una que se adapte a su caso de uso y personalícela para satisfacer sus necesidades específicas.
{% endalert %}

#### Paso 2.1: Añadir una variante

![Seleccione el botón "Añadir variante" para mostrar un menú contextual con la opción "Añadir variante".]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

Seleccione **Añadir variante** y añada una nueva variante a su Canvas. Las variantes representan un recorrido que realizarán sus usuarios y pueden contener múltiples pasos y ramificaciones.

Puede añadir variantes adicionales seleccionando el botón <i class="fas fa-plus-circle"></i> más. Cuando añada nuevas variantes, podrá ajustar cómo se distribuirán sus usuarios entre ellas para poder comparar y analizar la eficacia de las distintas estrategias de interacción.

![Dos variantes de ejemplo en un Canvas de Braze.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
De forma predeterminada, la asignación de variantes en Canvas se bloquea cuando los usuarios entran en el Canvas, lo que significa que si un usuario entra por primera vez en una variante, esa será su variante cada vez que vuelva a entrar en el Canvas. Sin embargo, hay formas de eludir este comportamiento. <br><br>Para ello, puede crear un generador de números aleatorios utilizando Liquid, ejecutarlo al principio de cada entrada del usuario en Canvas, almacenar el valor como un atributo personalizado y, a continuación, utilizar ese atributo para dividir aleatoriamente a los usuarios.

{% details Ampliar para ver los pasos %}

1. Cree un atributo personalizado para almacenar su número aleatorio. Asígnele un nombre fácil de localizar, como "lottery_number" o "random_assignment". Puede crear el atributo [en su panel]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) o mediante llamadas a la API a nuestro [punto final `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).<br><br>
2. Cree una campaña webhook al principio de su Canvas. Esta campaña será el medio en el que creará su número aleatorio y lo almacenará como atributo personalizado. Para más información, consulte [Crear un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook). Establezca la URL de nuestro punto final `/users/track`.<br><br>
3. Cree el generador de números aleatorios. Puede hacerlo con el código que [se indica aquí](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486), que aprovecha la hora única de entrada de cada usuario para crear un número aleatorio. Establezca el número resultante como una variable Liquid dentro de su campaña webhook.<br><br>
4. Formatee la llamada `/users/track` en su campaña webhook para que establezca el atributo personalizado que creó en el paso 1 con el número aleatorio que ha generado en el perfil de su usuario actual. Cuando este paso se ejecute, habrá conseguido crear un número aleatorio que cambiará cada vez que un usuario entre en su campaña.<br><br>
5. Ajuste las ramas de su Canvas para que, en lugar de estar divididas por variantes elegidas al azar, se dividan en función de las reglas de audiencia. En las reglas de audiencia de cada rama, establezca el filtro de audiencia según su atributo personalizado. <br><br>Por ejemplo, una rama puede tener "lottery_number es menor de 3" como filtro de audiencia, mientras que otra rama puede tener "lottery_number es mayor de 3 y menor de 6" como filtro de audiencia.

{% enddetails %}
{% endalert %}

#### Paso 2.2: Añadir pasos en Canvas

Puede añadir más pasos a su flujo de trabajo en Canvas arrastrando y soltando componentes desde la barra lateral **Componentes**. O bien, seleccione el botón <i class="fas fa-plus-circle"></i> más para añadir un componente con el menú desplegable.

{% alert tip %}
Cuando empiece a añadir más pasos, puede cambiar el nivel de zoom para centrarse en los detalles o abarcar todo el recorrido del usuario. Acérquese con <kbd>Shift</kbd> + <kbd>+</kbd> o aléjese con <kbd>Shift</kbd> + <kbd>-</kbd>.
{% endalert %}

![La ventana de búsqueda de componentes añade un paso de retraso en el Canvas de Braze.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
Puede añadir hasta 200 pasos en un Canvas. Si su Canvas supera los 200 pasos, pueden producirse problemas de carga.
{% endalert %}

##### Duración máxima

A medida que el recorrido de su Canvas aumenta en pasos, la duración máxima es el mayor tiempo posible que un usuario puede tardar en completar este Canvas. Se calcula sumando los retrasos y las ventanas de activación de cada paso de cada variante para el camino más largo. Por ejemplo, si su Canvas tiene un paso de Retraso con un retraso de 3 días y un paso de Mensaje, la duración máxima de su Canvas será de 3 días.

##### Editar un paso

¿Desea editar un paso de su recorrido de usuario? Compruebe cómo hacerlo en función de su flujo de trabajo en Canvas.

Puede editar cualquier paso de su flujo de trabajo en Canvas seleccionando cualquiera de los componentes. Por ejemplo, supongamos que desea editar su primer paso, un componente de [Retraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), en su flujo de trabajo a un día específico. Seleccione el paso para ver su configuración y ajuste su retraso al 1 de marzo. Esto significa que el 1 de marzo, sus usuarios pasarán al siguiente paso en su Canvas.

![Un ejemplo de paso "Retraso" con el retraso ajustado a "Hasta un día concreto".]({% image_buster /assets/img_archive/edit_delay_flow.png %})

También puede editar y ajustar rápidamente la **Configuración de acción** de su paso [Rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) para retener a los usuarios durante un periodo de tiempo. Esto prioriza su siguiente ruta en función de las acciones durante este período de evaluación.

![El segundo paso en Canvas, "Configuración de la acción", con una ventana de evaluación fijada en 1 día.]({% image_buster /assets/img_archive/action_paths_flow.png %})

Los componentes ligeros de Canvas permiten una experiencia de edición sencilla, por lo que ajustar los detalles más sutiles de su Canvas resulta más fácil. 

##### Mensajes en Canvas

Edite los mensajes de un componente de Canvas para controlar los mensajes que enviará un paso concreto. Canvas puede enviar mensajes push por correo electrónico, móvil y web, así como webhooks para integrarse con otros sistemas. De forma similar a las campañas, puede utilizar determinadas plantillas de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) para personalizar sus mensajes.

{% alert tip %}
¿Sabía que puede incluir nombres de componentes de Canvas en sus mensajes y plantillas de enlaces?<br>
Utilice la etiqueta de Liquid `campaign.${name}` en Canvas para mostrar el nombre del componente de Canvas actual.
{% endalert %}

El componente Mensaje gestiona los mensajes enviados a los usuarios. Puede seleccionar sus **Canales de mensajería** y ajustar la **Configuración de entrega** para optimizar su mensajería en Canvas. Para más detalles sobre este componente, consulte [Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

![El paso "Configurar mensajes", con la opción "Canales de mensajería" seleccionada, que muestra la lista de canales de mensajería disponibles, como push de Android, tarjetas de contenido, correo electrónico y otros.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Seleccione **Hecho** cuando haya terminado de configurar su componente de Canvas.

{% tabs local %}
{% tab Canvas Entry Properties %}

El [objeto `context`]({{site.baseurl}}/api/objects_filters/context_object) se configura en el paso **Horario de entrada** de la creación de un Canvas e indica el desencadenante que introduce a un usuario en un Canvas. Estas propiedades también pueden acceder a las propiedades de las cargas útiles de entrada en los Canvas activados por API. Tenga en cuenta que el objeto `context` puede ser de hasta 50 KB. 

Utilice el siguiente Liquid cuando haga referencia a estas propiedades creadas al entrar en el Canvas: {% raw %} ``context.${property_name}`` {% endraw %}. Tenga en cuenta que los eventos deben ser eventos personalizados o eventos de compra para ser utilizados de esta manera.

{% raw %}
Por ejemplo, considere la siguiente solicitud: `\"context\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Puede añadir la palabra "shoes" a un mensaje con este Liquid ``{{context.${product_name}}}``.
{% endraw %}

{% endtab %}

{% tab Event Properties %}
Las propiedades del evento son las propiedades establecidas por usted en los eventos personalizados y compras. Estos `event_properties` se pueden utilizar en campañas con entrega basada en acciones, así como en Canvas. 

En Canvas, las propiedades del evento personalizado y del evento de compra pueden utilizarse en Liquid en cualquier paso de Mensaje que siga a un paso de Rutas de acción. Utilice este Liquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} cuando haga referencia a estos `event_properties`. Estos eventos deben ser eventos personalizados o eventos de compra para ser utilizados de esta forma en el componente Mensaje.

En el primer paso de Mensaje que sigue a una Ruta de acción, puede utilizar `event_properties` relacionado con el evento al que se hace referencia en esa Ruta de acción. Puede tener otros pasos (que no sean otro paso de Rutas de acción o Mensaje) entre este paso de Rutas de acción y el paso de Mensaje. Tenga en cuenta que solo tendrá acceso a `event_properties` si su paso de Mensaje puede remontarse a una ruta que no sea Todos los demás en un paso de Ruta de acción.

{% endtab %}
{% endtabs %}

#### Paso 2.3: Editar conexiones

Para mover una conexión entre pasos, seleccione la flecha que conecta los dos componentes y seleccione un componente diferente. Para eliminar la conexión, seleccione la flecha seguida de **Cancelar conexión** en el pie de página del compositor de Canvas.

### Paso 3: Añadir un grupo de control

Puede añadir un grupo de control a su Canvas seleccionando el botón <i class="fas fa-plus-circle"></i> más para añadir una nueva variante. 

Braze realizará un seguimiento de las conversiones de los usuarios incluidos en el grupo de control, aunque no recibirán ningún mensaje. Para que la prueba sea precisa, realizaremos un seguimiento del número de conversiones de sus variantes y del grupo de control durante exactamente el mismo periodo de tiempo, como se muestra en la pantalla de selección del evento de conversión. 

Puede ajustar la distribución entre sus mensajes haciendo doble clic en las cabeceras de **Nombre de variante**.

En este ejemplo, tenemos nuestro Canvas dividido en dos variantes. La variante 1 cuenta con el 70 % de los usuarios. La segunda variante es un grupo de control con el 30 % restante de usuarios.

![Una variante de ejemplo en un Canvas de Braze, donde el 70 % va a la "Variante 1", que retrasa 1 día en el primer paso y luego envía un mensaje en el segundo paso. El otro 30 % va a un "Control" que no tiene ningún paso de seguimiento.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

#### Intelligent Selection para Canvas

Las funciones de Intelligent Selection ya están disponibles en los Canvas multivariantes. De forma similar a la característica [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) para campañas multivariantes, Intelligent Selection para Canvas analiza el rendimiento de cada variante de Canvas y ajusta el porcentaje de usuarios que se canalizan a través de cada variante. Esta distribución se basa en las métricas de rendimiento de cada variante para maximizar el número total esperado de conversiones.

Tenga en cuenta que los Canvas multivariantes no solo le permiten probar el texto, sino también el momento y los canales. Gracias a Intelligent Selection, puede probar los Canvas de forma más eficaz y confiar en que sus usuarios realizarán el mejor recorrido posible en Canvas.

![La opción "Intelligent Selection" está habilitada en la página "Editar distribución de variantes". A medida que analiza y optimiza el Canvas, muestra una barra horizontal a través de la página dividida en varias secciones, cada una de las cuales varía en color y tamaño. Esto es solo una representación visual y no se correlaciona con ningún análisis específico.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

Intelligent Selection para Canvas optimiza los resultados de su Canvas realizando ajustes graduales en tiempo real de la distribución de usuarios clasificados en cada variante. Cuando el algoritmo estadístico determine un ganador decisivo entre sus variantes, descartará las variantes de menor rendimiento y asignará a todos los futuros destinatarios elegibles del Canvas a las variantes ganadoras. 

Por esta razón, Intelligent Selection funciona mejor en Canvas en los que entran nuevos usuarios con frecuencia.

### Paso 4: Guardar y lanzar

Cuando haya terminado de crear su Canvas, seleccione **Lanzar Canvas** para guardarlo y lanzarlo. Una vez que haya lanzado su Canvas, podrá ver los análisis de su recorrido a medida que vayan llegando en la página **Detalles del Canvas**. 

También puede guardar su Canvas como borrador si necesita volver a él.

![Un ejemplo de Canvas en Braze.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
¿Necesita modificar su Canvas después del lanzamiento? ¡Puede hacerlo! Para más información, consulte [Editar Canvas después del lanzamiento]({{site.baseurl}}/post-launch_edits/).
{% endalert %}