---
nav_title: Etiquetas
article_title: Etiquetas
page_order: 12
page_type: reference
description: "Este artículo de referencia trata de las etiquetas en el panel de Braze, que puedes utilizar para organizar y clasificar mejor tu interacción."

---
# Etiquetas

> Braze realiza un seguimiento de la información sobre autor, editor, fecha y estado de los segmentos, campañas y Lienzos, y te ofrece la posibilidad de crear etiquetas para organizar y clasificar mejor tu interacción.

## Etiquetas de campaña, Canvas y segmento

Puedes añadir etiquetas al crear o editar una campaña, Canvas o segmento. Haz clic en <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Etiquetas** bajo el nombre de la interacción y selecciona una etiqueta existente, o empieza a escribir para añadir una nueva etiqueta.

\![Añadir etiquetas durante la creación de la campaña.]({% image_buster /assets/img_archive/tags_add_tag.png %}){: style="max-width:60%;" }

{% alert important %}
Puedes añadir hasta 175 etiquetas a una campaña, Canvas o segmento.
{% endalert %}

### Etiquetado masivo

También puedes añadir etiquetas a varias campañas, lienzos o segmentos seleccionando varias interacciones y seleccionando <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Etiquetar como**.

Añadir etiquetas a varias campañas a la vez.]({% image_buster /assets/img_archive/tags_apply_multiple.gif %})

{% alert important %}
Cuando utilices el etiquetado masivo para aplicar una nueva etiqueta a varias campañas que ya tengan etiquetas diferentes, cada campaña seleccionada recibirá la nueva etiqueta, y cualquier etiqueta presente en una campaña se aplicará a todas las demás campañas seleccionadas, aunque esas etiquetas no estuvieran asociadas originalmente a ellas.
{% endalert %}

### Ver etiquetas

Las etiquetas configuradas en una campaña, Canvas o segmento son visibles en la página de detalles, cerca del nombre de la interacción. También aparecen en los análisis de campaña.

Etiquetas mostradas en la página de análisis de la campaña.]({% image_buster /assets/img_archive/tag_details_page.png %}){: style="max-width:60%;" }

### Filtrar por etiqueta

Las etiquetas son visibles en la lista de campañas, Lienzos o segmentos, junto con etiquetas adicionales para estados como **Archivado** y **Borrador**. Para filtrar por una etiqueta, selecciona el nombre de la etiqueta en la lista de etiquetas.

Etiquetas en la lista de campañas.]({% image_buster /assets/img_archive/tags_grid.png %})

## Etiquetas de datos personalizados

También se pueden añadir etiquetas a los datos de clientes cuando se gestionan [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) y [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#managing-custom-events). 

{% alert important %}
Esta característica está actualmente en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente si estás interesado en participar en este acceso anticipado.
{% endalert %}

## Administrador de etiquetas

Puedes utilizar las mismas etiquetas en todas las campañas, lienzos y segmentos. Para renombrar, eliminar o añadir etiquetas de forma eficaz en tu panel, ve a **Configuración** > Gestión de etiquetas **.**

\![Pestaña Etiquetas en la página Administrar configuración.]({% image_buster /assets/img_archive/tags_view.png %})

Para organizar mejor tus etiquetas, anídalas bajo una etiqueta principal. Por ejemplo, puedes mantener todas las etiquetas de vacaciones anidadas bajo una etiqueta padre `Holidays`, o todas las etiquetas relacionadas con una etapa de tu embudo de marketing bajo una etiqueta padre `Funnel`. 

Para ello, crea una nueva etiqueta, selecciona **Anidar etiqueta bajo** y elige bajo qué etiqueta existente anidar tu nueva etiqueta. También puedes anidar las etiquetas existentes desde la página de **administrador de etiquetas**. En esta página, pasa el ratón por encima de una fila con tu etiqueta y haz clic en **<i class="fas fa-pencil-alt"></i>Editar**. Después, sigue los mismos pasos que antes.

\![Crea una etiqueta anidada.]({% image_buster /assets/img_archive/tag_nested.png %}){: style="max-width:70%;" }

## Buenas prácticas {#tags-best-practices}

Las etiquetas pueden ser una herramienta de organización útil para llevar un seguimiento de las tácticas de interacción. Puedes vincular segmentos y campañas a objetivos empresariales, etapas del embudo, etc.

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
    <td>Incorporación<br>Reactivación de la interacción<br>Leal<br>PowerUser<br>Abandono<br>Perdido</td>
    <td>HighSpender<br>UsuarioActivo<br>NuevosUsuarios<br>FacebookAtribución<br>PrimeraAcción</td>
    <td>Estados Unidos<br>Noreste<br>Medio Oeste<br>Sur<br>Oeste<br>LATAM<br>AP<br>Europa Occidental<br>Oriente Medio</td>
    <td>Ventas<br>Cupones<br>Eventos</td>
    <td>MLK<br>SuperBowl<br>Día de la Pi<br>Día de San Patricio<br>MarchMadness<br>Pascua<br>Pascua judía<br>Día de la Madre<br>Día de los Caídos<br>Día del Padre<br>CuartoJulio<br>Día del Trabajo<br>Día de los Veteranos<br>ColumbusDay<br>Día del Presidente<br>Halloween<br>RoshHashanah<br>Acción de Gracias<br>Navidad<br>Hanukkah<br>NuevosAños</td>
    <td>Transacción<br>Notificación<br>ConectadoAcciónTomada</td>
  </tr>
</tbody>
</table>

## Casos de uso

¿Buscas inspiración sobre cómo aprovechar las etiquetas para gestionar el ciclo de vida de tu mensajería? He aquí algunos casos de uso habituales.

{% tabs %}
{% tab Throttling %}

### Estrangulamiento

Limita la frecuencia con la que tus clientes reciben campañas de un determinado tipo. Por ejemplo, podrías establecer los siguientes filtros para limitar la frecuencia de las campañas promocionales:

`Last received campaign` con la etiqueta `Promo` hace más de 5 días
<br>`OR`<br>
`Has not received campaign` con etiqueta `Promo`

{% endtab %}
{% tab Reporting %}

### Informar

Configura un informe de interacción para controlar el volumen de todas las campañas con una etiqueta determinada. Por ejemplo, si quieres controlar todas tus campañas push, puedes añadir una etiqueta como `Push Reporting` a esas campañas, y luego configurar un [Informe de interacción]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases) para que te envíe un informe de esas campañas etiquetadas cada día.

{% endtab %}
{% endtabs %}