---
nav_title: Seguimiento analítico por segmentos
article_title: Seguimiento analítico por segmentos
page_order: 8
page_type: reference
description: "Este artículo de referencia cubre el seguimiento analítico de segmentos y cómo ver los ingresos y las compras a lo largo del tiempo, las sesiones a lo largo del tiempo y los eventos personalizados a lo largo del tiempo."
tool: 
  - Segments
  - Reports
---

# Seguimiento analítico por segmentos

> Cuando el seguimiento analítico está activado para un segmento, puede ver las sesiones, los eventos personalizados y los ingresos a lo largo del tiempo para ese segmento.

Si no activas el seguimiento analítico para un segmento, podrás acceder a [las estadísticas en tiempo real][11] de ese segmento y dirigirte a sus usuarios con campañas. La única diferencia es si puede acceder a las herramientas de análisis específicas mencionadas en esta página.

## Activar el análisis por segmentos

En la sección **Detalles del segmento** de la página de un segmento, active **Seguimiento de análisis**.

![Activación del seguimiento analítico de un segmento][16]

Una aplicación puede tener activado el seguimiento de hasta 25 segmentos. Braze recomienda realizar un seguimiento de los segmentos que le resulten importantes para analizar los efectos de sus campañas sobre las sesiones, los ingresos y las compras.

## Ver los ingresos y las compras a lo largo del tiempo

Vaya a **Análisis** > **Informe de ingresos** para ver los datos sobre [ingresos y compras a lo largo del tiempo para este segmento][14].

{% alert note %}
Si utilizas la [navegación antigua]({{site.baseurl}}/navigation), puedes encontrar **Ingresos** en **Datos**.
{% endalert %}

![Datos de ingresos por segmento][17]

Para comparar visualmente los datos de los segmentos de cualquier intervalo de tiempo personalizado, añada o elimine segmentos del gráfico. Seleccione **Por segmento** en el desplegable **Desglose** y, a continuación, seleccione sus segmentos en **Valores de desglose**.

Seleccione cualquier nombre de segmento encima del gráfico para activar o desactivar la visibilidad de las métricas de ese segmento.

![Ingresos por segmentos múltiples][21]

## Sesiones a lo largo del tiempo

Del mismo modo, puede encontrar datos sobre [las sesiones a lo largo del tiempo para este segmento en particular][13] en la página **de inicio**.

{% alert note %}
Si utiliza la [navegación antigua]({{site.baseurl}}/navigation), ésta es su página de **descripción general**.
{% endalert %}

![Datos de la sesión por segmento][18]

## Ver eventos personalizados a lo largo del tiempo

Para ver los datos sobre [Eventos personalizados a lo largo del tiempo para los segmentos][20], vaya a **Análisis** > **Informe de eventos personalizados**.

## Utilización de las plantillas del Generador de consultas

Cuando el seguimiento analítico está activado, puede utilizar las plantillas de informes del Generador de consultas para desglosar las métricas de rendimiento de las campañas, Canvas, variantes y pasos por segmentos. Para saber más, consulta [Datos de segmentos]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment).

[11]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#segment-statistics
[13]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data
[14]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/
[16]: {% image_buster /assets/img_archive/A_Tracking_2.png %}
[17]: {% image_buster /assets/img_archive/Revenue.png %}
[18]: {% image_buster /assets/img_archive/events_over_time2.png %}
[20]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics
[21]: {% image_buster /assets/img_archive/segment_revenue_multiple.png %}
