---
nav_title: Solución de problemas
article_title: Solución de problemas de lonas
page_order: 11
page_type: reference
description: "Esta página proporciona pasos para la solución de problemas con los Lienzos."
tool: Canvas
---

# Solución de problemas de lonas

> Esta página te ayuda a solucionar problemas con tus Lienzos.

## ¿Por qué un usuario no ha recibido un paso en Canvas desencadenado?

Primero, confirma que el evento personalizado se está pasando a Braze. Ve a **Análisis** > **Informe de eventos personalizados** y, a continuación, selecciona el evento personalizado y el intervalo de fechas correspondientes. Si el evento no se muestra, confirma que se ha configurado correctamente y que el usuario ha realizado la acción correcta.

Si aparece el evento personalizado, soluciona el problema haciendo lo siguiente:

- Comprueba la descarga del perfil del usuario para confirmar que desencadenó el evento y cuándo lo hizo. Si se desencadenó el evento, compara la marca de tiempo de cuando se desencadenó el evento con la hora en que el Canvas salió en vivo. El evento puede haberse desencadenado antes de que el Canvas estuviera en vivo.
- Revisa los registros de cambios del Canvas y de cualquier segmento utilizado en la segmentación para determinar si el usuario estaba en el segmento cuando se desencadenó su evento personalizado. Si no estuvieran en el segmento, no habrían recibido el paso en Canvas.
- Comprueba si el usuario fue introducido en un grupo de control mediante segmentación y, en consecuencia, se le impidió recibir el paso en Canvas.
- Si hay un retraso programado, comprueba si el evento personalizado del usuario se desencadenó antes del retraso. Si el evento se hubiera desencadenado antes del retraso, no habrían recibido el paso en Canvas.

{% alert note %}
Los mensajes dentro de la aplicación sólo pueden desencadenarse por eventos enviados a través del SDK, no de la API REST.
{% endalert %}

## ¿Por qué mi Canvas no se envía como esperaba?

Los Canvas son robustos y complejos, y sabemos que dedicas tiempo y cuidado al crearlos. Así que, si ves que tu Canvas no se envía como quieres, te recomendamos que compruebes el horario de tu Canvas, la audiencia de entrada y la configuración de entrada, y que revises los pasos para [crear un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

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
- ¿Has confirmado que el segmento contiene algún usuario?
- ¿Has añadido algún filtro adicional que limite el número de usuarios que entran en el Canvas?
- ¿Los usuarios cumplen los requisitos para recibir el primer paso de tus variantes? Por ejemplo, si el primer paso de tu Canvas es una notificación push, pero toda la audiencia de entrada está deshabilitada para push, ningún usuario recibirá mensajes.

## ¿Por qué mi audiencia no se dividió por igual entre el grupo de control y el grupo de variantes?

Al crear tu Canvas, puede que esperases que tu audiencia se dividiera a partes iguales entre tu grupo de control y tu grupo de variantes, como en el siguiente [caso de uso](#use-case). Hablemos de por qué y de cómo solucionarlo.

El grupo al que se une un usuario depende de su configuración. Puede ser el grupo de control o el grupo variante. Un usuario entrará en un Canvas cuando cumpla todos los criterios definidos en el [Paso en]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=entry%20schedule#step-12-determine-your-canvas-entry-schedule) Canvas. Al configurar tu Canvas, define qué porcentaje de usuarios entrará en cada variante y el grupo de control.

Si tu grupo de control es grande en comparación con tu grupo de variantes (y ésta no es tu intención), te recomendamos lo siguiente:
1. Establece que el filtro de audiencia de entrada **sea Push en primer plano habilitado**.
2. Establece el filtro de audiencia de entrada para el **estado de suscripción push**, el **estado de suscripción por correo electrónico**, o ambos, como **Adherido** o **Suscrito**.

Al crear un Canvas con un grupo de control, confirma que todos los usuarios de la audiencia de entrada pueden recibir mensajes dentro del Canvas (como que el Canvas contiene mensajes push y por correo electrónico).

### Casos de uso

Imaginemos el siguiente escenario:
- Un Canvas tiene una única variante y un grupo de control.
- El primer paso de la variante es una notificación push.
- El 90 % de los usuarios fueron seleccionados para entrar en la variante, y el 10 %, para entrar en el grupo de control.

![Ejemplo de Canvas con un 90% de variante y un 10% de grupo de control.]({% image_buster /assets/img_archive/trouble15.png %})

En este caso, el 90% de los usuarios que entren en el Canvas entrarán en la variante. 

Si volvemos la vista a los usuarios activos, podemos ver que, aunque contiene 29,8k usuarios, sólo el 64% de ellos tienen habilitado el push:

![Segmento con el filtro "Push habilitado" ajustado a "true", y una estimación de usuarios de 29,8k.]({% image_buster /assets/img_archive/trouble16.png %})

Esto significa que, aunque hayamos especificado que el 90% de los usuarios introduzcan la variante, no todos esos usuarios pueden recibir realmente una notificación push. Estos usuarios que no pueden recibir una notificación push seguirán entrando en la variante a pesar de todo.