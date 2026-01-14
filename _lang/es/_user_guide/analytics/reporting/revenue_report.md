---
nav_title: Informe de ingresos
article_title: Informe de ingresos
page_type: reference
description: "Esta página describe cómo utilizar la página Informe de ingresos para ver datos sobre los ingresos durante periodos de tiempo específicos, los ingresos de un producto concreto y los ingresos totales de tu aplicación."
tool: Reports
---

# Informe de ingresos

> La página Informe de ingresos te permite ver datos sobre los ingresos durante periodos de tiempo concretos, los ingresos de un producto específico y los ingresos totales de tu aplicación.

Para ver un informe de tus ingresos desde el panel, ve a **Análisis** > **Informe de ingresos**. 

## Personaliza tu informe de ingresos

Puedes personalizar tu informe de ingresos seleccionando un intervalo de fechas, las aplicaciones sobre las que informar y los parámetros.

La página "Informe de ingresos" muestra el gráfico "Rendimiento en el tiempo" con "Ingresos" como parámetro.]({% image_buster /assets/img/revenue_report.png %})

### Filtrar por fecha y aplicaciones

Selecciona el intervalo de fechas para tu informe de ingresos y, si quieres, una aplicación específica o una selección de aplicaciones.

### Filtrar por parámetros

El gráfico **Rendimiento en el tiempo** muestra los datos de distintos parámetros, que puedes seleccionar en el desplegable **Estadísticas para**. Puedes desglosar opcionalmente los datos de determinados parámetros en el desplegable **Desglose**.

Puedes ver los siguientes datos en el **Gráfico de rendimiento en el tiempo**:
- Fórmulas KPI
- Compras
    - (Opcional) Compras por producto
- Ingresos
    - (Opcional) Ingresos por segmento
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
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">Ingresos de toda la vida</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">Valor de duración del ciclo de vida por usuario</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">Ingresos medios diarios</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-purchases">Compras diarias</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">Ingresos diarios por usuario</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

## Ver el desglose del producto

Consulta la tabla **Desglose de productos** para ver una lista de los productos comprados durante el intervalo de fechas seleccionado, cuántos se compraron de cada producto y cuántos ingresos generó cada producto.

La tabla "Desglose de productos" muestra las columnas "Nombre del producto", "Comprado" e "Ingresos".]({% image_buster /assets/img/revenue_report_product_breakdown.png %})


