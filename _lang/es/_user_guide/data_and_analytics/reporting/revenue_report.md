---
nav_title: Informe de ingresos
article_title: Informe de ingresos
page_type: reference
description: "Este artículo de referencia cubre la página Informe de ingresos."
tool: Reports
---

# Informe de ingresos

> La página Informe de ingresos le permite ver datos sobre los ingresos durante periodos de tiempo específicos, los ingresos de un producto concreto y los ingresos totales de su aplicación.

Para ver un informe de sus ingresos desde el panel de control, vaya a **Análisis** > **Informe de ingresos**. 

{% alert note %}
Si utiliza la [navegación antigua]({{site.baseurl}}/navigation), esta página se encuentra en **Datos**.
{% endalert %}

## Personalización del informe de ingresos

Puede personalizar su informe de ingresos seleccionando un intervalo de fechas, las aplicaciones sobre las que informar y los parámetros.

![La página "Informe de ingresos" muestra el gráfico "Rendimiento en el tiempo" con "Ingresos" como parámetro.][1]

### Filtrado por fecha y aplicaciones

Seleccione el intervalo de fechas para su informe de ingresos y, si lo desea, una aplicación específica o una selección de aplicaciones.

### Filtrado por parámetros

El gráfico **Rendimiento en el tiempo** muestra los datos de distintos parámetros, que pueden seleccionarse en el desplegable **Estadísticas para**. Puede desglosar opcionalmente los datos de determinados parámetros en el desplegable **Desglose**.

Puedes ver los siguientes datos en el **Gráfico de rendimiento en el tiempo**:
- Fórmulas de KPI
- Compras
    - (Opcional) Compras por producto
- Ingresos
    - (Optativo) Ingresos por segmento
    - (Opcional) Ingresos por producto
- Ingresos por hora
    - (Opcional) Ingresos por hora por segmento
- Ingresos por usuario

## Comprender los cálculos de ingresos

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">Ingresos del ciclo de vida</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Ingresos de toda la vida' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">Valor de duración del ciclo de vida por usuario</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Valor de duración del ciclo de vida por usuario' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">Ingresos medios diarios</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Ingresos medios diarios' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-purchases">Compras diarias</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Compras diarias' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">Ingresos diarios por usuario</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Ingresos diarios por usuario' %}</td>
        </tr>
    </tbody>
</table>

## Ver el desglose del producto

Consulte la tabla **Desglose de productos** para obtener una lista de los productos adquiridos durante el intervalo de fechas seleccionado, cuántos productos de cada tipo se adquirieron y cuántos ingresos generó cada producto.

![La tabla "Desglose de productos" muestra las columnas "Nombre del producto", "Comprado" e "Ingresos".][2]


[1]: {% image_buster /assets/img/revenue_report.png %}
[2]: {% image_buster /assets/img/revenue_report_product_breakdown.png %}
