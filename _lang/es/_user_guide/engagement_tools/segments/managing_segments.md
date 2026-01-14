---
nav_title: Administrador de segmentos
article_title: Administrador de segmentos
page_order: 1
page_type: tutorial
tool: Segments
description: "Este artículo cubre las acciones que puedes realizar para gestionar tus segmentos, como filtrar una lista de segmentos, crear segmentos y editar segmentos."

---

# Administrador de segmentos

> La sección Segmentos te permite ver una lista completa de tus segmentos existentes, crear nuevos segmentos y editar los segmentos existentes. Puedes refinar la lista de segmentos seleccionando diversos filtros y columnas, de modo que sólo se muestre la información más relevante para ti.

\![La sección Segmentos muestra una lista de los segmentos Activos.]({% image_buster /assets/img/segment/segments_page.png %})

## Personalizar tu vista

Adapta la vista de la lista de segmentos utilizando filtros y cambiando las columnas que quieres que aparezcan. Cuando salgas de la sección **Segmentos** y vuelvas, la lista volverá a la vista predeterminada, borrando cualquier filtro que hayas seleccionado previamente.

### Filtro de estado

Puedes restringir la lista para mostrar sólo los segmentos activos o archivados. Cualquier segmento no archivado se considera activo.

### Filtros

Ordena los segmentos de la lista ajustando los siguientes filtros:
- **Último editado por:** El usuario que editó por última vez los segmentos
- **Última edición:** Intervalo de tiempo en el que se editaron los segmentos por última vez
- **Tamaño estimado:** Rango aproximado de cuántos usuarios hay en los segmentos
- **Etiquetas:** Etiquetas asociadas a los segmentos
- **Equipos:** Equipos asociados a los segmentos
- **Sólo segmentos de seguimiento avanzado:** Ver sólo los segmentos que tienen habilitado el [seguimiento de análisis]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking#segment-analytics-tracking).

### Columnas

Estas son las columnas de información que puedes seleccionar para mostrar en la lista de segmentos:
- **Filtrar:** Número de filtros en el segmento
- **Última edición:** Fecha de la última edición del segmento
- **Última edición por:** El usuario que editó por última vez el segmento
- **Etiquetas:** Etiquetas asociadas al segmento
- **Equipos:** Equipos asociados al segmento
- **Tamaño estimado:** Número estimado de usuarios en el segmento
- **Lienzos:** Número de lienzos que utilizan el segmento
- **Campañas:** Número de campañas que utilizan el segmento

### Mostrar sólo estrellas

Si seleccionas **Mostrar sólo** marcados, la vista se limitará a los segmentos marcados por ti.

## Ver el uso de la mensajería de un segmento

Ve a la sección **Uso de la mensajería** de un segmento para obtener una visión general de dónde se está utilizando el segmento, como dentro de otros segmentos, campañas y Lienzos.

{% alert note %}
Para evitar bucles de segmentos que se referencian entre sí, los segmentos que utilizan el filtro **Pertenencia a segmento** no pueden ser referenciados por otros segmentos. Para más detalles, consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).
{% endalert %}

## Administrador de segmentos específicos

Menú de edición de un segmento con las opciones "Editar", "Duplicar", "Archivar" y "Añadir a destacados".]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

Para administrar un segmento concreto, pasa el ratón por encima de él y selecciona el icono de menú situado al final de la fila para que aparezcan las siguientes opciones:
- **Edita:** Edita los filtros de tu segmento.
- **Duplicar:** Haz una copia de tu segmento.
- **Archivo:** Archiva el segmento. Ten en cuenta que esto también archivará cualquier campaña o Lienzo que utilice ese segmento.
- **Añadir a estrelladas:** Marca con una estrella el segmento, lo que te permitirá acceder rápidamente a él marcando la casilla Mostrar sólo las estrellas en la sección de segmentos.
 
También puedes realizar acciones masivas -en concreto, archivado masivo y etiquetado masivo- marcando las casillas situadas junto a los nombres de varios segmentos.

Múltiples segmentos seleccionados con "CRM" seleccionado en el campo desplegable "Etiquetar como".]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### Cambios desde la última visita

El número de actualizaciones de los segmentos por parte de otros miembros de tu equipo se sigue mediante la métrica *Cambios desde la última visita* en la página de resumen de segmentos. Selecciona **Cambios desde la última vez que lo viste** para ver un registro de cambios de las actualizaciones del nombre, descripción y audiencia objetivo del segmento. Para cada actualización, puedes ver quién la realizó y cuándo. Puedes utilizar este registro de cambios para auditar los cambios en tu segmento.

## Búsqueda de segmentos
Busca nombres de segmentos introduciendo términos en el campo de búsqueda. 

Se buscarán todos los términos y cadenas introducidos en este campo. Por ejemplo, la búsqueda de "segmento de prueba 1" devolverá segmentos con "prueba", "segmento" o "1" en cualquier parte de su nombre. Para buscar una cadena exacta, escribe el término de búsqueda entre comillas. La búsqueda ["segmento de prueba 1"] devolverá todos los segmentos que contengan la frase exacta "segmento de prueba 1" en su nombre.

\![Los resultados de la búsqueda al introducir "todos los usuarios" en el campo de búsqueda incluyen "Todos los usuarios (Prueba)", "Todos los usuarios", "Todos los usuarios 15".]({% image_buster /assets/img/segment/segments_search.png %})

