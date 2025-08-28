---
nav_title: Recorridos de experimentos 
article_title: Recorridos de experimentos 
alias: /experiment_step/
page_order: 4
page_type: reference
description: "Este artículo trata sobre las Rutas de experimentación, un componente que le permite probar múltiples rutas de Canvas entre sí y con un grupo de control en cualquier punto del recorrido del usuario."
tool: Canvas
---

# Recorridos de experimentos

> Las rutas de experimentación le permiten probar varias rutas de Canvas entre sí y con un grupo de control en cualquier punto del recorrido del usuario. Con este componente, puedes hacer un seguimiento del rendimiento de la ruta para tomar decisiones informadas sobre tu recorrido en Canvas.

Cuando incluyas un paso de ruta de experimentos en tu recorrido de usuario, asignará aleatoriamente a los usuarios a las diferentes rutas (o a un grupo de control opcional) que crees. Porciones de la audiencia se asignarán a diferentes rutas según los porcentajes que selecciones, lo que te permitirá probar diferentes mensajes o rutas entre sí y determinar cuál es más eficaz. 

![Un paso de ruta de experimentos que se divide en ruta 1, ruta 2 y control.]({% image_buster /assets/img/experiment_step/experiment_step.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

## Ejemplos

Las rutas de experimentación son las más adecuadas para probar la entrega, la cadencia, el texto del mensaje y las combinaciones de canales.

- **Entrega:** Comparar los resultados entre mensajes enviados con diferentes [retardos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), en función de las acciones de los usuarios[(Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)), y utilizando [la Temporización Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#canvas).<br><br>
- **Cadencia:** Pruebe varios flujos de mensajería durante un periodo determinado. Por ejemplo, podrías probar dos cadencias de incorporación diferentes:
    - Cadencia 1: Enviar 2 mensajes en las 2 primeras semanas del usuario
    - Cadencia 2: Enviar 3 mensajes en las 2 primeras semanas del usuario
    
    Cuando te dirijas a usuarios rezagados, puedes probar la eficacia de enviar dos mensajes de recuperación en una semana frente a enviar solo uno.
- **Copia del mensaje:** De forma similar a una [prueba A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) estándar, puede probar diferentes textos de mensajes para ver qué redacción da lugar a una mayor tasa de conversión.<br><br>
- **Combinaciones de canales:** Probar la eficacia de distintas combinaciones de canales de mensajes. Por ejemplo, puede comparar el impacto de utilizar sólo un correo electrónico frente a un correo electrónico combinado con un push.

## Requisito previo

Para utilizar rutas de experimentos, tu Canvas debe incluir eventos de conversión. Aunque no puedes añadir eventos de conversión después de haber lanzado un Canvas, puedes clonar el Canvas lanzado y añadir eventos de conversión para añadir Rutas de experimentos.

## Crear una ruta de experimentos

Para crear un componente de Rutas de Experimento, primero añada un paso a su Lienzo. Arrastre y suelte el componente desde la barra lateral, o haga clic en el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y seleccione **Rutas de experimentación**. 

En la configuración por defecto de este componente, hay dos rutas por defecto, **Ruta 1** y **Ruta 2**, con el 50% de la audiencia siendo enviada por cada ruta. Haga clic en el componente para ampliar el panel **Configuración del experimento**, y verá las opciones de configuración del componente.

### Paso 1: Elija el número de vías y la distribución de la audiencia

Puede añadir hasta cuatro rutas haciendo clic en **Añadir ruta** y un grupo de control opcional marcando **Añadir un grupo de control**. Utilizando las casillas de porcentaje para cada ruta, puede especificar el porcentaje de la audiencia que debe ir a cada ruta y al grupo de control. Los porcentajes indicados deben sumar 100% para poder continuar. Si desea ajustar rápidamente todas las rutas disponibles (y el control) al mismo porcentaje, haga clic en **Distribuir rutas uniformemente**.

También puede elegir si los usuarios del grupo de control deben continuar por el Canvas o salir después de la ventana de seguimiento de conversiones para el **Comportamiento del grupo de control**. Opcionalmente, puede añadir una descripción para explicar a los demás lo que esta ruta de experimento pretende probar o incluir información adicional que podría ser útil tener en cuenta.

![Configuración de experimentos donde puedes añadir rutas y distribuir el porcentaje de usuarios en cada ruta.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
Si se activa la reelegibilidad del Canvas, los usuarios que entren en el Canvas y recorran un camino elegido al azar volverán a recorrer el mismo camino si se convierten en reelegibles y vuelven a entrar en el Canvas. Esto mantiene la validez del experimento y de los análisis asociados. Si desea que el paso asigne siempre de forma aleatoria las rutas, seleccione **Rutas aleatorias en Rutas del experimento**. Esta opción no está disponible cuando se utilizan Rutas Ganadoras o Rutas Personalizadas.
{% endalert %}

### Paso 2: Activar Trayectoria ganadora o Trayectorias personalizadas (opcional) {#step-2}

Puede optar por optimizar su experimento activando [Trayectoria ganadora]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path) o [Trayectorias personalizadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths). Ambas opciones funcionan probando inicialmente tus rutas con una parte de tu audiencia. Una vez finalizado el experimento, los usuarios restantes y siguientes son enviados por la ruta de mejor rendimiento global (Ruta Ganadora) o por la ruta de mejor rendimiento para cada usuario (Rutas Personalizadas).

### Paso 3: Crear rutas

Por último, debes construir tus rutas descendentes. Seleccione **Hecho** y vuelva al Canvas Builder. Haga clic en el botón <i class="fas fa-plus-circle"></i> más debajo de cada trayecto para empezar a crear trayectos utilizando las herramientas habituales del lienzo según le convenga, e inicie el lienzo cuando esté listo.

![Añadir pasos a cada ruta que se separa de un componente Ruta de experimentos.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

Tenga en cuenta que las rutas y sus pasos descendentes no pueden eliminarse de un lienzo una vez creados. Sin embargo, cuando se lanza, puedes modificar la distribución de la audiencia entre las rutas según te convenga. Por ejemplo, si un día después de lanzar un Canvas, llega a la conclusión de que una ruta es superior al resto basándose en los análisis, puede establecer esa ruta al 100% y las demás al 0%. O, según tus necesidades, puedes seguir enviando a los usuarios por varias rutas.

{% alert important %}
Para evitar la contaminación de experimentos, si tu Canvas tiene un experimento activo o en curso y actualizas el Canvas activo (aunque no sea al paso de ruta de experimentos), el experimento en curso finalizará. Para reiniciar el experimento, puedes desconectar la Ruta de experimentos existente y lanzar una nueva, o duplicar el Canvas y lanzar un nuevo Canvas. Tampoco puede activar Rutas Personalizadas o Rutas Ganadoras para un Lienzo ya activo con un paso de Ruta de Experimento.<br><br>Para más información, consulta [Editar Canvas después del lanzamiento]({{site.baseurl}}/post-launch_edits/).
{% endalert %}

## Seguimiento del rendimiento

En la página **Canvas Analytics**, haga clic en la ruta del experimento para abrir una [tabla detallada]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) idéntica a la pestaña **Analizar variantes** para comparar estadísticas detalladas de rendimiento y conversión entre rutas. También puede exportar la tabla mediante CSV y comparar los cambios porcentuales de las métricas de interés en relación con la ruta o el control que seleccione.

Cada paso de cada ruta mostrará estadísticas en la vista [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/), igual que cualquier paso de Canvas. Sin embargo, ten en cuenta que el análisis de los pasos individuales **no** tiene en cuenta la estructura del experimento. El análisis en el Paso de Experimentos debe utilizarse para comparar entre rutas.

### Rendimiento de la Ruta ganadora y las Rutas personalizadas

Aprovecha las Rutas ganadoras para hacer un seguimiento del rendimiento durante un período de tiempo y luego enviar automáticamente a los usuarios siguientes por la ruta con el mejor rendimiento. Para obtener más información sobre los análisis cuando la **Ruta ganadora** o **las Rutas personalizadas** están activadas para tu experimento, consulta:

- [Recorrido ganador]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path/#analytics)
- [Recorridos personalizados]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths/#analytics)

### Configuración adicional

Las Rutas de Experimento registrarán los usuarios que entran en cada paso y se convierten mientras están en la ruta asignada. Esto rastreará todos los eventos de conversión especificados en la configuración de Canvas. En la pestaña **Configuración adicional**, introduzca cuántos días (entre 1 y 30) desea que este experimento realice un seguimiento de las conversiones. La ventana de tiempo que especifiques aquí determinará durante cuánto tiempo se realizará el seguimiento de los eventos de conversión (elegidos en la configuración de Canvas) para el experimento. Las ventanas de conversión por evento especificadas en la configuración de Canvas no se aplicarán al seguimiento de este paso y serán sustituidas por esta ventana de conversión.

