---
nav_title: Medición del tamaño del segmento
article_title: Medir el tamaño de los segmentos
page_order: 5
page_type: reference
tool: 
- Segments
description: "Esta página explica cómo puedes controlar el número de miembros y el tamaño de tu segmento."
---

# Medición del tamaño del segmento

> Esta página explica cómo puedes controlar el número de miembros y el tamaño de tu segmento.

## Cálculo de la pertenencia a un segmento

Braze actualiza la pertenencia del usuario a un segmento a medida que los datos se envían a nuestros servidores y se procesan, normalmente de forma instantánea. La pertenencia a un segmento de un usuario no cambiará hasta que se haya procesado esa sesión. Por ejemplo, un usuario que cae en un segmento de usuarios caducados cuando se inicia la sesión por primera vez, saldrá inmediatamente del segmento de usuarios caducados cuando se procese la sesión.

### Cálculo del total de usuarios accesibles

Cada segmento muestra el número total de usuarios que pertenecen a ese segmento. Al filtrar por **Usuarios de todas las aplicaciones**, también muestra algunos de los canales de mensajería más utilizados (como el push web o el correo electrónico) y el número de usuarios accesibles para esos canales específicos. 

Es posible que el número de usuarios totales sea distinto del número de usuarios alcanzables por cada canal. Además, no todos los canales aparecen en la tabla de usuarios accesibles. Por ejemplo, las tarjetas de contenido, los webhooks y WhatsApp no se muestran en el desglose. Esto significa que el recuento total de usuarios alcanzables podría ser mayor que la suma de los usuarios de cada canal mostrado.

Tabla que muestra el total de usuarios accesibles desglosado por usuarios accesibles por correo electrónico, push de iOS, push de Android, push web y push de Kindle.]({% image_buster /assets/img_archive/segmenter_reachable_users.png %})

Para que un usuario aparezca como accesible a través de un canal determinado, debe tener ambos:
* Una dirección de correo electrónico válida o un token de notificaciones push asociado a su perfil; y
* Adhesión voluntaria o suscriptor a tu aplicación.

Un mismo usuario puede pertenecer a diferentes grupos de usuarios accesibles. Por ejemplo, un usuario puede tener tanto una dirección de correo electrónico como un token de notificaciones push de Android válidos y estar adherido a ambos, pero no tener ningún token de notificaciones push de iOS asociado. La diferencia entre el total de usuarios accesibles y la suma de los distintos canales es el número de usuarios que cumplen los requisitos para el segmento, pero no son accesibles a través de esos canales de comunicación.

## Estadísticas del tamaño de los segmentos

Las estadísticas estimadas se aproximan mediante el muestreo de sólo una parte de tu segmento, por lo que es de esperar que los tamaños estimados sean mayores o menores que el valor real, y que los espacios de trabajo más grandes tengan márgenes de error potencialmente mayores. Para obtener un recuento exacto de los usuarios de tu segmento, selecciona **Calcular estadísticas exactas**. La pertenencia exacta a un segmento siempre se calculará antes de que un segmento se vea afectado por un mensaje enviado en una campaña o Canvas. 

Braze proporciona las siguientes estadísticas sobre el tamaño de los segmentos. 

### Estadísticas del filtro

Para cada grupo de filtrar, puedes ver los usuarios alcanzables estimados. Selecciona **Ampliar estadísticas adicionales del embudo** para ver un desglose por canales.

\![Un grupo de filtrado con un filtro para usuarios que hayan tenido exactamente una sesión de recuento.]({% image_buster /assets/img_archive/segment_filter_stats.png %}){: style="max-width:80%;"}

## Estimación de usuarios alcanzables

Puedes ver los usuarios alcanzables estimados de todo un segmento, incluyendo los recuentos de usuarios estimados para cada canal, en el panel lateral **Usuarios alcanzables**. Esta **estimación** te muestra un rango aproximado para el tamaño de tu segmento, y una estimación de qué porcentaje de tu base global de usuarios pertenece a este segmento. Ten en cuenta que las estadísticas estimadas se almacenan en caché durante 15 minutos, a menos que realices modificaciones en tu segmento, en cuyo caso las estadísticas estimadas se actualizarán automáticamente. También puedes ver un recuento exacto de los usuarios alcanzables (tanto para el segmento en general como por canal) seleccionando **Calcular estadísticas exactas**. 


El panel "Usuarios accesibles" indica que hay entre 2,3 y 2,4 millones de usuarios estimados.]({% image_buster /assets/img_archive/reachable_users_side_panel.png %})

### Consideraciones para el recuento de estimaciones

