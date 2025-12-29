---
nav_title: Rutas de experimentos
article_title: Rutas de experimentos 
alias: /experiment_step/
page_order: 4
page_type: reference
description: "Este artículo trata de las Rutas de experimentos, un componente que te permite probar varias rutas Canvas entre sí y con un grupo de control en cualquier punto del recorrido del usuario."
tool: Canvas
---

# Rutas de experimentos

> Las rutas de experimentos te permiten probar varias rutas Canvas entre sí y con un grupo de control en cualquier punto del recorrido del usuario. Con este componente, puedes hacer un seguimiento del rendimiento de la ruta para tomar decisiones informadas sobre tu recorrido en Canvas.

Cuando incluyas un paso de ruta de experimentos en tu recorrido de usuario, asignará aleatoriamente a los usuarios a las diferentes rutas (o a un grupo de control opcional) que crees. Porciones de la audiencia se asignarán a diferentes rutas según los porcentajes que selecciones, lo que te permitirá probar diferentes mensajes o rutas entre sí y determinar cuál es más eficaz. 

\![Un paso de ruta de experimentos que se divide en Ruta 1, Ruta 2 y Control.]({% image_buster /assets/img/experiment_step/experiment_step.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

## Casos de uso

Las rutas de experimentos son las más adecuadas para probar la entrega, la cadencia, el texto del mensaje y las combinaciones de canales.

- **Entrega:** Compara los resultados entre mensajes enviados con diferentes [retardos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), basándote en las acciones de los usuarios[(Rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)), y utilizando [la Temporización Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#canvas).<br><br>
- **Cadencia:** Prueba varios flujos de mensajería durante un periodo determinado. Por ejemplo, podrías probar dos cadencias de incorporación diferentes:
    - Cadencia 1: Envía 2 mensajes en las 2 primeras semanas del usuario
    - Cadencia 2: Envía 3 mensajes en las 2 primeras semanas del usuario
    
    Cuando te dirijas a usuarios rezagados, puedes probar la eficacia de enviar dos mensajes de recuperación en una semana frente a enviar sólo uno.
- **Copia del mensaje:** De forma similar a una [prueba A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) estándar, puedes probar diferentes textos de mensajes para ver qué redacción da lugar a una mayor tasa de conversión.<br><br>
- **Combinaciones de canales:** Prueba la eficacia de distintas combinaciones de canales de mensajería. Por ejemplo, puedes comparar el impacto de utilizar sólo un correo electrónico frente a un correo electrónico combinado con un push.

## Requisito previo

Para utilizar rutas de experimentos, tu Canvas debe incluir eventos de conversión. Aunque no puedes añadir eventos de conversión después de haber lanzado un Canvas, puedes clonar el Canvas lanzado y añadir eventos de conversión para añadir Rutas de experimentos.

## Crear una ruta de experimentos

Para crear un componente Rutas de experimentos, añade primero un paso a tu Canvas. Arrastra y suelta el componente desde la barra lateral, o haz clic en el botón más <i class="fas fa-plus-circle"></i> situado en la parte inferior de un paso y selecciona **Rutas de experimentos**. 

En la configuración predeterminada de este componente, hay dos rutas predeterminadas, **Ruta 1** y **Ruta 2**, con un 50% de la audiencia enviada por cada ruta. Haz clic en el componente para ampliar el panel **Configuración del experimento**, y verás las opciones de configuración del componente.

### Paso 1: Elige el número de recorridos y la distribución de la audiencia

Puedes añadir hasta cuatro rutas haciendo clic en **Añadir ruta** y un grupo de control opcional marcando **Añadir un grupo de control**. Mediante las casillas de porcentaje de cada ruta, puedes especificar el porcentaje de audiencia que debe ir a cada ruta y al grupo de control. Los porcentajes indicados deben sumar 100% para poder continuar. Si quieres ajustar rápidamente todas las rutas disponibles (y el control) al mismo porcentaje, haz clic en **Distribuir rutas uniformemente**.

También puedes elegir si los usuarios del grupo de control deben continuar por el Canvas o salir después de la ventana de seguimiento de la conversión para el **Comportamiento del grupo de control**. Opcionalmente, puedes añadir una descripción para explicar a los demás qué pretende probar esta ruta de experimentos o incluir información adicional que pueda ser útil anotar.

\![Configuración de experimentos donde puedes añadir rutas y distribuir el porcentaje de usuarios en cada ruta.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
Si se habilita la re-habilitación del Canvas, los usuarios que entran en el Canvas y recorren un camino elegido al azar, volverán a recorrer el mismo camino si son re-habilitados y vuelven a entrar en el Canvas. Esto mantiene la validez del experimento y de los análisis asociados. Si quieres que el paso asigne siempre la ruta al azar, selecciona **Rutas al azar en Rutas de experimentos**. Esta opción no está disponible cuando se utilizan Caminos Ganados o Caminos Personalizados.
{% endalert %}

### Paso 2: Activa el Camino Ganador o los Caminos Personalizados (opcional) {#step-2}

Puedes elegir optimizar tu experimento activando [Ruta ganadora]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path) o [Rutas personalizadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths). Ambas opciones funcionan probando inicialmente tus rutas con una parte de tu audiencia. Una vez finalizado el experimento, los usuarios restantes y siguientes son enviados por la ruta de mejor rendimiento global (Ruta Ganadora) o por la ruta de mejor rendimiento para cada usuario (Rutas Personalizadas).

### Paso 3: Crear caminos

Por último, debes construir tus caminos descendentes. Selecciona **Hecho** y vuelve al constructor de Canvas. Haz clic en el botón más de <i class="fas fa-plus-circle"></i> que hay debajo de cada recorrido para empezar a crear recorridos utilizando las herramientas habituales del Canvas como mejor te parezca, e inicia el Canvas cuando estés listo.

\![Añadir pasos a cada ruta que parte de un componente Ruta de experimentos.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

Ten en cuenta que las rutas y sus pasos descendentes no pueden eliminarse de un Canvas una vez creados. Sin embargo, cuando se lanza, puedes modificar la distribución de la audiencia entre las rutas según te convenga. Por ejemplo, si un día después de lanzar un Canvas, llegas a la conclusión de que una ruta es superior al resto basándote en los análisis, puedes establecer esa ruta al 100% y las demás al 0%. O, según tus necesidades, puedes seguir enviando a los usuarios por varios caminos.

{% alert important %}
Para evitar la contaminación de experimentos, si tu Canvas tiene un experimento de ruta ganadora o de ruta personalizada activo o en curso y actualizas el Canvas activo, independientemente de si actualizas el propio paso de ruta de experimentos, el experimento en curso finalizará y el paso de experimentos no determinará una ruta ganadora o rutas personalizadas. Para reiniciar el experimento, puedes desconectar la Ruta de experimentos existente y lanzar una nueva, o duplicar el Canvas y lanzar un nuevo Canvas. De lo contrario, los usuarios fluirán por la ruta de experimentos como si no se hubiera seleccionado ningún método de optimización. Tampoco puedes activar Rutas personalizadas o Rutas ganadoras para un Canvas ya activo con un paso de ruta de experimentos.<br><br>Para más información, consulta [Editar lienzos después del lanzamiento]({{site.baseurl}}/post-launch_edits/).
{% endalert %}

## Seguimiento del rendimiento

En la página **de análisis de Canvas**, selecciona la ruta de experimentos para abrir una [tabla detallada]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) idéntica a la pestaña **Analizar variantes** para comparar estadísticas detalladas de rendimiento y conversión entre las distintas rutas. También puedes exportar la tabla mediante CSV y comparar los cambios porcentuales de las métricas de interés en relación con la ruta o el control que selecciones.

Cada paso de cada ruta mostrará estadísticas en la vista [Análisis de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/), como cualquier paso de Canvas. Sin embargo, ten en cuenta que el análisis de los pasos individuales **no** tiene en cuenta la estructura del experimento. El análisis en el Paso de Experimentos debe utilizarse para comparar entre trayectorias.

### Rendimiento del Camino Ganador y de los Caminos Personalizados

Aprovecha las Rutas Ganadoras para hacer un seguimiento del rendimiento durante un periodo de tiempo y luego enviar automáticamente a los usuarios siguientes por la ruta con el mejor rendimiento. Para obtener más información sobre los análisis cuando la **Ruta ganadora** o **las Rutas personalizadas** están activadas para tu experimento, consulta:

- [Camino Ganador]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path/#analytics)
- [Caminos personalizados]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths/#analytics)

### Configuraciones adicionales

Las Rutas de experimentos registrarán a los usuarios que entren en cada paso y se conviertan mientras estén en la ruta asignada. Esto hará un seguimiento de todos los eventos de conversión especificados en la configuración de Canvas. En la pestaña **Configuración adicional**, introduce cuántos días (entre 1 y 30) quieres que este experimento realice un seguimiento de las conversiones. La ventana de tiempo que especifiques aquí determinará durante cuánto tiempo se realizará el seguimiento de los eventos de conversión (elegidos en la configuración de Canvas) para el experimento. Las ventanas de conversión por evento especificadas en la configuración de Canvas no se aplicarán al seguimiento de este paso y serán sustituidas por esta ventana de conversión.

