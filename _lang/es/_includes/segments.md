{% if include.section == "Differing audience size" %}

El tamaño de la población objetivo que se muestra en una campaña o Canvas puede diferir del [tamaño de la audiencia alcanzable para un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size#segment-membership-calculation), incluso si estás añadiendo directamente ese segmento a tu campaña o Canvas sin filtros adicionales.
Esto puede ocurrir por varias razones:

- Cuando un grupo de control global se aplica a una campaña o Canvas, los usuarios de ese grupo de control global quedan excluidos en el recuento de usuarios accesibles.
- El tamaño de la población objetivo en una campaña o Canvas excluye a los usuarios con los que no se puede contactar a través de varios canales de mensajería; el comportamiento difiere de un canal a otro. Por ejemplo, la audiencia alcanzable para una campaña o Canvas excluye a los usuarios que se han dado de baja, han sido marcados como correo no deseado (en el caso de los correos electrónicos) o han recibido un rebote blando (en el caso de los correos electrónicos). El segmento en sí, sin embargo, sólo excluye las adhesiones voluntarias cuando muestra el número estimado de usuarios alcanzables por correo electrónico. 
- Braze sólo envía mensajes SMS a usuarios dentro del grupo de suscripción seleccionado, por lo que la población objetivo de SMS para una campaña o Canvas también excluirá a cualquier usuario que no forme parte de tu grupo de suscripción seleccionado.

{% endif %}

{% if include.section == "Refresh settings" %}

Si no necesitas que tu extensión se actualice de forma periódica, puedes guardarla sin utilizar la configuración de actualización, y Braze generará por defecto tu Extensión de segmento basándose en tu número de usuarios en ese momento. Utiliza el comportamiento predeterminado si sólo quieres generar la audiencia una vez y luego dirigirte a ella con una campaña puntual.

Tu segmento siempre empezará a procesarse después del guardado inicial. Cada vez que se actualice tu segmento, Braze volverá a ejecutar el segmento y actualizará la pertenencia al mismo para reflejar los usuarios de tu segmento en el momento de la actualización. Esto puede ayudar a que tus campañas recurrentes lleguen a los usuarios más relevantes.

#### Configurar una actualización periódica

Para establecer una programación recurrente designando la configuración de actualización, selecciona **Habilitar actualización**. La opción de designar la configuración de actualización está disponible para todos los tipos de extensiones de segmento, incluidos los segmentos SQL, las extensiones de segmento CDI y las extensiones de segmento basadas en formularios simples.

{% alert important %}
Para optimizar tu gestión de datos, la configuración de actualización se desactiva automáticamente para las extensiones de segmento no utilizadas. Las extensiones de segmento se consideran no utilizadas cuando lo están:

- No se utiliza en ninguna campaña, lienzo o segmento activo o inactivo (borrador, detenido, archivado).
- No tuvo modificaciones en los últimos 7 días

Braze notificará al contacto de la empresa y al creador de la extensión si se desactiva esta configuración. La opción de regenerar las extensiones diariamente puede volver a activarse en cualquier momento.
{% endalert %}

#### Seleccionar tu configuración de actualización

![Configuración del intervalo de actualización con una frecuencia de actualización semanal, hora de inicio a las 10 de la mañana y lunes seleccionado como día.]({% image_buster /assets/img/segment/segment_interval_settings.png %}){: style="max-width:50%;"}

En el panel **Configuración del intervalo de actualización**, puedes seleccionar la frecuencia con la que se actualizará esta extensión de segmento: cada hora, cada día, cada semana o cada mes. También se te pedirá que selecciones la hora concreta (que esté en la zona horaria de tu empresa) a la que se produciría la actualización, por ejemplo:

- Si tienes una campaña de correo electrónico que se envía todos los lunes a las 11 de la mañana, hora de la empresa, y quieres asegurarte de que tu segmento se actualiza justo antes de enviarlo, debes elegir un programa de actualización semanal a las 10 de la mañana de los lunes.
- Si quieres que tu segmento se actualice todos los días, selecciona la frecuencia de actualización diaria y, a continuación, elige la hora del día en que se actualizará.

{% alert note %}
La posibilidad de establecer un programa de actualización por horas no está disponible para las extensiones de segmento basadas en formularios (pero puedes establecer programas diarios, semanales o mensuales).
{% endalert %}

#### Consumo de créditos y costes adicionales

Como las actualizaciones vuelven a ejecutar la consulta de tu segmento, cada actualización de segmentos SQL consumirá créditos de segmentos SQL, y cada actualización de extensiones de segmento CDI supondrá un coste dentro de tu almacén de datos de terceros.

{% alert note %}
La actualización de los segmentos podría requerir hasta 60 minutos debido a los tiempos de procesamiento de los datos. Los segmentos que estén actualmente en proceso de actualización tendrán un estado de "Procesando" dentro de tu lista de Extensiones de segmento. Esto tiene un par de implicaciones:

- Para terminar de procesar tu segmento antes de una hora determinada, elige una hora de actualización que sea 60 minutos antes. 
- Sólo puede producirse una actualización a la vez para una extensión de segmento específica. Si hay un conflicto en el que se inicia una nueva actualización cuando una actualización existente ya ha comenzado a procesarse, Braze cancelará la nueva solicitud de actualización y continuará el procesamiento en curso.
{% endalert %}

#### Criterios para desactivar automáticamente las extensiones obsoletas

Las actualizaciones programadas se desactivan automáticamente cuando una extensión de segmento caduca. Una extensión de segmento es antigua si cumple los siguientes criterios:

- No se ha utilizado en ninguna campaña o Canvas activos
- No se utiliza en ningún segmento que esté en una campaña o Canvas activos
- No se utiliza en ningún segmento que tenga activado el [seguimiento de análisis]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) 
- No se ha modificado en más de siete días
- No se ha añadido a una campaña o Canvas (incluidos borradores), o segmento en más de siete días

Si la actualización programada está desactivada para una extensión de segmento, dicha extensión tendrá una notificación que así lo indique.

![Una notificación que dice que "Las actualizaciones programadas se han desactivado para esta extensión porque no se utiliza en ninguna campaña, lienzo o segmento activos". La extensión de segmento se desactivó el 23 de febrero de 2025 a las 12:00 AM."]({% image_buster /assets/img/segment/segment_extension_disabled.png %})

Cuando estés listo para utilizar una Extensión de segmento obsoleta, revisa la configuración de actualización, selecciona el programa de actualización que se ajuste a tu caso de uso y, a continuación, guarda las modificaciones.

{% endif %}