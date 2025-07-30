---
nav_title: Administrador de segmentos
article_title: Administrador de segmentos
page_order: 1
page_type: tutorial
tool: Segments
description: "Este artículo cubre las acciones que puede realizar para gestionar sus segmentos, como filtrar una lista de segmentos, crear segmentos y editar segmentos."

---

# Administrador de segmentos

> La sección Segmentos le permite ver una lista completa de sus segmentos existentes, crear nuevos segmentos y editar segmentos existentes. Puede refinar la lista de segmentos seleccionando una variedad de filtros y columnas para que sólo se muestre la información más relevante para usted.

![La sección Segmentos muestra una lista de los segmentos Activos.]({% image_buster /assets/img/segment/segments_page.png %})

## Personalizar la vista

Adapte su vista de la lista de segmentos utilizando filtros y cambiando las columnas que desea que aparezcan. Cuando salga de la sección **Segmentos** y vuelva, la lista volverá a la vista por defecto, borrando cualquier filtro que hubiera seleccionado previamente.

### Filtro de estado

Puede restringir la lista para mostrar sólo los segmentos activos o archivados. Cualquier segmento no archivado se considera activo.

### Filtros

Ordene los segmentos de la lista ajustando los siguientes filtros:
- **Modificado por última vez por:** El usuario que editó por última vez los segmentos
- **Última edición:** Intervalo de tiempo en el que los segmentos se editaron por última vez
- **Tamaño estimado:** Rango aproximado de cuántos usuarios hay en los segmentos
- **Etiquetas:** Etiquetas asociadas a los segmentos
- **Equipos:** Equipos asociados a los segmentos
- **Solo segmentos de seguimiento avanzado:** Ver sólo los segmentos que tienen activado el [Seguimiento Analítico]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking#segment-analytics-tracking).

### Columnas

Estas son las columnas de información que puede seleccionar para mostrar en la lista de segmentos:
- **Filtros:** Número de filtros en el segmento
- **Última edición:** Fecha de la última edición del segmento
- **Modificado por última vez por:** El usuario que editó el segmento por última vez
- **Etiquetas:** Etiquetas asociadas al segmento
- **Equipos:** Equipos asociados al segmento
- **Tamaño estimado:** Número estimado de usuarios en el segmento
- **Canvas:** Número de lonas que utilizan el segmento
- **Campañas:** Número de campañas que utilizan el segmento

### Mostrar solo marcados con estrellas

Si selecciona **Mostrar sólo marcados**, la vista se limitará a los segmentos marcados por usted.

## Gestión de segmentos específicos

![El menú de edición de un segmento muestra las opciones "Editar", "Duplicar", "Archivar" y "Añadir a destacados".]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

Para gestionar un segmento concreto, pase el ratón por encima de él y seleccione el icono de menú situado al final de la fila para ver las siguientes opciones:
- **Editar:** Edita los filtros de tu segmento.
- **Duplicar:** Haz una copia de tu segmento.
- **Archivar:** Archiva el segmento. Tenga en cuenta que esto también archivará cualquier campaña o lienzo que utilice ese segmento.
- **Añadir a marcados con estrella:** Ponga una estrella en el segmento, lo que le permitirá acceder rápidamente a él marcando la casilla Mostrar sólo las estrellas en la sección de segmentos.
 
También puede realizar acciones en bloque -en concreto, archivar y etiquetar en bloque- marcando las casillas situadas junto a los nombres de varios segmentos.

![Múltiples segmentos seleccionados con "CRM" seleccionado en el campo desplegable "Etiquetar como".]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### cambios desde la última visualización

El número de actualizaciones de los segmentos por parte de otros miembros de tu equipo se sigue mediante la métrica *Cambios desde la última visita* en la página de resumen de segmentos. Selecciona **Cambios desde la última vez que lo viste** para ver un registro de cambios de las actualizaciones del nombre, descripción y audiencia objetivo del segmento. Para cada actualización, puedes ver quién la realizó y cuándo. Puedes utilizar este registro de cambios para auditar los cambios en tu segmento.

## Búsqueda de segmentos
Busque nombres de segmentos introduciendo términos en el campo de búsqueda. 

Se buscarán todos los términos y cadenas introducidos en este campo. Por ejemplo, la búsqueda de "segmento de prueba 1" devolverá segmentos con "prueba", "segmento" o "1" en cualquier parte de su nombre. Para buscar una cadena exacta, escriba el término de búsqueda entre comillas. La búsqueda ["segmento de prueba 1"] devolverá todos los segmentos que contengan la frase exacta "segmento de prueba 1" en su nombre.

![Los resultados de la búsqueda al introducir "todos los usuarios" en el campo de búsqueda incluyen "Todos los usuarios (Prueba)", "Todos los usuarios", "Todos los usuarios 15".]({% image_buster /assets/img/segment/segments_search.png %})

