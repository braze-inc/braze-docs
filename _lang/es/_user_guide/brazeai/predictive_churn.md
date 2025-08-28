---
nav_title: Predictive Churn
article_title: Predictive Churn
description: "Esta página de aterrizaje cubre el Predictive Churn, una herramienta que te permite definir lo que significa el abandono para tu empresa, así como los usuarios que te gustaría evitar que abandonen."
page_order: 2.0
alias: /predictive_churn/
search_rank: 2
---

# Predictive Churn

> Con Predictive Churn, puedes definir qué significa el abandono para tu empresa e identificar a los usuarios que quieres retener. Cuando creas una predicción, Braze entrena un modelo de aprendizaje automático que utiliza [árboles de decisión potenciados por gradiente](https://en.wikipedia.org/wiki/Gradient_boosting) para reconocer a los usuarios de riesgo mediante el análisis de patrones de comportamiento anteriores, tanto de los usuarios que abandonaron como de los que no lo hicieron.

{% alert tip %}
Para más información, consulta [Definición de abandono]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) y [Predicción de audiencia]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience).
{% endalert %}

## Acerca del Predictive Churn

Una vez construido el modelo de predicción, a los usuarios de la audiencia de predicción se les asignará una [puntuación de riesgo de abandono de]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/#churn_score) entre 0 y 100, que denota la probabilidad de abandono según tu definición. Cuanto mayor sea la puntuación, más probable es que un usuario abandone. 

La actualización de las puntuaciones de riesgo de la audiencia de predicción puede hacerse con la [frecuencia que elijas]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions). De este modo, puedes llegar a los usuarios que corren el riesgo de abandonar antes de que lo hagan y evitar que ocurra en primer lugar. Utilizando hasta tres predicciones activas, puedes aprovechar Predictive Churn para adaptar modelos individuales que te ayuden a evitar el abandono en segmentos específicos de tus usuarios que consideres más valiosos.

![Un resumen del abandono, que incluye una audiencia de predicción pasada con entrenamiento con datos históricos. Esto contribuye a predecir el riesgo de futuros abandonos midiendo la audiencia prevista hoy con una puntuación de riesgo de abandono.]({% image_buster /assets/img/churn/churn_overview.png %})

## Acceder al Predictive Churn

La página **Predicciones** se encuentra en la sección **Análisis**. Para obtener acceso completo, ponte en contacto con tu director de cuentas.

Antes de adquirir esta característica, está disponible en modo vista previa. Esto te permitirá ver una predicción de abandono de demostración con datos sintéticos y crear un modelo de predicción de abandono basado en tus datos de usuario a la vez. Esta vista previa no te permitirá segmentar a los usuarios para la mensajería en función del riesgo de abandono y no se actualizará regularmente tras su creación.

Con la vista previa, también puedes editar y reconstruir tu única predicción o archivarla y crear otras para probar la [calidad de predicción]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) esperada de diferentes [definiciones]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn).
