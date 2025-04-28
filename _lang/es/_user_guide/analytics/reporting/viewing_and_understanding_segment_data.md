---
nav_title: Datos de los segmentos
article_title: Visualización y comprensión de los datos de los segmentos
page_order: 2
page_type: reference
description: "Esta página explica la sección de segmentos de tu panel de Braze, e incluye un resumen de las estadísticas proporcionadas."
tool: 
  - Segments
  - Reports
  
---
# Datos de los segmentos

> Esta página explica la sección de segmentos de tu panel de Braze, e incluye un resumen de las estadísticas proporcionadas.

## Acceder a datos sobre tus segmentos y membresía

La página **Segmentos** de su cuadro de mandos Braze contiene un resumen de todos sus segmentos y le permite examinar datos detallados de cada uno de ellos. En esta página, busca y selecciona el nombre de un segmento para editar y ver sus datos. Para saber cómo crear un segmento, consulte [Creación de un segmento][3].

![Página de segmentos][1]

Tras seleccionar el nombre de un segmento, puedes ver las estadísticas y los filtros del segmento, y editarlo añadiendo o eliminando filtros. Asegúrate de guardar los cambios.

![Datos de los segmentos][2]

Cuando activas [seguimiento de análisis para un segmento][9], Braze te permite ver las sesiones, eventos personalizados e ingresos a lo largo del tiempo por este segmento.

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
            <td class="no-split">Usuarios totales</td>
            <td class="no-split">Cuántos usuarios tiene tu aplicación en total.</td>
        </tr>
        <tr>
            <td class="no-split">Usuarios seleccionados</td>
            <td class="no-split">Cuántos usuarios hay en su segmento y qué porcentaje de su base total de usuarios representan.</td>
        </tr>
        <tr>
            <td class="no-split">LTV (usuarios de pago)</td>
            <td class="no-split">El valor de vida por usuario (LTV) en este segmento y el valor de vida por usuario de pago en este segmento. El LTV se calcula dividiendo los ingresos de toda la vida entre los usuarios de toda la vida.</td>
        </tr>
        <tr>
            <td class="no-split">Envío por correo electrónico (adhesión voluntaria)</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Emailable' %} Debido a <a href="/docs/help/best_practices/spam_regulations/#spam-regulationsspam regulations">las normativas sobre correo electrónico no deseado</a>, es una buena idea pedir a tus usuarios que se adhieran voluntariamente de forma explícita, implementando una política de doble adhesión en la que los usuarios deban hacer clic en un enlace en un correo electrónico de confirmación inicial. Para animar a más usuarios a que se adhieran voluntariamente, puedes dirigir un mensaje a <a href="/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions">aquellos que ni se han adherido ni se han excluido</a>.</td>
        </tr>
        <tr>
            <td class="no-split">Push habilitado (adhesión voluntaria)</td>
            <td class="no-split">Push habilitado se refiere al número de usuarios con al menos un token push. Algunos usuarios pueden tener varios tokens push (por ejemplo, si poseen un iPhone y un iPad), por lo que el número de notificaciones push que envíe a este segmento puede ser mayor que el número de usuarios "habilitados para push". "Adheridos" se refiere al número de usuarios que han optado explícitamente por las notificaciones push. Los usuarios siempre deben aceptar explícitamente que se les envíen mensajes push.</td>
        </tr>
    </tbody>
</table>

### Información del segmento

Puede ver el rendimiento de un segmento en comparación con otro a través de un conjunto de KPI preseleccionados visitando la página [Segment Insights]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/) de su panel de control.

### Uso de la mensajería
La sección **Uso de la mensajería** muestra qué segmentos, campañas habilitadas actualmente y lienzos habilitados actualmente se dirigen a tu segmento.

![En Uso de mensajería, vea las campañas en las que se está utilizando su segmento.][4]

### Afiliación histórica
La sección **Afiliación histórica** muestra cómo ha cambiado el tamaño de tu segmento a lo largo del tiempo. Utilice el menú desplegable para filtrar los miembros del segmento por intervalo de fechas. 

El recuento histórico de miembros del segmento es una estimación, del mismo modo que el tamaño del segmento es una estimación antes de hacer clic en **Calcular estadísticas exactas**. Braze calcula el número de miembros consultando a los usuarios en un intervalo de cubos aleatorio. Esto significa que un día, el recuento de miembros podría basarse en usuarios con un número de contenedor aleatorio de 111-120, y otro día, en usuarios con un número de contenedor aleatorio de 8452-8455. Por lo tanto, el gráfico podría mostrar ligeras fluctuaciones en cada fecha debido a las diferentes cantidades de usuarios que aterrizan dentro de los rangos de cubos aleatorios.

![Utilice el desplegable Afiliación histórica para filtrar la afiliación a segmentos por intervalo de fechas.][10]

