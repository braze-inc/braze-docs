---
nav_title: Ver informes
article_title: Visualización de los informes del estudio de toma de decisiones
page_order: 3
description: "Aprende a ver los informes de BrazeAI Decisioning Studio™ en Braze, para que puedas entender cómo afectan a tus campañas las decisiones basadas en IA."
---

# Visualización de los informes del estudio de decisión

> Aprende a ver los informes de BrazeAI Decisioning Studio™ en Braze, para que puedas entender cómo afectan a tus campañas las decisiones basadas en IA. Desde las métricas de rendimiento hasta el estado de los datos y los cambios del sistema, estos informes te ayudan a comprender los resultados, solucionar problemas y tomar decisiones informadas con confianza.

## Requisitos previos

Antes de poder ver los informes del estudio de decisión en el Braze, tendrás que

- Tener un contrato activo para Braze y BrazeAI Decisioning Studio™. 
- Ponte en contacto con tu CSM para que te habilite BrazeAI Decisioning Studio™ en tu nombre.
- Disponer de un agente BrazeAI Decisioning Studio™ en vivo.

## Ver informes {#view}

Para ver las métricas de los agentes de un estudio de decisión en Braze, ve a **AI Decisioning** > **BrazeAI Decisioning Studio™**, y luego selecciona un agente.

La pantalla de inicio de informes de BrazeAI Decisioning Studio™ muestra un panel con varias tarjetas de informe. Cada tarjeta muestra un tipo de informe, como Rendimiento, Información, Diagnóstico y Cronología, con breves descripciones e iconos para cada uno.]( {% image_buster /assets/img/decisioning_studio/reporting_home.png %} )

