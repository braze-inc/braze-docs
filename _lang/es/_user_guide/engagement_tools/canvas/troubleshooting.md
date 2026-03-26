---
nav_title: Solución de problemas
article_title: Solución de problemas con los lienzos
page_order: 11
page_type: reference
description: "Esta página proporciona pasos para la solución de problemas relacionados con los lienzos."
tool: Canvas
---

# Solución de problemas con los lienzos

> Esta página te ayuda con la solución de problemas relacionados con tus lienzos.

## ¿Por qué un usuario no recibió un paso en Canvas desencadenado?

En primer lugar, confirma que el evento personalizado se está transmitiendo a Braze. Ve a **Análisis** > **Informe de eventos personalizados** y, a continuación, selecciona el evento personalizado y el intervalo de fechas correspondientes. Si el evento no se muestra, confirma que esté configurado correctamente y que el usuario haya realizado la acción correcta.

Si se muestra el evento personalizado, continúa con la solución de problemas realizando lo siguiente:

- Comprueba la descarga del perfil de usuario para confirmar que tú desencadenaste el evento y cuándo lo hiciste. Si el evento fue desencadenado, compara la marca de tiempo en la que se desencadenó el evento con la hora en la que Canvas pasó a ser en vivo. Es posible que el evento se haya desencadenado antes de que Canvas entrara en funcionamiento en vivo.
- Revisa los registros de cambios de Canvas y de cualquier segmento utilizado en la segmentación para determinar si el usuario se encontraba en el segmento cuando su evento personalizado fue desencadenado. Si no estuvieran en el segmento, no habrían recibido el paso en Canvas.
- Verifica si el usuario fue incluido en un grupo de control mediante la segmentación y, por lo tanto, se le impidió recibir el paso en Canvas.
- Si hay un retraso programado, comprueba si el evento personalizado del usuario se desencadenó antes del retraso. Si el evento se hubiera desencadenado antes del retraso, no habrían recibido el paso en Canvas.

{% alert note %}
Los mensajes dentro de la aplicación solo pueden desencadenarse mediante eventos enviados a través del SDK, no de la API REST.
{% endalert %}

## ¿Por qué no se envía mi Canvas como esperaba?

