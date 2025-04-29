---
nav_title: Medir el tamaño de los segmentos
article_title: Medir el tamaño de los segmentos
page_order: 9
page_type: reference
tool: 
- Segments
description: "Esta página explica cómo puedes controlar el número de miembros y el tamaño de tu segmento."
---

# Medición del tamaño del segmento

> Esta página explica cómo puedes controlar el número de miembros y el tamaño de tu segmento.

## Cálculo de la pertenencia a un segmento

Braze actualiza la pertenencia a un segmento del usuario a medida que los datos se envían a nuestros servidores y se procesan, normalmente de forma instantánea. La pertenencia a un segmento de un usuario no cambiará hasta que se haya procesado esa sesión. Por ejemplo, un usuario que cae en un segmento de usuarios caducados cuando se inicia la sesión por primera vez, será desplazado inmediatamente fuera del segmento de usuarios caducados cuando se procese la sesión.

### Cálculo del total de usuarios accesibles

Cada segmento muestra el número total de usuarios que son miembros de ese segmento. Al filtrar por **Usuarios de todas las aplicaciones**, también muestra algunos de los canales de mensajería más utilizados (como el push web o el correo electrónico) y el número de usuarios accesibles para esos canales específicos. 

Es posible que el número de usuarios totales sea diferente del número de usuarios alcanzables por cada canal. Además, no todos los canales aparecen en la tabla de usuarios accesibles. Por ejemplo, las tarjetas de contenido, los webhooks y WhatsApp no se muestran en el desglose. Esto significa que el recuento total de usuarios alcanzables podría ser mayor que la suma de los usuarios de cada canal mostrado.

![Una tabla que muestra el total de usuarios accesibles desglosado por usuarios accesibles por correo electrónico, push de iOS, push de Android, notificación push web, push de Kindle y push de Android China.][3]

Para que un usuario figure como localizable a través de un canal determinado, debe tener ambos:
* Una dirección de correo electrónico válida o un token push asociado a su perfil; y
* Optaron por adhesión voluntaria o se suscribieron a tu aplicación.

Un mismo usuario puede pertenecer a diferentes grupos de usuarios accesibles. Por ejemplo, un usuario puede tener tanto una dirección de correo electrónico como un token de notificaciones push de Android válidos y estar adherido a ambos, pero no tener ningún token de notificaciones push de iOS asociado. La diferencia entre el total de usuarios accesibles y la suma de los distintos canales es el número de usuarios que cumplen los requisitos para el segmento, pero no son accesibles a través de esos canales de comunicación.

## Estadísticas sobre el tamaño de los segmentos

Las estadísticas estimadas se aproximan mediante el muestreo de sólo una parte de tu segmento, por lo que es de esperar que los tamaños estimados sean mayores o menores que el valor real, y que los espacios de trabajo más grandes tengan márgenes de error potencialmente mayores. Para obtener un recuento exacto de los usuarios de tu segmento, selecciona **Calcular estadísticas exactas**. La pertenencia exacta a un segmento siempre se calculará antes de que un segmento se vea afectado por un mensaje enviado en una campaña o Canvas.

Braze proporciona las siguientes estadísticas sobre el tamaño de los segmentos. 

### Estadísticas de filtrado

Para cada grupo de filtros, puede ver los usuarios accesibles estimados. Seleccione **Ampliar estadísticas adicionales del embudo** para ver un desglose por canales.

![Un grupo de filtros con un filtro para un género que no es desconocido.][2]{: style="max-width:80%;"}

### Estadísticas de los segmentos

En la parte inferior de la página, puede ver la estimación de usuarios alcanzables de todo un segmento, así como el recuento estimado de usuarios de cada canal. También puede ver un recuento exacto de los usuarios accesibles (tanto para el segmento en general como por canal) seleccionando **Calcular estadísticas exactas**.

Toma nota:
- Calcular las estadísticas exactas puede llevar unos minutos. Esta función sólo calcula las estadísticas exactas a nivel de segmento, no a nivel de filtro o grupo de filtros.
- En el caso de segmentos grandes, es normal que se produzcan ligeras variaciones incluso cuando se calculan estadísticas exactas. Se espera que la precisión de esta característica sea del 99,999 % o superior.

## Visualización del tamaño histórico de los miembros del segmento

Para todos los segmentos, puedes ver un gráfico de afiliación histórica que muestra la afiliación estimada del segmento para cada día. Este gráfico muestra cómo ha cambiado el tamaño de tu segmento a lo largo del tiempo. Utilice el menú desplegable para filtrar los miembros del segmento por intervalo de fechas.

![Utilice el desplegable Afiliación histórica para filtrar la afiliación a segmentos por intervalo de fechas.][1]

Como el objetivo de este gráfico es darte una idea de las tendencias generales de pertenencia a un segmento, el recuento diario es una estimación, de forma similar a como el tamaño del segmento es una estimación antes de que selecciones **Calcular estadísticas exactas**. Y como este gráfico muestra estimaciones, es posible que el tamaño de tu segmento aparezca como "0" en este gráfico, aunque su tamaño real (que puede determinarse tras seleccionar **Calcular estadísticas exactas**) no sea "0". Es especialmente probable que el gráfico muestre una estimación de "0" si tu segmento es muy pequeño en relación con el tamaño de la población de tu espacio de trabajo.

Braze calcula el recuento de miembros del segmento consultando a un subconjunto de tus usuarios, y luego extrapolando esos resultados a toda tu audiencia. Esto significa que los resultados del gráfico sólo proporcionan una estimación de lo que podría ser la pertenencia a un segmento ese día, y es de esperar que también fluctúe de un día para otro porque cada día se puede consultar a una muestra diferente de usuarios para obtener esta estimación.

{% alert note %}
Todas las estimaciones pueden ser superiores o inferiores al valor indicado en aproximadamente un 1% del tamaño de la población total de tu espacio de trabajo. Los espacios de trabajo más grandes y con más usuarios tienen más probabilidades de tener estimaciones que pueden diferir de los cálculos exactos en una cantidad numérica mayor, aunque la diferencia siga siendo del 1% de la población de usuarios del espacio de trabajo. Esto significa que cabe esperar mayores diferencias entre las estimaciones y los recuentos exactos en los espacios de trabajo grandes.
{% endalert %}

### Motivos de los cambios significativos

El recuento de afiliados puede cambiar significativamente por diversas razones, como las que figuran en este cuadro.

| Causa | Ejemplo |
| --- | --- |
| Comportamiento normal del usuario | Los usuarios se suscriben tras una campaña especialmente exitosa. |
| Los usuarios se importan por CSV | Se importó un archivo CSV de usuarios que aumentó significativamente el número de miembros del segmento. |
| Se modifican los criterios de segmentación de la audiencia | Se modificaron las reglas de audiencia de un segmento existente (como los filtros), provocando cambios significativos en la composición del segmento. |
| Se eliminan usuarios | Se eliminó un número importante de usuarios. |
| Una integración del socio sincronizada con Braze | Un tercero envió datos a Braze que influyeron significativamente en la pertenencia a un segmento. |
| Los usuarios inactivos son archivados | Se archivó un número importante de perfiles inactivos. Por ejemplo, un gran número de usuarios importados en CSV nunca registran actividad y se archivan al mismo tiempo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

[1]: {% image_buster /assets/img_archive/historical_membership2.png %}
[2]: {% image_buster /assets/img_archive/segment_filter_stats.png %}
[3]: {% image_buster /assets/img_archive/segmenter_reachable_users.png %}