Braze mide el número de usuarios estimados consultando a un subconjunto de tus usuarios, y luego extrapola esos resultados a toda tu audiencia. Dado que el subconjunto de usuarios que consulta Braze puede diferir cada vez que calculamos esta estimación, ésta también puede cambiar en casos en los que el número de miembros de tu audiencia técnicamente debería haber permanecido igual. Por ejemplo, si reordenas tus filtros o vuelves a comprobar el mismo segmento en otro momento, es posible que el recuento estimado cambie (aunque **Calcular estadísticas exactas** revelaría los mismos resultados si tu segmento no hubiera cambiado).

Si tienes una gran población de usuarios en tu espacio de trabajo, puede que veas más variación entre tus recuentos estimados en comparación con tus recuentos de cálculo exactos, especialmente en los casos en que tu segmento sea un porcentaje muy pequeño de la población total de tu espacio de trabajo. Esto se debe a que Braze mide la estimación consultando a un subconjunto de tus usuarios y extrapolando los resultados a toda tu base de usuarios. Para bases de usuarios más grandes, cabe esperar mayores diferencias entre los recuentos estimados y los exactos.

Los segmentos muy pequeños tendrán un rango estimado que incluye 0, lo que significa que el porcentaje del total de usuarios puede redondearse a 0. En estos casos, **Calcular estadísticas exactas** te ayudará a ver un recuento exacto del tamaño de tu segmento, que en realidad puede no ser 0.

\![El panel lateral "Usuarios accesibles".]({% image_buster /assets/img_archive/reachable_users_panel.png %})

### Usuarios alcanzables por canal

Para ver el número de usuarios accesibles para cada canal de mensajería, selecciona **Mostrar desglose** en el panel **Usuarios accesibles**. Muestra algunos de los canales de mensajería más utilizados (como la notificación push web o el correo electrónico) y el número de usuarios accesibles para esos canales específicos. 

La métrica _Total_ representa a los usuarios únicos. Por ejemplo, si un usuario tiene tanto push de Android como push de iOS, se contará para ambas filas, pero sólo contará como 1 usuario en la fila _Total_.

Sin embargo, es posible que el número de usuarios totales sea distinto de la suma de usuarios alcanzables por cada canal, ya que un mismo usuario puede pertenecer a distintos grupos de usuarios alcanzables. Por ejemplo, un usuario puede tener tanto una dirección de correo electrónico como un token de notificaciones push de Android válidos y estar adherido a ambos, pero no tener ningún token de notificaciones push de iOS asociado. 

Ten en cuenta que no todos los canales aparecen en la tabla de **usuarios alcanzables** (como las tarjetas de contenido, los webhooks y WhatsApp). Por ejemplo, si tienes usuarios sólo localizables a través de Whatsapp, se reflejarán en el _Total_ pero no en ninguna de las filas específicas del canal. Esto significa que el recuento total de usuarios alcanzables puede ser diferente de la suma de los usuarios de cada canal mostrado.

En los casos en que el _Total_ es superior a la suma de los canales, la brecha representa el número de usuarios cualificados para el segmento pero a los que no se puede llegar a través de esos canales de comunicación.

Para que un usuario aparezca como accesible a través de un canal determinado, debe tener:
- Una dirección de correo electrónico válida o un token de notificaciones push asociado a su perfil, y
- Adhesión voluntaria o suscripción a tu aplicación.

## Calcular estadísticas exactas 

Para ver un recuento exacto del número de usuarios de tu segmento, selecciona **Calcular estadísticas exactas** en el panel **Usuarios alcanzables**.

Para actualizar las estadísticas de un cálculo que hayas ejecutado previamente, selecciona **Actualizar estadísticas exactas**. La fecha de la última vez que se ejecutó este cálculo se actualizará automáticamente.

Ten en cuenta que la precisión de un cálculo es sólo del 99,999% o superior. Por eso, en los segmentos grandes, puedes notar ligeras variaciones -incluso al calcular estadísticas exactas-, lo cual es un comportamiento normal. Además, los resultados de las estadísticas exactas se almacenan en caché durante 24 horas, a menos que realices modificaciones en tu segmento, en cuyo caso puedes volver a calcular las estadísticas exactas.

\![El panel "Usuarios accesibles" con una opción para mostrar el desglose.]({% image_buster /assets/img_archive/reachable_users_breakdown.png %})

Las estadísticas a nivel de filtro siempre serán estimadas, aunque calcules las estadísticas exactas. **Calcular** estadísticas exactas sólo calcula las estadísticas exactas a nivel de segmento, no a nivel de filtro o grupo de filtros. Este cálculo puede tardar unos minutos en ejecutarse. Los espacios de trabajo más grandes, en particular, pueden requerir períodos más largos para completar los cálculos. Puedes hacer un seguimiento de tu progreso en la barra de progreso del panel de **usuarios de Reachable**. Cuando se prevea que un cálculo va a durar más de cinco minutos, Braze te enviará los resultados por correo electrónico. 

