---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre Canvas
page_order: 8
alias: "/canvas_v2_101/"
description: "Este artículo ofrece respuestas a las preguntas más frecuentes sobre Canvas y Canvas Flow."
tool: Canvas

---

# Preguntas más frecuentes

> Este artículo proporciona respuestas a algunas preguntas frecuentes sobre Canvas y [Canvas Flow](#canvas-flow).

{% alert important %}
A partir del 28 de febrero de 2023, ya no podrás crear o duplicar Lienzos utilizando la experiencia Canvas original. Braze recomienda a los clientes que utilicen la experiencia Canvas original que se pasen a Canvas Flow. Es una experiencia de edición mejorada para construir y gestionar mejor los Lienzos. Más información sobre la [clonación de tus lienzos en el flujo de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

## General

### ¿Qué ocurre si la audiencia y el tiempo de envío son idénticos para un Canvas que tiene una variante, pero múltiples ramas?

Ponemos en cola un trabajo para cada paso, se ejecutan más o menos al mismo tiempo y uno de ellos "gana". En la práctica, la clasificación puede ser algo uniforme, pero es probable que tenga al menos un ligero sesgo hacia el paso que se creó en primer lugar. 

Además, no podemos garantizar cómo será exactamente esa distribución. Si desea una división uniforme, añada un filtro [Número de cubo aleatorio]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/).

### ¿Qué ocurre cuando se detiene un lienzo?

Cuando detienes un Canvas, se aplica lo siguiente:

- Se impedirá a los usuarios entrar en el Canvas.
- No se enviarán más mensajes, sin importar dónde se encuentre el usuario en el flujo.
- **Excepción:** Los lienzos con correos electrónicos no se detendrán inmediatamente. Después de que las solicitudes de envío vayan a SendGrid, no hay nada que podamos hacer para evitar que se entreguen al usuario.

### ¿Debo crear un solo Canvas o Canvas separados por ciclo de vida del usuario?

Dependiendo de lo que quieras conseguir con tu Canvas, puede que necesites diferentes enfoques en la forma de construir tu recorrido del usuario. La flexibilidad de Canvas te permite mapear recorridos de usuario para cualquier etapa del ciclo de vida del usuario. Echa un vistazo a nuestras [plantillas Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates) para ver varios ejemplos de enfoques simplificados para crear recorridos de usuario eficaces.

#### Mensajes in-app en Canvas

Los mensajes dentro de la aplicación se envían al iniciar la siguiente sesión. Esto significa que si el usuario entra en el paso en Canvas antes de que se detenga el Canvas, seguirá recibiendo el mensaje dentro de la aplicación al iniciar su próxima sesión, siempre que el mensaje dentro de la aplicación no haya caducado todavía.

Es posible que un usuario inicie una sesión antes de que se detenga el Canvas, pero que no se le muestre el mensaje dentro de la aplicación inmediatamente. Esto puede ocurrir si el mensaje dentro de la aplicación se desencadena por un evento personalizado o se retrasa. Esto significa que es posible que un usuario registre una impresión de mensaje dentro de la aplicación y "reciba" el mensaje dentro de la aplicación después de que se detenga el Canvas. Sin embargo, el usuario tendría que haber iniciado la sesión antes de que se detuviera el Canvas, pero **después de** haber recibido el paso en Canvas.

{% alert note %}
Detener un Canvas no hará que los usuarios que están esperando recibir mensajes salgan del recorrido del usuario. Si vuelves a habilitar el Canvas y los usuarios siguen esperando el mensaje, lo recibirán (a menos que haya pasado el tiempo en que se les debería haber enviado el mensaje, entonces no lo recibirán).
{% endalert %}

### ¿Cuándo se desencadena un evento de excepción?

Los eventos de excepción sólo se desencadenan mientras el usuario está esperando recibir el componente Canvas al que está asociado. Si un usuario realiza una acción por adelantado, el evento de excepción no se desencadenará. Si desea excluir a los usuarios que hayan realizado un determinado evento con anterioridad, utilice [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) en su lugar.

### ¿Cómo afecta la edición de un lienzo a los usuarios que ya están en él?

Si edita algunos de los pasos de un Canvas de varios pasos, los usuarios que ya estaban en la audiencia pero no han recibido los pasos recibirán la versión actualizada del mensaje. Ten en cuenta que esto solo ocurrirá si aún no han sido evaluados para el paso.

Para más información sobre lo que puede editar después del lanzamiento, consulta [Cambiar tu Canvas después del lanzamiento]({{site.baseurl}}/post-launch_edits/).

### ¿Cómo se realiza el seguimiento de las conversiones de los usuarios en un Canvas?

Un usuario sólo puede convertir una vez por entrada de Canvas. Las conversiones se asignan al mensaje más reciente recibido por el usuario para esa entrada. El bloque de resumen al principio de un Canvas refleja todas las conversiones realizadas por los usuarios dentro de esa ruta, hayan recibido o no un mensaje. Cada paso posterior solo mostrará las conversiones que se produjeron mientras ese era el paso más reciente recibido por el usuario.

{% details Ejemplos %}

**Ejemplo 1**

Hay una ruta de Canvas con 10 notificaciones push y el evento de conversión es «session start» (inicio de sesión) («Opens App» [Abre la aplicación]):

- El usuario A abre la aplicación después de entrar pero antes de recibir el primer mensaje.
- El usuario B abre la aplicación después de cada notificación push.

**Resultado:** El resumen mostrará dos conversiones, mientras que los pasos individuales mostrarán una conversión de uno en el primer paso y cero en todos los pasos siguientes.

{% alert note %}
Si las Horas de Silencio están activas cuando se produce el evento de conversión, se aplican las mismas reglas.
{% endalert %}

**Ejemplo 2**

Hay un lienzo de un solo paso con las horas de silencio activadas:

1. El usuario entra en el lienzo.
2. El primer paso no tiene retardo, pero está dentro de las Horas Silenciosas establecidas, por lo que el mensaje se suprime.
3. El usuario realiza el evento de conversión.

**Resultado:** El usuario contará como convertido en la variante general Canvas, pero no el paso ya que no recibió el paso.

{% enddetails %}

### ¿Cuál es la diferencia entre los distintos tipos de tasa de conversión?

- El total de conversiones en Canvas refleja cuántos usuarios únicos completaron un evento de conversión, no cuántas conversiones completó cada uno. 
- La tasa de conversión variante o bloque resumen al principio de un Canvas refleja todas las conversiones realizadas por los usuarios dentro de esa ruta, hayan recibido o no un mensaje, como un total agregado. 
- La tasa de conversión de pasos refleja cuántas personas recibieron ese paso del mensaje y completaron alguno de los eventos de conversión descritos.

### ¿Cuál es la diferencia entre un componente y un paso?

Un [componente]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) es una parte individual de su lienzo que puede utilizar para determinar la eficacia de su lienzo. Los componentes pueden incluir acciones como dividir el recorrido del usuario, añadir un retraso e incluso probar varias rutas de Canvas. Un paso en Canvas se refiere al recorrido personalizado del usuario en sus ramas de Canvas. Esencialmente, tu Canvas está formado por componentes individuales que crean pasos para tu recorrido de usuario.

