---
nav_title: Medir el tamaño del segmento
article_title: Medir el tamaño del segmento
page_order: 5
page_type: reference
tool: 
- Segments
description: "Esta página explica cómo puedes supervisar la composición y el tamaño de tu segmento."
---

# Medir el tamaño del segmento

> Esta página explica cómo puedes supervisar la composición y el tamaño de tu segmento.

## Cálculo de la pertenencia a un segmento

Braze actualiza la pertenencia a un segmento del usuario a medida que los datos se envían a nuestros servidores y se procesan, normalmente de forma instantánea. La pertenencia a un segmento de un usuario no cambiará hasta que se haya procesado esa sesión. Por ejemplo, un usuario que cae en un segmento de usuarios caducados cuando se inicia la sesión por primera vez, será desplazado inmediatamente fuera del segmento de usuarios caducados cuando se procese la sesión.

### Cálculo del total de usuarios accesibles

Cada segmento muestra el número total de usuarios que son miembros de ese segmento. Al filtrar por **usuarios de todas las aplicaciones**, también muestra algunos de los canales de mensajería más utilizados (como notificaciones push web o correo electrónico) y el número de usuarios accesibles para esos canales específicos. 

Es posible que el número de usuarios totales sea diferente del número de usuarios alcanzables por cada canal. Además, no todos los canales aparecen en la tabla de usuarios accesibles. Por ejemplo, las tarjetas de contenido, los webhooks y WhatsApp no se muestran en el desglose. Esto significa que el número total de usuarios alcanzables podría ser mayor que la suma de los usuarios de cada canal mostrado.

![Una tabla que muestra el total de usuarios accesibles desglosados por usuarios accesibles por correo electrónico, notificaciones push de iOS, notificaciones push de Android, notificaciones push web y notificaciones push de Kindle.]({% image_buster /assets/img_archive/segmenter_reachable_users.png %})

Para que un usuario figure como localizable a través de un canal determinado, debe tener ambos:
* Una dirección de correo electrónico válida o un token de notificaciones push asociado a tu perfil, y
* Has realizado una adhesión voluntaria a tu aplicación.

Un mismo usuario puede pertenecer a diferentes grupos de usuarios accesibles. Por ejemplo, un usuario puede tener tanto una dirección de correo electrónico como un token de notificaciones push de Android válidos y estar adherido a ambos, pero no tener ningún token de notificaciones push de iOS asociado. La diferencia entre el total de usuarios alcanzables y la suma de los diferentes canales es el número de usuarios que cumplen los requisitos para formar parte del segmento, pero a los que no se puede llegar a través de esos canales de comunicación.

## Estadísticas sobre el tamaño de los segmentos

Las estadísticas estimadas son aproximadas, ya que solo se toma una muestra de una parte de tu segmento, por lo que es probable que los tamaños estimados sean mayores o menores que el valor real, y que los espacios de trabajo más grandes presenten márgenes de error potencialmente mayores. Para obtener un recuento preciso de los usuarios de tu segmento, selecciona **Calcular estadísticas exactas**. La pertenencia exacta a un segmento siempre se calculará antes de que un segmento se vea afectado por un mensaje enviado en una campaña o Canvas. 

Braze proporciona las siguientes estadísticas sobre el tamaño de los segmentos. 

### Estadísticas de filtrado

Para cada grupo de filtros, puede ver los usuarios accesibles estimados. Seleccione **Ampliar estadísticas adicionales del embudo** para ver un desglose por canales.

![Un grupo de filtros con un filtro para usuarios que tuvieron exactamente una sesión.]({% image_buster /assets/img_archive/segment_filter_stats.png %})

## Estimación de usuarios accesibles

Puedes ver el número estimado de usuarios accesibles de todo un segmento, incluido el número estimado de usuarios de cada canal, en el panel lateral **Usuarios accesibles**. Esta **estimación** muestra un rango aproximado del tamaño de tu segmento y una estimación del porcentaje de tu base de usuarios total que pertenece a este segmento. Ten en cuenta que las estadísticas estimadas se almacenan en caché durante 15 minutos, a menos que realices modificaciones en tu segmento, en cuyo caso las estadísticas estimadas se actualizarán automáticamente. También puedes ver el recuento exacto de usuarios alcanzables (tanto para el segmento en general como por canal) seleccionando **Calcular estadísticas exactas**. 


![El panel «Usuarios accesibles» indica que hay entre 2,3 y 2,4 millones de usuarios estimados.]({% image_buster /assets/img_archive/reachable_users_side_panel.png %})

### Consideraciones para los recuentos estimados

Braze mide el número estimado de usuarios mediante una consulta a una parte de tus usuarios y, a continuación, extrapola esos resultados al conjunto total de tu audiencia. Dado que el subconjunto de usuarios que Braze consulta puede variar cada vez que calculamos esta estimación, es posible que la estimación también cambie en casos en los que, técnicamente, la composición de tu audiencia debería haber permanecido igual. Por ejemplo, si reordenan tus filtros o vuelven a comprobar el mismo segmento en un momento diferente, es posible que cambie el recuento estimado (aunque **la** opción **Calcular estadísticas exactas** mostraría los mismos resultados si tu segmento no hubiera cambiado).