Braze da prioridad a un cálculo a la vez por espacio de trabajo, por lo que ejecutar varios cálculos a la vez provocará retrasos. Puedes seleccionar **Ver cola de cálculo** para ver qué segmentos van por delante del tuyo, su progreso y su iniciador, y hacerte una idea de cuándo puede priorizarse tu cálculo.

Cola de cálculo con un cálculo.]({% image_buster /assets/img_archive/calculation_queue.png %})

Puedes cancelar un cálculo estadístico exacto seleccionando **Cancelar**. Esto puede ser beneficioso si hay varios cálculos en la cola y quieres dar prioridad a otro cálculo en primer lugar. 

\![Un cálculo activo con la opción de cancelar]({% image_buster /assets/img_archive/cancel_calculation.png %}){: style="max-width:25%"}

## Visualización del tamaño histórico de los miembros del segmento

Para todos los segmentos, puedes ver un gráfico de afiliación histórica que muestra la afiliación estimada del segmento para cada día. Este gráfico muestra cómo ha cambiado el tamaño de tu segmento a lo largo del tiempo. Utiliza el desplegable para filtrar la pertenencia a un segmento por intervalo de fechas.

\![Utiliza el desplegable Afiliación histórica para filtrar la afiliación a segmentos por intervalo de fechas.]({% image_buster /assets/img_archive/historical_membership2.png %})

Como el objetivo de este gráfico es darte una idea de las tendencias generales de pertenencia a un segmento, el recuento diario es una estimación, de forma similar a como el tamaño del segmento es una estimación antes de que selecciones **Calcular estadísticas exactas**. Y como este gráfico muestra estimaciones, es posible que el tamaño de tu segmento aparezca como "0" en este gráfico, aunque su tamaño real (que puede determinarse tras seleccionar **Calcular estadísticas exactas**) no sea "0". Es especialmente probable que el gráfico muestre una estimación de "0" si tu segmento es muy pequeño en relación con el tamaño de la población de tu espacio de trabajo.

Por ejemplo, supongamos que tu espacio de trabajo contiene 100 millones de usuarios y tu segmento tiene unos 700 usuarios. Es posible que algunos días no haya usuarios en el segmento, y que ningún usuario caiga en el intervalo de contenedores aleatorios utilizado para la estimación histórica de miembros, lo que da como resultado un recuento de miembros de un día de 0.

Braze calcula el recuento de miembros del segmento consultando a un subconjunto de tus usuarios, y luego extrapolando esos resultados a toda tu audiencia. Esto significa que los resultados del gráfico sólo proporcionan una estimación de lo que podría ser la pertenencia a un segmento ese día, y es de esperar que también fluctúe de un día para otro porque cada día se puede consultar a una muestra diferente de usuarios para obtener esta estimación.

{% alert note %}
Todas las estimaciones pueden ser superiores o inferiores al valor indicado en aproximadamente un 1% del tamaño de la población total de tu espacio de trabajo. Los espacios de trabajo más grandes y con más usuarios tienen más probabilidades de tener estimaciones que pueden diferir de los cálculos exactos en una cantidad numérica mayor, aunque la diferencia siga siendo del 1% de la población de usuarios del espacio de trabajo. Esto significa que cabe esperar mayores diferencias entre las estimaciones y los recuentos exactos en los espacios de trabajo grandes.
{% endalert %}

### Motivos de los cambios significativos

El recuento de afiliados puede cambiar significativamente por diversas razones, como las que figuran en este cuadro.

| Razón | Ejemplo |
| --- | --- |
| Comportamiento normal del usuario | Los usuarios se suscriben tras una campaña especialmente exitosa. |
| Los usuarios se importan por CSV | Se importó un archivo CSV de usuarios que aumentó significativamente el número de miembros del segmento. |
| Se modifican los criterios de segmentación de la audiencia | Se modificaron las reglas de audiencia de un segmento existente (como los filtros), provocando cambios significativos en la composición del segmento. |
| Se eliminan usuarios | Se eliminó un número importante de usuarios. |
| Una integración del socio sincronizada con Braze | Un tercero envió datos a Braze que influyeron significativamente en la pertenencia a un segmento. |
| Los usuarios inactivos son archivados | Se archivó un número importante de perfiles inactivos. Por ejemplo, un gran número de usuarios importados en CSV nunca registran actividad y se archivan al mismo tiempo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
