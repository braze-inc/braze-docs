---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre Canvas
page_order: 8
alias: "/canvas_v2_101/"
description: "Este artículo responde a las preguntas más frecuentes sobre Canvas."
tool: Canvas

---

# Preguntas más frecuentes

> Este artículo ofrece respuestas a algunas preguntas frecuentes sobre Canvas.

### ¿Cuántos pasos puedo incluir en un Canvas?

Puedes añadir hasta 200 pasos en un Canvas.

### ¿Qué ocurre si la audiencia y el tiempo de envío son idénticos para un Canvas que tiene una variante, pero múltiples ramas?

Ponemos en cola un trabajo para cada paso: se ejecutan más o menos al mismo tiempo y uno de ellos "gana". En la práctica, la distribución puede ser algo uniforme, pero es probable que tenga al menos un ligero sesgo hacia el paso que se creó primero. 

Además, no podemos garantizar cómo será exactamente esa distribución. Si deseas una división uniforme, añade un filtro [Número de contenedor aleatorio]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/).

### ¿Puedo lanzar un Canvas con pasos desconectados?

Sí. También puedes guardar Canvas después del lanzamiento con pasos desconectados. 

### ¿Adónde van los usuarios cuando llegan a un paso desconectado?

Si un usuario está en un paso desconectado de tu flujo de trabajo Canvas, avanzará al paso siguiente si lo hay, y la configuración del paso dictará cómo debe avanzar el usuario. El objetivo es permitir que los usuarios puedan realizar cambios en los pasos sin tener que conectarlos directamente con el resto del Canvas. Esto también te da cierto margen para hacer pruebas antes de pasar a producción de inmediato, lo que te permite guardar un borrador.

Recomendamos comprobar la vista de análisis de usuarios pendientes en un paso de Canvas antes de desconectar un paso.

### ¿Qué ocurre cuando se detiene un Canvas?

Cuando detienes un Canvas, se aplica lo siguiente:

- Se impedirá a los usuarios entrar en el Canvas.
- No se enviarán más mensajes, sin importar dónde se encuentre el usuario en el flujo.
- **Excepción:** Los Canvas con correos electrónicos no se detendrán inmediatamente. Después de que las solicitudes de envío vayan a SendGrid, no hay nada que podamos hacer para evitar que se entreguen al usuario.

### ¿Debo crear un solo Canvas o Canvas separados por ciclo de vida del usuario?

Dependiendo de lo que quieras conseguir con tu Canvas, puede que necesites diferentes enfoques en la forma de construir tu recorrido del usuario. La flexibilidad de Canvas te permite mapear recorridos de usuario para cualquier etapa del ciclo de vida del usuario. Echa un vistazo a nuestras [plantillas de Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates) para ver varios ejemplos de enfoques simplificados para crear recorridos de usuario eficaces.

### ¿Cuándo se envían los mensajes dentro de la aplicación en Canvas?

Los mensajes dentro de la aplicación se envían al iniciar la siguiente sesión. Esto significa que si el usuario entra en el paso en Canvas antes de que se detenga el Canvas, seguirá recibiendo el mensaje dentro de la aplicación al iniciar su próxima sesión, siempre que el mensaje dentro de la aplicación no haya caducado todavía.

Es posible que un usuario inicie una sesión antes de que se detenga el Canvas, pero que no se le muestre el mensaje dentro de la aplicación inmediatamente. Esto puede ocurrir si el mensaje dentro de la aplicación se desencadena por un evento personalizado o se retrasa. Esto significa que es posible que un usuario registre una impresión de mensaje dentro de la aplicación y "reciba" el mensaje dentro de la aplicación después de que se detenga el Canvas. Sin embargo, el usuario tendría que haber iniciado la sesión antes de que se detuviera el Canvas, pero **después de** haber recibido el paso en Canvas.

{% alert note %}
Detener un Canvas no hará que los usuarios que están esperando recibir mensajes salgan del recorrido del usuario. Si vuelves a habilitar el Canvas y los usuarios siguen esperando el mensaje, lo recibirán (a menos que haya pasado el tiempo en que se les debería haber enviado el mensaje, en cuyo caso no lo recibirán).
{% endalert %}

### ¿Cuándo se desencadena un evento de excepción?

Los eventos de excepción solo se desencadenan mientras el usuario está esperando recibir el componente Canvas al que está asociado. Si un usuario realiza una acción por adelantado, el evento de excepción no se desencadenará. Si deseas excluir a los usuarios que hayan realizado un determinado evento con anterioridad, utiliza [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) en su lugar.

