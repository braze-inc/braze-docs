---
nav_title: Datos del segmento
article_title: Visualización y comprensión de los datos de los segmentos
page_order: 4
page_type: reference
description: "Esta página explica la sección de segmentos de tu panel de Braze, e incluye un resumen de las estadísticas proporcionadas."
alias: /viewing_and_understanding_segment_data/
tool: 
  - Segments
  - Reports
  
---
# Datos del segmento

> Esta página explica la sección de segmentos de tu panel de Braze, e incluye un resumen de las estadísticas proporcionadas.

## Acceder a datos sobre tus segmentos y afiliación

La página **Segmentos** de tu panel de Braze contiene un resumen de todos tus segmentos y te permite examinar datos detallados de cada uno de ellos. En esta página, busca y selecciona el nombre de un segmento para editar y ver sus datos. Para saber cómo crear un segmento, consulta [Crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment).

\![Página de segmentos]({% image_buster /assets/img_archive/segments.png %})

Tras seleccionar el nombre de un segmento, puedes ver las estadísticas y los filtros del segmento, y editarlo añadiendo o eliminando filtros. Asegúrate de guardar los cambios.

Cuando activas el [seguimiento de análisis para un segmento]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/), puedes ver las sesiones, eventos personalizados e ingresos a lo largo del tiempo para este segmento.

\![Alternar el seguimiento de análisis para un segmento]({% image_buster /assets/img_archive/A_Tracking_2.png %})

### Estadísticas de los segmentos

Puedes ver las siguientes estadísticas de segmentos, que se actualizan en tiempo real a medida que añades o eliminas filtros:

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Estadística</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Total de usuarios</td>
            <td class="no-split">Cuántos usuarios tiene tu aplicación en total.</td>
        </tr>
        <tr>
            <td class="no-split">Usuarios seleccionados</td>
            <td class="no-split">Cuántos usuarios hay en tu segmento y qué porcentaje de tu base total de usuarios representan.</td>
        </tr>
        <tr>
            <td class="no-split">LTV (Usuarios de pago)</td>
            <td class="no-split">El valor de duración por usuario (LTV) en este segmento y el valor de duración por usuario de pago en este segmento. El LTV se calcula dividiendo tus ingresos de toda la vida entre los usuarios de toda la vida.</td>
        </tr>
        <tr>
            <td class="no-split">Envío por correo electrónico (adhesión voluntaria)</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Emailable' %} Debido a <a href="/docs/help/best_practices/spam_regulations/#spam-regulationsspam regulations">la normativa sobre correo no deseado</a>, es una buena idea pedir a tus usuarios que se adhieran explícitamente mediante la implementación de una política de doble adhesión en la que los usuarios deban hacer clic en un enlace en un correo electrónico de confirmación inicial. Para animar a más usuarios a que se adhieran voluntariamente, puedes dirigir un mensaje a <a href="/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions">aquellos que ni se han adherido ni se han excluido</a>.</td>
        </tr>
        <tr>
            <td class="no-split">Push habilitado (adhesión voluntaria)</td>
            <td class="no-split">La habilitación push se refiere al número de usuarios con al menos un token de notificaciones push. Algunos usuarios pueden tener varios tokens de notificaciones push (por ejemplo, si tienen un iPhone y un iPad), por lo que el número de notificaciones push que envíes a este segmento puede ser mayor que el número de usuarios "habilitados para push". "Adheridos" se refiere al número de usuarios que han optado explícitamente por las notificaciones push. Los usuarios siempre deben expresar explícitamente su adhesión voluntaria para que les envíes push.</td>
        </tr>
    </tbody>
</table>

### Información por segmentos

Puedes ver el rendimiento de un segmento en comparación con otro a través de un conjunto de KPI preseleccionados visitando la página [Información del segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/) de tu panel.

### Uso de la mensajería
La sección **Uso de la mensajería** muestra qué segmentos, campañas habilitadas actualmente y lienzos habilitados actualmente se dirigen a tu segmento.

### Afiliación histórica

La sección **Afiliación histórica** muestra cómo ha cambiado el tamaño de tu segmento a lo largo del tiempo. Utiliza el desplegable para filtrar la pertenencia a un segmento por intervalo de fechas.

Para saber más sobre cómo controlar el número de miembros y el tamaño de tu segmento, consulta [Medir el tamaño del segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/).

### Vista previa del usuario

Para ver información detallada y específica del usuario sobre tus segmentos, haz clic en **Datos de usuario** y selecciona **Vista previa de usuario**.

