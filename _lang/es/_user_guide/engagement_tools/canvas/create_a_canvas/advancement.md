---
nav_title: Comportamientos de avance
article_title: Comportamientos de avance
page_order: 10
alias: /auto_advance/
page_type: reference
description: "Este artículo de referencia describe el Comportamiento de Avance y cubre varios escenarios que pueden surgir a medida que se avanza en un Lienzo."
tool: Canvas

---

# Comportamientos de avance

{% alert important %}
A partir del 28 de febrero de 2023, ya no podrás crear o duplicar Lienzos utilizando el editor original. Este artículo está disponible como referencia para entender cómo sus usuarios avanzan a través de los componentes de Canvas en el editor original. <br><br>Para los componentes en el Flujo del lienzo, el **Comportamiento de avance** está configurado para que el público avance siempre inmediatamente, o **Avanzar inmediatamente público**. Esto también se aplicará a los [pasos desconectados]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#disconnected-steps/).
{% endalert %}

> La función **Comportamiento de avance** le permite elegir los criterios de avance a través de su [componente Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/). 

![Configuración del Comportamiento de Avance con dos opciones para hacer avanzar a la audiencia cuando se envía el mensaje, o hacer avanzar a la audiencia inmediatamente.]({% image_buster /assets/img/push-advancement-behavior.png %} "Comportamiento de Avance")

Los usuarios deben cumplir los criterios del paso para poder avanzar en él. Con Pasos de [mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), puede activar las validaciones de entrega para comprobar que su público cumple los criterios de entrega en el momento de enviar el mensaje. Esto contará para los criterios del paso cuando se utilice el Canvas Flow. Así, si un usuario no cumple los criterios de validación de entrega, saldrá del Canvas.

Si se selecciona **Avanzar cuando se envía el mensaje**, los usuarios sólo avanzarán a los pasos siguientes del Lienzo cuando se dé una de las siguientes condiciones:

- Se envía un mensaje de correo electrónico
- Se envía un mensaje push
- Se envía un webhook
- Se visualiza un mensaje in-app
- Se envía una tarjeta de contenido

Cuando se selecciona **Audiencia Avanzar Inmediatamente**, los usuarios avanzarán a los siguientes pasos de Canvas cuando se produzca una de las siguientes condiciones:

- Se envía cualquier mensaje o el mensaje dentro de la aplicación en este paso se convierte en mensaje en vivo
- El webhook no se envía porque el webhook causa un error o errores
- No se envía una notificación push o un correo electrónico porque no se puede acceder al usuario mediante notificación push o correo electrónico
- Se intenta enviar la tarjeta de contenido 
- Una tarjeta se cancela y no se envía
- Un mensaje no se envía porque tiene un límite de frecuencia
- Un mensaje no se envía porque se ha anulado

### Pasos programados

Para un componente programado, los usuarios deben cumplir con las opciones de audiencia para el paso con el fin de avanzar a través del paso. Si el paso tiene un [evento]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/#exception-events) de excepción, los usuarios que realicen el evento de excepción no avanzarán por el paso.

Al enviar un componente multicanal con [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/), podemos enviar o intentar enviar mensajes a horas diferentes para canales diferentes. Braze adelantará automáticamente a los usuarios en el momento en que el primer mensaje de un componente intente enviarse.

### Medidas basadas en la acción

Para los pasos basados en acciones, los usuarios deben realizar la acción desencadenante y cumplir las opciones de audiencia para poder avanzar en el paso. Si el paso tiene un evento de excepción, los usuarios que realicen el evento de excepción no avanzarán por el paso.

{% alert important %}
Los usuarios que avancen por un paso sin recibir mensajes no se contarán como destinatarios únicos del paso. Los usuarios deben recibir uno o más mensajes de un paso para ser contados como destinatarios únicos.
{% endalert %}

## Caso de uso

El avance funciona bien cuando los mensajes posteriores se relacionan con los anteriores. Por ejemplo, no querría enviar un push de seguimiento sobre un correo electrónico que nunca se envió a los usuarios.

Puede haber ocasiones en las que desee que los usuarios sigan avanzando por un lienzo aunque no reciban un determinado mensaje. Por ejemplo, puede enviar un push de "Bienvenida" el tercer día y un correo electrónico de "Bienvenida" el sexto día. Es posible que no pueda llegar a algunos de sus usuarios a través de notificaciones push, ya que no todos optan por recibir mensajes push. Es posible que desee enviar el correo electrónico del Día 6 a todos los usuarios, aunque no se les haya enviado el push del Día 3.

En este caso, puede utilizar las opciones de Comportamiento de avance para asegurarse de que los usuarios continúan en el Lienzo aunque no se les envíe el push del Día 3.

Si desea que todos los usuarios reciban el correo electrónico del Día 6, aunque no hayan recibido el push del Día 3, puede establecer el **Comportamiento de avance** en **Audiencia de avance inmediato** para el push del Día 3.

Si selecciona el comportamiento **Avance inmediato del público** para el push del Día 3, los usuarios avanzarán cuando Braze intente enviar el push. A los usuarios que coincidan con las opciones de audiencia y que no sean localizables vía push no se les enviará el push pero se les avanzará de todas formas.

{% details Comportamiento previo de avance en Canvas %}

Antes del lanzamiento de Advancement Behavior, Braze hacía avanzar a los usuarios a través de un componente Canvas después de haberles enviado un mensaje desde ese componente. Por ejemplo, si un componente de Canvas incluyera un correo electrónico y un push, los usuarios no avanzarían a los siguientes pasos del Canvas hasta que Braze enviara al usuario el push o el correo electrónico.

Si al usuario no se le enviaba el push o el correo electrónico, no avanzaba a los siguientes pasos del Canvas.

A los clientes de Braze que no participaron en la primera ronda de la beta de mensajes in-app de Canvas se les aplicará la opción de comportamiento de avance "Mensaje enviado" a todos los pasos de Canvas creados antes del 30 de julio de 2019. Antes de la versión de Comportamiento de Avance, el avance del usuario se producía cuando se enviaban mensajes desde los pasos de Canvas.

A los clientes de Braze que sí participaron en la primera ronda de la beta de mensajes in-app de Canvas se les aplicará la opción de comportamiento de avance "Mensaje enviado" a todos los pasos de Canvas sin mensajes in-app creados antes del 30 de julio de 2019 y "Audiencia avanzada tras retraso" a todos los pasos de Canvas con mensajes in-app creados antes del 30 de julio de 2019. Antes del lanzamiento de Comportamiento de avance, el avance del usuario se producía cuando los mensajes de Canvas en la aplicación se activaban.

{% enddetails %}