### ¿Cómo afecta la edición de un Canvas a los usuarios que ya están en él?

Si editas algunos de los pasos de un Canvas de varios pasos, los usuarios que ya estaban en la audiencia pero no han recibido los pasos recibirán la versión actualizada del mensaje. Ten en cuenta que esto solo ocurrirá si aún no han sido evaluados para el paso.

Para más información sobre lo que puedes editar después del lanzamiento, consulta [Cambiar tu Canvas después del lanzamiento]({{site.baseurl}}/post-launch_edits/).

### ¿Cómo se realiza el seguimiento de las conversiones de los usuarios en un Canvas?

Un usuario solo puede convertir una vez por entrada de Canvas. Las conversiones se asignan al mensaje más reciente recibido por el usuario para esa entrada. El bloque de resumen al principio de un Canvas refleja todas las conversiones realizadas por los usuarios dentro de esa ruta, hayan recibido o no un mensaje. Cada paso posterior solo mostrará las conversiones que se produjeron mientras ese era el paso más reciente recibido por el usuario.

{% alert note %}
Cuando un usuario vuelve a entrar en un Canvas, los eventos de conversión solo se rastrean para la entrada más reciente. Los eventos de conversión no se registran para las entradas anteriores, aunque el evento de conversión se rellene de forma retroactiva.
{% endalert %}

{% details Ampliar para ver ejemplos %}

**Ejemplo 1**

Hay una ruta de Canvas con 10 notificaciones push y el evento de conversión es "session start" (inicio de sesión) ("Opens App"):

- El usuario A abre la aplicación después de entrar pero antes de recibir el primer mensaje.
- El usuario B abre la aplicación después de cada notificación push.

**Resultado:** El resumen mostrará dos conversiones, mientras que los pasos individuales mostrarán una conversión de uno en el primer paso y cero en todos los pasos siguientes.

{% alert note %}
Si las horas tranquilas están activas cuando se produce el evento de conversión, se aplican las mismas reglas.
{% endalert %}

**Ejemplo 2**

Hay un Canvas de un solo paso con las horas tranquilas habilitadas:

1. El usuario entra en el Canvas.
2. El primer paso no tiene retraso, pero está dentro de las horas tranquilas establecidas, por lo que el mensaje se suprime.
3. El usuario realiza el evento de conversión.

**Resultado:** El usuario contará como convertido en la variante general de Canvas, pero no en el paso, ya que no recibió el paso.

{% enddetails %}

### ¿Cuál es la diferencia entre los distintos tipos de tasa de conversión?

- El total de conversiones en Canvas refleja cuántos usuarios únicos completaron un evento de conversión, no cuántas conversiones completó cada uno. 
- La tasa de conversión de variante o bloque de resumen al principio de un Canvas refleja todas las conversiones realizadas por los usuarios dentro de esa ruta, hayan recibido o no un mensaje, como un total agregado. 
- La tasa de conversión de pasos refleja cuántas personas recibieron ese paso del mensaje y completaron alguno de los eventos de conversión descritos.

### ¿Cuál es la diferencia entre un componente y un paso?

Un [componente]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) es una parte individual de tu Canvas que puedes utilizar para determinar la eficacia de tu Canvas. Los componentes pueden incluir acciones como dividir el recorrido del usuario, añadir un retraso e incluso probar varias rutas de Canvas. Un paso en Canvas se refiere al recorrido personalizado del usuario en tus ramas de Canvas. Esencialmente, tu Canvas está formado por componentes individuales que crean pasos para el recorrido de usuario.

### ¿Cómo puedo ver los análisis de cada uno de mis componentes de Canvas?

