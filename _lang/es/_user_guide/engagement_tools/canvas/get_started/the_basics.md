---
nav_title: Aspectos básicos del Canvas
article_title: Conceptos básicos sobre Canvas
page_order: 1
page_type: reference
description: "Este artículo de referencia trata de los aspectos básicos de Canvas, cubriendo varias preguntas que deberías hacerte al configurar tu primer Canvas."
tool: Canvas

---

# Aspectos básicos del Canvas

> Este artículo de referencia trata de los aspectos básicos de Canvas, cubriendo varias preguntas que deberías hacerte al configurar tu primer Canvas. También explicaremos las cinco W (qué, cuándo, quién, por qué y dónde) de la visualización y cómo esto puede dar forma y definir cómo puedes construir tu Canvas.

## Comprender la estructura de Canvas

Antes de empezar con los detalles más sutiles de la [configuración de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/), identifiquemos las partes clave que componen un Canvas.

{% tabs %}
  {% tab Canvas %}
  Canvas es una interfaz unificada donde los especialistas en marketing elaboran campañas con múltiples mensajes. Es un poco como una herramienta de programación visual, que te permite construir un recorrido del usuario coherente a partir de una serie de pasos.

  \![Un ejemplo de Canvas con un paso para la división de decisiones en dos recorridos de usuario diferentes dependiendo de si un usuario está habilitado para push.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %})

  {% endtab %}

  {% tab Journey %}

  Un recorrido, o comúnmente denominado recorrido del usuario, es la experiencia de un usuario individual dentro del Canvas.<br><br> \![Un gráfico con el recorrido del cliente para un nuevo usuario. Un usuario anónimo instala una aplicación, Kat crea una cuenta, Kat no abre la aplicación durante una semana, una notificación push hace que Kat vuelva a la aplicación, entonces Kat utiliza la aplicación con regularidad.]({% image_buster /assets/img_archive/Journey_2.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Canvas Builder %}
  El constructor de Canvas mapea los pasos a seguir para crear tu Canvas. Esto incluye aspectos básicos como poner nombre a tu Canvas y añadir equipos. Esencialmente, el constructor de Canvas es la configuración crucial necesaria antes de empezar a construir tu Canvas. Aquí puedes controlar la forma en que tus usuarios comienzan y completan su recorrido del cliente, con opciones para editar el [horario de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule), la [audiencia objetivo]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2c-set-your-target-entry-audience) y la [configuración de envío]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2d-select-your-send-settings).<br><br> \![El constructor de Canvas en la sección Básicos para un Canvas llamado "Nuevo Canvas".]({% image_buster /assets/img_archive/canvas_flow_entry_wizard.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Variants %}
  Una variante es el camino que sigue cada cliente en su recorrido. Canvas admite hasta ocho variantes con un grupo de control. Tú controlas qué segmento de tu audiencia seguirá cada variante.<br><br> \![Seleccionando el botón "Añadir variante".]({% image_buster /assets/img/canvas_intro/add_canvas_variant.gif %})

  {% endtab %}

  {% tab Steps %}
  Un paso en Canvas es un punto de decisión de marketing: "si esto, entonces aquello". Aprovecha [los componentes de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/#about-canvas-components) para construir los pasos de un recorrido de usuario.<br><br> \![Ejemplo de añadir un paso en Canvas.]({% image_buster /assets/img/canvas_intro/add_canvas_step.gif %}) <br><br> Cuando un usuario entra en un Canvas, empieza por el primer paso. Cada paso tiene unas condiciones que determinan si un usuario puede pasar al siguiente. En un paso, puedes desencadenar o programar la entrega, afinar la orientación añadiendo filtros o marcando eventos de excepción, y especificar diferentes canales como notificaciones push o eventos webhook. En Canvas, los pasos se producen en una secuencia, lo que significa que el primer paso se produce antes de que pueda producirse el segundo. Supongamos que tenemos un Canvas con los siguientes pasos: Retrasa el paso A con un retraso de 24 horas, Mensajea el paso A con un mensaje push y Mensajea el paso B con un mensaje dentro de la aplicación. El usuario A es retenido en un retraso de 24 horas, después de 24 horas, recibirá un mensaje push y, a continuación, un mensaje dentro de la aplicación.

  {% endtab %}
{% endtabs %}

## Construir el recorrido del cliente

Utilizar las cinco W (qué, cuándo, quién, por qué y dónde) de la visualización puede ayudarte a identificar tus estrategias de interacción con los clientes para crear un recorrido de mensajes personalizado para cada uno de tus usuarios.

### El "qué": Ponle nombre a tu Canvas

> ¿Qué intentas ayudar al usuario a hacer o entender?

Nunca subestimes el poder del nombre. Braze está hecho para la colaboración, así que éste es un buen momento para poner los cimientos sobre cómo comunicarás los objetivos a tu equipo.

Puedes añadir etiquetas y nombrar los pasos y variantes en un Canvas. Para saber más sobre el recorrido del cliente, consulta nuestro curso de Braze Learning sobre [el mapeado del ciclo de vida del usuario](https://learning.braze.com/mapping-customer-lifecycles).

### El "por qué": Identificar eventos de conversión

> Partiendo del "qué", ¿por qué estás construyendo este Canvas? 

Siempre es importante tener un objetivo definido en mente y Canvas te ayuda a comprender cómo estás rindiendo con respecto a KPI como la interacción con los clientes, las compras y los eventos personalizados.

Seleccionar al menos un [evento de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) te permitirá comprender cómo optimizar el rendimiento dentro del Canvas. Y si tu Canvas tiene múltiples variantes o un grupo de control, Braze utilizará el evento de conversión para determinar la mejor variante para alcanzar este objetivo.

* **Comienza la sesión**: Quiero que mis usuarios vuelvan e interactúen con la aplicación.
* **Haz la compra**: Quiero que mis usuarios compren.
* **Realiza un evento personalizado**: Quiero que mis usuarios realicen una acción específica que estoy siguiendo como un evento personalizado.
* **Actualiza la aplicación:** Quiero que mis usuarios actualicen la versión de su aplicación.

### El "cuándo": Crear condiciones de partida

> ¿Cuándo iniciará el usuario esta experiencia?

Tu respuesta determinará los detalles de cuándo y cómo se entregará tu Canvas a tu cliente. Los usuarios pueden entrar en tu Canvas de una de estas dos formas: desencadenantes programados o basados en acciones.

{% alert tip %}
Consulta [Funcionalidades basadas en el tiempo]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/delivery_types/) para Canvas para conocer más estrategias y respuestas a preguntas habituales.
{% endalert %}

La entrega programada te permite enviar un Canvas inmediatamente a tu audiencia objetivo. También puedes hacer que se envíe regularmente, o programarlo para un momento concreto en el futuro. Las Lonas basadas en la acción responden a comportamientos del cliente específicos a medida que se producen. Por ejemplo, un desencadenante basado en una acción puede incluir abrir una aplicación, realizar una compra, interactuar con otra campaña o desencadenar cualquier evento personalizado. En el momento en que se produce la acción, puedes hacer que el Canvas se envíe a tus usuarios.

### El "quién": Selecciona una audiencia

> ¿A quién quieres llegar? 

Para definir tu "quién", puedes utilizar segmentos predefinidos disponibles en Canvas. También puedes añadir más filtros para centrarte aún más en conectar con tu audiencia objetivo. Después de crear estos segmentos, sólo los usuarios que coincidan con los criterios de la audiencia objetivo podrán entrar en el viaje de Canvas, lo que dará lugar a una experiencia más personalizada. Consulta esta tabla para ver los filtros disponibles y cómo segmentan a tus usuarios para adaptarse a tu caso de uso.

| Filtrar              | Descripción                                                                                         |
|---------------------|-----------------------------------------------------------------------------------------------------|
| Datos personalizados         | Segmenta a los usuarios en función de los eventos y atributos que definas. Puedes utilizar características específicas de tu producto. |
| Actividad del usuario       | Segmenta a los clientes en función de sus acciones y compras.                                             |
| Reorientación         | Segmenta a los clientes que hayan enviado, recibido o interactuado con Lienzos anteriores.               |
| Actividad de marketing  | Segmenta a los clientes basándote en comportamientos universales como la última interacción.                         |
| Atributos del usuario     | Segmenta a los clientes por sus atributos y características constantes.                                 |
| Atribución de instalación | Segmenta a los clientes por su primera fuente, grupo de anuncios, campaña o anuncio.                                 |

### El "dónde": Encontrar mi audiencia

> ¿Dónde puedo llegar mejor a mi audiencia? 

Aquí es donde determinamos qué canales de mensajería tienen más sentido para el recorrido de tu usuario. Lo ideal sería llegar a tus usuarios allí donde son más accesibles. Teniendo esto en cuenta, puedes utilizar cualquiera de los siguientes canales con Canvas:
* [Correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)
* [Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)
* [Mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)
* [Tarjetas de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)
* [SMS o MMS]({{site.baseurl}}/about_sms/)
* [Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)

### El "cómo": Construye la experiencia completa

> ¿Cómo construyo mi viaje en Canvas después de identificar las cinco W?

El "cómo" resume colectivamente cómo crearás tu Canvas y cómo llegarás a tus usuarios con tu mensaje. Por ejemplo, para que un mensaje sea eficaz, debes optimizar el horario de tu mensajería con respecto a las zonas horarias de tus diferentes usuarios.

Responder al "cómo" también determina la cadencia de envío de un Canvas a tu audiencia (por ejemplo, una vez a la semana o cada dos semanas), y qué canales de mensajería aprovechar para cada Canvas que construyas, tal y como se describe con el "dónde".

## Casos de uso: Flujo de incorporación de clientes

Por ejemplo, supongamos que eres especialista en marketing de MovieCanon, una empresa de servicios de streaming online, y te encargas de crear un flujo de incorporación para los nuevos usuarios de tu aplicación. Haciendo referencia a las cinco W, podríamos construir el Canvas de la siguiente manera.

* **Qué**: El nombre de nuestro Canvas será "Nuevo viaje de incorporación".
* **¿Por qué**? El objetivo de nuestro Canvas es dar la bienvenida a nuestros usuarios y hacer que sigan interactuando con la aplicación.
* **Cuándo**: Después de que un usuario abra la aplicación por primera vez, queremos enviarle un correo electrónico para darle la bienvenida. 
* **Quién**: Nos dirigimos a nuevos usuarios que utilizan nuestra aplicación por primera vez.
* **Dónde**: Confiamos en poder llegar a los nuevos usuarios a través de su correo electrónico, que es como hemos hecho toda nuestra mensajería anterior.
* **Cómo**: Queremos establecer un retraso de un día para no abrumar a nuestros nuevos usuarios con notificaciones. Después de este retraso, enviaremos un correo electrónico con una lista de las películas y programas de televisión más populares para animarles a seguir utilizando la aplicación.

## Consejos generales

### Determina cuándo y cómo utilizar pasos y variantes

Cada Canvas debe tener al menos una variante y al menos un paso. A partir de ahí, el cielo es el límite, así que ¿cómo decides la forma de tu Canvas? Aquí es donde entran en juego tus objetivos, datos e hipótesis. La lluvia de ideas sobre "cómo" y "dónde" te ayudará a mapear la forma y estructura adecuadas de tu Canvas.

### Trabaja hacia atrás

Algunos objetivos tienen subobjetivos más pequeños. Por ejemplo, si tu objetivo es convertir a un usuario gratuito en suscriptor, puede que necesites una página en la que se describan tus servicios de suscripción. Un visitante puede necesitar ver las opciones antes de comprar. Puedes centrar tus esfuerzos de mensajería en mostrarles esta página antes de la página de pago. Trabajar hacia atrás para comprender el recorrido que debe hacer un cliente para llegar a tu objetivo es clave para guiarle hasta la conversión.

### Mezcla tu mensajería

¿Has realizado alguna campaña similar en el pasado? ¿O hay alguno en marcha? Intenta utilizar ese único mensaje y añadirle más personalización. Prueba a filtrar o añade un mensaje de seguimiento. A medida que vayas combinando tus técnicas de mensajería, controla tu rendimiento y sigue optimizando mediante cambios graduales.
