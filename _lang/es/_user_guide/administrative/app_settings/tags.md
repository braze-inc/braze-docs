---
nav_title: Etiquetas
article_title: Etiquetas
page_order: 12
page_type: reference
description: "Este artículo de referencia trata sobre las etiquetas en el panel de control de Braze, que puede utilizar para organizar y clasificar mejor su compromiso."

---
# Etiquetas

> Braze realiza un seguimiento de la información sobre autor, editor, fecha y estado de los segmentos, campañas y lienzos, y te ofrece la posibilidad de crear etiquetas para organizar y clasificar mejor tu participación.

## Etiquetas de campaña, lienzo y segmento

Puede añadir etiquetas al crear o editar una campaña, un lienzo o un segmento. Haga clic en <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Etiquetas** bajo el nombre del compromiso y seleccione una etiqueta existente, o empiece a escribir para añadir una nueva etiqueta.

![Añadir etiquetas durante la creación de la campaña.]({% image_buster /assets/img_archive/tags_add_tag.png %}){: style="max-width:60%;" }

{% alert important %}
Puedes añadir hasta 175 etiquetas a una campaña, Canvas o segmento.
{% endalert %}

### Etiquetado masivo

También puedes añadir etiquetas a varias campañas, lienzos o segmentos seleccionando varias interacciones y seleccionando <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Etiquetar como**.

![Añadir etiquetas a varias campañas al mismo tiempo.]({% image_buster /assets/img_archive/tags_apply_multiple.gif %})

{% alert important %}
Cuando utilices el etiquetado masivo para aplicar una nueva etiqueta a varias campañas que ya tengan etiquetas diferentes, cada campaña seleccionada recibirá la nueva etiqueta, y cualquier etiqueta presente en una campaña se aplicará a todas las demás campañas seleccionadas, aunque esas etiquetas no estuvieran asociadas originalmente a ellas.
{% endalert %}

### Ver etiquetas

Las etiquetas configuradas en una campaña, Canvas o segmento son visibles en la página de detalles, cerca del nombre de la interacción. También aparecen en los análisis de campaña.

![Etiquetas mostradas en la página de análisis de la campaña.]({% image_buster /assets/img_archive/tag_details_page.png %}){: style="max-width:60%;" }

### Filtrar por etiqueta

Las etiquetas son visibles en la lista de campañas, Lienzos o segmentos, junto con etiquetas adicionales para estados como **Archivado** y **Borrador**. Para filtrar por una etiqueta, selecciona el nombre de la etiqueta en la lista de etiquetas.

![Etiquetas en la lista de campañas.]({% image_buster /assets/img_archive/tags_grid.png %})

## Etiquetas de datos personalizadas

También se pueden añadir etiquetas a los datos personalizados cuando se gestionan [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) y [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#managing-custom-events). 

{% alert important %}
Esta función se encuentra actualmente en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente si estás interesado en participar en este acceso anticipado.
{% endalert %}

## Administrador de etiquetas

Puede utilizar las mismas etiquetas en todas las campañas, Canvases y segmentos. Para renombrar, eliminar o añadir etiquetas de forma eficaz en tu panel de control, ve a **Configuración** > **Gestión de etiquetas**.

![Pestaña Etiquetas de la página Administrar configuración.]({% image_buster /assets/img_archive/tags_view.png %})

Para organizar mejor tus etiquetas, anídalas bajo una etiqueta padre. Por ejemplo, puede mantener todas las etiquetas de vacaciones anidadas bajo una etiqueta padre `Holidays`, o todas las etiquetas relacionadas con una etapa de su embudo de marketing bajo una etiqueta padre `Funnel`. 

Para ello, cree una nueva etiqueta, seleccione **Anidar etiqueta bajo** y elija la etiqueta existente bajo la que desea anidar la nueva etiqueta. También puede anidar las etiquetas existentes desde la página **Gestión de etiquetas**. En esta página, pase el ratón por encima de una fila con su etiqueta y haga clic en **<i class="fas fa-pencil-alt"></i>Editar**. A continuación, siga los mismos pasos que antes.

![Crea una etiqueta anidada.]({% image_buster /assets/img_archive/tag_nested.png %}){: style="max-width:70%;" }

## Buenas prácticas {#tags-best-practices}

Las etiquetas pueden ser una herramienta organizativa útil para realizar un seguimiento de las tácticas de participación. Puede vincular segmentos y campañas a objetivos empresariales, etapas del embudo, etc.

Este es un ejemplo de etiquetas que pueden ser útiles para una aplicación de comercio electrónico:

<style>
table td {
    word-break: break-word;
}
</style>


<table>
<thead>
  <tr>
    <th>Embudo</th>
    <th>Objetivos empresariales</th>
    <th>Regional</th>
    <th>Campañas</th>
    <th>Vacaciones</th>
    <th>Transacciones</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Incorporación<br>Reactivación de la interacción<br>Leal<br>PowerUser<br>Cancelación<br>Perdido</td>
    <td>HighSpender<br>ActiveUser<br>NewUsers<br>FacebookAttribution<br>FirstAction</td>
    <td>Estados Unidos<br>Noreste<br>Medio Oeste<br>Sur<br>Oeste<br>LATAM<br>AP<br>Europa Occidental<br>Oriente Medio</td>
    <td>Ventas<br>Cupones<br>Eventos</td>
    <td>MLK<br>SuperBowl<br>PiDay<br>Día de San Patricio<br>MarchMadness<br>Semana Santa<br>Pascua judía<br>Día de la madre<br>MemorialDay<br>Día del padre<br>Cuarto de julio<br>Día del Trabajo<br>Día de los Veteranos<br>ColumbusDay<br>Día del Presidente<br>Halloween<br>RoshHashanah<br>Acción de Gracias<br>Navidad<br>Hanukkah<br>Año Nuevo</td>
    <td>Transaccional<br>Notificación<br>ConnectedActionTaken</td>
  </tr>
</tbody>
</table>

## Ejemplos

¿Buscas inspiración sobre cómo aprovechar las etiquetas para gestionar el ciclo de vida de tus mensajes? He aquí algunos casos de uso habituales:

### Limitación

Limite la frecuencia con la que sus clientes reciben campañas de un determinado tipo. Por ejemplo, puede establecer los siguientes filtros para limitar la frecuencia de las campañas promocionales:

`Last received campaign` con la etiqueta `Promo` hace más de 5 días
<br>`OR`<br>
`Has not received campaign` con etiqueta `Promo`

### Informe

Configure un informe de participación para controlar el volumen de todas las campañas con una etiqueta determinada. Por ejemplo, si quieres controlar todas tus campañas push, puedes añadir una etiqueta como `Push Reporting` a esas campañas, y luego configurar un [Informe de participación]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases) para que te envíe un informe de esas campañas etiquetadas cada día.
