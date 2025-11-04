---
nav_title: Lista de control previa y posterior al lanzamiento
article_title: Lista de comprobación previa y posterior al lanzamiento
page_order: 2
description: "Este artículo proporciona una guía de las cosas que debes comprobar antes y después de lanzar un Canvas."
tool: Canvas

---

# Lista de control previa y posterior al lanzamiento

> Este artículo proporciona una guía de las cosas que debes comprobar antes y después de lanzar un Canvas.

## Cosas a tener en cuenta antes del lanzamiento

Antes de lanzar un Canvas, hay varios detalles que puedes comprobar para asegurarte de que tu mensajería y los tiempos de envío se ajustan a las preferencias de tu audiencia. Hay que tener en cuenta las variaciones en las zonas horarias, la configuración de entrada, etc. Utilizando esta lista de comprobación como guía, afina estas áreas basándote en tu caso de uso para contribuir al éxito de tu Canvas. 

### Revisar la configuración de la zona horaria

Si estás introduciendo usuarios según su zona horaria local utilizando un horario de entrada programado, debes lanzar tu Canvas al menos 24 horas antes de la fecha en que quieres que los usuarios entren en tu Canvas. Por ejemplo, aquí tienes un Canvas que no ha dejado tiempo suficiente entre el lanzamiento y la hora de entrada programada. En este caso, puede haber algunos usuarios que no entren en tu Canvas porque la hora de entrada programada ya ha pasado en determinadas zonas horarias. 

{% alert tip %}
Verás una alerta si no has programado un buffer suficiente. Una solución rápida es ajustar la hora de envío para garantizar que los usuarios puedan permanecer en el segmento objetivo durante 24 horas completas.
{% endalert %}

\![Un Canvas programado para que los usuarios entren a la vez a partir de las 10 de la mañana del 30 de abril de 2025, en su hora local.]({% image_buster /assets/img_archive/canvas_checklist1.png %}){: style="max-width:75%;"}

### Considera la posibilidad de utilizar expresiones regulares para filtrar la audiencia

Después de configurar los detalles preliminares de cuándo deben entrar tus usuarios en un Canvas, se recomienda que ahora compruebes tus segmentos o filtros en el paso **Audiencia objetivo** de la creación de un Canvas. En este paso, también puedes revisar el resumen **Población objetivo** para ver cómo se ha configurado tu audiencia objetivo. 

Aquí, considera también el uso de una expresión regular para los segmentos o filtros en los pasos de las rutas de audiencia, la configuración de validación de la entrega en los pasos para la división de decisiones y mensajes. Una [expresión regular]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/) (también llamada regex) es una cadena, lo que significa que reconoce patrones y tiene en cuenta caracteres, en lugar de cosas como las mayúsculas. Esto significa que si utilizas "Igual / No igual", podrías estar limitando el tamaño de tu audiencia por simples errores de sintaxis.

Si observas que tu audiencia objetivo es menor de lo esperado, prueba a utilizar "Coincide con regex" o "No coincide con regex" en lugar de "Iguala" o "No iguala". Esto puede dar cuenta de los usuarios que faltan, y dirigirse a una audiencia mayor. 

### Identifica la configuración de entrada y las condiciones de carrera

Una condición de carrera puede producirse cuando has utilizado los mismos criterios de entrada tanto en la configuración **del horario de entrada** como en la de **la audiencia objetivo**. 

Si utilizas la entrada basada en la acción, comprueba que no has utilizado aquí la misma acción desencadenante que en tu audiencia objetivo. Puede darse una condición de carrera en la que el usuario no se encuentre entre la audiencia en el momento de desencadenar el evento, lo que significa que no entrará en el Canvas.

{% alert tip %}
Consulta las [mejores prácticas]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#scenario-3-matching-action-based-triggers-and-audience-filters) para evitar esta condición de carrera al configurar un Canvas basado en acciones con el mismo desencadenante que el filtro de audiencia.
{% endalert %}

### Comprueba las propiedades de la entrada en Canvas y las propiedades del evento

Aunque tienen un nombre similar, [las propiedades de entrada y las propiedades del evento de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) funcionan de forma diferente dentro de tus flujos de trabajo de Canvas. Las propiedades de entrada del Canvas están vinculadas a tu configuración de entrada, y se puede hacer referencia a ellas en cualquier componente de mensaje de todo tu Canvas. Las propiedades de entrada al Canvas son propiedades del evento o de la llamada a la API que desencadena la entrada de un usuario en un Canvas, utilizando configuraciones de entrada basadas en la acción o desencadenadas por la API.

Las propiedades del evento, en cambio, sólo pueden referenciarse en el primer paso de Mensaje que sigue a un paso de Ruta de acción. Las propiedades del evento son propiedades de un evento personalizado o de un evento de compra que el usuario realizó durante la ventana de evaluación de un paso de Rutas de acción, y que desencadena su progresión por una de las rutas de acción definidas.

Comprueba en la vista previa de tu mensaje si hay algún paso en Mensajería que haga referencia a propiedades de la entrada en Canvas o propiedades del evento.

### Revisión Pasos del mensaje para el avance del usuario

