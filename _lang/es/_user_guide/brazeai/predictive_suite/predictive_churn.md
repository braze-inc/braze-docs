---
nav_title: Predictive Churn
article_title: Predictive Churn
page_order: 6.4
layout: dev_guide
alias: /predictive_churn/
search_rank: 2
guide_top_header: "Predictive Churn"
guide_top_text: "El abandono de clientes, también conocido como rotación de clientes o pérdida de clientes, es una de las métricas más importantes que deben tener en cuenta las empresas en crecimiento. Disponer de las herramientas adecuadas para abordar el abandono es crucial para minimizar las pérdidas y maximizar la retención de clientes. Para anticiparse a estos usuarios potencialmente desertores, Braze ofrece Predictive Churn, que proporciona un enfoque proactivo para minimizar futuros abandonos."
description: "Esta página de aterrizaje cubre el Predictive Churn, una herramienta que te permite definir lo que significa el abandono para tu empresa, así como los usuarios que te gustaría evitar que abandonen."

guide_featured_title: "Temas"
guide_featured_list:
- name: Crear una predicción de abandono de clientes
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/
  image: /assets/img/braze_icons/settings-01.svg
- name: Análisis de predicciones
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Usuarios de mensajería
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/
  image: /assets/img/braze_icons/arrow-narrow-right.svg
- name: Solución de problemas
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/prediction_faq/
  image: /assets/img/braze_icons/annotation-question.svg

---

## Resumen

![Un resumen del abandono, que incluye una audiencia de predicción pasada con entrenamiento con datos históricos. Esto contribuye a predecir el riesgo de abandono futuro, midiendo la audiencia prevista hoy con una puntuación de riesgo de abandono.][1]

> Con Predictive Churn, puedes definir lo que significa el abandono para tu empresa[(definición de abandono]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)), y los usuarios que te gustaría evitar que abandonen[(audiencia de predicción]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience)). Cuando creas una predicción, Braze entrena un modelo de aprendizaje automático que utiliza [árboles de decisión potenciados por gradiente](https://en.wikipedia.org/wiki/Gradient_boosting) para identificar a los usuarios con riesgo de abandono, aprendiendo de los patrones de actividad de los usuarios anteriores que abandonaron y no abandonaron según tu definición.

Una vez construido el modelo de predicción, a los usuarios de la audiencia de predicción se les asignará una [puntuación de riesgo de abandono de]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/#churn_score) entre 0 y 100, que denota la probabilidad de abandono según tu definición. Cuanto mayor sea la puntuación, más probable es que un usuario abandone. 

La actualización de las puntuaciones de riesgo de la audiencia de predicción puede hacerse con la [frecuencia que elijas]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions). De este modo, puedes llegar a los usuarios que corren el riesgo de abandonar antes de que lo hagan y evitar que ocurra en primer lugar. Utilizando hasta tres predicciones activas, puedes aprovechar Predictive Churn para adaptar modelos individuales que te ayuden a evitar el abandono en segmentos específicos de tus usuarios que consideres más valiosos.

## Acceso Predictive Churn

La página **Predicciones** se encuentra en la sección **Análisis**. Para obtener acceso completo, ponte en contacto con tu director de cuentas.

Antes de adquirir esta característica, está disponible en modo vista previa. Esto te permitirá ver una predicción de abandono de demostración con datos sintéticos y crear un modelo de predicción de abandono basado en tus datos de usuario a la vez. Esta vista previa no te permitirá segmentar a los usuarios para la mensajería en función del riesgo de abandono y no se actualizará regularmente tras su creación.

Con la vista previa, también puedes editar y reconstruir tu única predicción o archivarla y crear otras para probar la [calidad de predicción]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/) esperada de diferentes [definiciones]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn).

<br><br>

[1]: {% image_buster /assets/img/churn/churn_overview.png %}
