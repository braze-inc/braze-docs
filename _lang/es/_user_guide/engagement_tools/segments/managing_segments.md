---
nav_title: Administrar segmentos
article_title: Administrar segmentos
page_order: 1
page_type: tutorial
tool: Segments
description: "Este artículo cubre las acciones que puedes realizar para administrar tus segmentos, como filtrar una lista de segmentos, crear segmentos y editar segmentos."

---

# Administrar segmentos

> La sección Segmentos te permite ver una lista completa de tus segmentos existentes, crear nuevos segmentos y editar segmentos existentes. Puedes refinar la lista de segmentos seleccionando una variedad de filtros y columnas para que solo se muestre la información más relevante para ti.

![La sección Segmentos muestra una lista de segmentos activos.]({% image_buster /assets/img/segment/segments_page.png %})

## Personalizar tu vista

Adapta tu vista de la lista de segmentos utilizando filtros y cambiando las columnas que deseas que aparezcan. Cuando salgas de la sección **Segmentos** y vuelvas, la lista volverá a la vista predeterminada, borrando cualquier filtro que hayas seleccionado previamente.

### Filtro de estado

Puedes restringir la lista para mostrar solo los segmentos activos o archivados. Cualquier segmento no archivado se considera activo.

### Filtros

Ordena los segmentos de la lista ajustando los siguientes filtros:
- **Modificado por última vez por:** El usuario que editó por última vez los segmentos
- **Última edición:** Intervalo de tiempo en el que los segmentos se editaron por última vez
- **Tamaño estimado:** Rango aproximado de cuántos usuarios hay en los segmentos
- **Etiquetas:** Etiquetas asociadas a los segmentos
- **Equipos:** Equipos asociados a los segmentos
- **Solo segmentos de seguimiento avanzado:** Ver solo los segmentos que tienen habilitado el [seguimiento de análisis]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking#segment-analytics-tracking).

### Columnas

Estas son las columnas de información que puedes seleccionar para mostrar en la lista de segmentos:
- **Filtros:** Número de filtros en el segmento
- **Última edición:** Fecha de la última edición del segmento
- **Modificado por última vez por:** El usuario que editó el segmento por última vez
- **Etiquetas:** Etiquetas asociadas al segmento
- **Equipos:** Equipos asociados al segmento
- **Tamaño estimado:** Número estimado de usuarios en el segmento
- **Canvas:** Número de Canvas que utilizan el segmento
- **Campañas:** Número de campañas que utilizan el segmento

### Mostrar solo destacados

Seleccionar **Mostrar solo destacados** limita tu vista a los segmentos que hayas marcado con estrella.

## Ver el uso de mensajería de un segmento {#messaging-use}

Ve a la sección **Uso de mensajería** de un segmento para obtener un resumen de dónde se está utilizando el segmento, como dentro de otros segmentos, campañas y Canvas.

{% alert note %}
Para evitar bucles de segmentos que se referencian entre sí, los segmentos que utilizan el filtro **Pertenencia a segmento** no pueden ser referenciados por otros segmentos. Para más detalles, consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).
{% endalert %}

## Administrar segmentos específicos

![El menú de edición de un segmento muestra las opciones "Editar", "Duplicar", "Archivar" y "Añadir a destacados".]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

Para administrar un segmento específico, pasa el cursor sobre él y selecciona el icono de menú al final de la fila para ver las siguientes opciones:
- **Editar:** Edita los filtros de tu segmento.
- **Duplicar:** Haz una copia de tu segmento.
- **Archivar:** Archiva el segmento. Ten en cuenta que esto también archivará cualquier campaña o Canvas que utilice ese segmento.
- **Añadir a destacados:** Marca el segmento con estrella, lo que te permite acceder rápidamente a él marcando la casilla Mostrar solo destacados en la sección de segmentos.
 
También puedes realizar acciones masivas —específicamente, archivar y etiquetar en bloque— marcando las casillas junto a los nombres de varios segmentos.

![Múltiples segmentos seleccionados con "CRM" seleccionado en el campo desplegable "Etiquetar como".]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### Cambios desde la última visualización

El número de actualizaciones de los segmentos por parte de otros miembros de tu equipo se registra mediante la métrica *Cambios desde la última visualización* en la página de resumen de segmentos. Selecciona **Cambios desde la última visualización** para ver un registro de cambios de las actualizaciones del nombre, descripción y audiencia objetivo del segmento. Para cada actualización, puedes ver quién la realizó y cuándo. Puedes utilizar este registro de cambios para auditar los cambios en tu segmento.

## Buscar segmentos

Busca nombres de segmentos introduciendo términos en el campo de búsqueda. 

Se buscarán todos los términos y cadenas introducidos en este campo. Por ejemplo, buscar "segmento de prueba 1" devolverá segmentos con "prueba", "segmento" o "1" en cualquier parte de su nombre. Para buscar una cadena exacta, escribe el término de búsqueda entre comillas. Buscar ["segmento de prueba 1"] devolverá todos los segmentos que contengan la frase exacta "segmento de prueba 1" en su nombre.

![Los resultados de la búsqueda al introducir "all users" en el campo de búsqueda incluyen "All Users (Test)", "All Users", "All Users 15".]({% image_buster /assets/img/segment/segments_search.png %})

### Segmentos en Canvas

Para buscar todas las referencias de segmentos, incluidas las que están en otros segmentos, campañas o Canvas, ve a la sección [Uso de mensajería](#messaging-use) de un segmento. El filtro **Segmento objetivo** en la página de **Canvas** busca solo segmentos de audiencia de Canvas. 

![Filtro de segmento objetivo en la página de Canvas.]({% image_buster /assets/img/segment/target_segment.png %}){: style="max-width:45%;"}