### ¿Cómo puedo ver los análisis de cada uno de mis componentes de Canvas?

Para ver los análisis de un componente del lienzo, vaya a su lienzo y desplácese hacia abajo por la página **Detalles del lienzo**. Aquí puede ver los análisis de cada componente. Consulta [los análisis de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para obtener más información.

### Si nos fijamos en el número de usuarios únicos, ¿es más preciso el análisis de Canvas o el segmentador?

El segmentador es una estadística más precisa para los datos de usuario único frente a las estadísticas de Canvas o de campaña. Esto se debe a que las estadísticas de Canvas y de campaña son números que Braze incrementa cuando ocurre algo, lo que significa que hay variables que podrían hacer que este número fuera diferente al del segmentador. Por ejemplo, los usuarios pueden convertir más de una vez un Canvas o una campaña.

### ¿Por qué el número de usuarios que entran en un lienzo no coincide con el número esperado?

El número de usuarios que entran en un Canvas puede diferir del número esperado debido a cómo se evalúan las audiencias y los activadores. En Braze, un público se evalúa antes del desencadenante (a menos que se utilice un desencadenante de [cambio de atributo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) ). Esto hará que los usuarios abandonen el Canvas si no forman parte de su audiencia seleccionada antes de que se evalúe cualquier acción desencadenante.

### ¿Qué ocurre con los usuarios anónimos durante su viaje por Canvas?

Aunque los usuarios anónimos pueden entrar y salir de los Lienzos, sus acciones no se asocian a un perfil de usuario específico hasta que se identifican, por lo que es posible que sus interacciones no se sigan completamente en tus análisis. Puedes utilizar el [Generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/) para generar un informe de estas métricas.

### ¿Por qué mi tasa de conversión de pasos de Canvas no es igual a mi tasa de conversión total de variantes de Canvas?

Es habitual que el total de conversiones de una variante de Canvas sea mayor que la suma de su total de pasos. Esto ocurre porque un usuario puede realizar un evento de conversión para una variante tan pronto como la introduce. Sin embargo, este mismo evento de conversión no cuenta para un paso de Canvas. Por lo tanto, cualquier usuario que entre en el lienzo y realice el evento de conversión antes de recibir el primer paso del lienzo, se contabilizará en el total de conversiones de la variante y no en el total de pasos. Lo mismo ocurre con un usuario que entra en el lienzo pero sale de él antes de recibir ningún paso.

### ¿Cómo se evalúan las audiencias de Canvas? 

Por defecto, los filtros y segmentos de los pasos completos del lienzo se comprueban en el momento del envío. En el caso del flujo Canvas, el componente de división de decisiones realiza una evaluación justo después de recibir un paso anterior (o antes de un retraso).

{% alert tip %}
Para obtener más ayuda con la solución de problemas de Canvas, asegúrese de ponerse en contacto con el servicio de asistencia de Braze en los 30 días siguientes a la aparición del problema, ya que sólo disponemos de los registros de diagnóstico de los últimos 30 días.
{% endalert %}

## Canvas Flow

### ¿Qué es Canvas Flow?

Canvas Flow es la experiencia de edición mejorada que simplifica el modo en que los profesionales del marketing pueden crear y gestionar sus experiencias de usuario en Canvas. Puede esperar ver y utilizar fácilmente los componentes Canvas en el constructor Canvas. También tiene acceso a más funciones de edición posteriores al lanzamiento para editar conexiones entre pasos, eliminar pasos y variantes, y redirigir a los usuarios a pasos diferentes.

### ¿Cómo convierto un Canvas existente en Canvas Flow?

Puedes [clonar tu Canvas a Canvas Flow]({{site.baseurl}}/cloning_canvases/). Esto crea una copia de tu Canvas original en el flujo de trabajo del Flujo del Canvas.

### ¿Qué pasará con los lienzos que creé con el editor original?

Todos los lienzos existentes y el editor de lienzos original seguirán existiendo y serán compatibles con Braze. Los clientes que decidan unirse a Canvas Flow para el acceso anticipado tendrán la opción de crear un Canvas utilizando el flujo de trabajo original o Flow.

### ¿Hay algún límite en el número de pasos que puedo incluir?

Sí. Un lienzo creado con el flujo del lienzo puede contener hasta 200 pasos.

### ¿Puedo lanzar un Canvas con pasos desconectados?

¡Sí! Canvas Flow te permite lanzar tu Canvas con pasos desconectados. También puede guardar los lienzos después del lanzamiento con pasos desconectados. 

### ¿Adónde van los usuarios cuando llegan a un paso desconectado?

Si un usuario se encuentra en un paso desconectado de su flujo de trabajo del Flujo del lienzo, avanzará al paso siguiente si lo hay, y la configuración del paso dictará cómo debe avanzar el usuario. Con ello se pretende que los usuarios puedan realizar cambios en los pasos sin tener que conectarlos directamente con el resto del lienzo. Esto también te da cierto margen para hacer pruebas antes de ponerte en vivo inmediatamente, lo que te permite guardar un borrador.

Recomendamos comprobar la vista de análisis de usuarios pendientes en un paso de Canvas antes de desconectar un paso.

### ¿Cuáles son las principales diferencias entre el Canvas Flow y el editor Canvas original?

#### Barra de herramientas del componente Canvas

Anteriormente, con el editor Canvas original, se añadía por defecto un paso completo cada vez que se creaba cualquier paso en el recorrido del usuario. Ahora, con Canvas Flow, estos pasos completos se sustituyen por diferentes componentes de Canvas, lo que te ofrece la ventaja de una mayor visibilidad y personalización para tu experiencia de edición. Puede ver inmediatamente todos sus componentes del lienzo desde la barra de herramientas de pasos del lienzo.

#### Comportamiento de los pasos

Anteriormente, cada paso completo incluía información como ajustes de retraso y programación, eventos de excepción, filtros de audiencia, configuración de mensajes y opciones de avance de mensajes, todo en un solo componente. Se trata de ajustes independientes en el Flujo de Canvas para que tu experiencia de creación de Canvas sea más personalizable e introduce algunas diferencias en la funcionalidad.

#### Avance del componente de mensajes

[Los componentes del mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) adelantan a todos los usuarios que entran en el paso. No es necesario especificar el comportamiento de avance de los mensajes, lo que simplifica la configuración del paso general. Si desea implementar la opción **Avanzar cuando se envíe el mensaje**, añada una Ruta de público independiente para filtrar los usuarios que no hayan recibido el paso anterior.  

#### Retraso "en" el comportamiento

[Los componentes de retardo]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) esperarán todo el tiempo de retardo antes de pasar al siguiente paso. 

