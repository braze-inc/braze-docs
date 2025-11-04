---
nav_title: Panel de inicio
article_title: Panel de inicio (Antes resumen)
page_order: 1
page_type: reference
description: "Este artículo de referencia describe tu panel de Inicio y proporciona definiciones para las estadísticas disponibles en esta página."
tool: 
  - Reports

---

# Panel de inicio

> La página de **inicio** del panel proporciona métricas clave para que puedas hacer un seguimiento y comprender el rendimiento de tu aplicación o sitio web, y te da una visión general de alto nivel de tu base de usuarios.

La página de **inicio** tiene dos secciones principales:
- [Continúa donde lo dejaste](#pick-up-where-you-left-off)
- [Resumen de rendimiento](#peformance-overview)

\![Panel de inicio en Braze.]({% image_buster /assets/img_archive/home_dashboard.png %})

## Continúa donde lo dejaste

Puedes continuar donde lo dejaste en el panel de Braze, con acceso directo a los archivos que hayas editado o creado recientemente. Esta sección aparece en la parte superior de la página de **Inicio** del panel de Braze.

Puedes volver a visitar campañas, lienzos y segmentos editados o creados recientemente. Cada tarjeta está emparejada con etiquetas que indican el tipo de contenido (campaña, Canvas, segmento) y el estado (activo, borrador, archivado, detenido).

{% alert note %}
La sección **Retomar donde lo dejaste** aparece después de haber editado o creado una campaña, Canvas o segmento.
{% endalert %}

\![Un borrador de Canvas, un segmento activo y un borrador de campaña en la sección "Continúa donde lo dejaste".]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

## Resumen de rendimiento

Por defecto, la sección **Resumen de rendimiento** muestra los datos de los últimos 30 días de todas las aplicaciones y sitios. Todas tus métricas se calculan en función del intervalo de fechas seleccionado.

\![Intervalo de fechas y campos de aplicación en el panel de inicio.]({% image_buster /assets/img_archive/home_dashboard_select_date.png %}){: style="max-width:60%;"}

Los porcentajes se calculan basándose en el intervalo de fechas actual en comparación con el intervalo de fechas anterior, con la excepción de *los Usuarios Activos Mensuales* (MAU), que utiliza el último día del periodo anterior en lugar de un intervalo. 

Por ejemplo, si estableces tu intervalo de fechas en **Últimos 7 días** y tus *Usuarios activos diarios* muestran un aumento porcentual del 1,8%, eso significa que has tenido un 1,8% más de usuarios activos diarios esta semana en comparación con la semana pasada.

\![]({% image_buster /assets/img_archive/home_dashboard_metric_tile.png %}){: style="max-width:60%;"}

### Desglose del espectáculo

Selecciona **Mostrar desglose** en cada fila de las estadísticas del resumen de rendimiento para ver el valor de cada estadística por día para el intervalo de fechas especificado.

Expandir]({% image_buster /assets/img_archive/home_dashboard_breakdown.png %})

## Estadísticas disponibles

A continuación encontrarás las definiciones de tus estadísticas disponibles, cómo las calculamos y por qué deberían ser importantes para ti.

### Usuarios

*Usuarios* es el número total de usuarios creados en ese espacio de trabajo. Esto incluye a todos los usuarios que registramos utilizando tu aplicación o sitio web en cualquier momento, y a aquellos que podrían no estar asociados a una aplicación o sitio web específico. Este número es el porcentaje de cuántos de tus usuarios de toda la vida están representados como *usuarios activos al mes* (MAU), lo que resulta útil para ver la retención de usuarios durante un largo periodo de tiempo.

Un ratio MAU-usuario bajo puede indicar que necesitas diversificar tus canales de mensajería o aumentar tus esfuerzos para llegar a los usuarios rezagados. Para más información, consulta nuestra guía rápida sobre la [captura de usuarios caducados]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users). En general, la proporción entre MAU y tiempo de vida disminuirá inevitablemente con el tiempo debido al abandono de usuarios, pero las herramientas de Braze pueden ayudarte a minimizar este efecto manteniendo a los usuarios comprometidos durante más tiempo.

### Sesiones de por vida

