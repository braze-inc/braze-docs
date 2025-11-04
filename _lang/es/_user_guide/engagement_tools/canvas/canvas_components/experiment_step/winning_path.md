---
nav_title: Camino Ganador
article_title: Ruta ganadora en Rutas de experimentos 
page_type: reference
description: "Este artículo de referencia trata de Winning Path, una característica que te permite automatizar tus pruebas A/B cuando está activada para un paso de ruta de experimentos."
tool: Canvas
---

# Ruta ganadora en Rutas de experimentos

> Winning Path es similar a [Winning Variant]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) en las campañas, y te permite automatizar tus pruebas A/B.

Cuando se activa la ruta ganadora en un paso de ruta de experimentos, tras un periodo de tiempo especificado, todos los usuarios posteriores serán enviados por la ruta con la tasa de conversión más alta.

## Utilizar la senda ganadora

### Paso 1: Añade un paso de ruta de experimentos

Añade una [Ruta de experimentos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) a tu Canvas y, a continuación, activa la **Ruta ganadora**.

\![Configuración en la ruta de experimentos titulada "Distribuir usuarios subsiguientes a la ruta ganadora". La sección incluye un botón para alternar la ruta de experimentos y opciones para configurar el evento de conversión y la ventana de experimentos.]({% image_buster /assets/img/experiment_step/experiment_winning_path_recurring.png %})

### Paso 2: Configurar los ajustes de la Ruta de Ganado

Especifica el evento de conversión que debe determinar el ganador. Si no hay eventos de conversión disponibles, vuelve al primer paso de la configuración de Canvas y [asigna eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events). 

Si eliges aperturas o clics como evento de conversión, asegúrate de que el primer paso de la ruta sea un [paso de Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step). Braze sólo cuenta la interacción a partir del primer paso de Mensaje en cada ruta respectiva. Si la ruta comienza con un paso diferente (como un paso de Retraso o de Ruta de audiencia) y el mensaje llega más tarde, ese mensaje no se incluirá al evaluar el rendimiento.

A continuación, configura la **Ventana del Experimento**. La **Ventana de experimentos** especifica cuánto tiempo durará el experimento antes de que se determine la Ruta de experimentos ganadora y todos los usuarios que la sigan sean enviados por esa ruta. La ventana comienza cuando el primer usuario entra en el paso.

\![Configuración de la ruta de experimentos con el evento de conversión "Clics" seleccionado para una ventana de experimentos de 12 horas.]({% image_buster /assets/img/experiment_step/experiment_winning_settings.png %})

### Paso 3: Determinar la alternativa {#statistical-significance}

Por predeterminado, si los resultados de la prueba no son suficientes para determinar un ganador estadísticamente significativo, todos los usuarios futuros serán enviados por el camino de mejor rendimiento.

Alternativamente, puedes seleccionar **Continuar enviando a todos los futuros usuarios la mezcla de rutas**. Esta opción enviará a los futuros usuarios por la mezcla de rutas según los porcentajes especificados en la distribución de rutas de experimentos.

\!["Seguir enviando a todos los futuros usuarios la mezcla de rutas" seleccionada como lo que ocurrirá a los usuarios si el resultado de la prueba no es estadísticamente significativo.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

{% alert note %}
Un Grupo de Retraso sólo aparecerá en tu distribución de rutas si tu Canvas está configurado para una entrada única y tu paso de Experimentos tiene tres rutas o menos. Los Lienzos recurrentes y desencadenados no tendrán Grupo de Retraso cuando esté activada la Trayectoria Ganadora.
{% endalert %}

### Paso 4: Añade tus rutas y lanza el Canvas

Un único componente Ruta de experimentos puede contener hasta cuatro rutas. Sin embargo, si tu Canvas está configurado para [una sola entrada](#one-time-entry), debe reservarse una ruta para el Grupo de Retraso que Braze añade automáticamente cuando se activa la Ruta Ganadora. Esto significa que para los Lienzos con entrada única, puedes añadir hasta tres rutas a tu experimento.

Termina de configurar tu Canvas como necesites, y luego lánzalo. Cuando el primer usuario haya entrado en el experimento, puedes consultar el Canvas para ver los análisis a medida que entran y [hacer un seguimiento del rendimiento de tu experimento.]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance)

Una vez concluida una Ruta Ganadora, todos los usuarios posteriores que entren en el Canvas recorrerán la Ruta Ganadora, incluidos los usuarios que volvieron a entrar y que antes estaban en el grupo de control del paso de ruta de experimentos.

## Análisis {#analytics}

Si se activó Winning Path, tu vista de análisis se separa en dos pestañas: **Experimento inicial** y **ruta ganadora**.

- **Experimento inicial:** Muestra las métricas de cada ruta durante la ventana de experimentos. Puedes ver un resumen del rendimiento de todas las rutas para los eventos de conversión especificados y qué ruta se seleccionó como ganadora.
- **Camino ganador:** Muestra sólo las métricas de la Ruta de experimentos ganadora a partir del momento en que finalizó el Experimento inicial.

## Lo que debes saber

### Entrada única {#one-time-entry}

Cuando se utilizan Trayectorias Ganadoras en un Canvas en el que los usuarios sólo pueden entrar una vez, se incluye automáticamente un Grupo de Retraso. Durante la duración del experimento, un porcentaje de usuarios se mantendrá en el Grupo de Retraso mientras los usuarios restantes entran en tus Rutas de experimentos.

\![Paso de experimentos con un grupo de retardo para la ruta de experimentos ganadora]({% image_buster /assets/img/experiment_step/experiment_one_time.png %}){: style="max-width:75%"}

Cuando finalice la prueba y se determine una Ruta Ganadora, los usuarios asignados al Grupo de Retraso serán dirigidos a la ruta elegida, y continuarán a través del Canvas.

\![Paso de experimento con un grupo de retraso enviado por la ruta ganadora]({% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}){: style="max-width:75%"}

### Entrega según zona horaria local

No recomendamos utilizar la entrega según la zona horaria local en Lienzos con rutas ganadoras. Esto se debe a que las ventanas de experimentación comienzan cuando pasa el primer usuario. Los usuarios que se encuentran en zonas horarias muy tempranas pueden entrar en el paso y desencadenar el inicio de la ventana del experimento mucho antes de lo que esperas, lo que puede dar lugar a que el Experimento concluya antes de que el grueso de tus usuarios en zonas horarias más típicas hayan tenido tiempo suficiente para entrar en el Canvas o convertirse, o ambas cosas. 

Alternativamente, si deseas utilizar la entrega local, utiliza una ventana de experimentación de 24-48 horas o más. De este modo, los usuarios de zonas horarias tempranas entran en el Canvas y desencadenan el inicio del experimento, pero queda mucho tiempo en la ventana del experimento. Los usuarios de las zonas horarias más tardías aún tendrán tiempo suficiente para entrar en el Canvas y en el Paso del Experimento con Rutas Ganadoras y, posiblemente, convertirse antes de que expire la ventana del experimento.