Digamos que el 12 de abril tenemos un componente Retraso en el que el retraso está configurado para enviar a tu usuario al siguiente paso en un día a las 2 de la tarde. Un usuario entra en el componente a las 14:01 horas del 13 de abril. 
- En el flujo de trabajo original, el usuario pasaría al siguiente paso a las 14.00 horas del 14 de abril, es decir, menos de un día después de la hora de entrada. 
- En el caso de Canvas Flow, el usuario pasaría al siguiente paso a las 14:00 horas del 15 de abril. Ten en cuenta que se trata de la misma hora, pero a más de un día de la hora de entrada. 

#### Comportamiento de sincronización inteligente

Como [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) se almacena en el componente Mensaje, los retrasos se aplicarán antes de los cálculos de Intelligent Timing. Esto significa que, dependiendo del momento en que un usuario entre en el componente, puede recibir el mensaje más tarde de lo que lo haría en un lienzo construido con el flujo de trabajo original del lienzo.

Supongamos que el retraso es de 2 días, la sincronización inteligente está activada y ha determinado que la mejor hora para enviar el mensaje son las 14:00. Un usuario entra en el paso Retraso a las 14:01.
- **Canvas Flow:** El retraso tardará 48 horas en transcurrir, por lo que el usuario recibirá el mensaje el tercer día a las 14:00 horas.
- **Flujo de trabajo original:** El usuario recibe el mensaje el segundo día a las 14.00 horas.

