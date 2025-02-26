---
nav_title: Datos sobre ingresos de exportación e ingresos totales
article_title: Datos sobre ingresos de exportación e ingresos totales
page_order: 4
page_type: reference
description: "Este artículo de referencia explica cómo exportar datos y estadísticas de ingresos."
tool: 
  - Reports

---

# Datos sobre ingresos de exportación e ingresos totales

> Esta página cubre la página [Informe de ingresos]({{site.baseurl}}/user_guide/data_and_analytics/reporting/revenue_report/) del panel, donde puedes ver datos sobre los ingresos durante periodos de tiempo específicos, los ingresos de un producto concreto y los ingresos totales de tu aplicación.

Encontrará el **Informe de ingresos** en **Análisis**.

{% alert note %}
Si utilizas la [navegación antigua]({{site.baseurl}}/navigation), puedes encontrar **Ingresos** en **Datos**.
{% endalert %}

{% alert tip %}
¿Busca más formas de obtener datos sobre ingresos? Pruebe a añadir el comportamiento de compra (así como la compra de un producto) a las campañas o a los Canvases como [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/).
{% endalert %}

Para exportar tus datos de ingresos, selecciona <i class="fas fa-bars" title="Menú contextual del gráfico"></i> en el gráfico **Rendimiento en el tiempo** y selecciona tu opción de exportación.

## Gráfico de rendimiento a lo largo del tiempo

Los siguientes datos pueden verse en el gráfico **Rendimiento a lo largo del tiempo**:

- Fórmulas de KPI
- Compras
    - (Opcional) Compras por producto
- Ingresos
    - (Optativo) Ingresos por segmento
    - (Opcional) Ingresos por producto
- Ingresos por hora
    - (Opcional) Ingresos por hora por segmento
- Ingresos por usuario

![Gráfico de ingresos][9]

## Ingresos totales

Puede consultar las estadísticas de ingresos caso por caso en las páginas [Análisis de campaña]({{site.baseurl}}/user_guide/data_and_analytics/reporting/campaign_analytics/) o [Análisis de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/). 

{% multi_lang_include metrics.md metric='Ingresos totales' %}

{% alert tip %}
Los informes de ingresos no se pueden exportar a través de la API. Para obtener ayuda con las exportaciones CSV, consulte la sección [de resolución de problemas de exportación]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% comment %}

## Ingresos directos

Puede ver las siguientes métricas de ingresos adicionales generando un Informe de Comparación de Campañas utilizando el [Generador de Informes][1]:

- [Total de ingresos directos][2]
- [Total de compras directas][3]
- [Compras directas únicas][4]
- [Ingresos por destinatario][5]

Estas métricas se basan en la atribución al último clic, lo que significa que los ingresos se atribuirán a una campaña si esa campaña:

1. Es la última campaña en la que el usuario hizo clic antes de comprar
    <br>**Y**<br>
2. Fue clicado por el usuario menos de 3 días antes de la compra

{% endcomment %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-revenue
[3]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-purchases
[4]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#unique-direct-purchases
[5]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#revenue-per-recipient



[9]: {% image_buster /assets/img_archive/Export_revenue_graph.png %}
