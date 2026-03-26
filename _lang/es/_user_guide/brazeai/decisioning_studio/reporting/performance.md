---
nav_title: Rendimiento
article_title: Informe de rendimiento
page_order: 1
description: "Aprende a usar el informe de rendimiento para comparar grupos de tratamiento y grupos de control en BrazeAI Decisioning Studio."
---

# Informe de rendimiento

> El informe de rendimiento muestra cómo se desempeña tu agente de decisión en comparación con los grupos de control. Esta guía explica qué representa cada sección del informe, cómo se calculan las métricas y cómo interpretar los resultados.

## Cómo se construye el informe

Tu informe de rendimiento se construye por capas, completamente personalizado para tu caso de uso. Trabajando en colaboración con tu equipo:

1. Braze define qué cuenta como una acción (como un envío, clic, compra o conversión).
2. Braze define cómo medir esa acción diariamente (volumen, ingresos, personas únicas y similares).
3. Braze define la métrica de negocio que quieres ver (como tasa de conversión o ingresos por usuario).
4. Se aplican reglas de tiempo y segmentación.
5. La pestaña **Rendimiento** muestra los resultados.

Nada en el dashboard crea datos nuevos. Visualiza resultados diarios almacenados basados en esas definiciones.

## Rango de fechas y grupos de comparación

En la parte superior del dashboard, eliges:

- **Rango de fechas**: El período de tiempo para el informe.
- **Grupos de comparación**: Los grupos que se comparan (como Decisioning Studio versus Business as Usual).
- **Agregación**: La configuración de agregación del gráfico (diaria, promedio móvil de 7 días o promedio móvil de 30 días).
- **Segmentos**: Cualquier segmento aplicado. Estos se configuran de forma personalizada con tu equipo de AI Expert Services.
- **Eventos de línea de tiempo**: Si se superponen eventos de línea de tiempo configurados en el gráfico para ayudarte a entender cambios o eventos que podrían impactar el rendimiento.

![Informe de rendimiento que muestra los grupos de comparación, agregación, segmentos y filtros de eventos de línea de tiempo en la parte superior, junto con el selector de rango de fechas en la esquina superior derecha.]({% image_buster /assets/img/decisioning_studio/reporting_performance_date_range.png %})

Estas selecciones determinan qué días se incluyen, qué grupos se comparan, cómo se suaviza la línea de tendencia y qué población estás viendo.

{% alert important %}
Cambiar la configuración de agregación (como promedio móvil de 7 días) solo afecta la visualización del gráfico. No cambia los datos almacenados.
{% endalert %}

Si no puedes seleccionar una fecha reciente en el selector de fechas, es probable que esa fecha esté deshabilitada para reflejar un retraso temporal en los datos. Normalmente toma unos días obtener los datos de tu CDP en Decisioning Studio de forma confiable.

## Tarjetas de KPI

Las tarjetas de KPI en el lado izquierdo del informe muestran los indicadores clave de rendimiento configurados para tu caso de uso, como:

- LTV incremental / Cliente
- Conversiones / Cliente
- Cancelaciones de suscripción / Cliente

Cada tarjeta representa el KPI calculado a lo largo de todo el rango de fechas seleccionado. Este es un valor del período completo, no un promedio diario. Por ejemplo, si ves "LTV incremental / Cliente = 3.192", eso refleja el rendimiento a lo largo de toda la ventana seleccionada.

![Informe de rendimiento que muestra las tarjetas de resumen de KPI en el lado izquierdo, incluyendo métricas como LTV incremental / Cliente, Conversiones / Cliente y Cancelaciones de suscripción / Cliente.]({% image_buster /assets/img/decisioning_studio/reporting_performance_kpi_cards.png %})

## Gráfico de tendencia de KPI

Usa el gráfico para entender tendencias a lo largo del tiempo, cambios en el rendimiento y efectos de estacionalidad o temporalidad. Usa la tarjeta de KPI para entender el impacto general a lo largo de toda la ventana. El gráfico central muestra el mismo KPI que la tarjeta superior, pero calculado por día. Cada punto representa el valor del KPI de ese día. Si tienes seleccionado el promedio móvil de 7 días, cada punto refleja un promedio móvil, lo que suaviza la volatilidad diaria.

![Informe de rendimiento que muestra el gráfico de tendencia central titulado LTV incremental / Cliente, con líneas para Decisioning Studio y el grupo Business as Usual BAU trazadas a lo largo del tiempo.]({% image_buster /assets/img/decisioning_studio/reporting_performance_trend_chart.png %})