### Vista previa del usuario

Para ver información detallada y específica del usuario sobre sus segmentos, haga clic en **Datos del usuario** y seleccione **Vista previa del usuario**.

![Información específica del usuario][7]

En esta página, puede ver una serie de atributos específicos de los usuarios, como el sexo, la edad, el número de sesiones y si han optado por el push y el correo electrónico.

![Vista previa del usuario][8]

## Visualización de los datos de rendimiento por segmento

Utilice [las plantillas de informes del Generador de consultas]({{site.baseurl}}/user_guide/analytics/reporting/data_by_segments/) para desglosar las métricas de rendimiento de las campañas, Canvas, variantes y pasos por segmentos.

## Creación de un informe de desglose de segmentos mediante Query Builder

Para crear un informe a partir de una plantilla de [Generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/), vaya al **Generador de consultas** y haga lo siguiente:

1. Seleccione **Crear consulta SQL** > **Plantilla de consulta**.
2. Filtre las plantillas por aquellas que tengan métricas que incluyan "desgloses por segmentos".
3. Seleccione la plantilla que desea utilizar.
4. Rellene las variables de su plantilla SQL en la pestaña [Variables](#variables).
5. (Opcional) Edita directamente el SQL de la plantilla.
6. Seleccione **Ejecutar consulta**. Los resultados se mostrarán en una tabla.

## Variables {#variables}

Antes de generar su informe, vaya a la pestaña **Variables** para proporcionar información para la plantilla del Generador de Informes, incluyendo las variables requeridas que variarán en función del informe. 

![][11]

Las variables incluyen:

- **Campaña o lienzo:** Puede incluir una o varias campañas o lienzos (no hay un máximo para el número de campañas o lienzos que puede especificar). Si no especifica ninguna campaña o lienzo, el informe incluirá todas las campañas o lienzos del periodo de tiempo elegido.
- **Variante:** Si utiliza una plantilla que ofrece desgloses a nivel de variante, después de seleccionar una campaña o un lienzo, puede seleccionar variantes dentro de esa campaña o lienzo. Si selecciona varias variantes, los resultados se agruparán por variante.
- **Paso:** Si selecciona una variante de Canvas, puede seleccionar un paso de Canvas. No puede seleccionar un paso sin seleccionar primero una variante del lienzo. 
- **Intervalo de tiempo:** Identifique el periodo de tiempo del que desea extraer datos. Si no se especifica ningún intervalo de tiempo, éste será por defecto el de los últimos 30 días.
- **Nombre del producto:** Si ejecuta un informe de datos de compra, puede identificar un producto específico del que extraer datos.
- **Ventana de conversión:** Siempre necesario para informes con datos de ingresos y compras. El número de días tras la recepción del correo electrónico o el clic al que Braze debe atribuir las compras o los ingresos.
- **Segmentos:** Identificar los segmentos por los que desglosar los datos. Si no se especifica, el informe se ejecutará para todos los segmentos que tengan activado el seguimiento analítico.
- **Etiquetas:** Especifique etiquetas en **Variables** para ejecutar su informe para todas las campañas o Lienzos con determinadas etiquetas. Puede incluir varias etiquetas. Si añade etiquetas y campañas o lienzos específicos a un informe, éste incluirá datos de sus etiquetas y de las campañas o lienzos especificados. 

## Disponibilidad de datos

Se dispone de datos para los periodos de tiempo en los que se cumplen ambas condiciones:

1. El [seguimiento de análisis por segmentos]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) está activado para los segmentos de los que quieres ver datos.
2. La función de datos de rendimiento por segmento está activada.

No puedes acceder a datos de periodos de tiempo anteriores a la activación de esta característica para tu empresa. Por ejemplo, si el seguimiento de análisis está activado para el segmento A el 1 de octubre y esta característica está activada para tu empresa el 2 de octubre, entonces sólo podrás ver los datos del segmento A para las campañas y los lienzos que registraron métricas después del 2 de octubre. 

Si su empresa activó esta función el 2 de octubre y activó el seguimiento analítico del segmento B el 3 de octubre, sólo podrá ver los datos del segmento B de las campañas y los lienzos que registraron métricas después del 3 de octubre.


[1]: {% image_buster /assets/img_archive/segments.png %}
[2]: {% image_buster /assets/img_archive/A_Tracking.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[4]: {% image_buster /assets/img_archive/historical_membership1.png %}
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions
[6]: {{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations
[7]: {% image_buster /assets/img_archive/preview_users.png %}
[8]: {% image_buster /assets/img_archive/user_preview.png %}
[9]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking/
[10]: {% image_buster /assets/img_archive/historical_membership2.png %}
[11]:{% image_buster /assets/img_archive/variables_panel.png %}