*Sesiones de por vida* es el recuento total de sesiones que Braze ha registrado desde la integración. En pocas palabras, una sesión es cada vez que un usuario utiliza la aplicación o visita tu sitio web. Para una definición más precisa sobre cómo se definen las sesiones por plataforma, consulta el correspondiente
Artículos para desarrolladores de [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [Android y FireOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), o de seguimiento de sesiones [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web).

### Usuarios activos al mes

Los *usuarios activos mensuales* (MAU) son el número de usuarios que han registrado una sesión en tu aplicación o sitio web en los últimos 30 días. Las MAU se calculan cada noche con una ventana móvil de 30 días. El MAU te proporciona una buena comprensión de la salud de una aplicación o sitio durante un largo periodo de tiempo, ya que suaviza las incoherencias entre días de intensidad de uso variable.

El porcentaje junto al recuento de MAU muestra la variación de MAU de este periodo respecto al anterior.

$$\text{Change in MAU} = \frac{\text{MAU of last date in range} - \text{MAU of day before start date}}{\text{MAU of day before start date}}$$

{% alert note %}
Los usuarios anónimos también cuentan para tu MAU. En los dispositivos móviles, los usuarios anónimos dependen del dispositivo. Para los usuarios Web, los usuarios anónimos dependen de la caché del navegador.
{% endalert %}

### Usuarios activos diarios

*Usuarios activos diarios* (DAU) muestra el número de usuarios únicos que registran al menos una sesión en tu aplicación o sitio web en un día determinado. DAU puede ser una estadística útil para examinar la variabilidad diaria del uso de tu aplicación o sitio y adaptar tus campañas de mensajería para que sean lo más eficaces posible. Por ejemplo, el uso de tu aplicación puede experimentar un pico apreciable los fines de semana, lo que te informaría de que podrías llegar a más usuarios con mensajes dentro de la aplicación en esos días, en comparación con los días laborables.

### Nuevos usuarios

*Nuevos usuarios* te indica cuántos usuarios que nunca antes habían registrado una sesión han empezado a utilizar tu aplicación o sitio web. Este número es el total de nuevos usuarios durante el periodo de tiempo dado. Esta estadística puede ser muy valiosa para el seguimiento de la eficacia de tus esfuerzos publicitarios.

{% alert note %}
Cuando realices la integración inicial de Braze, todos los usuarios parecerán nuevos porque Braze nunca ha registrado una sesión para ellos.
{% endalert %}

### Adherencia

El valor de *adherencia* es una relación entre la DAU y la MAU de un periodo determinado. En esencia, la adherencia mide el porcentaje de tus MAU que vuelven a diario.

Por ejemplo, si el intervalo de fechas se establece en 30 días, una proporción del 50% indica que, de media, un usuario activo utiliza la aplicación o el sitio web durante 15 de cada 30 días, o que aproximadamente la mitad de tus usuarios activos vuelven a diario. La adherencia es una métrica importante para el éxito, porque la mayoría de los usuarios no dejan de utilizar una aplicación porque la odien activamente, sino porque no se ha convertido en parte de su rutina diaria. Por lo tanto, puedes utilizar la adherencia como indicador para medir lo bien que estás interactuando con tus usuarios.

El porcentaje junto al índice de adherencia muestra el cambio en la adherencia de este periodo en comparación con el periodo anterior.

$$\text{Change in stickiness} = \frac{\text{Stickiness of last period} - \text{Stickiness of this period}}{\text{Stickiness of last period}}$$

Los plazos para "último periodo" y "este periodo" vienen determinados por el intervalo de fechas que selecciones.

{% alert important %}
El valor MAU se calcula cada noche y no se actualizará hasta el día siguiente.
{% endalert %}

### Sesiones diarias

*Sesiones diarias* es el número de sesiones registradas en un día determinado. Comparar este valor con tu recuento de DAU puede informarte de cuántas veces tus usuarios abren la aplicación o visitan tu sitio web en los días en que registran al menos una sesión.

### Sesiones diarias por MAU

*Sesiones diarias por MAU* es la relación entre *Sesiones diarias* y MAU en un día determinado. Esta estadística te indica cuántas sesiones al día puedes esperar que se registren por MAU. Cuando se agregan y promedian, pueden darte una idea de la frecuencia relativa con la que tus usuarios utilizan tu aplicación o sitio web. Es decir, si tus *Sesiones diarias por MAU* fueran de media 0,5, entonces podrías esperar que cada MAU grabara una sesión aproximadamente cada 2 días.  

