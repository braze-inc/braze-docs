---
nav_title: Fundamentos de Canvas
article_title: Fundamentos de Canvas
page_order: 1
page_type: reference
description: "Este artículo de referencia cubre los aspectos básicos de Canvas, cubriendo varias preguntas que deberías hacerte mientras configuras tu primer Canvas."
tool: Canvas

---

# Fundamentos del lienzo

> Este artículo de referencia cubre los aspectos básicos de Canvas, cubriendo varias preguntas que deberías hacerte mientras configuras tu primer Canvas. También explicaremos las cinco W (qué, cuándo, quién, por qué y dónde) de la visualización y cómo esto puede dar forma y definir el modo en que puedes construir tu Canvas.

## Comprender la estructura de Canvas

Antes de empezar con los detalles más sutiles de la [configuración de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/), identifiquemos las partes clave que componen un Canvas.

{% tabs %}
  {% tab Canvas %}
  Canvas es una interfaz unificada en la que los profesionales del marketing elaboran campañas con múltiples mensajes. Es un poco como una herramienta de programación visual, que permite construir un recorrido de usuario coherente a partir de una serie de pasos.

  ![Un ejemplo de Canvas con un paso para la división de decisiones en dos recorridos de usuario diferentes dependiendo de si un usuario está habilitado para push.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %})

  {% endtab %}

  {% tab Recorrido %}

  Un recorrido, o comúnmente denominado recorrido del usuario, es la experiencia de un usuario individual dentro del Canvas.<br><br> ![Un gráfico con el recorrido del cliente para un nuevo usuario. Un usuario anónimo instala una aplicación, Kat crea una cuenta, Kat no abre la aplicación durante una semana, una notificación push hace que Kat vuelva a la aplicación, entonces Kat utiliza la aplicación con regularidad.]({% image_buster /assets/img_archive/Journey_2.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Generador de Canvas %}
  El constructor del lienzo le indica los pasos que debe seguir para crear su lienzo. Esto incluye aspectos básicos como poner nombre a tu Canvas y añadir equipos. Esencialmente, el Canvas Builder es la configuración crucial requerida antes de empezar a construir tu Canvas. Aquí puede controlar la forma en que sus usuarios inician y completan su recorrido como clientes, con opciones para editar el [calendario de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule), el [público objetivo]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2c-set-your-target-entry-audience) y [los ajustes de envío]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2d-select-your-send-settings).<br><br> ![El constructor de Canvas en la sección Básicos para un Canvas llamado "Nuevo Canvas".]({% image_buster /assets/img_archive/canvas_flow_entry_wizard.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Variantes %}
  Una variante es el camino que sigue cada cliente en su recorrido. Canvas admite hasta ocho variantes con un grupo de control. Usted controla qué segmento de su audiencia seguirá cada variante.<br><br> ![Selecciona el botón "Añadir variante".]({% image_buster /assets/img/canvas_intro/add_canvas_variant.gif %})

  {% endtab %}

  {% tab Pasos %}
  Un paso en Canvas es un punto de decisión de marketing: "si esto, entonces aquello". Aproveche los [componentes de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/#about-canvas-components) para construir los pasos de un recorrido de usuario.<br><br> ![Ejemplo de añadir un paso en Canvas.]({% image_buster /assets/img/canvas_intro/add_canvas_step.gif %}) <br><br> Cuando un usuario entra en un Canvas, empieza por el primer paso. Cada paso tiene unas condiciones que determinan si un usuario puede pasar al siguiente. En un paso, puedes desencadenar o programar la entrega, afinar la orientación añadiendo filtros o marcando eventos de excepción, y especificar diferentes canales como notificaciones push o eventos webhook. En Canvas, los pasos se producen en una secuencia, lo que significa que el primer paso se produce antes de que pueda producirse el segundo. Supongamos que tenemos un Canvas con los siguientes pasos: Retrasa el paso A con un retraso de 24 horas, Mensajea el paso A con un mensaje push y Mensajea el paso B con un mensaje dentro de la aplicación. El usuario A es retenido en un retraso de 24 horas, después de 24 horas, recibirá un mensaje push y, a continuación, un mensaje dentro de la aplicación.

  {% endtab %}
{% endtabs %}

## Construir el recorrido del cliente

Utilizar las cinco W (qué, cuándo, quién, por qué y dónde) de la visualización puede ayudarle a identificar sus estrategias de captación de clientes para crear un viaje de mensajes personalizado para cada uno de sus usuarios.

### El "qué": Ponga nombre a su lienzo

> ¿Qué intenta ayudar al usuario a hacer o entender?

Nunca subestimes el poder del nombre. Braze se ha creado para la colaboración, así que es un buen momento para poner los cimientos sobre cómo comunicarás los objetivos a tu equipo.

Puede añadir etiquetas y nombrar los pasos y variantes en un Lienzo. Para obtener más información sobre el recorrido del cliente, consulte nuestro curso de Braze Learning sobre [el trazado del ciclo de vida del usuario](https://learning.braze.com/mapping-customer-lifecycles).

### El "por qué": Identificar eventos de conversión

> Partiendo del "qué", ¿por qué construyes este lienzo? 

Siempre es importante tener un objetivo definido en mente y Canvas te ayuda a entender cómo te estás desempeñando con respecto a los KPI, como la participación en la sesión, las compras y los eventos personalizados.

La selección de al menos un [evento de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) le permitirá comprender cómo optimizar el rendimiento dentro del Canvas. Y si su Canvas tiene múltiples variantes o un grupo de control, Braze utilizará el evento de conversión para determinar la mejor variación para alcanzar este objetivo.

* **Inicia sesión**: Quiero que mis usuarios vuelvan y se interesen por la aplicación.
* **Hace una compra**: Quiero que mis usuarios compren.
* **Realizar evento personalizado**: Quiero que mis usuarios realicen una acción específica que estoy rastreando como un evento personalizado.
* **Actualiza la aplicación:** Quiero que mis usuarios actualicen la versión de su aplicación.

### El "cuándo": Crear condiciones de partida

> ¿Cuándo iniciará el usuario esta experiencia?

Su respuesta determinará los detalles de cuándo y cómo se entregará su lienzo a su cliente. Los usuarios pueden entrar en tu Canvas de dos maneras: activadores programados o basados en acciones.

{% alert tip %}
Consulte [Funcionalidades basadas en el tiempo]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/delivery_types/) para Canvas para obtener más estrategias y respuestas a preguntas comunes.
{% endalert %}

La entrega programada le permite enviar un Canvas inmediatamente a su público objetivo. También puede enviarla periódicamente o programarla para un momento determinado en el futuro. Los lienzos basados en acciones responden a comportamientos específicos de los clientes a medida que se producen. Por ejemplo, un activador basado en una acción puede incluir la apertura de una aplicación, la realización de una compra, la interacción con otra campaña o la activación de cualquier evento personalizado. En el momento en que se produce la acción, puede hacer que el Canvas se envíe a sus usuarios.

### El "quién": Seleccionar un público

> ¿A quién quieres llegar? 

Para definir su "quién", puede utilizar segmentos predefinidos disponibles en Canvas. También puede añadir más filtros para centrarse aún más en conectar con su público objetivo. Una vez creados estos segmentos, sólo los usuarios que coincidan con los criterios del público objetivo podrán acceder al recorrido de Canvas, lo que dará lugar a una experiencia más personalizada. Consulte esta tabla para ver los filtros disponibles y cómo segmentan a sus usuarios para adaptarse a su caso de uso.

| Filtro              | Descripción                                                                                         |
|---------------------|-----------------------------------------------------------------------------------------------------|
| Datos personalizados         | Segmente a los usuarios en función de los eventos y atributos que defina. Puede utilizar características específicas de su producto. |
| Actividad del usuario       | Segmente a los clientes en función de sus acciones y compras.                                             |
| Reorientación         | Segmente a los clientes que hayan enviado, recibido o interactuado con lienzos anteriores.               |
| Actividad de marketing  | Segmente a los clientes en función de comportamientos universales como el último compromiso.                         |
| Atributos del usuario     | Segmentar a los clientes por sus atributos y características constantes.                                 |
| Atribución de instalación | Segmente a los clientes por su primera fuente, grupo de anuncios, campaña o anuncio.                                 |

### El "dónde": Encontrar mi público

> ¿Dónde puedo llegar mejor a mi público? 

Aquí es donde determinamos qué canales de mensajería tienen más sentido para el recorrido de tu usuario. Lo ideal sería llegar a los usuarios allí donde son más accesibles. Teniendo esto en cuenta, puedes utilizar cualquiera de los siguientes canales con Canvas:
* [Correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)
* [Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)
* [Mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)
* [Tarjetas de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)
* [SMS o MMS]({{site.baseurl}}/about_sms/)
* [Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)

### El "cómo": Construir la experiencia completa

> ¿Cómo construyo mi viaje en Canvas después de identificar las cinco W?

El "cómo" resume colectivamente cómo crearás tu Canvas y cómo llegarás a tus usuarios con tu mensaje. Por ejemplo, para que un mensaje sea eficaz, debe optimizar el horario de sus mensajes en función de las zonas horarias de los distintos usuarios.

Responder al "cómo" también determina la cadencia para enviar un Canvas a su audiencia (por ejemplo, una vez a la semana o cada dos semanas), y qué canales de mensajería aprovechar para cada Canvas que construya como se describe con el "dónde".

## Caso de uso: Flujo de incorporación de clientes

Por ejemplo, digamos que usted es un vendedor para MovieCanon, una empresa de servicios de streaming en línea, y está a cargo de la creación de un flujo de incorporación para los nuevos usuarios de su aplicación. Haciendo referencia a las cinco W, podríamos construir el Canvas de la siguiente manera.

* **Qué (What)**: El nombre de nuestro Canvas será "Nuevo recorrido de incorporación".
* **¿Por qué**? El objetivo de nuestro Canvas es dar la bienvenida a nuestros usuarios y hacer que sigan interactuando con la aplicación.
* **Cuando**: Cuando un usuario abre la aplicación por primera vez, queremos enviarle un correo electrónico de bienvenida. 
* **Quién**: Nos dirigimos a nuevos usuarios que utilizan nuestra aplicación por primera vez.
* **Dónde**: Confiamos en poder llegar a los nuevos usuarios a través de su correo electrónico, que es como hemos hecho todos nuestros mensajes anteriores.
* **Cómo**: Queremos establecer un retraso de un día para no abrumar a nuestros nuevos usuarios con notificaciones. Después de este retraso, enviaremos un correo electrónico con una lista de las películas y programas de televisión más populares para animarles a seguir utilizando la aplicación.

## Consejos generales

### Determinar cuándo y cómo utilizar pasos y variantes

Cada Canvas debe tener al menos una variante y al menos un paso. A partir de ahí, el cielo es el límite, así que ¿cómo decidir la forma de su lienzo? Aquí es donde entran en juego sus objetivos, datos e hipótesis. La lluvia de ideas sobre "cómo" y "dónde" le ayudará a trazar la forma y la estructura adecuadas de su lienzo.

### Trabajar hacia atrás

Algunos objetivos tienen subobjetivos más pequeños. Por ejemplo, si su objetivo es convertir a un usuario gratuito en suscriptor, es posible que necesite una página en la que se describan sus servicios de suscripción. Un visitante puede necesitar ver las opciones antes de comprar. Puede centrar sus esfuerzos de mensajería en mostrarles esta página antes de una página de pago. Trabajar hacia atrás para comprender el recorrido que debe realizar un cliente para llegar a su objetivo es clave para guiarle hasta la conversión.

### Combina tu mensajería

¿Ha realizado alguna campaña similar en el pasado? ¿O hay alguno en marcha? Intenta utilizar ese único mensaje y añadirle más personalización. Prueba un filtro nuevo o añade un mensaje de seguimiento. A medida que vayas combinando tus técnicas de mensajería, controla tu rendimiento y sigue optimizando mediante cambios graduales.
