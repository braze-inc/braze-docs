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

![Añadir etiquetas durante la creación de la campaña][2]

También puede añadir etiquetas a varias campañas, lienzos o segmentos seleccionando varias interacciones y haciendo clic en <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Etiquetar como**.

![Añadir etiquetas a varias campañas al mismo tiempo][5]

Las etiquetas establecidas en una campaña, lienzo o segmento son visibles en la página de detalles, cerca del nombre del compromiso.

![Etiquetas mostradas en la página de detalles de la campaña][3]

También son visibles en la lista de campañas, Lienzos o segmentos, junto con etiquetas de estado adicionales como **Archivado** y **Borrador**.

![Etiquetas de la lista de campañas][4]{: style ="max-width:70%;" }

Para filtrar por una etiqueta, seleccione el nombre de la etiqueta en la lista de etiquetas o búsquela en el panel de búsqueda mediante el selector `tag:`. Por ejemplo, para buscar la etiqueta `Onboarding`, introduce "tag:Onboarding".

![Buscar todas las campañas etiquetadas como Correo de bienvenida][6]

{% alert important %}
Puedes añadir hasta 175 etiquetas a una campaña, Canvas o segmento.
{% endalert %}

## Etiquetas de datos personalizadas

También se pueden añadir etiquetas a los datos personalizados cuando se gestionan [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) y [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#managing-custom-events). 

{% alert important %}
Esta función se encuentra actualmente en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente si estás interesado en participar en este acceso anticipado.
{% endalert %}

## Buenas prácticas {#tags-best-practices}

Las etiquetas pueden ser una herramienta organizativa útil para realizar un seguimiento de las tácticas de participación. Puede vincular segmentos y campañas a objetivos empresariales, etapas del embudo, etc.

A continuación se ofrece un ejemplo de etiquetas que una aplicación de comercio electrónico podría considerar útiles:

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

Puede utilizar las mismas etiquetas en todas las campañas, Canvases y segmentos. Para renombrar, eliminar o añadir etiquetas de forma eficaz en tu panel de control, ve a **Configuración** > **Gestión de etiquetas**.

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), esta página se encuentra en **Configuración** > **Administrar configuración** > **Etiquetas**.
{% endalert %}

![Pestaña Etiquetas de la página Administrar configuración][8]

Para organizar mejor tus etiquetas, anídalas bajo una etiqueta padre. Por ejemplo, puede mantener todas las etiquetas de vacaciones anidadas bajo una etiqueta padre `Holidays`, o todas las etiquetas relacionadas con una etapa de su embudo de marketing bajo una etiqueta padre `Funnel`. 

Para ello, cree una nueva etiqueta, seleccione **Anidar etiqueta bajo** y elija la etiqueta existente bajo la que desea anidar la nueva etiqueta. También puede anidar las etiquetas existentes desde la página **Gestión de etiquetas**. En esta página, pase el ratón por encima de una fila con su etiqueta y haga clic en **<i class="fas fa-pencil-alt"></i>Editar**. A continuación, siga los mismos pasos que antes.

![Crear una etiqueta anidada][1]{: style ="max-width:70%;" }

## Ejemplos

¿Buscas inspiración sobre cómo aprovechar las etiquetas para gestionar el ciclo de vida de tus mensajes? He aquí algunos casos de uso habituales:

### Limitación

Limite la frecuencia con la que sus clientes reciben campañas de un determinado tipo. Por ejemplo, puede establecer los siguientes filtros para limitar la frecuencia de las campañas promocionales:

`Last received campaign` con la etiqueta `Promo` hace más de 5 días
<br>`OR`<br>
`Has not received campaign` con etiqueta `Promo`

### Informe

Configure un informe de participación para controlar el volumen de todas las campañas con una etiqueta determinada. Por ejemplo, si quieres controlar todas tus campañas push, puedes añadir una etiqueta como `Push Reporting` a esas campañas, y luego configurar un [Informe de participación]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases) para que te envíe un informe de esas campañas etiquetadas cada día.



[1]: {% image_buster /assets/img_archive/tag_nested.png %}
[2]: {% image_buster /assets/img_archive/tags_add_tag.png %}
[3]: {% image_buster /assets/img_archive/tag_details_page.png %}
[4]: {% image_buster /assets/img_archive/tags_grid.png %}
[5]: {% image_buster /assets/img_archive/tags_apply_multiple.png %}
[6]: {% image_buster /assets/img_archive/tags_filtering.png %}
[7]: {% image_buster /assets/img_archive/Tags-Potential_Tags.png %}
[8]: {% image_buster /assets/img_archive/tags_view.png %}