Aquí puedes ver informes como los de rendimiento, información, diagnósticos y plazos. Para más detalles, consulta [Informes disponibles](#reports).

## Cambiar las fechas de los informes

Tras [abrir un informe](#view), puedes cambiar el intervalo de fechas seleccionando una nueva fecha de inicio y fin en el desplegable del calendario.

\![BrazeAI Decisioning Studio™ selector de intervalos de fechas abierto con un calendario desplegable. El calendario muestra fechas de inicio y fin seleccionables para personalizar la vista del informe.]({% image_buster /assets/img/decisioning_studio/reporting_change_date_range.png %}){: style="max-width:50%;"}

También puedes establecer una fecha de inicio predeterminada o elegir fechas para excluir siempre. Las fechas excluidas se filtrarán de todos los informes de ese agente.

Para establecer o excluir fechas, selecciona <i class="fa-solid fa-gear"></i> **Configuración** y, a continuación, cambia la fecha predeterminada o excluye las fechas que necesites.

\![Panel de configuración abierto en BrazeAI Decisioning Studio™ que muestra opciones para establecer una fecha de inicio predeterminada y excluir fechas concretas de los informes. El panel muestra dos secciones denominadas Fecha de inicio predeterminada y Fechas excluidas. En Excluir fechas, aparecen varias fechas con casillas de verificación junto a cada una.]({% image_buster /assets/img/decisioning_studio/reporting_set_exclude_dates.png %})

## Informes disponibles {#reports}

### Rendimiento

El informe de rendimiento ofrece métricas de agente de alto nivel que comparan los grupos de tratamiento (de Braze) con uno o más grupos de control, (como los ingresos). Admite dos puntos de vista diferentes: **Árbol de****tendencias** y conductores.

Por defecto, el informe utiliza la vista **Tendencias**, que compara el rendimiento de BrazeAI™ a lo largo del tiempo con el de tus grupos de control, y hace un seguimiento de la evolución del aumento.

\![Vista de tendencias del informe de rendimiento que muestra un gráfico de líneas que compara el rendimiento de BrazeAI™ y del grupo de control a lo largo del tiempo. El gráfico muestra dos líneas denominadas BrazeAI™ y Control, con el eje y denominado Elevación y el eje x mostrando las fechas. Una leyenda identifica cada grupo por colores.]({% image_buster /assets/img/decisioning_studio/reporting_agent_performance_trending.png %})

También puedes seleccionar **Árbol de controladores** para ver cómo se vinculan los controladores de valor clave con las métricas objetivo, lo que te ayudará a comprender mejor la relación entre ellos.

\![Vista en árbol de los controladores del informe de rendimiento que muestra un diagrama jerárquico que mapea los controladores de valor clave con las métricas objetivo. El diagrama muestra varios nodos conectados, cada uno de ellos etiquetado con un nombre de controlador o métrica, que ilustra cómo los distintos factores contribuyen al rendimiento global.]({% image_buster /assets/img/decisioning_studio/reporting_performance_drivertree.png %})

Para comparar el rendimiento entre dos grupos, utiliza los desplegables para seleccionar los criterios de comparación que desees. Consulta la tabla siguiente para más detalles:

| Campo | Descripción |
|-------|-------------|
| Grupos de comparación | Los grupos que quieres comparar en tu informe. |
| Agregación | La forma en que el informe agrupa los datos, como totales, medias o porcentajes. |
| Segmentos | Los [segmentos de audiencia]({{site.baseurl}}/user_guide/engagement_tools/segments/) que creaste en Braze. |
| Calendario de acontecimientos | Los eventos específicos mostrados a lo largo del tiempo, como envíos de mensajes, aperturas o conversiones. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Información

Las informaciones te muestran cómo se generan las distintas opciones de recomendación de tu banco de acciones, como la selección de SL o de bloque. Hay dos informes de información diferentes: **Preferencias de los agentes** y **SHAPs**.

{% tabs local %}
{% tab agent preferences %}
El informe de **preferencias del Agente** te ayuda a identificar las tendencias estacionales y a evaluar la relevancia de las opciones del banco de acciones, orientando las decisiones de actualización con conocimiento de causa.

\![Informe de preferencias del agente que muestra un gráfico de barras en el que se compara la frecuencia con la que se seleccionaron distintas opciones de recomendación durante un periodo de tiempo determinado. El gráfico muestra varias barras de colores, cada una de las cuales representa una opción de recomendación del banco de acciones, con el eje y etiquetado como porcentaje de veces elegidas y el eje x enumerando los nombres de las opciones.]({% image_buster /assets/img/decisioning_studio/reporting_insights_agent_preferences.png %})

Consulta la tabla siguiente para obtener más detalles sobre este informe:

| Campo | Descripción |
|-------|-------------|
| Dimensión | Atributo utilizado para organizar los resultados, como canal, campaña o plataforma. |
| Grupo de comparación | Los grupos que quieres comparar en tu informe. Puedes seleccionar varios grupos de comparación, hasta NUM. |
| Parámetro | La métrica aplicada a ese atributo, como aperturas, clics o tasa de conversión. |
| Segmento | El [segmento de audiencia]({{site.baseurl}}/user_guide/engagement_tools/segments/) que creaste en Braze. |
| Opción             | La opción de recomendación específica seleccionada del banco de acciones. |
| Descripción        | Una breve explicación de lo que representa la opción.            |
| \# nº de veces elegido  | El recuento total de las veces que se seleccionó la opción.         |
| % de tiempo elegido   | El porcentaje de selecciones totales en las que se eligió esta opción. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab shaps %}
El informe **SHAPs** utiliza el modelo SHapley Additive exPlanations (SHAP) para ayudarte a cuantificar cómo contribuye cada característica o variable a tu modelo de recomendación. Cada punto del gráfico representa un SHAP y la distribución de los puntos representa un sentido general del impacto direccional de una característica.

\![Gráfico del informe SHAPs que muestra un gráfico de barras horizontales con múltiples barras de colores que representan distintas características o variables. Cada barra muestra el impacto de una característica en el modelo de recomendación, con el eje x etiquetado como valor SHAP y el eje y enumerando nombres de características como Recencia, Frecuencia y Canal. El gráfico visualiza cómo cada característica contribuye positiva o negativamente a las predicciones del modelo.]({% image_buster /assets/img/decisioning_studio/reporting_insights_shaps.png %})

{% endtab %}
{% endtabs %}

### Diagnóstico

El informe de diagnóstico contiene dos tipos de informe diferentes: **Salientes** y **Entrantes**.

{% tabs local %}
{% tab outbound %}
El informe de diagnóstico saliente muestra el volumen diario de recomendaciones generadas y activadas en tus audiencias. Utilízalo para detectar problemas de entrega, hacer un seguimiento de los picos o caídas de las activaciones, y confirmar que los mensajes llegan a los grupos adecuados según lo esperado.

\![Informe de diagnóstico saliente que muestra un gráfico de líneas con el seguimiento del volumen diario de recomendaciones generadas y activadas para distintos grupos de audiencia. El gráfico muestra dos líneas denominadas Generado y Activado, en las que el eje y representa el número de recomendaciones y el eje x muestra las fechas. Una leyenda identifica cada línea por colores. La interfaz incluye filtros desplegables para el intervalo de fechas y la selección de audiencia encima del gráfico.]({% image_buster /assets/img/decisioning_studio/reporting_diagnostics_outbound.png %})

{% endtab %}

{% tab inbound %}

El informe de diagnóstico de entrada supervisa la salud de tus fuentes de datos en BrazeAI™. Realiza un seguimiento de detalles como el recuento de archivos, tamaños y volúmenes de filas de cada activo, ayudándote a confirmar que los datos fluyen según lo esperado y a solucionar problemas antes de que afecten a tus modelos o campañas.

Puedes utilizar el menú desplegable para seleccionar diferentes métricas del gráfico, como el tamaño medio de los archivos o el recuento de archivos.

\![Informe de diagnóstico de entrada que muestra un gráfico de líneas con el seguimiento del recuento diario de archivos y el tamaño medio de los archivos de los activos de datos entregados a BrazeAI™. El gráfico muestra dos líneas denominadas Recuento de archivos y Tamaño medio de archivo MBs, con el eje y representando valores y el eje x mostrando fechas. Encima del gráfico hay filtros desplegables para el intervalo de fechas y la selección de activos de datos.]( {% image_buster /assets/img/decisioning_studio/reporting_diagnostics_inbound.png %} )

Consulta la tabla siguiente para obtener más detalles sobre cada métrica del informe de entrada:

| Campo | Descripción |
|-------|-------------|
| Activo de datos | El nombre del conjunto de datos o archivo entregado. |
| Fecha | La fecha en que se recibieron los datos. |
| Última hora de entrega | La hora más reciente en que se entregaron los datos. |
| Recuento de archivos | El número total de archivos recibidos. |
| Tamaño máximo del archivo (MBs) | El tamaño del archivo más grande recibido, en megabytes. |
| Tamaño medio del archivo (MBs) | El tamaño medio de todos los archivos recibidos, en megabytes. |
| Recuento de filas del archivo | El número total de filas que contienen los archivos entregados. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}