Los Canvas son robustos y complejos, y sabemos que dedicas tiempo y cuidado al crearlos. Por lo tanto, si observas que tu Canvas no se envía como deseas, te recomendamos que compruebes tu calendario de Canvas, la audiencia de entrada y la configuración de entrada, y que revises los pasos para [crear un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

### Planificación

- ¿Está [bien programado]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#entry-schedule-types) el Canvas?
- ¿Has seleccionado la fecha y hora correctas?
- Para la [entrega basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=action-based%20delivery#entry-schedule-types), ¿han realizado los usuarios las acciones especificadas desde que lanzaste el Canvas?

### Configuración de la entrada

La [configuración de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=basics#selecting-entry-controls) es importante para entender cómo envían tus Lienzos. Comprueba si has limitado el número de personas que pueden entrar en el Canvas.

Los usuarios también pueden salir de un Canvas si ya no son elegibles para recibir mensajes. Por ejemplo, si el Canvas sólo contiene notificaciones push, y un usuario opta por no recibir notificaciones push después de recibir el primer paso, entonces ese usuario abandonaría el Canvas. Considera la posibilidad de utilizar [diferentes pasos en Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) para añadir recorridos de usuario alternativos.

### Segmentar tu audiencia

Considera las siguientes preguntas para tu audiencia objetivo:

- ¿Has seleccionado el segmento correcto?
- ¿Cómo se configura el segmento?
- ¿Has confirmado que el segmento contiene usuarios?
- ¿Has añadido algún filtro adicional que limite el número de usuarios que entran en el Canvas?
- ¿Los usuarios cumplen los requisitos para recibir el primer paso de tus variantes? Por ejemplo, si el primer paso de tu Canvas es una notificación push, pero toda la audiencia de entrada está deshabilitada para push, ningún usuario recibirá mensajes.

## ¿Por qué ningún usuario entró en mi Canvas programado diariamente el día del cambio al horario de verano?

En los días de cambio al horario de verano (DST), los Canvases programados diariamente pueden ejecutarse hasta una hora antes o después de lo habitual. Si tus criterios de entrada se basan en atributos personalizados o eventos con marcas de tiempo que caen dentro de una hora de la hora de entrada programada, es posible que los usuarios aún no califiquen en el día del horario de verano porque el atributo o evento no se ha registrado.

Por ejemplo, supongamos que los usuarios suelen recibir una actualización de atributos personalizados a las 3:00 p.men la zona horaria de Canvas y que Canvas se ejecuta diariamente a las 3:30 p.men esa misma zona horaria. En un día de cambio horario de primavera, Canvas puede evaluar a los usuarios hasta una hora antes de lo habitual en relación con esa actualización de atributos, antes de que se haya registrado el atributo. Si se desactiva la posibilidad de volver a ser elegible, los usuarios que hayan participado en días anteriores no podrán volver a ser elegibles, lo que dará lugar a que no haya entradas ese día.

Para evitarlo, asegúrate de que las actualizaciones de tus atributos o eventos personalizados se produzcan más de una hora antes de la hora de entrada programada en Canvas.

## ¿Por qué tu audiencia no se dividió de manera uniforme entre el grupo de control y el grupo variante?

Al crear tu Canvas, es posible que hayas esperado que tu audiencia se dividiera de manera uniforme entre tu grupo de control y tu grupo variante, como en el siguiente [caso de uso](#use-case). ¡Analicemos por qué ocurre esto y cómo solucionarlo!

El grupo al que se une un usuario depende de su configuración. Puede ser el grupo de control o el grupo variante. Un usuario entrará en un Canvas cuando cumpla todos los criterios definidos en el [paso de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=entry%20schedule#step-12-determine-your-canvas-entry-schedule). Al configurar tu Canvas, define qué porcentaje de usuarios entrará en cada variante y el grupo de control.

Si tu grupo de control es grande en comparación con tu grupo de variantes (y ésta no es tu intención), te recomendamos lo siguiente:
1. Configura tu filtro de audiencia de entrada en **«Foreground Push Enabled» (Empuje en primer plano habilitado**).
2. Configura tu filtro de audiencia de entrada para **el estado de suscripción a notificaciones push**, **el estado de suscripción a correos electrónicos** o ambos en **«Opted In»** **(Suscrito)** o **«Subscribed» (Suscrito)**.

Al crear un Canvas con un grupo de control, confirma que todos los usuarios de la audiencia de entrada puedan recibir mensajes dentro del Canvas (por ejemplo, que el Canvas contenga mensajes push y de correo electrónico).

### Casos de uso

Imaginemos el siguiente escenario:
- Un Canvas tiene una única variante y un grupo de control.
- El primer paso de la variante es una notificación push.
- El 90 % de los usuarios fueron seleccionados para entrar en la variante, y el 10 %, para entrar en el grupo de control.

![Ejemplo de Canvas con un 90 % de variante y un 10 % de grupo de control.]({% image_buster /assets/img_archive/trouble15.png %})

En este caso, el 90% de los usuarios que entren en el Canvas entrarán en la variante. 

Si echamos la vista atrás a los usuarios activos, podemos ver que, aunque hay 29 800 usuarios, solo el 64 % de ellos tienen habilitada la función push:

![Segmento con el filtro «Push Enabled» (Push habilitado) establecido en «true» (verdadero) y un número estimado de usuarios de 29 800.]({% image_buster /assets/img_archive/trouble16.png %})

Esto significa que, aunque hayamos especificado que el 90% de los usuarios introduzcan la variante, no todos esos usuarios pueden recibir realmente una notificación push. Estos usuarios que no pueden recibir una notificación push seguirán entrando en la variante a pesar de todo.