Si tienes una gran cantidad de usuarios en tu espacio de trabajo, es posible que observes una mayor variación entre los recuentos estimados y los recuentos exactos, especialmente en los casos en los que tu segmento representa un porcentaje muy pequeño de la población total de tu espacio de trabajo. Esto se debe a que Braze calcula la estimación mediante una consulta a un subconjunto de tus usuarios y extrapolando los resultados a toda tu base de usuarios. En el caso de bases de usuarios más grandes, es de esperar que las diferencias entre los recuentos estimados y los exactos sean mayores.

Los segmentos muy pequeños tendrán un rango estimado que incluye 0, lo que significa que el porcentaje del total de usuarios puede redondearse a 0. En estos casos, la opción **«Calcular estadísticas exactas»** te ayudará a ver un recuento preciso del tamaño de tu segmento, que puede que en realidad no sea 0.

![El panel lateral «Usuarios accesibles» muestra un recuento exacto de usuarios de «31».]({% image_buster /assets/img_archive/reachable_users_panel.png %})

### Usuarios accesibles por canal

Para ver el número de usuarios a los que se puede llegar por cada canal de mensajería, selecciona **Mostrar desglose** en el panel **Usuarios accesibles**. Esto muestra algunos de los canales de mensajería más utilizados (como notificaciones push web o correo electrónico) y el número de usuarios accesibles para esos canales específicos. 

La métrica _Total_ representa los usuarios únicos. Por ejemplo, si un usuario tiene tanto push de Android como push de iOS, se contará en ambas filas, pero solo se contará como 1 usuario en la fila _Total_.

Sin embargo, es posible que el número total de usuarios sea diferente a la suma de los usuarios accesibles por cada canal, ya que un mismo usuario puede pertenecer a diferentes grupos de usuarios accesibles. Por ejemplo, un usuario puede tener tanto una dirección de correo electrónico como un token de notificaciones push de Android válidos y estar adherido a ambos, pero no tener ningún token de notificaciones push de iOS asociado. 

Ten en cuenta que no todos los canales aparecen en la tabla **Usuarios accesibles** (como las tarjetas de contenido, los webhooks y WhatsApp). Por ejemplo, si tienes usuarios con los que solo se puede contactar a través de Whatsapp, estos aparecerán reflejados en el _Total,_ pero no en ninguna de las filas específicas de cada canal. Esto significa que el número total de usuarios alcanzables puede ser diferente de la suma de los usuarios de cada canal mostrado.

En los casos en que el _total_ es superior a la suma de los canales, la diferencia representa el número de usuarios que cumplen los requisitos para formar parte del segmento, pero a los que no se puede llegar a través de esos canales de comunicación.

Para que un usuario aparezca como accesible a través de un canal determinado, debe cumplir los siguientes requisitos:
- Una dirección de correo electrónico válida o un token de notificaciones push asociado a tu perfil, y
- Has realizado una adhesión voluntaria a tu aplicación.

#### Filtros aplicados para usuarios accesibles específicos del canal

Se aplican los siguientes filtros para cada canal a la hora de determinar los usuarios accesibles.

| Canal | Filtro |
| --- | --- |
| Correo electrónico | **El correo electrónico** está **disponible**. |
| Push | **La opción «Foreground Push Enabled»** (Habilitar primer plano) es verdadera. |
| SMS | **Un grupo de suscripción** es cualquier grupo de suscripción SMS. **El número de teléfono no es válido** es falso. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cálculo de estadísticas exactas 

Para ver un recuento preciso del número de usuarios de tu segmento, selecciona **Calcular estadísticas exactas** en el panel **Usuarios accesibles**.

Para actualizar las estadísticas de un cálculo que hayas ejecutado anteriormente, selecciona **Actualizar estadísticas exactas**. La fecha en la que se realizó este cálculo por última vez se actualizará automáticamente.

Ten en cuenta que la precisión de un cálculo es solo del 99,999 % o superior. Por lo tanto, en segmentos grandes, es posible que observes ligeras variaciones, incluso al calcular estadísticas exactas, lo cual es normal. Además, los resultados estadísticos exactos se almacenan en caché durante 24 horas, a menos que realices modificaciones en tu segmento, en cuyo caso podrás volver a calcular las estadísticas exactas.

{% alert note %}
Los segmentos divididos uniformemente por [números de contenedor aleatorios]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) no tendrán el mismo tamaño. Por ejemplo, si creas un segmento con el filtro **«Random Bucket # inferior a 5000»** y otro segmento con el filtro **«Random Bucket # superior o igual a 5000**», es posible y previsible que el tamaño de los segmentos varíe en unos pocos puntos porcentuales. Esto se debe a situaciones como la eliminación de usuarios inactivos y la imposibilidad de contactar con algunos usuarios.
{% endalert %}

![El panel «Usuarios accesibles» con una opción para mostrar el desglose.]({% image_buster /assets/img_archive/reachable_users_breakdown.png %})