De forma predeterminada, los usuarios avanzarán por todos los pasos de la Mensajería independientemente de si han recibido o no el mensaje. Si quieres hacer avanzar a los usuarios que reciben un mensaje concreto, puedes hacerlo añadiendo un paso para la división de decisiones directamente después de tu componente Mensaje. Añade el filtro "Mensaje recibido del paso en Canvas" como filtro adicional y, a continuación, selecciona el paso en Canvas y Mensaje.

Para los pasos de Mensajes con mensajería dentro de la aplicación, puede que quieras utilizar un componente de Rutas de acción en lugar del componente de División de decisiones. Esto te permitirá hacer avanzar a los usuarios en función de si han visto tu mensaje dentro de la aplicación. Define un grupo de acciones añadiendo el filtro "Interactuar con Paso" y selecciona **Ver mensaje dentro de la aplicación**. A continuación, ajusta la ventana de evaluación del paso a la ventana de caducidad del mensaje dentro de la aplicación.

Para un componente Mensaje en mensajería multicanal, recomendamos lo siguiente:
* Incluye un paso de Retraso entre tus pasos de Mensaje y División de decisiones, y establece el retraso en al menos cinco segundos.
* Si el componente incluye Intelligent Timing, ajusta el retraso a 24 horas
* Si el componente incluye límite de tasa, divide tus mensajes en varios pasos de mensajería de un solo canal y conéctalos entre sí. A continuación, conecta el paso para la división de decisiones directamente después del último paso de mensajes para comprobar si un usuario ha recibido alguno de los mensajes. También puedes utilizar este método como alternativa para un paso de Mensaje multicanal con Intelligent Timing.

## Cosas a tener en cuenta después del lanzamiento

¡Has lanzado tu Canvas! ¿Y ahora qué? Utiliza esta lista de comprobación para ver cómo puedes revisar y ajustar tu Canvas en caso de discrepancias tras el lanzamiento, basándote en estos supuestos.

### Muchas entradas, pero pocos envíos

Por ejemplo, supongamos que has observado una disparidad entre el número de mensajes enviados y el total de entradas. Puedes identificar y descubrir áreas para ajustar tu Canvas comprobando estas áreas clave.

#### Audiencia de entrada

Si utilizas una campaña de envío programado, vuelve a comprobar tu audiencia objetivo revisando tu población objetivo. ¿Cómo se ven las cifras a través de los canales, y cómo se relacionan con los canales que has utilizado en tu Canvas? Si los números más bajos se corresponden con los canales que has utilizado en tu Canvas, puede que hayas encontrado el problema.

#### Primer componente del Canvas

Revisa los filtros de audiencia, desencadenantes de acciones o segmentos utilizados en los componentes iniciales de tu Canvas. ¿Hay faltas de ortografía o condiciones demasiado estrictas que impiden que tu Canvas empiece bien? ¿Estás utilizando "Iguales" cuando deberías utilizar "Coincidencias regex"?

#### Grupo de control Canvas 

Revisa la distribución de usuarios entre tus variantes y tu grupo de control. ¿El grupo de control es mayor de lo que pretendías? Si es así, puedes editar esta configuración. Si tienes activada **la Selección Inteligente** y el grupo de control va ganando, considera la posibilidad de detener tu Canvas y probar un nuevo enfoque.

### Una audiencia total vacía

Si no ves ningún dato de entrada en tu Canvas, la razón de que los usuarios no entren en tu Canvas puede deberse a condiciones de carrera y a filtros de segmentación de audiencia restrictivos.

Si utilizas la entrada basada en acciones en tu programa de entrada, comprueba que no has utilizado aquí la misma acción desencadenante que en tu **Audiencia objetivo**. Puede darse una condición de carrera en la que el usuario no se encuentre entre la audiencia en el momento de desencadenar el evento, lo que significa que no entrará en el Canvas.

Además, comprueba que el segmento seleccionado tiene usuarios revisando la tabla de **población objetivo** en la configuración de **la audiencia objetivo**. Si este número es bajo, comprueba cómo puedes ajustar la configuración de entrada o revisar los segmentos o filtros seleccionados para ver si hay algún error.

### Descenso inesperado entre peldaños

Otra forma aparente de identificar áreas de ajuste para tu Canvas puede ocurrir cuando hay una gran caída de un paso en Canvas al siguiente. En este caso, comprueba que tus filtros de audiencia y eventos de excepción no tienen faltas de ortografía ni errores de mayúsculas. Y como siempre, comprueba que tus filtros de audiencia no son tan estrictos como para omitir a la mayoría de tus usuarios de entrar en el Canvas. 

A continuación, es importante identificar estas configuraciones que pueden afectar a cuándo y si se envían mensajes a tus usuarios:
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)
- Horas tranquilas
- Validaciones de entrega

En general, elige o bien Intelligent Timing o bien Horas tranquilas para tu Canvas, no ambos. La misma sugerencia se aplica a utilizar o bien Intelligent Timing o bien [el límite de tasa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/), no ambos. Para más información sobre cómo utilizar mejor la Intelligence Suite, lee nuestros [casos de uso de la Suite Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/#use-cases).

### Volúmenes de envío sospechosos entre rutas

Cuando el volumen de envíos entre dos o más rutas (ya sean rutas de audiencia o rutas de acción) no es el esperado, puede ser una oportunidad para revisar tus segmentos, filtros o acciones desencadenantes. Además, asegúrate de identificar y eliminar los filtros que se solapen.