Para ver los análisis de un componente de Canvas, ve a tu Canvas y desplázate hacia abajo por la página **Detalles del Canvas**. Aquí puedes ver los análisis de cada componente. Consulta [Análisis de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para obtener más información.

### Si nos fijamos en el número de usuarios únicos, ¿es más preciso el análisis de Canvas o el segmentador?

El segmentador es una estadística más precisa para los datos de usuario único frente a las estadísticas de Canvas o de campaña. Esto se debe a que las estadísticas de Canvas y de campaña son números que Braze incrementa cuando ocurre algo, lo que significa que hay variables que podrían hacer que este número fuera diferente al del segmentador. Por ejemplo, los usuarios pueden convertir más de una vez en un Canvas o una campaña.

### ¿Por qué el número de usuarios que entran en un Canvas no coincide con el número esperado?

El número de usuarios que entran en un Canvas puede diferir del número esperado debido a cómo se evalúan las audiencias y los desencadenantes. En Braze, una audiencia se evalúa antes del desencadenante (a menos que se utilice un desencadenante de [cambio de atributo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value)). Esto hará que los usuarios abandonen el Canvas si no forman parte de tu audiencia seleccionada antes de que se evalúe cualquier acción desencadenante.

### ¿Qué ocurre con los usuarios anónimos durante su recorrido por Canvas?

Aunque los usuarios anónimos pueden entrar y salir de Canvas, sus acciones no se asocian a un perfil de usuario específico hasta que se identifican, por lo que es posible que sus interacciones no se rastreen completamente en tus análisis. Puedes utilizar el [Generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/) para generar un informe de estas métricas.

### ¿Por qué mi tasa de conversión de pasos de Canvas no es igual a mi tasa de conversión total de variantes de Canvas?

Es habitual que el total de conversiones de una variante de Canvas sea mayor que la suma del total de sus pasos. Esto ocurre porque un usuario puede realizar un evento de conversión para una variante tan pronto como entra en ella. Sin embargo, este mismo evento de conversión no cuenta para un paso de Canvas. Por lo tanto, cualquier usuario que entre en el Canvas y realice el evento de conversión antes de recibir el primer paso de Canvas se contabilizará en el total de conversiones de la variante, pero no en el total de pasos. Lo mismo ocurre con un usuario que entra en el Canvas pero sale de él antes de recibir ningún paso.

### ¿Cómo se evalúan las audiencias de Canvas? 

Por defecto, los filtros y segmentos de los pasos completos del Canvas se comprueban en el momento del envío. El paso para la división de decisiones realiza una evaluación justo después de recibir un paso anterior (o antes de un retraso).

{% alert tip %}
Para obtener más ayuda con la solución de problemas de Canvas, asegúrate de ponerte en contacto con soporte de Braze en los 30 días siguientes a la aparición del problema, ya que solo disponemos de los registros de diagnóstico de los últimos 30 días.
{% endalert %}

### ¿Cuál es la diferencia entre "No ha entrado en la variación Canvas" y "No está en el grupo de control Canvas"?

Consulta las definiciones completas de los filtros en [Filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

#### No ha entrado en la variación Canvas

El usuario nunca entró en una ruta de variación de un Canvas concreto. Se incluyen todos los usuarios que no están en el grupo de control, independientemente de si han entrado o no en el Canvas. Esto incluye a los usuarios que entraron en otra variación y a los usuarios que no han entrado en ninguna variación. 

#### No está en el grupo de control de Canvas

El usuario entró en el Canvas, pero no está en el grupo de control y, en consecuencia, recibió una variación. Esto solo incluye a los usuarios que entraron en el Canvas.

Ten en cuenta que la asignación de variaciones se produce a la entrada en Canvas. Si un usuario no ha entrado en un Canvas, no se le asignará ninguna variante. En otras palabras, no estarán en el grupo de control ni en una variante.

{% details Ampliar para ver las preguntas frecuentes del editor original de Canvas %}

### ¿Cómo convierto un Canvas existente del editor original al editor actual?

Puedes [clonar tu Canvas]({{site.baseurl}}/cloning_canvases/). Esto crea una copia de tu Canvas original en el flujo de trabajo Canvas más actual.

### ¿Cuáles son las principales diferencias entre los editores de Canvas actual y original?

#### Barra de herramientas del componente Canvas

Anteriormente, con el editor Canvas original, se añadía por defecto un paso completo cada vez que se creaba cualquier paso en el recorrido del usuario. Estos pasos completos se sustituyen por diferentes componentes de Canvas, lo que te proporciona la ventaja de una mayor visibilidad y personalización para tu experiencia de edición. Puedes ver inmediatamente todos tus componentes de Canvas desde la barra de herramientas de pasos de Canvas.

#### Comportamiento de los pasos

Anteriormente, cada paso completo incluía información como ajustes de retraso y programación, eventos de excepción, filtros de audiencia, configuración de mensajes y opciones de avance de mensajes, todo en un solo componente. Se trata de configuraciones independientes en el editor actual para que tu experiencia de construcción en Canvas sea más personalizable, e introduce algunas diferencias en la funcionalidad.

#### Avance del componente de mensajes

[Los componentes del mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) hacen avanzar a todos los usuarios que entran en el paso. No es necesario especificar el comportamiento de avance de los mensajes, lo que simplifica la configuración del paso general. Si deseas implementar la opción **Avanzar cuando se envíe el mensaje**, añade una ruta de audiencia independiente para filtrar los usuarios que no hayan recibido el paso anterior.  

#### Comportamiento del retraso "en"

[Los componentes de retraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) esperarán todo el tiempo de retraso antes de pasar al siguiente paso. 

Digamos que el 12 de abril tenemos un componente de retraso en el que el retraso está configurado para enviar a tu usuario al siguiente paso en un día a las 2 de la tarde. Un usuario entra en el componente a las 14:01 del 13 de abril. 
- En el flujo de trabajo original, el usuario pasaría al siguiente paso a las 14:00 del 14 de abril, es decir, menos de un día después de la hora de entrada. 
- En el editor actual, el usuario pasaría al siguiente paso a las 14:00 del 15 de abril. Ten en cuenta que se trata de la misma hora, pero a más de un día de la hora de entrada. 

#### Comportamiento de Intelligent Timing

Como [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) se almacena en el componente de mensaje, los retrasos se aplicarán antes de los cálculos de Intelligent Timing. Esto significa que, dependiendo del momento en que un usuario entre en el componente, puede recibir el mensaje más tarde de lo que lo haría en un Canvas construido con el flujo de trabajo original de Canvas.

Supongamos que el retraso es de 2 días, Intelligent Timing está activado y ha determinado que la mejor hora para enviar el mensaje son las 14:00. Un usuario entra en el paso de retraso a las 14:01.
- **Flujo de trabajo actual:** El retraso tardará 48 horas en transcurrir, por lo que el usuario recibirá el mensaje el tercer día a las 14:00.
- **Flujo de trabajo original:** El usuario recibe el mensaje el segundo día a las 14:00.

Ten en cuenta que si Intelligent Timing está activado, el mensaje se enviará en un plazo de 24 horas desde que el usuario entre en el componente de mensaje a la hora inteligente identificada (incluso si no interviene ningún componente de retraso).

#### Eventos de excepción

##### Horas tranquilas

El evento de excepción se aplica mediante rutas de acción, que son independientes de los pasos de mensaje. Las horas tranquilas se aplican en el componente de mensaje. Esto significa que si un usuario ya ha pasado por la ruta de acción (y no ha sido excluido con el evento de excepción), luego se encuentra con horas tranquilas cuando llega al componente de mensaje, y tiene configurado su Canvas de forma que el mensaje se reenvíe después del periodo de horas tranquilas, el evento de excepción ya no se aplicará. Ten en cuenta que este caso de uso no es habitual.

Para los segmentos y filtros, el paso de mensaje tiene validaciones de entrega que permiten a los usuarios configurar segmentos y filtros adicionales que se validan en el momento del envío. De este modo se evita el mencionado caso límite de las horas tranquilas.

##### Configuración de programación "En" o "En el siguiente"

Los eventos de excepción se crean utilizando rutas de acción. Las rutas de acción solo admiten "después de una ventana de tiempo X" y no "en un tiempo X" o "en el próximo tiempo X".

{% enddetails %}

### ¿Qué debo incluir al enviar un ticket de soporte por un error de "Tiempo de espera agotado"?

Si encuentras un error de "Tiempo de espera agotado" al editar un Canvas y necesitas ponerte en contacto con [soporte de Braze]({{site.baseurl}}/braze_support/), incluye la siguiente información para ayudar a acelerar la resolución:

- **Grabación de pantalla:** Una grabación de los pasos que seguiste antes de ver el error, incluyendo cualquier transición de página.
- **Marca de tiempo y zona horaria:** La hora exacta en que ocurrió el error y tu zona horaria.
- **Navegador y versión:** El navegador que estás usando (por ejemplo, Chrome 120, Safari 17) y si has intentado reproducir el error en un navegador diferente.
- **Pasos para reproducir:** Una descripción clara de las acciones que desencadenan el error, incluyendo cualquier paso o configuración específica de Canvas involucrada.
- **Registros de red (opcional):** Abre las herramientas de desarrollador de tu navegador (pestaña **Red**), reproduce el error y exporta el registro de red como un archivo de registro HTTP Archive (HAR). Esto ayuda al equipo de soporte a identificar qué llamada a la API está agotando el tiempo de espera.