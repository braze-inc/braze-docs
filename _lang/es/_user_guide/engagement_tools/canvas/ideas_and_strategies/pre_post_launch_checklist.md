---
nav_title: Lista de comprobación previa y posterior al lanzamiento
article_title: Lista de comprobación previa y posterior al lanzamiento
page_order: 2
description: "Este artículo proporciona una guía de las cosas que debes comprobar antes y después de lanzar un Canvas."
tool: Canvas

---

# Lista de control previa y posterior al lanzamiento

> Este artículo proporciona una guía de las cosas que debes comprobar antes y después de lanzar un Canvas.

## Aspectos a tener en cuenta antes del lanzamiento

Antes de lanzar un Canvas, hay varios detalles que puedes comprobar para asegurarte de que tus mensajes y tiempos de envío se ajustan a las preferencias de tu audiencia. Entre las cosas que hay que tener en cuenta están las variaciones en las zonas horarias, los ajustes de entrada, etc. Utilizando esta lista de comprobación como guía, afine estas áreas en función de su caso de uso para contribuir al éxito de su Canvas. 

{% alert important %}
Desde el 28 de febrero de 2023 ya no puedes crear ni duplicar Canvas mediante la experiencia Canvas original. Braze recomienda a los clientes que utilicen la experiencia Canvas original que se pasen a Canvas Flow. Es una experiencia de edición mejorada para construir y gestionar mejor los Lienzos. Más información sobre la [clonación de tus lienzos en el flujo de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

### Revisar la configuración de la zona horaria

Si está introduciendo usuarios según su zona horaria local utilizando un horario de entrada programado, debe lanzar su Canvas al menos 24 horas antes de la fecha en la que desea que los usuarios entren en su Canvas. Por ejemplo, aquí hay un Canvas que no ha dejado suficiente tiempo entre el lanzamiento y la hora de entrada programada. En este escenario, puede haber algunos usuarios que no entren en tu Canvas porque la hora de entrada programada ya ha pasado en determinadas zonas horarias. 

{% alert tip %}
Verás una alerta si no has programado un buffer suficiente. Una solución rápida es ajustar la hora de envío para garantizar que los usuarios puedan permanecer en el segmento objetivo durante 24 horas completas.
{% endalert %}

![Un Canvas programado para que los usuarios entren a la vez a partir de las 10 de la mañana del 30 de abril de 2025, en su hora local.]({% image_buster /assets/img_archive/canvas_checklist1.png %}){: style="max-width:75%;"}

### Considere el uso de expresiones regulares para los filtros de audiencia

Después de configurar los detalles preliminares de cuándo deben entrar sus usuarios en un Canvas, se recomienda comprobar ahora sus segmentos o filtros en el paso **Público objetivo** de la creación de un Canvas. En este paso, también puede revisar el resumen de la **población objetivo** para ver cómo se ha configurado su público objetivo. 

En este caso, considere la posibilidad de utilizar una expresión regular para segmentos o filtros en los pasos Rutas de audiencia, ajustes de validación de entrega también en los pasos Mensaje y División de decisión. Una [expresión regular]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/) (también denominada regex) es una cadena, lo que significa que reconoce patrones y tiene en cuenta caracteres, en lugar de cosas como las mayúsculas. Esto significa que si está utilizando "Igual / No igual", podría estar limitando el tamaño de su audiencia debido a simples errores de sintaxis.

Si observa que su público objetivo es menor de lo esperado, pruebe a utilizar "Coincide con Regex" o "No coincide con Regex" en lugar de "Es igual a" o "No es igual a". De este modo, se puede dar cuenta de los usuarios que faltan y llegar a un público más amplio. 

### Identifica la configuración de entrada y las condiciones de carrera

Una condición de carrera puede producirse cuando has utilizado los mismos criterios de entrada tanto en la configuración **del horario de entrada** como en la de **la audiencia objetivo**. 

Si utiliza la entrada basada en acciones, compruebe que no ha utilizado aquí la misma acción desencadenante que en su público objetivo. Puede producirse una condición de carrera en la que el usuario no se encuentre entre el público en el momento de realizar el evento desencadenante, lo que significa que no entrará en el Canvas.

{% alert tip %}
Consulta las [mejores prácticas]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#scenario-3-matching-action-based-triggers-and-audience-filters) para evitar esta condición de carrera al configurar un Canvas basado en acciones con el mismo desencadenante que el filtro de audiencia.
{% endalert %}

### Comprobar las propiedades de las entradas y eventos del lienzo

Aunque su nombre es similar, [las propiedades de entrada del lienzo y las propiedades de evento]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) funcionan de forma diferente en los flujos de trabajo del lienzo. Las propiedades de entrada del lienzo están vinculadas a la configuración de entrada y se puede hacer referencia a ellas en cualquier componente de mensaje de todo el lienzo. Las propiedades de entrada del lienzo son propiedades del evento o de la llamada a la API que desencadena la entrada de un usuario en un lienzo, utilizando configuraciones de entrada basadas en acciones o desencadenadas por la API.

Las propiedades de evento, por otro lado, sólo pueden ser referenciadas en el primer paso de Mensaje que sigue a un paso de Rutas de Acción. Las propiedades de evento son propiedades de un evento personalizado o de compra que el usuario ha realizado durante la ventana de evaluación de un paso de Rutas de Acción, y que desencadena su progresión por una de las rutas de acción definidas.