El gráfico y la tarjeta de KPI están diseñados para mostrar cosas diferentes. El gráfico muestra el rendimiento diario ("¿Cómo fue tu rendimiento cada día?"). La tarjeta de KPI muestra el rendimiento del período completo ("¿Cómo fue tu rendimiento a lo largo de todo el período?"). Para métricas de tasa, responden preguntas diferentes.

Considera el siguiente ejemplo con estas tasas de conversión:

- Día 1: 10 conversiones de 100 clientes = 10%
- Día 2: 2 conversiones de 10 clientes = 20%

El gráfico muestra ambos. La tarjeta de KPI recalcula combinando ambos días (12 conversiones / 110 clientes = 10.9%), no un promedio de 10% y 20%.

## Gráfico de uplift

El gráfico de uplift muestra la diferencia porcentual entre tus grupos de comparación. Se calcula como: **(Grupo primario - Grupo de comparación) / Grupo de comparación**. Esto se calcula dinámicamente basándose en los valores del gráfico de KPI.

![Informe de rendimiento que muestra el gráfico de porcentaje de uplift en el lado derecho, mostrando la diferencia porcentual entre Decisioning Studio y el grupo BAU a lo largo del tiempo.]({% image_buster /assets/img/decisioning_studio/reporting_performance_uplift.png %})

{% alert important %}
El uplift no se almacena. Se calcula a partir de los resultados de KPI. Si el uplift cambia, es porque el KPI subyacente cambió.
{% endalert %}

## Tabla agregada

La tabla en la parte inferior del informe muestra los totales brutos a lo largo del rango de fechas seleccionado, como:

- LTV incremental total
- Total de clientes
- Valor de KPI derivado

Esta sección refuerza la relación entre las diferentes vistas:

- La tarjeta de KPI es un cálculo a nivel de ventana.
- El gráfico es un cálculo diario.
- La tabla muestra los totales subyacentes que impulsan el KPI.

![Informe de rendimiento que muestra la tabla agregada en la parte inferior, con columnas para Grupo, LTV incremental, Cliente y LTV incremental / Cliente para cada grupo de comparación.]({% image_buster /assets/img/decisioning_studio/reporting_performance_aggregate_table.png %})

## Árbol de factores

El árbol de factores descompone un KPI en sus factores componentes. Por ejemplo, LTV incremental / Cliente puede descomponerse en:

- Conversiones / Cliente
- Ingresos por conversión

![Informe de rendimiento en vista de árbol de factores, mostrando un diagrama jerárquico que descompone KPIs como LTV incremental / Cliente en factores componentes como Conversiones / Cliente y Clics / Cliente.]({% image_buster /assets/img/decisioning_studio/reporting_performance_driver_tree.png %})

Los árboles de factores usan las mismas definiciones de KPI que el resto del dashboard y no introducen cálculos nuevos. Ayudan a explicar qué está impulsando el rendimiento. Si una definición de KPI cambia, los gráficos, tarjetas, uplift y árboles de factores se actualizan juntos.

## Preguntas frecuentes

### ¿Cómo funcionan los segmentos?

Los segmentos te permiten desglosar el rendimiento por grupos definidos, como niveles de interacción, características de clientes, tipo de dispositivo u otras características configuradas.

La pertenencia a un segmento se configura de forma personalizada para tu caso de uso y se calcula diariamente. Esto significa que el segmento pasado de un cliente refleja quién era ese día. Si su comportamiento cambia después, los días históricos permanecen sin cambios. Esto preserva la precisión histórica y evita que los informes cambien retroactivamente.

### ¿El informe de rendimiento difiere entre agentes Go y Pro?

Los KPIs para casos de uso Go se establecen automáticamente y están estandarizados, ya que todos los casos de uso Go tienen la misma métrica objetivo: clics únicos.

### ¿Por qué no puedo seleccionar ciertas fechas recientes?

El selector de fechas puede no permitir seleccionar los días más recientes. Esto es intencional. Los informes pueden aplicar retrasos de activación, retrasos en la disponibilidad de datos o fechas explícitamente excluidas. Estas protecciones evitan que datos incompletos o inestables aparezcan en tus resultados.

Si necesitas claridad sobre tu ventana de informes o las reglas de disponibilidad de datos, ponte en contacto con tu AI Success Manager para conocer la configuración específica de tu caso de uso.

### ¿Cuál es la diferencia entre KPIs de "volumen" y de "tasa"?

Los KPIs generalmente se dividen en dos categorías:

- **Métricas de volumen** (como conversiones totales, ingresos totales o clics totales) responden: "¿Cuánto ocurrió?"
- **Métricas de tasa** (como tasa de conversión, ingresos por usuario o tasa de click-through) responden: "¿Qué tan eficientemente ocurrió?"

