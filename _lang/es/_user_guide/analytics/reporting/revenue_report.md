---
nav_title: Informe de ingresos
article_title: Informe de ingresos
page_type: reference
description: "Esta página describe cómo utilizar la página Informe de ingresos para ver datos sobre los ingresos durante periodos de tiempo específicos, los ingresos de un producto concreto y los ingresos totales de tu aplicación."
tool: Reports
---

# Informe de ingresos

> La página Informe de ingresos le permite ver datos sobre los ingresos durante periodos de tiempo específicos, los ingresos de un producto concreto y los ingresos totales de su aplicación.

Para ver un informe de sus ingresos desde el panel de control, vaya a **Análisis** > **Informe de ingresos**. 

## Personalización del informe de ingresos

Puede personalizar su informe de ingresos seleccionando un intervalo de fechas, las aplicaciones sobre las que informar y los parámetros.

![La página "Informe de ingresos" muestra el gráfico "Rendimiento en el tiempo" con "Ingresos" configurado como parámetro.]({% image_buster /assets/img/revenue_report.png %})

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
            <td class="no-split">{% multi_lang_include metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">Valor de duración del ciclo de vida por usuario</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">Ingresos medios diarios</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-purchases">Compras diarias</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">Ingresos diarios por usuario</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

## Ver el desglose del producto

Consulte la tabla **Desglose de productos** para obtener una lista de los productos adquiridos durante el intervalo de fechas seleccionado, cuántos productos de cada tipo se adquirieron y cuántos ingresos generó cada producto.

![La tabla "Desglose de productos" que muestra las columnas "Nombre del producto", "Comprado" e "Ingresos".]({% image_buster /assets/img/revenue_report_product_breakdown.png %})


