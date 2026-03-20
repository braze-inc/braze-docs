---
nav_title: Información
article_title: Informe de información
page_order: 2
description: "Aprende a usar el informe de información para entender cómo se generan las opciones de recomendación en tu banco de acciones en BrazeAI Decisioning Studio."
---

# Informe de información

> La sección de información te muestra cómo se generan las distintas opciones de recomendación en tu banco de acciones, como la selección de bloques. Hay dos informes de información diferentes: **Preferencias del agente** y **SHAPs**.

{% tabs local %}
{% tab agent preferences %}
El informe de **Preferencias del agente** te ayuda a identificar tendencias estacionales y evaluar la relevancia de las opciones en el banco de acciones, orientando decisiones informadas para actualizaciones.

![Informe de preferencias del agente que muestra un gráfico de barras comparando la frecuencia con la que se seleccionaron diferentes opciones de recomendación durante un período de tiempo específico. El gráfico muestra varias barras de colores, cada una representando una opción de recomendación del banco de acciones, con el eje y etiquetado como porcentaje de veces elegida y el eje x listando los nombres de las opciones.]({% image_buster /assets/img/decisioning_studio/reporting_insights_agent_preferences.png %})

Consulta la siguiente tabla para más detalles sobre este informe:

| Campo | Descripción |
|-------|-------------|
| Dimensión | El atributo utilizado para organizar los resultados, como canal, campaña o plataforma. |
| Grupo de comparación | Los grupos que quieres comparar en tu informe. Puedes seleccionar múltiples grupos de comparación. |
| Parámetro | La métrica aplicada a ese atributo, como aperturas, clics o tasa de conversión. |
| Segmento | El [segmento de audiencia]({{site.baseurl}}/user_guide/engagement_tools/segments/) que creaste en Braze. |
| Opción             | La opción de recomendación específica seleccionada del banco de acciones. |
| Descripción        | Una breve explicación de lo que representa la opción.            |
| N.º de veces elegida  | El recuento total de las veces que se seleccionó la opción.         |
| % de veces elegida   | El porcentaje del total de selecciones en que se eligió esta opción. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab SHAPs %}
El informe de **SHAPs** utiliza el modelo de explicaciones aditivas de Shapley (SHAP) para ayudarte a cuantificar cómo cada característica o variable contribuye a tu agente de recomendación. Cada punto en el gráfico representa un valor SHAP y la distribución de los puntos representa una idea general del impacto direccional de una característica.

![Gráfico del informe SHAPs que muestra un gráfico de barras horizontales con múltiples barras de colores representando diferentes características o variables. Cada barra muestra el impacto de una característica en el agente de recomendación, con el eje x etiquetado como valor SHAP y el eje y listando nombres de características como Recencia, Frecuencia y Canal. El gráfico visualiza cómo cada característica contribuye positiva o negativamente a las predicciones del agente.]({% image_buster /assets/img/decisioning_studio/reporting_insights_shaps.png %})

{% endtab %}
{% endtabs %}