Tenga en cuenta que si la Temporización Inteligente está activada, el mensaje se enviará en un plazo de 24 horas desde que el usuario introduzca el componente Mensaje a la hora inteligente identificada (incluso si no interviene ningún componente Retraso).

#### Eventos de excepción

##### Horas tranquilas

La funcionalidad de eventos de excepción en el Canvas Flow se aplica utilizando Rutas de Acción, que son independientes de los pasos de Mensaje. Las horas de silencio se aplican en el componente de Mensajes. Esto significa que si un usuario ya ha pasado por la Ruta de Acción (y no ha sido excluido con el evento de excepción allí), luego llega a las Horas de Silencio cuando llega al componente Mensaje, y tiene su Canvas configurado para que el mensaje se reenvíe después del período de Horas de Silencio, el evento de excepción ya no se aplicará. Tenga en cuenta que este caso de uso no es habitual.

Para los segmentos y filtros, el componente Mensaje del Flujo del lienzo tiene una nueva función llamada Validaciones de entrega que permite a los usuarios configurar segmentos y filtros adicionales que se validan en el momento del envío. De este modo se evita el mencionado caso límite de las Horas de Silencio.

##### Configuración del horario "En" o "En el siguiente"

Los eventos de excepción en el Canvas Flow se crean utilizando Rutas de Acción. Las rutas de acción sólo admiten "después de una ventana de tiempo X" y no "en un tiempo X" o "en el próximo tiempo X".
