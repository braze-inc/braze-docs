---
nav_title: Predictive Churn
article_title: Predictive Churn
description: "Esta página de destino trata sobre Predictive Churn, una herramienta de Braze Predictive Suite que te permite definir qué significa el abandono de clientes para tu negocio, así como los usuarios que deseas evitar que se vayan."
page_order: 8
alias: /predictive_churn/
search_rank: 2
---

# Predictive Churn

> Con Predictive Churn, una herramienta de Braze Predictive Suite, puedes definir qué significa el abandono para tu negocio e identificar a los usuarios que deseas retener. Cuando creas una predicción, Braze entrena un modelo de aprendizaje automático utilizando [árboles de decisión potenciados por gradientes](https://en.wikipedia.org/wiki/Gradient_boosting) para reconocer a los usuarios en riesgo mediante el análisis de patrones de comportamiento pasado, tanto de los usuarios perdidos como de los que no.

{% alert tip %}
Para obtener más información, consulta [Definición de abandono]({{site.baseurl}}/user_guide/brazeai/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) y [Audiencia de predicción]({{site.baseurl}}/user_guide/brazeai/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience).
{% endalert %}

## Acerca de Predictive Churn

Una vez creado el modelo de predicción, a los usuarios de la audiencia de predicción se les asignará una [puntuación de riesgo de abandono]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/#churn_score) entre 0 y 100 que indicará la probabilidad de que abandonen según tu definición. Cuanto mayor sea la puntuación, más probable es que un usuario abandone. 

La actualización de las puntuaciones de riesgo de la audiencia de predicción puede hacerse con la [frecuencia que elijas]({{site.baseurl}}/user_guide/brazeai/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-prediction). De esta manera, puedes contactar con los usuarios que corren el riesgo de sufrir abandono antes de que lo hagan y evitar que eso suceda. Utilizando hasta tres predicciones activas, puedes aprovechar Predictive Churn para adaptar modelos individuales que te ayuden a evitar el abandono en segmentos específicos de tus usuarios que consideres más valiosos.

![Un resumen del abandono, que incluye una audiencia de predicción pasada con entrenamiento con datos históricos. Esto contribuye a predecir el riesgo de abandono futuro, midiendo la audiencia prevista hoy con una puntuación de riesgo de abandono.]({% image_buster /assets/img/churn/churn_overview.png %})

## Acceso a la predicción de abandono

{% multi_lang_include brazeai/predictions_page_access.md %}

Antes de adquirir esta característica, está disponible en modo vista previa. Esto te permitirá ver una predicción de abandono de demostración con datos sintéticos y crear un modelo de predicción de abandono basado en tus datos de usuario a la vez. Esta vista previa no te permitirá segmentar a los usuarios para la mensajería en función del riesgo de abandono y no se actualizará regularmente tras su creación.

Con la vista previa, también puedes editar y reconstruir tu única predicción o archivarla y crear otras para probar la [calidad de predicción]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) esperada de diferentes [definiciones]({{site.baseurl}}/user_guide/brazeai/predictive_churn/creating_a_churn_prediction/#step-2-define-churn).