### Cronología

El informe cronológico proporciona un registro visual de los acontecimientos clave junto con tus métricas de rendimiento. Estos eventos incluyen ejecuciones de modelos, cambios de configuración, actualizaciones de barandillas, etc. Las anotaciones aparecen directamente en los gráficos ascendentes y en una pestaña dedicada a la línea de tiempo, lo que te proporciona un contexto instantáneo de los cambios en los resultados sin necesidad de hacer un seguimiento de los cambios históricos.

\![Informe cronológico que muestra un gráfico con las métricas de rendimiento a lo largo del tiempo. Los eventos clave, como las ejecuciones del modelo, los cambios de configuración y las actualizaciones de las barandillas, se marcan como iconos a lo largo de la línea de tiempo. Debajo del gráfico, una tabla enumera los eventos con columnas para la fecha, el tipo, la etiqueta, los detalles y la visibilidad en los gráficos.]({% image_buster /assets/img/decisioning_studio/reporting_timeline.png %})

Para comparar el rendimiento entre dos grupos, utiliza los desplegables para seleccionar los criterios de comparación que desees. Consulta la tabla siguiente para más detalles:

| Campo | Descripción |
|-------|-------------|
| Fecha | La fecha en que ocurrió el suceso. |
| Tipo | La categoría del evento, como actualización del sistema, ejecución del modelo o cambio de configuración. |
| Etiqueta | El nombre o identificador dado al evento. |
| Detalles | Información adicional que describe el acontecimiento. |
| Visible en Gráficos | Indica si el evento se muestra en los gráficos relacionados. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
