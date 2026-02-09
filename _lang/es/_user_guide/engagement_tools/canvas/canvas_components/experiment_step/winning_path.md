---
nav_title: Recorrido ganador
article_title: Recorrido ganador en recorridos de experimentos 
page_type: reference
description: "Este artículo de referencia trata sobre Winning Path, una función que le permite automatizar sus pruebas A/B cuando está activada para un paso de Experiment Path."
tool: Canvas
---

# Recorrido ganador en recorridos de experimentos

> La Ruta ganadora es similar a la [Variante ganadora]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) en las campañas, y te permite automatizar tus pruebas A/B.

Cuando se activa Winning Path en un paso de ruta de experimentos, tras un periodo de tiempo especificado, todos los usuarios posteriores son enviados por la ruta con la tasa de conversión más alta.

## Utilizar la senda ganadora

### Paso 1: Añade un paso de ruta de experimentos

Añade una [Ruta de Experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) a tu Lienzo y activa la **Ruta Ganadora**.

![Ajustes en la Ruta de Experimento titulada "Distribuir Usuarios Subsiguientes a la Ruta Ganadora". La sección incluye un botón para alternar la Ruta ganadora y opciones para configurar el evento de conversión y la ventana de experimentos.]({% image_buster /assets/img/experiment_step/experiment_winning_path_recurring.png %})

### Paso 2: Configurar los ajustes de la Ruta ganadora

Especifique el evento de conversión que debe determinar el ganador. Si no hay eventos de conversión disponibles, vuelva al primer paso de la configuración de Canvas y [asigne eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events). 

Si eliges aperturas o clics como evento de conversión, asegúrate de que el primer paso de la ruta sea un [paso de Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step). Braze sólo cuenta la interacción a partir del primer paso de Mensaje en cada ruta respectiva. Si la ruta comienza con un paso diferente (como un paso de Retraso o de Ruta de audiencia) y el mensaje llega más tarde, ese mensaje no se incluirá al evaluar el rendimiento.

A continuación, configure la **Ventana del experimento**. La **Ventana de experimentos** especifica cuánto tiempo dura el experimento antes de que se determine la Ruta de experimentos ganadora y todos los usuarios que la sigan sean enviados por esa ruta. La ventana comienza cuando el primer usuario entra en el paso.

![Configuración de la ruta de experimentos con el evento de conversión "Clics" seleccionado para una ventana de experimentos de 12 horas.]({% image_buster /assets/img/experiment_step/experiment_winning_settings.png %})

### Paso 3: Determinar la alternativa {#statistical-significance}

Por defecto, si los resultados de la prueba no son suficientes para determinar un ganador estadísticamente significativo, todos los futuros usuarios son enviados por la ruta de mejor rendimiento. Alternativamente, puedes seleccionar **Continuar enviando a todos los futuros usuarios la mezcla de rutas**. Esta opción envía a los futuros usuarios por la mezcla de rutas según los porcentajes especificados en la distribución de rutas de experimentos.

!["Seguir enviando a todos los futuros usuarios la mezcla de rutas" seleccionada como lo que ocurre a los usuarios si el resultado de la prueba no es estadísticamente significativo.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

{% alert note %}
Un Grupo de Retraso sólo aparece en tu distribución de rutas si tu Canvas está configurado para una entrada única y tu paso de Experimentos tiene tres rutas o menos. Los Lienzos recurrentes y desencadenados no tienen Grupo de Retraso cuando está activada la Trayectoria Ganadora.
{% endalert %}

### Paso 4: Añade tus rutas y lanza el Canvas

Un único componente Ruta de experimento puede contener hasta cuatro rutas. Sin embargo, si tu Canvas está configurado para [una sola entrada](#one-time-entry), debe reservarse una ruta para el Grupo de Retraso que Braze añade automáticamente cuando se activa la Ruta ganadora. Esto significa que para los lienzos con entrada única, puede añadir hasta tres caminos a su experimento.

Termina de configurar tu Canvas como necesites y lánzalo. Cuando el primer usuario haya entrado en el experimento, puedes consultar el Canvas para ver los análisis a medida que entran y [hacer un seguimiento del rendimiento de tu experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance).

Una vez concluida una Ruta Ganadora, todos los usuarios posteriores que entren en el Canvas recorrerán la Ruta Ganadora, incluidos los usuarios que volvieron a entrar y que antes estaban en el grupo de control del paso de ruta de experimentos.

## Análisis {#analytics}

Si Winning Path está activado, tu vista de análisis se separa en dos pestañas: **Experimento inicial** y **trayectoria ganadora**.

- **Experimento inicial:** Muestra las métricas de cada ruta durante la ventana del experimento. Puede ver un resumen de cómo se comportaron todas las rutas para los eventos de conversión especificados y qué ruta se seleccionó como ganadora.
- **Recorrido ganador:** Muestra sólo las métricas de la ruta ganadora a partir del momento en que finalizó el experimento inicial.

## Lo que hay que saber

### Entrada única {#one-time-entry}

Cuando se utilizan Rutas Ganadoras en un Lienzo en el que los usuarios sólo pueden entrar una vez, se incluye automáticamente un Grupo de Retraso. Durante la duración del experimento, un porcentaje de usuarios se mantiene en el Grupo de Retraso mientras los usuarios restantes entran en tus Rutas de experimentos.

![Paso experimental con un grupo de retardo para la Ruta ganadora]({% image_buster /assets/img/experiment_step/experiment_one_time.png %}){: style="max-width:75%"}

Cuando finaliza la prueba y se determina una Ruta Ganadora, los usuarios asignados al Grupo de Retraso se dirigen a la ruta elegida y continúan por el Canvas.

![Paso del experimento con un grupo de retardo enviado por la Ruta ganadora]({% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}){: style="max-width:75%"}

### Entrega según la zona horaria local

No recomendamos utilizar la entrega en hora local en Lienzos con trayectorias ganadoras. Esto se debe a que las ventanas de experimentación comienzan cuando pasa el primer usuario. Los usuarios que se encuentran en zonas horarias muy tempranas pueden entrar en el paso y activar el inicio de la ventana del experimento mucho antes de lo que usted espera, lo que puede provocar que el Experimento concluya antes de que el grueso de sus usuarios en zonas horarias más típicas haya tenido tiempo suficiente para entrar en el Lienzo o convertirse, o ambas cosas. 

Alternativamente, si desea utilizar la entrega local, utilice una ventana de experimentación de 24-48 horas o más. De este modo, los usuarios de zonas horarias tempranas entran en el lienzo y activan el experimento para que comience, pero queda mucho tiempo en la ventana del experimento. Los usuarios de zonas horarias más tardías aún tienen tiempo suficiente para entrar en el Canvas y en el Paso del Experimento con Rutas de experimentos ganadoras y, posiblemente, convertirse antes de que expire la ventana del experimento.

### Variantes basadas en los clics

Si estás configurando una variante de Winning Path basada en clics, cada interacción cuenta como un clic a menos que Braze la identifique como un clic para cancelar suscripción.