El volumen y la tasa cuentan historias diferentes. Una campaña puede generar mayor volumen pero menor eficiencia, o viceversa. Al interpretar los resultados, siempre confirma qué tipo de KPI estás viendo.

### ¿Qué significa "único" (o "distinto")?

Cuando una métrica se define como "única", los individuos se deduplican usando un identificador específico (típicamente cliente). Cada persona se cuenta una vez por día.

"Único por día" es diferente de "único a lo largo de todo el rango de fechas". Si ves conteos únicos diarios sumados a lo largo de múltiples días, el mismo individuo puede aparecer más de una vez (una vez por cada día en que interactuó). Eso es intencional.

Si necesitas entender cómo se definió la unicidad en tu configuración, ponte en contacto con tu AI Success Manager.

### ¿Por qué este informe podría diferir de otro sistema?

Si tu informe de rendimiento no coincide con otro dashboard (como un ESP, herramienta de análisis o informe interno de BI), no necesariamente significa que algo esté mal. Diferentes sistemas a menudo aplican definiciones y reglas diferentes. Las razones comunes incluyen:

- **Reglas de atribución:** Algunas métricas aplican lógica de atribución, lo que significa que solo se cuenta la actividad que cumple con criterios definidos. Si otro sistema cuenta toda la actividad sin lógica de atribución, los totales pueden diferir.
- **Filtrado de interacción de máquinas y bots:** La interacción conocida generada por máquinas o bots (como escaneos de seguridad automatizados o clics no humanos) se filtra para asegurar que el rendimiento refleje el comportamiento humano real. Algunas plataformas incluyen estas interacciones en sus totales.
- **Diferentes definiciones de "único":** En este informe, la unicidad se aplica típicamente por día. Otro sistema puede calcular la unicidad a lo largo de toda la ventana de una campaña. Esas son preguntas de negocio diferentes y producen números diferentes.
- **Rango de fechas y reglas de disponibilidad de datos:** Los informes pueden aplicar retrasos de activación, retrasos en la disponibilidad de datos o fechas excluidas. Otro sistema puede incluir datos muy recientes o incompletos, creando discrepancias temporales.
- **Diferencias de volumen versus tasa:** Un sistema puede mostrar volumen total (como conversiones totales), mientras que otro muestra una tasa (como conversiones por cliente). Siempre confirma que estás comparando el mismo tipo de métrica.

### ¿Por qué el número en el gráfico no coincide con la tarjeta de resumen?

El gráfico y la tarjeta de resumen responden preguntas diferentes:

- **Gráfico:** Muestra el rendimiento diario. Cada punto refleja el KPI calculado para ese día individual.
- **Tarjeta de resumen:** Muestra el rendimiento del período completo. Recalcula el KPI a lo largo de todo el rango de fechas seleccionado.

Usa el gráfico para entender la volatilidad día a día, los efectos de temporalidad y los cambios de rendimiento a lo largo del tiempo. Usa la tarjeta de resumen para entender el impacto general a lo largo del período.

Considera este ejemplo con la siguiente tasa de conversión:

- Día 1: 10 conversiones de 100 clientes = 10%
- Día 2: 2 conversiones de 10 clientes = 20%

El gráfico muestra 10% en el Día 1 y 20% en el Día 2. La tarjeta de resumen calcula el rendimiento combinando ambos días: 12 conversiones totales de 110 clientes = 10.9%. No promedia 10% y 20%.

### ¿Cuál es el enfoque recomendado para conteos "únicos"?

Al medir comportamiento único (como clics únicos o conversores únicos), la unicidad se aplica por día. Por ejemplo:

- Día 1: Clientes que hicieron clic: A, B, C = 3 únicos
- Día 2: Clientes que hicieron clic: B, C, D = 3 únicos

El gráfico muestra 3 en el Día 1 y 3 en el Día 2. A lo largo de ambos días, puedes ver 3 + 3 = 6. Los clientes B y C se cuentan una vez por día, lo cual es intencional.

Esta configuración responde: "¿Cuántas interacciones únicas de clientes ocurrieron a lo largo de los días?" No responde: "¿Cuántos clientes individuales interactuaron al menos una vez a lo largo de todo el período?"

Si tu objetivo es la unicidad a nivel de ventana (individuos únicos a lo largo de toda la campaña o trimestre), ese es un enfoque de modelado diferente. Ponte en contacto con tu AI Success Manager para obtener orientación sobre cómo diseñarlo.