Las estadísticas a nivel de filtro siempre serán estimadas, incluso si calculas estadísticas exactas. **Calcular estadísticas exactas** solo calcula las estadísticas exactas a nivel de segmento, no a nivel de filtro o grupo de filtros. Este cálculo puede tardar unos minutos en ejecutarse. Los espacios de trabajo más grandes, en particular, pueden requerir períodos más largos para completar los cálculos. Puedes realizar el seguimiento de tu progreso en la barra de progreso del panel **Usuarios accesibles**. Cuando se prevé que un cálculo tardará más de cinco minutos, Braze te enviará los resultados por correo electrónico. 

Braze da prioridad a un cálculo cada vez por espacio de trabajo, por lo que ejecutar varios cálculos a la vez provocará retrasos. Puedes seleccionar **Ver cola de cálculo** para ver qué segmentos están por delante del tuyo, su progreso y su iniciador, y hacerte una idea de cuándo se dará prioridad a tu cálculo.

![Una cola de cálculo con un cálculo.]({% image_buster /assets/img_archive/calculation_queue.png %})

Puedes cancelar un cálculo estadístico exacto seleccionando **Cancelar**. Esto puede resultar útil si hay varios cálculos en la cola y deseas dar prioridad a otro cálculo. 

![Un cálculo activo con la opción de cancelar]({% image_buster /assets/img_archive/cancel_calculation.png %}){: style="max-width:35%"}

## Ver el tamaño histórico de la membresía del segmento

Para todos los segmentos, puedes ver un gráfico histórico de membresía que muestra la membresía estimada del segmento para cada día. Este gráfico muestra cómo ha cambiado el tamaño de tu segmento a lo largo del tiempo. Utilice el menú desplegable para filtrar los miembros del segmento por intervalo de fechas.

![Utilice el desplegable Afiliación histórica para filtrar la afiliación a segmentos por intervalo de fechas.]({% image_buster /assets/img_archive/historical_membership2.png %})

Dado que el objetivo de este gráfico es ofrecerte una idea general de las tendencias de pertenencia al segmento, el recuento diario es una estimación, al igual que el tamaño del segmento es una estimación antes de seleccionar **Calcular estadísticas exactas**. Y dado que este gráfico muestra estimaciones, es posible que el tamaño de tu segmento aparezca como «0» en este gráfico, aunque su tamaño real (que se puede determinar después de seleccionar **Calcular estadísticas exactas**) no sea «0». Es especialmente probable que el gráfico muestre una estimación de «0» si tu segmento es muy pequeño en relación con el tamaño de la población de tu espacio de trabajo.

Por ejemplo, supongamos que tu espacio de trabajo contiene 100 millones de usuarios y tu segmento tiene unos 700 usuarios. Es posible que algunos días no haya usuarios en el segmento y que ningún usuario entre en el contenedor aleatorio utilizado para la estimación histórica de la pertenencia, lo que daría lugar a un recuento de pertenencia de un día igual a 0.

Braze calcula el número de miembros del segmento mediante una consulta a un subconjunto de tus usuarios y, a continuación, extrapola esos resultados a toda tu audiencia. Esto significa que los resultados del gráfico solo proporcionan una estimación de cuál podría ser la pertenencia al segmento en ese día, y se espera que también fluctúe de un día para otro, ya que cada día se puede realizar una consulta con una muestra diferente de usuarios para obtener esta estimación.

{% alert note %}
Todas las estimaciones pueden ser superiores o inferiores al valor mostrado en aproximadamente un 1 % del tamaño total de la población de tu espacio de trabajo. Los espacios de trabajo más grandes con más usuarios son más propensos a tener estimaciones que pueden diferir de los cálculos exactos en una cantidad numérica mayor, incluso si la diferencia sigue siendo del 1 % de la población de usuarios del espacio de trabajo. Esto significa que cabe esperar mayores diferencias entre las estimaciones y los recuentos exactos en los espacios de trabajo grandes.
{% endalert %}

### Razones de los cambios significativos

El número de miembros puede variar significativamente por varias razones, como las que se indican en esta tabla.

| Causa | Ejemplo |
| --- | --- |
| Comportamiento normal de los usuarios | Los usuarios se convierten en suscriptores tras una campaña especialmente exitosa. |
| Los usuarios se importan mediante CSV. | Se importó un archivo CSV de usuarios que aumentó significativamente la pertenencia al segmento. |
| Se modifican los criterios de segmentación de la audiencia. | Se modificaron las reglas de audiencia (como los filtros) de un segmento existente, lo que provocó cambios significativos en la pertenencia al segmento. |
| Se eliminan usuarios | Se ha eliminado un número significativo de usuarios. |
| Una integración del socio sincronizada con Braze. | Un tercero envió datos a Braze que influyeron significativamente en la pertenencia al segmento. |
| Los usuarios inactivos se archivan. | Se archivó un número significativo de perfiles inactivos. Por ejemplo, un gran número de usuarios importados en CSV nunca registran actividad y se archivan al mismo tiempo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
