---
nav_title: Informar
article_title: Informes LINE
page_order: 4
description: "Este artículo de referencia cubre las métricas de LINE utilizadas en Braze, así como la forma de verlas en tus campañas de LINE."
page_type: reference
channel:
 - LINE
alias: /line/reporting/
---

# Informes LINE

> Después de lanzar tu campaña o Canvas, puedes ver las métricas clave en la página de detalles de la campaña o en los análisis de Canvas. Este artículo explica dónde puedes encontrar esas métricas y qué representan.

{% alert tip %}
¿Buscas definiciones para los términos y métricas de tu informe? Consulta el [glosario de métricas del Informe]({{site.baseurl}}/user_guide/data/report_metrics/).
{% endalert %}

## Análisis de campaña

En la pestaña **Análisis de campaña**, puedes ver tus informes en una serie de paneles. Puede que veas más o menos de los que se enumeran en las secciones siguientes, pero cada uno tiene su finalidad.

{% alert note %}
Las estadísticas de aperturas y clics de LINE sólo se calculan si más de 20 usuarios realizan el evento en un día determinado.
{% endalert %}

### Detalles de la campaña

El panel **Detalles de la campaña** muestra un resumen de alto nivel del rendimiento de tus mensajes LINE.

Revisa este panel para ver métricas generales como el número de mensajes enviados al número de destinatarios, la tasa de conversión primaria y los ingresos totales generados por este mensaje. También puedes revisar la configuración de entrega, audiencia y conversión desde esta página.

#### Grupos de control

Para medir el impacto de un mensaje individual de LINE, puedes añadir un [grupo de control]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) a una prueba A/B. El panel de **detalles de campaña** de nivel superior no incluye métricas de la variante Grupo de control.

### LÍNEA rendimiento

El panel de **rendimiento de LINE** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás realizando o no una prueba multivariante. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Vista previa** para ver tu mensaje para cada variante o canal.

El panel "Rendimiento de la línea" muestra las métricas de dos variantes.]({% image_buster /assets/img/line/line_performance.png %})

Si quieres simplificar la vista, selecciona **\+ Añadir/Eliminar columnas** y borra las métricas que desees. Por predeterminado, se muestran todas las métricas.

#### Métrica LINE

Aquí tienes algunas métricas clave de LINE que puedes ver en tus análisis. Para ver las definiciones de todas las métricas LINE utilizadas en Braze, consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics/).

| Plazo | Definición |
| --- | --- |
| Envía | El número total de envíos comunicados con éxito entre Braze y LINE. Esto no significa que el usuario haya recibido el mensaje. |
| Unique Opens | El número total de mensajes de LINE enviados que fueron abiertos por los usuarios una vez alcanzado un umbral mínimo de 20 mensajes al día. |
| Aperturas totales | El número total de veces que los mensajes de LINE enviados fueron abiertos por los usuarios una vez alcanzado un umbral mínimo de 20 mensajes al día. |
| Clics únicos | El número total de mensajes de LINE enviados en los que han hecho clic los usuarios, una vez alcanzado un umbral mínimo de 20 mensajes al día. |
| Clics totales | El número total de veces que los usuarios han hecho clic en los mensajes enviados por LINE tras alcanzar un umbral mínimo de 20 mensajes al día. |
{: .reset-td-br-1 .reset-td-br-2 }

### Rendimiento histórico

El panel **Rendimiento histórico** te permite ver las métricas del panel **Rendimiento de mensajes** como un gráfico a lo largo del tiempo. Utiliza los filtros de la parte superior del panel para modificar las estadísticas y los canales que aparecen en el gráfico. El intervalo de tiempo de este gráfico siempre reflejará el intervalo de tiempo especificado en la parte superior de la página.

Para obtener un desglose día a día, selecciona el menú hamburguesa <i class="fas fa-bars"></i> y selecciona **Descargar CSV** para recibir una exportación CSV del informe.

### Detalles del evento de conversión
 
El panel **Detalles del evento de conversión** te muestra el rendimiento de los eventos de conversión de tu campaña. Para más información, consulta [Eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation).

### Correlación de conversión

El panel **Correlación de conversiones** te da información sobre qué atributos y comportamientos de los usuarios ayudan o perjudican los resultados que estableces para las campañas. Para más información, consulta [Correlación de la conversión]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation).


