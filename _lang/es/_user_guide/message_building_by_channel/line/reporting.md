---
nav_title: Informe
article_title: Informes LINE
page_order: 4
description: "Este artículo de referencia cubre las métricas LINE utilizadas en Braze, así como la forma de visualizarlas en sus campañas LINE."
page_type: reference
channel:
 - LINE
alias: /line/reporting/
---

# Informes LINE

> Después de lanzar tu campaña o Canvas, puedes ver las métricas clave en la página de detalles de la campaña o en las analíticas de Canvas. Este artículo explica dónde puedes encontrar esas métricas y qué representan.

{% alert tip %}
¿Busca definiciones para los términos y métricas de su informe? Consulte el [glosario de métricas del informe]({{site.baseurl}}/user_guide/data/report_metrics/).
{% endalert %}

## Análisis de campañas

En la pestaña **Análisis de campaña**, puede ver sus informes en una serie de paneles. Puede que vea más o menos de los que se enumeran en las secciones siguientes, pero cada uno tiene su propósito.

{% alert note %}
Las estadísticas de aperturas y clics de LINE sólo se calculan si más de 20 usuarios realizan el evento en un día determinado.
{% endalert %}

### Detalles de la campaña

El panel **Detalles de la campaña** muestra una visión general de alto nivel del rendimiento de sus mensajes LINE.

Revise este panel para ver métricas generales como el número de mensajes enviados al número de destinatarios, la tasa de conversión primaria y los ingresos totales generados por este mensaje. También puedes revisar la configuración de entrega, audiencia y conversión desde esta página.

#### Grupos de control

Para medir el impacto de un mensaje LINE individual, puede añadir un [grupo de control]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) a una prueba A/B. El panel de **detalles de campaña** de nivel superior no incluye métricas de la variante Grupo de control.

### Rendimiento de LINE

El panel **LINE Performance** muestra el rendimiento de su mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si está realizando o no una prueba multivariante. Puede hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Vista previa** para ver su mensaje para cada variante o canal.

![El panel "Rendimiento de la LÍNEA" muestra las métricas de dos variantes.]({% image_buster /assets/img/line/line_performance.png %})

Si desea simplificar la vista, seleccione **\+ Añadir/Eliminar columnas** y borre las métricas que desee. Por defecto, se muestran todas las métricas.

#### Métrica LINE

Estas son algunas de las métricas clave de LINE que puede ver en sus análisis. Para ver las definiciones de todas las métricas LINE utilizadas en Braze, consulte el [glosario de métricas de informes]({{site.baseurl}}/user_guide/data/report_metrics/).

| Plazo | Definición |
| --- | --- |
| Envíos | El número total de envíos comunicados con éxito entre Braze y LINE. Esto no significa que el usuario haya recibido el mensaje. |
| Aperturas únicas | El número total de mensajes de LINE enviados que fueron abiertos por los usuarios una vez alcanzado un umbral mínimo de 20 mensajes al día. |
| Total de aperturas | El número total de veces que los mensajes de LINE enviados fueron abiertos por los usuarios una vez alcanzado un umbral mínimo de 20 mensajes al día. |
| Clics únicos | El número total de mensajes de LINE enviados en los que han hecho clic los usuarios, una vez alcanzado un umbral mínimo de 20 mensajes al día. |
| Clics totales | El número total de veces que los usuarios han hecho clic en los mensajes enviados por LINE tras alcanzar un umbral mínimo de 20 mensajes al día. |
{: .reset-td-br-1 .reset-td-br-2 }

### Rendimiento histórico

El panel de **Rendimiento histórico** permite ver las métricas del panel **Rendimiento de mensajes** en forma de gráfico a lo largo del tiempo. Utiliza los filtros de la parte superior del panel para modificar las estadísticas y los canales que aparecen en el gráfico. El intervalo de tiempo de este gráfico siempre reflejará el intervalo de tiempo especificado en la parte superior de la página.

Para obtener un desglose día a día, seleccione el menú hamburguesa <i class="fas fa-bars"></i> y seleccione **Descargar CSV** para recibir una exportación CSV del informe.

### Detalles del evento de conversión
 
El panel **Detalles del evento de conversión** le muestra el rendimiento de sus eventos de conversión para su campaña. Para más información, consulta los [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation).

### Correlación de conversión

El panel **Correlación de conversiones** le ofrece información sobre qué atributos y comportamientos de los usuarios favorecen o perjudican los resultados que establece para las campañas. Para más información, consulta los [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation).