Compruebe la vista previa del mensaje para ver si hay algún paso de Mensaje que haga referencia a las propiedades de entrada del lienzo o a las propiedades del evento.

### Revisión Pasos del mensaje para el avance del usuario

Por defecto, los usuarios avanzarán por todos los pasos del Mensaje independientemente de si han recibido o no el mensaje. Si desea avanzar los usuarios que reciben un mensaje en particular, puede hacerlo añadiendo un paso de División de decisión directamente después de su componente Mensaje. Añada el filtro "Mensaje recibido del paso Canvas" como filtro adicional y, a continuación, seleccione el paso Canvas y Mensaje.

Para los pasos de Mensaje con mensajería in-app, puede que desee utilizar un componente de Rutas de Acción en lugar del componente de División de Decisión. Esto te permitirá hacer avanzar a los usuarios en función de si han visto tu mensaje in-app. Defina un grupo de acciones añadiendo el filtro "Interactuar con Paso" y seleccione **Ver en mensaje de aplicación**. A continuación, ajuste la ventana de evaluación del paso a la ventana de expiración del mensaje in-app.

Para un componente Mensaje en la mensajería multicanal, recomendamos lo siguiente:
* Incluye un paso de Retraso entre tus pasos de Mensaje y División de decisiones, y establece el retraso en al menos cinco segundos.
* Si el componente incluye Intelligent Timing, ajusta el retraso a 24 horas
* Si el componente incluye limitación de velocidad, divida sus mensajes en varios pasos de mensaje monocanal y conéctelos entre sí. A continuación, conecte el paso Decision Split directamente después del último paso Message para comprobar si un usuario ha recibido alguno de los mensajes. También puede utilizar este método como alternativa para un paso de Mensaje multicanal con Temporización inteligente.

## Aspectos a tener en cuenta tras el lanzamiento

¡Has lanzado tu Canvas! ¿Y ahora qué? Utilice esta lista de comprobación para ver cómo puede revisar y ajustar su Canvas en caso de discrepancias tras el lanzamiento, basándose en estos escenarios.

### Muchas entradas, pero pocos envíos

Por ejemplo, supongamos que ha observado una disparidad entre el número de mensajes enviados y el total de entradas. Puede identificar y descubrir áreas para ajustar su lienzo comprobando estas áreas clave.

#### Público de entrada

Si utilizas una campaña de envío programado, vuelve a comprobar tu audiencia objetivo revisando tu población objetivo. ¿Cómo se ven las cifras en todos los canales y cómo se relacionan con los canales que has utilizado en tu Canvas? Si los números más bajos se corresponden con los canales que has utilizado en tu Canvas, puede que hayas encontrado el problema.

#### Primer componente del lienzo

Revise los filtros de audiencia, los activadores de acciones o los segmentos utilizados en los componentes iniciales de su Canvas. ¿Hay faltas de ortografía o condiciones demasiado estrictas que impiden que su lienzo empiece bien? ¿Estás utilizando "Iguales" cuando deberías utilizar "Coincidencias regex"?

#### Grupo de control en Canvas 

Revise la distribución de usuarios entre sus variantes y su grupo de control. ¿Es el grupo de control más grande de lo que pretendía? Si es así, puede editar esta configuración. Si tiene activada **la Selección Inteligente** y el grupo de control va ganando, considere la posibilidad de detener su Lienzo y probar un nuevo enfoque.

### Una audiencia total vacía

Si no ves ningún dato de entrada en tu Canvas, la razón de que los usuarios no entren en tu Canvas puede deberse a condiciones de carrera y a filtros de segmentación de audiencia restrictivos.

Si utilizas la entrada basada en acciones en tu programa de entrada, comprueba que no has utilizado aquí la misma acción desencadenante que en tu **Audiencia objetivo**. Puede producirse una condición de carrera en la que el usuario no se encuentre entre el público en el momento de realizar el evento desencadenante, lo que significa que no entrará en el Canvas.

Además, compruebe que el segmento seleccionado tiene usuarios revisando la tabla **Población objetivo** en la configuración de **Público objetivo**. Si este número es bajo, vea cómo puede ajustar la configuración de entrada, o revise los segmentos o filtros seleccionados en busca de errores.

### Descenso inesperado entre pasos

Otra forma evidente de identificar áreas de ajuste para su Canvas puede ocurrir cuando hay una gran caída de un paso de Canvas al siguiente. En este caso, compruebe que los filtros de audiencia y los eventos de excepción no tienen errores ortográficos o de mayúsculas. Y como siempre, comprueba que tus filtros de audiencia no son tan estrictos como para omitir a la mayoría de tus usuarios de entrar en el Canvas. 

A continuación, es importante identificar estos ajustes que pueden afectar a cuándo y si los mensajes se envían a sus usuarios:
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)
- Horas tranquilas
- Validaciones de entrega

En general, elija la Temporización Inteligente o las Horas de Silencio para su Lienzo, no ambas. La misma sugerencia se aplica a utilizar la sincronización inteligente o [la limitación de velocidad]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/), no ambas. Para más información sobre la mejor manera de utilizar Intelligence Suite, lea nuestras [Preguntas frecuentes sobre Inteligencia]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/).

### Volúmenes de envío sospechosos entre rutas

Cuando el volumen de envíos entre dos o más rutas (ya sean rutas de audiencia o rutas de acción) no es el esperado, puede ser una oportunidad para revisar sus segmentos, filtros o acciones de activación. Asegúrese también de identificar y eliminar los filtros superpuestos.