En esta página, puedes ver una serie de atributos específicos de los usuarios, como el sexo, la edad, el número de sesiones y si han optado por el push y el correo electrónico.

Ten en cuenta que en los casos en los que tu segmento sea muy pequeño en relación con el tamaño de tu espacio de trabajo, es posible que la vista previa de usuario devuelva cero usuarios. Esto no significa necesariamente que haya cero usuarios en tu segmento; ejecuta [Calcular estadísticas exactas]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/#statistics-for-segment-size) para determinar el tamaño exacto de tu segmento.

\![Vista previa del usuario]({% image_buster /assets/img_archive/user_preview.png %})

## Visualización de los datos de rendimiento por segmento

Utiliza [las plantillas de informes del Generador de consultas]({{site.baseurl}}/user_guide/analytics/reporting/data_by_segments/) para desglosar las métricas de rendimiento de las campañas, Canvas, variantes y pasos por segmentos.

## Crear un informe de desglose de segmentos mediante el Generador de consultas

Para crear un informe a partir de una plantilla [del Generador]({{site.baseurl}}/user_guide/analytics/query_builder/) **de** informes, ve al **Generador de informes** y haz lo siguiente:

1. Selecciona **Crear consulta SQL** > Plantilla de consulta **.**
2. Filtra las plantillas que tengan métricas que incluyan "desgloses por segmento".
3. Selecciona la plantilla que quieras utilizar.
4. Rellena las variables de tu plantilla SQL en la pestaña [Variables](#variables).
5. (Opcional) Edita directamente el SQL en la plantilla.
6. Selecciona **Ejecutar consulta**. Tus resultados se mostrarán en una tabla.

## Variables {#variables}

Antes de generar tu informe, ve a la pestaña **Variables** para proporcionar información a la plantilla del generador de informes, incluidas las variables necesarias que variarán en función del informe. 

Las variables incluyen:

- **Campaña o Canvas:** Puedes incluir una o varias campañas o Lienzos (no hay un máximo para el número de campañas o Lienzos que puedes especificar). Si no especificas ninguna campaña o Lienzo, el informe incluirá todas las campañas o Lienzos del periodo de tiempo que hayas elegido.
- **Variante:** Si utilizas una plantilla que ofrece desgloses a nivel de variante, después de seleccionar una campaña o Canvas, puedes seleccionar variantes dentro de esa campaña o Canvas. Si seleccionas varias variantes, los resultados se agruparán por variantes.
- **Paso:** Si seleccionas una variante en Canvas, puedes seleccionar un paso en Canvas. No puedes seleccionar un paso sin seleccionar antes una variante en Canvas. 
- **Intervalo de tiempo:** Identifica el periodo de tiempo del que quieres extraer datos. Si no se especifica ningún intervalo de tiempo, éste será predeterminado a los últimos 30 días.
- **Nombre del producto:** Si ejecutas un informe de datos de compra, puedes identificar un producto específico del que extraer datos.
- **Ventana de conversión:** Siempre es necesario para los informes con datos de ingresos y compras. El número de días tras la recepción del correo electrónico o el clic al que Braze debe atribuir las compras o los ingresos.
- **Segmentos:** Identifica los segmentos por los que desglosar los datos. Si no se especifica, el informe se ejecutará para todos los segmentos que tengan activado el seguimiento de análisis.
- **Etiquetas:** Especifica etiquetas en **Variables** para ejecutar tu informe para todas las campañas o Lienzos con determinadas etiquetas. Puedes incluir varias etiquetas. Si añades tanto etiquetas como campañas o Canvases específicos a un informe, tu informe incluirá datos de tus etiquetas y de las campañas o Canvases especificados. 

## Disponibilidad de datos

Los datos están disponibles para los periodos de tiempo en los que se cumplen ambas condiciones:

1. El [seguimiento de análisis por segmentos]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) está activado para los segmentos de los que quieres ver datos.
2. Se activa la característica de datos de rendimiento por segmento.

No puedes acceder a datos de periodos de tiempo anteriores a la activación de esta característica para tu empresa. Por ejemplo, si el seguimiento de análisis está activado para el segmento A el 1 de octubre y esta característica está activada para tu empresa el 2 de octubre, entonces sólo podrás ver los datos del segmento A para las campañas y los lienzos que registraron métricas después del 2 de octubre. 

Si tu empresa activó esta característica el 2 de octubre, y activó el seguimiento de análisis para el segmento B el 3 de octubre, entonces sólo podrás ver los datos del segmento B para las campañas y los lienzos que registraron métricas después del 3 de octubre.


